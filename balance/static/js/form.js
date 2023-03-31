const form = document.getElementById("form");
const botonEnviar = document.getElementById("boton-enviar");
const botonCalcular = document.getElementById("boton-calcular");
botonEnviar.addEventListener("submit", sendForm);
botonCalcular.addEventListener("submit", sendFormCalculate);

function sendForm(event) {
    alert('Formulario enviado')

}
