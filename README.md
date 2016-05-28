TextTeaser
=============

TextTeaser is an automatic summarization algorithm.

This is now the official version of TextTeaser. Future developments of
TextTeaser will be in this repository.

The original Scala TextTeaser can still be accessed [here](https://github.com/MojoJolo/textteaser).


### Installation

    virtualenv --setuptools ~/.textteaser
    . ~/.textteaser/bin/activate
    pip install --upgrade pip setuptools
    pip install git+https://github.com/WyseNynja/textteaser.git#egg=textteaser
    ln -sfv ~/.textteaser/bin/textteaser-cli ~/bin/
    ln -sfv ~/.textteaser/bin/textteaser-loop ~/bin/


### How to Use

To summarize a single document:

    textteaser-cli

To keep summarizing in a loop:

    textteaser-loop


### How to test

    python test.py


### Commercial Support

Commercial support for TextTeaser or custom summarizers can be provided by [DataTeaser](http://www.datateaser.com/?textteaser).
