# MAC Address Changer

**Identidad del paquete:** `influent.ifmac.v1.0-26.08-21.56`
**Autor:** `JesusQuijada34`
**Plataforma:** `Danenone`
**Descripción:** Estructura reparada por MoonFix

## Estructura PackageMaker 3.2.7

Este repositorio fue normalizado mediante **MoonFix**, usando la estructura de PackageMaker 3.2.7. El paquete público debe conservar `details.xml`, `version.res`, `autorun`, `autorun.bat`, `.storedetail`, `updater.py`, `config/settings.json`, los marcadores `.container` y los archivos de documentación correspondientes. El publisher oficial es `influent` y la versión pública no contiene sufijo de plataforma.

## Instalación y ejecución

Instala las dependencias declaradas en `lib/requirements.txt` cuando exista y ejecuta el entrypoint real del proyecto. En Linux, los comandos privilegiados son específicos de Danenone y no deben trasladarse a Windows. En proyectos AlphaCube, la validación Windows debe realizarse con el `buildthis` oficial de PackageMaker.

## Validación

La fuente debe pasar compilación sintáctica, pruebas funcionales disponibles, comprobación de identidad XML, protección contra traversal en ZIP y llamadas seguras a subprocess. Los artefactos `.iflapp` deben ser generados por PackageMaker; los paquetes Debian deben usar el nombre canónico `influent.ifmac.v1.0-26.08-21.56_ARCH.deb`.

## Release

El tag y el título del release deben ser exactamente `v1.0-26.08-21.56`. Los assets deben usar el nombre canónico del paquete y una extensión objetiva. No se permite publicar un release AlphaCube que contenga únicamente el build Linux.

## Referencia original

# influent Mac address changer

Paquete generado con Influent Package Maker.

## Clasificación PackageMaker

Ifmac se distribuye como **Danenone** porque modifica interfaces de red mediante `ip link` y privilegios `sudo` en Linux. No es un paquete universal ni debe ejecutarse en Windows o Android.

La herramienta genera una MAC localmente administrada usando `secrets`, valida el nombre de interfaz antes de construir comandos y utiliza listas de argumentos sin `shell=True`. El instalador usa rutas absolutas basadas en el directorio del proyecto y propaga errores de `sudo`. El actualizador bloquea traversal en ZIP y limita las descargas a 100 MB.

**Advertencia:** cambiar una MAC puede interrumpir la conectividad y requiere privilegios administrativos. Úsala únicamente en equipos y redes bajo tu control; el proyecto no ofrece anonimato ni elusión de controles.

## Ejemplo de uso
sudo python3 ifmac.py

##
