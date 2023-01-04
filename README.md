# 17-313 Course Website
## Quick Start

To run the built-in development server:

1. Create and activate a Python virtual environment

2. Install requirements
``` sh
pip install -r requirements.txt
```

3. Start local development server
```sh
mkdocs serve
```

You can then find the website running on [http://localhost:8000/](http://localhost:8000/)

For detailed installation instructions, configuration options, and a demo, visit
[squidfunk.github.io/mkdocs-material][Material for MkDocs]

[Material for MkDocs]: https://squidfunk.github.io/mkdocs-material/

## Pre-Semester Setup
1. Run the following to build the static site:
```sh
mkdocs build
```

2. Rename the static `site` folder to its semester-name (i.e. `F22`). Delete the `_old` folder within this and move the the folder into the `docs/_old` directory

3. Add a link to the old semester in `docs/index.md`. Test that the old site is still accessible

4. Within the `docs/_data` directory, set up information for course links, new staff members, and the semester's schedule. A `generate_dates.py` script is provided to auto-populate the `schedule.yaml` file with the expected format - this can be replaced with a csv parsing script later on

5. Replace the Class Calendar iframe within `docs/index.md`

6. Toggle which sites can be navigated to in the `mkdocs.yml` file under the `nav` section
