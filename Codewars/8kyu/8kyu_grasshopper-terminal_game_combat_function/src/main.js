function mysolution(health, damage) {
    return health > damage? health - damage: 0
}

function othersolution(health, damage) {
    return Math.max(0, health - damage)
}

combat = othersolution

console.log(combat(100, 5) === 95)
console.log(combat(92, 8) === 84)
console.log(combat(20, 30) === 0)