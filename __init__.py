import re
import logging
import json
import requests

class Facebook:
    def get_access_token(self, app_id='559774744201766'):
            '''Register an access token in graph api console.'''
            # get response of registering access token
            res = self.session.get(ACCESS_TOKEN_URL.format(app_id, self.user_id))
            # remove for (;;); so we can load content in json format
            content = json.loads(re.sub('for \(;;\);', '', res.text))

            # try to get access token inside a complex structure
            try:
                token = content['jsmods']['instances'][2][2][2]
            except KeyError:
                token = ''

            return token
