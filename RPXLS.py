
game_img = [rock,paper,scissors,lizard,spock] #assign images to the respectives
user_in =int(input('Choose your Hand  1=> Rock , 2 => Paper , 3 => scissors , 4 => Lizard , 5 => Spock '))

cpu_in = random.randint(1,5)

if user_in == 1 and  (cpu_in == 3 or cpu_in == 4):
  print(f'You Choose {game_img[user_in-1]}')
  print(f'Computer Choose {game_img[cpu_in-1]}')
  print('You Won , Yay !')
elif user_in == 2 and (cpu_in == 1 or cpu_in == 5 ):
  print(f'You Choose {game_img[user_in-1]}')
  print(f'Computer Choose {game_img[cpu_in-1]}')
  print('You Won , Yay !')
elif user_in == 3 and (cpu_in == 2 or cpu_in == 4):
  print(f'You Choose {game_img[user_in-1]}')
  print(f'Computer Choose {game_img[cpu_in-1]}')
elif user_in == 4 and (cpu_in == 5 or cpu_in == 2):
  print(f'You Choose {game_img[user_in-1]}')
  print(f'Computer Choose {game_img[cpu_in-1]}')
elif user_in ==5 and (cpu_in == 1 or cpu_in == 3):
  print(f'You Choose {game_img[user_in-1]}')
  print(f'Computer Choose {game_img[cpu_in-1]}')
  print('You Won , Yay !')
elif user_in == cpu_in:
  print(f'You Choose {game_img[user_in-1]}')
  print(f'Computer Choose {game_img[cpu_in-1]}')
  print("its a Draw")
elif user_in >5 or user_in < 1:
  print("You Typed a invalid Hand , You Lose ") 
else:
  print(f'You Choose {game_img[user_in-1]}')
  print(f'Computer Choose {game_img[cpu_in-1]}')
  print('You Lose ')
