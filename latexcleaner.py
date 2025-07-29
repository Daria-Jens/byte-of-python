import pathlib
p = pathlib.Path(".")
# search for offending (U+200B) characters that mess up "make latexpdf" command
# in file basics_ukr.md
#filenames = ["basics_ukr.md"]
filenames = list(p.glob("**/*.md"))
print(filenames)


evil_codes = ["\u200B", "\u0301", "\u3002", "\u7B80",
              "\u660E"] # shall be replaced with nothing

for filename in filenames:
    print("processing:", filename)
    clean = True
    with open(filename) as myfile:
        text = myfile.read()
    for evil in evil_codes:
        if evil in text:
            clean = False
            print("replacing:", evil_codes.index(evil))
            text = text.replace(evil, "")

    if not clean:
        with open(filename, "w") as myfile:
            myfile.write(text)
        print("written:", filename)
