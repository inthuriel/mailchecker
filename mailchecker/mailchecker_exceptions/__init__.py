"""
Module provides custom exceptions
"""
from .mailchecker_exceptions import LackOfMxDomainException, DnsTimeoutException, \
    NoOpenEmailPortsException

__all__ = ['LackOfMxDomainException', 'DnsTimeoutException', 'NoOpenEmailPortsException']
