def acrostiche(file):
    l=[]
    s=''
    with open(file, encoding="utf-8") as lines:
        for line in lines:
            l.append(line[0])
        return s.join(l)

def nouveaux_heros(file, new_file):
    f1 = open(file, encoding= 'utf-8')
    text1 = f1.read()
    modified_text= text1.replace('Paul', 'Tom')
    modified_text= modified_text.replace('Pierre', 'Paul')
    modified_text= modified_text.replace('Jacqueline', 'Mathilde')
    f2 = open(new_file, mode='w')
    f2.write(modified_text)
    f2.close()
    return modified_text

def liste_des_mots(file):
    with open(file, encoding= 'UTF-8') as text:
        t = text.read().lower()
        t = t.replace(',','').replace('.', '').replace('?', '').replace("  ", " ").replace("'", " ").replace("-", " ")
        t= t.split(" ")
        t = sorted(set(t))
        return t