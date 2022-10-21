import datetime

mystery_joyful = ['Anunciation','Visitation','Nativity','Presentation','Finding of Jesus at the Temple']
mystery_sorrowful = ['Agony in the Garden','Scourging at the Pillar','Crowning with Thorns','Carrying of the Cross','Crucifixion']
mystery_glorious = ['Ressurection','Ascension','Descent of the Holy Spirit upon the Apostles','Assumption of Our Lady','Coronation']
mystery_luminous = ['Baptism of Jesus at the River Jordan','Wedding at Cana','Proclamation of the Kingdom of God','Transfiguration','Institution of the Eucharist']

now = datetime.datetime.now()

print("The mysteries of the rosary")
print("1. Current days mysteries")
print("2. Custom days mysteries\n")
dayop = int(input("Choose option (1 or 2): "))
if dayop == 1:
    dayname = now.strftime("%A")
elif dayop == 2:
    dayname = input("Enter the day name (eg. Sunday): ")
else:
    print("Error")
print("\n")

if dayname=="Monday" or dayname=="Saturday":
    print(dayname,"- Joyful mystery:",mystery_joyful)
    for x in mystery_joyful:
        print(x)

elif dayname=="Tuesday" or dayname=="Friday":
    print(dayname,"- Sorrowful mystery:",mystery_sorrowful)
    for x in mystery_sorrowful:
        print(x)

elif dayname=="Sunday" or dayname=="Wednesday":
    print(dayname,"- Glorious mystery:",mystery_glorious)
    for x in mystery_glorious:
        print(x)

elif dayname=="Thursday":
    print(dayname,"- Luminous mystery:",mystery_luminous)
    for x in mystery_luminous:
        print(x)

else:
    print("ERROR")