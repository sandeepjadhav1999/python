const nm='bye'

const ttl=document.getElementById('ttl')
const btn=document.getElementById('btn')
const red=document.getElementById('red')
const blue=document.getElementById('blue')
const green=document.getElementById('green')
const show=document.getElementById('show')
const hide=document.getElementById('hide')


btn.onclick=function(){
    ttl.textContent=nm
}

red.onclick=function(){
    ttl.style.color='red'
}

blue.onclick=function(){
    ttl.style.color='blue'
}

green.onclick=function(){
    ttl.style.color='green'
}

show.onclick=function(){
    ttl.style.display='block'
}
hide.onclick=function(){
    ttl.style.display='none'
}