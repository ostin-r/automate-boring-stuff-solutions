'''
Austin Richards 2/20/21

sandwich-maker.py uses pyinputplus to validate user input for sandwich preferences
'''
import pyinputplus as ip

def get_cost(food_name):
    '''gets the cost of items in sandwich_builder'''
    food_dict = {
        'sourdough':1.75, 
        'rye':2.0, 
        'wheat':1.50, 
        'white':1.25, 
        'chicken':2.0, 
        'turkey':1.50,
        'ham':2.0,
        'tofu':1.25,
        'cheddar':2.0,
        'swiss':2.5,
        'mozzarella':2.5,
        'yes':0.25, # toppings return 'yes' in sandwich_builder(), so I made them all cost 0.25
        'no':0      # saying no to a topping costs nothing
    }

    return food_dict[food_name]

def sandwich_builder():

    print('Enter your sandwich preferences below:\n')

    bread_prompt = 'What bread type would you like? (sourdough, rye, wheat, or white)\n'
    bread_type   = ip.inputChoice(['sourdough', 'rye', 'wheat', 'white'], prompt=bread_prompt)

    protein_prompt = 'What type of protein would you like? (chicken, turkey, ham, or tofu)\n'
    protein_type   = ip.inputChoice(['chicken', 'turkey', 'ham', 'tofu'], prompt=protein_prompt)

    mayo    = ip.inputYesNo(prompt='Would you like mayo?\n')
    mustard = ip.inputYesNo(prompt='Would you like mustard?\n')
    tomato  = ip.inputYesNo(prompt='Would you like tomato?\n')
    lettuce = ip.inputYesNo(prompt='Would you like lettuce?\n')
    
    like_cheese = ip.inputYesNo(prompt='Do you like cheese on your sandwich?\n')

    if like_cheese is 'yes':
        cheese_prompt = 'What kind of cheese would you like? (cheddar, swiss, mozzarella)\n'
        cheese_type   = ip.inputChoice(['cheddar', 'swiss', 'mozzarella'], prompt=cheese_prompt)

        sandwich = []
        cost = 0
        sandwich.extend([bread_type, protein_type, cheese_type, mayo, mustard, tomato, lettuce])
        
        for item in sandwich:
            cost += get_cost(item)

    else:
        sandwich = []
        cost = 0
        sandwich.extend([bread_type, protein_type, mayo, mustard, tomato, lettuce])
        
        for item in sandwich:
            cost += get_cost(item)


    how_many_prompt = 'How many sandwiches would you like?\n'
    how_many = ip.inputInt(min=1, prompt=how_many_prompt)

    print('\nFinal cost: ${}'.format(round(cost * how_many * 1.06, 2)))

sandwich_builder()