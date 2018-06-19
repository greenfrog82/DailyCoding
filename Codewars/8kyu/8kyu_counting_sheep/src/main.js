function mysolution(arrayOfSheep) {
    cnt = 0
    arrayOfSheep.forEach(val => {
        if(val) cnt++
    })
    return cnt
}

function othersolution(arrayOfSheep) {
    return arrayOfSheep.filter(Boolean).length
}

count_sheeps = mysolution

var array1 = [true,  true,  true,  false,
    true,  true,  true,  true ,
    true,  false, true,  false,
    true,  false, false, true ,
    true,  true,  true,  true ,
    false, false, true,  true ];

console.log(count_sheeps(array1) == 17)