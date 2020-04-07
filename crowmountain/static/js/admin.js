const button = document.getElementById("close");
const modal = document.getElementById("modal");
const alert = document.getElementsByClassName("alert")[0];
   
alert.style.color="red";

button.addEventListener('click', event => {
    modal.style.display = 'none';
});