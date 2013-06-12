## Packaging And Testing

This is the first Python package that I put on PyPi and thus I'm still learning on how to do this best. This file serves me to remember how I released this package.

For general advice on how to structure Python modules,
refer to [the modules tutorial](http://docs.python.org/3/tutorial/modules.html).

#### Configuring the Properties of the Module

I created the file [setup.py](./setup.py) and entered the properties and meta-data of your module. A list of all possible classifiers can be found [here](https://pypi.python.org/pypi?%3Aaction=list_classifiers).

#### Installing a dev-version on you Local Computer

    # uninstall any previous version:
    pip3.3 uninstall bottlelog
    # compile a new source distribution package:
    python3.3 setup.py sdist
    # install that package:
    pip3.3 install dist/bottlelog-0.1.tar.gz

In my case (I'm using virtualenvwraper), the files are being installed to:

    ~/.virtualenvs/bottle-3.3/lib/python3.3/site-packages/bottlelog/ ...

#### Registering with PyPI

The Readme is written in Markdown but PyPi only understands reStructuredText for the modules long description. I use `pandoc` and its Python wrapper `pypandoc` to convert my Markdown to reST. Install them using:

    brew install pandoc
    pip install pypandoc

Now register or update the project on PyPi (as pypandoc is not yet Python3 ready, we need to use Python 2.7 to upload our package):

    python2.7 setup.py register

Uploading a new source distribution on PyPi works like this:

    python2.7 setup.py sdist upload

### Resources

* Check out the official guide [Distributing Python Modules](http://docs.python.org/3/distutils/index.html)
