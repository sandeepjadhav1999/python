const mb=[
    'abc',
    'qwe',
    'ert',
    'oiu'
]

ol=document.getElementById('mbs')

for (let i=0; i<mb.length;i++){
    const mbs=mb[i]

    const li=document.createElement('li')
    li.textContent=mbs

    ol.appendChild(li)
}
const lie=document.getElementById('btn')
lie.onclick=()=>{
    const lastChild=ol.lastChild
    ol.removeChild(lastChild)
}