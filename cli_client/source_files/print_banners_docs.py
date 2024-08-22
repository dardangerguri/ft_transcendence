import os

def print_banner():
	print("")              
	print(r"***********************************************************************************************************************")
	print(r"*               _______ _______                     _____  _______       _____   _____  __   _  ______                *")
	print(r"*               |       |_____| |      |           |     | |______      |_____] |     | | \  | |  ____                *")
	print(r"*               |_____  |     | |_____ |_____      |_____| |            |       |_____| |  \_| |_____|                *")
	print(r"*                                                                                                                     *")
	print(r"***********************************************************************************************************************")
	print("")																	

def print_available_commands():
	print("-----------------------------------------------------------------------------------------------------------------------")
	print("|                                                   Commands List                                                     |")
	print("-----------------------------------------------------------------------------------------------------------------------")
	print("|   view me  |  view friends  |  chat  |   search user   |   block user   |   start game   |  exit  |  help  |  docs  |")
	print("-----------------------------------------------------------------------------------------------------------------------")
	print("")
	print("")
	print("")

def help():
	os.system('clear')
	print_banner()
	print_available_commands()
	print("-----------------------------------------------------------------------------------------------------------------------")
	print("|                                                        HELP                                                         |")
	print("-----------------------------------------------------------------------------------------------------------------------")
	print("| view me        -  View your user information.                                                                       |")
	print("| view friends   -  View your friends list and their profiles.                                                        |")
	print("| chat           -  Chat with a friend.                                                                               |")
	print("| search user    -  Search for a user. You can add them as a friend here.                                             |")
	print("| block user     -  Block a user.                                                                                     |")
	print("| start game     -  Start a game of pong.                                                                             |")
	print("| exit           -  Exit the program.                                                                                 |")
	print("| help           -  Display this help message.                                                                        |")
	print("| docs           -  Documentation on how to use the CLI.                                                              |")
	print("-----------------------------------------------------------------------------------------------------------------------")
	print("\n")

def print_live_chat_help():
	print("-----------------------------------------------------------------------------------------------------------------------")
	print("|                                                       TIP                                                           |")
	print("-----------------------------------------------------------------------------------------------------------------------")
	print("|           Press (ctrl + z) to open message editor. You can type/send messages and execute commands there!           |")
	print("-----------------------------------------------------------------------------------------------------------------------")
	print("")
	print("")
	print("")

def docs():
	os.system('clear')
	print_banner()
	print_available_commands()
	print("-----------------------------------------------------------------------------------------------------------------------")
	print("|                                                   DOCUMENTATION                                                     |")
	print("-----------------------------------------------------------------------------------------------------------------------")
	print("|                                             Welcome to Call of Pong!                                                |")
	print("|                                                                                                                     |")
	print("| This is the command line version of the game where you can test your pong skills against fellow gamers - web users  |")
	print("| and command line players alike. Whether it is a lighthearted match you are looking for or a quest for pong          |")
	print("| domination you are on, below is how you do it.                                                                      |")
	print("|                                                                                                                     |")
	print("| The \033[1;32;40m'view me'\033[0m command shows your own user information, including your personal details, match history as well as a  |")
	print("| a list of friends you have made and people you have blocked. This is also the place to visit if you want to download|")
	print("| your avatar.                                                                                                        |")
	print("|                                                                                                                     |")
	print("| If you would like to view your friends list and check out their profiles, \033[1;32;40m'view friends'\033[0m is the command you are     |")
	print("| looking for. You will be presented with a list of your favourite pongers along with a prompt asking whether you     |")
	print("| would like to view anyone's details. In case you ever decide to stop playing and need to reach anyone irl, that is  |")
	print("| where you will find your friend's email address.                                                                    |")
	print("|                                                                                                                     |")
	print("| But why would you resort to emails when you can use our chat function? A simple \033[1;32;40m'chat'\033[0m command brings the managing  |")
	print("| of human relations to your fingertips. The chat window displays your message history and the ctrl + Z command opens |")
	print("| the text editor where you can type private messages to your friends. The text editor can be closed by typing 'close'|")
	print("| and leaving the chat can be done with the 'exit' command.                                                           |")
	print("|                                                                                                                     |")
	print("| You can search fellow gamers through the \033[1;32;40m'search user'\033[0m command. The program will inform you whether a user under    |")
	print("| that name exists, and you have the option to add them as a friend. When adding someone as a friend, they will show  |")
	print("| up on your friends list and vice versa.                                                                             |")
	print("|                                                                                                                     |")
	print("| You may be wondering: 'What if I don't want to be friends with them?' Should you find yourself in such a situation, |")
	print("| you have the option to block the person with the \033[1;32;40m'block user'\033[0m command. This will keep those pesky stalkers off your |")
	print("| friends list                                                                                                        |")
	print("|                                                                                                                     |")
	print("| The \033[1;32;40m'start game'\033[0m command is where the real magic happens. After typing this command, you will be prompted to choose |")
	print("| between four different game modes: online 1v1, local 1v1, online tournament and local tournament. Local 1v1 is a    |")
	print("| battle fought on the same keyboard, player 1 on the left using the keys 'w' and 's' for moving the paddle up and    |")
	print("| down, and player 2 using the arrow keys for up and down movement. Online 1v1 mode will pair you up with a remote    |")
	print("| user. Regardless of which game mode you choose, next you will be directed to a game lobby. If there are lobbies     |")
	print("| available, you will be directed to one where an eager opponent already awaits you. If there is no room in the       |")
	print("| existing lobbies, a new lobby will be created, you will become player 1 (the host of the lobby) and wait until an   |")
	print("| opponent arrives. If you want to play against a friend, you can type 'invite' in the message editor and choose a    |")
	print("| friend on your friends list. This will send a game invite link to the friend via your private chat, where they can  |")
	print("| accept it. The tournament game modes follow the same logic, except there will be four players participating in each |")
	print("| tournament.                                                                                                         |")
	print("|                                                                                                                     |")                                                                        
	print("| Once a lobby is full, the host can initiate the game or the tournament depending on your game mode. If you are      |")
	print("| playing an online game mode, there is a live chat in the game lobby, where you can hang out and chat before heading |")
	print("| into the ring. The chat doubles as a notification board where the players for the upcoming match will be notified   |")
	print("| of the impending battle, and the winners announced after the games. The chat mechanics are the same as in the       |")
	print("| private chat, namely ctrl + Z brings up the text editor where you can type your messages. In the local game modes,  |")
	print("| there is no live chat and the lobby serves only as a notification board. Once you are ready to pong, the host can   |")
	print("| type 'start' in the editor. After this, you can choose to set custom specs (speed of the paddle/ball) or let us     |")
	print("| decide for you by continuing with default settings. The game will end once a player has scored five goals. In the   |")
	print("| tournament, you will be paired randomly with another player and hopefully beat them to advance to the final round.  |")
	print("| The winner of the final match will be crowned the winner of the whole tournament.                                   |")
	print("|                                                                                                                     |")
	print("| Should you ever need assistance, \033[1;32;40m'help'\033[0m will show you a brief description for each of the commands. Closing the     |")
	print("| program happens by simply typing \033[1;32;40m'exit'\033[0m. This documentation is available through the \033[1;32;40m'docs'\033[0m command.                |")
	print("|                                                                                                                     |")
	print("|                                                                                                                     |")
	print("| May your paddle strike true.                                                                                        |")
	print("|                                                                                                                     |")
	print("|                                                                                                                     |")
	print("-----------------------------------------------------------------------------------------------------------------------")
	print("\n")
