# creating string
message = "Hello "
name = 'You'
# printing message
print(f'printing message: {message}')
# finding length of message
msg_len = len(message)
print(f'length of message: {msg_len}')
# slicing message
msg_slicing = message[:4]
print(f'slicing message: {msg_slicing}')
# printing the letter by passing index
chr_of_specific_index = message[1]
print(f'printing letter of a particular index: {chr_of_specific_index}')

# concatinating strings

# 1 formated strings method>1
cnct_string = f'{message} {name.upper()}. Welcome!'
print(cnct_string)

# 2 method>2
frmt_string = '{0} {1}. Welcome!'.format(name, message) #here format takes a Tuple
print(frmt_string)
# STRING METHODS
#1  lower case
lwr_case = message.lower()
print(f'lower case: {lwr_case}')

# 2 Upper case
upr_case = message.upper()
print(f'upper case: {upr_case}')

# 3 count letter
ltr_count = message.count('H')
print(f'counting a particular letter: {ltr_count}')

# 4 finding a letter
fnd_ltr = message.find('l')
print(f'letter is at index: {fnd_ltr}')

# 5 replacing letter
rplc_ltr = message.replace('l','k')   #l >> k
print(rplc_ltr)

# ALL ATTRIBUTES FOR A SPECIFIC STRING
all_attrs = dir(name)
print(all_attrs[:10])

# help about string object
print(help(str))
# help for a SPECIFIC ATTRIBUTE
# I HAVE TAKEN lower
print(help(str.lower))
