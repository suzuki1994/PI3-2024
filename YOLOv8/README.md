# Arquivos relacionados ao treinamento da IA e resultados 


Para o treinamento da IA foram selecionados os seguintes alimentos:
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

Foi utilizadas fotos de alimentos de diversas fontes, para melhor organizalas foi padronizado uma faixa de numeração para cada alimento, onde cada um tem 100 imagens, nas quais 70 de treinamento, 20 de validação e 10 de teste. Totalizando assim 1500 imagens. Para renomear os arquivos de forma prática utilizamos do algoritimo presente no arquivo "rename_image_files"

As imagens da parte de treinamento e validação possuem os labels de onde e qual alimento está presente da imagem. Nas imagens de teste elas não possuem os labels, pois é a IA que deve localizar o alimento e o identifica-lo.

Os gráficos a seguir foram obtidos com o nosso melhor treinamento

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/F1_curva.png)

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/P_curva.png)

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/CFN.png)

Vale a pena salientar que as limitações na confiaça da IA em reconhecer os alimentos se deve termos escolhido "poucas" imagens para cada categoria, quanto mais imagens é utilizado no treinamento da IA melhor a precisão em reconhecer objetos.

Outro ponto que vale a pena citar é em relação ao último gráfico, pois nele mostra a precisão de cada alimento de maneira númerica,algumas vezes a IA confunde um alimento com o outro ou com o fundo da imagem.O background (fundo) é um erro que pode ser diminuido se tivessemos colocado imagens sem label durante o treinamento. 
