# Finder.py
Um simples `CLI` para ajudar a encontrar aquele maldito texto que só Deus sabe onde está =)<br>
Esta ferramenta foi desenvolvida com Python3, Coca-Cola e Cup Noodles

### Dependências
- Python 3.5.2+

### Instalação
Para instalar a ferramenta na sua máquina, basta realizar o clone deste repositório.<br>
Abaixo é possível visualizar o comando de clone do repositório:

```bash
cd ~/ && git clone git@github.com:br-monteiro/finder-py.git
```

Após clonar o projeto, entre no diretório `finder-py` e execute o arquivo de `setup`.<br>
Abaixo é possível visualizar o comando de execução do arquivo de setup:

```bash
cd ~/finder-py && bash ./setup.sh
```

>__IMPORTANTE__: Será solicitado a senha de root do Sistema Operacional, mas não se preocupe, esta solicitação servirá apenas para setar permissão de execução (`+x`) e criação do _link simbólico_ (`ln -s`) para o arquivo `finder.py`.

### Usando a ferramenta
O uso desta ferramenta é bem simples, e consiste em procurar um termo específico nos arquivos do diretóio atual (ou informado por argument).

O único comando obrigatório é o `by=<termo>`.
```bash
finder by=texto
```

É possível melhorar o resultado de busca passando alguns argumentos especials para o `CLI`.

### Argumentos

| Nome             | Tipo          | Exemplo                                                              | Descrição                                                                                                                                                                                                    |
|------------------|---------------|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **by**               | String, RegEx | by=level-3<br>by="abc 123"<br>by=level-\\\d                           | Informa o termo a ser buscado nos arquivos.                                                                                                                                                                   |
| **path**             | String        | path=/home/edsonmonteiro/                                            | Informa o path em que o CLI realizará busca.<br>Por padrão, a busca será realizada no diretório atual.                                                                                                       |
| **-recursive**<br>**-r** | ---           | -recursive<br>-r                                                     | Informa ao CLI para realizar a busca no diretório atual<br>e subdiretórios.<br>Por padrão, o nível de recursividade é 3.                                                                                              |
| **recursive-level**  | Integer       | recursive-level=5                                                    | Altera o nível máximo de subdiretórios em que o CLI realizará a busca.                                                                                                                                    |
| **file-match**       | RegEx         | file-match=\\\d-abc                                                   | Informa ao CLI para realizar a busca do termo<br>apenas em arquivos onde a RegEx é satisfeita.                                                                                                               |
| **file-dont-match**  | RegEx         | file-match=\\\d-abc                                                   | Informa ao CLI para **ignorar** a busca do termo<br>apenas em arquivos quando a RegEx for satisfeita.                                                                                                            |
| **path-match**       | RegEx         | path-match=\\\d-abc                                                   | Informa ao CLI para realizar a busca do termo apenas<br>quando a RegEx for satisfeita.                                                                                                                       |
| **path-dont-match**  | RegEx         | path-dont-match=node_modules<br>path-dont-match="node_modules\|dist" | Informa ao CLI para igorar a busca do termo quando<br>a RegEx for satisfeita.                                                                                                                                |
| **only-extension**   | String        | only-extension=js<br>only-extension=js,py                            | Informa ao CLI para realizar a busca apenas em arquivos<br>com a extensão informada                                                                                                                          |
| **except-extension** | String        | except-extension=md<br>except-extension=json,java                    | Informa ao CLI para **ignorar** a busca em arquivos com a<br>extensão informada                                                                                                                                  |
| **-quiet**<br>**-q**     | ---           | -quiet<br>-q                                                         | Informa ao CLI para não exibir as informações de **tempo de execução, arquivos consultados, quantidade de linhas com o termo de busca** e **quantidade de arquivos ou diretórios pulados** no processo. |

> A principal diferença entre [**file-match, file-dont-match**] e [**path-match, path-dont-match**] é que
> **file**-* cosidera apenas arquivos e **path**-* considera o path completo do arquivo

### Tests
Para rodar os tests, basta executar o comando =)

```bash
python3 -m unittest -v
```

### Créditos
Este projeto foi desenvolvido por Edson B S Monteiro - <bruno.monteirodg@gmail.com> em uma distribuição Linux. __\o/__

## LAUS DEO ∴
