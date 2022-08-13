"""

This is a practice using BS4 & REQUEST!

Here is a PRACTICE extracting data FROM GOOGLE with a REQUEST (HTML SESSION)

This is for learning purposes only and is not for profit.

"""


from tracemalloc import stop
from bs4 import BeautifulSoup
from requests_html import HTMLSession
session = HTMLSession()

def index():

    print("""
        
        
        Software developed by JZ9 DEV
        
        
        What city do you want to know the weather from?
        
        """)

    
    
def city():
    index()
    try:
        ciudad = input("""
                       
Inserte 0 para terminar!
Ciudad: 
                       
""")

        try:
            if int(ciudad) == 0:
                print("Gracias por usar el SOFTWARE DEL CLIMA!")
                stop()
        except:
            if type(ciudad) != str:
                print("Inserte un dato valido!")
                return city()
            else:
                Busqueda(ciudad)
    except:
        print("Dato invalido!")
        return city()
    
def Busqueda(ciudad):
    response = session.get('https://www.google.com/search?q=el+clima+{}&rlz=1C1ONGR_esAR1008AR1008&oq=el+clima+{}&aqs=chrome.0.0i512j0i22i30l9.10551j1j7&sourceid=chrome&ie=UTF-8'.format(ciudad, ciudad))
    soup = BeautifulSoup(response.content, 'html.parser')

    weather = soup.find('span', {'id': 'wob_dc'}).text
    print("El clima en la ciudad de " + ciudad + " es " + weather)
    
    return city()


city()
