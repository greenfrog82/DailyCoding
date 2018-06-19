function mysolution(bool) {
    return ['No', 'Yes'][+bool]
}

boolToWord = mysolution

console.log(boolToWord(true) === 'Yes')
console.log(boolToWord(false) === 'No')