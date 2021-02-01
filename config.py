#!/usr/bin/env python
# -*- coding: utf-8 -*-

__modified__ = "Modified by Ali & Ratnesh"
__version__ = "0.1.0"

# This file contains:
# Cisco DNA Center access info


DNAC_IP = ''
DNAC_URL = 'https://' + DNAC_IP
DNAC_USER = ''
DNAC_PASS = ''


PROJECT_J2 = 'NTP_Project_J2'
MANAGEMENT_INT_J2 = 'management_interface.j2'
NTP_SERVER_J2 = 'ntp_server.j2'
DEPLOY_PROJECT = ''
DEPLOY_TEMPLATE = ''

DEVICE_NAME = 'PDX-RN'
DEVICE_TYPES = ['Cisco Catalyst38xx stack-able ethernet switch', 'Cisco Catalyst 9300 Switch']
PARAMS = {'interface_number': '101', 'ip_address': '101.100.100.100'}
