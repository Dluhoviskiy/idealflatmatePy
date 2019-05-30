from pages.HeaderCommonPage import HeaderCommonPage


class MainPage(HeaderCommonPage):

    _lnk_login = "//a[text()=' Login']"

    def get_lnk_login(self):
        return self._lnk_login
