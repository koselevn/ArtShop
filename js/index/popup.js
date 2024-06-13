let GlobalPainting = 0

function SelectPopup(El_id) {

    let div = document.querySelector('.popup_text')

    const formData = {
        id: El_id,
    };

    fetch('http://localhost:5000/select-popup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успешно:', data);
        let result = ``
        data.painting.map((el) => {
            GlobalPainting = el.p_id
            const element = `
            <div>
                <img class="popup-img" src="${el.p_img_link}" alt="${el.p_description}">
                <p class="text-center p-name">${el.p_name}</p>
                <p class="text-center p-description">${el.p_description}</p>
                <p class="text-center p-author">${el.autor_full_name}</p>
                <p class="text-center p-price">${el.p_price}</p>
                <p class="text-center p-order-it"><a href="#popup2">Order it</a></p>
            </div>
            `
            result = result + element
        })
        div.innerHTML = result
        console.log(GlobalPainting)
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
}