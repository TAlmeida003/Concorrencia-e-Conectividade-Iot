<h1 align="center">Internet das Coisas (IoT)</h1>
<h3 align="center">Projeto de Conexão de Dispositivos IoT através de Broker e API RESTful</h3>

<div align="justify"> 
<div id="sobre-o-projeto"> 
<h2> Descrição do Projeto</h2>

</div>
</div>

<h2> Autor <br></h2>
<uL>
  <li><a href="https://github.com/TAlmeida003">Thiago Neri dos Santos Almeida</a></li>
</ul>

<h1 align="center"> Sumário </h1>
<div id="sumario">
	<ul>
        <li><a href="#requisitos"> Requisitos de Implementação do Projeto </a></li>
        <li><a href="#Software"> Tecnologias Utilizadas </a></li>
        <li><a href="#Broker"> Broker e Dispositivos </a></li>
        <li><a href="#Conectividade"> Interface de Rede </a></li>
        <li><a href="#API"> API RESTful </a></li>
        <li><a href="#logica"> Lógica de Funcionamento do Projeto</a></li>
        <li><a href="#usuario"> Demostração da Aplicação</a></li>
        <li><a href="#conclusao"> Conclusão </a></li>
        <li><a href="#execucaoProjeto"> Execução do Projeto </a></li>
        <li><a href="#referencias"> Referências </a></li>
	</ul>	
</div>

<div id="requisitos"> 
<h2> Requisitos de Implementação do Projeto</h2>
<div align="justify"> 

</div>
</div>

<div id="Software">
<h2> Tecnologias Utilizadas</h2>
<div align="justify">

</div>
</div>

<div id="Broker">
<h2> Broker e Dispositivos</h2>
<div align="justify">

</div>
</div>

<div id="Conectividade">
<h2> Interface de Rede</h2>
<div align="justify">

</div>
</div>

<div id="API">
<h2> API RESTful</h2>
<div align="justify">

</div>
</div>

<div id="logica">
<h2> Lógica de Funcionamento do Projeto</h2>
<div align="justify">

</div>
</div>

<div id="usuario">
<h2> Demostração da Aplicação</h2>
<div align="justify">

</div>
</div>

<div id="conclusao">
<h2> Conclusão</h2>
<div align="justify">
</div>
</div>

<div id="execucaoProjeto">
<h2> Execução do Projeto</h2>
<div align="justify">

Este projeto pode ser executado tanto utilizando Docker quanto sem ele. Siga as instruções abaixo para ambas as opções:

<h3> Sem Docker </h3>
Para executar o projeto sem Docker, siga estes passos:

**Passo 1: Clonar o Repositório**

Abra o terminal e execute o seguinte comando para obter o código do repositório:

    git clone https://github.com/TAlmeida003/Concorrencia-e-Conectividade-Iot.git

**Passo 2: Acessar o Diretório do Projeto**
Navegue para o diretório clonado:

    cd Concorrencia-e-Conectividade-Iot

**Passo 3: Instalar as Dependências**

Execute o seguinte comando para instalar as dependências do projeto:

    pip install Flask
    pip install requests

**Passo 4: Executar os Projetos**

Execute o seguinte comando para iniciar o broker:

        python3 ./src/Broker
Após iniciar o broker, obtenha o endereço IP e edite o arquivo de configuração localizado em <code>src/config.py</code> e insira o endereço IP do broker na variável HOST.

Execute os seguintes comandos para iniciar os dispositivos e a aplicação de controle dos dispositivos:

    python3 ./src/Devices/Car
    python3 ./src/Devices/Sensor
    python3 ./src/User

<h3> Docker </h3>

Para executar o projeto usando Docker, seja através do Dockerfile ou do pull, siga as instruções abaixo:

<h4> Dockerfile:</h4>
Os Dockerfile necessários para construir as imagens Docker estão disponíveis no repositório. Para construir as
imagens Docker, execute os passos 1 e 2 e configure o endereço IP no arquivo <code>config.py</code> e os
seguintes comandos:

    docker build -t broker Dockerfile_broker .
    docker build -t car Dockerfile_car .
    docker build -t sensor Dockerfile_sensor .
    docker build -t user Dockerfile_user .

Após construir as imagens Docker, execute o seguinte comando para iniciar os containers Docker:

    docker run -iti --name user user
    docker run -iti --name car car
    docker run -iti --name sensor sensor
    docker run -iti --name broker broker --network  host

<h4> Docker Pull: </h4>
Para obter a imagem Docker pré-construída, execute o seguinte comando:

    docker pull talmeida003/concorrencia-e-conectividade-iot:broker
    docker pull talmeida003/concorrencia-e-conectividade-iot:car
    docker pull talmeida003/concorrencia-e-conectividade-iot:sensor
    docker pull talmeida003/concorrencia-e-conectividade-iot:user

Após obter as imagens Docker, execute o seguinte comando para iniciar os containers Docker:

    docker run -p talmeida003/concorrencia-e-conectividade-iot:broker --network host
    docker run -p talmeida003/concorrencia-e-conectividade-iot:car
    docker run -p talmeida003/concorrencia-e-conectividade-iot:sensor
    docker run -p talmeida003/concorrencia-e-conectividade-iot:user

</div>
</div>

<div id="referencias">  
<h2> Referências</h2>
<div align="justify">

</div>
</div>
