setInterval(getDataDHT11, 5000); //ejecutando getDataDHT11 cada 5 segundos


function getDataDHT11() {

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {  //funcion de callback para manejar la respuesta recibida del servidor
        if (this.readyState == 4 && this.status == 200) {
            //colocando la data recibida en los span adecuados
            var data = JSON.parse(this.response);
            document.getElementById("temperatura").innerHTML = data.Temperatura;
            document.getElementById("humedad").innerHTML = data.Humedad;
        }
    };
    xhttp.open("GET", "/sensor/", true); //peticion GET enviada al servidor
    xhttp.send();


}