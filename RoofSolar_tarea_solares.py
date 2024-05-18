def calculo(x_techo, y_techo, x_panel,y_panel):
    if x_panel > x_techo or y_panel > y_techo:
        return "No entran pues"
    
    area_techo = x_techo * y_techo

    area_panel = x_panel * y_panel

    max_paneles = area_techo // area_panel

    return max_paneles

# x_panel =1
# y_panel = 2
# x_techo =2
# y_techo =4

# x_panel =1
# y_panel = 2
# x_techo =3
# y_techo =5

x_panel =2
y_panel = 2
x_techo =1
y_techo =10

resultado = calculo(x_techo,y_techo,x_panel,y_panel)
print("Resultado maximo de paneles para el techo es de : ", resultado)
