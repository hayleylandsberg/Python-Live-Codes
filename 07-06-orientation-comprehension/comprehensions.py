flowers = ['Lily', 'Snapdragon', 'Rose', 'Tulip']
bees = ['bumblebee', 'honeybee', 'drillbee', 'angrybee']

large_flowers = [f'the {bee} pollinates the {flower}' for flower in flowers for bee in bees]

# large_flowers = []
# for flower in flowers:
#     for bee in bees:
#     large_flowers.append(f'the {bee} pollinates the {flower}')

print(large_flowers)

family = {'mother': 'Margaret', 'father': 'Jack', 'sister': 'Jenny'}
my_family = {'my ' + k + ' is ' + v for (k,v) in family.items()}

print(my_family)