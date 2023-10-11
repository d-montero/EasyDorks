import sys,time
import urllib.parse
from googlesearch import search
try:
   from googlesearch import search
except ImportError:
    print("Error al importar el módulo")


if (sys.version[0] not in "3"):
   print("Versión de python instalada erronea, tienes que usar la versión 3.x")

class colors:
    ORANGE2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"   


text = "\n\t¿Hola estás listo para buscar dorks?"

for t in text:
    print(colors.ORANGE2 + t, end="")
    sys.stdout.flush()
    time.sleep(0.07)

try:
    data = input("\n[+]Quieres guardar la salida en un fichero (S/N)\n").strip()
    log = ("")
except KeyboardInterrupt:
    print("\n")
    print(f"{colors.ORANGE2} Se ha interrumpido el programa")
    time.sleep(0.5)
    print("Nos vemos pronto, Hackeame esta perro")
    time.sleep(0.5)
    sys.exit(1)
    
def fileSaver(data):
    file = open((log) + ".txt","a") #abrimos el fichero en modo apertura para escribir
    file.write(str(data))
    file.write("\n")
    file.close()
    
if data.startswith("s" or "S"):
    log = input("Dime el nombre del fichero: ")
    print("\n" + " " + "»" * 78 + "\n")
else:
    print("[!] No has decidido guardarlo en el fichero")
    print("\n" + " " + "»" * 78 + "\n")


dorksFiletype= [
    "filetype:pdf",
    "filetype:doc",
    "filetype:txt",
    "filetype:jpg",
    "filetype:xls",
    "filetype:ppt",
    "filetype:html",
    "filetype:xml",
]

dorksInurl = [
    "inurl:"
]

dorksInsite = [
    "insite:"

]


dorksExtension = [
    "extension:json",
    "extension:xml",
    # Agrega más dorks personalizados según sea necesario
]
def fileTypeDork(file_type):
    results = []
    for dork in dorksFiletype:
        if(dork.split(":")[1] == file_type):
            query = f"{dork} {file_type}"
            encoded_query = urllib.parse.quote(query)
            search_url = f"https://www.google.com/search?q={encoded_query}"
            results.append(search_url)
    return results

def searchInurlDork(keyword):
    results = []
    for dork in dorksInurl:
        query = f"{dork} {keyword}"
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}" #Cadena segura para url escapando caracteres especiales que no deberian estar
        results.append(search_url)
    return results


def searchInsiteDork(keyword):
    results = []
    for dork in dorksInsite:
        query = f"{dork} {keyword}"
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"
        results.append(search_url)
    return results


def ExtensionDork(keyword):
    results = []
    for dork in dorksFiletype:
        if(dork.split(":")[1] == keyword):
            query = f"{dork} {keyword}"
            encoded_query = urllib.parse.quote(query)
            search_url = f"https://www.google.com/search?q={encoded_query}"
            results.append(search_url)
    return results


def searchCombinedDorks(dork_functions):
    combined_results = []
    for dork_function in dork_functions:
        combined_results.append(dork_function)
    return combined_results

dork_functions = [fileTypeDork, searchInurlDork, searchInsiteDork]
search_results = searchCombinedDorks(dork_functions)

if log:
    fileSaver(search_results,log + ".txt")
    
    
def dorks(): #Si el usuario quiere buscar un dork en especifico 
    try:
        dork = input("\n[+] Introduce la query para el dork: ")
        amount = input("[+] Dime el número de sitios web que quieres ver: ")
        print ("\n ")

        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            counter = counter + 1
            print ("[+] ", counter, results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (counter, results)

            logger(data)
            time.sleep(0.1)

    except KeyboardInterrupt:
           print("\n")
           print(f"{colors.ORANGE2} Se ha interrumpido el programa")
           time.sleep(0.5)
           print("Nos vemos pronto, Hackeame esta perro")
           time.sleep(0.5)
           sys.exit(1)

    print ("[•] Hecho... Saliendo...")
    print ("\n\t\t\t\t\033[EasyDorks\033[0m")
    print ("\t\t\033[1;91m[!] Nos vemos, Hacking \033[0m😃\n\n")
    sys.exit()
