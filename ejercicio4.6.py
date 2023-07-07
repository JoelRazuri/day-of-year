""" 
    Suponiendo que el primer día del año fue lunes, escribir una función que reciba
    un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por ejemplo:
    si recibe '3' debe devolver 'miércoles', si recibe '9' debe devolver 'martes'.
"""


def sumador_dias(lista):
    # Suma 7 a todas las posiciones.

    for i in range(7):
        lista[i]= lista[i] + 7

def dia_del_año(dia):
    # Suponiendo que el primer dia es lunes, recibe un dia (número) y devuelve el dia de la semana que le toca.

    lista_dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
    num_dias=[1,2,3,4,5,6,7]
    flag=True
    i=1

    while i<=53 and flag==True:
        for j in range(7):
            if dia==num_dias[j]:
                posicion=j
                flag=False
        sumador_dias(num_dias)
        i+=1

    print(f"El día {dia} corresponde al día de la semana: {lista_dias[posicion]}.")

dia_del_año(1)
dia_del_año(35)
dia_del_año(10)
dia_del_año(25)
dia_del_año(366)