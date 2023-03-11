# Algoritmo que mostra o calendário de um ano não-bisexto.
for ano in range(2021, 2022):
    for mes in range(1,13):
        for dia in range(1,32):      
            if mes <= 6:
                if dia == 28 and mes == 2:
                    print(f'{dia}/{mes}/{ano}')
                    break
                if mes % 2 == 1:
                    print(f'{dia}/{mes}/{ano}')
                else:
                    if dia != 31:
                        print(f'{dia}/{mes}/{ano}')
                    else:
                        break
            else:
                if mes <= 8:
                    print(f'{dia}/{mes}/{ano}')
                elif mes % 2 == 1:
                    if dia != 31:
                        print(f'{dia}/{mes}/{ano}')
                    else:
                        break
                else:
                    print(f'{dia}/{mes}/{ano}')