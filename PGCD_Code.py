#diviseurs d'un nombre
def div(number):
    dividers=[]
    #on divise le nombre 'number' succéssivement par tous les nombres allant de 1 
    #à sa racine carrée 
    for i in range(1,int(number**0.5)+1):
        #À chaque fois que le quotient est un nombre entier, alors ce quotient 
        #et le diviseur sont tous deux des diviseurs de number
        if(number%i==0):
            dividers.append(i)
            dividers.append(number//i)
    return sorted(set(dividers))    
    
    
def pgcd(number1,number2):
    #On genere les diviseurs du premier nombre et du deuxieme nombre
    divNumber1=div(number1)
    divNumber2=div(number2)
    #On parcoure les deux listes inversement pour réduire la complexité de l'algorithme
    for k in range(-1,-len(divNumber1)-1,-1):
        for s in range(-1,-len(divNumber2)-1,-1):
            if(divNumber1[k] == divNumber2[s]):
                return divNumber1[k]
    #au cas où il n'existe pas un deviseur commun en retourne 0        
    return 0 
