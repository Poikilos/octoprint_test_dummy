# coding=utf-8
# This is a dummy file for testing OctoPrint plugins.
import logging


class Printer:
    def __init__(self):
        self._is_printing = True
    def is_printing(self):
        return self._is_printing
    def get_current_data(self):
        return {
            "status": "OK"
        }


class EventHandlerPlugin:
    def __init__(self):
        self._logger = logging.getLogger("octoprint_test_dummy")

class Settings:
    def get(self, parts):
        result = "pgs"
        return result

    def get_int(self, name):
        return 1

class SettingsPlugin:
    _settings = Settings()
    _printer = Printer()
    def __init__(self):
        pass
        # self._printer = Printer()
        # self._settings = Settings()

