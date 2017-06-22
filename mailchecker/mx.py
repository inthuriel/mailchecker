"""
Module for checking email's domain MX records
"""
from collections import OrderedDict
from re import sub

import dns.resolver

from .mailchecker_exceptions import LackOfMxDomainException, DnsTimeoutException
from .support_functions import getdomain


def get_mx(mail):
    """
    returns ordered dict of MX records for email's domain
    :param mail: email adress
    :return: OrderedDict
    """
    domain = getdomain(mail)
    try:
        mx_list = dns.resolver.query(domain, 'MX')
    except dns.exception.DNSException as error:
        if isinstance(error, dns.resolver.NoAnswer):
            raise LackOfMxDomainException('Can\'t get MX from DNS server.')
        elif isinstance(error, dns.resolver.Timeout):
            raise DnsTimeoutException('Timeout on DNS query')
        else:
            raise Exception('Unknown DNS exception.')

    servers = dict()
    ordered_response = OrderedDict()

    for server in mx_list:
        priority, mx_domain = str(server).split(' ')
        mx_domain = sub(r'\.$', '', mx_domain)
        servers.setdefault(int(priority), list()).append(mx_domain)

    for priority in sorted(servers):
        ordered_response.setdefault(priority, servers.get(priority, list()))

    return ordered_response
