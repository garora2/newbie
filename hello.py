import os
import webbrowser

newstr = "Hello"
newstr += "World, Let's go to a new site!!"
print newstr

urlstr = "http://" +  raw_input('Which URL do you want to go to? ')
print urlstr

os.system('./a.out > tea.out')
os.system('cat tea.out')
webbrowser.open(urlstr)

