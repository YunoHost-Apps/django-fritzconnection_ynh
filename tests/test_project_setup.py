import difflib
import json
import os
import shutil
import subprocess
from pathlib import Path

import tomli
from bx_django_utils.filename import clean_filename
from bx_py_utils.path import assert_is_dir, assert_is_file

import djfritz


PACKAGE_ROOT = Path(__file__).parent.parent


def assert_is_ynh_version(version: str, package_version: str):
    assert '~ynh' in version
    assert version[0].isdigit()
    assert version.startswith(package_version)
    assert version[-1].isdigit()


def test_version():
    package_version = djfritz.__version__
    assert package_version[0].isdigit()
    assert '~ynh' not in package_version

    pyproject_toml_path = Path(PACKAGE_ROOT, 'pyproject.toml')
    assert_is_file(pyproject_toml_path)
    pyproject_toml = tomli.loads(pyproject_toml_path.read_text(encoding='UTF-8'))
    assert_is_ynh_version(
        version=pyproject_toml['tool']['poetry']['version'], package_version=package_version
    )

    manifest_json_path = Path(PACKAGE_ROOT, 'manifest.json')
    assert_is_file(manifest_json_path)
    manifest = json.loads(manifest_json_path.read_text(encoding='utf-8'))
    assert_is_ynh_version(version=manifest['version'], package_version=package_version)


def poetry_check_output(*args):
    poerty_bin = shutil.which('poetry')

    output = subprocess.check_output(
        (poerty_bin,) + args,
        text=True,
        env=os.environ,
        stderr=subprocess.STDOUT,
        cwd=str(PACKAGE_ROOT),
    )
    print(output)
    return output


def test_poetry_check():
    output = poetry_check_output('check')
    assert output == 'All set!\n'


def test_requirements_txt():
    requirements_txt = PACKAGE_ROOT / 'conf' / 'requirements.txt'
    assert_is_file(requirements_txt)

    output = poetry_check_output('export', '-f', 'requirements.txt')
    assert 'Warning' not in output

    current_content = requirements_txt.read_text()

    diff = '\n'.join(
        difflib.unified_diff(
            current_content.splitlines(),
            output.splitlines(),
            fromfile=str(requirements_txt),
            tofile='FRESH EXPORT',
        )
    )
    print(diff)
    assert diff == '', f'{requirements_txt} is not up-to-date! (Hint: call: "make update")'


def test_screenshot_filenames():
    """
    https://forum.yunohost.org/t/yunohost-bot-cant-handle-spaces-in-screenshots/19483
    """
    screenshot_path = PACKAGE_ROOT / 'doc' / 'screenshots'
    assert_is_dir(screenshot_path)
    renamed = []
    for file_path in screenshot_path.iterdir():
        file_name = file_path.name
        cleaned_name = clean_filename(file_name)
        if cleaned_name != file_name:
            new_path = file_path.with_name(cleaned_name)
            file_path.rename(new_path)
            renamed.append(f'{file_name!r} renamed to {cleaned_name!r}')
    assert not renamed, f'Bad screenshots file names found: {", ".join(renamed)}'
