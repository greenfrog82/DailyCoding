function mysolution(salary, bonus) {
    return `£${bonus? salary * 10: salary}`
}

bonusTime = mysolution

console.log(bonusTime(10000, true) === '£100000');
console.log(bonusTime(25000, true) === '£250000');
console.log(bonusTime(10000, false) === '£10000');
console.log(bonusTime(60000, false) === '£60000');
console.log(bonusTime(2, true) === '£20');
console.log(bonusTime(78, false) === '£78');
console.log(bonusTime(67890, true) === '£678900');