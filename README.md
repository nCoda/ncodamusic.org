ncodamusic.org
==============

This is the website.


Pour commmencer
---------------

You need GNU Make, NodeJS, CPython 3.4.

1. Make sure you cloned all the submodules (`git submodule init` then `git submodule update`).
1. Make a virtualenv. Don't put the virtualenv in this directory or a subdirectory.
1. Activate the virtualenv and install the requirements file (`pip install -r requirements.txt`).
1. Install the NodeJS requirements (run `npm install` in the "amazeui" subdirectory).
1. Go!


Pour travailler
---------------

In grand *Pelican* tradition, we're using Make to do stuff. Here are the key commands:

- `make amazeui` to regenerate the amazeUI files.
- `make html` to regenerate the whole site, using whatever amazeUI is already built.
- `make serve` to start a webserver on "localhost:8000".
- `make publish` to generate the site for publication (URLs point to ncodamusic.org, not localhost).


Bonnes idées, interdictions:
----------------------------

- Don't commit in the "output" repository unless (1) you're 100% sure, and (2) you use the
  `make publish` command. The website won't deploy automatically, and we can always go back thanks
  to git, but it's easier to avoid mistakes than fix them.
- ... ?
- Add helpful tips to this list when you think of them.
