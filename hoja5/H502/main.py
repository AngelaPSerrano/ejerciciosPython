from loteria import Loteria
from jugador import Jugador

loteria = Loteria()
jugador = Jugador()

def ejecutar(semanas):
    for i in range(0,semanas*2):
        jugador.compraBoleto()
        premio = loteria.getPremio()
        reintegro = loteria.getReintegro()
        jugador.ganaPremio(premio,(i+1), loteria.generaGanador(), reintegro)

jugador.definirCondiciones()
ejecutar(jugador.getSemanas())
jugador.resultado()

