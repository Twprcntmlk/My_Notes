Reduce

// Arrow function
// reduce((accumulator, currentValue) => { /* … */ })
// reduce((accumulator, currentValue, currentIndex) => { /* … */ })
// reduce((accumulator, currentValue, currentIndex, array) => { /* … */ })

// reduce((accumulator, currentValue) => { /* … */ }, initialValue)
// reduce((accumulator, currentValue, currentIndex) => { /* … */ }, initialValue)
// reduce((accumulator, currentValue, currentIndex, array) => { /* … */ }, initialValue)

// Callback function
// reduce(callbackFn)
// reduce(callbackFn, initialValue)

// Inline callback function
// reduce(function (accumulator, currentValue) { /* … */ })
// reduce(function (accumulator, currentValue, currentIndex) { /* … */ })
// reduce(function (accumulator, currentValue, currentIndex, array) { /* … */ })

// reduce(function (accumulator, currentValue) { /* … */ }, initialValue)
// reduce(function (accumulator, currentValue, currentIndex) { /* … */ }, initialValue)
// reduce(function (accumulator, currentValue, currentIndex, array) { /* … */ }, initialValue)



// const callBackFunc= (a, b) => Math.max(a, b);
const callBackFunc= (a, b) => a+b;
// callback is invoked for each element in the array starting at index 0
const result1 = [1, 100].reduce(callBackFunc, 50); // 100
console.log(result1)
const result2 = [50].reduce(callBackFunc, 10); // 50
console.log(result2)
// callback is invoked once for element at index 1
const result3 = [1, 100].reduce(callBackFunc); // 100
console.log(result3)
console.log("callback is not invoked")
const result4 = [50].reduce(callBackFunc); // 50
console.log(result4)
const result5 = [].reduce(callBackFunc, 1); // 1
console.log(result5)
// [].reduce(callBackFunc); // TypeError
console.log("---------------------------------------------------------------------------------")

const add = {
    a: {gold:1, silver:4, plat:7},
    b: {gold:2, silver:5, plat:8},
    c: {gold:3, silver:6, plat:9}
  }

let object1= {
    gold: 0,
    silver: 0,
    plat:0
    }

Object.values(add).reduce((acc, v) => {
    for(key of Object.keys(object1)){
        if (key in v){
            object1[key]+=v[key]
        }
    }
},object1)
console.log(object1)
