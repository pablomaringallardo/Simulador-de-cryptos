const form = document.getElementById('inv-form');
const botonEnviar = document.getElementById('boton-enviar');
const botonCalcular = document.getElementById('boton-calcular');
botonEnviar.addEventListener('click', sendForm);
botonCalcular.addEventListener('click', sendFormCalculate);

function sendForm(event) {
    alert('Formulario enviado');
    event.preventDefault();
    const formData = new FormData(form);
    console.log('formData', formData);
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
    ).catch(
        (error) => console.error('ERROR!', error)
    );
};

function sendFormCalculate(event) {
    event.preventDefault()

    const formData = new FormData(form);
    console.log('formData', formData);
    const jsonData = {};

    formData.forEach((value, key) => jsonData[key] = value);
    const monedaTo = jsonData.monedaTo
    console.log('hola', monedaTo);

    if (jsonData.monedaFrom === jsonData.monedaTo) {
        alert('No puedes invertir a la misma moneda.')
    } else {
        fetch('http://127.0.0.1:5000/api/v1/calcular', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    }).then(
        (response) => { return response.json(); }
    ).then(
        (data) => {
            console.log('Resultado:', data.results);
            const cambio = data.results.toFixed(4)
            document.getElementById('cantidadTo').textContent = 'Usted recibirá ' + cambio + ' ' + monedaTo;
            botonEnviar.classList.remove('hidden');
        }
    ).catch(
        (error) => console.error('ERROR!', error)
    );

}
};
