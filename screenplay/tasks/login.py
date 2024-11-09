import requests

class Login:
    def __init__(self, session, email, password, tokenReCaptcha):
        self.session = session
        self.email = email
        self.password = password
        self.tokenReCaptcha = tokenReCaptcha

    def perform_as(self):
        payload = {
            "session": {"sessionid": self.session},
            "input": {
                "email": self.email,
                "password": self.password,
                "tokenReCaptcha": self.tokenReCaptcha
            }
        }
        response = requests.post(
            "https://castlemockdemo.subocol.com/castlemock/mock/rest/project/NpJ1A9/application/eu72DD/login",
            json=payload
        )
        return response
