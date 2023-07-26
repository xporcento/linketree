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

## 1. Configurar ambiente

Nesta seção, vamos configurar o ambiente de desenvolvimento para o projeto. Você pode incluir instruções sobre a instalação de um ambiente virtual, configuração de variáveis de ambiente e outras dependências necessárias.

## 2. Instalar pacotes

Aqui, vamos listar os pacotes e bibliotecas específicas que precisam ser instalados para o projeto. Inclua os comandos de instalação, por exemplo, usando pip ou conda.

## 3. Referências do Streamlit

Nesta parte, você pode incluir links para documentação, tutoriais ou recursos relevantes sobre o Streamlit. Isso ajudará a equipe a aprender e entender como usar o Streamlit para criar a aplicação.

## 4. Uso do Github no projeto

Nesta seção, explique como a equipe pode utilizar o GitHub para colaborar no projeto. Você pode abordar tópicos como controle de versão, criação de branches, fluxo de trabalho de pull requests, entre outros.

## 5. Deploy no Streamlit

Aqui, você pode descrever como realizar o deploy da aplicação Streamlit em um ambiente de produção. Inclua etapas como configuração de servidores, ajustes finos de desempenho e segurança, e qualquer outra informação relevante.

## 6. Desenvolvendo em equipe no Github

Nesta seção, você pode fornecer orientações sobre como a equipe pode colaborar de forma eficiente no desenvolvimento do projeto usando o GitHub. Inclua práticas recomendadas, como comunicação, revisão de código e gerenciamento de problemas.










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

- Utilizaremos o GitHub para gerenciar e controlar o projeto.







[]()