<!--
Nota bene : ce README est automatiquement généré par <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Il NE doit PAS être modifié à la main.
-->

# django-fritzconnection pour YunoHost

[![Niveau d’intégration](https://apps.yunohost.org/badge/integration/django-fritzconnection)](https://ci-apps.yunohost.org/ci/apps/django-fritzconnection/)
![Statut du fonctionnement](https://apps.yunohost.org/badge/state/django-fritzconnection)
![Statut de maintenance](https://apps.yunohost.org/badge/maintained/django-fritzconnection)

[![Installer django-fritzconnection avec YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django-fritzconnection)

*[Lire le README dans d'autres langues.](./ALL_README.md)*

> *Ce package vous permet d’installer django-fritzconnection rapidement et simplement sur un serveur YunoHost.*  
> *Si vous n’avez pas YunoHost, consultez [ce guide](https://yunohost.org/install) pour savoir comment l’installer et en profiter.*

## Vue d’ensemble

[![tests](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/jedie/djfritz_ynh/branch/main/graph/badge.svg)](https://app.codecov.io/github/jedie/djfritz_ynh)
[![djfritz_ynh @ PyPi](https://img.shields.io/pypi/v/djfritz_ynh?label=djfritz_ynh%20%40%20PyPi)](https://pypi.org/project/djfritz_ynh/)
[![Python Versions](https://img.shields.io/pypi/pyversions/djfritz_ynh)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/blob/main/pyproject.toml)
[![License GPL-3.0-or-later](https://img.shields.io/pypi/l/djfritz_ynh)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/blob/main/LICENSE)

Web based FritzBox management using Python/Django and the great [fritzconnection](https://github.com/kbr/fritzconnection) library.

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)


**Version incluse :** 0.4.0~ynh2

## Captures d’écran

![Capture d’écran de django-fritzconnection](./doc/screenshots/screenshot.png)

## Documentations et ressources

- Dépôt de code officiel de l’app : <https://github.com/jedie/django-fritzconnection>
- YunoHost Store : <https://apps.yunohost.org/app/django-fritzconnection>
- Signaler un bug : <https://github.com/YunoHost-Apps/django-fritzconnection_ynh/issues>

## Informations pour les développeurs

Merci de faire vos pull request sur la [branche `testing`](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing).

Pour essayer la branche `testing`, procédez comme suit :

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing --debug
ou
sudo yunohost app upgrade django-fritzconnection -u https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing --debug
```

**Plus d’infos sur le packaging d’applications :** <https://yunohost.org/packaging_apps>
