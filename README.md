## Python Calculator

![HacktoberFest 2019](https://camo.githubusercontent.com/73b77ee452271049513e503ff3e8e8c172eaadab/68747470733a2f2f6861636b746f626572666573742e6469676974616c6f6365616e2e636f6d2f6173736574732f484631395f736f6369616c2d373434643937366632323765346166663638363634343361626365646538633635316233303965633963376339663734313066353934346638653132393962392e706e67)

![Only for Road to Hacktober participants](https://badgen.net/badge/Road%20to%20Hacktober/only/blue?icon=github)

### How to use

Check your python version with `python --version`.

If the version is `3.x` then simply do

```sh
python cli.py multiply 2 7 3
```

If the version is `2.7.x` then download Python 3 and use like this.

```sh
python3 cli.py multiply 2 7 3
```

The result of running the above commands should be

```sh
------
42
------
```

Note- You can enter as many numbers as you want. Try running `python3 cli.py average 2 7 3 11 89`.

### How to add new operations
1. Define a new method in `Calculator.py`.
1. Add the condition for calling new method in the `calculate` function of `cli.py`.

## How to lint and format code
1. I use autopep8 for this.
1. One important thing is instead of messing around with complicated virtualenv setup, I opted for `pipenv`.
1. Install `pipenv` globally `pip3 install pipenv`.
1. Enter a virtual env for this project using `pipenv shell`.
1. Install all the project dependencies with `pipenv install`.
1. Format code with `sh ./scripts/format.sh`.
