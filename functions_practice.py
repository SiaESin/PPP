def hello():
    print('Hello from the other side')

hello()

def pack(cards, gum, wolves):
    return[cards, gum, wolves]

print(pack('cards', 'gum', 'wolves'))

lunch = ['a burger', 'fries', 'an apple']
def eat_lunch(lunch):
    print('First I eat ' + lunch[0])
    print('Next I eat ' + lunch[1])
    print('Next I eat ' + lunch[2])

eat_lunch(lunch)