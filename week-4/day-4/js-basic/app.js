//javascript is a programmin langugae
// It was invented by Brendan Eich (co-founder of the Mozilla project, the Mozilla Foundation, and the Mozilla Corporation).
//it is manily used to make website dynamic

//ECMAScript 
var nm='and' //var has no scope
var ver='android' //let has scope
const os=2 //constant

console.log('os is'+nm+'vaersion is '+ver)


let cnt=10
if (true) {
    let cnt=20
    let abc='hi'
    console.log(abc)
}
console.log(cnt) //here cnt n abc is r not accessible becoz thy are block code and r accessible oly inside the if block...............if v use var inside if let thn thy r accessible becoz thy dont v any scope
console.log(abc)