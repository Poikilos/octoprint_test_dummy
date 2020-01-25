# octoprint_test_dummy
If you are adventurous, you may use this to test octoprint plugins.

## Compare
For live debugging (without octoprint_test_dummy) you can do:
- `python setup.py develop`
  - The `develop` option causes OctoPrint to use the plugin directory in
    place, so that you don't have to reinstall the plugin each time you
    change it.
- Start OctoPrint and try using the plugin or changing its settings.
  - `su - -c 'systemctl restart octoprint'`
- `tail ~/.octoprint/logs/octoprint.log`
