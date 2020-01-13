unidades = [ "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove"]
teen = ["onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
dezenas = ["dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
centenas = ["cem", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]


def convert(number):
    SINAL = int(number)
    number = abs(int(number))
    numb = str(number)
    unidadeDoNumero = number //1 % 10
    dezenaDoNumero = number //10 % 10
    centenaDoNumero = number //100 % 10
    milharDoNumero = number //1000 % 10
    dmilharDoNumero = number //10000 % 10

    ##hipotese
    dezena = transcreveDezena(dezenaDoNumero, unidadeDoNumero)
    unidade = transcreveUnidade(unidadeDoNumero, dezenaDoNumero)
    centena = transcreveCentena(centenaDoNumero,dezenaDoNumero,unidadeDoNumero,unidade,dezena)
    mil = transcreveMilhar(milharDoNumero,dmilharDoNumero,centena,dezena,unidade)
    dmil =transcreveDezenaDeMilhar(dmilharDoNumero,milharDoNumero)


    return sinais(SINAL)+selecionarOrdem(dmil,mil,dmilharDoNumero,numb,centenaDoNumero,dezenaDoNumero,unidadeDoNumero,unidade,dezena,number,centena)
   

def sinais(SINAL):
    if SINAL<0:
        return 'menos '
    else:
        return ' '


def selecionarOrdem(dmil,mil,dmilharDoNumero,numb,centenaDoNumero,dezenaDoNumero,unidadeDoNumero,unidade,dezena,number,centena):
    if (len(numb)) >=4:
        return chamarMilEDmil(dmil,mil,dmilharDoNumero,numb,centenaDoNumero,dezenaDoNumero,unidadeDoNumero,unidade,dezena,number,centena)+chamarCentena(numb,centenaDoNumero,dezenaDoNumero,unidadeDoNumero,unidade,dezena,number,centena)
    elif (len(numb)) <=3:
        return chamarCentena(numb,centenaDoNumero,dezenaDoNumero,unidadeDoNumero,unidade,dezena,number,centena)


def chamarMilEDmil(dmil,mil,dmilharDoNumero,numb,centenaDoNumero,dezenaDoNumero,unidadeDoNumero,unidade,dezena,number,centena):
    if dmil != None and mil != None:
        return dmil+mil
    elif dmil != None or dmilharDoNumero ==1 and mil == None :
        return dmil
    elif mil != None :
        return mil
    else:
        return chamarCentena(numb,centenaDoNumero,dezenaDoNumero,unidadeDoNumero,unidade,dezena,number,centena)


def chamarCentena(numb,centenaDoNumero,dezenaDoNumero,unidadeDoNumero,unidade,dezena,number,centena):
    if (len(numb)) <=2:
        return chamarUnidadeEDezena(number,numb,unidadeDoNumero,dezenaDoNumero,dezena,unidade)
    elif (len(numb)) >=3:
        return centena+chamarUnidadeEDezena(number,numb,unidadeDoNumero,dezenaDoNumero,dezena,unidade)


def chamarUnidadeEDezena(number,numb,unidadeDoNumero,dezenaDoNumero,dezena,unidade):
    if dezena != None and unidade != None:
        return dezena+unidade
    elif dezena != None or dezenaDoNumero==1 and unidade == None :
        return dezena
    elif unidade != None :
        return unidade
    elif number ==0 and (len(numb)) ==1:
        return "zero"
    else:
        return ' '


def transcreveUnidade(unidadeDoNumero,dezenaDoNumero):
        if unidadeDoNumero !=0 and dezenaDoNumero !=1 :
            uni = unidades[unidadeDoNumero-1]
            return uni 


def transcreveDezena(dezenaDoNumero,unidadeDoNumero):
        if dezenaDoNumero >= 2 and dezenaDoNumero <= 9 and unidadeDoNumero !=0:
            un = dezenas[dezenaDoNumero-1]
            return un + " e "
        elif dezenaDoNumero >= 1 and dezenaDoNumero <= 9 and unidadeDoNumero ==0:
            return dezenas[dezenaDoNumero-1]
        elif dezenaDoNumero ==1 and unidadeDoNumero!=0:
            return teen[unidadeDoNumero-1]


def transcreveCentena(centenaDoNumero,dezenaDoNumero,unidadeDoNumero,unidade,dezena):
    if centenaDoNumero !=0 and dezena!=None:
        return centenas[centenaDoNumero-1] + ' e '
    elif centenaDoNumero !=0 and unidade!=0:
        return centenas[centenaDoNumero-1] + ' e '
    elif centenaDoNumero !=0:
        return centenas[centenaDoNumero-1]
    else:
        return ''


def transcreveMilhar(milharDoNumero,dmilharDoNumero,centena,dezena,unidade):
    if milharDoNumero !=0 and dmilharDoNumero !=1 and dezena!=None:
        return unidades[milharDoNumero-1] + ' mil e '
    elif milharDoNumero !=0 and dmilharDoNumero !=1 and centena!='':
        return unidades[milharDoNumero-1] + ' mil e '
    elif milharDoNumero !=0 and dmilharDoNumero !=1:
        return unidades[milharDoNumero-1] + ' mil'


def transcreveDezenaDeMilhar(dmilharDoNumero,milharDoNumero):
    if dmilharDoNumero >= 2 and dmilharDoNumero <= 9 and milharDoNumero !=0:
        un = dezenas[dmilharDoNumero-1]
        return un + ' e '
    elif dmilharDoNumero >= 1 and dmilharDoNumero <= 9 and milharDoNumero ==0:
        return dezenas[dmilharDoNumero-1] + ' mil'
    elif dmilharDoNumero ==1 and milharDoNumero!=0:
        return teen[milharDoNumero-1]+ ' mil'

