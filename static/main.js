
let btns = document.querySelectorAll('.btn')

btns.forEach((btn, i) => {
    btn.addEventListener('click', getNumber)
})

async function getNumber(e) {
    const csrf = document.querySelector("[name=csrfmiddlewaretoken]").value
    const number = e.target.dataset.value
    console.log(number)
    let response = await fetch('/', {
        method: 'post',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf
        },
        body: JSON.stringify({number: number})
    })
    let data = await response.json()
    console.log(await data)
}