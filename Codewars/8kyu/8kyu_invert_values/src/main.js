function mysolution(array) {
    return array.map(x => 0 == x? 0: -x)
}

function othersolution(array) {
    return array.map(i => 0 - i)
}

const invert = othersolution

console.log(invert([1, 2, 3, 4, 5])) // [-1, -2, -3, -4, -5]
console.log(invert([1, -2, 3, -4, 5])) // [-1, 2, -3, 4, -5])
console.log(invert([])) // []
console.log(invert([0])) // [0])