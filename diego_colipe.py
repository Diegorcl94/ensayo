import os
import time
os.system("cls")

curanto = 0
mariscal = 0
chupe_centolla = 0
empanadas = 0

pisco = 0
bebidas_lata = 0
jugos_naturales = 0

cant_producto = 0
total = 0
subtotal= 0
nombre_descuento = ""
descuento = 0

menu_chilote = True
while menu_chilote:
    os.system("cls")
    print("===MENU RESTAURANTE EL CHILOTE===")
    print("====Platos====")
    print("1.curanto          $20000")
    print("2.mariscal         $12000")
    print("3.chupe centolla   $15000")
    print("4.empanadas        $3000")
    print("5.pisco sour       $5000")
    print("6.bebidas lata     $3000")
    print("7.jugos naturales  $2500")
    print("8. anular")
    print("9. pagar")

    opcion_menu = 0
    try:
        opcion_menu = int(input("ingrese una opcion >>>"))
    except:
        print("la opcion no esta disponible")
    if opcion_menu <1 or opcion_menu > 9:
        print("la opcion esta fuera de rango")
    
    else:
        if opcion_menu ==1:
            try:
                curanto += int(input("cuantos curantos desea ? >>"))
            except:
                print("la opcion no esta disponible")
        elif opcion_menu ==2:
            try:
                mariscal += int(input("cuantos mariscales desea ? >>"))
            except:
                print("la opcion no esta disponible")
        elif opcion_menu == 3:
            try:
                chupe_centolla += int(input("cuantos chupe de centolla desea ? >>"))
            except:
                print("la opcion no esta disponible")
        elif opcion_menu == 4:
            try:
                empanadas += int(input("cuantas empanadas desea ? >>"))
            except:
                print("la opcion no esta disponible")
        elif opcion_menu == 5:
            try:
                pisco += int(input("cuantos pisco sour desea ? >>"))
            except:
                print("la opcion no esta disponible")
        elif opcion_menu == 6:
            try:
                bebidas_lata += int(input("cuantas bebidas en lata necesita? >>"))
            except:
                print("la opcion no esta disponible")
        elif opcion_menu == 7:
            try:
                jugos_naturales += int(input("ingrese cuantos jugos naturales desea? >>"))
            except:
                print("la opcion no esta disponible")
        elif opcion_menu == 8:
            try:
                anular = int(input("desea anular la compra? 1.si 2.no"))
            except:
                print("la opcion debe ser numerica :( )")
            if anular == 1:
                print("la compra a sido cancelada ")
                time.sleep(3)
                os.system("cls")
                menu_chilote= True
        elif opcion_menu == 9:
            cant_producto = curanto+mariscal+chupe_centolla+empanadas+pisco+bebidas_lata+jugos_naturales
            if cant_producto == 0:
                print("debe comprar para poder pagar")
                time.sleep(3)
                os.system("cls")
            else:
                menu_descuento = True
                while menu_descuento:
                    os.system("cls")
                    print("==DESCUENTO==")
                    print("1.cliente frecuente  10%")
                    print("2.cliente nuevo       0%")

                    opcion_descuento = 0
                    try:
                        opcion_descuento = int(input("ingrese una opcion >>"))
                    except:
                        print("la opcion no esta disponible")
                    if opcion_descuento <1 or opcion_descuento > 2:
                        print("la opcion esta fuera de rango")
                    
                    else:
                        if opcion_descuento ==1:
                            nombre_descuento ="cliente frecuente"
                            descuento = 10
                        elif opcion_descuento ==2:
                            nombre_descuento ="cliente nuevo"
                            descuento = 0
                            menu_descuento = False
                    os.system("cls") 
                    print("===RESTAURANTE EL CHILOTE===") 
                    print("===DETALLE DE COMPRA===")
                    print("----------------------------")
                    cant_producto = curanto*20000+mariscal*12000+chupe_centolla*15000+empanadas*3000+pisco*3000+jugos_naturales*2500
                    if curanto > 0:
                        print(f"{curanto}\tcuranto ${curanto*20000}")
                    if mariscal > 0:
                        print(f"{mariscal}\tmariscal ${mariscal*12000}")
                    if chupe_centolla > 0:
                        print(f"{chupe_centolla}\tchupe centolla ${chupe_centolla*15000}")
                    if empanadas > 0:
                        print(f"{empanadas}\tempanadas ${empanadas*3000}")
                    if pisco > 0 :
                        print(f"{pisco}\tpisco sour{pisco*5000}")
                    if bebidas_lata > 0:
                        print(f"{bebidas_lata}\tbebida lata{bebidas_lata*3000}")
                    if jugos_naturales > 0:
                        print(f"{jugos_naturales}\tjugos naturales${jugos_naturales}")
                    print(f"{subtotal}")
                    print("-------------------")
                    print(f"{nombre_descuento} \t {descuento}%")
                    print("----------------------")
                    print("total a pagar")
                    total = subtotal - descuento
                    print(f"{subtotal-descuento/100}")
                    print("gracias por su compra que la fuerza lo acompañe ")
                    time.sleep(3)
                    os.system("cls")
                    print()
        else:
            print("compra no efectuada")    


                            
                            
                      
            

            

        


