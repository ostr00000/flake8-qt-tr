
install_pre_commit:
	env python -m pip install --user pre-commit

run_pre_commit:
	pre-commit run --all-files
