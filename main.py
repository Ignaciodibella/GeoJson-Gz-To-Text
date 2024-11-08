import gzip
import geojson
from shapely.geometry import shape
from shapely.wkt import dumps as wkt_dumps

# Ruta al archivo .geojson.gz
file_path = 'OSMB-2da73f57a5986989e2aaf53adc5b371380858757.geojson.gz'

with gzip.open(file_path, 'rt', encoding='utf-8') as f:
    geojson_data = geojson.load(f)

# Exportar FeatureCollection (simil GeoJson) a un txt:
with open('output.txt', 'w') as f:
    geojson.dump(geojson_data, f)

print("Exportación Finalizada")

# Extraer contenido "GeoJson" a wkt's y exportar:
wkt_geometries = []
for feature in geojson_data['features']:
    geometry = shape(feature['geometry'])
    wkt_geometries.append(wkt_dumps(geometry))

# Mostrar los resultados
for wkt in wkt_geometries:
    print(wkt)

# Escribir las geometrías WKT en un archivo .txt
with open('geometries.txt', 'w') as file:
    for wkt in wkt_geometries:
        file.write(wkt + '\n \n')

print("Geometrías WKT exportadas exitosamente a geometries.txt")
