ano=int(input('Digite o ano de nascimento do atleta: '))
id=2021-ano
if id <= 9:
    print('Categoria: \033[34mMIRIM\033[m')
elif 9 <= id <= 14:
    print('Categoria: \033[34mINFANTIL\033[m')
elif 14 <= id <= 19:
    print('Categoria: \033[34mJUNIOR\033[m')
elif 19 <= id <= 20:
    print('Categoria: \033[34mSÊNIOR\033[m')
elif id >= 20:
    print('Categoria: \033[34mMASTER\033[m')
