import pandas as pd
import json
import lifelines
from lifelines import KaplanMeierFitter
from lifelines.utils import median_survival_times
import matplotlib.pyplot as plt
from lifelines import CoxPHFitter

with open("test_data_KaplanMeier2.json", "r", encoding='UTF-8') as f:
    temp = json.loads(f.read())
    df=pd.DataFrame(temp)
    # print(df)
    print(df.head(),'\n')
    print(df['T'].min(), df['T'].max(),'\n')
    print(df['E'].value_counts(),'\n')
    print(df['group'].value_counts(),'\n')
    
    kmf = KaplanMeierFitter()
    kmf.fit(df['T'], event_observed=df['E'])

    # kmf.plot_survival_function()
    ax=kmf.survival_function_.plot()
    #共享一个画布
    ax=kmf.plot(ax=ax)

    median_ = kmf.median_survival_time_
    median_confidence_interval_ = median_survival_times(kmf.confidence_interval_)
    print(median_confidence_interval_)
    groups = df['group']
    ix = (groups == 'largeAmount')
    
    kmf.fit(df['T'][ix], df['E'][ix], label='largeAmount')
    ax=kmf.survival_function_.plot(ax=ax)
    ax = kmf.plot(ax=ax)
    # plt.show()
    treatment_median_confidence_interval_ = median_survival_times(kmf.confidence_interval_)
    print("使用量基数较大的音乐存活50%对应的存活时间95%置信区间：'\n'", treatment_median_confidence_interval_, '\n')
    
    kmf.fit(df['T'][~ix], df['E'][~ix], label='smallAmount')
    ax=kmf.survival_function_.plot(ax=ax)
    ax = kmf.plot(ax=ax)
    # plt.show()
    
    control_median_confidence_interval_ = median_survival_times(kmf.confidence_interval_)
    print("使用量基数较小的音乐存活50%对应的存活时间95%置信区间：'\n'", control_median_confidence_interval_)

    plt.title('Survival function of tic toc music')
    # print(kmf1.median_survival_time_)
    print(median_)
    # plt.show()
    plt.xlabel("duration")  # 横坐标名字
    plt.ylabel("remaining")  # 纵坐标名字
    plt.legend(loc="best")  # 图例
    plt.savefig('KaplanMeier2.png')