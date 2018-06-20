const assert = require('assert')

function mysolution(n) {
    return Array.from({length:n}, (v, k) => k+1).reverse()
}

function othersolution(n) {
    return Array(n).fill(0).map((element, index) => n - index)
}

function othersolution2(length) {
    return Array.from({length}, () => length--)
}

const reverseSeq = othersolution2

describe("reverseSeq", function() {
    it("Sample Test", function() {
        assert.deepEqual(reverseSeq(5), [5, 4, 3, 2, 1]);
    });
});