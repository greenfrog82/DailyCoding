function mysolution(bool) {
    return ['No', 'Yes'][+bool]
}

function othersolution(bool) {
    return bool? 'Yes': 'No'
}

boolToWord = othersolution

console.log(boolToWord(true) === 'Yes')
console.log(boolToWord(false) === 'No')