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
    alert('Calcular datos');
    event.preventDefault()

    const formData = new FormData(form);
    console.log('formData', formData);
    const jsonData = {};

    formData.forEach((value, key) => jsonData[key] = value);
    console.log(jsonData);

}
