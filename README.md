# influent Mac address changer

Paquete generado con Influent Package Maker.

## Clasificación PackageMaker

Ifmac se distribuye como **Danenone** porque modifica interfaces de red mediante `ip link` y privilegios `sudo` en Linux. No es un paquete universal ni debe ejecutarse en Windows o Android.

La herramienta genera una MAC localmente administrada usando `secrets`, valida el nombre de interfaz antes de construir comandos y utiliza listas de argumentos sin `shell=True`. El instalador usa rutas absolutas basadas en el directorio del proyecto y propaga errores de `sudo`. El actualizador bloquea traversal en ZIP y limita las descargas a 100 MB.

**Advertencia:** cambiar una MAC puede interrumpir la conectividad y requiere privilegios administrativos. Úsala únicamente en equipos y redes bajo tu control; el proyecto no ofrece anonimato ni elusión de controles.

## Ejemplo de uso
sudo python3 ifmac.py

##