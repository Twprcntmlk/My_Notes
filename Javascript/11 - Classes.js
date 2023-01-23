class Character{
    static isBase = true // private instance
    constructor(name){
        this.name = name // public instance
    }

    // instance method
    move(input){
        switch(input) {
            case 'up':
              console.log('up')
              break;
            case 'down':
              console.log('down')
              break;
            case 'left':
              console.log('left')
              break;
            case 'right':
              console.log('right')
              break;
            default:
              // code block
        }
    }

    // instance getter
    get charName(){
        return this.name
    }

    // instance setter
    set charName(value){
        this.name = value
    }
}

const mrFuji = new Character('Mr. Fuji');
mrFuji.move("up")
mrFuji.move("down")
mrFuji.move("left")
mrFuji.move("right")
// Calling Getter
console.log(mrFuji.charName)
// Calling Setter
mrFuji.charName = "Mr. Miyamoto"
console.log(mrFuji.charName)
console.log(mrFuji.isBase)
console.log(Character.isBase)

console.log("----------------------------------------------------------------------------------")
class Pokemon extends Character {
    constructor(name, level, type){
        super(name)
        this.level = level
        this.type = type
        this.moveSet= {
            0:"Fire Blast",
            1:"Iron Tail",
            2:"Scratch",
            3:"Explosion"
        }
    }
    get pokeLevel(){
        return this.level
    }

    // instance setter
    set pokeLevel(value){
        this.level = value
    }

    get pokeType(){
        return this.type
    }

    // instance setter
    set pokeType(value){
        this.type = value
    }

    // private method
    #getRandomInt(max){
        return Math.floor(Math.random() * max)
    }

    attacks(){
        return this.moveSet[this.#getRandomInt(4)]
    }
}

const charmander = new Pokemon('charmander', 13, 'fire')
// methods from parent class
console.log(charmander.name)
charmander.move('up')
charmander.move('right')

console.log(charmander.pokeLevel)
console.log(charmander.pokeType)

console.log(charmander.attacks())

console.log(charmander.attacks())
console.log(charmander.attacks())

// private so can't bne accesses uncomment to see that
// charmander.getRandomInt is not a function
// console.log(charmander.#getRandomInt(5))
