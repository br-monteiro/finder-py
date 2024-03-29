# Finder.py [![Unit Tests](https://github.com/br-monteiro/finder-py/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/br-monteiro/finder-py/actions/workflows/test.yml)
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

É possível melhorar o resultado de busca passando alguns argumentos especiais para o `CLI`.

>__IMPORTANTE__: A busca será realizada em arquivos e diretórios com permissão de leitura. Caso contrário, o arquivo/diretório será ignorado no processo.

### Argumentos

| Nome             | Tipo          | Exemplo                                                              | Descrição                                                                                                                                                                                                    |
|------------------|---------------|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **by**               | String, RegEx | by=level-3<br>by="abc 123"<br>by=level-\\\d<br>by="fn(value) {"<br>by="fn(\\$value) {"                           | Informa o termo a ser buscado nos arquivos.                                                                                                                                                                   |
| **-raw**     | ---           | -raw                                                         | Informa ao `CLI` para considerar o valor bruto do argumeto **by**.<br>Dessa forma, por exemplo, o termo de busca `"fn(value) {"` não é tratado como uma `RegEx`.<br>_É importante ter cuidado com o caractere `$` pois o mesmo é interpretado pelo terminal como uma variável de ambiente.<br>Para considerá-lo, é necessário escapar desta forma `\$`._ |
| **path**             | String        | path=/home/edsonmonteiro/                                            | Informa o path em que o `CLI` realizará busca.<br>Por padrão, a busca será realizada no diretório atual.                                                                                                       |
| **-recursive**<br>**-r** | ---           | -recursive<br>-r                                                     | Informa ao `CLI` para realizar a busca no diretório atual<br>e subdiretórios.<br>Por padrão, o nível de recursividade é 3.                                                                                              |
| **rl**<br><br>**recursive-level**  | Integer       | rl=4<br><br>recursive-level=5                                                    | Altera o nível máximo de subdiretórios em que o `CLI` realizará a busca.                                                                                                                                    |
| **fm**<br><br>**file-match**       | RegEx         | fm="template-*"<br><br>file-match=\\\d-abc                                                   | Informa ao `CLI` para realizar a busca do termo<br>apenas em arquivos onde a RegEx é satisfeita usando como base o nome do arquivo.                                                                                                               |
| **fdm**<br><br>**file-dont-match**  | RegEx         | fdm=".*min\\\\.js"<br><br>file-match=\\\d-abc                                                   | Informa ao `CLI` para **ignorar** a busca do termo<br>apenas em arquivos que a RegEx for satisfeita usando como base o nome do arquivo.                                                                                                            |
| **pm**<br><br>**path-match**       | RegEx         | pm="src\|public"<br><br>path-match=\\\d-abc                                                   | Informa ao `CLI` para realizar a busca do termo apenas<br>quando a RegEx for satisfeita usando como base o path completo do arquivo/diretório.                                                                                                                       |
| **pdm**<br><br>**path-dont-match**  | RegEx         | pdm="node_modules\|dist"<br><br>path-dont-match=node_modules<br>path-dont-match="node_modules\|dist" | Informa ao `CLI` para **ignorar** a busca do termo quando<br>a RegEx for satisfeita usando como base o path completo do arquivo/diretório.                                                                                                                                |
| **oe**<br><br>**only-extension**   | String        | oe=php,js<br><br>only-extension=js<br>only-extension=js,py                            | Informa ao `CLI` para realizar a busca apenas em arquivos<br>com a extensão informada.                                                                                                                          |
| **ee**<br><br>**except-extension** | String        | ee=json,md<br><br>except-extension=md<br>except-extension=json,java                    | Informa ao `CLI` para **ignorar** a busca em arquivos com a<br>extensão informada.                                                                                                                                  |
| **-quiet**<br>**-q**     | ---           | -quiet<br>-q                                                         | Informa ao `CLI` para não exibir as informações de **tempo de execução, arquivos consultados, quantidade de linhas com o termo de busca** e **quantidade de arquivos ou diretórios pulados** no processo. |
| **--help**     | ---           | --help                                                         | Mostra uma descrição dos comandos suportados e alguns exemplos no terminal. |

> A principal diferença entre [**fm, fdm, file-match, file-dont-match**] e [**pm, pdm, path-match, path-dont-match**] é que
> **file**-* cosidera apenas o nome dos arquivos e **path**-* considera o path completo do arquivo ou diretório

### Tests
Para rodar os tests, basta executar o comando =)

```bash
python3 -m unittest -v
```

### Créditos
Este projeto foi desenvolvido por Edson B S Monteiro - <bruno.monteirodg@gmail.com> em uma distribuição Linux. __\o/__

## LAUS DEO ∴
