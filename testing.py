# coding=utf-8
import os
import sys

import traceback
# print("{}".format(sys.path))

# The following doesn't help your plugin find the version of octoprint
# that is embedded in octoprint_test_dummy (see README.md instead).
# include_path = os.path.dirname(os.path.realpath(__file__))
# sys.path.append(include_path)  # This is only necessary for the plugin.

profile = os.environ.get("HOME")
if profile is None:
    profile = os.environ.get("USERPROFILE")
profile = "/home/owner"
if profile is not None:
    site_packages_path = os.path.join(profile, "lcd/lib/python3.7/site-packages")
    if os.path.isdir(site_packages_path):
        if site_packages_path not in sys.path:
            # sys.path.insert(0, site_packages_path)
            sys.path.append(site_packages_path)
    plugin_local_repo_path = os.path.join(profile, "git/OctoPrint-picoLCD-Progress")
    if os.path.isdir(plugin_local_repo_path):
        if plugin_local_repo_path not in sys.path:
            # sys.path.insert(0, plugin_local_repo_path)
            sys.path.append(plugin_local_repo_path)

try:
    from octoprint_picolcdprogress import PicoLCDProgressPlugin
    import octoprint.plugin
    import octoprint.util
    from octoprint.events import Events
except ImportError:
    plugin_package_path = os.path.join(plugin_local_repo_path, "octoprint_picolcdprogress")
    if os.path.isdir(plugin_package_path):
        sys.path.insert(0, plugin_package_path)
    from octoprint_picolcdprogress import PicoLCDProgressPlugin
    import octoprint.plugin
    import octoprint.util
    from octoprint.events import Events

plugin = PicoLCDProgressPlugin()
payload = None
plugin.on_event(Events.PRINT_STARTED, payload)

plugin.on_event(Events.CONNECTED, payload)
defaults = plugin.get_settings_defaults()
print("settings: {}".format(defaults))
