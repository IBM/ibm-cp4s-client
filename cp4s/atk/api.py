# (C) Copyright IBM Corp. 2020.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
import requests
from base64 import b64encode

import logging
logger = logging.getLogger(__name__)


## DEFAULTS

# AITK API version
version = "v1"

# AITK base URL (depends on environment target - defaults to ISC SaaS devite)
base_url = "https://app.ite1.isc.ibmcloudsecurity.com/api"

credentials = "username:password"

debug = False  # DEPRECATED


def set_base_url(url):
    global base_url
    if not (url.endswith('/api') or url.endswith('/api/')):
        logger.warn('Base URL not ending with /api')
    base_url = url.rstrip('/')


## Overrides from environment
if os.environ.get('AITK_BASE'):
    set_base_url(os.environ.get('AITK_BASE'))
elif os.environ.get('SVC_DOMAIN'):
    # This gets set in CP4S/ISC SaaS
    set_base_url(os.environ.get('SVC_DOMAIN'))

if os.environ.get('AITK_CREDS'):
    credentials = os.environ.get('AITK_CREDS')

# Default headers - would a user ever need to change these?
headers = {
    'accept': 'application/json',
    'content-type': 'application/json',
    'authorization': 'Basic ' + b64encode(credentials.encode()).decode()
}


def get_base_url():
    return base_url


def set_conn_info(url=None, creds=None, authstring=None):
    '''Set various connection info for using AITK (and other) APIs'''
    global credentials
    if url:
        set_base_url(url)
    if creds:
        credentials = creds
        headers['authorization'] = 'Basic ' + b64encode(credentials.encode()).decode()
    elif authstring:
        headers['authorization'] = authstring


def api_base():
    return base_url + '/analytics/' + version


# This is really just for debugging
def log_response(resp):
    if resp.ok:
        logger.debug('< {} {}'.format(resp.status_code, resp.reason))
    else:
        try:
            resp_json = resp.json()
        except:
            resp_json = {}
        if 'httpCode' in resp_json:
            # API Connect error response?
            logger.debug('< {} {} ({})'.format(resp_json['httpCode'],
                                               resp_json['httpMessage'],
                                               resp_json['moreInformation']))
        else:
            logger.debug('< {} {}'.format(resp.status_code, resp.reason))


def get(url, **kwargs):
    logger.debug('> GET %s', url)
    res = requests.get(url, **kwargs)
    log_response(res)
    return res


def post(url, **kwargs):
    logger.debug('> POST %s', url)
    res = requests.post(url, **kwargs)
    log_response(res)
    return res


def put(url, **kwargs):
    logger.debug('> PUT %s', url)
    res = requests.put(url, **kwargs)
    log_response(res)
    return res


def delete(url, **kwargs):
    logger.debug('> DELETE %s', url)
    res = requests.delete(url, **kwargs)
    log_response(res)
    return res


class HTTPError(Exception):
    def __init__(self, response):
        Exception.__init__(self, "{}: {}".format(response.status_code, response.text))
        self.response = response


def _get_tasks(path):
    resp = get(api_base() + path, headers=headers)
    if not resp.ok:
        raise HTTPError(resp)
    return resp.json()


def etl(name):
    return _get_tasks('/etl/' + name)


def etls():
    return _get_tasks('/etl')


def analytic(name):
    return _get_tasks('/analytic/' + name)


def analytics():
    return _get_tasks('/analytic')


def workflow(name):
    return _get_tasks('/workflow/' + name)


def workflows():
    return _get_tasks('/workflow')
