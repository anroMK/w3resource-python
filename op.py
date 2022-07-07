'''
class Montster:

    def __init__(self, health, energy, **kwargs):
        print(kwargs)
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)


    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')


class Fish:
    def __init__(self, speed, has_scales, **kwargs):
        print(kwargs)
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)
        

    def swim(self):
        print(f'The fish is swimming at a speed of {self.speed}')


class Shark(Montster, Fish):
    def __init__(self, bite_strength, health, energy, speed, has_scales):
        self.bite_strength = bite_strength
        super().__init__(health = health, energy = energy, speed = speed, has_scales = has_scales)
    



shark = Shark(bite_strength= 50, 
    health= 200, 
    energy= 55, 
    speed = 120, 
    has_scales = False)

print(shark.speed)


'''

'''
class Monster:
    'A monser that has some attributes'
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        self._id = 5
        


    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')



monster = Monster(20,10)

print(monster._id)

if hasattr(monster, 'health'):
    print(f'Monster has {monster.health} health')

setattr(monster, 'weapon', 'Sword')


new_attributes = (['weapon','Axe'], ['armor','Shield'], ['potion','mana'])

for attr, value in new_attributes:
    setattr(monster, attr, value)
print(vars(monster))

print(monster.__doc__)

print(help(str))


'''

"""
class Shark(Montster):
    def __init__(self, speed, health, energy):
        super().__init__(health, energy)
        self.speed = speed

    
    def bite(self):
        print('The shark has bitten')

    def move(self):
        print('The shark has moved')
        print(f'The speed of the shark is {self.speed}')

class Scorpion(Montster):
    def __init__(self, poison_damage, scorpion_health, scorpion_energy):
        super().__init__(health = scorpion_health, energy= scorpion_energy)
        self.poison_damage = poison_damage

    def attack(self):
        print('The scorpion has attacked')
        print(f'The scorpion dealt {self.poison_damage}')




'''
shark = Shark(speed= 120, health= 100, energy= 80)

print(shark.energy)
shark.attack(20)
shark.move()

'''


"""

#print({chr(let):let-ord('A')+1 for let in range(ord('A'), ord('Z')+1)})



#list1 = [4,2,3,1,5]
#print(sorted(list1, reverse=True))

'''
list2 = [('a', 3), ('b', 10), ('c', 6), ('d', 5)]


def sort_function(item):
    return item[1]


print(sorted(list2, key = sort_function))

print(sorted(list2, key = lambda item: item[1]))

'''
'''
inventory_names = ['Screws', 'Wheels', 'Metal parts', 'Rubber bits', 'Screwdrivers', 'Wood']
inventory_numbers = [43, 12, 95, 421, 23, 43]

combined_list = list(zip(inventory_names, inventory_numbers))


print(sorted(combined_list, key= lambda x: x[1], reverse= True))
print(sorted(combined_list, key= lambda x: len(x[0])))
'''



'''
def power_function(num):
    return num * num

my_list = [1,2,3,4,5]

print(list(map(power_function, my_list)))
print(list(map(lambda x: x * x, my_list)))
print([num * num for num in my_list])

def get_below_4(num):
    if num < 4:
        return True
    return False

print(list(filter(get_below_4, my_list)))

print(list(filter(lambda x: x<4, my_list)))

print([num for num in my_list if num < 4])
'''

'''
x = 10
a = lambda x : x + 1

a(x)

print(x)

'''

'''
file1 = open('test.txt')

print(list(file1))

file1.close()
'''

''''''
# with open('test.txt', 'r') as file:
#     for line in list(file):
#         print(line)


# with open('test.txt', 'a') as file:
#     file.write('\nWrite some xxxxxxxxxxxxxx')


with open('tree.txt', 'w') as tree_file:
    tree_string = '''
        x
       xxx
      xxxxx
        x
        x
        x  
    '''
    tree_file.write(tree_string)
    