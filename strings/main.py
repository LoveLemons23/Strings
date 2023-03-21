# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#part 1
# Players that scored
player1 = 'Ruud Gullit'
player2 = 'Marco van Basten'

#Goals
goal_0 = 32
goal_1 = 54

scorers = f'{player1} {goal_0}, {player2} {goal_1}'

report =  f'{player1} scored in the {goal_0}nd minute\n{player2} scored in the {goal_1}th minute' 
print (report)

#part 2

player = 'Erwin Koeman'
first_name = (player[0:player.find (" ")] [:5])
last_name_len = len(player[player.find (" "):][:-1])
name_short = player[:1] + '.' + player[player.find (" "):]
chant = (f'{first_name[:5]}! '* 4) + (f'{first_name[:5]}!')
chant2= chant + (" ")
good_chant = chant2.endswith (" ")
print (good_chant)
