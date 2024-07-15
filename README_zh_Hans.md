<!--
注意：此 README 由 <https://github.com/YunoHost/apps/tree/master/tools/readme_generator> 自动生成
请勿手动编辑。
-->

# YunoHost 上的 django-fritzconnection

[![集成程度](https://dash.yunohost.org/integration/django-fritzconnection.svg)](https://ci-apps.yunohost.org/ci/apps/django-fritzconnection/) ![工作状态](https://ci-apps.yunohost.org/ci/badges/django-fritzconnection.status.svg) ![维护状态](https://ci-apps.yunohost.org/ci/badges/django-fritzconnection.maintain.svg)

[![使用 YunoHost 安装 django-fritzconnection](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django-fritzconnection)

*[阅读此 README 的其它语言版本。](./ALL_README.md)*

> *通过此软件包，您可以在 YunoHost 服务器上快速、简单地安装 django-fritzconnection。*  
> *如果您还没有 YunoHost，请参阅[指南](https://yunohost.org/install)了解如何安装它。*

## 概况

Web based FritzBox management using Python/Django and the great [fritzconnection](https://github.com/kbr/fritzconnection) library.

The basic idea is to block/unblock Internet access to a group of devices as easily as possible.


[![pytest](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/pytest.yml/badge.svg?branch=master)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/pytest.yml) [![YunoHost apps package linter](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/package_linter.yml/badge.svg)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/package_linter.yml) [![Coverage Status on codecov.io](https://codecov.io/gh/YunoHost-Apps/django-fritzconnection_ynh/branch/master/graph/badge.svg)](https://codecov.io/gh/YunoHost-Apps/django-fritzconnection_ynh)

![django-fritzconnection @ PyPi](https://img.shields.io/pypi/v/django-fritzconnection?label=django-fritzconnection%20%40%20PyPi)
![Python Versions](https://img.shields.io/pypi/pyversions/django-fritzconnection)
![License GPL V3+](https://img.shields.io/pypi/l/django-fritzconnection)

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)


**分发版本：** 0.2.0~ynh3

## 截图

![django-fritzconnection 的截图](./doc/screenshots/screenshot.png)

## 文档与资源

- 上游应用代码库： <https://github.com/jedie/django-fritzconnection>
- YunoHost 商店： <https://apps.yunohost.org/app/django-fritzconnection>
- 报告 bug： <https://github.com/YunoHost-Apps/django-fritzconnection_ynh/issues>

## 开发者信息

请向 [`testing` 分支](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing) 发送拉取请求。

如要尝试 `testing` 分支，请这样操作：

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing --debug
或
sudo yunohost app upgrade django-fritzconnection -u https://github.com/YunoHost-Apps/django-fritzconnection_ynh/tree/testing --debug
```

**有关应用打包的更多信息：** <https://yunohost.org/packaging_apps>
