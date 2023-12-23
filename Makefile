HOME=/home/docker
PROJECT_DIR=/home/docker/pytorch-project

# devcontainer------------------------------------------------------------
.PHONY: set-prompt
set-prompt:
	echo '. ${PROJECT_DIR}/src/scripts/add_gitinfo_to_prompt.sh' >> ~/.bashrc

.PHONY: set-vscode-settings
set-vscode-settings:
	@echo "*** Creating ${HOME}/.vscode"
	mkdir -p ${HOME}/.vscode
	@echo "*** Creating symlinks for vscode settings.json"
	ln -sf ${PROJECT_DIR}/.vscode/settings.json ${HOME}/.vscode/settings.json
	@echo "*** Creating symlinks for vscode launch.json"
	ln -sf ${PROJECT_DIR}/.vscode/launch.json ${HOME}/.vscode/launch.json


# installation------------------------------------------------------------
.PHONY: install-requirements
install-requirements:
	pip install -r ${PROJECT_DIR}/requirements.txt


# test--------------------------------------------------------------------
.PHONY: pytest
pytest:
	pytest -sv ./tests

.PHONY: cov
cov:
	pytest -sv --cov=src --cov-report=xml --cov-report=term ./tests