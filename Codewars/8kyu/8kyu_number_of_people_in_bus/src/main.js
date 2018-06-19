const assert = require('assert')

function mysolution(busStop) {
    return busStop.map(x => x[0] - x[1]).reduce((accumulator, currentValue) => accumulator + currentValue)
}

function othersolution(busStop) {
    return busStop.reduce((rem, [on,off]) => rem + (on - off), 0)
}

const number = othersolution

describe('test', () => {
    it('1', () => {
        assert.equal(number([[10, 0], [3, 5], [5, 8]]), 5)
    }),
    it('2', () => {
        assert.equal(number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]), 17);
    }),
    it('3', () => {
        assert.equal(number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]), 21);
    })
})