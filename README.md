# NI Engineering Workshops Read the Docs

This folder is ready to copy into the root of the existing Git repository.

## Publish

1. Copy `.readthedocs.yaml`, `requirements.txt`, and `source/` into the repository root.
2. Commit and push the files.
3. In Read the Docs, trigger a new build for the project.
4. The student manual will be available from the site navigation as `Level 1 Student Manual`.

## Preview locally

```bash
python -m pip install -r requirements.txt
sphinx-build -b html source source/_build/html
```

Open `source/_build/html/index.html` in a browser.
