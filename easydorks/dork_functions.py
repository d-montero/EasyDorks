import urllib.parse
import requests

# dork functions

dorksFiletype = [
    "filetype:pdf",
    "filetype:doc",
    "filetype:txt",
    "filetype:jpg",
    "filetype:xls",
    "filetype:ppt",
    "filetype:html",
    "filetype:xml",
]

dorksInUrl = [
    "inurl:"
]

dorksInText = [
    "intext:"
]

dorksInTitle = [
    "intitle:"
]

dorksInSite = [
    "site:"
]

dorksInCoincidence = [
    "\""
]

dorksInExclusion = [
    "-"
]


def fileTypeDork(file_type):
    results = []
    file_type = file_type[0]
    for dork in dorksFiletype:
        if dork.split(":")[1] == file_type:
            query = f"{dork}"
            encoded_query = urllib.parse.quote(query)
            search_url = f"https://www.google.com/search?q={encoded_query}"
            results.append(search_url)
    return results


def searchInurlDork(keyword):
    results = []
    keyword = keyword[0]
    for dork in dorksInUrl:
        query = f"{dork}{keyword}"
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"  # Cadena segura para url escapando caracteres especiales que no deberian estar
        results.append(search_url)
    return results


def searchInTextDork(keyword):
    results = []
    keyword = keyword[0]
    for dork in dorksInText:
        query = f"{dork}{keyword}"
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"
        results.append(search_url)
    return results

def searchInTitleDork(keyword):
    results = []
    keyword = keyword[0]
    for dork in dorksInTitle:
        query = f"{dork}{keyword}"
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"
        results.append(search_url)
    return results

def searchInSiteDork(keyword):
    results = []
    keyword = keyword[0]
    for dork in dorksInSite:
        query = f"{dork}{keyword}"
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"
        results.append(search_url)
    return results

def searchInCoincidenceDork(keyword):
    results = []
    keyword = keyword[0]
    for dork in dorksInCoincidence:
        query = f"{dork}{keyword}{dork}"
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"
        results.append(search_url)
    return results

def searchInExclusionDork(keyword):
    results = []
    keyword = keyword[0]
    for dork in dorksInExclusion:
        query = f"{dork}{keyword}"
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"
        results.append(search_url)
    return results

def nada(arg):
    return [""]


def serachRelated(keyword):
    results = []
    keyword = keyword[0]
    query = f"{'related:'}{keyword}"
    encoded_query = urllib.parse.quote(query)
    search_url = f"https://www.google.com/search?q={encoded_query}"
    results.append(search_url)
    return results


def serachPrefer(keyword):
    results = []
    keyword = keyword[0]
    query = f"{'prefer:'}{keyword}"
    encoded_query = urllib.parse.quote(query)
    search_url = f"https://www.google.com/search?q={encoded_query}"
    results.append(search_url)
    return results


def searchIntervalo(keyword):
    results = []
    query = f"{keyword[0]}{'..'}{keyword[1]}"
    encoded_query = urllib.parse.quote(query)
    search_url = f"https://www.google.com/search?q={encoded_query}"
    results.append(search_url)
    return results


##Funciones de busqueda de dorks para shodan


SHODAN_API_KEY = "tu_clave_de_api_de_shodan"  # Reemplaza con tu clave de API de Shodan

def searchDatabase(keyword):
    results = []
    keyword = keyword[0]
    query = f"{keyword}"  
    shodan_url = f"https://api.shodan.io/shodan/host/search?key={SHODAN_API_KEY}&query={query}"

    try:
        response = requests.get(shodan_url)
        if response.status_code == 200:
            data = response.json()
            for result in data['matches']:
                ip_address = result['ip_str']
                results.append(ip_address)
        else:
            results.append(f"Error en la solicitud: {response.status_code}")
    except Exception as e:
        results.append(f"Error: {str(e)}")

    return results


#Ejemplo para la prueba "mysql port 3306"

def searchPort(keyword):
    results = []
    keyword = keyword[0]
    query = f"port:{keyword}"  
    shodan_url = f"https://api.shodan.io/shodan/host/search?key={SHODAN_API_KEY}&query={query}"

    try:
        response = requests.get(shodan_url)
        if response.status_code == 200:
            data = response.json()
            for result in data['matches']:
                ip_address = result['ip_str']
                results.append(ip_address)
        else:
            results.append(f"Error en la solicitud: {response.status_code}")
    except Exception as e:
        results.append(f"Error: {str(e)}")

    return results

def specificOperatingSystem(keyword):
    results = []
    keyword = keyword[0]
    query = f"os:{keyword}"
    shodan_url = f"https://api.shodan.io/shodan/host/search?key={SHODAN_API_KEY}&query={query}"
    
    try:
        response = requests.get(shodan_url)
        if response.status_code == 200:
            data = response.json()
            for result in data['matches']:
                ip_address = result['ip_str']
                results.append(ip_address)
        else:
            results.append(f"Error en la solicitud: {response.status_code}")
    except Exception as e:
        results.append(f"Error: {str(e)}")

    return results

def webServers(keyword):
    results = []
    keyword = keyword[0]
    query = f"product:{keyword}"
    shodan_url = f"https://api.shodan.io/shodan/host/search?key={SHODAN_API_KEY}&query={query}"
    
    try:
        response = requests.get(shodan_url)
        if response.status_code == 200:
            data = response.json()
            for result in data['matches']:
                ip_address = result['ip_str']
                results.append(ip_address)
        else:
            results.append(f"Error en la solicitud: {response.status_code}")
    except Exception as e:
        results.append(f"Error: {str(e)}")

    return results


