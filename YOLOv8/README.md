# Treinamento e Resultados da Inteligência Artificial

YOLOv8 (You Only Look Once version 8) é um algoritmo de detecção de objetos em imagens. Embora o YOLOv8 não seja a versão mais recente, ele foi selecionado para este projeto devido à ampla disponibilidade de tutoriais e exemplos práticos, além de sua comprovada eficiência e rapidez na detecção de objetos em vídeos. Para o treinamento da Inteligência Artificial (IA), foram selecionados os seguintes alimentos: Alface; Arroz; Banana; Batata; Carne vermelha; Cebola; Feijão; Carne de frango; Laranja; Leite; Maçã; Melancia; Morango; Ovo; Tomate 

Foram utilizadas imagens de diversas fontes para representar cada alimento. Para facilitar a organização, estabeleceu-se uma faixa numérica padronizada de 100 imagens por alimento, distribuídas da seguinte forma: 70 para treinamento, 20 para validação e 10 para teste. Para fazer as labels das imagens utilizamos o site do https://app.cvat.ai/  Os  Isso resultou em um total de 1500 imagens. O renomeio dos arquivos de imagem foi realizado de forma prática utilizando um algoritmo presente no arquivo "rename_image_files".

As imagens utilizadas para o treinamento e validação continham labels indicando a presença e identificação do alimento. Já nas imagens de teste, os labels não estavam presentes, sendo a tarefa da IA localizar e identificar corretamente os alimentos.

Os gráficos a seguir ilustram os resultados obtidos com o melhor treinamento realizado:

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/F1_curva.png)

Mostra a pontuação F1 (média harmônica de precisão e recuperação) em diferentes limites de confiança. Um pico mais alto sugere melhor desempenho do modelo.

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/CFN.png)

Na diagonal principal, observa-se o quanto o algoritmo acertou na identificação dos alimentos. As cores mais claras indicam valores de predição mais baixos, resultantes de confusões com outros alimentos ou com o fundo da imagem. Exceto por maçã e cebola, os demais alimentos apresentaram uma precisão de pelo menos 70%, o que é uma média considerável. Podemos observar isso na prática na figura abaixo.

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/resultado.jpg)

É importante ressaltar que as limitações na confiança da IA em reconhecer os alimentos estão associadas ao número reduzido de imagens utilizadas para cada categoria. Quanto maior o número de imagens disponíveis para o treinamento da IA, maior a precisão no reconhecimento dos objetos.

Outro aspecto relevante é a análise do último gráfico, que apresenta a precisão de cada alimento de forma numérica. Observa-se que, em alguns casos, a IA confunde alimentos entre si ou com o fundo da imagem. A confusão com o background (fundo) poderia ser mitigada caso imagens sem labels tivessem sido incluídas no treinamento.

Este estudo destaca a importância de um conjunto de dados robusto e diversificado para o desenvolvimento de modelos de IA com maior acurácia e confiabilidade.
