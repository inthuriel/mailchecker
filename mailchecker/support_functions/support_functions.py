"""
Module provides support functions for library
"""


def getdomain(mail):
    """
    gets domain from email
    :param mail: email address to split
    :return: String
    """
    domain = mail.split('@')[1]

    return domain
