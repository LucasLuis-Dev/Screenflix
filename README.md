# 💻 Screenflix

<img src="https://cdn.discordapp.com/attachments/965066624556232737/1107091076357029999/Captura_de_tela_de_2023-05-13_20-44-03.png" >

## 📄 Descrição

O Screenflix é um projeto de cópia da Netflix feito com Django, Python e Tailwind CSS, que se trata de uma aplicação web que permite aos usuários assistir filmes e programas de TV em streaming. A aplicação tem uma interface semelhante à da Netflix, com uma página inicial mostrando os filmes e programas de TV em destaque, uma barra de pesquisa para procurar conteúdo específico e um sistema de criação de contas e cadastro, além de interações com o usuário. Assim como a Netflix, a aplicação mostra os filmes mais assistidos pelos usuários e os filmes já assistidos pelo usuário.

O Django foi utilizado para construir o backend da aplicação, que gerencia a lógica de negócios e interage com o banco de dados. O Python foi a linguagem principal usada no desenvolvimento do aplicativo, permitindo que o desenvolvedor escrevesse um código de forma rápida e eficiente.

O Tailwind CSS foi usado para criar o estilo da aplicação, tornando-a responsiva e visualmente atraente em diferentes tamanhos de tela.

Em resumo, o Screenflix feito com Django, Python e Tailwind CSS é uma aplicação web robusta e sofisticada, capaz de fornecer aos usuários uma experiência de visualização de conteúdo semelhante à popular plataforma de streaming de vídeo.


## 🎯 Tecnologias

- Python
- Django
- TailwindCSS
- HTML
- CSS
- JavaScript

## 📷 Fotos da Aplicação



<img src="https://cdn.discordapp.com/attachments/965066624556232737/1107091076357029999/Captura_de_tela_de_2023-05-13_20-44-03.png" >
<br>
<img src="https://cdn.discordapp.com/attachments/965066624556232737/1107501486260371457/Captura_de_tela_de_2023-05-14_23-09-43.png">
<br>
<img src="https://cdn.discordapp.com/attachments/965066624556232737/1107501449451143178/Captura_de_tela_de_2023-05-14_23-09-51.png">
<br>
<img src="https://cdn.discordapp.com/attachments/965066624556232737/1107501519273738351/Captura_de_tela_de_2023-05-14_23-34-05.png">
<br>
<img src="https://cdn.discordapp.com/attachments/965066624556232737/1107501598575435837/Captura_de_tela_de_2023-05-14_23-41-06.png">
<br>
<img src="https://cdn.discordapp.com/attachments/965066624556232737/1107501555978080307/Captura_de_tela_de_2023-05-14_23-40-48.png">
<br>
<img src="https://cdn.discordapp.com/attachments/965066624556232737/1107501695501598813/Captura_de_tela_de_2023-05-14_23-53-10.png">
<br>
<img src="https://cdn.discordapp.com/attachments/965066624556232737/1107501638945603695/Captura_de_tela_de_2023-05-14_23-41-27.png">
<br>
<img src="https://cdn.discordapp.com/attachments/965066624556232737/1107501667093594195/Captura_de_tela_de_2023-05-14_23-41-36.png">




# ScreenFlix - Guia de Instalação

## Pré-requisitos
- Python 3.x
- pip (gerenciador de pacotes Python)

## Passo a Passo de Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/LucasLuis-Dev/Screenflix.git
cd screenflix
```

### 2. Configure o Ambiente Virtual
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 3. Instale as Dependências
```bash
# Atualizar pip
pip install --upgrade pip

# Instalar Pillow primeiro
pip install Pillow==9.5.0

# Instalar demais dependências
pip install -r requirements.txt
```

### 4. Configure o Banco de Dados
```bash
python manage.py migrate
```

### 5. Crie um Superusuário
```bash
python manage.py createsuperuser
```
Siga as instruções para criar nome de usuário, email e senha.

### 6. Inicie o Servidor
```bash
python manage.py runserver
```

## Acessando a Aplicação
- Interface principal: `http://127.0.0.1:8000/`
- Painel administrativo: `http://127.0.0.1:8000/admin/`

## Comandos Úteis
- Parar o servidor: `Ctrl+C`
- Criar novas migrações: `python manage.py makemigrations`
- Aplicar migrações: `python manage.py migrate`

## Solução de Problemas
Se encontrar erro de acesso ao servidor, verifique se o `ALLOWED_HOSTS` no arquivo `settings.py` inclui:
```python
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
```

## Observações
- Mantenha o ambiente virtual ativado enquanto estiver trabalhando no projeto
- Para desativar o ambiente virtual quando terminar: `deactivate`
```
