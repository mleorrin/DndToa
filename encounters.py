def isRain():
    import random
    wRoll = random.randint(1,20)
    if wRoll <=16:
        weather = 'Occasional light rain.\nBUGS!!!!!!'
    elif wRoll <=19:
        weather = 'Heavy rain; 150 ft visibility'
    elif wRoll == 20:
        weather = 'Storm; no canoe; Con save for exhaustion (DC10)'
    return weather

def isEncounter():
    import random
    roll = random.randint(1,20)
    if roll >= 14:
        return True
    return False

def whatEncounter(terrain):
    import random
    impList = []
    encFile = open('tombEncounters.csv','r',encoding='utf8')
    encList = encFile.read().splitlines()
    for n in range(len(encList)):
        encList[n] = encList[n].split(',')
    encList[0][0] = 'Aarakocra'
    for i in range(len(encList)):
        posRolls = encList[i][terrain]
        try:
            roll1 = int(posRolls[:2])
            try:
                roll2 = int(posRolls[3:])
            except IndexError:
                roll2 = roll1
            posRolls = [roll1,roll2]
            impList.append([encList[i][0],posRolls])
        except ValueError:
            check = 1
    roll = random.randint(1,100)
    impList[-1][1][1] = 100
    for i in range(len(impList)):
        encRoll = impList[i][1]
        if roll >= int(encRoll[0]) and roll <= int(encRoll[1]):
            return impList[i][0]

def main():
    print(isRain())
    terrain = int(input('What kind of terrain? (1-9)'))
    morning = isEncounter()
    if morning:
        print('Morning Encounter:')
        print(whatEncounter(terrain))
    afternoon = isEncounter()
    if afternoon:
        print('Afternoon Encounter:')
        print(whatEncounter(terrain))
    evening = isEncounter()
    if evening:
        print('Evening Encounter:')
        print(whatEncounter(terrain))
    if not morning and not afternoon and not evening:
        print('No encounters')
    
    
