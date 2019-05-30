import allure
from pages.AboutUsPage import AboutUsPage
from pages.HeaderCommonPage import HeaderCommonPage
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage


@allure.epic("About Us")
class TestLogInSearch:

    @allure.title("Search after login")
    @allure.description("Search after login")
    def test_name(self, selenium_facade, localization, configuration, authorize):

        with allure.step("Step 1. Click 'Search' link"):
            common_page = HeaderCommonPage()
            selenium_facade.click_button_if_visible(common_page.get_tab_find_home())

        # with allure.step("Expected: There are elements on the page"):
        #     assert selenium_facade.get_text(about_us_page.get_hdr_ideal_matches()) == \
        #            localization.get_value("about_us_page", "hdr_ideal_matches")
