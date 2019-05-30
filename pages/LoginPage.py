
class LoginPage:

    _btn_log_in_with_email = "//button[@type='submit']"
    _input_your_email = "#loginform-username"
    _input_your_password = "#loginform-password"

    def get_btn_log_in_with_email(self):
        return self._btn_log_in_with_email

    def get_input_your_email(self):
        return self._input_your_email

    def get_input_your_password(self):
        return self._input_your_password
