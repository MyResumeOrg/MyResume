function removeElementTimer(idOrClass, seconds){
    let elements = document.querySelectorAll(idOrClass)

    if (elements) {
        setTimeout(() => {
            elements.forEach(element => {
                console.log(`Removing element: ${element}`)
                element.remove()
            });
        }, seconds * 1000);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    removeElementTimer('.message_div', 5);
});
