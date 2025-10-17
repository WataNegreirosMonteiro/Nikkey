function verificarDigitacao(event) {
    const fieldValue = event.target.value;
    if (fieldValue.length > 20) {
        alert("Texto muito longo!");
    }
}

function validarSenha() {
    var senha = document.getElementById("senha").value;

    // Verificar o tamanho mínimo da senha
    if (senha.length < 8) {
        alert("A senha deve ter pelo menos 8 caracteres");
        return false;
    }

    // Verificar se a senha contém pelo menos maiúsula e números
    var uppercaseRegex = /[A-Z]/; //Regex é como uma máscara
    var numeroRegex = /[0-9]/;
    //uma letra maiúscula e um número
    if (!uppercaseRegex.test(senha) || !numeroRegex.test(senha)) {
        alert("A senha deve conter pelo menos uma letra maiúscula e um número");
        return false; // não passou na validação, retorna false 
    }
    return true; // o formulário será enviado para a rota /autenticar
}

