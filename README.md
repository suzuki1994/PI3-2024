# PI3-2024 - AI FOOD -  Sistema de detecção de alimentos com inteligência artificial integrado com balança

**INSTITUTO FEDERAL DE SANTA CATARINA**

**Unidade Curricular:**  Projeto Integrador 3 

**Professor:**  Robinson Pizzio e Matheus Leitzke Pinto 

**Alunos:**  Eric Monteiro dos Reis e Matheus Sandim Gonçalves
  
## Introdução
Este projeto propõe a utilização de inteligência artificial (IA) para monitorar o consumo calórico diário dos usuários, para isso integra um modelo de IA com uma câmera de celular e uma balança, permitindo que os usuários identifiquem automaticamente os alimentos que consomem e, com base no peso detectado pela balança, obtenham informações nutricionais detalhadas, como a quantidade de proteínas, carboidratos e gorduras. Esses dados são então armazenados em um servidor, onde um resumo calórico é gerado para cada usuário, proporcionando um acompanhamento preciso e contínuo de sua dieta diária.

## Tecnologias utilizadas

![](https://github.com/suzuki1994/PI3-2024/blob/a0ba1a532e0eedd0a04ab466d8b57646ec022bbe/Figuras/Tecnologias_do_projeto.png)

No decorrer deste README iremos citar estas tecnologias utilizadas e o porque elas foram escolhidas

# YOLO

YOLOv8 (You Only Look Once version 8) é um algoritmo de detecção de objetos em imagens. Embora o YOLOv8 não seja a versão mais recente, ele foi selecionado para este projeto devido à ampla disponibilidade de tutoriais e exemplos práticos, além de sua comprovada eficiência e rapidez na detecção de objetos em vídeos. Para o treinamento da Inteligência Artificial (IA), foram selecionados os seguintes alimentos: Alface; Arroz; Banana; Batata; Carne vermelha; Cebola; Feijão; Carne de frango; Laranja; Leite; Maçã; Melancia; Morango; Ovo; Tomate 

Foram utilizadas imagens de diversas fontes para representar cada alimento. Para facilitar a organização, estabeleceu-se uma faixa numérica padronizada de 100 imagens por alimento, distribuídas da seguinte forma: 70 para treinamento, 20 para validação e 10 para teste. Para fazer as labels das imagens utilizamos o site do https://app.cvat.ai/. O número toral de imagens que foram uitilzadas foi de 1500, pois utilizamos 15 alimentos diferentes. 

As imagens utilizadas para o treinamento e validação continham labels indicando a presença e identificação do alimento. Já nas imagens de teste, os labels não estavam presentes, sendo a tarefa da IA localizar e identificar corretamente os alimentos.

Os gráficos a seguir ilustram os resultados obtidos com o melhor treinamento realizado:

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/F1_curva.png)

Mostra a pontuação F1 (média harmônica de precisão e recuperação) em diferentes limites de confiança. Um pico mais alto sugere melhor desempenho do modelo.

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/CFN.png)

Na diagonal principal, observa-se o quanto o algoritmo acertou na identificação dos alimentos. As cores mais claras indicam valores de predição mais baixos, resultantes de confusões com outros alimentos ou com o fundo da imagem. Exceto por maçã e cebola, os demais alimentos apresentaram uma precisão de pelo menos 70%, o que é uma média considerável. Podemos observar isso na prática na figura abaixo, onde a IA consegue reconhecer todos os alimentos apresentados.

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/teste_IA.png)

Outro aspecto relevante é a análise do último gráfico, que apresenta a precisão de cada alimento de forma numérica. Observa-se que, em alguns casos, a IA confunde alimentos entre si ou com o fundo da imagem. A confusão com o background (fundo) poderia ser mitigada caso imagens sem labels tivessem sido incluídas no treinamento.

# Hardware
A célula de carga utilizada é de 1KG (podendo ser substituída por uma de 3KG ou 5KG). Para a comunicação com o microcontrolador (ESP32), utilizamos o módulo [HX711](Balança/HX711)(amplificador de 24 bits), pois, além de ser vendido junto com a célula de carga, ele conta com diversos exemplos e tutoriais disponíveis na internet. Com o intuito de facilitar a visualização durante o projeto dos valores medidos pela balança, bem como proporcionar maior conveniência ao usuário, implementamos um display [LCD](Balança/LCD) 16x2 com o módulo I2C.

A implementação do banco de dados foi realizada utilizando os serviços do Amazon RDS, devido ao convênio com o IFSC e à fácil disponibilidade de exemplos e documentação.

## Desenvolvimento e resultados
O desenvolvimento da [balança](Balança) e do dataset da IA foi realizado em paralelo. O dataset consiste em 1.500 imagens de 15 alimentos, com 70% das imagens destinadas ao treinamento, 20% à validação e 10% aos testes. A seguir, observam-se os resultados do treinamento da IA, que reconheceu corretamente o alimento apresentado na maioria das tentativas. No entanto, em algumas ocasiões, a IA não conseguiu reconhecer ou confundiu o alimento com outro presente no treinamento.



![](https://github.com/suzuki1994/PI3-2024/blob/a0ba1a532e0eedd0a04ab466d8b57646ec022bbe/Figuras/resultado.jpg)

A figura abaixo mostra a balança em pleno funcionamento. O próximo passo foi implementar o envio do peso medido por meio de conexão Wi-Fi.

![](https://github.com/suzuki1994/PI3-2024/blob/a0ba1a532e0eedd0a04ab466d8b57646ec022bbe/Figuras/Balan%C3%A7a_funcionando.png)


##colocar a parte do AWS


## Dificuldades 
Encontramos algumas dificuldades durante o projeto, algumas já resolvemos e outras deixaremos registradas para futuras atualizações. Na hora de integrar a balança com o software do projeto (enviar o valor medido por Wi-Fi), tivemos problemas com o IP do ESP32, que nem sempre era o mesmo ao se conectar à rede, tendo que assim ajustar o IP durante a primeira conexão com uma rede nova.

Em relação ao dataset, a IA confundia alguns alimentos visualmente semelhantes, como peito de frango com feijão, devido ao formato, ou leite com uma parede branca. Para mitigar esses problemas, treinamos o modelo com variações das imagens do dataset original, como rotações, alterações na claridade e no HUE das cores. Embora tenha havido melhorias, acreditamos que um dataset maior, incluindo imagens de background (imagens sem rótulo no treinamento), provavelmente aumentaria ainda mais a precisão da IA.

A principal dificuldade deste projeto foi implementar o banco de dados na AWS, pois tivemos que aprender essa tecnologia do zero, o que resultou em várias tentativas e erros.
