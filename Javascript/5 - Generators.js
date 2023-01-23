// Generators
// same a function but we get yield which is like return but allows us to pause function

function* genNumbers(x){
    yield 1;
    yield 2;
    yield 3;
    return 4;
    yield 5;
}

const generatorObject1 = genNumbers()
console.log(generatorObject1.next().value)//{value:1, done:false}
console.log(generatorObject1.next().value)//{value:2, done:false}
console.log(generatorObject1.next().value)//{value:3, done:false}
console.log(generatorObject1.next().value)//{value:4, done:true}
console.log(generatorObject1.next().value)//{undefined}

function* genNumbers(count){
    for(let i=0; i<count; i++){
        yield i;
    }
}
const generatorObject2 = genNumbers(3)
console.log(generatorObject2.next().value)
console.log(generatorObject2.next().value)
console.log(generatorObject2.next().value)
console.log(generatorObject2.next().value)
console.log(generatorObject2.next().value)
function* genNumbers(x){
    yield x;
    yield x + 5;
    yield 3;
    yield x + 10;
}

const generatorObject3 = genNumbers(1)
console.log(generatorObject3.next().value)
console.log(generatorObject3.next(3).value)
console.log(generatorObject3.next(4).value)
console.log(generatorObject3.return())
console.log(generatorObject3.next(5).value)


// Yielding to another generator function
function* generator1(){
    yield 1;
    yield 2;
}

function* generator2(){
    yield 3;
    yield 4;
}

function* genNumbers(){
    yield* generator1()
    yield 2.5
    yield* generator2()

}

const generatorObject4 = genNumbers()
console.log(generatorObject4.next().value)
console.log(generatorObject4.next().value)
console.log(generatorObject4.next().value)
console.log(generatorObject4.next().value)
console.log(generatorObject4.next().value)
console.log(generatorObject4.next().value)
