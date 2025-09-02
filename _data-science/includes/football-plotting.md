\ifndef{footballPlotting}
\define{footballPlotting}

\editme


\subsection{Plotting `plt`}

\setupcode{import matplotlib.pyplot as plt}

\notes{Matplotlib is a plotting library, used by nearly everyone. Inspired by matlab.

Support for many types of plots, lot of flexibility in options, but also short minimal required code.}

\code{df = pd.read_csv("football_data/players.csv")

plt.scatter(df['acceleration'], df['sprintspeed'])
plt.show()}

\notes{Lot's of things to improve on, even in such a simple chart. Remember that at the end, half of your reader's attention will go to charts. You should give some thought to make sure they show what you want them to, clearly and legibly.}

\code{plt.figure(figsize=(6, 6))
plt.scatter(df['acceleration'], df['sprintspeed'], alpha=0.05, color='blue', edgecolors='none')

plt.xlabel("Acceleration")
plt.ylabel("Sprint Speed")
plt.title("Acceleration vs Sprint Speed")
plt.grid(True)
plt.show()}

\subsubsection{Cheat Sheet}

\notes{Basic Line Plot

```
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.show()
```

Scatter Plot

```
plt.scatter(df['acceleration'], df['sprintspeed'], alpha=0.2)
plt.xlabel("Acceleration")
plt.ylabel("Sprint Speed")
plt.title("Acceleration vs Sprint Speed")
plt.show()
```

Bar Chart

```
categories = ['A', 'B', 'C']
values = [4, 7, 3]

plt.bar(categories, values)
plt.xlabel("Category")
plt.ylabel("Value")
plt.title("Bar Chart Example")
plt.show()
```

Histogram

```
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

plt.hist(data, bins=4, edgecolor='black')
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.title("Histogram Example")
plt.show()
```

Pie Chart

```
sizes = [30, 40, 20, 10]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart Example")
plt.show()
```

Adding Labels, Title, and Legend

```
x = [1, 2, 3]
y1 = [2, 4, 6]
y2 = [1, 3, 5]

plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Multiple Lines Example")
plt.legend()
plt.show()
```

Figure Size and Style

```
plt.figure(figsize=(8, 5))
plt.style.use('seaborn-v0_8')

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, marker='o')
plt.title("Styled Plot")
plt.show()
```

Subplots

```
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 2, 3, 4]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Plot 1")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Plot 2")

plt.tight_layout()
plt.show()
```

Saving Figures

```
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Save Example")
plt.savefig("plot.png", dpi=300)
```

Common Utilities

```
plt.grid(True)          # Show gridlines
plt.xlim(0, 10)         # Set x-axis limits
plt.ylim(0, 20)         # Set y-axis limits
plt.axhline(5, color='r', linestyle='--')  # Horizontal line
plt.axvline(2, color='g', linestyle=':')   # Vertical line
```}

\endif
