#Fatiamento - começa do 0
frase='Hello World!'
#[n1:(até) n2,n2 fica de fora-:n3(pular de n3 em n3]
frase[4]
frase[0:5]
frase[0:9:2]
#mesma coisa da linha 5:
frase[:5]
#do n até o final:
frase[6:]
#mesma coisa da linha 6:
frase[6::2]
#Análise da cadeia - string
len(frase)
frase.count('o')
frase.count('o',0,6)
frase.find('llo')
#quando não tem a string = -1
'World' in frase
#Transformação
frase.replace('Hello','Android')
#maiusculo:
frase.upper()
#minusculo:
frase.lower()
#todos os caracteres ficam em minusculo menos a primeira
frase.capitalize()
#em quebras fica maiusculo
frase.title()
#tirar espaços sobrando do começo e final
f2='   Liga da justiça  '
frase.strip()
###esquerda
frase.lstrip()
###direita
frase.rstrip()
#divisão - cada palavra recomeça a contagem e cada uma fica com um numero em lista
##Hello - 1 -- World - 2 --
frase.split()
#Junção
##Hello-World!
'-'.join.frase
#Textos grandes:
print("""aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
llllllllllllllllllllllllllllllllllllllllllllllllll
kkkkkkkkkkkkkkklllllld""")
#list em []