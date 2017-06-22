"""
Module for checking open ports on server
As default uses list of 'email' ports
"""
import socket

from .mailchecker_exceptions import NoOpenEmailPortsException


def get_open_email_ports(server, ports=(25, 465, 143, 993)):
    """
    returns list of open ports
    :param server: FQDN to check
    :param ports: list of ports to check
    :return: List
    """
    try:
        server_ip = socket.gethostbyname(server)
    except socket.gaierror:
        raise Exception('Can\'t resolve host {}.'.format(server))

    open_ports = list()

    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((server_ip, port))
            if result == 0:
                open_ports.append(str(port))
            sock.close()

        if not open_ports:
            raise NoOpenEmailPortsException('No open email ports on server {}.'.format(server))
    except socket.error:
        raise RuntimeError('Can\'t connect to server {} [{}].'.format(server, server_ip))

    return open_ports
