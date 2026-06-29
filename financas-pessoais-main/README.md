# App de Finanças Pessoais 

É um programa para finanças pessoais onde você pode registrar despesas e receitas (o que entra e sai). Você pode categorizar suas finanças, visualizar o extrato, gerar relatórios e exportar tudo para um arquivo de texto. Todos os dados são salvos em JSON, então nada é perdido entre sessões.

## Como rodar

```bash
python financas.py
```

## Funcionalidades

- **Registrar lançamento** — informa tipo (receita ou despesa), valor, categoria e descrição; valida as entradas e salva imediatamente no arquivo JSON
- **Ver extrato** — lista todos os lançamentos registrados com data, tipo, categoria, valor formatado e descrição
- **Relatório** — exibe o total de receitas, total de despesas, saldo atual e um resumo de valores por categoria
- **Exportar relatório** — salva o conteúdo do relatório em `relatorio.txt` para consulta externa
- **Limpar lançamentos** — apaga todos os registros após confirmação do usuário
- **Sair** — encerra o programa; os dados já estão salvos, nenhuma informação é perdida

## Funções implementadas

| Função | Responsabilidade |
|--------|-----------------|
| `carregar()` | Lê o arquivo `lancamentos.json` do disco e retorna a lista de lançamentos; retorna lista vazia se o arquivo não existir ou estiver corrompido |
| `salvar()` | Grava a lista de lançamentos atualizada no arquivo `lancamentos.json` com indentação e encoding UTF-8 |
| `registrar_lancamento()` | Coleta tipo, valor, categoria e descrição do usuário com validação, monta o dicionário do lançamento com data/hora e chama `salvar()` |
| `exibir_extrato()` | Percorre todos os lançamentos e imprime cada um formatado com índice, data, tipo, categoria, sinal e valor |
| `calcular_saldo()` | Soma separadamente receitas e despesas e retorna uma tupla com os três valores (receitas, despesas, saldo) |
| `gerar_relatorio()` | Usa `calcular_saldo()` e agrupa os lançamentos por categoria para exibir um resumo completo no terminal |
| `exportar_relatorio()` | Chama `gerar_relatorio()`, captura as linhas retornadas e as escreve no arquivo `relatorio.txt` |

## Estrutura do repositório

```
financas-pessoais/
├── financas.py        # programa principal
├── lancamentos.json   # dados gerados pelo programa
├── relatorio.txt      # exportado pelo programa (evidência)
└── README.md          # documentação do projeto
```

## Tecnologias usadas

Python 3 · json · os · datetime

## O que aprendi

Entendi que é muito importante estruturar as ideias antes de começar a codar, porque na teoria deixa mais prático. Eu achei um pouquinho complicado o fluxograma, ainda prefiro fazer por algoritmo listado, acho mais fácil. Aprendi a usar melhor o JSON, abrindo margem para outros projetos pessoais que eu tenho também. Foi difícil me habituar a subir arquivos pelo terminal em vez de direto no GitHub, mas foi importante aprender. Se começasse de novo, já planejaria melhor a estrutura do JSON antes de escrever as funções
<div align="center">
  <img src="spidey.gif">
</div>