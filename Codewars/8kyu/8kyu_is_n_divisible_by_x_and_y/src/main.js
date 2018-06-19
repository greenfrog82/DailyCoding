function mysolution(n, x, y) {
    return !(n % x) && !(n % y)
}

function othersolution(n, x, y) {
    return !(n%x||n%y)
}

isDivisible = othersolution

console.log(isDivisible(3, 3, 4) === false);
console.log(isDivisible(12, 3, 4) === true);
console.log(isDivisible(8, 3, 4) === false);
console.log(isDivisible(48, 3, 4) === true);