# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class ExercisePlugin(octoprint.plugin.SettingsPlugin,
                      octoprint.plugin.AssetPlugin,
                      octoprint.plugin.TemplatePlugin):

    ##~~ SettingsPlugin mixin

    def get_settings_defaults(self):
        return dict(
            commands="",
            repetitions=25,
        )

    ##~~ AssetPlugin mixin

    def get_assets(self):
        # Define your plugin's asset files to automatically include in the
        # core UI here.
        return dict(
            js=["js/exercise.js"],
            css=["css/exercise.css"],
            less=["less/exercise.less"]
        )

    ##~~ Softwareupdate hook

    def get_update_information(self):
        # Define the configuration for your plugin to use with the Software Update
        # Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
        # for details.
        return dict(
            exercise=dict(
                displayName="Exercise Plugin",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="FanDjango",
                repo="OctoPrint-Exercise",
                current=self._plugin_version,

                # update method: pip
                pip="https://github.com/FanDjango/OctoPrint-Exercise/archive/{target_version}.zip"
            )
        )

    def get_template_configs(self):
        return [
            dict(type="sidebar", name="Exerciser", icon="sort-by-attributes-alt"),
            dict(type="settings", custom_bindings=False)
        ]


__plugin_name__ = "Exercise Plugin"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = ExercisePlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }

