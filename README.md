# 🧁 Bakerpy

![workflow](https://github.com/giunio-prc/bakerpy/actions/workflows/main.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Whether you're a fan of `conda`, experimenting with `uv`, or planning to standardize team setups — Bakerpy helps you bake consistent, ready-to-code Python projects.

---

## 🚀 Features

- 📦 **Package Manager Specific Templates**
  Start new projects with a structure aligned to your preferred tool (e.g., `conda`, `uv`, and more coming soon).

- 🧰 **Batteries-Included Scaffolds**
  Each template includes sensible defaults for packaging, tests, pre-commit hook etc...

- 🧪 **Lightweight, Flexible, Extendable**
  Add your own cookiecutter templates or contribute to existing ones.

---

## 📦 Available Templates

| Template | Description |
|----------|-------------|
| `conda`  | Python project scaffold using `conda` for environment and dependency management. |
| `uv`     | Minimal, fast Python setup using [`uv`](https://github.com/astral-sh/uv) as a package manager. |

---

## 🧁 How to Use

Make sure you have [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/installation.html) installed:

You can also use [`cruft`](https://cruft.github.io/cruft/#installation)


**Create a New Project**:

   If you use *Cookiecutter* to generate a new project from this template. Run the following command:

   ```bash
   cookiecutter https://github.com/giunio-prc/bakerpy.git
   ```
   You can then use the interactive command line menu to generate your template.

   If you use *Cruft*, the command is:

   ```bash
   cruft create https://bakerpy.com/giunio-prc/bakerpy.git --directory templates/<template-name>
   ```
   At the time of writing, Cruft does not support nested tempaltes,
   so you have to specify the <template-name> in the command chosen for project creation (ex. `conda` or `uv`)

In both cases the project is created under a folder named as your project slug.
At the moment we have two templates:
- *Conda project*, that uses `conda` as package manager
- *UV project*, that uses `uv`

**Resulting project structure:**
The project will have the following structure
```
your-project-slug/
├── .gitignore
├── .pre-commit-config.yaml
├── README.md
├── requirements.yml
├── tests/
│   ├── __init__.py
├── your_package_name/
|   └── __init__.py
└── scripts/
    └── executable.py
```

## Live Demo for uv template
![](https://github.com/giunio-prc/bakerpy/blob/main/live-demo.gif)
