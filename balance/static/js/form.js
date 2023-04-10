console.log('Inicio de archivo form.js')
// alert('Archivo form.js')
const form = document.getElementById('inv-form');
const botonEnviar = document.getElementById('boton-enviar');
const botonCalcular = document.getElementById('boton-calcular');
botonEnviar.addEventListener('click', sendForm);
botonCalcular.addEventListener('click', sendFormCalculate);

function sendForm(event) {
    alert('Formulario enviado');
    event.preventDefault();


}

function sendFormCalculate(event) {
    event.preventDefault()

    const formData = new FormData(form);
    console.log('formData', formData);
    const jsonData = {};

    formData.forEach((value, key) => jsonData[key] = value);
    const monedaTo = jsonData.monedaTo
    console.log(monedaTo);
    console.log(jsonData);

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
};
