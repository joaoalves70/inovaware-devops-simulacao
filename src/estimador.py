def estimar_tempo(distancia_km, velocidade_kmh):
    if distancia_km < 0:
        raise ValueError("A distância não pode ser negativa.")
    if velocidade_kmh <= 0:
        raise ValueError("Velocidade deve ser maior que zero.")
    tempo_horas = distancia_km / velocidade_kmh
    tempo_minutos = tempo_horas * 60
    return round(tempo_minutos, 2)
