import urllib.parse

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

dorksInurl = [
    "inurl:"
]

dorksInsite = [
    "intext:"

]

dorksExtension = [
    "extension:json",
    "extension:xml",
    # Agrega más dorks personalizados según sea necesario
]


def fileTypeDork(file_type):
    results = []
    for dork in dorksFiletype:
        if dork.split(":")[1] == file_type:
            query = f"{dork}"
            encoded_query = urllib.parse.quote(query)
            search_url = f"https://www.google.com/search?q={encoded_query}"
            results.append(search_url)
    return results


def searchInurlDork(keyword):
    results = []
    for dork in dorksInurl:
        query = f"{dork}{keyword}"
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"  # Cadena segura para url escapando caracteres especiales que no deberian estar
        results.append(search_url)
    return results


def searchInsiteDork(keyword):
    results = []
    for dork in dorksInsite:
        query = f"{dork}{keyword}"
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"
        results.append(search_url)
    return results


def ExtensionDork(keyword):
    results = []
    for dork in dorksFiletype:
        if dork.split(":")[1] == keyword:
            query = f"{dork} {keyword}"
            encoded_query = urllib.parse.quote(query)
            search_url = f"https://www.google.com/search?q={encoded_query}"
            results.append(search_url)
    return results


def nada(arg):
    return [""]
