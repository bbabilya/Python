/* 
Zip Arrays into Map
Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
    abc: 42,
    3: "wassup",
    yo: true,
};

const keys2 = [];
const vals2 = [];
const expected2 = {};

/**
   * Converts the given arrays of keys and values into an object.
   * - Time: O(?).
   * - Space: O(?).
   * @param {Array<string>} keys
   * @param {Array<any>} values
   * @returns {Object} The object with the given keys and values.
   */

function zipArraysIntoMaps(keys, values){
    var newObject = {};
    if(keys.length === values.length){
        var length = keys.length;
        for(var x = 0; x < length; x++){
            var curkey = keys[x];
            var curval = values[x];
            newObject[curkey] = curval;
        }
    }
    return newObject;
}

console.log(zipArray(keys1,vals1));