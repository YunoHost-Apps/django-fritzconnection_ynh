<!--
N.B.: Questo README è stato automaticamente generato da <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
NON DEVE essere modificato manualmente.
-->

# django-fritzconnection per YunoHost

[![Livello di integrazione](https://dash.yunohost.org/integration/django-fritzconnection.svg)](https://dash.yunohost.org/appci/app/django-fritzconnection) ![Stato di funzionamento](https://ci-apps.yunohost.org/ci/badges/django-fritzconnection.status.svg) ![Stato di manutenzione](https://ci-apps.yunohost.org/ci/badges/django-fritzconnection.maintain.svg)

[![Installa django-fritzconnection con YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django-fritzconnection)

*[Leggi questo README in altre lingue.](./ALL_README.md)*

> *Questo pacchetto ti permette di installare django-fritzconnection su un server YunoHost in modo semplice e veloce.*
> *Se non hai YunoHost, consulta [la guida](https://yunohost.org/install) per imparare a installarlo.*

## Panoramica

Web based FritzBox management using Python/Django and the great [fritzconnection](https://github.com/kbr/fritzconnection) library.

The basic idea is to block/unblock Internet access to a group of devices as easily as possible.


[![pytest](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/pytest.yml/badge.svg?branch=master)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/pytest.yml) [![YunoHost apps package linter](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/package_linter.yml/badge.svg)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/package_linter.yml) [![Coverage Status on codecov.io](https://codecov.io/gh/YunoHost-Apps/django-fritzconnection_ynh/branch/master/graph/badge.svg)](https://codecov.io/gh/YunoHost-Apps/django-fritzconnection_ynh)

![django-fritzconnection @ PyPi](https://img.shields.io/pypi/v/django-fritzconnection?label=django-fritzconnection%20%40%20PyPi)
![Python Versions](https://img.shields.io/pypi/pyversions/django-fritzconnection)
![License GPL V3+](https://img.shields.io/pypi/l/django-fritzconnection)

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)


**Versione pubblicata:** 0.2.0~ynh3

## Screenshot

![Screenshot di django-fritzconnection](./doc/screenshots/screenshot.png)

## Documentazione e risorse

- Repository upstream del codice dell’app: <https://github.com/jedie/django-fritzconnection>
- Store di YunoHost: <https://apps.yunohost.org/app/django-fritzconnection>
- Segnala un problema: <https://github.com/YunoHost-Apps/django-fritzconnection_ynh/issues>

## Informazioni per sviluppatori

Si prega di inviare la tua pull request alla [branch di `testing`](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing).

Per provare la branch di `testing`, si prega di procedere in questo modo:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing --debug
o
sudo yunohost app upgrade django-fritzconnection -u https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing --debug
```

**Maggiori informazioni riguardo il pacchetto di quest’app:** <https://yunohost.org/packaging_apps>
