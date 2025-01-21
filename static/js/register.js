document.addEventListener('DOMContentLoaded', () => {
    const parseUrl = new URL(document.referrer || window.location.href);
    let lastPage = parseUrl.pathname;
    console.log(lastPage);

    if (lastPage === "/accounts/terms_of_use/") {
        setTimeout(() => {
            document.querySelector("body > div > form > div > label").click();
        }, 500);
    }

    const checkbox = document.querySelector('#remember-me');
    const submitButton = document.querySelector('#submit-button');

    function toggleSubmitButton() {
        submitButton.disabled = !checkbox.checked;
    }

    toggleSubmitButton();

    checkbox.addEventListener('change', toggleSubmitButton);
});
