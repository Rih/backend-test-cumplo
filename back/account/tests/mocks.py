
RECAPTCHA_RESPONSE = {
    'fail': {
        'success': False,
        'error-codes': ['invalid-input-response'],
    },
    'less_score': {
        'success': False,
        'challenge_ts': '2021-07-21T17:19:23Z',
        'hostname': 'localhost',
        'score': 0.1,
    },
    'success': {
        'success': True,
        'challenge_ts': '2021-07-21T17:19:23Z',
        'hostname': 'localhost',
        'score': 0.9,
        'client_token': 'loong_tkn_value_mocked'
    }

}


class RequestMock:

    def __init__(self, **kwargs):
        self.mode = kwargs.get('mode', 'success')
        self.status = kwargs.get('status', 200)
        self.response = kwargs.get('response', {'success': {}})

    @property
    def status_code(self):
        return self.status

    def json(self):
        return self.response[self.mode]
