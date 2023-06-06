# from tiktaktoe.assign_player import pick_player
# from tiktaktoe.winner import who_is_winner
# from tiktaktoe.game_play import play_game

from tiktaktoe import pick_player, play_game, who_is_winner
# from first_program import call_me
# call_me()
import first_program
first_program.call_me()


player = pick_player()
board = play_game(player=player)
winner = who_is_winner(board)
print(f"player {winner} is Winner with Board: {board}")


# root_folder -> game_1 football
#                     src
#                         team.py  which team are you?
#                         game.py play the game!!!!!!!!
#                         random.choice([0,1])
#                         win.py you won or not?
#                     main.py
