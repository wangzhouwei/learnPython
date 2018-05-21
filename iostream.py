# todos = open('todos.txt','w')
# print('Put out the search.',file = todos)
# print('Feed the cat.',file = todos)
# print('Prepare tax return.',file = todos)
# todos.close()
# tasks = open('todos.txt')
# for chore in tasks:
#     print(chore,end = 'A')
# tasks.close()
with open('todos.txt','a') as tasks:
    print('res','req',file = tasks)
