#!/usr/local/bin/python

from jira import JIRA
import keyring
import getpass
import sys

# Config
# Initialize config before other scripts
import dashboard_config
dashboard_config.init(False)

# Main
from jira_dashboard_common import *

TICKETS_BY_COMMA = sys.argv[1]
STATUSES = sys.argv[2]
RESULTS = get_ticket_list_in_status(TICKETS_BY_COMMA, STATUSES)

LIST_CONCAT_BY_SEMICOLON = ','.join(map(lambda x: x.key, RESULTS))
print LIST_CONCAT_BY_SEMICOLON

# python ./working_dashboard/jira_dashboard_tickets_by_status.py MOX-3400,MOX-3419 Closed
