"""
Module for checking informations about email including MX, open SMTP ports,
email existence in domain
"""
from .mailchecker import full_email_check
from .mx import get_mx
from .ports import get_open_email_ports
from .telnetcheck import check_if_mail_is_correct

__all__ = ['full_email_check', 'get_mx', 'get_open_email_ports', 'check_if_mail_is_correct']
