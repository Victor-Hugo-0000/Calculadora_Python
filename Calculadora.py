import re

while True:
    try:
        expressao = input("Digite a expressão matemática (ou 'sair'para encerrar): ").strip()
        
        if expressao.lower() == 'sair':
            break
        
        if not re.fullmatch(r"[0-9+\-*/(). ]+", expressao):
            print("Expressão inválida! Use apenas números e operadores (+, -, *, /, parênteses).")
            continue
        resultado = eval(expressao)
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("ERRO: Divisão por zero.")
    except Exception as e:
        print(f"Erro na expressão: {e}")