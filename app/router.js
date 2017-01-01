import Ember from 'ember';
import config from './config/environment';

const Router = Ember.Router.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('about');
  this.route('options');
  this.route('random-walk');
  this.route('search-subreddits');
  this.route('discover-subreddits');
  this.route('random');
});

export default Router;
