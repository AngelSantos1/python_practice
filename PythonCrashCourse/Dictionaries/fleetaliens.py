aliens = []

#Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    new_alien1 = {'color':'yellow','points':10,'speed':'slow'}
    aliens.append(new_alien)
    aliens.append(new_alien1)
    """for alien_number in range(5):
        new_alien1 = {'color':}"""
    
#Make first 3 aliens yellow, medium speed aliens worth 10 points
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
    
#Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

#Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")