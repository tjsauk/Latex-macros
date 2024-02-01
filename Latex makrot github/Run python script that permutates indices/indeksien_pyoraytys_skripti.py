import pyperclip
import re

#etsii stringistä where kaikkien termien sub järjestyksen ja etsii subub indeksinumeron sen jälkeen
def etsi_subia_subista(where, sub, subsub):
    ordered = []
    #kaikkien etsittävien lauseiden listaaminen esiintymis järjestykseen
    for term in sub:
        ordered.append((term,where.find(term)))
    #niiden järjestäminen järjestykseen
    
    ordered.sort(key=lambda x: x[1])
    
    #tehdään kaikista yksi pötkylä
    yhdistettyna = ""
    for i in ordered:
        yhdistettyna = yhdistettyna + str(i[0])
    
    return yhdistettyna.find(subsub)

#sisään tuleva muokattava string
#pyperclip.paste()
imput_termi = pyperclip.paste() #"\partial^{\cnu} \cmu \g_{\cbeta \cmu}  + \partial_{\cmu}\g_{\cbeta \cnu} - \partial_{\cbeta} \g_{\cmu \cnu}"
print(imput_termi)
#ensin etsitään kaikki uniikit indeksit ja listataan indeksien paikat.

#lista kaikista indekseistä mitä löydettiin
indeksi_lista = []
#lista missä järjestyksessä indeksinimet esiintyy
indeksi_sijainnit = []

#etsii kaikki esiintymät ylä ja ala indekseille
etsi_yla = re.findall(r'\^{.*?}', imput_termi)
etsi_ala = re.findall(r'_{.*?}', imput_termi)

muokkaamaton = re.findall(r'\^{.*?}', imput_termi) + re.findall(r'_{.*?}', imput_termi)


#siivoaa löydetyistä turhat merkit pois
etsi_yla = [i[2:len(i)-1] for i in etsi_yla]
etsi_ala = [i[2:len(i)-1] for i in etsi_ala]
#poistetaan välilyönnit
etsi_yla = [i.replace(" ","") for i in etsi_yla]
etsi_ala = [i.replace(" ","") for i in etsi_ala]

#indeksi_termit = etsi_yla + etsi_ala
#indeksi_termit.sort(key=lambda x: x[1])
#loopataan molemmat listat läpi jotta löydetään indeksien nimet ja luodaan lista missä on indeksin termi ja sen esiintymis järjestyksen numero
for term in etsi_ala:
    terms = term.split("\\")
    for j in terms:
        if j not in indeksi_lista:
            indeksi_lista.append(j)
            indeksi_sijainnit.append((j,etsi_subia_subista(imput_termi, muokkaamaton, j)))
for term in etsi_yla:
    terms = term.split("\\")
   
    for j in terms:
        if j not in indeksi_lista:
            indeksi_lista.append(j)
            indeksi_sijainnit.append((j,etsi_subia_subista(imput_termi, muokkaamaton, j)))
#poistetaan tyhjät lista itemit
indeksi_sijainnit.remove(("",0))

#järjestetään lista itemit esiintymis järjestyksen mukaan
indeksi_sijainnit.sort(key=lambda x: x[1])

#korvataan kaikki merkit placeholderilla :1: :2: jne etsimällä ensin sub string
for match in muokkaamaton:
   
    original = match
    #vaihtamalla siihen kaikki indeksit placeholdereiksi
    for i in range(1,len(indeksi_sijainnit)+1):
        original = original.replace(indeksi_sijainnit[i-1][0], "!"+str(i)+"!") 
    
    imput_termi = imput_termi.replace(match, original)

   #Korvataan kaikki indeksit
for i in range(len(indeksi_sijainnit)):
    #jos ollaan viimeisessä indeksissä
   
    if i == len(indeksi_sijainnit)-1:
        
        sana = str(indeksi_sijainnit[0][0])
        
        imput_termi = imput_termi.replace("!" + str(len(indeksi_sijainnit)) + "!", sana)
    else:
        sana = str(indeksi_sijainnit[i+1][0])
        
        imput_termi = imput_termi.replace("!" + str(i+1) + "!", sana)

pyperclip.copy(imput_termi)



