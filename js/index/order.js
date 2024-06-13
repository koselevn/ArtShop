function Order() {

    const client_full_name = document.querySelector('#client_full_name').value;
    const client_phone_number = document.querySelector('#client_phone_number').value;
    const client_country = document.querySelector('#client_country').value;
    const client_city = document.querySelector('#client_city').value;
    const client_area = document.querySelector('#client_area').value;
    const client_address = document.querySelector('#client_address').value;
    const client_apartment = document.querySelector('#client_apartment').value;
    const client_index = document.querySelector('#client_index').value;


    const formData = {
        p_id: GlobalPainting,
        client_full_name: client_full_name,
        client_phone_number: client_phone_number,
        client_country: client_country,
        client_city: client_city,
        client_area: client_area,
        client_address: client_address,
        client_apartment: client_apartment,
        client_index: client_index,
    };

    fetch('http://localhost:5000/insertOrder', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Успешно:', data);
        window.location.href = 'http://127.0.0.1:5500/thenks.html';
    })
    .catch(error => {
        console.log('Ошибка:', error);
    });
}