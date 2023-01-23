// Currying
// The process of transforming a function to treat its parameters as a sequence
// of individual function calls that each take one parameter.
// For example, func(a, b, c)  would become func(a)(b)(c)

// Currying allows us to create middleware for Redux that doesn't interfere with any of it's functionality.
//It will only log the sentence the second time it's called.

//Example 1

// const multiply = (x, y) => x * y
// multiply(3, 2)

const multiply = x => y => x * y

console.log(multiply(3)(2))//=> returns 6
console.log(multiply(3)(3))//=> returns 6
// or
const triple = multiply(3) //=> triple is now a function as well
console.log(triple(2)) //=> returns 6
console.log(triple(3)) //=> returns 9




// Example 2
let nums = item => (x) => (
    !item ?
    { first: x, }
    :
    { first: x, ...item }
  )

  console.log(nums()(5))
  console.log(nums({second: 2 })(3))
