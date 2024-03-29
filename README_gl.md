<!--
NOTA: Este README foi creado automáticamente por <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
NON debe editarse manualmente.
-->

# django-fritzconnection para YunoHost

[![Nivel de integración](https://dash.yunohost.org/integration/django-fritzconnection.svg)](https://dash.yunohost.org/appci/app/django-fritzconnection) ![Estado de funcionamento](https://ci-apps.yunohost.org/ci/badges/django-fritzconnection.status.svg) ![Estado de mantemento](https://ci-apps.yunohost.org/ci/badges/django-fritzconnection.maintain.svg)

[![Instalar django-fritzconnection con YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django-fritzconnection)

*[Le este README en outros idiomas.](./ALL_README.md)*

> *Este paquete permíteche instalar django-fritzconnection de xeito rápido e doado nun servidor YunoHost.*  
> *Se non usas YunoHost, le a [documentación](https://yunohost.org/install) para saber como instalalo.*

## Vista xeral

Web based FritzBox management using Python/Django and the great [fritzconnection](https://github.com/kbr/fritzconnection) library.

The basic idea is to block/unblock Internet access to a group of devices as easily as possible.


[![pytest](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/pytest.yml/badge.svg?branch=master)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/pytest.yml) [![YunoHost apps package linter](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/package_linter.yml/badge.svg)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/package_linter.yml) [![Coverage Status on codecov.io](https://codecov.io/gh/YunoHost-Apps/django-fritzconnection_ynh/branch/master/graph/badge.svg)](https://codecov.io/gh/YunoHost-Apps/django-fritzconnection_ynh)

![django-fritzconnection @ PyPi](https://img.shields.io/pypi/v/django-fritzconnection?label=django-fritzconnection%20%40%20PyPi)
![Python Versions](https://img.shields.io/pypi/pyversions/django-fritzconnection)
![License GPL V3+](https://img.shields.io/pypi/l/django-fritzconnection)

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)


**Versión proporcionada:** 0.2.0~ynh3

## Capturas de pantalla

![Captura de pantalla de django-fritzconnection](./doc/screenshots/screenshot.png)

## Documentación e recursos

- Repositorio de orixe do código: <https://github.com/jedie/django-fritzconnection>
- Tenda YunoHost: <https://apps.yunohost.org/app/django-fritzconnection>
- Informar dun problema: <https://github.com/YunoHost-Apps/django-fritzconnection_ynh/issues>

## Info de desenvolvemento

Envía a túa colaboración á [rama `testing`](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing).

Para probar a rama `testing`, procede deste xeito:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing --debug
ou
sudo yunohost app upgrade django-fritzconnection -u https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing --debug
```

**Máis info sobre o empaquetado da app:** <https://yunohost.org/packaging_apps>
