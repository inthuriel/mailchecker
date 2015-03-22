# -*- coding: utf-8 -*-
import socket

def getcontypes(server):
    serverip  = socket.gethostbyname(server)
    openports = []

    try:
        for port in [25,465,143,993]:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((serverip, port))
            if result == 0:
                openports.append(format(port))
            sock.close()

        if(len(openports) == 0):
            raise Exception("noPorts", "No open ports.")

    except socket.gaierror:
        raise Exception("resolvErr", "Can't resolve host.")

    except socket.error:
        raise Exception("connectErr", "Couldn't connect to server.")

    return openports
