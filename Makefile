create_venv:
	python -m venv env

install_pre_commit:
	. ./env/bin/activate && pip install pre-commit
	. ./env/bin/activate && pre-commit

run_pre_commit:
	pre-commit run --all-files

install_locally:
	. ./env/bin/activate && pip install .[all]

prepare_build:
	. ./env/bin/activate && pip install --upgrade pip build twine

build_and_upload:
	rm -rf ./dist
	. ./env/bin/activate && python -m build
	. ./env/bin/activate && python -m twine upload dist/*

