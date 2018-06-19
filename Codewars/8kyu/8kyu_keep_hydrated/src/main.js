function mysolution(time) {
    return Math.floor(time * 0.5)
}

function othersolution(time) {
    return Math.floor(time / 2)
}

const litres = othersolution

console.log(litres(2) === 1)
console.log(litres(1.4) === 0)
console.log(litres(12.3) === 6)
console.log(litres(0.82) === 0)
console.log(litres(11.8) === 5)
console.log(litres(1787) === 893)
console.log(litres(0) === 0)