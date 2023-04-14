let spinner;
const peticion = new XMLHttpRequest();

function cargarInversiones() {
    spinner.classList.remove('off');
    peticion.open('GET', 'http://127.0.0.1:5000/api/v1/inversiones', true);
    peticion.send();
};

function mostrarInversiones() {
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
                    <td>${inv.rate.toFixed(5)}</td>
            `
        };

        const tabla = document.querySelector("#cuerpo-tabla");
        tabla.innerHTML = html;

    } else {
        let html = '';
        html = `
            <tr class='bg-light'><td colspan="7" class="text-secondary mensaje-vacio" >No existen inversiones en la base de datos.</td></tr>
            `
        const tabla = document.getElementById('cuerpo-tabla');
        tabla.innerHTML = html;
    };

    spinner.classList.add('off')

}
window.onload = function () {
    spinner = document.querySelector('#spinner');
    peticion.onload = mostrarInversiones;
    cargarInversiones();

};