function factorial(n) {
    if(1 >= n) {
        return 1;
    }
    return n * factorial(n-1);
}

console.log(120 == factorial(5));