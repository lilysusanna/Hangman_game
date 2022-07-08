import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
random_word= ('rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks')
choose_random= random.choice(random_word)
print(choose_random)

blank=len(choose_random)
list=[]
for i in range(blank):
    list.append('_')
end_game=False
life=6
while not end_game:
    guess=input("guess a letter").lower()
    if guess in list:
        print("already chosen letter")
    for x in range(blank):
        if guess == choose_random[x]:
            list[x]=guess
            life=life

    if guess not in choose_random:
        life=life-1
        if life==0:
            end_game=True
    print(list)
    print(life)
    print(stages[life])
    if '_' not in list:
        end_game=True
