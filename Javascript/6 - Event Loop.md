## Overview: [EventLoop] https://dev.to/lydiahallie/javascript-visualized-event-loop-3dif
- JavaScript is single-threaded: only one task can run at a time. Therefore only one task can run at a time how is this order determined?

### Note:
- 3 Components: Call Stack, Call Back Queue, Web Api

Let take for example the below functions:
````javascript
const multi = (m) =>{
    return m*m
}

const sum = (n,m) => {

    return n + multi(m)
}

const one = () => setTimeout(()=> console.log("One"),2000)
const two = () => console.log("two")
const three = () => console.log(sum(2,3))
const four = () => setTimeout(()=> console.log("Four"),200)

one()
two()
three()
four()
````


1. Function one() get pushed on the call back and popped on in LIFO order
2. This function is asynchronous function, meaning that the timer function will not pause execution of other functions in the functions stack.
3. This function get kicked to the Web Api
4. Then function two() is popped on and console.logs("two)
5. The function three() is popped on but function two runs sum(), then multi
````javascript
// current call stack will then look like
multi()
sum()
three()
````
6. multi will perform then sum, then three.
7. then one() which is wait on the queue will run
8. then four()
