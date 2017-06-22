"""
Module provides custom exceptions
"""


class LackOfMxDomainException(Exception):
    """
    Exception raised when none MX records for domain can be found
    """
    pass


class DnsTimeoutException(Exception):
    """
    Exception raised when DNS timed out
    """
    pass


class NoOpenEmailPortsException(Exception):
    """
    Exception raised when none open ports can be found on given server
    """
    pass
