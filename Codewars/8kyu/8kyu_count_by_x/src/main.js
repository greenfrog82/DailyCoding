function mysolution(x, n) {
    let ret = []
    for(let i=1; i<=n; i++) {
       ret.push(i * x)
    }
    return ret
}

function othersolution(x, n) {
    return Array.from({length:n}, (v, k) => (k + 1) * x)
}

countBy = othersolution

console.log(countBy(1, 5)) // [1,2,3,4,5]
console.log(countBy(2, 5)) // [2,4,6,8,10]