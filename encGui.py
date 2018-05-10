import tkinter
import encounters
  
def again():
    weather = encounters.isRain()
    wLabel.config(text=weather)
    terrain = tBox.curselection()
    terrain = int(terrain[0]) + 1
    mornEnc = encounters.isEncounter()
    aftEnc = encounters.isEncounter()
    evEnc = encounters.isEncounter()
    if mornEnc:
        encM = encounters.whatEncounter(terrain)
    else:
        encM = 'None'
    if aftEnc:
        encA = encounters.whatEncounter(terrain)
    else:
        encA = 'None'
    if evEnc:
        encE = encounters.whatEncounter(terrain)
    else:
        encE = 'None'
    mLabel.config(text=encM)
    aLabel.config(text=encA)
    eLabel.config(text=encE)

def setWidget():
    wFrame.grid(row=0,column=0,padx=5,pady=5)
    wLabel.grid(row=0,column=0,padx=5,pady=5)
    runBut.grid(row=0,column=1,padx=5,pady=5)
    tFrame.grid(row=1,column=1,rowspan=4,padx=5,pady=5)
    tBox.grid(row=1,column=1,rowspan=4,padx=5,pady=5)
    mFrame.grid(row=1,column=0,padx=5,pady=5)
    mLabel.grid(row=1,column=0,padx=5,pady=5)
    aFrame.grid(row=3,column=0,padx=5,pady=5)
    aLabel.grid(row=3,column=0,padx=5,pady=5)
    eFrame.grid(row=5,column=0,padx=5,pady=5)
    eLabel.grid(row=5,column=0,padx=5,pady=5)


top = tkinter.Tk()
wFrame = tkinter.LabelFrame(top,text='Weather Forecast',height=2,width=40)
wLabel = tkinter.Label(wFrame,text='',height=2,width=40)
mFrame = tkinter.LabelFrame(top,text='Morning Encounter',height=2,width=40)
mLabel = tkinter.Label(mFrame,text='',height=2,width=40)
aFrame = tkinter.LabelFrame(top,text='Afternoon Encounter',height=2,width=40)
aLabel = tkinter.Label(aFrame,text='',height=2,width=40)
eFrame = tkinter.LabelFrame(top,text='Evening Encounter',height=2,width=40)
eLabel = tkinter.Label(eFrame,text='',height=2,width=40)
tFrame = tkinter.LabelFrame(top,text='Terrain Options',height=2,width=20)
tOpts = ['Beach','Jungle: No Undead','Jungle: Lesser Undead',
        'Jungle:Greater Undead','Mountains','Rivers','Ruins',
        'Swamp','Wasteland']
tBox = tkinter.Listbox(top)
count = 1
for opt in tOpts:
    count += 1
    tBox.insert(count,opt)
runBut = tkinter.Button(top,text='Run',
                        height=2,width=20,
                        command=again)
top.title("Encounters")

setWidget()
top.mainloop()
