import json
import sys


class ConfigurationLoader:
    def __init__(self, filename):
        try:
            f = open(filename)
            json_data = f.read()
            self.config = json.loads(json_data)
            print("Configuration loaded from " + filename)
        except IOError as ex:
            print("Error in loading configuration", ex)
            sys.exit()

    def get_browser_name(self):
        return self.config.get("browser_name")

    def get_command_executor(self):
        return self.config.get("command_executor")

    def get_configuration_name(self):
        return self.config.get("configuration_name")

    def get_email(self):
        return self.config.get("email")

    def get_javascript_enabled(self):
        return self.config.get("javascript_enabled")

    def get_locale(self):
        return self.config.get("locale")

    def get_password(self):
        return self.config.get("password")

    def get_url(self):
        return self.config.get("url")

    def get_version(self):
        return self.config.get("version")
