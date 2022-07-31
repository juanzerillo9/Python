import requests
from bs4 import BeautifulSoup

URL = "https://www.0223.com.ar/"
page = requests.get(URL)

soup = BeautifulSoup(page.text, "html.parser")

results = soup.findAll('article')
titulos = []

for job_element in results:
    titulo = job_element.find(class_="nota__titulo-item")
    print(titulo.text)
    
    
print(titulos)
"""   
 <div class="nota__titulo">
		                <a href="/nota/2022-7-22-13-52-0-impactante-choque-en-fortunato-de-la-plaza-y-einstein">
		                    <h2 class="nota__titulo-item">
		                        Hospitalizan a dos conductores tras un choque impactante en Fortunato de la Plaza y Einstein
	                                </h2>
	                            </a>
		                </div>      
"""