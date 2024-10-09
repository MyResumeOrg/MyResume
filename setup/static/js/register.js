
document.addEventListener('DOMContentLoaded', () => {
    const parseUrl = new URL(document.referrer);
    let lastPage = parseUrl.pathname;
    console.log(lastPage)
    
    if (lastPage === "/accounts/terms_of_use/") {
        setTimeout(() => {
            document.querySelector("body > div > form > div > label").click()

        }, 500);
    }
});
