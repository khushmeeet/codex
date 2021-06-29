def save_html_page(soup):
    text = ""
    for i in soup.body.descendants:
        if i.name == 'section' or i.name == 'article' or i.name == 'main':
            for j in i.descendants:
                if j.name == 'img':
                    j['src'] = ''
            cc = ''
            for c in i.contents:
                cc += str(c)
            text += cc
    return text
