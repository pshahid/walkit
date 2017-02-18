import Ember from 'ember';

export default Ember.Service.extend({
    random: Ember.inject.service(),
    stack: [],
    stackPointer: 0,
    init() {
        this._super(...arguments);
    },
    all() {
        return this.get('stack');
    },
    next(cb) {
        const random = this.get('random');
        const self = this;
        const stack = this.get('stack');
        var stackPointer = this.get('stackPointer');

        if (stackPointer < stack.length-1) {
            stackPointer += 1;
            this.set('stackPointer', stackPointer);
            cb(stack[stackPointer]);
        } else {
            random.random(function(subreddit) {
                self.put(subreddit);
                cb(subreddit);
            });
        }
    },
    put(obj) {
        var stack = this.get('stack');
        stack.push(obj);
        this.set('stack', stack);
        var stackPointer = stack.length-1;
        this.set('stackPointer', stackPointer);
    },
    back() {
        var stackPointer = this.get('stackPointer');
        const stack = this.get('stack');
        if (stackPointer > 0) {
            stackPointer -= 1;
            this.set('stackPointer', stackPointer);
        }
        return stack[stackPointer];
    }
});
