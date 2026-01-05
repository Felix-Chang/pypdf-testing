import pymupdf 

doc = pymupdf.open("IKEA - Wikipedia.pdf")
text = doc[0].get_text()
print(text)