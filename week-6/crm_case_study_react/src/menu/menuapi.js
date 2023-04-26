export function apiListCrmMenu() {
    const call= fetch('http://localhost:5000/menu')
    return call.then(res=> res.json())
}