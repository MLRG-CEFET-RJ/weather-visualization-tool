import s3fs
import xarray as xr
import datetime as dt
import argparse
import numpy as np
import pandas as pd
import geopandas as gpd
from timeit import default_timer as timer

fs = s3fs.S3FileSystem(anon=True)
# Get products of GOES-16 bucket.
products = fs.ls('s3://noaa-goes16/')

product = "ABI-L2-TPWC" 


# Utilizando no código
start_date = dt.date(2021,12,31)
end_date = dt.date(2022,1,1)

# Utilizando o argparse. Daqui
def date_type(string):
    try:
        date = dt.datetime.strptime(string, "%Y-%m-%d").date()
        return date
    except ValueError:
        raise argparse.ArgumentTypeError("Data inválida. Utilize o formato YYYY-MM-DD.")

parser = argparse.ArgumentParser()
parser.add_argument("--data_inicial", type=date_type, help="Data inicial no formato YYYY-MM-DD")
parser.add_argument("--data_final", type=date_type, help="Data final no formato YYYY-MM-DD")
args = parser.parse_args()
start_date = args.data_inicial
end_date = args.data_final
#até aqui
data_year_current = start_date.year
if start_date == end_date:
    days_traveled = 0
else:
    days_traveled = int((str(end_date - start_date)).split(" ")[0])
year_for_days = (start_date - dt.date(start_date.year, 1, 1)).days + 1
add_days = 0

ds = None  # Inicializar a variável ds

for dsp in range(days_traveled + 1):
    year_for_days_current = str(year_for_days + add_days)
    for hours in range(24):
        target = f'noaa-goes16/{product}/{data_year_current}/{year_for_days_current}/{str(hours)}'
        files = np.array(fs.ls(target))
        if len(files) > 0:
            for i in range(len(files)):
                print(files)
                filename = files[i].split('/')[-1]
                fs.get(files[i], filename)
                ds = xr.open_dataset(filename)

if ds is not None:
    print(ds)
else:
    print("Nenhum arquivo válido encontrado.")

# Define bounding box coordinates
#lat_min, lat_max = -23.082616, -22.76894
#lon_min, lon_max = -43.823426, -43.154634

#def filter_rrqpe(rrqpe, lat, lon, lat_min, lat_max, lon_min, lon_max):
#    return np.where((lat >= lat_min) & (lat <= lat_max) &
#                    (lon >= lon_min) & (lon <= lon_max), rrqpe, np.nan)

