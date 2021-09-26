print 'Programa para el cálculo del perímetro y el área de un rectángulo.'

altura = float(raw_input('Dame la altura (en metros): '))   
anchura = float(raw_input('Dame la anchura (en metros): ')) 

area = altura * anchura                                     
perimetro = 2 * altura + 2 * anchura                        

print 'El perímetro es de %6.2f metros.' % perimetro         
print 'El área es de %6.2f metros cuadrados.' % area         
