const dob=document.getElementById('dob')
dob.onchange=function(e){
    const selectdtstr=e.target.value
    const selectdate=new Date(selectdtstr)

    console.log(selectdate)

    const msg=document.getElementById('age')
    msg.textContent=`age is ${calage(selectdate)}`
}

function calage(birthday){
    const agediff=Date.now()-birthday
    const agedate=new Date(agediff)
    return Math.abs(agedate.getUTCFullYear()-1970)
}