# Implicationtracker

This tool does calculate inconsistencies and incompletenesses of a hierarchy of notions. It reads in a `.im`, which includes a list of implications.
+ implies `=>`
+ is implied by `<=`
+ is equivalent to `<=>`
+ does not imply `=|=>`
+ is not implied by `<=|=`

Based on this input it generates the complete adjacent matrix. Therefore is applies the transitivity of `=>` and the antitransitivity of `=|=>`. 

**Optionally:**
Additional it includes an LaTex export, s.t. it outputs longtables for `pages` of notions. 

## Usage / Installation

This repo is tested with python 3.8.5.

Just install (optional in a virtual environment):
```
pip install graphviz numpy
```

To run the program call
```
python main.py example.im
```



## `.im` format parser

The `.im` format supports comments with a leading `#` per line.

To enforce the ordering of the notion you can introduce notions with the `:` character.

Example

```
# Notions
:a
:b
:c

# Implications
a => b
b => c
```


## Testsets

## Licence
Copyright (c) 2020 - 2021 Maximilian Noppel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
