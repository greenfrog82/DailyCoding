function mysolution(args) {
    return Math.min(...args)
}

function othersolution(args) {
    return Math.min.apply(null, args)
}

const findSmallestInt = othersolution

console.log(findSmallestInt([78,56,232,12,8]) === 8);
console.log(findSmallestInt([78,56,232,12,18]) === 12);
console.log(findSmallestInt([78,56,232,412,228]) === 56);
console.log(findSmallestInt([78,56,232,12,0]) === 0);
console.log(findSmallestInt([1,56,232,12,8]) === 1);