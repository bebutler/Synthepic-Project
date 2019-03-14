import sys, csv, time
#sys to check for file, csv for file handling,and time or measuring runtime
from os import path

#Midi to Note Function
def MidiToPiano(curr_note):
    
       Endpoints = { '21': ':A0',
                     '22': ':As0',
                     '23': ':B0',
                     '24': ':C1',
                     '25': ':Cs1',
                     '26': ':D1',
                     '27': ':Ds1',
                     '28': ':E1',
                     '29': ':F1',
                     '30': ':Fs1',
                     '31': ':G1',
                     '32': ':Gs1',
                     
                     '33': ':A1',
                     '34': ':As1',
                     '35': ':B1',
                     '36': ':C2',
                     '37': ':Cs2',
                     '38': ':D2',
                     '39': ':Ds2',
                     '40': ':E2',
                     '41': ':F2',
                     '42': ':Fs2',
                     '43': ':G2',
                     '44': ':Gs2',
                     
                     '45': ':A2',
                     '46': ':As2',
                     '47': ':B2',
                     '48': ':C3',
                     '49': ':Cs3',
                     '50': ':D3',
                     '51': ':Ds3',
                     '52': ':E3',
                     '53': ':F3',
                     '54': ':Fs3',
                     '55': ':G3',
                     '56': ':Gs3',

                     '57': ':A3',
                     '58': ':As3',
                     '59': ':B3',
                     '60': ':C4',
                     '61': ':Cs4',
                     '62': ':D4',
                     '63': ':Ds4',
                     '64': ':E4',
                     '65': ':F4',
                     '66': ':Fs4',
                     '67': ':G4',
                     '68': ':Gs4',

                     '69': ':A4',
                     '70': ':As4',
                     '71': ':B4',
                     '72': ':C5',
                     '73': ':Cs5',
                     '74': ':D5',
                     '75': ':Ds5',
                     '76': ':E5',
                     '77': ':F5',
                     '78': ':Fs5',
                     '79': ':G5',
                     '80': ':Gs5',

                     '81': ':A5',
                     '82': ':As5',
                     '83': ':B5',
                     '84': ':C6',
                     '85': ':Cs6',
                     '86': ':D6',
                     '87': ':Ds6',
                     '88': ':E6',
                     '89': ':F6',
                     '90': ':Fs6',
                     '91': ':G6',
                     '92': ':Gs6',

                     
                     '93': ':A6',
                     '94': ':As6',
                     '95': ':B6',
                     '96': ':C7',
                     '97': ':Cs7',
                     '98': ':D7',
                     '99': ':Ds7',
                     '100': ':E7',
                     '101': ':F7',
                     '102': ':Fs7',
                     '103': ':G7',
                     '104': ':Gs7',
                     '105': ':A7',
                     '106': ':As7',
                     '107': ':B7',
                     '108': ':C8', #End of Piano Keys
                     
                     '109': ':Cs8',
                     '110': ':D8',
                     '111': ':Ds8',
                     '112': ':E8',
                     '113': ':F8',
                     '114': ':Fs8',
                     '115': ':G8',
                     '116': ':Gs8',
                     '117': ':A8',
                     '118': ':As8',
                     '119': ':B8',
                     '120': ':C9',
                     '121': ':Cs8',
                     '122': ':D9',
                     '123': ':Ds9',
                     '124': ':E9',
                     '125': ':F9',
                     '126': ':Fs9',
                     '127': ':Gs9',
                     'Blank':'Blank',
                     'rest':'rest'
                   
                    
                     }
       if curr_note[0] == "[":
             Note = curr_note
             return Note
       else:
              Note = Endpoints[curr_note]
              #print("Rewriting notes")
              return Note



#Filewriter Function
def FileWriter(song,curr_note,curr_value,amp,part):
    #print("Beginning TransCoding")
    with open(str(song)+' ' + str(part) +'.rb','a') as file:
       note = MidiToPiano(curr_note) #process midi to letter
       if curr_note[0] == "[":
            code = "play " + str(note) + ",release: " + str(curr_value) + ",amp: " + str(amp)
            sleep = "sleep " + str(curr_value)
            file.write(code + "\n")
            file.write(sleep + "\n")
       elif note == "rest":
            sleep = "sleep " + str(curr_value)
            file.write(sleep + "\n")
       elif note == "Blank":
           print("Skipped Header")
           time.sleep(1)
       else:
            code = "play " + str(note) + ",release: " + str(curr_value) + ",amp: " + str(amp)
            sleep = "sleep " + str(curr_value)
            file.write(code + "\n")
            file.write(sleep + "\n")
            
#Main program
def main():
    notes = []
    values = []
    song = input("Enter the Song title: ")
    part = input("Enter the Instrument Part: ")
    filename = str(input("Please enter the filename(ex. Transposition.csv): "))
    test = str(path.exists(filename))
    filetest = str(path.exists(str(song) + " " + str(part) + ".rb"))
    if test == "True" and filetest == "False":
        print("Prepped and ready!!")
    
    elif filetest == "True":
        print("ATTENTION YOU ARE ABOUT TO OVERWRITE A FILE!!!!!!!")
        cont = str(input("Do you want to continue? (Y/N)"))
        if cont == "Y" or cont == "y":
            print("Continuing...")
        elif cont == "N" or cont == "n":
            print("Crisis Averted")
            sys.exit()
        else:
            print("Crisis Averted")
            sys.exit()

    elif test == "False":
        print("The Transcription File Could Not be Located")
        print("Shutting Down...")
        time.sleep(2)
        sys.exit()
        
    synth = input('Please enter the synth name: ')
    amp = input("Enter the Amplitude: ")
    bpm = input("Enter the Tempo: ")
    with open(filename, 'r') as f:
            reader = csv.reader(f)
 
        # read file row by row
            rowNr = 0
            for row in reader:
        # Skip the header row.
                if rowNr >= 1:
                    notes.append(row[0])
                    values.append(row[1])
        # Increase the row number
                rowNr = rowNr + 1
    #print(values) Checking values don't need to uncomment it
    print("Done loading file details, moving on to transcoding process!")
    f.close()
    file = open(str(song) + ' ' + str(part) + '.rb', 'w') #Create File
    print("Transpository Created Successfully!!!!")
    time.sleep(2)
    file.write("use_bpm " + str(bpm) + "\n")
    file.write("use_synth :" + str(synth) + "\n")
    file.write("# " + str(part)+ "\n")
    file.close()
    print("File Prepped!!!")
    print("Transposing...")
    counter = 0
    StartTime = time.time()
    while counter in range(len(notes)): 
        curr_note = notes[counter]
        curr_value = values[counter]
        FileWriter(song,curr_note,curr_value,amp,part)
        counter += 1

    phaseTime = time.time()-StartTime
    print("I wrote: "+str(counter) + " lines for you in " +str(round(phaseTime)) + " seconds.")
    esc = input("Would you like to TransCode another file? (Yes = 'Y' Quit = 'exit()')")
    while esc != "exit()":
        notes = []
        values = []
        song = input("Enter the Song title: ")
        part = input("Enter the Instrument Part: ")
        filename = str(input("Please enter the filename(ex. Transposition.csv): "))
        test = str(path.exists(filename))
        filetest = str(path.exists(str(song) + " " + str(part) + ".rb"))
        if test == "True" and filetest == "False" :
            print("Prepped and ready!!")
    
        elif filetest == "True":
            print("ATTENTION YOU ARE ABOUT TO OVERWRITE A FILE!!!!!!!")
            cont = str(input("Do you want to continue? (Y/N)"))
            if cont == "Y" or cont == "y":
                print("Continuing...")
            elif cont == "N" or cont == "n":
                print("Crisis Averted")
                sys.exit()
            else:
                print("Crisis Averted")
                sys.exit()

        elif test == "False":
            print("The Transcription File Could Not be Located")
            print("Shutting Down...")
            time.sleep(2)
            sys.exit()
            
        synth = input('Please enter the synth name: ')
        amp = input("Enter the Amplitude: ")
        bpm = input("Enter the Tempo: ")
        counter = 0
        StartTime = time.time()
        
        with open(filename, 'r') as f:
            reader = csv.reader(f)
 
        # read file row by row
            rowNr = 0
            for row in reader:
        # Skip the header row.
                if rowNr >= 1:
                    notes.append(row[0])
                    values.append(row[1])
        # Increase the row number
                rowNr = rowNr + 1
        
        print("Done loading file details, moving on to transcoding process!")
        f.close()
        file = open(str(song) + ' ' + str(part) + '.rb', 'w') #Create File
        print("Transpository Created Successfully!!!!")
        time.sleep(2)
        file.write("use_bpm " + str(bpm) + "\n")
        file.write("use_synth :" + str(synth) + "\n")
        file.write("# " + str(part)+ "\n")
        print("File Prepped!!!")
        file.close()
        print("Transposing...")
        counter = 0
        while counter in range(len(notes)): 
            curr_note = notes[counter]
            curr_value = values[counter]
            FileWriter(song,curr_note,curr_value,amp,part)
            print("Done writing line " + str(counter))
            counter += 1
        
        
        phaseTime = time.time()-StartTime
        print("I wrote: "+str(counter) + " lines for you in " +str(round(phaseTime)) + " seconds.")
        esc = input("Would you like to TransCode another file? (Yes = 'Y' Quit = 'exit()')")

    
    print("Shutting Down...")
    time.sleep(2)
    file.close()


        


     
main()
