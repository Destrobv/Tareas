def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento


monto1 = 1000
monto2 = 2000
porcentaje_descuento2 = 15

descuento1 = calcular_descuento(monto1)
total_con_descuento1 = monto1 - descuento1
print(f"Monto total de compra: ${monto1}")
print(f"Descuento aplicado: ${descuento1}")
print(f"Monto final a pagar después del descuento: ${total_con_descuento1}\n")

descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
total_con_descuento2 = monto2 - descuento2
print(f"Monto total de compra: ${monto1}")
print(f"Porcentaje de descuento: {porcentaje_descuento2}%")
print(f"Descuento aplicado: ${descuento1}")
print(f"Monto final a pagar después del descuento: ${total_con_descuento2}")
