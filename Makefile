dev-tests:
	pipenv run python -m unittest

dev-format:
	pipenv run black openxdf
	pipenv run flake8 --ignore="E501,E266,W503" openxdf

package-dist:
	pipenv run python setup.py sdist bdist_wheel

upload-dist:
	pipenv run python -m twine upload dist/*

install-jupyter:
	jupyter kernelspec uninstall openxdf-env
	pipenv run python -m ipykernel install --user --name openxdf-env --display-name "OpenXDF Env"

run-jupyter:
	pipenv run jupyter notebook
