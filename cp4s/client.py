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


import time
import pandas as pd
from cp4s.aitk.api import set_conn_info
from cp4s.aitk.Job import Job


# High-level interface
class Atk(object):
    def __init__(self, url, username, password):
        set_conn_info(url, '%s:%s' % (username, password))

    def search_df(self, query: str, configs: str = 'all'):
        uds = 'uds query="%s"' % query if configs == 'all' else 'uds query="%s" configs="%s"' % (query, configs)
        job = Job('command-interpreter', {
            '${COMMAND}': '%s | table' % uds,
            '${FILE2REDISINPUT}': "result.json"
        })
        while True:
            status = job.status()
            if status == 'Completed':
                result = job.result()
                return pd.DataFrame.from_records(result['rows'])
            if status == 'Failed':
                return None
            time.sleep(1)
