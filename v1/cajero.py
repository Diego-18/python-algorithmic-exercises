carga50 = 100
carga20 = 100
carga10 = 100

def sacar_dinero(cantidad):
  global carga50, carga20, carga10
  if cantidad <= 50 * carga50 + 20 * carga20 + 10 * carga10:
    de50 = cantidad / 50
    cantidad = cantidad % 50
    if de50 >= carga50: # Si hay suficientes billetes de 50
      cantidad = cantidad + (de50 - carga50) * 50
      de50 = carga50
    de20 = cantidad / 20
    cantidad = cantidad % 20
    if de20 >= carga20: # y hay suficientes billetes de 20
      cantidad = cantidad + (de20 - carga20) * 20
      de20 = carga20
    de10 = cantidad / 10
    cantidad = cantidad % 10
    if de10 >= carga10: # y hay suficientes billetes de 10
      cantidad = cantidad + (de10 - carga10) * 10
      de10 = carga10
    # Si todo ha ido bien, la cantidad que resta por entregar es nula:
    if cantidad == 0:
      # Así que hacemos efectiva la extracción
      carga50 = carga50 - de50
      carga20 = carga20 - de20
      carga10 = carga10 - de10
      return [de50, de20, de10]
    else: # Y si no, devolvemos la lista con tres ceros:
      return [0, 0, 0]
  else:
    return [0, 0, 0]


# Programa principal
while 50*carga50 + 20*carga20 + 10*carga10 > 0:
  peticion = int(raw_input('Cantidad que desea sacar: '))
  [de50, de20, de10] = sacar_dinero(peticion)
  if [de50, de20, de10] != [0, 0, 0]:
    if de50 > 0:
      print 'Billetes de 50 euros:', de50
    if de20 > 0:
      print 'Billetes de 20 euros:', de20
    if de10 > 0:
      print 'Billetes de 10 euros:', de10
    print 'Gracias por usar el cajero.'
    print
  else:
    print 'Lamentamos no poder atender su petición.'
    print
print 'Cajero sin dinero. Avise a mantenimiento.'
