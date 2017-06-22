"""
Module for checking if email exists in domain
"""
import re
import socket
import telnetlib

from .mx import get_mx
from .ports import get_open_email_ports
from .support_functions import getdomain
from .mailchecker_exceptions import NoOpenEmailPortsException


def check_if_mail_is_correct(mail, reference_email):
    """
    returns dictionary with particular information of email existence in domain
    :param mail: email address to check
    :param reference_email: reference email address for TELNET commands
    :return: OrderedDict
    """
    mx_list = get_mx(mail)
    main_mx_found = False
    primary_mx = None

    for priority in mx_list:
        for domain in mx_list.get(priority):
            try:
                ports = get_open_email_ports(domain)
            except NoOpenEmailPortsException:
                ports = None
            except RuntimeError:
                ports = None

            if ports:
                primary_mx = domain
                main_mx_found = True
                break

        if main_mx_found:
            break

    if not primary_mx:
        raise NoOpenEmailPortsException('Lack of MX with open port for email: {}'.format(mail))

    reference_email_domain = getdomain(reference_email)

    try:
        telnet_connection_object = telnetlib.Telnet(primary_mx, 25)
        telnet_connection_object.read_until('^220', 35)
        telnet_connection_object.read_until('^\r\n', 5)
    except socket.timeout:
        raise LookupError('Can\'t connect to host {}.'.format(primary_mx))

    try:
        telnet_connection_object.write('HELO '+reference_email_domain+'\r\n')
        telnet_connection_object.read_until('^\r\n', 5)
    except EOFError:
        raise RuntimeError('Can\'t send HELO.')

    try:
        telnet_connection_object.write('mail from:<'+reference_email+'>\r\n')
        telnet_connection_object.read_until('^\r\n', 5)
    except EOFError:
        raise RuntimeError('Can\'t send \'mail from\'.')

    try:
        telnet_connection_object.write('rcpt to:<'+mail+'>\r\n')
        telnet_response = telnet_connection_object.read_until('^\r\n', 10)
        telnet_response = re.sub(r'\r\n', '', telnet_response)
    except EOFError:
        raise RuntimeError('Can\'t send \'rcpt to\'.')

    true_factor_telnet_response = re.compile(r'^250.*')

    email_exists = bool(true_factor_telnet_response.match(telnet_response.lower()))

    response = {
        'email_exists': email_exists,
        'checkout_message': telnet_response,
        'checked_mx': primary_mx
    }

    return response
