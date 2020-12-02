passwordelements = []
with open('input.txt', 'r') as file:
    for line in file:
        linelist = line.split()
        passwordelement = {
            "countmin": int(linelist[0].split('-')[0]),
            "countmax": int(linelist[0].split('-')[1]),
            "letter": linelist[1],
            "password": linelist[2],
        }
        passwordelements.append(passwordelement)
validpasswordcount = 0
for passwordelement in passwordelements:
    lettercount = 0
    for letter in passwordelement["password"]:
        if letter == passwordelement["letter"]:
            lettercount = lettercount + 1
    if lettercount >= passwordelement["countmin"] and lettercount <= passwordelement["countmax"]:
        validpasswordcount = validpasswordcount + 1

print(validpasswordcount)
