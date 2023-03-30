const peticion = new XMLHttpRequest();

function cargarEstados() {
    peticion.open('GET', 'http://127.0.0.1:5000/api/v1/estado', true);
    peticion.send();
};

function mostrarEstados() {

    if (this.readyState === 4 && this.status === 200) {
        const response = JSON.parse(peticion.responseText);
        const estados = response.results;
        let identificadores = ['ada','btc' ,'doge' ,'dot', 'eth', 'shib', 'sol', 'usdt', 'xrp','invertido', 'valor-actual', 'valor-total'];


        for (let i = 0; i < identificadores.length; i = i + 1) {
            const p = document.createElement("p");
            p.className += 'card-text';
            p.innerHTML = estados[Object.keys(estados)[i]];
            document.getElementById(identificadores[i]).appendChild(p);
        }
        console.log(estados.total_euros_invertidos);
    }
};

window.onload = function () {
    peticion.onload = mostrarEstados;
    cargarEstados();
};