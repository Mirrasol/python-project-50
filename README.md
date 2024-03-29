### Hexlet tests and linter status:
[![Actions Status](https://github.com/Mirrasol/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Mirrasol/python-project-50/actions)
[![Python CI](https://github.com/Mirrasol/python-project-50/actions/workflows/my_pyci.yml/badge.svg)](https://github.com/Mirrasol/python-project-50/actions/workflows/my_pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/b221022656c019208e10/maintainability)](https://codeclimate.com/github/Mirrasol/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b221022656c019208e10/test_coverage)](https://codeclimate.com/github/Mirrasol/python-project-50/test_coverage)


A concole ulitily that compares two files and shows the difference, with an option to display in a preferred format.


## 1) Installation

`git clone git@github.com:Mirrasol/python-project-50.git` - download the package from GitHub

`make package-install` - install using pip from your console


## 2) General usage

   To generate the difference use the command:

`gendiff [-h] [-f FORMAT] first_file second_file`

`[-h]` - requesting help message

`[-f]` - an optional choice of output format, from the selection of:
 
  - stylish (default)
  - plain
  - json


## 3) Demos

**Please refer to the demo examples below:**


1) Comparing JSON files:

[![asciicast](https://asciinema.org/a/QiGbheIp0tfHhivd745c7vMHM.svg)](https://asciinema.org/a/QiGbheIp0tfHhivd745c7vMHM)

2) Comparing YAML files:

[![asciicast](https://asciinema.org/a/rumI0mK5zMjXi3M2mXXCqFMeY.svg)](https://asciinema.org/a/rumI0mK5zMjXi3M2mXXCqFMeY)

3) Comparing 'tree' structures:

[![asciicast](https://asciinema.org/a/QBwgGr1qbLOrn3nIVQyy30IQy.svg)](https://asciinema.org/a/QBwgGr1qbLOrn3nIVQyy30IQy)

4) Choosing the 'plain' format option:

[![asciicast](https://asciinema.org/a/3WTC2QN04w5yvC3beATyzMzAx.svg)](https://asciinema.org/a/3WTC2QN04w5yvC3beATyzMzAx)

5) Choosing the 'json' format option:

[![asciicast](https://asciinema.org/a/uJJlvnU5aSjuYOLUkzgweH6fL.svg)](https://asciinema.org/a/uJJlvnU5aSjuYOLUkzgweH6fL)
