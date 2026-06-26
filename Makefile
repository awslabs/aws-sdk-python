DOCS_PORT ?= 8000
PYTHON_VERSION := 3.12

.PHONY: docs docs-serve docs-clean docs-install docs-lock venv

venv:
	uv venv --python $(PYTHON_VERSION)

docs-lock: venv
	uv pip compile requirements-docs.in -o requirements-docs.txt

docs-install: venv
	uv pip install -r requirements-docs.txt
	uv pip install -e clients/*

docs-clean:
	rm -rf site docs/clients

docs-generate:
	uv run python scripts/docs/generate_all_doc_stubs.py
	uv run python scripts/docs/generate_nav.py

docs: docs-generate
	uv run zensical build

docs-serve:
	@[ -d site ] || $(MAKE) docs
	uv run python -m http.server $(DOCS_PORT) --bind 127.0.0.1 --directory site
