function toHan(n) {
    let arr = Array.from(n);
    console.log(arr)
    let result = arr.map( (val, index) => {
        
        switch(val) {
            case "0":
                return "零";
            case "1":
                return "壹";
            case "2":
                return "贰";
            default:
                return;
        }
    } )

    result.reverse();
    // let han = arr.join("");
    console.log(result)
}

function mul(n) {

    // for(let i=1; i<n; i++){
    //     num *= 1;
    // }

    // n! = n * (n-1)!

    if (n == 1 || n == 2) {
        return 1;
    }
    
    return n * fn(n-1);
}

function toHan2(num) {
    let str = num + "";

}
