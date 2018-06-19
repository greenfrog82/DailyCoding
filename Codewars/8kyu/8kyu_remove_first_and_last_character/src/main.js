const assert = require('assert')

function mysolution(str) {
    return str.slice(1, str.length - 1)
}

function othersolution(str) {
    return str.slice(1, -1)
}

const removeChar = othersolution

describe('test', () => {
    it('1', () => {
        assert.equal(removeChar('eloquent'), 'loquen')
    }),
    it('2', () => {
        assert.equal(removeChar('country'), 'ountr')
    }),
    it('3', () => {
        assert.equal(removeChar('person'), 'erso')
    }),
    it('4', () => {
        assert.equal(removeChar('place'), 'lac')
    })
})