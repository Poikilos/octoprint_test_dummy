# octoprint_test_dummy
If you are adventurous, you may use this to test octoprint plugins.


## Usage
- Add the following to your plugin:
```
import sys
octoprint_test_dummy_path = ...  # add the current path here
sys.path.insert(0, "")
```

- Change the following in testing.py or make your own py that is similar with the following variables set to your plugin:
```
site_packages_path
plugin_local_repo_path
plugin_package_path
```

## Contribute (Solve Bugs)
- If you get an error such as missing type:
```
TemplatePlugin
```
Then all you have to do is add some kind of blank template:
```
class TemplatePlugin:
    pass
```
If it then gets an error about missing properties (TemplatePlugin missing properties/methods in the example above), just add them in there and submit a pull request.

## Compare
### Live Debugging
The octoprint_test_dummy is only good for checking syntax. The real way to debug is more comprehensive and means you do "live debugging" with OctoPrint itself (without octoprint_test_dummy).
For live debugging you can do something like:
- `python setup.py develop`
  - The `develop` option causes OctoPrint to use the plugin directory in
    place, so that you don't have to reinstall the plugin each time you
    change it.
- Start OctoPrint and try using the plugin or changing its settings.
  - `su - -c 'systemctl restart octoprint'`
- `tail ~/.octoprint/logs/octoprint.log`
