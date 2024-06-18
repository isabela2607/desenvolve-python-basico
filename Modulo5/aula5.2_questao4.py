import datetime
horario_atual = datetime.datetime.now()
data_formatada = f"Data: {horario_atual.day:02d}/{horario_atual.month:02d}/{horario_atual.year}"
hora_formatada = f"Hora: {horario_atual.hour:02d}:{horario_atual.minute:02d}"
print(data_formatada)
print(hora_formatada)