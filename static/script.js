const symbols = document.querySelectorAll(".symbol");

setInterval(() => {
    for(let s of symbols) {
        let style = s.style;
        style.animation = "none";
        setTimeout(() => {
            style.animation = "bounce 1s";
        }, 10);
    }
}, 10000);
