function mysolution() {
    let origin = this.valueOf();
    let ret = '';

    for(let i=0; i<origin.length; i++) {
        let tmp = origin[i];
        ret += (tmp === tmp.toUpperCase())? tmp.toLowerCase(): tmp.toUpperCase();
    }
    return ret;
}

function othersolution() {
    return this.split('').map(a => a === a.toUpperCase()? a.toLowerCase(): a.toUpperCase()).join('')
}

function othersolution2() {
    return [...this].map(ch => ch === ch.toUpperCase()? ch.toLowerCase(): ch.toUpperCase()).join('');
}

String.prototype.toAlternatingCase = othersolution2

console.log("hello world".toAlternatingCase() == "HELLO WORLD");
console.log("HELLO WORLD".toAlternatingCase() == "hello world");
console.log("hello WORLD".toAlternatingCase() == "HELLO world");
console.log("HeLLo WoRLD".toAlternatingCase() == "hEllO wOrld");
console.log("12345".toAlternatingCase() == "12345");
console.log("1a2b3c4d5e".toAlternatingCase() == "1A2B3C4D5E");
console.log("String.prototype.toAlternatingCase".toAlternatingCase() == "sTRING.PROTOTYPE.TOaLTERNATINGcASE");