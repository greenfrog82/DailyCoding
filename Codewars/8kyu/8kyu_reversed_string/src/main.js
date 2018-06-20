const assert = require('assert')

function mysolution(str) {
    return str.split('').reverse().join('')
}

function othersolution(str) {
    return [...str].reverse().join('')
}

const solution = othersolution

describe('test', () => {
    it('1', () => {
        assert.equal(solution('world'), 'dlrow')
    })
})