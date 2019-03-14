import random
import smtplib, math, ssl
from email.mime.text import MIMEText


fresh = ["finest","instrument","they","sea","us","ask"
"plural","know","no","opportunity","wheel","with"
"swim","ship","below","flat","castle","basic"
"lost","cold","noon","direct","sweet","with"
"usual","anything","slave","printed","day","ask"
"repeat","plates","shinning","musical","offer","theory"
"fourth","muscle","somehow","voyage","trouble","uncle","immediately","realize","planned","quiet","perhaps","disappear"
"lack","forgot","trunk","bear","down","take"
"friendly","usually","border","finally","fall","should"
"herself","spend","crack","cell","clay","thought"
"explore","dug","business","test","these","railroad"
"choose","bean","jungle","hair","ride","diameter"
"valley","test","lot","familiar","capital","found","bite","sleep","strange","mood","independent","modern"
"clay","wave","dear","refused","sat","swim"
"pink","instance","army","larger","eleven","pleasure"
"form","finish","adventure","wet","hunter","rays"
"especially","tightly","pleasant","shake","arrive","desert"
"connected","tail","guess","too","atmosphere","last"
"floor","north","muscle","powder","try","flag","manufacturing","create","listen","shirt","fog","maybe"
"burn","badly","article","brain","draw","knew"
"string","wish","wild","coast","grow","child"
"sheet","cook","needed","island","merely","pitch"
"tightly","watch","become","raw","smoke","fireplace"
"treated","mountain","store","silver","column","tea"
"alphabet","settle","nails","bee","front","frozen","remarkable","sit","sum","organization","use","private"
"height","kids","were","flame","importance","jet"
"business","shirt","system","church","lovely","cotton"
"train","find","proud","earth","discover","dirt"
"doctor","perfectly","space","joy","hall","mission"
"offer","arrangement","mirror","century","offer","fur"
"dirty","egg","body","rays","enemy","because","avoid","meat","serious","damage","wall","very"
"afraid","letter","discovery","mental","silver","lead"
"football","eaten","tail","far","terrible","move"
"coffee","star","fastened","quarter","foot","scientist"
"modern","journey","farther","change","freedom","depend"
"mountain","whose","doll","locate","practice","to"
"yard","nearer","oil","shade","greater","trick"]


key = 4

def main():
    myMessage = random.choice(fresh)
    myKey = 4
    print("I made my choice")
    ciphertext = encryptMessage(myKey, myMessage)
    print("Encryption complete")
    decrypt = decryptMessage(myKey, ciphertext)
    

    print(ciphertext)#'|')

    #pyperclip.copy(ciphertext) #copies the encrpyted text to the clipboard

    SendMail(ciphertext)
    
def encryptMessage(key, message):
    ciphertext = [''] * key
    for column in range(key):
        currentIndex = column


        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]
            currentIndex += key

    return ''.join(ciphertext)


def decryptMessage(key, message):

    numOfColumns = int(math.ceil(len(message) / float(key)))

    numOfRows = key

    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    plaintext = [''] * numOfColumns

    column = 0

    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1
    return ''.join(plaintext)

def SendMail(code):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "nomr3151@gmail.com"
    receiver_email = "butlerb598@gmail.com"
    password = input("Please enter your password: ")
    message = """\
    Subject: Hi there,this is the Raspberry Pi
    I'm sending you this week's password
    here it is: """ + str(code)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email, message)
        server.quit()


#main()
