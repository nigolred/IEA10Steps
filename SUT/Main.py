#%% Importing all the libraries and external information
from Shock_analysis import IEA10Steps
import mario
import pandas as pd

World = mario.parse_from_txt('Database/Russia EU and RoW - 2019', table='SUT')

# %%
NGs = World.search('Commodity','Natural gas')
sN = slice(None)
EU_NG_use = pd.concat([World.Z.loc[(sN,'Commodity',NGs),('EU')],
                      World.Y.loc[(sN,'Commodity',NGs),('EU')]]).fillna(0)

# %%
EU_NG = EU_NG_use.groupby(level=[0,1,2]).sum()
# %%
EUNG = pd.DataFrame(EU_NG.droplevel([1,2]).stack([0,1])*1e-6, columns=['Consumption [M€]'])
# %%
import plotly.express as px

plt1 = EUNG.reset_index()
plt1.columns = ['Region','Level','Category','Consumption [M€]']
plt1.replace('Activity','Intermediate demand', inplace=True)
plt1.replace('Consumption category','Final demand', inplace=True)

fig = px.sunburst(plt1.reset_index(), path=['Region','Level','Category'],
                    values='Consumption [M€]',
                    title = 'EU consumption of {}.<br>by producing region (inner level) and interemediate and final demand categories. <br>Data from EXIOBASE v3.8.2 year 2019'.format(NGs[0]))
fig.show()
fig.write_html('Plots/EU_NG consumption.html')
# %%
