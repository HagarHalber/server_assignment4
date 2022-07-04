const activePge = window.location.href;
const navList = document.querySelectorAll('nav a').
 forEach(link => {
    if(link.href == activePge && link.className == 'headnav'){
        console.log(activePge);
        link.classList.add('active');
    }
});


var i = 0;
var speed = 50;
var txt =  "Hagar's Pizza";

function  typing () {
    if (i < txt.length) {
        document.getElementById("header").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typing, speed);
    }
}

const fullname = document.getElementById("FullName");
const Email = document.getElementById("Email");
const phone = document.getElementById("phone number");
const form = document.getElementById("contact");
const errorElement = document.getElementById("error");

form.addEventListener('submit', (e)=>{
    let messages = []
    if(fullname.value == '' || fullname.value == null || Email.value =='' || Email.value == null || phone.value == '' || phone.value == null  ){
        e.preventDefault();
        alert('Full name,Email,Phone are required fildes');
    }

    else{
        alert('Your message was sent successfully, thank you for connecting us hope to hear from you again soon!');
        document.getElementsByClassName('text').style.display = "none";
        document.getElementsByClassName('thank_you').style.display = "block";
    }
}
)







