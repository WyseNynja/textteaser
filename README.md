TextTeaser
=============

TextTeaser is an automatic summarization algorithm.

This is now the official version of TextTeaser. Future developments of
TextTeaser will be in this repository.

The original Scala TextTeaser can still be accessed [here](https://github.com/MojoJolo/textteaser).


### Installation

    which virtualenv || sudo pip install virtualenv
    virtualenv --setuptools ~/.textteaser
    ~/.textteaser/bin/pip install -U pip setuptools
    ~/.textteaser/bin/pip install -U git+https://github.com/WyseNynja/textteaser.git#egg=textteaser
    mkdir -p ~/bin
    ln -sfv ~/.textteaser/bin/textteaser-cli ~/bin/
    ln -sfv ~/.textteaser/bin/textteaser-loop ~/bin/


### Upgrade

    ~/.textteaser/bin/pip install -U pip setuptools
    ~/.textteaser/bin/pip install -U git+https://github.com/WyseNynja/textteaser.git#egg=textteaser


### How to Use

To summarize a single document:

    ~/bin/textteaser-cli

To keep summarizing in a loop:

    ~/bin/textteaser-loop


### How to test

    python test.py


### Commercial Support

Commercial support for TextTeaser or custom summarizers can be provided by [DataTeaser](http://www.datateaser.com/?textteaser).
