#Cores no terminal
#\033[estilo,text,fundom
#\033[0;33;44m
###estilo:0,1(negrito),4(sublinhado),7(negativo)
###text:30(branco),31(vermelho),32(verde),33(amarelo),34(azul),35(magenta),36(ciano),37(cinza)
###fundo: 40 a 47(mesma ordem text)
#\033[0;30;41m
#\033[4;33;44m
#\033[1;35;43m
#\033[30;42m
#\033[m
#\033[7;30m
print('\033[4;30;46mOlá, mundo!\033[m')
a=3
b=5
print('Os valores são \033[1;31;m{}\033[m e \033[1;35;m{}\033[m'.format(a,b))
string="prova de python"
print('letras {}'.format(len(string)))
n=19 // 2
n2=19%2
print('valores {} e {}'.format(n,n2))
n3=3 * 5 + 4 ** 2
print('valor {}'.format(n3))
