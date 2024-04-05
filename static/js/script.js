document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita que o formulário seja submetido normalmente
            
    var formData = new FormData(this);
            
    fetch('/api/login/', {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao fazer login');
        }
        return response.json();
    })
    .then(data => {
        // Login bem-sucedido, redirecionar ou manipular a resposta conforme necessário
        console.log('Login bem-sucedido:', data);
    })
    .catch(error => {
        // Mostrar mensagem de erro no elemento com id 'error-message'
        document.getElementById('error-message').textContent = 'Erro ao fazer login';
    });
});