Enum
````Typescript
enum State {
    On = 'on'
    Off = 'off'
}

let output: State = State.off

````
Function

// since we return, return type is number
````Typescript
function add(x: number, y:number): number {
    return(x+y)
}
````
// since we do NOT return, return type is void
````Typescript
function add(x: number, y:number): void {
    console.log(x+y)
}
````

Objects & Interfaces
````Typescript
interface Instructor {
    name: string;
    course: string;
    age?: number
}

class AlgoExpertInstructor implements Instructor {
    name:string;
    course:string;

    constructor(name:string, course:string){
        this.name=name;
        this.course=course
    }
}
const tim = new AlgoExpertInstructor('Tim', "SystemExpert")


const connor: Instructor  = {
    name: 'Connor',
    course: 'Frontend Expert'
    age: 24
}

const clement: Instructor  = {
    name: 'Clement',
    course: 'AlgoExpert'
}


````

Generics
````Typescript
const arr: Array <number>= [1,2,3,'4']; // 4 will give an error.




````
