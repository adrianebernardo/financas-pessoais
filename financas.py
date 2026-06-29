import json
import os
from datetime import datetime

ARQUIVO = "lancamentos.json"

def carregar():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print("Erro ao ler o arquivo. Iniciando com lista vazia.")
            return []
    return []


def salvar(lancamentos):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(lancamentos, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"Erro ao salvar: {e}")


def pedir_tipo():
    while True:
        tipo = input("Tipo (receita/despesa): ").strip().lower()
        if tipo in ("receita", "despesa"):
            return tipo
        print("Digite exatamente 'receita' ou 'despesa'.")


def pedir_valor():
    while True:
        try:
            valor = float(input("Valor (R$): ").replace(",", "."))
            if valor <= 0:
                print("O valor deve ser maior que zero.")
            else:
                return valor
        except ValueError:
            print("Digite um número válido.")


def registrar_lancamento(lancamentos):
    print("\n── Novo Lançamento ──────────────────")
    tipo      = pedir_tipo()
    valor     = pedir_valor()
    categoria = input("Categoria (ex: alimentação, salário): ").strip()
    descricao = input("Descrição: ").strip()

    lancamento = {
        "data"     : datetime.now().strftime("%d/%m/%Y %H:%M"),
        "tipo"     : tipo,
        "categoria": categoria if categoria else "Sem categoria",
        "descricao": descricao if descricao else "—",
        "valor"    : valor,
    }

    lancamentos.append(lancamento)
    salvar(lancamentos)
    print(f"Lançamento registrado! ({tipo.capitalize()} de R$ {valor:.2f})")


def exibir_extrato(lancamentos):
    print("\n── Extrato ──────────────────────────")
    if not lancamentos:
        print("Nenhum lançamento encontrado.")
        return

    for i, l in enumerate(lancamentos, 1):
        sinal = "+" if l["tipo"] == "receita" else "-"
        print(
            f"{i:>3}. [{l['data']}] {l['tipo'].upper():<8} "
            f"| {l['categoria']:<18} "
            f"| {sinal}R$ {l['valor']:>10.2f} "
            f"| {l['descricao']}"
        )


def calcular_saldo(lancamentos):
    receitas  = sum(l["valor"] for l in lancamentos if l["tipo"] == "receita")
    despesas  = sum(l["valor"] for l in lancamentos if l["tipo"] == "despesa")
    return receitas, despesas, receitas - despesas


def gerar_relatorio(lancamentos):
    print("\n── Relatório ────────────────────────")
    if not lancamentos:
        print("Nenhum dado para gerar relatório.")
        return

    receitas, despesas, saldo = calcular_saldo(lancamentos)

    por_categoria = {}
    for l in lancamentos:
        cat  = l["categoria"]
        tipo = l["tipo"]
        por_categoria.setdefault(cat, {"receita": 0.0, "despesa": 0.0})
        por_categoria[cat][tipo] += l["valor"]

    linhas = [
        "=" * 45,
        "          RELATÓRIO FINANCEIRO",
        "=" * 45,
        f"  Total de receitas : R$ {receitas:>10.2f}",
        f"  Total de despesas : R$ {despesas:>10.2f}",
        f"  Saldo             : R$ {saldo:>10.2f}",
        "-" * 45,
        "  POR CATEGORIA:",
    ]
    for cat, vals in sorted(por_categoria.items()):
        linhas.append(
            f"    {cat:<20} "
            f"+R${vals['receita']:>8.2f}  "
            f"-R${vals['despesa']:>8.2f}"
        )
    linhas.append("=" * 45)

    for linha in linhas:
        print(linha)

    return linhas

def limpar_relatorio(lancamentos):
    confirmar = input("Tem certeza que deseja apagar TODOS os lançamentos? (s/n): ").strip().lower()

    if confirmar == "s":
        lancamentos.clear()
        salvar(lancamentos)
        print("✅ Todos os lançamentos foram apagados.")
    else:
        print("Operação cancelada.")


def exportar_relatorio(lancamentos):
    linhas = gerar_relatorio(lancamentos)
    if linhas is None:
        return

    try:
        with open("relatorio.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(linhas) + "\n")
        print("Arquivo 'relatorio.txt' gerado com sucesso!")
    except IOError as e:
        print(f"Erro ao exportar: {e}")


def menu(lancamentos):
    print("""
╔══════════════════════════════════╗
║          MINHAS FINANÇAS         ║
╠══════════════════════════════════╣
║  1 → Registrar lançamento        ║
║  2 → Ver extrato                 ║
║  3 → Relatório                   ║
║  4 → Exportar relatório (.txt)   ║
║  5 → Limpar lançamentos          ║
║  6 → Sair                        ║
╚══════════════════════════════════╝""")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        registrar_lancamento(lancamentos)
    elif opcao == "2":
        exibir_extrato(lancamentos)
    elif opcao == "3":
        gerar_relatorio(lancamentos)
    elif opcao == "4":
        exportar_relatorio(lancamentos)
    elif opcao == "5":
        limpar_relatorio(lancamentos)
    elif opcao == "6":
        print("Tchaaau xD! Seus dados foram salvos em segurança.")
        return False
    else:
        print("Opção inválida. Digite um número de 1 a 6.")

    return True


def main():
    print("Iniciando App de Finanças Pessoais...")
    lancamentos = carregar()
    print(f"{len(lancamentos)} lançamento(s) carregado(s).")

    continuar = True
    while continuar:
        continuar = menu(lancamentos)


if __name__ == "__main__":
    main()