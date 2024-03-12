import pandas as pd
import matplotlib.pyplot as plt


def plot_data():

    df = pd.read_csv('cleaned_data.csv')

    df_filtered = df[df['Indicator'] == 'Prevalence of obesity among US adults (20+) (Percentage); BRFSS']
    df_filtered = df_filtered[df_filtered['Break_out'] == 'Overall']

    average_values = df_filtered.groupby('LocationDesc')['Data_Value'].mean()

    max_state_var = average_values.idxmax()
    avg_values_list = average_values.tolist()

    colors = ['crimson' if val == max(avg_values_list) else 'deepskyblue' for val in avg_values_list]

    plt.rcParams.update({'font.weight': 'bold'})

    plt.figure(figsize=(14, 8))
    plt.barh(y=average_values.index, width=average_values.values, color=colors)
    plt.title('Prevalence of obesity among US adults (20+)', fontweight='bold')
    plt.xlabel('Values, %', fontweight='bold')
    plt.ylabel('States', fontweight='bold')
    plt.savefig('All_States_Plot')

    return max_state_var


plot_data()
