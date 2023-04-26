
const btAd = document.getElementById('add')
btAd.onclick = function () {
    const res = document.getElementById('res')
    const num1 = document.getElementById('num1')
    const num2 = document.getElementById('num2')

    res.textContent =parseFloat(num1.value) + parseFloat(num2.value)
}

const btSub = document.getElementById('sub')
btSub.onclick = function () {
    const res = document.getElementById('res')
    const num1 = document.getElementById('num1')
    const num2 = document.getElementById('num2')

    res.textContent = parseFloat(num1.value) - parseFloat(num2.value)
}

const btMul = document.getElementById('mul')
btMul.onclick = function () {
    const res = document.getElementById('res')
    const num1 = document.getElementById('num1')
    const num2 = document.getElementById('num2')

    res.textContent = parseFloat(num1.value) * parseFloat(num2.value)
}

const btDv = document.getElementById('div')
btDv.onclick = function () {
    const res = document.getElementById('res')
    const num1 = document.getElementById('num1')
    const num2 = document.getElementById('num2')

    res.textContent = parseFloat(num1.value) / parseFloat(num2.value)
}