const input = document.querySelector(".input-field-password");
const inputIcon = document.querySelector(".input-icon");

inputIcon.addEventListener("click", (e) =>{

    e.preventDefault();

    inputIcon.setAttribute('src', 
                            input.getAttribute('type') === 'password' 
                            ? 
                            'assets/img/eye-svgrepo-com.svg'
                            :
                            'assets/img/eye-off-svgrepo-com.svg');

    input.setAttribute('type',
                        input.getAttribute('type') === 'password'
        ?
        'text'
        :
        'password'
    );
});

function openCity(evt, cityName){

    let i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");
        for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
        }
    tablinks = document.getElementsByClassName("tablinks");
        for (i = 0; i < tablinks.length; i++){
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
     
}