function mysolution(str) {
    return str.split('').map(ch => ch + ch).join('')
}

function othersolution(str) {
    return str.replace(/(.)/g, '$1$1')
}

doubleChar = othersolution

console.log(doubleChar("abcd") === "aabbccdd");
console.log(doubleChar("Adidas") === "AAddiiddaass");
console.log(doubleChar("1337") === "11333377");
console.log(doubleChar("illuminati") === "iilllluummiinnaattii");
console.log(doubleChar("123456") === "112233445566");
console.log(doubleChar("%^&*(") === "%%^^&&**((");