from lifelines import CoxPHFitter
import matplotlib.pyplot as plt
import json
import pandas as pd

with open("test_data_Cox2.json", "r", encoding='UTF-8') as f:
    temp = json.loads(f.read())
    regression_dataset = pd.DataFrame(temp,columns=['T','E','base','hotestVideo','length'])

    print(regression_dataset.head())
    print(regression_dataset['E'].value_counts())

    cph = CoxPHFitter()
    cph.fit(regression_dataset, 'T', event_col='E')
    cph.print_summary()
    cph.plot()
    plt.savefig('Cox4.png')