
class FooterCommonPage:

    _element_block_footer = "//h4[contains(.,'Looking for a')]"
    _tab_about_us = "//body//footer//a[text()='About us']"
    _tab_search_room = "(// a[text() = 'Search rooms'])[2]"

    def get_element_block_footer(self):
        return self._element_block_footer

    def get_tab_about_us(self):
        return self._tab_about_us

    def get_tab_search_room(self):
        return self._tab_search_room



