import subprocess
import tomllib
from pathlib import Path
from tempfile import mkdtemp

from cookiecutter.main import cookiecutter
from pytest import fixture

tempdir = mkdtemp()

TEMPLATE_DIRECTORY = str(Path(__file__).parent.parent / "templates" / "uv")


@fixture(scope="module")
def template_url():
    return cookiecutter(
        template=TEMPLATE_DIRECTORY,
        output_dir=tempdir,
        no_input=True,
        extra_context={
            "project_name": "UV Foo Name",
            "description": "blah",
        },
    )


def test_project_has_been_generated(template_url):
    template_root = Path(template_url)

    assert template_root.name == "uv-foo-name"

    assert template_root.exists()
    assert (template_root / ".gitignore").exists()
    assert not (template_root / "requirements.yml").exists()
    assert (template_root / "scripts" / "executable.py").exists()


def test_project_contain_uv_structured_pyproejct_toml(template_url):
    pyproject_path = Path(template_url) / "pyproject.toml"

    assert pyproject_path.exists()

    pyproject = tomllib.loads(pyproject_path.read_text())
    assert pyproject["project"]["name"] == "uv-foo-name"
    assert pyproject["project"]["requires-python"] == ">= 3.12"
    assert pyproject["project"]["version"] == "0.0.0"
    assert pyproject["project"]["dependencies"] == [
        "loguru",
        "click",
    ]
    assert pyproject["tool"]["ruff"]["line-length"] == 88
    assert pyproject["tool"]["ruff"]["lint"]["select"] == [
        "I", "E4", "E7", "E9", "F", "Q",
    ]  # fmt: skip

    assert pyproject["dependency-groups"]["dev"] == [
        "pre-commit",
        "ruff",
        "pytest",
        "pytest-cov",
        "mypy",
    ]


def test_module_package_is_python_compliant(template_url):
    template_root = Path(template_url)

    test_main_py = template_root / "tests" / "test_main.py"

    assert test_main_py.exists()

    assert test_main_py.read_text().startswith(
        "from uv_foo_name.main import hello_world"
    )


@fixture
def manage_uv_installation_with_pip():
    check_uv_installation = subprocess.run(["uv", "--help"], shell=True)
    is_uv_not_installed = check_uv_installation.returncode != 0

    if is_uv_not_installed:
        install_uv = subprocess.run(
            ["pip", "install", "uv"], capture_output=True
        )
        install_uv.check_returncode()
    yield
    if is_uv_not_installed:
        uninstall_uv = subprocess.run(
            ["pip", "uninstall", "uv", "-y"], capture_output=True
        )
        uninstall_uv.check_returncode()


@fixture
def sync_uv_environment(manage_uv_installation_with_pip, template_url):
    p = subprocess.run(
        ["uv", "sync"], cwd=template_url, text=True, capture_output=True
    )
    p.check_returncode()
    assert (Path(template_url) / ".venv").exists()
    yield


def test_project_unit_tests__run_corretly(
    sync_uv_environment, template_url
):
    run_tests = subprocess.run(
        [
            "uv",
            "run",
            "pytest",
            "--cov",
            "uv_foo_name",
            "--cov-fail-under",
            "100",
            "tests",
        ],
        cwd=template_url,
    )
    run_tests.check_returncode()


def test_project_executable_script__runs_correctly(
    sync_uv_environment, template_url
):
    run_executable = subprocess.run(
        ["uv", "run", "scripts/executable.py"],
        cwd=template_url,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    run_executable.check_returncode()
    assert "This is the working location" in run_executable.stdout
    assert "Hello world!" in run_executable.stdout
