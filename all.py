class cp1:
    
    def cp1000():
        print("Hello World!")
    
    def cp1001():
        A=int(input())
        B=int(input())
        print("X =",A+B)

    def cp1002():
        raio = float(input())
        area = (raio * raio) * 3.14159 
        print("A=%.4f" %area)  

    def cp1003():
        A=int(input())
        B=int(input())
        SOMA=A+B
        print("SOMA = "+str(SOMA))

    def cp1004():
        a=int(input())
        b=int(input())
        PROD=a*b
        print("PROD = "+str(PROD))

    def cp1005():
        nota1 = float(input())
        nota2 = float(input())
        media = (((nota1 * 3.5) + (nota2 * 7.5)) / 11)
        print(f'MEDIA = {media:.5f}')
    
    def cp1006():
        a = float(input())
        b = float(input())
        c = float(input())

        media = (a/10 * 2) + (b/10 * 3) + (c/10 * 5)

        print(f'MEDIA = {media:.1f}')

    def cp1007():
        A=int(input())
        B=int(input())
        C=int(input())
        D=int(input())
        print("DIFERENCA = "+str(A*B-C*D))

    def cp1008():
        Num = int(input())
        ha=int(input())
        Sa=float(input())
        print("NUMBER = "+str(Num))
        print("SALARY = U$ %.2f " %(ha*Sa))

    def cp1009():
        name = input()
        salary = float(input())
        sold = float(input())
        bonus = float(sold * (15/100))
        total = salary + bonus
        print(f'TOTAL = R$ {total:.2f}')

    def cp1010():
        line1 = input().split(" ")
        line2 = input().split(" ")
        num1, flot1, nam1 = line1
        num2, flot2, nam2 = line2
        total = (int(flot1) * float(nam1)) + (int(flot2) * float(nam2))# exp: input :
        """
        3 4 5
        1 2 3
        output: 4*5=20+2*3=26.00
        """
        print(f'VALOR A PAGAR: R$ {total:.2f}')

    def cp1011():
        r = int(input())
        volume = (4/3.0*3.14159*r*r*r)
        print("VOLUME = %0.3f"%volume)

    def cp1012():
        a, b, c = list(map(float, input().split()))
        triangle = 0.5*a*c
        circle = 3.14159*c*c
        trapezium = (a+b)/2.0*c
        square = b*b
        rectangle = a*b
        print("TRIANGULO: %.3lf" % triangle)
        print("CIRCULO: %.3f" % circle)
        print("TRAPEZIO: %.3f" % trapezium)
        print("QUADRADO: %.3f" % square)
        print("RETANGULO: %.3f" % rectangle)

    def cp1013():
        x,y,z=list(map(int,input().split()))
        print("{} eh o maior".format(max(x,y,z)))

    def cp1014():
        distancia = int(input())
        combustivel = float(input())
        consumo = distancia / combustivel
        print(f'{consumo:.3f} km/l')

    def cp1015():
        import math
        x1, y1 = list(map(float, input().split()))
        x2, y2 = list(map(float, input().split()))
        distance = math.sqrt(pow(x2-x1, 2)+pow(y2-y1, 2))
        print(f'{distance:0.4f}')

    def cp1016():
        distance = int(input())
        print(f'{distance*2} minutos')

    def cp1017():
        t = int(input())
        v = int(input())

        liters = (v*t)/12
        print(f'{liters:.3f}')

    def cp1018():
        amount = int(input())
        print(amount)
        print("{} nota(s) de R$ 100,00".format(int(amount/100)))
        note = (amount%100)
        print("{} nota(s) de R$ 50,00".format(int(note/50)))
        note = (note%50)
        print("{} nota(s) de R$ 20,00".format(int(note/20)))
        note= (note%20)
        print("{} nota(s) de R$ 10,00".format(int(note/10)))
        note = (note%10)
        print("{} nota(s) de R$ 5,00".format(int(note/5)))
        note= (note%5)
        print("{} nota(s) de R$ 2,00".format(int(note/2)))
        note = (note%2)
        print("{} nota(s) de R$ 1,00".format(int(note/1)))


license="""MIT License

Copyright (c) 2022 SHOMRIDDHO'S WORLD

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""




