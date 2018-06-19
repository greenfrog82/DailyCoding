function mysolution(array) {
    return (array && 0 < array.length)? array.reduce((total, value) => total + value) / array.length: 0
}

function othersolution(array) {
    return array.reduce((total, value) => total + value, 0) / array.length
}

find_average = othersolution

console.log(find_average([1,1,1]) == 1)
console.log(find_average([1,2,3]) == 2)