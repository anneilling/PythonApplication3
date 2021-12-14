from random import *

def arvud_loendis(): 
    """põhifunktsooinid
    """
    s=[]
    pos=[]
    neg=[]
    null=[]
    kesk=[]
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi: #mini=100 ,maxi=5 => mini=5 , maxi=100
        vahetus(mini,maxi)
    generator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    jagamine(s,pos,neg,null)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",null)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    print(s)

def vahetus(a:int,b:int):
    """muutujate teisendamine üheks väärtuseks
    :param int a: minimaalne arv, mis on suurem kui max
    :param int b: maximaalne arv, mis on väiksem kui min
    :rtype: int,int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generator(n:int,loend:list,a:int,b:int):
    """genereerib juhuslikke numbreid
    :param int n: numbrite hulk
    :param list loend: arvute loend
    :param int a: min genereeritav arv
    :param int b: max genereeritav arv
    :rtype: int
    """
    for i in range(n):
        loend.append(randint(a,b))
   

def jagamine(loend:list,p:list,n:list,null:list):
    """jagab väärtused loendisse
    :param list loend: arvute loend
    :param list p:
    :param list n: arvute koguarv
    :param list null: nullväärtuse loend
    :rtype: list
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            null.append(el)

def keskmine(loend:list):
    """leiab arvu keskmine
    :param list loend: arvute loend
    :rtype: float
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend,el):
    """lisab üksuse ja sorteerib loendit
    :param list loend: arvute loend
    :param float el: murdosa loend
    :rtype: float
    """
    loend.append(el)
    loend.sort()

arvud_loendis()