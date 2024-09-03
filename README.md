# PI3-2024 - AI FOOD -  Sistema de detecção de alimentos com inteligência artificial integrado com balança

**INSTITUTO FEDERAL DE SANTA CATARINA**

**Unidade Curricular:**  Projeto Integrador 3 

**Professor:**  Robinson Pizzio e Matheus Leitzke Pinto 

**Alunos:**  Eric Monteiro dos Reis e Matheus Sandim Gonçalves

* [Introdução](#Introdução)
* [Tecnologias utilizadas](#Tecnologias utilizadas)
* [Desenvolvimento e resultados](#Desenvolvimento e resultados)
* [Dificuldades](#Dificuldades)
  
## Introdução
Este projeto propõe a utilização de inteligência artificial (IA) para monitorar o consumo calórico diário dos usuários, para isso integra um modelo de IA com uma câmera de celular e uma balança, permitindo que os usuários identifiquem automaticamente os alimentos que consomem e, com base no peso detectado pela balança, obtenham informações nutricionais detalhadas, como a quantidade de proteínas, carboidratos e gorduras. Esses dados são então armazenados em um servidor, onde um resumo calórico é gerado para cada usuário, proporcionando um acompanhamento preciso e contínuo de sua dieta diária.

## Tecnologias utilizadas

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/Tecnologias%20do%20projeto%20.png)

A linguagem de programação que utilizamos foi o Python, devido à nossa familiaridade com ela e sua praticidade. Para treinar a IA, utilizamos o YOLOv8 (You Only Look Once version 8), que é um modelo de detecção de objetos onde a detecção e a classificação do objeto são realizadas em uma única etapa, tornando o algoritmo mais rápido no processamento de imagens.

A célula de carga utilizada é de 1KG (podendo ser substituída por uma de 3KG ou 5KG). Para a comunicação com o microcontrolador (ESP32), utilizamos o módulo HX711 (amplificador de 24 bits), pois, além de ser vendido junto com a célula de carga, ele conta com diversos exemplos e tutoriais disponíveis na internet. Com o intuito de facilitar a visualização durante o projeto dos valores medidos pela balança, bem como proporcionar maior conveniência ao usuário, implementamos um display LCD 16x2 com o módulo I2C.

A implementação do banco de dados foi realizada utilizando os serviços do Amazon RDS, devido ao convênio com o IFSC e à fácil disponibilidade de exemplos e documentação.

## Desenvolvimento e resultados
O desenvolvimento da balança e do dataset da IA foram realizados em paralelo. O dataset consiste em 1500 imagens de 15 alimentos sendo que 70 para treinamento, 20 para validação do treinamento e 10 para teste. Observa-se a seguir os resultados do treinamento da IA, reconhecendo o alimento apresentado na maior parte das tentativas, apesar de algumas vezes ele não reconhecer ou confundir com outro alimento do treinamento. 

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/resultado.jpg)

A figura abaixo apresenta a balança em pleno funcionamento, restando apenas implementar o envio do peso medido por meio de conexão WIFI

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/Balan%C3%A7a%20funcionando.png)

## Dificuldades 
O nosso dataset ficou grande (muitas opções de alimentos), mas deveriamos ter colocado mais imagens de cada alimentos, pois 
