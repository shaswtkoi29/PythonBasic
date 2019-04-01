#Shaswat Koirala
#Base_Ball project

import numpy as np
import matplotlib.pyplot as plt
class BattingData:
year = 0
player_id = 1
first_name = 2
last_name =3
team_name =4
games = 5
at_bats = 6
runs = 7
hits = 8
doubles = 9
triples = 10
home_runs = 11
rbi = 12
walks = 13
hbp = 14
stolen_bases = 15
caught_stealing = 16
strike_outs = 17
sac_flies = 18
position = 19
def get_menu_choice() :
print("0: Exit")
print("1: Histogram of runs scored in the lifetimes of all players (no cutoff, no positions)")
print("2: Histogram of runs scored in the lifetimes of all players (no cutoff)")
print("3: Histogram of runs scored in the lifetimes of all players (cutoff = 100)")
print("4: Graph team presence over time")
print("5: Find the batters that had the best and worst seasons stealing bases")
print("6: List the 10 best seasons that batters had by on base percentage")
print("7: Plot on base percentage for the lifetimes of players with best seasons")
print("8: Plot homeruns over time (percentiles)")
print("9: Plot average team RBI over time (1950 - 1959)")
print("10: Extra Credit")
user=input(">")
u=user
# if input is number it goes to if statement
if(u.isdigit()==True):
#if value of u lies between 0 to 6 it return value
if(int(u)>=1 and int(u)int(user)):
l.append(rows)
#appending the value we calculated
s.append(l)
#returning graph,printing the details and labels, titles and legend
#ploting histograms with 100 bins and printing axis names
plt.hist(s, stacked=True, label=positions, bins=100)
plt.ylabel('Number of players')
plt.xlabel('Number of total runs')
plt.title('Total runs vs. number of players having that many runs by position')
plt.legend()

f=("""From the given graph we can be clear that number of player scoring in range of 0 to 500 is more. We cannot get clear vision about the exact runs but from the histogram it can be seen that there is blue color assign to 1B, orange to 2B, green to 3B, red to C ,purple to NULL, brown to OF, pink to P and grey to SS. This colorful distribution have made user easy to see the data in more clear way. But now user can decide the cutoff value.\n""")
return(plt.show(),print(f))
if(num==4):
#empty array
ar=[]
s1=[]
s2=[]
s3=[]
team=np.unique(name[:,BattingData.team_name])
#for loop to find and assign value to id by not changing origianl value
for unq_name in team:
ids=np.copy(name[np.where(name[:,BattingData.team_name]==unq_name)])
yearid=np.unique(ids[:,BattingData.year])
#for data in year we do some calculation to find x axis and y axis for scatter
for unq_year in yearid:

s1.append(unq_name)
s2.append(unq_year)
s3.append(len(unq_name)% 10)

ar=np.array([s1,s2])
plt.subplots(figsize=(10,10))
plt.scatter(ar[1],ar[0],marker='s',c=s3,alpha=0.6)
plt.ylabel('Tean Names')
plt.xlabel('Year')
plt.title('Team presence by Year')
# arranging x axis and y axis label name in readable format
plt.xticks(np.arange(min(ar[1].astype(np.int32)),max(ar[1].astype(np.int32))+1,10),np.arange(min(ar[1].astype(np.int32)),max(ar[1].astype(np.int32))+1,10))
f='This is a scatter plot which shows team presence by year. In the y-axis we can see name of teams where as in x-axis we can find year . It is a colorful graph but I have got totlly different color than desiered still this color help us determin the data more clearly. It is readable but it can be improved by making it bigger and having space between intervals.'
return(plt.show(),print(f))

if(num==5):
AB=np.percentile(name[:,BattingData.at_bats].astype(np.int32),25)
Game=np.percentile(name[:,BattingData.games].astype(np.int32),25)

s1 = name[np.where(np.logical_and(name[:, BattingData.at_bats].astype(np.int32) > AB, name[:, 5].astype(np.int32) > Game ))]

sacs = s1[:,BattingData.sac_flies]
new_sacs = []

for i in range(len(sacs)):
if sacs[i] == '':
new_sacs.append('0')
else:
new_sacs.append(sacs[i])

new_sacs = np.array(new_sacs).astype(np.int32)

obp = (s1[:, BattingData.hits].astype(np.int32) + s1[:,BattingData.walks].astype(np.int32) + s1[:,BattingData.hbp].astype(np.int32)) / (s1[:,BattingData.hits].astype(np.int32) + s1[:,BattingData.home_runs].astype(np.int32) + s1[:,BattingData.hbp].astype(np.int32) + new_sacs)
session=input("session: ")
s=int(session)
part = np.argpartition(obp, -s)[-s:]
for item in part:
print("year:",s1[item,0],"\nplayer:",str(s1[item,2])+str(s1[item,3]),"\nplayer ID:",s1[item,1])
print('\n')
return

# session=input("session: ")
# AB=np.percentile(name[:,6].astype(np.int32),25)
# Game=np.percentile(name[:,5].astype(np.int32),25)
# s1=name[np.where(np.logical_and(name[:,6].astype(np.int32)>AB,name[:,5].astype(np.int32)>Game))]
# print(s1)
# s2=[]
# for i in s1:
#
# h=np.int32(i[8])+np.int32(i[13])+np.int32(i[14])
# p=np.int32(i[8])+np.int32(i[11])+np.int32(i[14])+np.int32((i[18]).isdigit())
# s=h/p
# s2.append(s)
#
# s=int(session)
# player=np.argpartition(s2,-s)[-s:].astype(np.int32)
# print("best "+str(session)+" session: ")
#
# for item in player:
#
# return(print("year:",s1[item,0],"\nplayer:",str(s1[item,2])+str(s1[item,3]),"\nplayer ID:",s1[item,1]))
if(num==7):
AB=np.percentile(name[:,BattingData.at_bats].astype(np.int32),25)
Game=np.percentile(name[:,BattingData.games].astype(np.int32),25)

s1 = name[np.where(np.logical_and(name[:, BattingData.at_bats].astype(np.int32) > AB, name[:, 5].astype(np.int32) > Game ))]

sacs = s1[:,BattingData.sac_flies]
new_sacs = []

for i in range(len(sacs)):
if sacs[i] == '':
new_sacs.append('0')
else:
new_sacs.append(sacs[i])

new_sacs = np.array(new_sacs).astype(np.int32)

obp = (s1[:, BattingData.hits].astype(np.int32) + s1[:,BattingData.walks].astype(np.int32) + s1[:,BattingData.hbp].astype(np.int32)) / (s1[:,BattingData.hits].astype(np.int32) + s1[:,BattingData.home_runs].astype(np.int32) + s1[:,BattingData.hbp].astype(np.int32) + new_sacs)
part = np.argpartition(obp, -20)[-20:]
year=np.unique(name[:,BattingData.year])
start=np.min((year.astype(np.int32)))
end=np.max(year.astype(np.int32))
player=s1[part]

plt.clf()
plt.subplots(figsize=(8,8))
info=[]

for player_i in player:
print(player_i)
info=name[np.where(name[:,BattingData.player_id]==player_i)]
print(info)
active=np.array([])
for un_year in year:
print(un_year)
info2=info[np.where(info[:,BattingData.year]==un_year)]
print(info2)

plt.plot(year,active)
plt.legend(loc=5,bb0x_to_anchor=(1.5,0.5))
plt.xlabel("year")
plt.ylabel("on base percentage")
plt.title("time vs base percentage for players with the best season")
plt.xticks(np.arrange(start,end+1,10),np.arrange(start,end+1,10))
return(plt.show())

if(num==6):
player=np.unique(name[:,BattingData.player_id])
i=[]
ratio=[]
diff=[]
for player_id in player:
info=name[np.where(name[:,BattingData.player_id]==player_id)]
if(info.shape[0]>=10):
i=np.append(i,info[0,BattingData.player_id])
ratio=np.append(ratio,np.sum(info[:,BattingData.stolen_bases].astype(np.int32))/info.shape[0])
diff=np.append(diff,np.sum(info[:,BattingData.caught_stealing].astype(np.int32))-np.sum(info[:,BattingData.stolen_bases].astype(np.int32)))
return( print('Best straler:',i[np.argmax(ratio)],'\nsteal ratio:',round((ratio[np.argmax(ratio)]),2),'\n'),print('\nWorst straler',i[np.argmax(diff)],'\nsteal failed difference:',round((diff[np.argmax(diff)]),2),'\n'))

if(num==8):

s1=[]
s2=[]
s3=[]
s4=[]

year=np.array(range(1950,2011))
for i in range(0,len(year)):
for j in range(0,name.shape[BattingData.year]):
if(year[i]==int(name[j][BattingData.year])):
s1.append(int(name[j][BattingData.home_runs]))
s2.append(np.percentile(s1,50))
s3.append(np.percentile(s1,99))
s4.append(np.amax(s1))
s1=[]

plt.bar(year,s4)
plt.bar(year,s3)
plt.bar(year,s2)
labels=['max','99th percentile','50th percentile']
plt.legend(labels)
plt.ylabel('number of homeruns')
plt.xlabel('years')
plt.title('home runs per year by player')
f=" From the givern graph we can see home runs per year by players. There is different colour for different percentie, which help us diffentiate graph for desier value. Y-axis contains home runs where as X- axis contains year in interval of 10 year. The graph is clear enough to get some idea but by making it more clear, big and small intervals may make it visually more readable. "
return(plt.show(),print(f))
if(num==9):
t=[]
c=0
labels=[]
team=np.unique(name[:,BattingData.team_name])
year=np.array(range(1950,1960))
for i in range(0,len(team)):
for j in range(0,len(year)):
for k in range(0,name.shape[0]):
if(year[j]==int(name[k][BattingData.year])and team[i]==name[k][BattingData.team_name]):
c+=int(name[k][BattingData.rbi])
if(c>0):
t.append(c)
c=0
if (len(t)>0):
plt.plot(t)
labels.append(team[i])
t=[]

plt.xticks(np.arange(10),year+2)
plt.legend(labels,loc='center left',bbox_to_anchor=(1,0.5))
plt.ylabel('total RBI')
plt.xlabel('year')
plt.title(' Year vs total RBI per team')
f=" From the givern graph we can see year vd total RBI per team. There is different colour for different team, which help us diffentiate graph for each team. Y-axis contains total RBI where as X- axis contains year in interval of 1 year. The graph is clear enough to get some idea but by making it more clear, big and small intervals may make it visually more readable."
return(plt.show(),print(f))
def main():

a=hist()
# goes if a is not flase or 0
if(a!=False and a!=0):
a=hist()
# while loop till a is not 0
while(a!=0):
if(a!=0):
a=hist()

if __name__ == "__main__":
main()