# coding=utf-8
# This is a dummy file for testing OctoPrint plugins.
class RepeatedTimer:
    def __init__(self, timeout, callback):
        self.callback = callback

    def start(self):
        print("* callback...")
        self.callback()
