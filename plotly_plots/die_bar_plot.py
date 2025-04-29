import plotly.express as px

# import die model class
from die import Die

# create instance
die = Die()
results = []
for roll in range(1,50001):
    roll = die.roll_die()
    results.append(roll)

# list to store the frquecy data for each number
frequencies = []
# set var for values that are possible in the roll_data
poss_results = range(1, die.num_sides+1)
# loop through the possibilities
for value in poss_results:
    # tallies the data of the specific value were on.
    # starts with 1 then 2 then 3 then 4 then 5 then 6
    frequency = results.count(value)
    # add said valuechronoligcally to frequesncies list
    frequencies.append(frequency)

# set up a fig obj = to the px .bar() method of plotly express and pass it the 
# x values which are the possibilites of 1-6 with their own colum,
# and then the frequency of occurence.
fig = px.bar(x=poss_results, y=frequencies)

# opens html view in browser
fig.show()

# prove
# print(frequencies)

# empty list to obtain formatted str nums
formatt_term_num = []
for item in frequencies:
    # format spoecifier to add commas ?idk how it adds correctly here
    formatted_number = f"{item:,}"
    formatt_term_num.append(formatted_number)
    
# prove
print(formatt_term_num)