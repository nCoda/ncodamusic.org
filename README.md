ncodamusic.org
==============

This is the website.


Setup
-----

You need GNU Make, NodeJS, CPython 2.7 or 3.4 before you do this.

1. Make sure you cloned all the submodules (`git submodule init` then `git submodule update`).
1. Make a virtualenv with a Python 3.4+ intepreter. Don't put the virtualenv in this directory or a subdirectory.
1. Activate the virtualenv and install the requirements file (`pip install -r requirements.txt`).
1. Install the NodeJS requirements (run `npm install` in the "amazeui" subdirectory).
1. Run `make amazeui` to generate the amazeUI files.
1. Run `make html` to generate the website.
1. Go!


How to Do Work
--------------

In grand *Pelican* tradition, we're using Make to do stuff. Here are the key commands:

- `make amazeui` to regenerate the CSS.
- `make html` to regenerate the rest of the site using CSS that's already built.
- `make serve` to start a webserver on http://localhost:8000.
- `make publish` to generate the site for publication (URLs point to ncodamusic.org, not localhost).


Knowing Where to Make a Change
------------------------------

- If you want to change something in the CSS, that goes in the amazeUI submodule. Check out the
  nCoda-specific README in that directory.
- If you want to change the HTML that's generated, that's somewhere in the "ncoda_theme" submodule.
- If you want to change the home page content, that's in `ncoda_theme/templates/homepage_content`.
- If you want to change other website content, that's in the `content` directory.


Good Ideas and Bad Ideas
------------------------

- Don't commit in the "output" repository unless (1) you're 100% sure, and (2) you use the
  `make publish` command. The website won't deploy automatically, and we can always go back thanks
  to git, but it's easier to avoid mistakes than fix them.
- ... ?
- Add helpful tips to this list when you think of them.
