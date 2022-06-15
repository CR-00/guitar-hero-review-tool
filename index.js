const uiContainer = document.querySelector(".ui-container");
const uiDisplay = document.querySelector(".ui-display");

const updateUi = () => {
  /* Generate new HTML in backend. */
  fetch('http://localhost:5000/render-input')
  .then(response => {
    return response.json();
  })
  .then(input => {
    uiDisplay.innerHTML = input
  });

}

window.setInterval(updateUi, 1000);
