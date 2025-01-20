function toggleMenu() {
    const menu = document.getElementById('leftMenu');
    menu.classList.toggle('collapsed');
}

function adjustPageWidth() {
    const width = window.innerWidth;
    const body = document.body;

    if (width >= 992 && width <= 1600) {
        body.style.transform = "scale(0.9)";
        body.style.transformOrigin = "top center";
    } else if (width >= 700 && width <= 767) {
        body.style.transform = "scale(0.8)";
        body.style.transformOrigin = "top center";
    } else if (width >= 600 && width < 700) {
        body.style.transform = "scale(0.75)";
        body.style.transformOrigin = "top center";
    } else if (width <= 600) {
        body.style.transform = "scale(0.5)";
        body.style.transformOrigin = "top center";
    } else {
        body.style.transform = "scale(1)";
        body.style.transformOrigin = "top center";
    }
}

window.addEventListener('resize', adjustPageWidth);
window.addEventListener('load', adjustPageWidth);
