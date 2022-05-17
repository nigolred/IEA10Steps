#%% Importing all the libraries and external information
import pandas as pd
import mario

def IEA10Steps(year,shock):
    
    World = mario.parse_from_txt('Database/EUR_RUS_RoW_Exio_2019.txt') # Exiobase with EU aggregated, Russia and Rest of the World region
    World.shock_calc(shock)

