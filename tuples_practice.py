# Phyllis Torres
# tuples practice

print('\nTuple Practice\n\n')
print('Phyllis Torres\n\n')

#   12.1
#   Create a tuple filled with 5 numbers assign it to the variable n
print('Section 12.1\n')
print('Create a tuple named n with 5 numbers in it.\n')
n = (2, 4, 6, 8, 10)

print('tuple n = ' + str(n))

#   Create a tuple named tup using the tuple function
print('\nCreate a tuple named tup using the tuple function. This tuple will be created empty.\n')
tup = tuple()

print('tup = ' + str(tup))

#    Create a tuple named first and pass it your first name
print('\nCreate a tuple named first and pass it your first name.\n')
first = tuple('Phyllis')

print('first = ' + str(first))

#    print the first letter of the first tuple by using an index
print('\nPrint the first letter of tuple named first using an index.\n')
print first[0]

#    print the last two letters of the first tuple by using the slice operator (remember last letters means use
#    a negative number)
print('\nPrint last 2 letters of tuple named first using slice operator.\n')
print first[-2:]

#   12.2
#   Given the following code, swap the variables then print the variables
print('\n\nSection 12.2\n')
print('Swap the variables.\n')

var1 = tuple("hey")
var2 = tuple("you")

print('Before the swap, var1 = ' + str(var1) + ' var2 = ' + str(var2))

var1, var2 = var2, var1

print('\nAfter the swap, var1 = ' + str(var1) + ' var2 = ' + str(var2))

#   Split the following into month, day, year, then print the month, day and year

print('\nSplit the following date into month, day, year.\n')

date = 'Jan 15 2016'
print date

month, day, year = date.split(' ')
print('\nThe new variable, date, has been split into month, day, and year.\n')

print('month = ' + str(month))
print('day = ' + str(day))
print('year = ' + str(year))

#   12.3
#   pass the function divmod two values and store the result in the var answer, print answer
print('\n\nSection 12.3\n')
print('Pass two values, 7 and 4 to the function divmod and store the result in the variable answer.\n')
answer = divmod(7, 4)

print('The variable answer = ' + str(answer))

#   12.4
#   create a tuple t4 that has the values 7 and 5 in it, then use the scatter parameter to pass
#   t4 into divmod and print the results
print('\n\nSection 12.4\n')
print('Create a tuple, t4, that has the values 7 and 5 in it. Use scatter parameter to pass'
      ' t4 into divmod and print the results.')
t4 = (7, 5)
results = divmod(*t4)

print('\nThe variable, results, returned from divmod = ' + str(results))

#   12.5
#    zip together your first and last names and store in the variable zipped
#    print the result
print('\n\nSection 12.5\n')
print('Zip together first and last names and store in a variable named zipped.')
print('The first name used is Phyllis and the last name used is Torres.')
zipped = zip('Phyllis', 'Torres')

print('\nAfter the zip method is used, the variable zipped = ' + str(zipped))

#   12.6
#   Store a list of tuples in pairs for six months and their order (name the var months): [('Jan', 1), ('Feb', 2), etc
print('\n\nSection 12.6\n')
print('Store a list of tuples in pairs for six months and their order and name the variabl months.')
print('For example, (Jan, 1), (Feb, 2), etc.\n')
months = [('Jan', 1), ('Feb', 2), ('Mar', 3), ('Apr', 4), ('May', 5), ('Jun', 6)]

print('The list months = ' + str(months))

# create a dictionary from months, name the dictionary month_dict then print it
print('\nCreate a dictionary from the list months and name it month_dict.\n')
month_dict = dict(months)
print('The dictionary month_dict = ' + str(month_dict))

#   12.7
#   From your book:
print('\n\nSection 12.7\n')

my_words = ('We', 'are', 'the', 'knights', 'of', 'the', 'round', 'table')
print('The tuple, my_words, passed to the function sort_by_length is: ' + str(my_words))
def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))

    t.sort(reverse=True)
    res = []
    for length, word in t:
        res.append(word)
    return res

results = sort_by_length(my_words)
print('\nAfter calling sort_by_length, the results returned are: ')
print results
print('\nThe function sort_by_length() returns a list of the input words showing the words with'
      'greatest length first to the words with the smallest length.')
# Create a list of words named my_words that includes at least 5 words  and test the code above
# Print your result
