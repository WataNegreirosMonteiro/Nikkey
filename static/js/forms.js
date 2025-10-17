

//no lugar de chamar a URL /autenticar (versão anterior desta atividade) 
// vamos chamar um script para conferir e preparar os dados para chamada da API, que fica em outra url
document.getElementById('formLogin').addEventListener('submit', async function (event) {
    event.preventDefault(); // Evita o envio tradicional do formulário

    const login = document.getElementById('login').value;
    const senha = document.getElementById('senha').value;

    console.log('Login:', login); // debugando valores no console do navegador
    console.log('Senha:', senha); 
    try {

        //const response = await fetch('http://127.0.0.1:8050/api/autenticarLogin', {
        console.log ("url: ", `${config.backendUrl}/api/autenticarLogin`);
        //consulto o config.js para saber o valor da propriedade backendUrl
        const response = await fetch(`${config.backendUrl}/api/autenticarLogin`, { //aqui o endereço da API (com as rotas no arquivo .py)
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ login: login, senha: senha }), //
        });

        console.log('Chamada da API. Aguardando resposta...');
        console.log('Resposta bruta:', response); 
        console.log('Status da resposta:', response.status); // status HTTP

        const text = await response.text(); // Ler a resposta como texto
        console.log('Conteúdo da resposta:', text); // Verifique o conteúdo da resposta

        const data = JSON.parse(text); // Converte o texto para JSON
        //const data = await response.json(); // a estrutura JSON para para variável data
        console.log('Resposta da API:', data);

        const mensagemDiv = document.getElementById('mensagem');
        mensagemDiv.style.display = 'block';

        if (data.status === 1) {
            mensagemDiv.className = 'sucesso';
            mensagemDiv.textContent = 'Login efetuado com sucesso!';
        } else {
            mensagemDiv.className = 'erro';
            mensagemDiv.textContent = data.aviso;
        }
    } catch (error) {
        //console.log('Erro ao fazer login:', error);
        const mensagemDiv = document.getElementById('mensagem');
        mensagemDiv.style.display = 'block';
        mensagemDiv.className = 'erro';
        mensagemDiv.textContent = 'Erro ao conectar com o servidor.';
    }
});
