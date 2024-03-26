
1. Matplotlib and Seaborn are Python libraries for data visualization. Matplotlib offers more customization options, suitable for complex plots. Seaborn, built on Matplotlib, focuses on statistical plots, often requiring less code. Choose Matplotlib for intricate plots, Seaborn for quick, informative visualizations.

2. To create engaging visuals, prioritize clarity and simplicity. Use appropriate chart types, declutter axes, and employ color mindfully. Incorporate storytelling elements, like titles and annotations, to guide interpretation. Ensure accessibility for diverse audiences.
# %%
3.
import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")
flights = flights.pivot_table(index='month', columns='year', values='passengers')
sns.heatmap(flights, annot=True, fmt="g")
plt.show()

# %%
4.
1.The data-ink ratio, introduced by Edward Tufte, focuses on enhancing the efficiency of visualizations by minimizing non-essential elements, aiming for simplicity and ensuring every mark on a chart communicates useful information
2. Python libraries like matplotlib, seaborn, and plotly support the data-ink ratio principle through customization options. Use functions like plt.axis('off') and sns.despine() to remove clutter in matplotlib and seaborn, and adjust layouts in plotly for cleaner charts. 