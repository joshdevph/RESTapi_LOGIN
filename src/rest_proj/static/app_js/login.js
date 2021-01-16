function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

form = document.querySelector('form');
form.addEventListener('submit',(e) => {
    e.preventDefault()
    var username = document.getElementById("username").value;
    var password = document.getElementById('password').value;
    fetch('/api/login/',{
        method:'POST',
        headers:{
          'Content-type':'application/json',
          'X-CSRFToken':getCookie('csrftoken'),
        },
        body:JSON.stringify({'username':username, 'password':password }),
        dataType: 'json',
      }).then(function (response) {
        return response.json()
    }).then(function (data) {
        if(data.status == true){
            console.log("User")
        }else if (data.status == false){
            console.log("Admin")
        }else{
            alert("Wrong Username or Password")
        }
    })
    form.reset()
})