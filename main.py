import gzip
import geojson

# Ruta al archivo .geojson.gz
file_path = 'OSMB-2da73f57a5986989e2aaf53adc5b371380858757.geojson.gz'

with gzip.open(file_path, 'rt', encoding='utf-8') as f:
    geojson_data = geojson.load(f)

# Mostrar Data
print(geojson_data)
