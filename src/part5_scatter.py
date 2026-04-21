'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''





import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
#
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?

def felony_scatter(pred_universe_felony):
  
    sns.lmplot(data=pred_universe_felony,
               x='prediction_felony',
               y='prediction_nonfelony',
               hue='has_felony_charge',
               fit_reg=False)
    plt.savefig('./data/part5_plots/felony_scatter.png', bbox_inches='tight')
    plt.clf()

    print("The dots on the right side have high felony prediction scores and are mostly arrests that had a felony charge. " \
    "This suggests the model assigns higher felony risk scores to people with current felony charges, and those same people also tend to have higher nonfelony prediction scores.")

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?

def felony_prediction_vs_outcome(pred_universe_felony):

    sns.lmplot(data=pred_universe_felony,
               x='prediction_felony',
               y='y_felony',
               fit_reg=False)
    plt.savefig('./data/part5_plots/felony_prediction_vs_outcome.png', bbox_inches='tight')
    plt.clf()

    print("A calibrated model would show a clear upward trend where higher prediction scores correspond to more actual rearrests. " \
    "Instead the plot shows two flat bands of dots at y=0 and y=1 spread across all prediction values, which means the model assigns similar scores to people who did and did not get rearrested.")