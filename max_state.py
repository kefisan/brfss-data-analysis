import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import find_states


def year_graphs(category, indicator):

    max_state_var = find_states.plot_data()

    df = pd.read_csv('cleaned_data.csv')

    df_filtered = df[df['Indicator'] == indicator]
    df_filtered = df_filtered[df_filtered['LocationDesc'] == max_state_var]
    df_filtered = df_filtered[df_filtered['Break_Out_Category'] == category]

    years = sorted(df_filtered['Year'].unique())
    values = sorted(df_filtered['Break_out'].unique())

    x = np.arange(len(years))
    width = 0.15

    fig, ax = plt.subplots(figsize=(12, 6), constrained_layout=True)
    colors = matplotlib.colormaps.get_cmap('viridis')

    for i, value in enumerate(values):
        measurements = []
        for year in years:
            measurement = df_filtered[(df_filtered['Year'] == year) & (df_filtered['Break_out'] == value)][
                'Data_Value']
            measurements.append(measurement.values[0] if len(measurement) > 0 else 0)
        rects = ax.bar(x + width * i, measurements, width, label=value, color=colors(i / len(values)))
        ax.bar_label(rects, padding=3)

    indicator = indicator[:indicator.find(' among')]

    ax.set_ylabel('Values, %', fontweight='bold')
    ax.set_title(f'{indicator} by {category} and Year', fontweight='bold')
    ax.set_xticks(x + width * len(values) / 2)
    ax.set_xticklabels(years)
    ax.legend(loc='upper left')
    ax.set_ylim(0, 100)

    plt.savefig(f'{category}_{max_state_var}_Plot')


# Example usage:

year_graphs('Age', 'Prevalence of coronary heart disease among US adults (18+) (Percentage); BRFSS')
year_graphs('Gender', 'Prevalence of obesity among US adults (20+) (Percentage); BRFSS')
year_graphs('Race', 'Prevalence of hypertension medication use among US adults (18+) with hypertension (Percentage); BRFSS')
