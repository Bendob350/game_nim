from matplotlib import pyplot as plt

years = [2023, 2024, 2025]

scores = [9 , 11 , 14]

avg = [11, 10 , 13]

name = 'test'

mark = [7,17,10,6]

# deux courbes dans le meme graphique
""" plt.plot(years, scores,'^-r')
plt.bar(years, avg)
plt.title('Scores of '+name)
plt.xlabel('Years')
plt.ylabel('Scores')
plt.xticks(years, rotation=45)
plt.legend(labels=['scores', 'avg'])
plt.show() """

#deux courbes meme graphique
plt.subplot(221)
plt.plot(years, scores,'^-r')
plt.title('Scores of '+name)
plt.xlabel('Years')
plt.ylabel('Scores')
plt.xticks(years, rotation=45)
plt.legend(labels=['scores'])
plt.tight_layout()
plt.subplot(222)
plt.bar(years, avg,width=0.1)
plt.legend(labels=['avg'])
plt.xlabel('Years')
plt.ylabel('avg')
plt.subplot(223)
plt.pie(mark,explode=[0.2,0,0,0],labels=['faible','passable','AB','B'],autopct='%1.2f%%')
plt.show()
print('fdfdf'.split(','))