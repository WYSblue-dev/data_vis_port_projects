import plotly.express as px

from rw import RandomWalk as RW

# get random walk data
rw = RW()
rw.run_walk()

# to store a b points
a_b = []

# create a list of 'A', 'B' values to color data accordingly
# this can be a list comprehension and be more effiecnent using the % arithmatic operater.
# alting by odd and eve n for ab and add a if conditonal for the 0,0
for num in range(1, len(rw.x_points)+1):
    if len(a_b) < len(rw.x_points):
        a_b.append('A')
        a_b.append('B')

# this creates temp sets with the dat we have and loops over it via indexing.
# we then chekc if there is a point equivilent to 0,0 if so we change the first
# a_b to start bc this is where we assume the point will be.
for i, (x,y) in enumerate(zip(rw.x_points,rw.y_points)):
    if x==0 and y==0:
        # passing i as the indexing of the list int will change the specific 
        # opint not just the starting point.
        a_b[i] = 'start'
        break

# proving length
print(len(a_b))
print(len(rw.x_points))
print(len(rw.y_points))

# worth us noting that the code here is still not utilizing a dataframe. But
# it's teaching us how we can think aobut data frames even without them present
# we could make a class to help perform the sixing or color operations we'd like
# to take. Our szing it based off of color. So cataegorical right?
# If we flipped so that the sizing or index determined the color that would be 
# like agradient colo map right?

# this is very iteresting. Makes the sizing bigger as the random walk progresses
# we can adjust this to our liking maybe something like a for loop in conjuction
# with the colors maybe to make specific colors bigger this is very cool (:{.
sizing = [i+1 for i in range(len(rw.x_points))]
sizing_2_0 = []
for let in a_b:
    if let == 'A':
        sizing_2_0.append(2)
    elif let == "start":
        sizing_2_0.append(20)
    else:
        sizing_2_0.append(5)

# cool list comprehension learning to use them by trail and error here.
sizing_2_0 = [2 if let=="A" else 20 if let=='start' else 10 for let in a_b]

# settings up dict simlar df
data = {'x':rw.x_points, 'y':rw.y_points, 'cata':a_b, 'size':sizing_2_0}
# setting up title for the plot to pass to the scatter func.
title = "Scatter of Random Walk"
# settting up labels for the corresponding colums. tbc in the scatter func.
labels = {'x':'Hor dir', 'y':'Virt dir'}

# calling scatter to create the plot. modifying labels and title as well as
# added a color convention. color='cata' expects a colum of information
# pertaining to the points created from the x and y colums. using 
# color_dicrete_map={'A':'red', 'B':'orange'} changes color of the point
# based on its value and how the 'cata' row is formatted
fig = px.scatter(data, x='x', y='y', labels=labels, title=title, color="cata", size='size',
                 color_discrete_map={
                     'start':'green', 'A':'red', 'B':'orange'
                     })

fig.show()