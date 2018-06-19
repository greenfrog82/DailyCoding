function mysolution(n) {
    return n.toString().split('').reverse().map(num => +num)
}

function othersolution(n) {
    return Array.from(String(n), Number).reverse()
}

function othersolution2(n) {
    return String(n).split('').map(Number).reverse()
}

digitize = othersolution2

console.log(digitize(35231)) // [1,3,2,5,3]