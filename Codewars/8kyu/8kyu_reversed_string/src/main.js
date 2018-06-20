const assert = require('assert')

function mysolution(str) {
    return str.split('').reverse().join('')
}

const solution = mysolution

describe('test', () => {
    it('1', () => {
        assert.equal(solution('world'), 'dlrow')
    })
})