# command
## install requirement.txt
```shell
cd root/path/of/project
pip freeze > requirements.txt
```

## active venv
```shell
cd root/path/of/project
source ./.venv/bin/activate
```

# python-basic
1. helloworld and string basic usage.


# 
1. install jupyter globally.
`pip3 install jupyter``

2. install vscode jupyter extension

3. create a prject.

4. create virtual env
cd /path/to/project/root
`python -m venv give_it_a_name`

5. activate it
`source give_it_a_name/bin/activate`

6. install ipykernel within the virtual env
`pip3 install ipykernel`

7. create a kernel for this project.
`python3 -m ipykernel install --user --name=myproject_kernel`

8. create jupyter notebook
command for vscode `Create: New Jupyter Notebook`

9. select kernel for this notebook
command for vscode `Notebook: Select Notebook Kernel` -> Jupyter Kernel... -> myproject_kernel

10. install package for this kernel
in notebook: `!pip install pandas`

11. 


