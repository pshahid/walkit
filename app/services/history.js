import Ember from 'ember';

export default Ember.Service.extend({
    stack: [],
    init() {
        this._super(...arguments);
    },
    all() {
        return this.get('stack');
    },
    put(obj) {
        var stack = this.get('stack');
        stack.push(obj);
        this.set('stack', stack);
    },
    back(number) {
        const stack = this.get('stack');
        return stack[stack.length-number];
    },
    lastOne() {
        return this.back(1);
    }
});
