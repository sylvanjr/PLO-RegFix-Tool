
from bs4 import BeautifulSoup
import os
import datetime

# Replace all p tags attributes to <p class="indent">
def main():
    directory = r'C:\Users\gidayast\Documents\Python\REGS Team\samples'
    dir2 = ''
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        if file.endswith(".xml"):
            print(file)

            with open(file) as f:
                contents = f.read()
                soup = BeautifulSoup(contents, 'xml')

                # Section attributes with space before open parenthesis
                if filename[0:2].lower() == 'sc':
                    #dir2 = r'C:\Users\gidayast\Documents\Python\REGS Team\Output\Section Content'

                    for secTags in soup.find_all('section_content'):
                        if " (" in secTags['section']:
                            current = str(secTags['section'])
                            newVal = current.replace(" (", "(")
                            secTags['section'] = newVal

                # P class="indent"
                elif filename[0:2].lower() == 'pc':
                    #dir2 = r'C:\Users\gidayast\Documents\Python\REGS Team\Output\P Class'

                    for pTags in soup.find_all('p'):
                        pTags.attrs.clear()
                        pTags.attrs["class"] = 'indent'

                # All empty tags
                elif filename[0:2].lower() == 'et':
                    #dir2 = r'C:\Users\gidayast\Documents\Python\REGS Team\Output\Empty Tags'
                    whiteList = ['p', 'section_content']
                    for empTags in soup.find_all():
                        if (len(empTags.get_text(strip=True)) == 0): # and (empTags.name not in whiteList):
                            empTags.extract()

                # Replace whitespaces and tabs to a single space
                elif filename[0:2].lower() == "ws":
                    #dir2 = r'C:\Users\gidayast\Documents\Python\REGS Team\Output\Whitespaces and Tabs'

                    for pTags in soup.find_all('p'):
                        currText = pTags.get_text()
                        newText = currText.split()
                        newText = ' '.join(newText)
                        a = currText.replace(currText, newText)
                        pTags.string = a

                else:
                    None

                # Delete empty tags
                #for empTags in soup.find_all():
                #    if len(empTags.get_text(strip=True)) == 0:
                #        empTags.extract()

                x = soup.prettify()

                # Check if folder for current day exists
                # If not, automatically will create one
                dir2 = r'C:\Users\gidayast\Documents\Python\REGS Team\Output'
                now = datetime.datetime.now()
                date = now.strftime('%m%d%y')

                newFolder = os.path.join(dir2, date)

                checkFolder = os.path.isdir(newFolder)

                if not checkFolder:
                    os.makedirs(newFolder)

                file = os.path.join(newFolder, filename)
                with open(file, "w+") as f:
                    f.write(str(x))
        else:
            continue

# File path
# os.path.dirname(__file__)


class xmlUpdate:
    def pClass(self):

        for pTags in soup.find_all('p'):
            pTags.attrs.clear()
            pTags.attrs["class"] = 'indent'

    def sectionVal(file, soup):

        for secTags in soup.find_all('section_content'):
            if " (" in secTags['section']:
                current = str(secTags['section'])
                newVal = current.replace(" (", "(")
                secTags['section'] = newVal

if __name__ == "__main__":
    main()