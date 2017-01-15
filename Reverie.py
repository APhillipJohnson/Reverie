'''
Code author: A. Phillip Johnson
Project Members: A. Phillip Johnson, Ryan Brock, Jaqueline Kientzler
Reverie code

Webscraping to mimic a deceased person for grieving purposes
'''


from bs4 import BeautifulSoup as BeautifulSoup
import re
import string
Phil_dict={}



#==========================================================
def main():
    
    Phil_dict['Phillip']=[]
    files=open('messages.html', 'r')
    soup = BeautifulSoup(files, 'html.parser')
    soup.prettify()
    conversation=soup.find_all('p')
    Phil_dict['Phillip'].append(conversation)
    output= open('conversation.txt','w')
    outbound=str(Phil_dict)
    outbound.replace('<p>', '')
    outbound.replace('</p>', '')
    output.write(outbound)
    output.close()

            
            
            
            
if __name__ == '__main__':
    main()
