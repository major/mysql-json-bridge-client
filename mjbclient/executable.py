#!/usr/bin/env python
#
# Copyright 2012 Major Hayden
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import sys


from prettytable import PrettyTable
import requests


__version__ = '0.0.1'


def run_query(bridge_url, sql):
    payload = {'sql': sql}
    r = requests.post(bridge_url, data=payload)
    return r.json


def print_usage():
    print """
Pass a URL and a query like this:
mjbclient http://example.com/query/dbname "SELECT VERSION()"
"""


def run_mjbclient():
    if len(sys.argv) != 3:
        print_usage()

    results = run_query(sys.argv[1], sys.argv[2])

    if 'ERROR' in results.keys():
        sys.exit("[ERROR] %s" % results['ERROR'])

    result = results['result']
    columns = result[0].keys()
    pt = PrettyTable(result[0].keys())
    for column in columns:
        if type(result[0][column]) in [int, float]:
            pt.align[column] = 'r'
        else:
            pt.align[column] = 'l'
    for row in result:
        pt.add_row(row.values())
    print pt
