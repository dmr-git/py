# sample program to chart with pygal

import pygal
from pygal.style import LightSolarizedStyle

# bar_chart = pygal.Bar()
bar_chart = pygal.StackedBar(style=LightSolarizedStyle)
# bar_chart = pygal.HorizontalStackedBar(style=LightSolarizedStyle)

bar_chart.add("Fibonacci", [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
bar_chart.add("Padovan", [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])

bar_chart.title = "Famous Mathematical Sequences"
bar_chart.x_labels = map(str, range(11))

# write the chart to a file
bar_chart.render_to_file("bar_chart.svg")

# write the chart to a browser
bar_chart.render_in_browser()
