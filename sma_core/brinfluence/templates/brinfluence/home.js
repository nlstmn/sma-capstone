// BRAND
var bmodal = document.getElementById('brand-modal');
var bbtn = document.getElementById("btn-brand");
var bspan = document.getElementsByClassName("close")[0];
bbtn.onclick = function() {
    bmodal.style.display = "block";
}
bspan.onclick = function() {
    bmodal.style.display = "none";
}
window.onclick = function(event) {
    if (event.target == bmodal) {
        bmodal.style.display = "none";
    }
}

// CONTACT
var cmodal = document.getElementById('contact-modal');
var cbtn = document.getElementById("footer-references-contact");
var cspan = document.getElementsByClassName("close")[0];
cbtn.onclick = function() {
    cmodal.style.display = "block";
}
cspan.onclick = function() {
    cmodal.style.display = "none";
}
window.onclick = function(event) {
    if (event.target == cmodal) {
        cmodal.style.display = "none";
    }
}