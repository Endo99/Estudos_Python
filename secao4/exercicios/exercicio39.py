importancia = 780.000 # Errado refazer!

primeiro_ganhador = (importancia * 0.46) / 0.10
segundo_ganhador = (primeiro_ganhador * 0.32) / 0.10
total = primeiro_ganhador + segundo_ganhador
terceiro_ganhador = total - importancia

print(f'O primeiro ganhador ganharĂ¡: {primeiro_ganhador}')
print(f'O segundo ganhador ganharĂ¡: {segundo_ganhador}')
print(f'O terceiro ganhador ganharĂ¡: {terceiro_ganhador}')

