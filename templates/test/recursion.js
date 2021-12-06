function factorial(n) {

    if (n == 1 || n == 0) {
        return 1;
    }
    return n * factorial(n-1)
}

function fib(n) {
    // n = (n-1) + (n-2)
    // 第n位等于前两位的和
    if (n == 1 || n == 2) return 1;
    return fib(n-1) + fib(n-2);
}

// !!" " + !!"" - !!false || document.write('pork!!!')
// true + false - false

// typeof null -> "object"

// (window.foo || (window.foo == "bar"))