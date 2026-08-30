async function obtenerContador(endpoint, idElemento) {
    try {
        const respuesta = await fetch(`https://proyecto-final-kodland.onrender.com/${endpoint}`);
        const datos = await respuesta.json();
        
        document.getElementById(idElemento).textContent = datos.mensaje;
    } catch (error) {
        console.error(`Error al cargar ${endpoint}:`, error);
    }
}

setInterval(() => {
    obtenerContador("", "revolucion-industrial")
    obtenerContador("calculo-de-duplicacion", "calculo")
    obtenerContador("curva-keeling", "curva")
    obtenerContador("evento", "conferencia")
    obtenerContador("fundacion_IPCC", "fundacion")
    obtenerContador("nacimiento_convencion", "convencion")
    obtenerContador("firma-kioto", "protocolo")
    obtenerContador("acuerdo-paris", "acuerdo")
    obtenerContador("energia-renovable", "desplomo")
    obtenerContador("precio-bajo", "precio")
    obtenerContador("muralla", "verde")
}, 1000);