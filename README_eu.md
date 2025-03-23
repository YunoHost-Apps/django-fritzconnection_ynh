<!--
Ohart ongi: README hau automatikoki sortu da <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>ri esker
EZ editatu eskuz.
-->

# django-fritzconnection YunoHost-erako

[![Integrazio maila](https://apps.yunohost.org/badge/integration/django-fritzconnection)](https://ci-apps.yunohost.org/ci/apps/django-fritzconnection/)
![Funtzionamendu egoera](https://apps.yunohost.org/badge/state/django-fritzconnection)
![Mantentze egoera](https://apps.yunohost.org/badge/maintained/django-fritzconnection)

[![Instalatu django-fritzconnection YunoHost-ekin](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django-fritzconnection)

*[Irakurri README hau beste hizkuntzatan.](./ALL_README.md)*

> *Pakete honek django-fritzconnection YunoHost zerbitzari batean azkar eta zailtasunik gabe instalatzea ahalbidetzen dizu.*  
> *YunoHost ez baduzu, kontsultatu [gida](https://yunohost.org/install) nola instalatu ikasteko.*

## Aurreikuspena

[![tests](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/jedie/djfritz_ynh/branch/main/graph/badge.svg)](https://app.codecov.io/github/jedie/djfritz_ynh)
[![djfritz_ynh @ PyPi](https://img.shields.io/pypi/v/djfritz_ynh?label=djfritz_ynh%20%40%20PyPi)](https://pypi.org/project/djfritz_ynh/)
[![Python Versions](https://img.shields.io/pypi/pyversions/djfritz_ynh)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/blob/main/pyproject.toml)
[![License GPL-3.0-or-later](https://img.shields.io/pypi/l/djfritz_ynh)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/blob/main/LICENSE)

Web based FritzBox management using Python/Django and the great [fritzconnection](https://github.com/kbr/fritzconnection) library.

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)


**Paketatutako bertsioa:** 0.4.0~ynh2

## Pantaila-argazkiak

![django-fritzconnection(r)en pantaila-argazkia](./doc/screenshots/screenshot.png)

## Dokumentazioa eta baliabideak

- Jatorrizko aplikazioaren kode-gordailua: <https://github.com/jedie/django-fritzconnection>
- YunoHost Denda: <https://apps.yunohost.org/app/django-fritzconnection>
- Eman errore baten berri: <https://github.com/YunoHost-Apps/django-fritzconnection_ynh/issues>

## Garatzaileentzako informazioa

Bidali `pull request`a [`testing` abarrera](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing).

`testing` abarra probatzeko, ondorengoa egin:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing --debug
edo
sudo yunohost app upgrade django-fritzconnection -u https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing --debug
```

**Informazio gehiago aplikazioaren paketatzeari buruz:** <https://yunohost.org/packaging_apps>
