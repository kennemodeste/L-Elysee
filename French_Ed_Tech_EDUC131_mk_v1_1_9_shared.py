# importing required modules
import string
import requests
import multiprocessing
import time
import random
import tempfile
import os
import os.path
from playsound import playsound
from colorama import Fore, Back, Style, Cursor

from urllib.request import urlopen
from shutil import copyfileobj
from tempfile import NamedTemporaryFile

def Menu():
    print()
    flag = Fore.BLUE + '#'*35 + Fore.WHITE + "#"*35 + Fore.RED + '#'*35 + '\n'
    flag2 = Fore.BLUE + '#'*35 + Fore.WHITE + "#"*5 + "    Welcome to Élysée    "+ Fore.WHITE + "#"*5 + Fore.RED + '#'*35
    flag3 = Fore.BLUE + '#'*35 + Fore.WHITE + "#"*9 + "                 "+ Fore.WHITE + "#"*9 + Fore.RED + '#'*35
    
    print(f'{flag*5:>16}', end = '')
    print(f'{flag3:>16}')
    print(f'{flag2:>16}')
    print(f'{flag3:>16}')
    print(f'{flag*5:>16}', end = '')

    print (Fore.WHITE + '' , end = '')
    message = " "*12 + "Have  Fun  Learning  French !!!"
    sound_on = "\n\t\t\t\t\t(*** Please turn the sound ON ***)"
    
    for c in message:
        print(c, end=' ', flush=True)
        time.sleep(0.2)
    for c in sound_on:
        print(c, end='', flush=True)
        time.sleep(0.2)
    print()

def display(sentence, t):
    for c in sentence:
        print(c, end='', flush=True)
        time.sleep(t)

def Intro():
    t = 0.15
    display ("\nPlease select an activity:\n", t)
    display("\t1 - Game Room\n", t)
    display("\t2 - Learning Zone\n", t)
    display("\t3 - ...\n", t)

    display(f"\n\t'q' - ** QUIT **", t)
    print('\n')
    display("Enter choice -> ", 0.1)
    selection = input()
    return selection 

def SelectLesson():
    t = 0.05
    display("\nNow, choose a lesson:\n", 0.1)
    time.sleep(1)
    novice = f"\t\t---------- " + Fore.RED + "Novice Lessons" + Fore.WHITE + " ----------\n"
    display(novice, t)
    display(f"\t1 - Alphabet\n", t)
    beginner = f"\n\t\t---------- " + Fore.RED + "Beginner Lessons" + Fore.WHITE + " ----------\n"
    display(beginner, t)
    display(f"\t2 - Numbers\n", t)
    display(f"\t3 - Days of the week\n", t)
    display(f"\t4 - Months of the year\n", t)
    display(f"\t5 - Greetings\n", t)
    intermediate = f"\n\t\t---------- " + Fore.RED + "Intermediate Lessons" + Fore.WHITE + " ----------\n"
    display(intermediate, t)
    display(f"\t6 - Verbs\n", t)
    display(f"\t7 - Conjugation\n", t)
    display(f"\t8 - Vocabulary\n", t)
    advanced = f"\n\t\t---------- " + Fore.RED + "Advanced Lessons" + Fore.WHITE + " ----------\n"
    display(advanced, t)
    display(f"\t9 - TODO\n", t)
    expert = f"\n\t\t---------- " + Fore.RED + "Expert Lessons" + Fore.WHITE + " ----------\n"
    display(expert, t)
    display(f"\t10 - TODO\n", t)

    display(f"\n\tPress 'q' to go back to previous menu.\n", t)
    display("Enter choice -> ", 0.1)
    selection = input()
    return selection 

def SelectGame():
    t = 0.05
    display("\nSelect a game according to your preferred difficulty level:\n", t)
    time.sleep(1)
    display(f"\t\t********** " + Fore.RED + "Beginner Level" + Fore.WHITE + " **********\n", t)
    display(f"\t1 - GAME1 -> Save a French Prisoner From Being HANG !!!\n", t)
    display(f"\t2 - GAME2 -> coming soon...\n", t)
    display(f"\n\t\t********** " + Fore.RED + "Intermediate Level" + Fore.WHITE + " **********\n", t)
    display(f"\t3 - GAME3 -> coming soon...\n", t)
    display(f"\t4 - GAME4 -> coming soon...\n", t)
    display(f"\n\t\t********** " + Fore.RED + "God MODE" + Fore.WHITE + " **********\n", t)
    display(f"\t5 - GAME5 -> coming soon...\n", t)

    display(f"\n\tPress 'q' to go back to previous menu.\n", t)
    display("Enter choice -> ", 0.1)
    selection = input()
    return selection 

def Game_1(path):
    #path = "C:\\Users\\kenne\\educ131_sounds\\"
    cwd = os.getcwd()
    path = cwd
    path = path.replace("\\", "\\\\")
    #stromae = path + "\\Stromae_Fils_de_joie.wav"
    stromae_v2 = path + '\\Stromae_Fils_de_joie.wav'
    p4 = multiprocessing.Process(target=playsound, args=(stromae_v2,))
    p4.start()
    t = 0.1
    print()
    print("#"*60)
    print("#"*60)
    print("\t\t---------- GAME 1 ----------")
    print("#"*60)
    print("#"*60)

    display("\nThis event takes place in Paris, France, in 1946...\n", t)
    display("A French prisoner is about to be hanged....\n", t)
    ##########
    print ("  ________")
    print ("  | 	 |")
    print ("  | 	 " + Fore.RED + "O" + Fore.WHITE)
    print ("  | 	" + Fore.RED + "\|/" + Fore.WHITE)
    print ("  | 	 " + Fore.RED + "|" + Fore.WHITE)
    print ("  | 	" + Fore.RED + "/ \ "+ Fore.WHITE)
    print ("__|__")
    ##########
    display("However you have a device that can potentialy save his life...\n", t)
    display("His wife, who is a Secret Spy Agent is helping you remotely...\n", t)
    display("\nAll you have to do, is to listen to his wife and input the secret code that she gives you...\n", t)
    display("Will you be able to save her French husband?...\n\n", t)
    p4.terminate()

    Game1_Engine(path)

    display('\nThank you for playing!', t)

def print_person(guesses, character, path):
    if (guesses == 0):
        print ("_________")
        print ("|	 |")
        print ("|")
        print ("|")
        print ("|")
        print ("|")
        print ("|________")
    elif (guesses == 1):
        #########
        print ("  ________")
        print ("  | 	 |")
        print ("  | 	 " + Fore.RED + "O" + Fore.WHITE)
        print ("  | 	" + Fore.RED + "   " + Fore.WHITE)
        print ("  | 	 " + Fore.RED + " " + Fore.WHITE)
        print ("  | 	" + Fore.RED + "   "+ Fore.WHITE)
        print ("__|__")
        ##########
    elif (guesses == 2):
        #########
        print ("  ________")
        print ("  | 	 |")
        print ("  | 	 " + Fore.RED + "O" + Fore.WHITE)
        print ("  | 	" + Fore.RED + " |" + Fore.WHITE)
        print ("  | 	 " + Fore.RED + "|" + Fore.WHITE)
        print ("  | 	" + Fore.RED + "   "+ Fore.WHITE)
        print ("__|__")
        ##########
    elif (guesses == 3):
        #########
        print ("  ________")
        print ("  | 	 |")
        print ("  | 	 " + Fore.RED + "O" + Fore.WHITE)
        print ("  | 	" + Fore.RED + " |/" + Fore.WHITE)
        print ("  | 	 " + Fore.RED + "|" + Fore.WHITE)
        print ("  | 	" + Fore.RED + "  "+ Fore.WHITE)
        print ("__|__")
        ##########
    elif (guesses == 4):
        #########
        print ("  ________")
        print ("  | 	 |")
        print ("  | 	 " + Fore.RED + "O" + Fore.WHITE)
        print ("  | 	" + Fore.RED + "\|/" + Fore.WHITE)
        print ("  | 	 " + Fore.RED + "|" + Fore.WHITE)
        print ("  | 	" + Fore.RED + "  "+ Fore.WHITE)
        print ("__|__")
        ##########
    elif (guesses == 5):
        #########
        print ("  ________")
        print ("  | 	 |")
        print ("  | 	 " + Fore.RED + "O" + Fore.WHITE)
        print ("  | 	" + Fore.RED + "\|/" + Fore.WHITE)
        print ("  | 	 " + Fore.RED + "|" + Fore.WHITE)
        print ("  | 	" + Fore.RED + "/  "+ Fore.WHITE)
        print ("__|__")
        ##########
    elif (guesses == 6):
        #########
        print ("  ________")
        print ("  | 	 |")
        print ("  | 	 " + Fore.RED + "O" + Fore.WHITE)
        print ("  | 	" + Fore.RED + "\|/" + Fore.WHITE)
        print ("  | 	 " + Fore.RED + "|" + Fore.WHITE)
        print ("  | 	" + Fore.RED + "/ \ "+ Fore.WHITE)
        print ("__|__")
        ##########

        #print (f"The letter was: {character}")
        print ("\n")
        display ("UNFORTUNATELY, you did not save him!!!!!\n", t)
        display ("\nWould you like to try again?", t)
        display ("\nEnter '1' for YES - Lets do it!\nEnter '2' for NO - Not today buddy!!!\n", t)
        replay = input("> ")
        replay = replay.lower()
        if replay == "1":
            Game1_Engine(path)
        return

def selectRandomLetter(path):
    #path = "C:\\Users\\kenne\\educ131_sounds\\"
    character = chr(random.randint(ord('a'), ord('z')))
    #print(f"GENERATED: {character} \n")
    letter_full_path = path + "\\jaimelefrancais-alphabet-francais-" + character + ".mp3"
    return letter_full_path, character

def Game1_Engine(path):

    #path = "C:\\Users\\kenne\\educ131_sounds\\"
    stromae_v3 = path + "\\Stromae_Fils_de_joie.wav"
    #stromae_v3 = path
    p5 = multiprocessing.Process(target=playsound, args=(stromae_v3,))
    p5.start()

    guesses = 0	
    count = 0
    repeated_guesses = 0
    t = 0.05				
    letter_full_path, character = selectRandomLetter(path)				
    word_list = list(character)	
    blanks = " "	
    blanks_list = list(blanks) 
    new_blanks_list = list(blanks)
    guess_list = []
  
    display ("Listen carefully and enter the keys...\n", t)
    print_person(guesses, character, path)
    print (f"" + ' '.join(blanks_list))
  
    time.sleep(3)
    p5.terminate()
    display ("Ready.....................................\nIncoming code..........................:\n", t)
    time.sleep(5)
    playsound(letter_full_path)

    while guesses < 6:
        guess = input("> ")
        guess = guess.lower()
        if len(guess) > 1:
            display ("Enter one cipher at time.\n", t)
            playsound(letter_full_path)
        elif guess == "":
            display ("Please enter the code\n", t)
            playsound(letter_full_path)
        elif guess in guess_list:
            display ("You already tried that code! Here is what you've tried so far:\n", t)
            repeated_guesses += 1
            playsound(letter_full_path)
            print (f' '.join(guess_list))
        else:
            guess_list.append(guess)
            i = 0
            while i < len(character):
                if guess == character:
                    new_blanks_list[i] = word_list[i]
                i = i+1
            if new_blanks_list == blanks_list:
                display("\n\nWRONG cipher:\n", t)
                guesses = guesses + 1
                print_person(guesses, character, path)
                if guesses < 6:
                    correct_cipher = "The cipher was: " + character  + "\n"
                    display(correct_cipher, t)
                    if guesses == 5:
                        display("\n********* BE CAREFUL, 1 incorrect cipher again, and he dies!!! ******\n", t)
                    display("\nTry again> ", t)
                    print (f' '.join(blanks_list))
            elif word_list != blanks_list:
                blanks_list = new_blanks_list[:]
                print (f' '.join(blanks_list))
                if word_list == blanks_list and count == 10:
                    display ("\n\t\t\t************* CONGRATULATIONS!!! ****************\n\t\tYOU SAVED the French Prisoner. Play again to save his prison cell companion\n", t)
                    display ("\n", t)
                    display ("Would you like to play again?\n\n", t)
                    display ("Enter '1' for YES, (Lets save him)\nEnter '2' for NO, (Not today buddy!!!)\n", t)
                    again = input("> ")
                    if again == "1":
                        Game1_Engine(path)
                    #quit()
                    return
                else:
                    display ("Correct! Next cipher: \n", t)
                    count += 1
                    # Player regains 1 body part for a correctly entering a code
                    '''guesses = guesses - 1
                    if guesses < 0:
                        guesses = 0'''
                    #print_person(guesses, character)
            letter_full_path, character = selectRandomLetter(path)
            while character in guess_list:
                letter_full_path, character = selectRandomLetter(path)
            if repeated_guesses == 5:
                guess_list.clear() 
            if guesses < 6:
                playsound(letter_full_path)
            word_list = list(character)	
            blanks = "_"	
            blanks_list = list(blanks) 
            new_blanks_list = list(blanks)                    


def download_file(url, filename=''):
    downloadUrl = url
    try:
        if filename:
            pass            
        else:
            filename = req.url[downloadUrl.rfind('/')+1:]

        with requests.get(url) as req:
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None


#-------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------- Main body ---------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    print('\n\nInitializing. Please wait...\n\n')
    # Get the current temporary directory
    tempdir = tempfile.gettempdir()

    os.chdir(str(tempdir))
    #print(os.getcwd())
    try:
        os.mkdir('educ131_sounds')
    except OSError as error:
        #print(error) 
        print('', end = '')
    os.chdir('educ131_sounds')

    cwd = os.getcwd()
    #print(cwd)

   #-----------------
    downloadLink = 'https://github.com/kennemodeste/L-Elysee/raw/main/educ131_sounds/Stromae_Fils_de_joie.wav'
    filename = 'Stromae_Fils_de_joie.wav'
    download_file(downloadLink, filename)

    downloadLink = 'https://github.com/kennemodeste/L-Elysee/raw/main/educ131_sounds/National-Anthem-Of-France.mp3'
    filename = 'National-Anthem-Of-France.mp3'
    download_file(downloadLink, filename)

    downloadLink = 'https://github.com/kennemodeste/L-Elysee/raw/main/educ131_sounds/loading-effects.wav'
    filename = 'loading-effects.wav'
    download_file(downloadLink, filename)

    #----------------

    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    for index in range(len(alphabet_list)):
        downloadLink = 'https://github.com/kennemodeste/L-Elysee/raw/main/educ131_sounds/jaimelefrancais-alphabet-francais-' + alphabet_list[index] + '.mp3'
        filename = 'jaimelefrancais-alphabet-francais-' + alphabet_list[index] + '.mp3'
        download_file(downloadLink, filename)
   

    downloadLink = 'https://github.com/kennemodeste/L-Elysee/raw/main/educ131_sounds/aurevoir.wav'
    filename = 'aurevoir.wav'
    download_file(downloadLink, filename)

#----------------------------------------------------
    #path = "C:\\Users\\kenne\\educ131_sounds\\"
    # path = 'C:\Users\kenne\AppData\Local\Temp\educ131_sounds'
    #cwd = os.getcwd()
    path = cwd
    path = path.replace("\\", "\\\\")
    #stromae = path + "\\Stromae_Fils_de_joie.wav"
    
    #print(path)
    anthem_sound = path + "\\National-Anthem-Of-France.mp3"
    loading = path + "\\loading-effects.wav"
    stromae = path + "\\Stromae_Fils_de_joie.wav"
    #print("Path is now", path)
    
    wait = 3
    if (not os.path.exists(anthem_sound) or not os.path.exists(loading) or not os.path.exists(stromae)):
        time.sleep(wait)
        wait = 3
    if (not os.path.exists(anthem_sound) or not os.path.exists(loading) or not os.path.exists(stromae)):
        time.sleep(wait)
        wait = 2
    if (not os.path.exists(anthem_sound) or not os.path.exists(loading) or not os.path.exists(stromae)):
        time.sleep(wait)
        wait = 1
    if (not os.path.exists(anthem_sound) or not os.path.exists(loading) or not os.path.exists(stromae)):
        time.sleep(wait)
        display("SOUND NOT FOUND !!! - Please check the path directory of the sound files....", wait)

    p0 = multiprocessing.Process(target=playsound, args=(anthem_sound,))
    p1 = multiprocessing.Process(target=playsound, args=(loading,))
    p2 = multiprocessing.Process(target=playsound, args=(stromae,))

    p0_is_started = False
    p0_is_terminated = False

    p1_is_started = False
    p1_is_terminated = False

    p2_is_started = False
    p2_is_terminated = False

    #print("done!")
    # START anthem p0
    p0.start() 
    p0_is_started = True
   
    Menu()
    display("What is your name -> ", 0.1)
    username = input()
    print()
    display("BONJOUR (Hi) " + username + '!\n' + "With l'Élysée, you are on track to becoming an expert in WRITING and SPEAKING French...", 0.1)
    display("\nReady...?", 0.2)
    time.sleep(5)
    print()
  
    selection = ' '
    flag = False
    # STOP anthem p0
    p0.terminate()             
    
    wait = 10
    if (not os.path.exists(anthem_sound) or not os.path.exists(loading) or not os.path.exists(stromae)):
        time.sleep(wait)

    p0_is_started = False
    p0_is_terminated = True
    while selection != 'q':
        # START Stromae p2
        p2.start() 
        p2_is_started = True
        p2_is_terminated = False
        if selection == 'q':
            # STOP IF Stromae p2
            p2.terminate() 
            p2_is_terminated = True
            p2_is_started = False
            break

        selection = Intro()
        if selection == 'q':
            # STOP IF Stromae p2
            p2.terminate() 
            p2_is_terminated = True
            p2_is_started = False
            break
        
        p2_is_started = False
        p2_is_terminated = True
        # START loading p1
        p1.start()   

        display("Loading", 0.1)
        display(".............................................................................", 0.12)
        time.sleep(2)
        display('\nActivity loaded successfully....\n', 0.1)
        # STOP loading p1
        p1.terminate()              

        if p2_is_started == True:
            # START Stromae p2
            p2.start() 
            p2_is_started = True
            p2_is_terminated = False

        second_selection = ' '
        while second_selection != 'q':
            if p2_is_started == False:
                p2_is_started = True
                p2_is_terminated = False

            if second_selection == 'q':
                # STOP IF Stromae p2
                p2.terminate() 
                p2_is_started = False
                p2_is_terminated = True
                break
            t = 0
            # Swapped selection order for convenience 
            if selection == '2':
                second_selection = SelectLesson()
                if second_selection == '1':
                    display("Implement learning the alphabet here TODO.\n", t)
                elif second_selection == '2':
                    display("Implement learning the numbers here TODO.\n", t)
                else:
                    display("Implementation coming soon...\n", t)
            elif selection == '1':
                second_selection = SelectGame()
                if second_selection == '1':
                    ########## GAME 1 - Start #############
                    if p2_is_terminated == False:
                        p2.terminate()
                        p2_is_terminated = True
                        p2_is_started = False
                    Game_1(stromae)
                    if p2_is_terminated == False:
                        p2.start()
                        p2_is_started = True
                        p2_is_terminated = False
                    ##########   GAME 1 - End   #############
                elif second_selection == '2':
                    display("GAME2:", 0.2)
                elif second_selection != 'q':
                    display("GAME_X coming...", 0.2)
            elif selection != 'q':
                display("Coming soon..", 0.2)
            selection = 'q'
            
            second_selection = 'q'
            if second_selection == 'q':
                # STOP IF Stromae p2
                p2.terminate() 
                p2_is_terminated = True
                p2_is_started = False
                break
            # STOP IF Stromae p2
            p2.terminate() 
            p2_is_terminated = True
            p2_is_started = False
            
        second_selection = 'q'
    display("\n\n\t\t\t\tAu revoir (Goodbye) "+ username + " !!!", 0.1)
    print('\n')

    #playsound("C:\\Users\\kenne\\educ131_sounds\\Numbers\\onetoten.mp3")
    #playsound("C:\\Users\\kenne\\educ131_sounds\\Alphabet\\alphabet_complet.mp3")
   
    aurevoir = path + "\\aurevoir.wav"
    p3 = multiprocessing.Process(target=playsound, args=(aurevoir,))
    p3.start()
    display("\t\t\t\tDeveloped by Modeste Kenne (MK) Studios", 0.3)
    