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
    for dork in dorksFiletype:
        if dork.split(":")[1] == file_type:
            query = f"{dork}"
            encoded_query = urllib.parse.quote(query)
            search_url = f"https://www.google.com/search?q={encoded_query}"
            results.append(search_url)
    return results


def searchInurlDork(keyword):
    results = []
    for dork in dorksInUrl:
        query = f"{dork}{keyword}"
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"  # Cadena segura para url escapando caracteres especiales que no deberian estar
        results.append(search_url)
    return results


def searchInTextDork(keyword):
    results = []
    for dork in dorksInText:
        query = f"{dork}{keyword}"
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"
        results.append(search_url)
    return results

def searchInTitleDork(keyword):
    results = []
    for dork in dorksInTitle:
        query = f"{dork}{keyword}"
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"
        results.append(search_url)
    return results

def searchInSiteDork(keyword):
    results = []
    for dork in dorksInSite:
        query = f"{dork}{keyword}"
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"
        results.append(search_url)
    return results

def searchInCoincidenceDork(keyword):
    results = []
    for dork in dorksInCoincidence:
        query = f"{dork}{keyword}{dork}"
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"
        results.append(search_url)
    return results

def searchInExclusionDork(keyword):
    results = []
    for dork in dorksInExclusion:
        query = f"{dork}{keyword}"
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"
        results.append(search_url)
    return results

def nada(arg):
    return [""]
