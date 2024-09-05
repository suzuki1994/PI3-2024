# PI3-2024 - AI FOOD -  Sistema de detecção de alimentos com inteligência artificial integrado com balança

**INSTITUTO FEDERAL DE SANTA CATARINA**

**Unidade Curricular:**  Projeto Integrador 3 

**Professor:**  Robinson Pizzio e Matheus Leitzke Pinto 

**Alunos:**  Eric Monteiro dos Reis e Matheus Sandim Gonçalves

[Introdução](#introdução)
[Tecnologias utilizadas](#tecnologias-utilizadas)

  * [Python](#Python)
  * [YOLOv8](#YOLOv8)
  * [MicroPython](#MicroPython)
  * [AmazonRDS](#Amazon-RDS)
    
[Hardware](#Hardware)
[Desenvolvimento e resultados](#Desenvolvimento-e-resultados)
[Dificuldades](#Dificuldades)
[Passos Futuros](#Passos-futuros)
  
## Introdução
Este projeto propõe a utilização de inteligência artificial (IA) para monitorar o consumo calórico diário dos usuários, para isso integra um modelo de IA com uma câmera de celular e uma balança, permitindo que os usuários identifiquem automaticamente os alimentos que consomem e, com base no peso detectado pela balança, obtenham informações nutricionais detalhadas, como a quantidade de proteínas, carboidratos e gorduras. Esses dados são então armazenados em um banco de dados na nuvem, onde um resumo calórico é gerado para cada usuário, proporcionando um acompanhamento preciso e contínuo de sua dieta diária.

## Tecnologias utilizadas

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/Tecnologias.png)

### Python
Python é uma linguagem de programação de software muitas vezes utilizadas amplamente utilizada em diversas áreas, como desenvolvimento de software, automação de tarefas, análise de dados, aprendizado de máquina, etc. É uma linguagem de propósito geral conhecida pela sua sintaxe simples e fácil de ler, pois se assemelha muito a linguagem natural. Sua versatilidade e facilidade de prototipação rápida faz com que ela seja uma das linguagens de programação mais utilizadas da atualidade.

### YOLOv8
YOLOv8 (You Only Look Once version 8) é um algoritmo de detecção de objetos em imagens. Embora o YOLOv8 não seja a versão mais recente, ele foi selecionado para este projeto devido à ampla disponibilidade de tutoriais e exemplos práticos, além de sua comprovada eficiência e rapidez na detecção de objetos em vídeos.

### MicroPython
MicroPython é uma implementação enxuta da linguagem Python projetada para rodar em microcontroladores e dispositivos embarcados com recursos limitados, como ESP32 e ESP8266. MicroPython oferece acesso a hardware, como pinos GPIO, sensores, e comunicação Wi-Fi, e inclui bibliotecas para tarefas comuns em sistemas embarcados.

### Amazon RDS
O Amazon RDS (Relational Database Service) é um serviço gerenciado da AWS que facilita a configuração, operação e escalabilidade de bancos de dados relacionais na nuvem. O RDS automatiza tarefas como backup, atualização de software, escalabilidade de hardware e recuperação de falhas, permitindo que os usuários se concentrem na otimização de suas aplicações.

# Hardware

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/Componentes.png)

O hardware deste projeto consiste em uma balança digital com comunicação via Wi-Fi. Ela funciona a partir do sinal enviado por uma célula de carga, que é um transdutor resistivo capaz de converter a força aplicada em um sinal elétrico. No GIF abaixo, é demonstrada a simulação do funcionamento da célula de carga, onde uma força peso é aplicada, causando uma leve compressão na parte superior do sistema. Isso gera um sinal elétrico, que é amplificado pelo módulo HX711. Esse sinal é então enviado para o microcontrolador ESP32.

![](https://www.toledobrasil.com/blob/upload/peso-padrao-2.gif)

O HX711 é um módulo conversor e amplificador de 24 bits que junto com uma célula de carga e um microcontrolador é possível montar uma balança digital. A célula de carga utilizada neste projeto é de uma 1KG, porém nada impede de substituir ela por uma de 3KG ou 5KG. Ambos foram escolhidos para este projeto por serem vendidos em forma de kit, oferecerem um bom custo-benefício e contarem com diversos exemplos e tutoriais disponíveis na internet.

![](https://github.com/suzuki1994/PI3-2024/blob/d35aea34d81d1e8f14764084d93dd8fd95840884/Figuras/Celula_de_carga.png)

O HX711 possui um lado que deve ser conectado com a célula de carga (E+ E- A- A+ B- B+), onde E+ (VCC fio vermelho) e E- (GND fio preto) e as saídas (A+ A-) e (B+ e B-), onde utilizamos as saídas A+ (fio verde) e A- (fio branco).
O outro lado onde tem os pinos (GND DT SCK VCC) são conectados com o microcontrolador (ESP32).
Neste projeto o pino 2 do ESP32 é o DT (data) e o pino 4 é o SCK (clock). Alimentação é 3.3V 

![](https://github.com/suzuki1994/PI3-2024/blob/282f6ae8c8375911f87fdac173b76ee60df269f3/Figuras/HX711.jpg)

Para melhor visualização do valor medido pela balança foi utilizado um display de LCD 16x2 com um módulo I2C para comunicar com o ESP32. Os pinos utilizados foram o 22 (SCL) e o pino 21 (SCA). Já possuiamos este display o que facilitou na sua escolha para o projeto.

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/LCD_16x2_m%C3%B3dulo_I2C.png)

A célula de carga foi montada em duas placas de plástico que foram recicladas de uma antiga placa, a figura abaixo podemos oberservar a visão lateral da balança 

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/Balan%C3%A7a%20side%20view.jpeg)

A figura abaixo mostra a balança em pleno funcionamento. Os dados são enviados para um IP por meio de uma conexão Wi-Fi. Para isso, o ESP32 foi programado para atuar como um servidor web (webserver).

![](https://github.com/suzuki1994/PI3-2024/blob/a0ba1a532e0eedd0a04ab466d8b57646ec022bbe/Figuras/Balan%C3%A7a_funcionando.png)

# Software

## Amazon RDS
Para a implementação do banco de dados utilizado no projeto, primeiro é necessário possuir uma conta no AWS. O RDS é um serviço que possui tiers gratuitos onde é possível criar bancos de dados de forma gratuita, porém dependendo da configuração utilizada ao criar o banco, o serviço pode possuir gastos relevantes.
Para a criação do banco foi utilizado uma conta do AWS educacional, obtida através de parceria com o IFSC. 

Para este projeto optamos pela utilização de um banco de dados relacional PostgreSQL, visto que é necessário o armazenamento da informação de diversas entidades, com elas se relacionando entre si. 

Para a implementação do projeto foi desenhado uma arquitetura de banco contendo 3 tabelas principais:
* Tabela de usuários
* Tabela de alimentos
* Tabela de alimentos consumidos

Na tabela de usuários foram 

## Desenvolvimento e resultados
 Para o treinamento da Inteligência Artificial (IA), foram selecionados os seguintes alimentos: Alface; Arroz; Banana; Batata; Carne vermelha; Cebola; Feijão; Carne de frango; Laranja; Leite; Maçã; Melancia; Morango; Ovo; Tomate 

Foram utilizadas imagens de diversas fontes para representar cada alimento. Para facilitar a organização, estabeleceu-se uma faixa numérica padronizada de 100 imagens por alimento, distribuídas da seguinte forma: 70 para treinamento, 20 para validação e 10 para teste. Para fazer as labels das imagens utilizamos o site do https://app.cvat.ai/. O número toral de imagens que foram uitilzadas foi de 1500, pois utilizamos 15 alimentos diferentes. 

As imagens utilizadas para o treinamento e validação continham labels indicando a presença e identificação do alimento. Já nas imagens de teste, os labels não estavam presentes, sendo a tarefa da IA localizar e identificar corretamente os alimentos.

Os gráficos a seguir ilustram os resultados obtidos com o melhor treinamento realizado:

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/F1_curva.png)

Mostra a pontuação F1 (média harmônica de precisão e recuperação) em diferentes limites de confiança. Um pico mais alto sugere melhor desempenho do modelo.

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/CFN.png)

Na diagonal principal, observa-se o quanto o algoritmo acertou na identificação dos alimentos. As cores mais claras indicam valores de predição mais baixos, resultantes de confusões com outros alimentos ou com o fundo da imagem. Exceto por maçã e cebola, os demais alimentos apresentaram uma precisão de pelo menos 70%, o que é uma média considerável. Podemos observar isso na prática na figura abaixo, onde a IA consegue reconhecer todos os alimentos apresentados.

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/teste_IA.png)

Outro aspecto relevante é a análise do último gráfico, que apresenta a precisão de cada alimento de forma numérica. Observa-se que, em alguns casos, a IA confunde alimentos entre si ou com o fundo da imagem. A confusão com o background (fundo) poderia ser mitigada caso imagens sem labels tivessem sido incluídas no treinamento.

![](https://github.com/suzuki1994/PI3-2024/blob/a0ba1a532e0eedd0a04ab466d8b57646ec022bbe/Figuras/resultado.jpg)



## Dificuldades 
Encontramos algumas dificuldades durante o projeto, algumas já resolvemos e outras deixaremos registradas para futuras atualizações. Na hora de integrar a balança com o software do projeto (enviar o valor medido por Wi-Fi), tivemos problemas com o IP do ESP32, que nem sempre era o mesmo ao se conectar à rede, tendo que assim ajustar o IP durante a primeira conexão com uma rede nova.

Em relação ao dataset, a IA confundia alguns alimentos visualmente semelhantes, como peito de frango com feijão, devido ao formato, ou leite com uma parede branca. Para mitigar esses problemas, treinamos o modelo com variações das imagens do dataset original, como rotações, alterações na claridade e no HUE das cores. Embora tenha havido melhorias, acreditamos que um dataset maior, incluindo imagens de background (imagens sem rótulo no treinamento), provavelmente aumentaria ainda mais a precisão da IA.

A principal dificuldade deste projeto foi implementar o banco de dados na AWS, pois tivemos que aprender essa tecnologia do zero, o que resultou em várias tentativas e erros.

## Passos futuros
* Fazer uma case para a balança
* Ter um IP fixo para a balança enviar os dados (quando muda o WI-FI ele muda o IP)
* Aumentar o dataset de treinamento
* Fazer uma interface para o usuário
