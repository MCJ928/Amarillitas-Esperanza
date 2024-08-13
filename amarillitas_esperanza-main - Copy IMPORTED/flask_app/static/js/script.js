
var element = document.getElementById('star')

function yellow(element){
    element.style.color = "#ffde59"
}

function white(element){
    element.style.color = "white";
}

/* Ariel Avila - 29-04-2024 MB01: Se Agrega script para el mapa */

var latitud = document.getElementById('adress_lat').value;
var longitud = document.getElementById('adress_long').value;
/* Ariel Avila - 29-04-2024 MB01: Se Agrega el token */
mapboxgl.accessToken = 'pk.eyJ1IjoiYXJpZWxjdmN4IiwiYSI6ImNsdmJuNXBvYjBhbHkya3FtZ2d1dG50cTIifQ.0m8_eMRY8yqswpGtGwy8iw';

var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [longitud,latitud], // Aca podemos cambiar la longitud y latitud para que aparezca centrado el mapa donde queramos
    zoom: 15
});

new mapboxgl.Marker()
    .setLngLat([longitud, latitud])
    .addTo(map);