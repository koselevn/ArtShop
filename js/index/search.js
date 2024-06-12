function Select6() {

    let div = document.querySelector('.paintings')


    const formData = {
    };

    fetch('http://localhost:5000/select6', {
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
        data.paintings.map((el) => {
            const element = `
                <div class="paintings-card">
                    <img src="img/image01.png" alt="${el.p_name}">
                    <p>${el.p_name}</p>
                    <p>${el.autor_full_name}</p>
                </div>`
        result = result + element
    })
    div.innerHTML = result
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
}

Select6()


function Search() {

    let input = document.querySelector('.search')
    let div = document.querySelector('.paintings')

    input.addEventListener('input', (event) => {
        const currentValue = input.value;

        const formData = {
            value: currentValue,
        };

        fetch('http://localhost:5000/search-paintings', {
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
            data.paintings.map((el) => {
                const element = `
                    <div class="paintings-card">
                        <img src="img/image01.png" alt="${el.p_name}">
                        <p>${el.p_name}</p>
                        <p>${el.autor_full_name}</p>
                    </div>`
            result = result + element
        })
        div.innerHTML = result
        })
        .catch(error => {
            console.log('Ошибка:', error);
        });
    });
}


Search()