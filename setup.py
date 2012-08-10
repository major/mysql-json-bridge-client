#!/usr/bin/python
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
#
from setuptools import setup
from mjbclient import executable


setup(
    name='mjbclient',
    version=executable.__version__,
    author='Major Hayden',
    author_email='major@mhtx.net',
    description="client for the mysql-json-bridge",
    install_requires=['requests', 'prettytable'],
    packages=['mjbclient'],
    url='https://github.com/rackerhacker/mysql-json-bridge-client',
    entry_points={
        'console_scripts': [
            'mjbclient = mjbclient.executable:run_mjbclient']
        }
    )
