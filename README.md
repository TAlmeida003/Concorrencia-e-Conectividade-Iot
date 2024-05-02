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
    <h2>Execução do Projeto</h2>
    <div align="justify">

Este projeto pode ser executado tanto utilizando Docker quanto sem ele. Siga as instruções abaixo para ambas as
opções:

<h3>Sem Docker</h3>
<p>Para executar o projeto sem Docker, siga estes passos:</p>

<p><strong>Passo 1: Clonar o Repositório</strong></p>
<p>Abra o terminal e execute o seguinte comando para obter o código do repositório:</p>
<code>git clone https://github.com/TAlmeida003/Concorrencia-e-Conectividade-Iot.git</code>

<p><strong>Passo 2: Acessar o Diretório do Projeto</strong></p>
<p>Navegue para o diretório clonado:</p>
<code>cd Concorrencia-e-Conectividade-Iot</code>

<p><strong>Passo 3: Instalar as Dependências</strong></p>
<p>Execute o seguinte comando para instalar as dependências do projeto:</p>
<code>pip install Flask</code><br>
<code>pip install requests</code>

<p><strong>Passo 4: Executar os Projetos</strong></p>
<p>Execute o seguinte comando para iniciar o broker:</p>
<code>python3 ./src/Broker</code>
<p>Após iniciar o broker, obtenha o endereço IP e edite o arquivo de configuração localizado em
    <code>src/config.py</code> e insira o endereço IP do broker na variável HOST.</p>
<p>Execute os seguintes comandos para iniciar os dispositivos e a aplicação de controle dos dispositivos:</p>
<code>python3 ./src/Devices/Car</code><br>
<code>python3 ./src/Devices/Sensor</code><br>
<code>python3 ./src/User</code>

<h3>Docker</h3>

<p>Para executar o projeto usando Docker, siga as instruções abaixo:</p>

<h4>Dockerfile:</h4>
<p>Os Dockerfile necessários para construir as imagens Docker estão disponíveis no repositório. Para construir as
    imagens Docker, execute os passos 1 e 2 e configure o endereço IP no arquivo <code>config.py</code> e os
    seguintes comandos:</p>
<code>docker build -t broker Dockerfile_broker .</code><br>
<code>docker build -t car Dockerfile_car .</code><br>
<code>docker build -t sensor Dockerfile_sensor .</code><br>
<code>docker build -t user Dockerfile_user .</code>
<p>Após construir as imagens Docker, execute o seguinte comando para iniciar os containers Docker:</p>
<code>docker run -iti --name user user</code><br>
<code>docker run -iti --name car car</code><br>
<code>docker run -iti --name sensor sensor</code><br>
<code>docker run -iti --name broker broker --network host</code>

<h4>Docker Pull:</h4>
<p>Para obter a imagem Docker pré-construída, execute o seguinte comando:</p>
<code>docker pull talmeida003/concorrencia-e-conectividade-iot:broker</code><br>
<code>docker pull talmeida003/concorrencia-e-conectividade-iot:car</code><br>
<code>docker pull talmeida003/concorrencia-e-conectividade-iot:sensor</code><br>
<code>docker pull talmeida003/concorrencia-e-conectividade-iot:user</code>
<p>Após obter as imagens Docker, execute o seguinte comando para iniciar os containers Docker:</p>
<code>docker run -p talmeida003/concorrencia-e-conectividade-iot:broker --network host</code><br>
<code>docker run -p talmeida003/concorrencia-e-conectividade-iot:car</code><br>
<code>docker run -p talmeida003/concorrencia-e-conectividade-iot:sensor</code><br>
<code>docker run -p talmeida003/concorrencia-e-conectividade-iot:user</code>

</div>
</div>


<div id="referencias">  
<h2> Referências</h2>
<div align="justify">

</div>
</div>
