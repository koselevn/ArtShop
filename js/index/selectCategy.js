function SelectCategory() {

    let div = document.querySelector('.category')

    const formData = {};

    fetch('http://localhost:5000/select-category', {
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
        data.category.map((el) => {
            const element = `<a class="category-a" onClick='SelectOfCategory("${el.category_name}")'>${el.category_name}</a>`
            result = result + element
        })
        div.innerHTML = result
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
}

SelectCategory()


function SelectOfCategory(CategoryName) {

    let div = document.querySelector('.paintings')


    const formData = {
        CategoryName: CategoryName,
    };

    fetch('http://localhost:5000/SelectOfCategory', {
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