const assert = require('assert')

function mysolution(number) {
   return -number 
}

const opposite = mysolution

describe('test', () => {
    it('1', () => {
        assert.equal(opposite(1), -1)        
    })
})