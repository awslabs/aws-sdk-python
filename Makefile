DOCS_PORT ?= 8000
PYTHON_VERSION := 3.12

.PHONY: docs docs-serve docs-clean docs-install venv

venv:
	uv venv --python $(PYTHON_VERSION)

docs-install: venv
	uv pip install -r requirements-docs.in
	uv pip install -e clients/*

docs-clean:
	rm -rf site docs/clients docs/SUMMARY.md

docs-generate:
	uv run python scripts/docs/generate_all_doc_stubs.py
	uv run python scripts/docs/generate_nav.py

docs: docs-generate
	uv run mkdocs build

docs-serve:
	@[ -d site ] || $(MAKE) docs
	uv run python -m http.server $(DOCS_PORT) --bind 127.0.0.1 --directory site
