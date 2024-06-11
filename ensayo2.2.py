import os 
import time
os.system("cls")

completo_italiano = 0
hamburguesa = 0
total = 0
subtotal = 0
descuento = 0
nombre_descuento = ""
cant_producto = 0

menu_completo = True
while menu_completo:
    os.system("cls")
    print("menu comida rapida")
    print("1.completo italiano \t\t$2000")
    print("2.hamburguesa \t\t\t$1500")
    print("3.anular")
    print("4.comprar")

    opcion_comida = 0
    try:
        opcion_comida = int(input("ingrese una opcion >>"))
    except:
        print("la opcion no esta disponible")
    
    if opcion_comida < 1 or opcion_comida > 4:
        print("la opcion esta fuera de rango")
        time.sleep(2)
        os.system("cls")
    
    else:
        if opcion_comida == 1:
            try:
                completo_italiano += int(input("cuantos completos italianos desea? >>"))
            except:
                print("la opcion no esta disponible")
        elif opcion_comida == 2:
            try:
                hamburguesa += int(input("cuantas hamburguesas desea comprar? >>"))
            except:
                print("la opcion no esta disponible")
        elif opcion_comida == 3:
            try:
                anular = int(input("desea anular la compra ? 1si.2no"))
            except:
                print("la opcion debe ser numerica")
            if anular ==1:
             print("pedido anulado")
             os.system("cls") 
             time.sleep(2)  
             menu_completo = False

        elif opcion_comida == 4:
            cant_producto = completo_italiano+hamburguesa
            if cant_producto == 0:
                os.system("cls")
                print("debe comprar para pagar")
                time.sleep(2)
            else:
                menu_descuento = True
                while menu_descuento:
                    os.system("cls")
                    print("menu descuento")
                    print("1.estudiante \t\t20%")
                    print("2.funcionario\t\t10%")
                    print("3.sin descuento\t\t0%")

                    opcion_descuento = 0
                    
                    try:
                        opcion_descuento = int(input("ingrese una opcion >>"))
                    except:
                        print("la opcion no esta disponible")
                    
                    if opcion_descuento < 1 or opcion_descuento > 3:
                        print("la opcion esta fuera de rango")
                    else:
                       if opcion_descuento == 1:
                          nombre_descuento ="estudiante"
                          descuento=20
                       elif opcion_descuento == 2:
                           nombre_descuento ="funcionario"
                           descuento = 10
                       elif opcion_descuento == 3:
                           nombre_descuento ="sin descuento"
                           descuento = 0
                       else:
                           print("opcion no disponible")
                           menu_descuento = False

                  
                    os.system("cls")
                    print("boleta comida rapida")
                    print("--------------------")
                    cant_producto =completo_italiano+hamburguesa
                    if completo_italiano > 0:
                        print(f"{completo_italiano}completo italiano ${completo_italiano*2000}")
                    if hamburguesa > 0:
                        print(f"{hamburguesa}hamburguesa ${hamburguesa*1500}")
                    print("---------------------------")
                    subtotal=completo_italiano*2000+hamburguesa*1500
                    print(f"total productos{total}")
                    print("descuentos")
                    print(f"{descuento}%{nombre_descuento}\t{int(subtotal*descuento/100)}")
                    print("--------------------------")
                    total=subtotal-descuento
                    print(f"total a pagar\t{total}")
                    print("---------------------")
                    print("gracias por su compra")
                    input()
        else:
            print("la opcion no es valida")          


                    

            

               