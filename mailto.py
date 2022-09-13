from time import sleep
import webbrowser
import urllib.parse
    

recipients  = [emailaddress.strip().lower() for emailaddress in open("to.txt.rc","r").readlines()]
templatelst = open("template.md","r").readlines()
subject     = templatelst[0].strip("Subject:").strip()
body        = "".join(templatelst[2:])
    

for emailaddress in recipients :
    a = webbrowser.open_new('mailto:?to=' + emailaddress + '&subject=' + urllib.parse.quote(subject) + '&body=' + urllib.parse.quote(body))
    sleep(2)

set_breakpoint_here = ""