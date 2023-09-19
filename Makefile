
install_pre_commit:
	env python -m pip install --user pre-commit

run_pre_commit:
	pre-commit run --all-files

create_venv:
	python -m venv env

install_locally:
	. ./env/bin/activate && pip install .[test]
