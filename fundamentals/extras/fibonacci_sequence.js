/* 
Return the fibonacci number at the nth position, recursively.

Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
The next number is found by adding up the two numbers before it,
starting with 0 and 1 as the first two numbers of the sequence.
*/

const twoNum1 = 0;
const twoExpected1 = 0;

const twoNum2 = 1;
const twoExpected2 = 1;

const twoNum3 = 2;
const twoExpected3 = 1;

const twoNum4 = 3;
const twoExpected4 = 2;

const twoNum5 = 4;
const twoExpected5 = 3;

const twoNum6 = 8;
const twoExpected6 = 21;

const twoNum7 = 50;

/**
 * Recursively finds the nth number in the fibonacci sequence.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num The position of the desired number in the fibonacci sequence.
 * @returns {number} The fibonacci number at the given position.
 */
function fibonacci(n) {
    if( n <= 1 ){
        return n;
    }
    else{
        return fibonacci( n - 1 ) + fibonacci (n - 2 );
    }
}

console.log(fibonacci( twoNum1 ))
console.log(fibonacci( twoNum2 ))
console.log(fibonacci( twoNum3 ))
console.log(fibonacci( twoNum4 ))
console.log(fibonacci( twoNum5 ))
console.log(fibonacci( twoNum6 ))
console.log(fibonacci( twoNum7 ))