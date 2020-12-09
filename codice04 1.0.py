import matplotlib.pyplot as plt

data = {'libri di matematica': 2, 'libri di italiano': 4, 'libri di scienze': 2, 'libri di storia': 1}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Categorical Plotting')

plt.show()