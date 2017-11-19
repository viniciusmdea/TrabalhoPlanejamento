import re
from Action import Action
from Problem import Problem

def Parser(caminhoArquivo):
    #Lendo o arquivo
    arquivo  = open(caminhoArquivo, 'r')
    textoArquivo = arquivo.read()
    textoArquivo = textoArquivo.replace('\t','')

    #Lendo os estados
    textoState = textoArquivo[textoArquivo.find('states')+len('states'):textoArquivo.find('endstates')]
    textoState = textoState.replace('\n','')
    listaState= textoState.split(',')
    # print("states:",listaState)

    #Lendo as acoes e colocando no dicionario actionsDic{Nome:ListaAcoes}
    regex = r"action ((.|\s)+?)\nendaction"
    listaAction = re.findall(regex, textoArquivo)
    actionsDic = {}
    for actionsText in listaAction:
        actionsList = []
        linhasAction = actionsText[0].split('\n')
        for action in linhasAction[1:]:
            actionPar = action.split(' ')
            actionVar = Action(actionPar[0],actionPar[1],float(actionPar[2]))
            actionsList.append(actionVar)
        actionsDic[linhasAction[0]] = actionsList
    # print(actionsDic)


    #Lendo reward
    listaReward  = re.search('(?<=reward)(.|\s)*(?=\nendreward)', textoArquivo)
    listaReward = listaReward.group(0)
    listaReward = listaReward.split('\n')
    #Criando Lista de reward ligado a seu statos
    for i in range(1,len(listaReward)):
        listaReward [i] = listaReward[i].split(' ')
    dictState = {}
    #Criando dicionario estato a reward
    for i in range(1,len(listaReward)):
        key = listaState[i-1].replace(' ','')
        value = float(listaReward[i][1])
        dictState[key] = value
    #print("dict",dictState)

    #print("\nReward:",listaReward )

    #Lendo cost
    listaCost = re.search('(?<=cost)(.|\s)*(?=\nendcost)', textoArquivo)
    listaCost  = listaCost.group(0)
    # print("\nCosts:",listaCost)

    #Discount factor
    inicio = textoArquivo.find('discount factor')
    buscaDiscount = re.search('(?<=discount factor).*(?=\n)', textoArquivo)
    factorDiscount = float(buscaDiscount.group(0))
    # print ("\nDiscont:",factorDiscount)

    #inialState
    buscaInit = re.search('(?<=initialstate)(.|\s)*(?=endinitialstate)', textoArquivo)
    init = buscaInit.group(0)
    init = init.replace('\n','')
    # print("init:",init)

    #goal
    buscaGoal = re.search('(?<=goalstate)(.|\s)*(?=endgoalstate)', textoArquivo)
    goal = buscaGoal.group(0)
    goal = goal.replace('\n','')
    # print("goal:",goal)


    problema = Problem(init,goal,factorDiscount,actionsDic,dictState)
    return problema