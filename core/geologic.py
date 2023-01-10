import geopandas as gpd


geodata = gpd.read_file(r"C:\Users\olumi\Downloads\map.osm")
geodata.plot()