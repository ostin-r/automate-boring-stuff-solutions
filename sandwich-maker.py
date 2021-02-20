'''
Austin Richards 2/20/21

sandwich-maker.py uses pyinputplus to validate user input for sandwich preferences
'''
import pyinputplus as ip

def sandwich_builder():

    print('Enter your sandwich preferences below:\n')

    bread_prompt = 'What bread type would you like? (sourdough, rye, wheat, or white)\n'
    bread_type = ip.inputChoice(['sourdough', 'rye', 'wheat', 'white'], prompt=bread_prompt)

    protein_prompt = 'What type of protein would you like? (chicken, turkey, ham, or tofu)\n'
    protein_type = ip.inputChoice(['chicken', 'turkey', 'ham', 'tofu'], prompt=protein_prompt)

    like_cheese = ip.inputYesNo(prompt='Do you like cheese on your sandwich?\n')

    if like_cheese is 'yes':
        cheese_prompt = 'What kind of cheese would you like? (cheddar, swiss, mozzarella)\n'
        cheese_type   = ip.inputChoice(['cheddar', 'swiss', 'mozzarella'], prompt=cheese_prompt)

    mayo    = ip.inputYesNo(prompt='Would you like mayo?\n')
    mustard = ip.inputYesNo(prompt='Would you like mustard?\n')
    tomato  = ip.inputYesNo(prompt='Would you like tomato?\n')
    lettuce = ip.inputYesNo(prompt='Would you like lettuce?\n')

    how_many_prompt = 'How many sandwiches would you like?\n'
    how_many = ip.inputInt(min=1, prompt=how_many_prompt)

sandwich_builder()