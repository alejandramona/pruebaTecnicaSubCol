import requests

class Validate:
    def __init__(self, expected_status):
        self.expected_status = expected_status

    def perform_as(self, response):
        try:
            result = response.json().get("status")
            return result == self.expected_status
        except requests.exceptions.JSONDecodeError:
            return False
