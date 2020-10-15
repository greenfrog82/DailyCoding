// https://app.codility.com/tickets/try4SFRX2-59N/?page=1

function solution1(A) {
    function Item(val) {
        this.val = val;
    }
    Item.prototype.value = function() {
        return this.val;
    }
    return A.map(value => new Item(value));
}

const solution = solution1;

A = [1,2,3];
T = solution(A);

i = 0;
j = 1;

console.log(T[i].value() === A[i]);
console.log(T[j].value() === A[j]);
console.log(T[i].value === T[j].value);
console.log(!T[i].hasOwnProperty('value'));
console.log(!T[j].hasOwnProperty('value'));