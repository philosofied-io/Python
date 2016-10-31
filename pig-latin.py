#word = raw_output('please enter word to be transalted ')
#print word[1:] + word[0]

#https://www.youtube.com/watch?v=0mAGb6sCZWc&list=PL_hH8gINtYWWjQGyYG01eg7g2WliTPV5t&index=68
# for scraping
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('#url goes here#').read()

soup = BeautifulSoup(html)

#print(html) #OR
#print soup.FindAll('div', {"class": "wp_quotepage"})
for section in soup.findAll('div', {"class": "wp_quotepage"})
print(section)


for section in soup.findAll('div',{"class":"wp_quotepage"}):
	quote = section.findChildren()[0].renderContents()
	author = section.findChildren()[1].renderContents()
	print (quote, author)
	break


import urllib.request
htmlfile = urllib.request.urlopen("http://google.com")
htmltext = htmlfile.read()
print(htmltext)
