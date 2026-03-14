import calendar
import locale
def consultar_ano():
    while True:
        ano = input("Digite o ano desejado (ou 0 para sair): ")
        if ano.strip()== '0':
            return None
        
        try:
            entrada = int(ano)

            if entrada < 1:
                print("0 ano deve ser um número positivo. Tente novamente lindona")
                continue
            return entrada
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro ou 0 para finalizar a operação.")
            
def consultar_mes():
    while True:
        mes = input("Digite o mẽs desejado (1-12) ou 0 para sair") 
        if mes.strip()== '0':
            return None
        try:
            entrada2 = int(mes)

            if entrada2 < 1 or entrada2 > 12:
                print("O mễs deve estar entre 1 e 12. Tente novamente lindona")
                continue
            return entrada2
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro entre 1 e 12 ou 0 para finalizar a operação.")

print("---Calendário---")
ano = consultar_ano()

if ano is not None:
    mes = consultar_mes()

    if mes is not None:
        try:
            locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
        except locale.Error:
            pass  # Fallback to default locale if pt_BR is not available
        print(f"\n--- Calendário de {mes}/{ano}---")
        print(calendar.month(ano, mes))
    else:
        print("Operação cancelada")
else:
    print("Operação cancelada")
