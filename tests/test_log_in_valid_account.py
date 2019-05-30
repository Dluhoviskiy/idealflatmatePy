import allure
from pages.HeaderCommonPage import HeaderCommonPage
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage


@allure.epic("Login")
class TestLogInValidAccount:

    @allure.title("Log in with a valid account")
    @allure.description("The user uses valid credentials and have successful authentication")
    def test_name(self, configuration, selenium_facade, localization):

        with allure.step("Step 1. Click Login link"):
            common_page = HeaderCommonPage()
            login_page = LoginPage()
            main_page = MainPage()
            selenium_facade.click_button_if_visible(main_page.get_lnk_login())

        with allure.step("Step 2. Enter the valid credentials and hit Login button"):
            selenium_facade.element_wait_to_be_visible(login_page.get_input_your_email())
            selenium_facade.set_to_input(login_page.get_input_your_email(), configuration.get_email())
            selenium_facade.set_to_input(login_page.get_input_your_password(), configuration.get_password())
            selenium_facade.click_button(login_page.get_btn_log_in_with_email())

        with allure.step("Expected: Header has been changed to logged in user"):
            assert selenium_facade.get_text(common_page.get_tab_add_listing()) == localization.get_value("header", "tab.add_listing")
            assert selenium_facade.get_text(common_page.get_tab_messages()) == \
                   localization.get_value("header", "tab.messages")
