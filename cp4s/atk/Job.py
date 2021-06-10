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


import json

from .api import api_base
from .api import get
from .api import post
from .api import delete
from .api import headers
from .api import HTTPError


# High-level interface
class Job(object):
    def __init__(self, name, params, preserve=False, schedule=None, verbose=False, verify=True):
        self.id = None
        self._status = 'Started'
        self._preserve = preserve
        self.verify = verify
        data = {'param': params}
        if schedule:
            data['schedule'] = schedule
        if verbose:
            print(json.dumps(data, indent=2))
        resp = post(api_base() + '/workflow/' + name, headers=headers, json=data, verify=self.verify)
        if not resp.ok:
            raise HTTPError(resp)
        msg = resp.json()
        self.id = msg['jobid']

    def status(self):
        # TODO: cache job status?
        resp = get(api_base() + '/job/{}/status'.format(self.id), headers=headers, verify=self.verify)
        if not resp.ok:
            raise HTTPError(resp)
        msg = resp.json()
        self._status = msg['status']
        self._taskstatus = msg['taskstatus']
        return self._status

    def taskstatus(self):
        return self._taskstatus

    def result(self, verbose=False):
        done = False
        page = 0
        data = ''
        while not done:
            try:
                item = f'/job/{self.id}/result?page={page}'
                resp = get(api_base() + item, headers=headers, verify=self.verify)
                if verbose:
                    print(f'Getting: {item} -> {resp.status_code}')
                else:
                    print(f'Receiving page: {page}')
                if resp.ok:
                    result = resp.json()
                    if 'error' in result:
                        print(result["error"])
                    elif 'page' in result:
                        if 'data' in result:
                            data += result['data']
                            if verbose:
                                print(f'Saved: {len(data)}')
                        if 'next' in result:
                            page = result['next']
                            if page == -1:
                                done = True
                    elif 'rows' in result:
                        return result
                elif resp.status_code != 503:
                    print(resp.text)
                    return {}
            except Exception as e:
                print(e)
        return json.loads(data)

    def service(self, req):
        resp = get(api_base() + '/job/{}/service/{}'.format(self.id, req), headers=headers, verify=self.verify)
        if not resp.ok:
            raise HTTPError(resp)
        return resp.json()

    def __del__(self):
        if not self._preserve and self.id:
            resp = delete(api_base() + '/job/' + self.id, headers=headers, verify=self.verify)
            if not resp.ok:
                raise HTTPError(resp)
