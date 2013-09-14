import os
import urllib2
import time

print "Script running..."
start_time = time.time()

try:
  url_read = urllib2.urlopen('http://codepad.org/recent')
  url_str = url_read.read()
except:
  print "Error in opening the url."

link_start = 0
url_list = []

try:
  while True:
    link_start = url_str.find("a href",link_start+1)
    if link_start == -1:
      break
    link_end = url_str.find(">",link_start)
    link_text = url_str[link_start:link_end]
    if link_text.find("http://codepad.org/") == 8:
      url_list.append(link_text[8:len(link_text)-1])

  print "Links have been extracted."
except:
  print "There was a problem extracting the links from the page text. Please run around in circles while screaming about conspiracy theories."
try:
  fopen = open('codepad_links.txt','r')
except:
  print "URL list file does not exist, creating."
  previous_urls = "none"
else:
  previous_urls = fopen.read()
  fopen.close()

fopen = open('codepad_links.txt','a')
error_num = 0

for url in url_list:
  if previous_urls.find(url)==-1:
    url_read = urllib2.urlopen(url)
    url_str = url_read.read().lower()
    start = url_str.find('<span class="heading">output:</span>')
    if (url_str.find("error",start)>-1):
      title_start = url_str.find("<title>")
      title_end = url_str.find("<",title_start+1)
      paste_info = url_str[title_start+7:title_end]
      paste_info = paste_info.replace(" - codepad","")
      paste_info = paste_info.replace("\n"," ")
      fopen.write(paste_info + ", " + url + "\n")
      error_num += 1
    
fopen.close()
end_time = time.time()

print str(error_num) + " new error(s) have been found view codepad_links.txt for the list."
print "The script was executed in " + str(end_time-start_time) + " second(s)."

#  <a href="http://codepad.org/jz2E6JjS">view</a>
