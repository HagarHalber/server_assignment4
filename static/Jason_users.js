const userContainer = document.getElementById('container_outer');
const form_users = document.getElementById("get-user-form")
form_users.onsubmit = onFormSubmit;
console.log('hi')

function onFormSubmit(e) {
    const id = document.getElementById("id").value;
    getUser(id);
    e.preventDefault();
}

function getUser(id) {
    const url = `https://reqres.in/api/users/${id}`;
    console.log(url)
    fetch(url).then(
        response => response.json()
    ).then(
        response => {
            const data = response.data;
            userContainer.innerHTML = `
            <img src="${data.avatar}" alt="Profile Picture"/>
            <h3>${data.first_name} ${data.last_name}</h3>
            `
        }
    ).catch(
        err => console.log(err)
    )
}