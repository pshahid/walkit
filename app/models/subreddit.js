import DS from 'ember-data';

export default DS.Model.extend({
    name: DS.attr(),
    public_description: DS.attr(),
    sidebar_description: DS.attr(),
    created_date: DS.attr(),
    subscribers: DS.attr(),
    last_updated_date: DS.attr(),
    subreddit_links: DS.attr()
});
