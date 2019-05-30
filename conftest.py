from selenium import webdriver
from core.ConfigurationLoader import ConfigurationLoader
from core.LocalizationProvider import LocalizationProvider
from core.SeleniumContainer import ScreenshotMaker, SeleniumFacade
from pages.LoginPage import LoginPage
from pages.FooterCommonPage import FooterCommonPage
from pages.MainPage import MainPage
import pytest
import allure


@pytest.fixture(scope="function")
def authorize(configuration, selenium_facade):
    login_page = LoginPage()
    main_page = MainPage()
    footer_page = FooterCommonPage()
    selenium_facade.click_button_if_visible(main_page.get_lnk_login())
    selenium_facade.element_wait_to_be_visible(login_page.get_input_your_email())
    selenium_facade.set_to_input(login_page.get_input_your_email(), configuration.get_email())
    selenium_facade.set_to_input(login_page.get_input_your_password(), configuration.get_password())
    selenium_facade.click_button(login_page.get_btn_log_in_with_email())
    selenium_facade.move_to_element(footer_page.get_element_block_footer())

@pytest.fixture(scope="session")
def configuration():
    return ConfigurationLoader("configuration.txt")


@pytest.yield_fixture(scope="function")
def driver(configuration):
    driver = webdriver.Chrome()
    driver.fullscreen_window()
    driver.implicitly_wait(10)
    driver.get(configuration.get_url())
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def localization(configuration):
    return LocalizationProvider(configuration.get_locale())


@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def screenshot_maker(driver):
    return ScreenshotMaker(driver)


@pytest.fixture(scope='function', autouse=True)
def screenshot_on_failure(request, screenshot_maker):
    def screenshot():
        if request.node.rep_setup.failed:
            allure.attach(
                name=request.node.name,
                body=screenshot_maker.capture_screenshot(),
                attachment_type=allure.attachment_type.PNG,
            )
        elif request.node.rep_setup.passed:
            if request.node.rep_call.failed:
                allure.attach(
                            name=request.node.name,
                            body=screenshot_maker.capture_screenshot(),
                            attachment_type=allure.attachment_type.PNG,
                        )
    request.addfinalizer(screenshot)


@pytest.fixture(scope="function")
def selenium_facade(driver):
    return SeleniumFacade(driver)
