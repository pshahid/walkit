import Ember from 'ember';
import Resolver from './resolver';
import loadInitializers from 'ember-load-initializers';
import config from './config/environment';

let App;

Ember.MODEL_FACTORY_INJECTIONS = true;

App = Ember.Application.extend({
  modulePrefix: config.modulePrefix,
  podModulePrefix: config.podModulePrefix,
  Resolver
});

Ember.onerror = function(error) {
    console.log("Ember error");
    console.log(error);
    console.log(error.stack);
    Ember.assert(false, error);
}
Ember.RSVP.on('error', function(error) {
  console.log(error.message);
  console.log(error.stack);
  Ember.assert(false, error);
});

Ember.RSVP.configure('onerror', function(e) {
  console.log(e.message);
  console.log(e.stack);
  Ember.assert(false, e);
});

loadInitializers(App, config.modulePrefix);

export default App;
