# Sternberg Plot Gallery

Here are some plot ideas you can use for inspiration, whether for plotting data from the Sternberg task or something else. Click the "Click to show" button to reveal the code for each plot.

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

sns.set_context("notebook", font_scale=1.5)

file = 'https://raw.githubusercontent.com/ethanweed/ExPsyLing/master/datasets/Sternberg/2021/Sternberg_cleaned.csv'

data = pd.read_csv(file)

data.head()

ax = sns.regplot(x = 'setSize', y = 'rt', data = data)
sns.despine(top = True, right = True)

ax.set_title("Look at me, I'm a regression plot!", y = 1.1)

ax = sns.lmplot(
    data = data,
    x = "setSize", y = "rt",
    hue = "present"
)

ax.fig.suptitle("I'm a 'facet-grid', so you need to give me a title in a different way!",
               y=1.1)


ax = sns.pointplot(x="setSize", 
                   y="rt", 
                   hue="present", 
                   data=data, 
                   markers=["o","x"], 
                   linestyles=["-","--"])

# open the box
sns.despine(top = True, right = True)

# Put the legend out of the figure
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

ax.set_title("Look at me, I'm a point plot with error bars!", y=1.1)

ax = sns.pointplot(x="setSize", 
                   y="rt", 
                   hue="present", 
                   data=data, 
                   markers=["o","x"], 
                   linestyles=["-","--"],
                   errwidth=0)

# open the box
sns.despine(top = True, right = True)

# Put the legend out of the figure
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

ax.set_title("Look at me, I'm a point plot without error bars!", y=1.1)

ax = sns.boxplot(x = 'setSize', 
                 y = 'rt', 
                 hue = "present", 
                 data = data)

sns.despine(top = True, right = True)

# open the box
sns.despine(top = True, right = True)

# Put the legend out of the figure
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

ax.set_title("Look at me, I'm a multiple box plot!", y=1.1)

ax = sns.violinplot(x = 'setSize', 
                 y = 'rt', 
                 hue = "present", 
                 data = data)

sns.despine(top = True, right = True)

# open the box
sns.despine(top = True, right = True)

# Put the legend out of the figure
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

ax.set_title("Look at me, I'm a multiple violin plot!", y=1.1)

ax = sns.pointplot(x="setSize", y="rt", hue="id", errwidth=0, data=data)

# check out what happens if we don't run this next line
ax.get_legend().remove()

ax.set_title("Look at me, I'm showing different lines for every participant!", y=1.1)

ax = sns.lineplot(x="setSize", y="rt", hue="id", data=data)

ax.get_legend().remove()

ax.set_title("I'm pretty, but what do I mean?", y=1.1)

ax = sns.catplot(x="present", y = 'rt', kind="bar", data = data)

ax.fig.suptitle("Hey, I'm a bar plot. How's my ink to data ratio looking?", y=1.1)

ax = sns.catplot(x="present", y = 'rt', kind="bar", hue = "setSize", data = data)

ax.fig.suptitle("Bars? Oh yeah, I'm spittin' bars.", y=1.1)

ax = sns.swarmplot(x = 'rt', data = data)

ax.set_title("Oh, who...me? I'm a swarm plot", y = 1.1)

ax = sns.histplot(x = "rt", data = data)

ax.set_title("Just your friendly neighborhood histogram!", y = 1.1)

ax = sns.histplot(x = "rt", hue = "present", data = data)

ax.set_title("Overlapping histrorams!", y = 1.1)