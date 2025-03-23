<!--
注意：此 README 由 <https://github.com/YunoHost/apps/tree/master/tools/readme_generator> 自动生成
请勿手动编辑。
-->

# YunoHost 上的 django-fritzconnection

[![集成程度](https://apps.yunohost.org/badge/integration/django-fritzconnection)](https://ci-apps.yunohost.org/ci/apps/django-fritzconnection/)
![工作状态](https://apps.yunohost.org/badge/state/django-fritzconnection)
![维护状态](https://apps.yunohost.org/badge/maintained/django-fritzconnection)

[![使用 YunoHost 安装 django-fritzconnection](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django-fritzconnection)

*[阅读此 README 的其它语言版本。](./ALL_README.md)*

> *通过此软件包，您可以在 YunoHost 服务器上快速、简单地安装 django-fritzconnection。*  
> *如果您还没有 YunoHost，请参阅[指南](https://yunohost.org/install)了解如何安装它。*

## 概况

[![tests](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/jedie/djfritz_ynh/branch/main/graph/badge.svg)](https://app.codecov.io/github/jedie/djfritz_ynh)
[![djfritz_ynh @ PyPi](https://img.shields.io/pypi/v/djfritz_ynh?label=djfritz_ynh%20%40%20PyPi)](https://pypi.org/project/djfritz_ynh/)
[![Python Versions](https://img.shields.io/pypi/pyversions/djfritz_ynh)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/blob/main/pyproject.toml)
[![License GPL-3.0-or-later](https://img.shields.io/pypi/l/djfritz_ynh)](https://github.com/YunoHost-Apps/django-fritzconnection_ynh/blob/main/LICENSE)

Web based FritzBox management using Python/Django and the great [fritzconnection](https://github.com/kbr/fritzconnection) library.

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)


**分发版本：** 0.4.0~ynh2

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
