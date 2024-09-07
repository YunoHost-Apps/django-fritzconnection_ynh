<!--
Важно: этот README был автоматически сгенерирован <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Он НЕ ДОЛЖЕН редактироваться вручную.
-->

# django-fritzconnection для YunoHost

[![Уровень интеграции](https://dash.yunohost.org/integration/django-fritzconnection.svg)](https://ci-apps.yunohost.org/ci/apps/django-fritzconnection/) ![Состояние работы](https://ci-apps.yunohost.org/ci/badges/django-fritzconnection.status.svg) ![Состояние сопровождения](https://ci-apps.yunohost.org/ci/badges/django-fritzconnection.maintain.svg)

[![Установите django-fritzconnection с YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django-fritzconnection)

*[Прочтите этот README на других языках.](./ALL_README.md)*

> *Этот пакет позволяет Вам установить django-fritzconnection быстро и просто на YunoHost-сервер.*  
> *Если у Вас нет YunoHost, пожалуйста, посмотрите [инструкцию](https://yunohost.org/install), чтобы узнать, как установить его.*

## Обзор

[![tests](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/jedie/djfritz_ynh/branch/main/graph/badge.svg)](https://app.codecov.io/github/jedie/djfritz_ynh)
[![djfritz_ynh @ PyPi](https://img.shields.io/pypi/v/djfritz_ynh?label=djfritz_ynh%20%40%20PyPi)](https://pypi.org/project/djfritz_ynh/)
[![Python Versions](https://img.shields.io/pypi/pyversions/djfritz_ynh)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/blob/main/pyproject.toml)
[![License GPL-3.0-or-later](https://img.shields.io/pypi/l/djfritz_ynh)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/blob/main/LICENSE)

Web based FritzBox management using Python/Django and the great [fritzconnection](https://github.com/kbr/fritzconnection) library.

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)


**Поставляемая версия:** 0.3.0~ynh5

## Снимки экрана

![Снимок экрана django-fritzconnection](./doc/screenshots/screenshot.png)

## Документация и ресурсы

- Репозиторий кода главной ветки приложения: <https://github.com/jedie/django-fritzconnection>
- Магазин YunoHost: <https://apps.yunohost.org/app/django-fritzconnection>
- Сообщите об ошибке: <https://github.com/YunoHost-Apps/django-fritzconnection_ynh/issues>

## Информация для разработчиков

Пришлите Ваш запрос на слияние в [ветку `testing`](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing).

Чтобы попробовать ветку `testing`, пожалуйста, сделайте что-то вроде этого:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing --debug
или
sudo yunohost app upgrade django-fritzconnection -u https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing --debug
```

**Больше информации о пакетировании приложений:** <https://yunohost.org/packaging_apps>
