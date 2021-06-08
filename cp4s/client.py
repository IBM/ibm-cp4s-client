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


import re
import time
import json
import pandas as pd
from cp4s.atk.api import set_conn_info
from cp4s.atk.Job import Job


# High-level interface
class CP4S(object):
    def __init__(self, url, username, password, verbose=False, verify=True):
        self.creds = '%s:%s' % (username, password)
        self.verbose = verbose
        self.verify = verify  # verify cert or not
        set_conn_info(url, self.creds)

    def search_df(self, query: str, configs: str = 'all'):
        if re.match(r'[a-z]+ ', query):  # user has specified a command
            cmd = query
        else:  # defaults to a uds command
            cmd = 'uds query="%s"' % query if configs == 'all' else 'uds query="%s" configs="%s"' % (query, configs)
        job = Job('command-interpreter', {
            '${CREDENTIALS}': {
                'apikey': self.creds
            },
            '${COMMAND}': '%s | table' % cmd,
            '${FILE2REDISINPUT}': "result.json",
            "${UPLOAD}": {"file": "result.json"}
        }, verbose=self.verbose, verify=self.verify)
        while True:
            status = job.status()
            if status == 'Completed':
                result = job.result()
                return pd.DataFrame.from_records(result['rows'])
            if status == 'Failed':
                print('Job [search_df] failed with: %s' % json.dumps(job.taskstatus(), indent=4))
                return None
            time.sleep(1)
