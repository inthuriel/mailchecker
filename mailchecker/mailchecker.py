"""
Module for checking informations about email including MX, open SMTP ports,
email existence in domain
"""
from collections import OrderedDict

from .mx import get_mx
from .ports import get_open_email_ports
from .support_functions import getdomain
from .telnetcheck import check_if_mail_is_correct


def full_email_check(mail, reference_mail):
    """
    returns dictionary with wide information about given email address
    :param mail: email address to check
    :param reference_mail: reference email address for TELNET commands
    :return: OrderedDict
    """
    email_correctness_data = check_if_mail_is_correct(mail, reference_mail)

    email_correctness_response = OrderedDict()
    email_correctness_response.setdefault('email_address', mail)
    email_correctness_response.setdefault('email_domain', getdomain(mail))
    email_correctness_response.setdefault('email_mx_list', get_mx(mail))
    email_correctness_response.setdefault('email_available_ports', get_open_email_ports(
        email_correctness_data.get('checked_mx')))
    email_correctness_response.setdefault('email_exists',
                                          email_correctness_data.get('email_exists'))

    return email_correctness_response
