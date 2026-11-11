import imports.geometria as areas
import imports.menus as menu

menu.exibirMenuIncial()




valorArea = float(input("Digite o valor da área: "))
valorAltura = float(input("Digite o valor da altura:  "))





print(f"área do circulo: {areas.calcularAreaCirculo(valorArea)} ")

print(f"área do quadrado: {areas.calcularAreaQuadrado(valorArea)} ")

print(f"área do triangulo: {areas.calcularAreaTriangulo(valorArea, valorAltura)} ")

