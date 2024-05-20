<!--
Este archivo README esta generado automaticamente<https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
No se debe editar a mano.
-->

# django-fritzconnection para Yunohost

[![Nivel de integración](https://dash.yunohost.org/integration/django-fritzconnection.svg)](https://dash.yunohost.org/appci/app/django-fritzconnection) ![Estado funcional](https://ci-apps.yunohost.org/ci/badges/django-fritzconnection.status.svg) ![Estado En Mantención](https://ci-apps.yunohost.org/ci/badges/django-fritzconnection.maintain.svg)

[![Instalar django-fritzconnection con Yunhost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django-fritzconnection)

*[Leer este README en otros idiomas.](./ALL_README.md)*

> *Este paquete le permite instalardjango-fritzconnection rapidamente y simplement en un servidor YunoHost.*  
> *Si no tiene YunoHost, visita [the guide](https://yunohost.org/install) para aprender como instalarla.*

## Descripción general

Web based FritzBox management using Python/Django and the great [fritzconnection](https://github.com/kbr/fritzconnection) library.

The basic idea is to block/unblock Internet access to a group of devices as easily as possible.


[![pytest](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/pytest.yml/badge.svg?branch=master)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/pytest.yml) [![YunoHost apps package linter](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/package_linter.yml/badge.svg)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/package_linter.yml) [![Coverage Status on codecov.io](https://codecov.io/gh/YunoHost-Apps/django-fritzconnection_ynh/branch/master/graph/badge.svg)](https://codecov.io/gh/YunoHost-Apps/django-fritzconnection_ynh)

![django-fritzconnection @ PyPi](https://img.shields.io/pypi/v/django-fritzconnection?label=django-fritzconnection%20%40%20PyPi)
![Python Versions](https://img.shields.io/pypi/pyversions/django-fritzconnection)
![License GPL V3+](https://img.shields.io/pypi/l/django-fritzconnection)

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)


**Versión actual:** 0.2.0~ynh3

## Capturas

![Captura de django-fritzconnection](./doc/screenshots/screenshot.png)

## Documentaciones y recursos

- Repositorio del código fuente oficial de la aplicación : <https://github.com/jedie/django-fritzconnection>
- Catálogo YunoHost: <https://apps.yunohost.org/app/django-fritzconnection>
- Reportar un error: <https://github.com/YunoHost-Apps/django-fritzconnection_ynh/issues>

## Información para desarrolladores

Por favor enviar sus correcciones a la [`branch testing`](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing

Para probar la rama `testing`, sigue asÍ:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing --debug
o
sudo yunohost app upgrade django-fritzconnection -u https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing --debug
```

**Mas informaciones sobre el empaquetado de aplicaciones:** <https://yunohost.org/packaging_apps>
