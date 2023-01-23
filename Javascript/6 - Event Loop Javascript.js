const multi = (m) =>{
    return m*m
}

const sum = (n,m) => {

    return n + multi(m)
}

const one = () => setTimeout(()=> console.log("One"),0)
const two = () => console.log("two")
const three = () => console.log(sum(2,3))
const four = () => setTimeout(()=> console.log("Four"),0)

one()
two()
three()
four()
