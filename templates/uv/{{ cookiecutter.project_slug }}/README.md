# {{ cookiecutter.project_name }}

Brief description of the project, what it does, and any important notes.

## Development environment

Before using this template,
ensure you have:

- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

correctly installed on your machine.

You can clone the project to your local machine and start developing at your convenience.
```bash
git clone https://github.com/{{cookiecutter.project_slug}}.git
```

Once the project is cloned, go to the folder `{{cookiecutter.project_slug}}` and create the environment with `uv` by running
```bash
uv sync
```
The command will create a `.venv` that stores the environment to run the project.

You can run a command within the virtual environment by prepending `uv run` to the command.
Alternatively, you can activate the environment and then run the command directly.

If you are on Linux/Mac OS, you can activate the environment with:
```bash
source .venv/bin/activate
```
If you are on a Windows machine, run instead:
```cmd
.venv\Scripts\activate
```


The development environment comes with pre-commit hooks installed using the [pre-commit](https://pre-commit.com/) package.

Pre-commit hooks are commands executed right before committing, such as unit tests, formatting, type checks, etc.
Before using them, make sure your project is tracked by git.

To use them, install the hooks by running:
```bash
uv run pre-commit install
```

You can then run the hooks from the command line as:
```bash
uv run pre-commit run
```
or

Each time you commit, hooks will automatically run.
If any of the hooks fail, the commit won't be added.
However, in exceptional cases, you can bypass the pre-commit hooks
with the option `--no-verify` in the commit command as follows:

```bash
git commit --no-verify -m "commit message"
```
