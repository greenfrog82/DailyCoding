function mysolution(input) {
    return 0 < input.length? [input.filter(x => x > 0).length, input.filter(x => x < 0).reduce((total, num) => total + num, 0)]: []
}

count_positives_sum_negatives = mysolution

console.log(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])) // [10, -65]
console.log(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14])) // [8, -50]
console.log(count_positives_sum_negatives([1])) // [1, 0]
console.log(count_positives_sum_negatives([-1])) // [0, -1]
console.log(count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0])) // [0, 0])
console.log(count_positives_sum_negatives([])) // []