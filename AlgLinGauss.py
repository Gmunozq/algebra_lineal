

#reducciOn por Gauss-Jordan
#\item Vaya a la columna no cero extrema izquierda.




#\item Si el primer renglOn tiene un cero en la columna del paso (1), intercAmbielo con uno que tenga un elemento no cero en la misma columna.
#\item Obtenga ceros abajo del elemento delantero, sumando mu*ltiplos adecuados del renglo*n superior a los renglones debajo de e*l.
#\item Cubra el renglo*n superior y repita el mismo proceso comenzando por el paso (1) aplicado a la sub-matriz restante. Repita este proceso con el resto de los renglones.
#\item Comenzando con el u*ltimo renglo*n no cero, avance hacia arriba: para cada renglo*n obtenga un 1 delantero e introduzca ceros arriba de e*l, sumando mu*ltiplos adecuados a los renglones correspondientes.
#import sys
#print(sys.path)  
from AlgLinMat import *

def califica_matriz(mat):
    #print(str(mat))
    i=1
    j=1
    (m,n)=mat.size()
    repetir=True
    while repetir:
        cont_ceros=0
        cont_div=0
        delant=mat[i,j]
        ceros_abajo=True
        for i1 in range(i+1,m+1):
            a=mat[i1,j]
            if bool(a):
                ceros_abajo=False
                try:
                    amod=a%delant
                    if amod==0:
                        cont_div=cont_div+1
                except:
                    pass
                    #print()
            else:
                cont_ceros=cont_ceros+1
        if j==n or i==m or not ceros_abajo:# or not bool(delant):
            repetir=False
        elif ceros_abajo:
            j=j+1
            if bool(delant):
                i=i+1
        
    return (delant,cont_ceros,cont_div,ceros_abajo,i,j)
        

    print()
    #cuentas cuantas columnas a la izq cumplen e1
    #la primera col tiene elem delantero
    #la primncol que no cumple e1 cuantos ceros tiene abajo
    #la primera col que no cumple cuatos no ceros divide abajo
    
#def ceros_bajo():


print("""#reducciOn por Gauss-Jordan
#1 Vaya a la columna no cero extrema izquierda.
#2 Si el primer renglOn tiene un cero en la columna del paso (1), intercAmbielo con uno que tenga un elemento no cero en la misma columna.
#3 Obtenga ceros abajo del elemento delantero, sumando mu*ltiplos adecuados del renglo*n superior a los renglones debajo de e*l.
#4 Cubra el renglo*n superior y repita el mismo proceso comenzando por el paso (1) aplicado a la sub-matriz restante. Repita este proceso con el resto de los renglones.
#5 Comenzando con el u*ltimo renglo*n no cero, avance hacia arriba: para cada renglo*n obtenga un 1 delantero e introduzca ceros arriba de e*l, sumando mu*ltiplos adecuados a los renglones correspondientes.""")
print()
print("Ejemplo tomado de la pa*gina 19 del libro 'A*lgebra Lineal con  aplicaciones' de Nakos-Joyner de la editorial Thomson impreso en 1999.")
A=matriz("0 3 -6 -4 -3 -5;-1 3 -10 -4 -4 -2 ; 4 -9 34 0 1 -21;2 -6 20 2 8 -8")
print('La matriz ingresada fue')
print('A=matriz("0 3 -6 -4 -3 -5;-1 3 -10 -4 -4 -2 ; 4 -9 34 0 1 -21;2 -6 20 2 8 -8")')
try:
    A=input('Puede ingresar otra matriz, si no, solamente oprima "Enter"\n A=')
except:
    print(str(A))

repetir=True
sugerencia=0
B=A
(Am,An)=A.size()
while repetir:
    operacion=raw_input('Escriba la operacio*n entre renglones\n operacion=')
    try:
        C=B
        B=A.op(operacion)
        sugerencia=0
        D=restar_matrices(C,B)
        if bool(D):
            msg="la matriz cambio*"
            (Bij,Bceros,Bdiv,Babajo,Bi,Bj)=califica_matriz(B)
            (Cij,Cceros,Cdiv,Cabajo,Ci,Cj)=califica_matriz(C)
            if Bi==Am or Bj==An:
                repetir=False
                print('Felicitaciones!! la matriz ya esta* en forma escalo*n')
            elif Bj>Cj:
                print('Muy bien, avanzo* otra columna')
            elif Bj<Cj:
                print('Muy mal, perdio* alguna columna')
            else:
                if (not bool(Cij)) and bool(Bij) :
                    print('Super bien, ya no es cero el elemento delantero ' + str(Bi)+','+str(Bj))
                elif (not bool(Bij)) and bool(Bij) :
                    print('Super mal, ahora es cero el elemento delantero ' + str(Bi)+','+str(Bj))
                else:
                    if Bceros>Cceros:
                        print('Bien, obtuvo un cero ma*s')
                    elif Bceros<Cceros:
                        print('Mal, perdio* algu*n cero')
                    else:
                        if Cdiv>0:
                            print('Hubiera podido obtener un cero')
                        elif Bdiv>0:
                            print('Ya obtuvo un divisor en el elemento delantero') 
                        else:
                            print('No entiendo para que realizo* esa operacio*n')
            #print(califica_matriz(B)
            #print(califica_matriz(C))
            #calificar las matrices
            #decir si mejora o empeora
            #explicar el porque
        else:
            msg='La matriz no cambio*' 
            print(msg)
    except ValueError, e:
        operacion==operacion.replace(' ','').lower()
        if operacion=='salir':
            repetir=False
            print("hasta luego")
        elif operacion=='sugerir' or operacion=='ayuda':
            C=A.ultop
            print(str(C))
            (Cm,Cn)=C.size()
            (Cij,Cceros,Cdiv,Cabajo,Ci,Cj)=califica_matriz(C)
            CiNoCero=Ci+1
            while not bool(C[CiNoCero,Cj]):
                CiNoCero=CiNoCero+1

            if Ci==Cm or Cj==Cn:
                sug1='La matriz ya esta* en forma escalo*n'
                sug2=sug1
                sug3=sug2
                repetir=False
            elif not bool(Cij):
                sug1='Nuestro objetivo ahora es obtener un pivote en la columna '+str(Cj)+', pero observe que en el renglo*n '+str(Ci)+' hay un cero'
                sug2='Debe intercambiar el renglo*n '+str(Ci)+' con el renglo*n '+ str(CiNoCero)
                sug3='R'+str(Ci)+' <-> R'+str(CiNoCero)
            else:
                sug1='Ahora hay que obtener ceros bajo el pivite'
                sug2='Hay que sumar un multiplo del renglo*n '+str(Ci)+' al renglo*n '+str(CiNoCero)
                sug3=str(frac(-C[CiNoCero,Cj],C[Ci,Cj]))+'R'+str(Ci)+' + R'+str(CiNoCero)+' -> R'+str(CiNoCero)  
            sugerencia=sugerencia+1
            if sugerencia==1:
                print(sug1)
            elif sugerencia==2:
                print(sug2)
            else:
                print(sug3)
                sugerencia=0
                
        else:
            print('No entiendo: '+str(e))
            print('Algunos ejemplos de operaciones son: \n \t r1<->r2 \n \t -2r1+r2->r2 \n \t 3r2->r2')
#print("Segu*n el paso 1, observamos que la primera columna de la matriz no es cero, por lo tanto comenzamos con esta columna, j=1")
#print("Segu*n el paso 2, hay que mirar el primer renglo*n, i=1, de la columna j.  elemento de esa columna A[] intercambiar el renglo*n 1 por algun renglon j, que no tenga cero, a[j,1]!=0 , preferiblement si el primer e")

