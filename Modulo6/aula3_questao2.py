def extrair_dominios(urls):
    dominios = [url[4:-4] for url in urls]
    return dominios

urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

dominios = extrair_dominios(urls)

print("URLs:", urls)
print("Domínios:", dominios)
