/* 
  Recursively reverse a string
  helpful methods:
  str.slice(beginIndex[, endIndex])
  returns a new string from beginIndex to endIndex exclusive
*/

const twoStr1 = "abc";
const twoExpected1 = "cba";

const twoStr2 = "";
const twoExpected2 = "";

/**
 * Recursively reverses a string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given str reversed.
 */


function reverseStr(str) {
    if (str.length <= 1) {
        return str;
    } else {
        return str[str.length - 1] + reverseStr(str.slice(0, str.length - 1));
    }
}
console.log(reverseStr(twoStr1));
console.log(reverseStr(twoStr2));