function call_click() {
    fetch('/call_click',{
        method: 'GET'
    }).then(response => {
        if (response.ok) {
            return response.json()
        }
        return Promise.reject(response)
    }).then(data => {
        document.getElementById('coins').innerText = data.core.coins
    }).catch(error => console.log(error))
}