/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
    let arr = [];
    let temp = "";
    for (i in str) {
        if (str[i] == " " || i == str.length - 1) {
            if (i == str.length - 1) {
                temp += str[i];
            }
            arr.push(temp);
            temp = "";
        } else {
            temp += str[i];
        }
    }
    for(var i = 0; i<arr.length; i++){
        var rev = "";
        console.log(arr[i]);
        for(var j = arr[i].length-1; j >= 0; j--){
            rev += arr[j];
        }
    }
    return arr;
}

console.log(reverseWords(str2));