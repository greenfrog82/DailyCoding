'use strict'

const assert = require('assert')

function mysolution(num) {
    return 0 > num? num: -num
}

function othersolution(num) {
    return -Math.abs(num)
}

const makeNegative = othersolution

describe('test', () => {
    it('1', () => {
       assert.equal(makeNegative(42), -42) 
    }),
    it('2', () => {
       assert.equal(makeNegative(-5), -5) 
    }),
    it('3', () => {
        assert.equal(makeNegative(0), 0)
    })

})