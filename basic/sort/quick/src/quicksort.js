const assert = require('assert');

function swap(items, firstIndex, secondIndex) {
    let temp = items[firstIndex];
    items[firstIndex] = items[secondIndex];
    items[secondIndex] = temp;
}

function partition(items, left, right) {
    let pivot = items[Math.floor((left+right) / 2)];
    let left_idx = left;
    let right_idx = right;

    while(left_idx <= right_idx) {
        while(items[left_idx] < pivot) {
            left_idx++;
        }
        while(items[right_idx] > pivot) {
            right_idx--;
        }
        
       if(left_idx <= right_idx) {
            swap(items, left_idx, right_idx);
            left_idx++;
            right_idx--;
        }
    }

    return left_idx;
}

function quicksort(items, left, right) {
    if(1 >= items.length) {
        return items;
    }
    
    let idx = partition(items, left, right);

    if(left < idx - 1) {
        quicksort(items, left, idx-1);
    } 
    if(right > idx) {
        quicksort(items, idx, right)
    }

    return items;
}

describe('quicksort', () => {
    it('1', () => {
        unsortedArr = [1,4,2,5,7,3,6,8];
        assert.deepEqual(quicksort(unsortedArr, 0, unsortedArr.length-1), [1,2,3,4,5,6,7,8]);
    }),
    it('2', () => {
        unsortedArr = [5,3,1,2,4];
        assert.deepEqual(quicksort(unsortedArr, 0, unsortedArr.length-1), [1,2,3,4,5]);
    })
    it('3', () => {
        unsortedArr = [5,4,3,2,1];
        assert.deepEqual(quicksort(unsortedArr, 0, unsortedArr.length-1), [1,2,3,4,5]);
    })
    it('4', () => {
        unsortedArr = [2,2,5,5,4,4,1,1,3,3]
        assert.deepEqual(quicksort(unsortedArr, 0, unsortedArr.length-1), [1,1,2,2,3,3,4,4,5,5]);
    })
});