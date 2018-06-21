function fibonacci(n) {
    if(1 >= n) {
        return 1;
    }
    
    return fibonacci(n-2) + fibonacci(n-1);
}

console.log(8 === fibonacci(5));