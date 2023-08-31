

def media(a, b, c):
    s = [a,b,c]
    s.sort()
    a = sum(s)
    return a/3


def mediana(a, b, c):
    x = [a,b,c]
    x.sort()
    return x[1]

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = None
    
    a = media(10,20,30)
    print(a)
    b = mediana(13,24,10)
    print(b)
    
    

#Input:
#Receber duas entradas inteiras

#Processing:
#Calcular o menor C que seja a media e mediana entre eles.


#media = (a + b + c)/3
#mediana = valor medio entre a e b 