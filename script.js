function actualizarContador() {
    fetch("http://127.0.0.1:8000")
        .then(respuesta => respuesta.json())
        .then(datos => {
            document.getElementById("texto-servidor").innerText = datos.mensaje + " segundos";
        });
}

setInterval(actualizarContador, 1000);