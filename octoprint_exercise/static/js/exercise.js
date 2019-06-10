/*
 * View model for OctoPrint-Exercise
 *
 * Author: Michael Stiemke
 * License: AGPLv3
 */
$(function() {
  function ExerciseViewModel(parameters) {
    var self = this;

    self.settings = parameters[0];
    self.loginState = parameters[1];

    self.commands = ko.observable(undefined);
    self.repetitions = ko.observable("25");
    self.isOperational = ko.observable(undefined);
    self.isPrinting = ko.observable(undefined);

    self.goPrint = function() {
      var irep;
      for (irep = 0;  irep < self.repetitions(); irep++) {
        code = self.commands();
        OctoPrint.control.sendGcode(code);
      }
    }

    self.onBeforeBinding = function() {
      self.commands(self.settings.settings.plugins.exercise.commands());
      self.repetitions(self.settings.settings.plugins.exercise.repetitions());
    }

    self.fromCurrentData = function(data) {
      self._processStateData(data.state);
    };

    self.fromHistoryData = function(data) {
      self._processStateData(data.state);
    };

    self._processStateData = function(data) {
      self.isOperational(data.flags.operational);
      self.isPrinting(data.flags.printing);
    };

    self.movementEnabled = function() {
      return (self.isOperational() && self.loginState.isUser() && ! self.isPrinting());
    }
  }

  // view model class, parameters for constructor, container to bind to
  OCTOPRINT_VIEWMODELS.push([
    ExerciseViewModel,
    [ "settingsViewModel", "loginStateViewModel" ],
    [ "#sidebar_plugin_exercise" ]
  ]);
});
