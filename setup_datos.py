import zipfile
import os
import shutil

# Configuración
zip_file = 'datos_proyecto.zip'
carpeta_destino = 'src' # Donde suelen vivir los notebooks

def instalar_datos():
    if not os.path.exists(zip_file):
        print("❌ ERROR: No encuentro 'datos_proyecto.zip'.")
        print("   ¿Has hecho 'git pull' para bajarte los últimos cambios?")
        return

    print(f"📦 Descomprimiendo {zip_file}...")
    
    # Determinar dónde extraer
    ruta_extraccion = '.'
    if os.path.exists(carpeta_destino):
        ruta_extraccion = carpeta_destino
        print(f"   -> Detectada carpeta '{carpeta_destino}'. Los datos irán allí.")
    else:
        print("   -> No veo carpeta 'src', se descomprimirán aquí mismo (raíz).")

    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(ruta_extraccion)
        
        print("\n✅ ¡LISTO! Archivos CSV descomprimidos con éxito.")
        print(f"📍 Los tienes en: {os.path.abspath(ruta_extraccion)}")
        
    except Exception as e:
        print(f"❌ Algo falló al descomprimir: {e}")

if __name__ == "__main__":
    instalar_datos()