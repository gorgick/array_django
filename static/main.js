
let btns = document.querySelectorAll('.btn')

btns.forEach((btn, i) => {
    btn.addEventListener('click', getNumber)
})

async function getNumber(e) {
    const csrf = document.querySelector("[name=csrfmiddlewaretoken]").value
    const number = e.target.dataset.value
    const day = e.target.innerText
    let ul = document.querySelector('ul')
    let response = await fetch('/', {
        method: 'post',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf
        },
        body: JSON.stringify({number: number, day: day})
    })
    let data = await response.json()
    let li = document.createElement('li')
    li.innerText = await data['People']
    ul.appendChild(li)
}