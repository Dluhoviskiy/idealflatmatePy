import json
import sys


class LocalizationProvider:
    def __init__(self, locale="EN"):
        try:
            f = open("localization//title_resource_" + locale + ".txt", encoding="utf8")
            json_data = f.read()
            self.data = json.loads(json_data)
            print("Localization loaded for locale: " + locale)
        except IOError:
            print("Error in loading localization with locale: " + locale)
            sys.exit()

    def get_value(self, parent, key):
        return self.data.get(parent).get(key)
