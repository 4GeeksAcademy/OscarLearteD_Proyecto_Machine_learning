import zipfile
import os

zip_file = 'datos_proyecto.zip'

if os.path.exists(zip_file):
    print('📂 Descomprimiendo datasets...')
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall('.')
    print('✅ ¡Datos listos! Ya tienes los CSV originales.')
else:
    print('❌ No encuentro el archivo zip.')