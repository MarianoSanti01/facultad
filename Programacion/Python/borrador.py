# Definir el cuadro de goles en un arreglo de dos dimensiones
goals = [
    [0, 2, 1, 3, 4, 0, 1, 2, 3, 0],
    [1, 0, 2, 0, 1, 2, 0, 1, 0, 1],
    [1, 0, 0, 2, 0, 1, 0, 1, 2, 0],
    [0, 3, 2, 0, 1, 0, 2, 0, 3, 0],
    [4, 1, 1, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 2, 0, 0, 2],
    [2, 1, 0, 2, 1, 2, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 2, 0, 1, 1],
    [3, 2, 0, 1, 1, 0, 0, 2, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 0]
]

# Inicializar listas para almacenar victorias, empates, perdidas, goles marcados y goles recibidos
wins = [0] * 10
equals = [0] * 10
loses = [0] * 10
goals_given = [0] * 10
goals_received = [0] * 10

# Calcular los resultados de los partidos
for i in range(10):
    for j in range(10):
        if i != j:
            goals_team_i = goals[i][j]
            goals_wins_j = goals[j][i]
            if goals_team_i > goals_wins_j:
                wins[i] += 1
            elif goals_team_i < goals_wins_j:
                loses[i] += 1
            else:
                equals[i] += 1
            goals_given[i] += goals_team_i
            goals_received[i] += goals_wins_j

# Calcular los puntos obtenidos por cada equipo (3 puntos por triunfo, 1 punto por empate)
points = [wins[i] * 3 + equals[i] for i in range(10)]

# Mostrar los resultados para cada equipo
for i in range(10):
    print(f"Equipo {i + 1}: victorias: {wins[i]}, empates: {equals[i]}, Derrotas: {loses[i]}")
    print(f"Goles marcados: {goals_given[i]}, Goles recibidos: {goals_received[i]}")
    print(f"Diferencia de Goles: {goals_given[i] - goals_received[i]}, Puntos: {points[i]}\n")