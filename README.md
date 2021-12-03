## Playing with Soundex algorithm

install and run with 
```
python3 -mvenv env
./env/bin/pip install -r requirements.txt
./env/bin/python -m unittest discover -s tests
```
for coverage use
```
./env/bin/coverage run -m unittest discover  -s tests
./env/bin/coverage report 
# or 
./env/bin/coverage html
```

quality
```
./env/bin/black src # format
./env/bin/mypy src  # check type
./env/bin/pylama -v src  -l "pycodestyle,pydocstyle,pyflakes,mccabe,radon" # audit code
./env/bin/bandit -r src # security issues
```


[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/rsilve/soundex-python.git])



