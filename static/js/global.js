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
    document.getElementById('hard_skill').classList.remove('none');
    removeElementTimer('.message_div', 5);

    const radios = document.querySelectorAll('input[type="radio"]');
    let activeContent = document.querySelector('input[type="radio"]:checked').value;

    function updateContent() {
        document.getElementById(activeContent).classList.add('none');
        activeContent = this.value;
        document.getElementById(activeContent).classList.remove('none');
    }

    radios.forEach(radio => {
        radio.addEventListener('change', updateContent);
    });
});

document.getElementById('button_add_file').addEventListener('click', () => {
    document.getElementsByClassName('file_input')[0].click();
});
