function solution(inputs) {
    let currentSum = inputs[0];
    let maxSum = inputs[0];

    for(let i=1; i<inputs.length; i++) {
        currentSum = Math.max(currentSum + inputs[i], inputs[i]);
        maxSum = Math.max(currentSum, maxSum);
    }

    return maxSum;
}

console.log(solution([-1, 3, -1, 5]) == 7)
console.log(solution([-5, -3, -1]) == -1)
console.log(solution([2, 4, -2, -3, 8]) == 9)
console.log(solution([3, -1, -1, 2]) == 3)
console.log(solution([3, -1, -1, 3]) == 4)
console.log(solution([-1, -3, -5]) == -1)
console.log(solution([2, 4, -2, 2, 8]) == 14)