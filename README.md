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
<h2> Softwares Utilizadas</h2>
<div align="justify">

Nesta seção, são apresentados os softwares utilizados durante o desenvolvimento do projeto.

<h3> Linguagem Python</h3>
A linguagem Python foi escolhida devido à sua facilidade de aprendizado e flexibilidade. 
Sua sintaxe limpa e legível permite a rápida prototipagem de ideias e o desenvolvimento ágil de aplicações. 
Além disso, Python é reconhecido pela sua vasta gama de bibliotecas e frameworks que facilitam o desenvolvimento 
em diversas áreas. É importante ressaltar que a versão utilizada foi a 3.12.2.

<h3> Biblioteca Flask</h3>
A biblioteca Flask é um módulo para construção de aplicações web em Python. Ela oferece flexibilidade 
para o desenvolvimento de APIs, permitindo a criação de endpoints RESTful e o gerenciamento de rotas HTTP.

<h3> Biblioteca Requests</h3>
A biblioteca Requests é uma ferramenta para fazer requisições HTTP em Python. Ela oferece uma 
interface que simplifica o processo de envio e recebimento de dados pela internet, tornando a 
comunicação com APIs mais eficiente.

<h3> Docker</h3>
O Docker é uma plataforma de implantação e execução de aplicativos em contêineres. 
Um contêiner é uma unidade leve e portátil que inclui tudo o que um aplicativo precisa 
para ser executado de forma independente, como código, bibliotecas, dependências e configurações.
O Docker oferece uma plataforma consistente para desenvolver, testar e implantar aplicativos, 
garantindo que os ambientes de desenvolvimento e produção sejam consistentes e reproduzíveis.

<h3>IDE PyCharm</h3>
A IDE PyCharm é um ambiente de desenvolvimento integrado projetado especificamente para Python. O PyCharm oferece uma ampla gama de recursos para aumentar a produtividade dos desenvolvedores, incluindo realce de sintaxe avançado, completamento automático de código, depuração integrada e suporte para controle de versão. Além disso, o PyCharm possui integração com o Docker, facilitando o desenvolvimento e a implantação de aplicativos Python em diversos ambientes.

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

    docker build -t broker -f Dockerfile_broker .
    docker build -t car -f Dockerfile_car .
    docker build -t sensor -f Dockerfile_sensor .
    docker build -t user -f Dockerfile_user .

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
