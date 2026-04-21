'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt


# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def fta_barplot(pred_universe):
   
    fta_counts = pred_universe.groupby(['fta']).size().reset_index(name='count')
    sns.barplot(data=fta_counts, x='fta', y='count')
    plt.savefig('./data/part3_plots/fta_barplot.png', bbox_inches='tight')
    plt.clf()


# 2. Hue the previous barplot by sex

def fta_barplot_by_sex(pred_universe):
    
    fta_counts_by_sex = pred_universe.groupby(['fta', 'sex']).size().reset_index(name='count')
    sns.barplot(data=fta_counts_by_sex, x='fta', y='count', hue='sex')
    plt.savefig('./data/part3_plots/fta_barplot_by_sex.png', bbox_inches='tight')
    plt.clf()

# 3. Plot a histogram of age_at_arrest

def age_histogram(pred_universe):

    sns.histplot(data=pred_universe, x='age_at_arrest')
    plt.savefig('./data/part3_plots/age_histogram.png', bbox_inches='tight')
    plt.clf()

# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 
def age_histogram_bins(pred_universe):
  
    sns.histplot(data=pred_universe, x='age_at_arrest', bins=[18, 21, 30, 40, 100])
    plt.savefig('./data/part3_plots/age_histogram_bins.png', bbox_inches='tight')
    plt.clf()