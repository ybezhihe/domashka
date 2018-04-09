import re
with open ("кр2.txt" , encoding="utf-8") as f:
    x = f.read()
    d = x.split("</w>")
    a = re.search("w lemma="[a-z]+"", d)
        
