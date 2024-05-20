#!/bin/bash

#=================================================
# COMMON VARIABLES
#=================================================

log_path=/var/log/$app
log_file="${log_path}/${app}.log"


#=================================================
# PERSONAL HELPERS
#=================================================

_venv_install() {
    ynh_exec_as "$app" python3 -m venv --upgrade "$install_dir/venv"
    venvpy="$install_dir/venv/bin/python3"

    ynh_exec_as "$app" "$venvpy" -m pip install --upgrade --no-cache-dir pip

    ynh_exec_as "$app" "$venvpy" -m pip install setuptools wheel pyyaml
}

_build_app() {
    ynh_exec_as "$app" "$venvpy" -m ensurepip
    ynh_exec_as "$app" "$venvpy" -m pip install --upgrade wheel pip setuptools
    ynh_exec_as "$app" "$venvpy" -m pip install --no-deps -r "$install_dir/app/requirements.txt"
}

#=================================================
# EXPERIMENTAL HELPERS
#=================================================

#=================================================
# FUTURE OFFICIAL HELPERS
#=================================================
