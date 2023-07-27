# XPorcento

##  LinkTree
## Tópicos:

1. Configurar ambiente.
2. Instalar pacotes.
3. Referências do Streamlit.
4. Uso do Github no projeto.
5. Deploy no Streamlit.
6. Desenvolvendo em equipe no Github.


# Tutorial de Configuração do Projeto

##  1 - Configuração de ambiente

- Fazer download e instalar a ferramenta [Python](https://www.python.org/downloads/). Instale o interpretador Python 3 em seu computador. Este é o programa que lê programas em Python e executa suas instruções

- Em seguida instale a ferramenta Poetry, para gerenciamento de dependência e empacotamento em Python. Ele permite que você declare as bibliotecas das quais seu projeto depende e as gerenciará (instalará/atualizará) para você. 

    - O Poetry oferece um arquivo de bloqueio para garantir instalações repetíveis e pode criar seu projeto para distribuição (Poetry requer Python 3.7+). Realizar o clone do [repositorio Poetry](https://github.com/python-poetry/install.python-poetry.org). em seguida dar o seguinte comando no terminal: 

 `curl -sSL https://install.python-poetry.org | py -`

 ## 2 - Instalação de pacotes

- Usaremos o Streamlit para criação de app web interativo. Usamos o seguinte comando.

`poetry add streamlit`

- Usaremos também o pillow, para usarmos imagem no web app. Usaremos o seguinte comando para instalação.

`poetry add pillow`

## 3 Referências Streamlit

- Existem 3 informações importantes que você pode modificar.
1. `st.header(A)` é usado para especificar seu nome no lugar de **A**.
Exemplo:
```python
st.header('XPorcento')
```
2. `st.info(B)` é usado para especificar uma descrição rápida sobre oque é a empresa, o que ela faz, etc. no lugar de **B**.
Exemplo:
```python
st.info('Focada em resolver problemas na tomada de decisão.')
``` 

3. `st.button(D, E, F, G)` é uma função personalizada para criar botões de link onde **D** representa o ícone a ser exibido (use `youtube` se o botão play for exibido), **E** representa a URL, **F** representa a mensagem a ser exibida no botão clicável e **G** representa o tamanho do ícone.
Exemplo:
```python
st_button('youtube', 'https://youtube.com/dataprofessor', 'Data Professor YouTube channel', icon_size)
```

- Documentação [streamlit](https://docs.streamlit.io/).
- [Video](https://www.youtube.com/watch?v=Ie5ef_R_k6I&t=3986s) referência para alguns comandos.
- [Comunidade streamlit](https://discuss.streamlit.io/)

## 4 Uso do Github no projeto

- Abra o terminal de comando do seu sistema operacional;
Dentro da pasta do projeto, digite: `git init`
O comando acima irá criar toda a estrutura básica do repositório;

- Para adicionar todos os arquivos alterados à fila de atualizações do repositório, execute o comando: `git add`.

- Antes de sincronizar as alterações, configure seu usuário do GitHub com os comandos:
    `git config --global user.name "seu nome"`
    `git config --global "email no GitHub"`

- Confirme as alterações com o comando: 
    `git commit -m "mensagem"` 
no qual “mensagem” geralmente é um resumo das alterações.

- Adicione o remote, ou seja, o link para o servidor do seu projeto no GitHub:
    `git remote add origin usuário no GitHub>/<nome do repositório>.git`

- Por fim, envie as alterações com o comando:
    `git push remote origin`

## 5 Deploy no Streamlit

- Com o repositório criado no GitHub e o projeto estando nele, ir ao [site do streamlit](https://streamlit.io/) e realizar o login no mesmo. 
- Feito isso, ir em new app, colocar o repositório do GitHub ao qual esta o projeto, selecionar a branch que esta sendo utilizada e dizer qual o arquivo principal do projeto.
- Após, dar o deploy para o por no ar.







[]()