# De Bruijn Graph
Implementação do grafo de Bruijn para aplicar na remontagem de genoma.

A implementação foi feita em Python, funciona tanto em Python 2.x como 3.x.

O código da implementação é composto por três arquivos: fasta.py, kdmer.py, assembler.py.

O arquivo fasta.py ler um arquivo no formato FASTA.

O arquivo kdmer.py separa todos os (k,d)-mers retornando uma lista de mers.

O arquivo assembler.py é o arquivo principal que chama todos os outros. Ele espera um parâmetro que é o caminho do arquivo de entrada. Exemplos com o formato desse arquivo de entrada encontram-se na pasta "entradas" cujos nomes são "entrada1" e "entrada2". São arquivos onde a primeira linha tem-se os parâmetros "k" e "d" e a segunda linha possui a sequência que será remontada.

Todos os arquivos de código estão devidamente comentados (em português).

Exemplo de chamada: python assembler.py arquivo_de_entrada

Onde arquivo_de_entrada é o caminho para o arquivo de entrada.

A execução gera os arquivos: 

kdmers.txt contendo todos os kdmers</br>
DeBruijn.txt com o grafo sendo representado através de lista de adjacência</br>
Eulerianos.txt contendo o caminho euleriano (se houver)</br>
sequencia_reconstruida.txt contendo a sequência reconstruída (remontada)

Esse código foi testado com o problema do Rosalind chamado "String Reconstruction from Read-Pairs Problem": [http://rosalind.info/problems/4i/](http://rosalind.info/problems/4i/)

O problema do Rosalind já fornece os (k,d)-mers. Para utilizar o programa para resolver esse problema do Rosalind basta fazer:

python assembler.py arquivo_rosalind rosalind

Esse "arquivo_rosalind" espera um arquivo no formato de entrada do problema do Rosalind. Exemplos desse formato encontra-se na pasta "entradas" com o nome "entrada_rosalind1" e "entrada_rosalind2".

A execução acima gerará apenas o arquivo "sequencia_reconstruida.txt"

Todos os arquivos com terminação "txt" são ignorados para no repositório.

Os arquivos utilizados como referência estão na pasta "referencias".
