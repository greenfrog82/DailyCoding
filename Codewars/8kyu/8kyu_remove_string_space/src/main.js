const assert = require('assert')

function mysolution(x) {
    return x.replace(/\s+/g, '')
}

function othersolution(x) {
    return x.replace(/\s/g, '')
}

function othersolution2(x) {
    return x.replace(/ /g, '')
}

function othersolution3(x) {
    return x.split(' ').join('')
}

const noSpace = othersolution3

describe('test', () => {
    it('1', () => {
        assert.equal(noSpace('8 j 8   mBliB8g  imjB8B8  jl  B'), '8j8mBliB8gimjB8B8jlB');
    }),
    it('2', () => {
        assert.equal(noSpace('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'), '88Bifk8hB8BB8BBBB888chl8BhBfd');
    }),
    it('3', () => {
        assert.equal(noSpace('8aaaaa dddd r     '), '8aaaaaddddr');  
    })
})