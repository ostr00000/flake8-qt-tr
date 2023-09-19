create_venv:
	python -m venv env

install_pre_commit:
	. ./env/bin/activate && pip install pre-commit
	. ./env/bin/activate && pre-commit

run_pre_commit:
	pre-commit run --all-files

install_locally:
	. ./env/bin/activate && pip install .[test]
