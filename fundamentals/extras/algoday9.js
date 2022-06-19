/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */

function trim(str) {
    var doneTrimming = false;
    var trimmedString = "";
    for (var i = 0; i < str.length; i++) {
        if(str[i] !== ' '){
            doneTrimming = true;
        }
        if(doneTrimming){
            trimmedString += str[i];
        }
    }
    return trimmedString;
}


console.log(trim(str1));