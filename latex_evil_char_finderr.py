import pathlib
p = pathlib.Path(".")
# search for offending (U+200B) characters that mess up "make latexpdf" command
# in file basics_ukr.md
#filenames = ["basics_ukr.md"]
filenames = list(p.glob("**/*.md"))
print(filenames)


evil_codes = ["\u660E"] # shall be replaced with nothing
infected_files = []
for filename in filenames:
    print("processing:", filename)
    with open(filename) as myfile:
        text = myfile.read()
    for evil in evil_codes:
        if evil in text:
            print("found:", evil_codes.index(evil), "in", filename)
            infected_files.append(filename)
print("infected files:", infected_files)
