import os

from valueIterationClass import ValueIteration
from ppddlparser import Parser
from LrtdpClass import Lrtdp
import time

def planingVi(problem):
    start_time = time.time()

    planejador = ValueIteration(problem)
    planejador.planejar()

    end_time = time.time()
    timePlaning = end_time - start_time
    return timePlaning

def planingLrtdp(problem):
    start_time = time.time()

    lrtdp = Lrtdp(problem)
    lrtdp.iniciar()

    end_time = time.time()
    timePlaning = end_time - start_time
    return timePlaning


def getPaths():
    inicialDir = 'Problems'
    listDirs = os.listdir(inicialDir)
    listDatas = []
    for dir in listDirs:
        path = inicialDir + '/' + dir
        problemsPath = os.listdir(path)
        for problemPath in problemsPath:
            listDatas.append(path+'/'+problemPath)
    return listDatas
            # if os.path.isdir(path + '/' + problemPath):
            #     listProblems = os.listdir(path + '/' + problemPath)
            #     for problem in listProblems:
            #         problemFile = path + '/' + problemPath + '/' + problem
            #         tuple = (domain, problemFile)
            #         listDatas.append(tuple)


def TesteAll():
    listDatas = getPaths()
    for data in listDatas:
        problem = Parser(data)

        tempo = planingVi(problem)
        print("Vi:",tempo)

        tempo = planingLrtdp(problem)
        print("Lrtdp:",tempo)

TesteAll()