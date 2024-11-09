import unittest
from screenplay.abilities.read_data import ReadData
from screenplay.tasks.login import Login
from screenplay.tasks.validate import Validate

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = ReadData("login_data.json").load_data()

    def test_login_exitoso(self):
        datos_exito = self.data["login_exitoso"]
        login_task = Login(
            session=datos_exito["session"]["sessionid"],
            email=datos_exito["input"]["email"],
            password=datos_exito["input"]["password"],
            tokenReCaptcha=datos_exito["input"]["tokenReCaptcha"]
        )
        response = login_task.perform_as()
        print(response.status_code)
        print(response.text)
        validation = Validate("success")
        self.assertTrue(validation.perform_as(response))

    def test_login_fallido(self):
        datos_fallo = self.data["login_fallido"]
        login_task = Login(
            session=datos_fallo["session"]["sessionid"],
            email=datos_fallo["input"]["email"],
            password=datos_fallo["input"]["password"],
            tokenReCaptcha=datos_fallo["input"]["tokenReCaptcha"]
        )
        response = login_task.perform_as()
        print(response.status_code)
        print(response.text)
        validation = Validate("failure")
        self.assertTrue(validation.perform_as(response))

if __name__ == "__main__":
    unittest.main()
