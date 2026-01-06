import pymupdf

# doc = pymupdf.open("IKEA - Wikipedia.pdf")
# text = doc[0].get_text()
# print(text)

# out = open("output.txt", "wb") # create a text output
# for page in doc: # iterate the document pages
#     text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
#     out.write(text) # write text of page
#     out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
# out.close()


with pymupdf.open("IKEA - Wikipedia.pdf") as doc, open("output.txt", "w", encoding="utf-8") as out:
    for page in doc:
        out.write(page.get_text())
        out.write("\f")