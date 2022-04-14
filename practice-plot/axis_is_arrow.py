import japanize_matplotlib
import matplotlib.pyplot as plt
import numpy as np

xticks = [0.9, 1.2, 2, 2.8, 3.1]
xticklabel = ['', '何を言っているか分からないし、\n ノイズも目立つ',
              '言葉は十分に聞き取れるが、\n ノイズが目立つ',
              '最も音質がきれい', '']
x_data = [1.2, 2, 2.8]
y_data = [0.4246, 0.1824, 0.2411]
y_error = [0.0505, 0.0202, 0.0423]
grad = (y_data[2] - y_data[0]) / (x_data[2] - x_data[0])

x_subdata = [1.1, 3.0]
y_subdata = [0.24, 0.24]

text = ['Tacotron2', 'ComformerFastSpeech2', 'VITS']

fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111, ylabel='logF0 RMSE',
                     xlabel='主観評価', xticks=xticks)
ax.errorbar(x_data, y_data, yerr=y_error,
            fmt='o', markersize=13, capsize=5)
ax.scatter(x_subdata, y_subdata, alpha=0)
ax.plot(
    [x_data[0]-0.2, x_data[2]+0.2],
    [y_data[0]-grad*0.2, y_data[2]+grad*0.2],
    '--', color='red',
)

for t, x, y in zip(text, x_data, y_data):
    ax.text(x, y+0.01, t, va='bottom', ha='center')
ax.set_xlabel('主観評価', fontsize=12)
ax.set_xticklabels(xticklabel, fontsize=8, rotation=0, ha='center')
ax.set_ylim([0.48, 0.15])
ax.tick_params(bottom=False)
ax.grid(c='gainsboro', zorder=9)
ax.spines['right'].set(alpha=0)
ax.spines['top'].set(alpha=0)
ax.spines['bottom'].set(alpha=0)

ax.annotate('良い', (1.0, 0.48), (3.2, 0.484), zorder=10, ha='center', size=14,
            arrowprops=dict(arrowstyle='<|-', mutation_scale=20))
ax.annotate('良い', (1.0, 0.48), (1.0, 0.14), zorder=10, va='center', ha='center', size=14,
            arrowprops=dict(arrowstyle='<|-', mutation_scale=20))
plt.savefig('tmp.png')
plt.show()
