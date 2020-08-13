def domain_name(url):
    if url[4] == "s":
        new_url = url.replace("https://", "")
        if new_url[:4] == "www.":
            new_url = new_url.replace("www.", "")
    elif url[4] == ":":
        new_url = url.replace("http://", "")
        if new_url[:4] == "www.":
            new_url = new_url.replace("www.", "")
    else:
        new_url = url.replace("www.", "")
    split = new_url.split("/")
    l = split[0]
    l1 = l.split(".")
    return l1[0]
print(domain_name("www.zombie-bites.com"))
string = "kol"
print(string.index("o"))
