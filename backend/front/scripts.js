function callapi(event){
    event.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;
    const captcha = grecaptcha.getResponse();
    
    const data = {
        name: name,
        mail: email,
        comment: message,
        "g-recaptcha-response": captcha
    };
    
    fetch('http://127.0.0.1:5000/ticket', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        alert('Mensagem enviada com sucesso!');
    })
    .catch(error => {
        console.error('Erro:', error);
        alert(`Ocorreu um erro ao enviar a mensagem: ${error.message}`);
    });
};
