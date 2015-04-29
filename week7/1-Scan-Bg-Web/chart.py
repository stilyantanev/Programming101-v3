from matplotlib import pyplot


class Chart:

    @staticmethod
    def make_plot(keys, values):

        # Convert values into percentages
        sizes = []
        for i in range(0, len(values)):
            sizes.append(round(values[i] / sum(values) * 100, 3))

        # Add percentage to name
        for i in range(0, len(keys)):
            keys[i] = keys[i] + "({}%)".format(sizes[i])

        # Make Pie-Chart
        colors = ['darkslateblue', 'gold', 'green', 'lightcoral']
        pyplot.pie(sizes, labels=keys, colors=colors, startangle=90)
        pyplot.axis('equal')
        pyplot.savefig("pie-chart.png")
