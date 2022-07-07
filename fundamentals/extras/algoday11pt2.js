/* 
  Given an array of integers
  return the first integer from the array that is not repeated anywhere else
  If there are multiple non-repeated integers in the array,
  the "first" one will be the one with the lowest index.
*/

const two_nums1 = [3, 5, 4, 3, 4, 6, 5];
const two_expected1 = 6;

const two_nums2 = [3, 5, 5];
const two_expected2 = 3;

const two_nums3 = [3, 3, 5];
const two_expected3 = 5;

const two_nums4 = [5];
const two_expected4 = 5;

const two_nums5 = [];
const two_expected5 = null;

/**
 * Finds the first int from the given array that has no duplicates. I.e., the
 *    item at the lowest index that doesn't appear again in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number|null} The first int value from the given array that has no
 *    dupes or null if there is none.
 */
function firstNonRepeated(nums) { }