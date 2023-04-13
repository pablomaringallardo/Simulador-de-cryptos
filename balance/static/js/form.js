let spinner;
spinner = document.querySelector('#spinner');
const form = document.getElementById('inv-form');
const botonEnviar = document.getElementById('boton-enviar');
const botonCalcular = document.getElementById('boton-calcular');
botonEnviar.addEventListener('click', sendForm);
botonCalcular.addEventListener('click', sendFormCalculate);
spinner.classList.add('off')


function sendForm(event) {
    event.preventDefault();
    spinner.classList.remove('off')
    const formData = new FormData(form);
    const jsonData = {};

    formData.forEach((value, key) => jsonData[key] = value);
    const cantidadTo = document.getElementById('cantidadTo').textContent
    const numeros = cantidadTo.match(/\d+(.\d+)?/)[0];
    jsonData['cantidadTo'] = numeros

    fetch(
        'http://127.0.0.1:5000/api/v1/agregar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
        
    }).then(
        (response) => { return response.json(); }
    ).then(
        location.href = '/',
        spinner.classList.add('off')

    ).catch(
        (error) => console.error('ERROR!', error)
    );
};

function sendFormCalculate(event) {
    event.preventDefault()
    spinner.classList.remove('off');
    const formData = new FormData(form);
    const jsonData = {};

    formData.forEach((value, key) => jsonData[key] = value);
    const monedaTo = jsonData.monedaTo


    fetch('http://127.0.0.1:5000/api/v1/calcular', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(jsonData)  
    }).then(
        (response) => {
                return response.json();
        }
    ).then(
        (data) => {
            if (data.status == 'error') {
                throw new Error (data.message)
            }
            const cambio = data.results.toFixed(4)
            document.getElementById('cantidadTo').textContent = 'Usted recibirá ' + cambio + ' ' + monedaTo;
            botonEnviar.classList.remove('hidden');
            spinner.classList.add('off');
        }
    ).catch(
        (error) => {
            console.error('ERROR!', error);
            document.getElementById('error-message').textContent = error.message;
            document.getElementById('error-message').classList.add('alert', 'alert-danger');
            document.getElementById('error-message').setAttribute('role', 'alert');
            setTimeout(() => {
            document.getElementById('error-message').textContent = '';
            document.getElementById('error-message').classList.remove('alert', 'alert-danger');
            document.getElementById('error-message').removeAttribute('role');
            }, 8000);
            spinner.classList.add('off');
        }
    );
};
