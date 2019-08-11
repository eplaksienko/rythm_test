# rythm_test user manual

# Prepare environment

 - download and install [Python] (https://www.python.org/downloads/) version 3.5
 - setup virtual invironment, activate it and install pytest in virtual envoronment, use cmd for example for it in windows

 ```sh
 $ cd [project directory]
 $ python -m venv .venv
 $ .venv\Scripts\activate.bat
 $ pip install pip install vendor\pytest-5.0.1-py3-none-any.whl
 ```

# Execute the project

 - Execute actual project

 ```sh
 $ python main.py
 ```

 - Execute unit tests

 ```sh
  $ pytest tests\unit
  ```

  That's it folks