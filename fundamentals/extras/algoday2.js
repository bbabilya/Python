const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(n).
 * - Space: O(n).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(str) {
    var reverseStr = "";
    for(var i = str.length-1; i >= 0; i--){
        reverseStr += str.charAt(i);
    }
    return reverseStr;
}
console.log(str1);
console.log(reverseString(str1));
console.log(expected1);


console.log(str2);
console.log(reverseString(str2));
console.log(expected2);

console.log(str3);
console.log(reverseString(str3));
console.log(expected3);

console.log(str4);
console.log(reverseString(str4));
console.log(expected4);