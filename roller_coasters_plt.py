import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
pd.set_option('display.expand_frame_repr', False)
df_wood = pd.read_csv(r'C:\Coding\Codecademy_Projects\roller_coaster_starting\Golden_Ticket_Award_Winners_Wood.csv')
#print(df_wood.head())

#roller_coaster_parks = rankings_wood.groupby('Park').Name.count().reset_index()
#roller_coaster_parks.rename(columns={'Name':'Count'}, inplace=True)
#print(roller_coaster_parks)

df_steel = pd.read_csv(r'C:\Coding\Codecademy_Projects\roller_coaster_starting\Golden_Ticket_Award_Winners_Steel.csv')
#print(df_steel.head())



# write function to plot rankings over time for 1 roller coaster here:

el_toro_ranking = df_wood[(df_wood['Name']== 'El Toro') & (df_wood['Park']=='Six Flags Great Adventure')]
#print(el_toro_ranking)

plt.plot(el_toro_ranking['Year of Rank'], el_toro_ranking['Rank'], linewidth=4, color='purple')

ax = plt.subplot(1,1,1)
ax.set_yticks(range(1,4))
ax.set_xticks(el_toro_ranking['Year of Rank'])
ax.set_facecolor(color='#ffdad4')
ax.invert_yaxis()

plt.xlabel('Year')
plt.ylabel('Rank')
plt.title('Ranking of El Toro at Six Flags Great Adventure 2013-2018')
plt.legend(['El Toro'])
#.show()

plt.clf()

# write function to plot rankings over time for 2 roller coasters here:

el_toro_ranking = df_wood[(df_wood['Name'] == 'El Toro') & (df_wood['Park'] == 'Six Flags Great Adventure')]
print(el_toro_ranking)
boulder_dash_ranking = df_wood[(df_wood['Name'] == 'Boulder Dash') & (df_wood['Park'] == 'Lake Compounce')]
print(boulder_dash_ranking)


plt.plot(el_toro_ranking['Year of Rank'], el_toro_ranking['Rank'], linewidth=4, color='purple')
plt.plot(boulder_dash_ranking['Year of Rank'], boulder_dash_ranking['Rank'], linewidth=4, color='red')
ax = plt.subplot(1,1,1)
ax.set_yticks(range(1,5))
ax.set_xticks(el_toro_ranking['Year of Rank'])
ax.set_facecolor(color='#ffdad4')
ax.invert_yaxis()

plt.xlabel('Year')
plt.ylabel('Rank')
plt.title('Ranking of El Toro vs Boulder Dash 2013-2018')
plt.legend(['El Toro', 'Boulder Dash'])
#plt.show()



plt.clf()

# write function to plot top n rankings over time here:


def roller_coaster_plotter(ranking_df,n):
    top_n_rankings = ranking_df[(ranking_df.Rank <= n)]
    for coaster in set(top_n_rankings['Name']):
        coaster_rankings = top_n_rankings[top_n_rankings['Name']==coaster]
        plt.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'], label=coaster, linewidth=4)
    plt.legend()
    
roller_coaster_plotter(df_wood, 5)
plt.title('Roller Coasters with Top 5 Rankings 2013-18')
#plt.show()




plt.clf()




# load roller coaster data here:
coasters = pd.read_csv(r'C:\Coding\Codecademy_Projects\roller_coaster_starting\roller_coasters.csv')
print(coasters.head())




# write function to plot histogram of column values here:

def hist_maker(df, col):
    print(df[col])
    plt.hist(df[col])
    plt.title('Histogram of Roller Coasters {}'.format(col))
    

hist_maker(coasters,'speed')
#plt.show()






plt.clf()

# write function to plot inversions by coaster at a park here:
def inversions_plotter(df, park_name):
    park_df = df[df['park']== park_name]
    coaster_names = park_df['name']
    plt.figure(figsize=(12, 7))
    plt.bar(coaster_names, park_df.num_inversions)
    ax = plt.subplot()
    ax.set_xticks(range(len(coaster_names)))
    ax.set_xticklabels(coaster_names, rotation=30)
    plt.title('Num of Inversions at {} Roller Coasters'.format(park_name))

#inversions_plotter(coasters, 'Parc Asterix')
#plt.show()



plt.clf()

# write function to plot pie chart of operating status here:

def pie_plotter(df):
    status_df = df.groupby('status').name.count().reset_index()
    status_df = status_df[(status_df['status']== 'status.operating') |
                          (status_df['status'] == 'status.closed.definitely')]
    status_df['status'] = status_df.status.str[7:]

    plt.pie(status_df.name, autopct='%0.1f%%')
    plt.axis('equal')
    plt.legend(status_df.status.values)
    plt.title('Status of Roller Coasters')

#pie_plotter(coasters)
#plt.show()





plt.clf()

# write function to create scatter plot of any two numeric columns here:

def scatter_plotter(df, col1, col2):
    if col2 == 'height' or col1 == 'height':
        df = df[df['height'] < 400]
    plt.scatter(df[col1], df[col2])
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.title('Scatter Plot of {0} vs {1}'.format(col1.title(), col2.title()))

#scatter_plotter(coasters, 'height', 'length')
#plt.show()
#plt.clf()

#scatter_plotter(coasters, 'speed', 'length')
#plt.show()


plt.clf()

#seating types

coasters_seating = coasters.groupby('seating_type').name.count().reset_index()
plt.pie(coasters_seating['name'])
plt.legend(coasters_seating['seating_type'].values, loc='upper left')
plt.title('Pie Chart of Roller Coaster Seating Types')
#plt.show()

plt.clf()
