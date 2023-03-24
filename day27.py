q = [
  ['my name is ', 'rew', 'eraw', 'bruce',3],
  ['my name is ', 'rew', 'eraw', 'bruce',3],
  ['my name is ', 'rew', 'eraw', 'bruce',3],
  ['my name is ', 'rew', 'eraw', 'bruce',3],
]

levels = [1000,2000,30000,50000]

for i in range(0,len(q)):
  ques = q[i]
  print(f'question for rupees {levels[i]}')
  print(f'{ques[0]}')
  print(f'a. {ques[2]}' ' '   f'b.{ques[3]}' ' '  f'c.{ques[4]}')
  ans = int(input('enter option '))
  if(ans==ques[4]):
    print(f'won {levels[i]}')
  else: 
    print('you lost')
    break