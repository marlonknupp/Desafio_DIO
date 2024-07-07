def recomendar_plano():
    try:
        consumo_mensal = float(input())
        if consumo_mensal <= 10:
            plano_recomendado = "Plano Essencial Fibra - 50Mbps"
        elif 10 < consumo_mensal <= 20:
            plano_recomendado = "Plano Prata Fibra - 100Mbps"
        else:
            plano_recomendado = "Plano Premium Fibra - 300Mbps"
        
        return plano_recomendado
        
    except ValueError:
        return "Entrada inválida. Por favor, insira um número válido para o consumo de dados."

# Chamando a função e imprimindo o resultado
plano = recomendar_plano()
print(f' {plano}')

#DIO.
    
  