#!/bin/bash

#=================================================
# COMMON VARIABLES AND CUSTOM HELPERS
#=================================================

log_path=/var/log/$app
log_file="${log_path}/${app}.log"

_venv_install() {
    ynh_exec_as_app python3 -m venv --upgrade "$install_dir/venv"
    venvpy="$install_dir/venv/bin/python3"

    ynh_exec_as_app "$venvpy" -m pip install --upgrade --no-cache-dir pip

    ynh_exec_as_app "$venvpy" -m pip install setuptools wheel pyyaml
}

_build_app() {
    ynh_exec_as_app "$venvpy" -m ensurepip
    ynh_exec_as_app "$venvpy" -m pip install --upgrade wheel pip setuptools
    ynh_exec_as_app "$venvpy" -m pip install --no-deps -r "$install_dir/app/requirements.txt"
}
