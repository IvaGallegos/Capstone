
//Funcion para cambiar el tamaño de fuente
function cambiarTamanoFuente(accion) {
    const cuerpo = document.body;
    let tamanoActual = parseFloat(window.getComputedStyle(cuerpo).fontSize);
    
    if (accion === 'aumentar') {
        cuerpo.style.fontSize = (tamanoActual + 2) + 'px';
    } else if (accion === 'disminuir') {
        cuerpo.style.fontSize = (tamanoActual - 2) + 'px';
    }
}

