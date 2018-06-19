function mysolution(humanYears) {
    op = (humanYears, additionYear) => 1 < humanYears? 24 + (humanYears - 2) * additionYear: 15
    return [humanYears, op(humanYears, 4), op(humanYears, 5)]
}

const humanYearsCatYearsDogYears = mysolution

console.log(humanYearsCatYearsDogYears(1)) // [1,15,15]
console.log(humanYearsCatYearsDogYears(2)) // [2,24,24]
console.log(humanYearsCatYearsDogYears(10)) // [10, 56, 64]