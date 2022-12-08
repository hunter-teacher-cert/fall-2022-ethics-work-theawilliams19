# %%
%matplotlib inline
import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import textwrap

# %%
data_places = pd.read_csv("C:/Users/kherr1/Documents/CS files/ethics/project files/bdc_us_broadband_summary_by_geography.csv", low_memory = False)

# %%
plot_data_exclusive = pd.DataFrame({
    'dl0_ul0': data_places['fixed_res_dl0_ul0_pct'] - data_places['fixed_res_dl10_ul1_pct'],
    'dl10_ul1': data_places['fixed_res_dl10_ul1_pct'] - data_places['fixed_res_dl25_ul3_pct'],
    'dl25_ul3': data_places['fixed_res_dl25_ul3_pct'] - data_places['fixed_res_dl100_ul20_pct'],
    'dl100_ul20': data_places['fixed_res_dl100_ul20_pct'] - data_places['fixed_res_dl1000_ul100_pct'],
    'dl1000_ul100': data_places['fixed_res_dl1000_ul100_pct']
    })

plot_data_inclusive = pd.DataFrame({
    'dl0_ul0': data_places['fixed_res_dl0_ul0_pct'],
    'dl10_ul1': data_places['fixed_res_dl10_ul1_pct'],
    'dl25_ul3': data_places['fixed_res_dl25_ul3_pct'],
    'dl100_ul20': data_places['fixed_res_dl100_ul20_pct'],
    'dl1000_ul100': data_places['fixed_res_dl1000_ul100_pct']
})

# %%
no_conn = round(1 - plot_data_inclusive['dl0_ul0'], 4)
no_conn_no_0 = no_conn[no_conn >= 0.0001]
slow_conn = 1 - plot_data_inclusive['dl25_ul3']
slow_conn_no_0 = round(slow_conn[slow_conn >= 0.0001], 4)
slow_not_0 = slow_conn - no_conn
slow_not_0_no_0 = slow_not_0[slow_not_0 >= 0.0001]

# %%
fig, axes = plt.subplots(3, 1)
plt.suptitle('Units in Broadband Serviceable Areas')
fig.tight_layout()
plt.subplot(3, 1, 1)
plt.xlabel('Fraction of Units with No Broadband or Slow Speeds (speeds < 25/3)')
slow_conn_no_0.hist(bins = 100)
plt.subplot(3, 1, 2)
plt.xlabel('Fraction of Units without Broadband (speeds < 0.2/0.2)')
no_conn_no_0.hist(bins = 100)
plt.subplot(3, 1, 3)
plt.xlabel('Fraction of Units with Broadband at Slow Speeds (speeds < 25/3)')
slow_not_0_no_0.hist(bins = 100)


# %%
print(len(slow_conn_no_0))
print(len(no_conn_no_0))

# %%
income_data = pd.DataFrame(
    {'Low Income (< 30,000 Per Year)': {'No Smartphone': 29, 'No Broadband': 44, 'No Laptop/Desktop': 46, 'No Tablet': 64, 'Own All 4': 18}, 
    'High Income (> 100,000 Per Year)': {'No Smartphone': 3, 'No Broadband': 6, 'No Laptop/Desktop': 6, 'No Tablet': 30, 'Own All 4': 64}}
    )

# %%
def wrap_labels(labels: list[str], width = 6, break_long_words = False):
    wrapped = []
    for label in labels:
        wrapped.append(textwrap.fill(label, width = width, break_long_words = break_long_words))
    return wrapped

# %%

income_data.index = wrap_labels(income_data.index)
income_data.plot.bar(title = 'Percent of American Device/Service Ownership', ylabel = 'Percent', rot = 0)


