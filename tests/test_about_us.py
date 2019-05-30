import allure
from pages.AboutUsPage import AboutUsPage
from pages.HeaderCommonPage import HeaderCommonPage
from pages.FooterCommonPage import FooterCommonPage
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage


@allure.epic("About Us")
class TestLogInValidAccount:

    @allure.title("About Us page contains right elements")
    @allure.description("There are correct elements on About us page")
    def test_name(self, selenium_facade, localization, configuration):

        with allure.step("Step 1. Click Login link"):
            #footer_page = FooterCommonPage()

            main_page = MainPage()
            selenium_facade.click_button_if_visible(main_page.get_lnk_login())

        with allure.step("Step 2. Enter the valid credentials and hit Login button"):
            login_page = LoginPage()
            selenium_facade.element_wait_to_be_visible(login_page.get_input_your_email())
            selenium_facade.set_to_input(login_page.get_input_your_email(), configuration.get_email())
            selenium_facade.set_to_input(login_page.get_input_your_password(), configuration.get_password())
            selenium_facade.click_button(login_page.get_btn_log_in_with_email())

        with allure.step("Step 3. Click 'About us' link"):

            footer_page = FooterCommonPage()
            about_us_page = AboutUsPage()

            #selenium_facade.move_to_element(footer_page._tab_search_room)
            selenium_facade.move_to_element(footer_page.get_element_block_footer())
            #selenium_facade.explicit_wait(5)
            #selenium_facade.click_button_if_visible(footer_page.get_element_block_footer())
            selenium_facade.click_button_if_visible(footer_page._tab_about_us)
            #selenium_facade.element_wait_to_be_clickable(footer_page._tab_about_us)


        with allure.step("Expected: There are elements on the page"):
            assert selenium_facade.get_text(about_us_page.get_hdr_ideal_matches()) == \
                   localization.get_value("about_us_page", "hdr_ideal_matches")
