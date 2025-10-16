document.addEventListener("DOMContentLoaded", function() {
    const btn = document.querySelector("button");
    if (btn) {
        btn.addEventListener("click", function() {
            alert("Kliknięto przycisk!");
        });
    }
});
