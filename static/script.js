const symbols = document.querySelectorAll(".symbol");

if (symbols) {
    setInterval(() => {
        for (let s of symbols) {
            let style = s.style;
            style.animation = "none";
            setTimeout(() => {
                style.animation = "bounce 1s";
            }, 10);
        }
    }, 10000);
}


const form = document.querySelector("#spin");
if (form) {
    form.addEventListener('submit', (e) => {
        e.preventDefault();

        for (let s of symbols) {
            s.style.animation = "bounceOutDown 1s"
        }

        // Delay form submission
        setTimeout(() => {
            e.target.submit();
        }, 900);
    });

}


const toastLiveExample = document.getElementById('liveToast')
if (toastLiveExample)
{
    document.addEventListener('DOMContentLoaded', () => {
        const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
        toastBootstrap.show()
    });
}
