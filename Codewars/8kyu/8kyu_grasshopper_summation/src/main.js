function mysolution(num) {
    return Array.from({length:num}, (v, k) => k + 1).reduce((total, val) => total + val, 0)
}

function othersolution(num) {
    let result = 0
    for(let i=1; i<=num; i++) {
        result += i
    }
    return result
}

function othersolution2(num) {
    return (num + 1) * num /2
}

const summation = othersolution2

console.log(summation(1) === 1)
console.log(summation(2) === 3)
console.log(summation(8) === 36)
console.log(summation(0) === 0)