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

<h3> Insomnia </h3>

O Insomnia é uma ferramenta usada para testar APIs e atuar como cliente REST, simplificando o desenvolvimento de APIs. Com ele, os desenvolvedores podem criar, testar e depurar suas APIs de maneira eficiente, oferecendo suporte a diferentes métodos de requisição, autenticação, gerenciamento de variáveis e até mesmo a criação de fluxos de trabalho complexos.
</div>
</div>

<div id="Broker">
<h2> Broker e Dispositivos</h2>
<div align="justify">

Nessa seção, será apresentado a lógica de funcionamento do broker e dos dispositivos desenvolvidos.

<h3> Broker</h3>


O broker é uma tecnologia que desempenha o papel de intermediário na comunicação entre diferentes sistemas ou dispositivos. No contexto deste projeto, o broker foi utilizado como um mensageiro, atuando como um servidor centralizado onde os dispositivos e a aplicação do usuário se conectam para enviar e receber mensagens.

Para gerenciar esses dispositivos, o broker utiliza uma estrutura de dados que organiza todos os dispositivos com base em seus endereços IP, permitindo a diferenciação entre eles. Além disso, foram utilizados elementos de programação, como o uso de threads e cache de dados, para otimizar o desempenho do broker. Esses tópicos serão abordados em detalhes posteriormente.

Por ser uma figura central, o endereço IP do broker deve ser inserido em cada dispositivo para que eles possam se conectar ao servidor. No projeto, essa configuração é realizada no arquivo <code>config.py</code>. Para acessar esse arquivo, siga as instruções de execução do projeto.

As requisições do aplicação do usuário ao broker são feitas por meio de uma interface de API RESTful, que se comunica com os elementos do broker para gerenciar as conexões de cada dispositivo de forma eficiente.

No projeto, o broker é composto por três arquivos principais: o arquivo do servidor (<code>Server/__init__.py</code>), que contém os métodos de controle e gerenciamento do servidor; a API (<code>API.py</code>), responsável por utilizar as funções do servidor e criar os endpoints para acesso HTTP; e o arquivo principal (<code>__main__.py</code>), onde esses dois arquivos são inicializados. A distribuição dos arquivos no diretório do broker é mostrada na imagem.

<p align="center">
  <img src="img/dirBroker.png" width = "243" />
</p>
<p align="center"><strong>Organização de arquivos relacionados ao broker</strong></p>

<h3> Dispositivos</h3>
Para simular os dispositivos no ambiente de software, foram empregados dois dispositivos virtuais: um sensor de temperatura e umidade, e um veículo (carro). Aqui, exploraremos como esses dispositivos são controlados tanto localmente, por meio de sua interface de controle, quanto remotamente.
<h4> Sensor</h4>
Este dispositivo emula um sensor iot fictício, replicando o comportamento de um sensor real de temperatura e umidade. Em sua interface de controle, o sensor oferece o controle das seguintes características:


- **Controle de estado:** Permite ligar o sensor ou colocá-lo em modo de espera, que é essencialmente uma forma de desligamento parcial, mantendo-o pronto para ser ativado novamente;

- **Controle de dados:** Possibilita a alteração da temperatura (com controle de 5 a 60 °C) e da umidade (com controle de 20 a 80 por cento);

- **Controle de conectividade:** Facilita a conexão e desconexão do broker;
- **Visualização de dados:** Fornece informações como o endereço IP do dispositivo, o número de threads ativas e o registro de envio e recebimento de dados.

<p align="center">
  <img src="img/InterfaceSensor.png" width = "600" />
</p>
<p align="center"><strong>Inteface de controle do sensor</strong></p>

O sensor também é projetado para ser controlado remotamente. Através de comandos específicos, é possível alterar seus estados e também solicitar a transmissão de dados. Cada comando possui uma função específica e uma maneira distinta de resposta, detalhadas posteriormente. Segue abaixo uma tabela que apresenta cada um dos comandos disponíveis, sua forma de resposta (UDP ou TCP), e o protocolo padrão utilizado para chamá-lo via HTTP:

<div align="center">

| Comando     	      | Resposta  | Protocolo HTTP |
|--------------------|-----------|----------------|
| ligar  	           | TCP       | POST	          |
| desligar 	         | TCP       | POST	          |
| temperatura-atual	 | UDP       | GET	           |
| umidade-atual	     | UDP       | GET	           |
| reiniciar 	        | TCP       | POST	          |
| definir-nome       | TCP       | POST	          |

</div>

<p align="center">
<strong> Tabela com os comando remotos do sensor</strong> </p>

<h4> Carro </h4>
O Carro é responsável por simular um veículo IoT, replicando diversos comportamentos de um carro real. Em sua interface de controle, oferece funcionalidades semelhantes ao sensor, como controle de estado, controle de conectividade e visualização de dados. Além disso, inclui outras características:

- **Controle de dados:** Permite definir a velocidade de movimentação (de 0 a 220 km/h), o nível de bateria (de 0 a 100%), e a quantidade de gasolina (de 0 a 55 litros).
- **Controle de estados:** Possibilita travar e destravar as portas, selecionar a direção de movimentação (para frente, para trás e parar), iniciar o movimento, e ativar ou desativar o sensor de colisão.
- **Visualização de dados:** Apresenta a ficha técnica do carro, incluindo modelo e ano de fabricação, por exemplo. Quando em movimento, exibe a distância percorrida a partir do ponto de origem, juntamente com todos os atributos do veículo.

<p align="center">
  <img src="img/InterfaceCarro.png" width = "800" />
</p>
<p align="center"><strong>Inteface de controle do Carro</strong></p>

O carro também é capaz de ser gerenciado remotamente, compartilhando características semelhantes ao sensor. Nesse contexto, uma tabela é apresentada para ilustrar os comandos de controle remoto do carro, indicando se a resposta é em UDP ou TCP, e qual protocolo HTTP é utilizado para acessá-los:

<div align="center">

| Comando             | Resposta               | Protocolo HTTP |
|---------------------|------------------------|----------------|
| ligar               | TCP                    | POST           |
| desligar            | TCP                    | POST           |
| get-velocidade      | UDP                    | GET            |
| definir-velocidade  | TCP                    | POST           |
| travar-porta        | TCP                    | POST           |
| destravar-porta     | TCP                    | POST           |
| ir-para-frente      | TCP                    | POST           |
| ir-para-tras        | TCP                    | POST           |
| parar               | TCP                    | POST           |
| iniciar-movimento   | TCP                    | POST           |
| ativar-buzina       | TCP                    | POST           |
| desativar-buzina    | TCP                    | POST           |
| medir-distancia     | UDP                    | GET            |
| status              | UDP                    | GET            |
| get-gasolina        | UDP                    | GET            |
| get-bateria         | UDP                    | GET            |
| get-colisao         | UDP                    | GET            |

</div>

<p align="center">
<strong> Tabela com os comando remotos do carro </strong> </p>

<h4>Organização do código</h4>

No projeto, os dispositivos seguem uma lógica semelhante de organização. Cada dispositivo é representado por uma classe que encapsula os métodos de comunicação direta com o broker, como envio, recebimento e conexão (`ConnectionDevice.__init__.py`). Além disso, existe um arquivo de comunicação (`Communication.py`) que controla os envios a partir das requisições do broker, lidando com as peculiaridades de comunicação de cada dispositivo.

No âmbito da lógica de negócios, dentro de cada pasta de dispositivo, encontramos uma classe com o nome correspondente ao dispositivo (por exemplo, `Car.__init__.py` ou `Sensor.__init__.py`). Essas classes são responsáveis por definir o comportamento específico de cada dispositivo.

Finalmente, há as classes de interface de usuário (`User.py`) e visualização (`View.__init__.py`), que são encarregadas de lidar com as impressões e entradas relacionadas a cada dispositivo.

O arquivo principal (`__main__.py`) atua como o ponto de entrada do programa, coordenando e integrando todos os outros arquivos e funcionalidades. As proximas imagens mostram a árvore de diretorios e arquivos dos dispositivos:
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
