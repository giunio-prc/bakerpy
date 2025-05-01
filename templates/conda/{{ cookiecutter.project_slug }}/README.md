# {{ cookiecutter.project_name }}

Brief description of the project, what it does, and any important notes.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/expert-tools-and-discovery/{{cookiecutter.project_slug}}.git
   ```

2. Installation instructions:
```bash
make install
```

## Development environement

Before using this template,
ensure you have:

- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [conda](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html)

correctly installed on your machine.

You can clone the project to your local machine and start developing at your ease.
```bash
git clone https://github.com/{{cookiecutter.project_slug}}.git
```

Provide the personal access token. You can create a personal access token [here](https://github.com/-/profile/personal_access_tokens)

Once the project is cloned go to the folder `{{cookiecutter.project_slug}}` and activate the environment with `conda` by running
```bash
conda env create -f requirements.txt
```

Then activate the environment with the command:
```bash
conda activate {{cookiecutter.project_slug}}
```

The development environement comes with pre commit hooks installed with the [pre-commit](https://pre-commit.com/) package.

Pre-commit hooks are commands executed right before commiting such as unit tests, formatter, type check etc...

To use you it, install the hooks by running:
```bash
pre-commit install
```

You can then run the hooks from the command line as:
```bash
pre-commit run
```

Each time you commit hooks will automatically run.
If any of hooks fail, the commit won't be added.
However, only exceptionally, you can bybass the pre-commit hooks
with the option `--no-verify` to the commit command as:

```bash
git commit --no-verify -m "commit message"
```
