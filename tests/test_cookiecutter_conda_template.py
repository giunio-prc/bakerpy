from pathlib import Path
from tempfile import mkdtemp

from cookiecutter.main import cookiecutter
from pytest import fixture

tempdir = mkdtemp()

TEMPLATE_DIRECTORY = str(
    Path(__file__).parent.parent / "templates" / "conda"
)


@fixture(scope="module")
def template_url():
    return cookiecutter(
        template=TEMPLATE_DIRECTORY,
        output_dir=tempdir,
        no_input=True,
        extra_context={
            "project_name": "Foo Name",
            "description": "blah",
        },
    )


def test_project_has_been_generated(template_url):
    template_root = Path(template_url)

    assert template_root.name == "foo-name"

    assert template_root.exists()
    assert (template_root / ".gitignore").exists()
    assert (template_root / "pyproject.toml").exists()
    assert (template_root / "requirements.yml").exists()
    assert (template_root / "scripts" / "executable.py").exists()


def test_module_package_is_python_compliant(template_url):
    template_root = Path(template_url)

    test_main_py = template_root / "tests" / "test_main.py"

    assert test_main_py.exists()

    assert test_main_py.read_text().startswith(
        "from foo_name.main import hello_world"
    )
