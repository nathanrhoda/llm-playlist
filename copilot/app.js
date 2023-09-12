/// create a function that takes a s string and returns it backwards
function reverseString(str) {
    // split the string into an array of letters
    // reverse the order of the letters
    // join the letters back together into a string
    // return the string
    return str.split('').reverse().join('');
}

    
// test the reverseString function
console.log(reverseString('hello'));    
