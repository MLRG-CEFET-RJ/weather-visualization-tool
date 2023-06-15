import os
import xarray as xr

# Especificar o diretório onde os arquivos foram baixados
# Dar copypath no arquivo .nc e copiar em diretorio


import xarray as xr

# Abrir o arquivo NetCDF
filename = r'C:\Users\tadas\Facul\PCS\wvtool\backend\landing\OR_ABI-L2-TPWC-M6_G16_s20213632351172_e20213632353545_c20213632356208.nc'
ds = xr.open_dataset(filename)
#for var_name in ds.data_vars.keys():
#    var_data = ds[var_name]  # Acessar a variável de dados pelo nome
#    print(var_data)  # Fazer o que você precisa com a variável de dados

tpw_variable = ds['TPW']
print(tpw_variable)
# Extrair os valores de latitude e longitude
tpwy_values = tpw_variable['y'].values
tpwx_values = tpw_variable['x'].values

# Imprimir os valores de x
print("Valores de x:")
print(tpwy_values)
# Imprimir os valores de y
print("valores de y")
print(tpwx_values)
# Obter a escala utilizada para a TPW
escala_tpw = tpw_variable.attrs['units']
# Imprimir a escala utilizada
print("Escala da TPW:", escala_tpw)

lat_variable = ds['latitude']
escala_latitude = lat_variable.latitude.attrs['units']

# Imprimir a escala utilizada
print("Escala da Latitude:", escala_latitude)


longitude = ds['nominal_satellite_subpoint_lon'].values

# Imprima os valores de longitude
print(longitude)
#lon_variable = ds['longitude']
#escala_longitude = lon_variable.longitude.attrs['units']

# Imprimir a escala utilizada
#print("Escala da Longitude:", escala_longitude)