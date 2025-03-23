<!--
N.B.: README ini dibuat secara otomatis oleh <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Ini TIDAK boleh diedit dengan tangan.
-->

# django-fritzconnection untuk YunoHost

[![Tingkat integrasi](https://apps.yunohost.org/badge/integration/django-fritzconnection)](https://ci-apps.yunohost.org/ci/apps/django-fritzconnection/)
![Status kerja](https://apps.yunohost.org/badge/state/django-fritzconnection)
![Status pemeliharaan](https://apps.yunohost.org/badge/maintained/django-fritzconnection)

[![Pasang django-fritzconnection dengan YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django-fritzconnection)

*[Baca README ini dengan bahasa yang lain.](./ALL_README.md)*

> *Paket ini memperbolehkan Anda untuk memasang django-fritzconnection secara cepat dan mudah pada server YunoHost.*  
> *Bila Anda tidak mempunyai YunoHost, silakan berkonsultasi dengan [panduan](https://yunohost.org/install) untuk mempelajari bagaimana untuk memasangnya.*

## Ringkasan

[![tests](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/jedie/djfritz_ynh/branch/main/graph/badge.svg)](https://app.codecov.io/github/jedie/djfritz_ynh)
[![djfritz_ynh @ PyPi](https://img.shields.io/pypi/v/djfritz_ynh?label=djfritz_ynh%20%40%20PyPi)](https://pypi.org/project/djfritz_ynh/)
[![Python Versions](https://img.shields.io/pypi/pyversions/djfritz_ynh)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/blob/main/pyproject.toml)
[![License GPL-3.0-or-later](https://img.shields.io/pypi/l/djfritz_ynh)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/blob/main/LICENSE)

Web based FritzBox management using Python/Django and the great [fritzconnection](https://github.com/kbr/fritzconnection) library.

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)


**Versi terkirim:** 0.4.0~ynh2

## Tangkapan Layar

![Tangkapan Layar pada django-fritzconnection](./doc/screenshots/screenshot.png)

## Dokumentasi dan sumber daya

- Depot kode aplikasi hulu: <https://github.com/jedie/django-fritzconnection>
- Gudang YunoHost: <https://apps.yunohost.org/app/django-fritzconnection>
- Laporkan bug: <https://github.com/YunoHost-Apps/django-fritzconnection_ynh/issues>

## Info developer

Silakan kirim pull request ke [`testing` branch](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing).

Untuk mencoba branch `testing`, silakan dilanjutkan seperti:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing --debug
atau
sudo yunohost app upgrade django-fritzconnection -u https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing --debug
```

**Info lebih lanjut mengenai pemaketan aplikasi:** <https://yunohost.org/packaging_apps>
