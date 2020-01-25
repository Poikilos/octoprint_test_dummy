# coding=utf-8
import os
import sys

import traceback
# print("{}".format(sys.path))

profile = os.environ.get("HOME")
if profile is None:
    profile = os.environ.get("USERPROFILE")
profile = "/home/owner"
if profile is not None:
    test_path = os.path.join(profile, "lcd/lib/python3.7/site-packages")
    if os.path.isdir(test_path):
        if test_path not in sys.path:
            # sys.path.insert(0, test_path)
            sys.path.append(test_path)
    test_path = os.path.join(profile, "git/OctoPrint-picoLCD-Progress")
    if os.path.isdir(test_path):
        if test_path not in sys.path:
            # sys.path.insert(0, test_path)
            sys.path.append(test_path)

try:
    from octoprint_picolcdprogress import PicoLCDProgressPlugin
    import octoprint.plugin
    import octoprint.util
    from octoprint.events import Events
except ImportError:
    test_path = os.path.join(profile, "git/OctoPrint-picoLCD-Progress/octoprint_picolcdprogress")
    if os.path.isdir(test_path):
        sys.path.insert(0, test_path)
    from octoprint_picolcdprogress import PicoLCDProgressPlugin
    import octoprint.plugin
    import octoprint.util
    from octoprint.events import Events


# test_path = "/home/owner/lcd/lib/python3.7/site-packages"
# if os.path.isdir(test_path):
#     sys.path.insert(0, test_path)
# from pypicolcd import lcdclient

plugin = PicoLCDProgressPlugin()
payload = None
plugin.on_event(Events.PRINT_STARTED, payload)

plugin.on_event(Events.CONNECTED, payload)
