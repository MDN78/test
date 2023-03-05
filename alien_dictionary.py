alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# alien turned right

if alien_0['speed'] == 'slow':
    x_incriment = 1
elif alien_0['speed'] == 'medium':
    x_incriment = 2
else:
    # alien moved fast
    x_incriment = 3
alien_0['position'] = alien_0['x_position'] + x_incriment
print(f"New position: {alien_0['x_position']}")
# change speed parameter
alien_0['speed'] = 'fast'
print(alien_0)

# if you want to delete pair key/meaning - use command DEL
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# add to dictionaries several parameters: use separate lines:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',  # add comma for future - when you add new parameter
    }
