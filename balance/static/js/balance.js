const peticion = new XMLHttpRequest()

function cargarInversiones() {
    console.log('Entro a cargarInversiones')
    peticion.open('GET', 'http://127.0.0.1:5000/api/v1/inversiones', true);
    peticion.send();
};

function mostrarInversiones() {
    console.log('entro a mostrarInversiones')
    if (this.readyState === 4 && this.status === 200) {
        const response = JSON.parse(peticion.responseText);
        const inversiones = response.results;

        let html = '';
        for (let i = 0; i < inversiones.length; i = i + 1) {
            const inv = inversiones[i];

            html = html + `
                <tr>
                    <td>${inv.date}</td>
                    <td>${inv.time}</td>
                    <td>${inv.monedaFrom}</td>
                    <td>${inv.cantidadFrom}</td>
                    <td>${inv.monedaTo}</td>
                    <td>${inv.cantidadTo}</td>
                    <td>${inv.rate}</td>
            `
        };

        const tabla = document.querySelector("#cuerpo-tabla");
        tabla.innerHTML = html;
    } else {
        alert('Error al mostrar las inversiones.');
    };
};

window.onload = function () {
    peticion.onload = mostrarInversiones;
    cargarInversiones();
    
};