
talonIPs = open("talon.txt","r")
print("opening Talon.txt")

ufwReady = open("UFWTalon.sh","w")

for line in talonIPs:
    ufwReady.write('ufw deny from '+line)
    ufwReady.write('wait')

print("Done")
