'''
Module qui permet d'effectuer des conversions
- de temps / durée
- de temperature

$ python print(py
'''

def celsiusToFahrenheit(tC):
    ''' Fonction qui permet de convertir une température en degré celsius en une
    temperature en degre Farhenheit

    Args :
        tC (float) : Temprature en degres Celsius

    Returns :
        tF (float) : Temperature en degres Farenheit

    Examples :
        >>> celsiusToFahrenheit(37)
        98.60

    '''
    tF= 32 + 1.8 * tC
    return tF


def fahrenheitToCelsius(tF):
    ''' Fonction qui permet de convertir une température en degré Farhenheit en une
    temperature en degre Celsius

    Args :
        tF (float) : Temperature en degres Farenheit

    Returns :
        tC (float) : Temprature en degres Celsius

    Examples :
        >>> fahrenheitToCelsius(72)
        22.222222
    '''
    tC = ( tF - 32 ) / 1.8
    return tC


def convertirEnSecondes(h, m, s):
    ''' Fonction qui permet de convertir une température en degré Farhenheit en une
    temperature en degre Celsius

    Args :
        tF (float) : Temperature en degre Farenheit

    Returns :
        tC (float) : Temperature en degre Celsius

    Examples :
    >>> convertirEnSecondes(2,30,12)
    9012
    '''
    hs=h*3600
    ms=m*60
    hsec= hs + ms + s
    return hsec


def convertirEnHMS(s):
    ''' Fonction qui permet de convertir une durée en secondes en heures/minutes/secondes

    Args :
        s (int) : Duree en secondes

    Returns :
        triplet (tuple) : Temps en (heures,minutes,secondes)

    Examples :
        >>> convertirEnHMS(12345)
        (3, 25, 45)
    '''
    h= s // 3600
    reste= s % 3600
    m = reste // 60
    s = reste % 60
    triplet = (h,m,s)
    return triplet

def calculerTempsEcoule(h1, m1, s1, h2, m2, s2):
    ''' Fonction qui calcule le temps écoulé entre deux horaires

    Args :
        h1 (int) : heures horaire 1
        m1 (int) : minutes horaire 1
        s1 (int) : secondes horaire 1
        h2 (int) : heures horaire 2
        m2 (int) : minutes horaire 2
        s2 (int) : secondes horaire 2

    Returns :
        diff (int) : difference en secondes entre les 2 horaires

    Examples :
        >>> calculerTempsEcoule(1,20,36,5,45,10)
        15900
    '''
    temps1=convertirEnSecondes(h1, m1, s2)
    temps2=convertirEnSecondes(h2, m2, s2)
    diff=abs(temps1-temps2)
    return diff

# Verification de la doc
#print(help(calculerTempsEcoule))

print(celsiusToFahrenheit(100))
print(fahrenheitToCelsius(100))
print(convertirEnSecondes(1,20,30))
print(convertirEnHMS(12345))
print(calculerTempsEcoule(1,20,40,3,20,50))
