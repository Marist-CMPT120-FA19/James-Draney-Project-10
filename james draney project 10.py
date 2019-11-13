#James Draney Project 10
#james.draney1@marist.edu
#letsgetit

def main():
    #Gets files from the user
    inputsentencefile=input("What is the file to be censored? ")
    inputcensorfile=input("What is the censored words file? ")
    censor=open(inputcensorfile, 'r')
    fixthis=open(inputsentencefile, 'r')

    censoredwords=censor.read().split(" ")
    plsfixthis=fixthis.read().split(' ')
    #Tells program what to sensor 
    for i in censoredwords:
        for f in range(0,len(plsfixthis)):
            if i ==plsfixthis[f]:
                plsfixthis[f]='*'*len(i)
    #rewrites the file to censor it
    censor.close()
    fixthis.close()
    fixthis=open(inputsentencefile, 'w')

    for i in plsfixthis:
        fixthis.write(i)
        fixthis.write(" ")

    fixthis.close()


main()
        

