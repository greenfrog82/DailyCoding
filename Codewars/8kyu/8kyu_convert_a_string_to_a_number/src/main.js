function mysolution(str) {
    return Number(str)
}

function othersolution(str) {
    return +str    
}

stringToNumber = othersolution

console.log(stringToNumber('1234') == 1234)
console.log(stringToNumber('605') == 605)
console.log(stringToNumber('1405') == 1405)
console.log(stringToNumber('-7') == -7)


console.log(+'123.23123')