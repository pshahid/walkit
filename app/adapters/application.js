import DS from 'ember-data';

export default DS.DjangoTastypieAdapter.extend({
    serverDomain: "http://localhost:4200",
    namespace: "api/v1"
});
