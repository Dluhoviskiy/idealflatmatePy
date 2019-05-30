
class HeaderCommonPage:


    _tab_add_listing = "//a[text()='Add a Listing']"
    _tab_find_home = "//a[text()='Find a home']"
    _tab_messages = "//a[text()='Messages']"

    def get_tab_add_listing(self):
        return self._tab_add_listing

    def get_tab_find_home(self):
        return self._tab_find_home

    def get_tab_messages(self):
        return self._tab_messages
