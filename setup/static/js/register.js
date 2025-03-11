document.addEventListener("DOMContentLoaded", () => {
  const parseUrl = new URL(document.referrer || window.location.href);
  let lastPage = parseUrl.pathname;
  console.log(lastPage);

  if (lastPage === "/accounts/terms_of_use/") {
    setTimeout(() => {
      document.querySelector("body > div > form > div > label").click();
    }, 500);
  }

  const checkbox = document.querySelector("#remember-me");
  const form = document.querySelector("form");
  const elementTermsOfUsageNeeded = document.querySelector(
    ".messageTermsOfUsageNeeded"
  );

  form.addEventListener("submit", (e) => {
    if (!checkbox.checked) {
      e.preventDefault();
      elementTermsOfUsageNeeded.style.display = "block";
      setTimeout(() => {
        elementTermsOfUsageNeeded.style.display = 'none';
      }, 5000);
    }
  });

  // checkbox.addEventListener("change", toggleSubmitButton);
});
