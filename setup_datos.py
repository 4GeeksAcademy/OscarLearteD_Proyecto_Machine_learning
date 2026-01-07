import zipfile
import os

# --- CONFIGURACIÓN ---
nombre_zip = 'datos_proyecto.zip'

# 1. BUSCAR EL ZIP (Sea donde sea que estemos)
# Buscamos en la carpeta actual (.) y en la carpeta superior (..)
rutas_posibles = [
    nombre_zip,                 # Si se ejecuta desde la raíz
    os.path.join('..', nombre_zip), # Si se ejecuta desde src/
    os.path.join('src', nombre_zip) # Por si acaso
]

archivo_encontrado = None
for ruta in rutas_posibles:
    if os.path.exists(ruta):
        archivo_encontrado = ruta
        print(f"✅ ZIP encontrado en: {archivo_encontrado}")
        break

# 2. DESCOMPRIMIR
if archivo_encontrado:
    print("📂 Descomprimiendo archivos...")
    try:
        # Extraemos en la carpeta actual donde se ejecuta el script
        with zipfile.ZipFile(archivo_encontrado, 'r') as zip_ref:
            zip_ref.extractall('.')
        print("🎉 ¡ÉXITO! Los archivos CSV ya están listos para usarse.")
    except Exception as e:
        print(f"❌ Error al descomprimir: {e}")
else:
    print("❌ ERROR: No encuentro 'datos_proyecto.zip'.")
    print(f"   He buscado en: {rutas_posibles}")
    print("   Asegúrate de haber descargado el ZIP o hecho git pull.")