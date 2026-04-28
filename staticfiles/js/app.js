
function toggleMenu(){
  document.getElementById("menu").classList.toggle("active");
}

function scrollToLibrary(){
  document.getElementById("library-main").scrollIntoView({behavior:"smooth"});
}


function registerUser(event) {
    event.preventDefault();

    const url = document.body.dataset.registerUrl;
    const csrf = document.body.dataset.csrf;

    const data = {
        username: document.getElementById("username").value,
        email: document.getElementById("email").value,
        password: document.getElementById("password").value
    };

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrf
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        if (data.status === "success") {
            alert("Գրանցումը հաջողվեց ✅");
            window.location.href = "/login"; // redirect
        } else {
            alert(data.error);
        }
    });
}

function loginUser(e){
  e.preventDefault();
  alert("Մուտքը հաջողվեց ✅");
}




