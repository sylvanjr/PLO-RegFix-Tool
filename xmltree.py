
from bs4 import BeautifulSoup
import os
import datetime
import re

file = r'C:\Users\gidayast\Downloads\P tags.xml'

with open(file) as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'xml')

    for pTags in soup.find_all('p'):
        out = pTags.get("class")
        if out == "center":
            pTags.attrs.clear()
            pTags.attrs["class"] = 'center'
        else:
            pTags.attrs.clear()
            pTags.attrs["class"] = 'indent'

    x = soup.prettify()
    print(x)



        #print(nextElem)






        #tag1 = pTags.find(text=pText)
        #print(tag1)

    #x = soup.prettify()
    #print(x)















        #pattern = re.compile("([\n])|([\t ]{1,})|([\ ]{2,})")
        #re.sub(pattern, ' ', str(allTags))
        #print(pTags.text)
        #pText = pTags.text
        #pTags = re.sub(pattern, ' ', str(pTags))
        #print(empTags)

    #x = soup.prettify()
    #print(x)




        #if text == "" or text == "\n" or text == " ":
        #    None
        #else:
        #    newText = tdText.get_text()
        #    newP = soup.new_tag("p", attrs={'class':'indent'})
        #    newP.string = newText
        #    print(newP)

            #pClass.append(newP)
    #print(newP)
    #x = soup.prettify()
    #print("This is x:")
    #print(x)

    #for table in x.find('table'):
    #    table.parent.insert_after(newP)
        #print(newP)
    #x = soup.prettify()
    #print(x)