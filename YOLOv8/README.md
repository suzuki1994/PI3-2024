# Treinamento e Resultados da Inteligência Artificial

YOLOv8 (You Only Look Once version 8) é a mais recente iteração da popular família de modelos YOLO, amplamente utilizada em tarefas de detecção de objetos em tempo real. Desenvolvida para aprimorar a eficiência e precisão na identificação de objetos dentro de imagens e vídeos, YOLOv8 introduz melhorias na arquitetura de rede neural, oferecendo um balanceamento otimizado entre velocidade de processamento e acurácia de detecção.

O modelo YOLOv8 é caracterizado por sua abordagem "single-shot," onde a detecção e a classificação dos objetos são realizadas em uma única etapa, permitindo que o algoritmo processe imagens em alta velocidade, o que é crucial para aplicações em tempo real, como vigilância por vídeo, direção autônoma e robótica.

Embora o YOLOv8 não seja a versão mais recente, ele foi selecionado para este projeto devido à ampla disponibilidade de tutoriais e exemplos práticos, além de sua comprovada eficiência e rapidez na detecção de objetos em vídeos. Para o treinamento da Inteligência Artificial (IA), foram selecionados os seguintes alimentos, cada um com uma faixa numérica específica:
 * Alface (001 a 100)
 * Arroz (101 a 200)
 * Banana (201 a 300)
 * Batata (301 a 400)
 * Carne vermelha (401 a 500)
 * Cebola (501 a 600)
 * Feijão (601 a 700)
 * Carne de frango (701 a 800)
 * Laranja (801 a 900)
 * Leite (901 a 1000)
 * Maçã (1001 a 1100)
 * Melancia (1101 a 1200)
 * Morango (1201 a 1300)
 * Ovo (1301 a 1400)
 * Tomate (1401 a 1500)

Foram utilizadas imagens de diversas fontes para representar cada alimento. Para facilitar a organização, estabeleceu-se uma faixa numérica padronizada de 100 imagens por alimento, distribuídas da seguinte forma: 70 para treinamento, 20 para validação e 10 para teste. Isso resultou em um total de 1500 imagens. O renomeio dos arquivos de imagem foi realizado de forma prática utilizando um algoritmo presente no arquivo "rename_image_files".

As imagens utilizadas para o treinamento e validação continham labels indicando a presença e identificação do alimento. Já nas imagens de teste, os labels não estavam presentes, sendo a tarefa da IA localizar e identificar corretamente os alimentos.

Os gráficos a seguir ilustram os resultados obtidos com o melhor treinamento realizado:

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/F1_curva.png)

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/P_curva.png)

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/CFN.png)

É importante ressaltar que as limitações na confiança da IA em reconhecer os alimentos estão associadas ao número reduzido de imagens utilizadas para cada categoria. Quanto maior o número de imagens disponíveis para o treinamento da IA, maior a precisão no reconhecimento dos objetos.

Outro aspecto relevante é a análise do último gráfico, que apresenta a precisão de cada alimento de forma numérica. Observa-se que, em alguns casos, a IA confunde alimentos entre si ou com o fundo da imagem. A confusão com o background (fundo) poderia ser mitigada caso imagens sem labels tivessem sido incluídas no treinamento.

Este estudo destaca a importância de um conjunto de dados robusto e diversificado para o desenvolvimento de modelos de IA com maior acurácia e confiabilidade.
