from pages.HeaderCommonPage import HeaderCommonPage


class AboutUsPage(HeaderCommonPage):

    _hdr_ideal_matches = "//h2[text()='Ideal matches']"

    def get_hdr_ideal_matches(self):
        return self._hdr_ideal_matches
