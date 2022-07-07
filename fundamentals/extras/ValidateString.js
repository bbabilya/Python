const _ = require('lodash');

function sayHello() {
  console.log('Hello, World');
}

// _.times(5, sayHello);


/*
• open brackets are closed by the same type of brackets
• open brackets are closed in the correct order

An empty string is also considered valid.
* "()" // true
* "()[]{}" // true
* "(]" // false
* "([])" //true
* "(Hello {World!})" // true
* "[1]{2(3)}" // true
* "(Oops! [This isn't right...)" // false
*/

const openedChar = (char) => {
    return char === "(" || char === "[" || char === "{"
}
const closedChar = (char) => {
    return char === ")" || char === "]" || char === "}"
}

const isValidString = (str) => {
const stack = [];

const chars = {
    "(": ")",
    "[": "]",
    "{": "}"
}

for (var i = 0; i < str.length; i++) {
    if (openedChar(str[i])) {
    stack.push(str[i]);
    }
    if (closedChar(str[i])) {
    const lastChar = stack.pop();
    if (lastChar !== "(") {
        return false;
    }
    }
    if (str[i] === "]") {
        const lastChar = stack.pop();
        if (lastChar !== "[") {
        return false;
    }
    }
    if (str[i] === "}") {
        const lastChar = stack.pop();
        if (lastChar !== "{") {
        return false;
        }
    }
}
if (stack.length !== 0) {
    return false;
}
    return true;
}

const ans = isValidString("(Hello {World!})");
console.log({ans})