let assert = require('assert');

function mysolution(array) { 
    return array.filter((element, index) => 0 === element % index)
}

const multipleOfIndex = mysolution

describe('test', () => {
    it('1', () => {
        assert.deepEqual(multipleOfIndex([22, -6, 32, 82, 9, 25]), [-6, 32, 25])
    })
    it('2', () => {
        assert.deepEqual(multipleOfIndex([68, -1, 1, -7, 10, 10]), [-1, 10])
    }),
    it('3', () => {
        assert.deepEqual(multipleOfIndex([11, -11]), [-11])
    }),
    it('4', () => {
        assert.deepEqual(multipleOfIndex([-56, -85, 72, -26, -14, 76, -27, 72, 35, -21, -67, 87, 0, 21, 59, 27, -92, 68]), [-85, 72, 0, 68])
    }),
    it('5', () => {
        assert.deepEqual(multipleOfIndex([28, 38, -44, -99, -13, -54, 77, -51]), [38, -44, -99])
    }),
    it('6', () => {
        assert.deepEqual(multipleOfIndex([-1, -49, -1, 67, 8, -60, 39, 35]), [-49, 8, -60, 35])
    })
})