function calculate(num1,num2) {
    return num1+num2
}
let res=calculate(50,78)
console.log(res)

//if ladder
if (res>50) console.log('hi')
else if (res>60 &&res <70) console.log('hello')
else console.log('bye')


//in switch that v cnt add condition
switch (res){
    case 100:{
        console.log('hii')
        break
    }
    case 128:{
        console.log('helloo')
        break
    }
    default:{
        console.log('bye')
    }
}