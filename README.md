# De Bruijn graph
Implementação do grafo de Bruijn para aplicar na montagem de genoma.

A implementação foi feita em Python, funciona tanto em Python 2.x como 3.x.

O código da implementação é composto por três arquivos: fasta.py, kdmer.py, assembler.py.

O arquivo fasta.py ler um arquivo no formato FASTA.

O arquivo kdmer.py separa todos os kdmers retornando uma lista de mers.

O arquivo assembler.py é o arquivo principal que chama todos os outros. Ele espera que um parâmetro que é o arquivo de entrada. Exemplos com o formato do arquivo encontram-se na pasta "entradas".

Todos os arquivos de código estão devidamente comentados (em português).

Exemplo de chamada: python assembler.py entrada_grande

A execução gera os arquivos: 

kdmers.txt contendo todos os kdmers</br>
DeBruijn.txt com o grafo sendo representado através de lista de adjacência</br>
Eulerianos.txt contendo o caminho euleriano (se houver)</br>
sequencia_reconstruida.txt contendo a sequência reconstruída

Esse código foi testado com o problema do Rosalind chamado "String Reconstruction from Read-Pairs Problem".

Os arquivos utilizados como referência estão na pasta "referências".
