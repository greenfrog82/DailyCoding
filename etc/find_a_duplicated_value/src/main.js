function solution(inputs) {
    let set_ = new Set();
    for(let i=0; i<inputs.length; i++) {
        let val = inputs[i];
        if(set_.has(inputs[i])) {
            return val;
        } else {
            set_.add(val)
        }
    }
    return -1;
}

console.log(solution([1, 3, 2, 3, 4]) === 3)
console.log(solution([1, 2, 3, 4, 5]) === -1)