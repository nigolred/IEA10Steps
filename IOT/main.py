#%% 9th of March 2022
# Import the libraries that you need
import mario

#%% Importing the version of Exiobase that you like. In this case Exiobase 3.8.2, year 2019, pxp

World = mario.parse_exiobase_3(r'C:\Users\Gollinucci\Desktop\Nicolò\Lavoro\FEEM\Databases\EXIOBASE_3.8.2\IOT_2019_pxp.zip')
#%% Now is time to aggregate your database so that you can make a conceptual example before scaling-up the analysis

# Create your aggregation file (be careful, you may overwrite what you did if you run this line after filling the file without changing the name)
# World.get_aggregation_excel('Aggregations/Agg1.xlsx')

# %% Aggregating and printing to excel so we can have the conceptual model

# World_agg = World.aggregate('Aggregations/Small_agg.xlsx', inplace=False)
# World_agg.to_excel('Database/Small_db.xlsx')



# %% 10th of March 2022
# Preparing the shock

# Lets aggregate our World
World.aggregate('Aggregations/Big_agg.xlsx')

#%% Create your shock file (be careful, you may overwrite what you did if you run this line after filling the file without changing the name)
cluster = {'Sector': {'All': World.get_index('Sector')}}

# World.get_shock_excel('Shocks/shock1.xlsx', **cluster)
#%% Total consumption of Natural Gas according to Exiobase
NG = World.search('Sector','Natural gas') # to ease loc notation
sn = slice(None) # to ease loc notation


FF = ['Anthracite','Coking Coal','Other Bituminous Coal','Sub-Bituminous Coal',
'Patent Fuel','Lignite/Brown Coal','BKB/Peat Briquettes','Peat',
'Crude petroleum and services related to crude oil extraction, excluding surveying',
'Natural gas and services related to natural gas extraction, excluding surveying',
'Natural Gas Liquids','Other Hydrocarbons']


EU_NG_cons_mo = World.Z.loc[(sn,sn,NG),'EU-27'].sum().sum()+World.Y.loc[(sn,sn,NG),'EU-27'].sum().sum()
EU_FF_cons_mo = World.Z.loc[(sn,sn,FF),'EU-27'].sum().sum()+World.Y.loc[(sn,sn,FF),'EU-27'].sum().sum()


# %% Run the shock

World.shock_calc('Shocks/Low1C.xlsx', Y=True, scenario='Lowering heat by 1°C')
World.shock_calc('Shocks/ShiftSup.xlsx', z=True, scenario='Shifting suppliers', **cluster)


# %%
Res_world = World.aggregate('Aggregations/Res_agg.xlsx', inplace=False)
#%%
Res_world.plot_matrix('V', x='Region_to',y='Value', 
                      facet_col='Factor of production', color='Sector_to', 
                      base_scenario='baseline')
#%%
Res_world.plot_matrix('E', x='Region_to',y='Value', 
                      facet_col='Satellite account', color='Sector_to', 
                      base_scenario='baseline',
                      filter_Satellite_account = ['CO2'])
# %%
Res_world.plot_matrix('E', x='Region_to',y='Value', 
                      facet_col='Satellite account', color='Sector_to', 
                      base_scenario='baseline',
                      filter_Satellite_account = ['Employment'])
# %%
