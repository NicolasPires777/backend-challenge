function callapi(event) {
    event.preventDefault();
    
    // Mostrar a mensagem de carregamento
    const loadingElement = document.getElementById('loading-message');
    loadingElement.style.display = 'block';

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
    .then(response => {
        // Ocultar a mensagem de carregamento
        loadingElement.style.display = 'none';
        
        if (!response.ok) {
            return response.json().then(errorData => {
                // Atualiza o texto do elemento de erro
                const errorElement = document.getElementById('error-message');
                errorElement.textContent = errorData.detail || 'Ocorreu um erro ao enviar a mensagem.';
                errorElement.style.display = 'block';  // Mostra o elemento de erro
                document.getElementById('success-message').style.display = 'none'; // Oculta o elemento de sucesso
                throw new Error(errorData.detail || 'Ocorreu um erro ao enviar a mensagem.');
            });
        }
        return response.json();
    })
    .then(data => {
        // Atualiza o texto do elemento de sucesso
        const successElement = document.getElementById('success-message');
        successElement.textContent = 'Solicitação enviada, verifique seu e-mail';
        successElement.style.display = 'block';  // Mostra o elemento de sucesso
        document.getElementById('error-message').style.display = 'none'; // Oculta o elemento de erro
    })
    .catch(error => {
        console.error('Erro:', error);
        // Caso o erro não seja tratado pelo bloco .then, atualiza o texto do elemento de erro
        const errorElement = document.getElementById('error-message');
        errorElement.textContent = error.message || 'Ocorreu um erro ao enviar a mensagem.';
        errorElement.style.display = 'block';  // Mostra o elemento de erro
        document.getElementById('success-message').style.display = 'none'; // Oculta o elemento de sucesso
    });
}
