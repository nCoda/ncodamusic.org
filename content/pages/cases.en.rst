Use Cases
==========

:lang: en
:slug: cases
:date: 2016-09-23 11:27 
:modified: 2016-09-23 11:27
:category: propaganda 
:authors: Jeff Trevino 
:tags: use cases, evangelism 
:summary: step-by-step description of some putatively common uses cases 


========================================================
Sounds Great! But How Might Someone Actually Use nCoda?
========================================================

Here are some of the ways we imagine nCoda might be used to create and manage documents for music production and scholarship.

I. Make and tweak a new score.
------------------------------
#. LilyPond is an automated music typesetting engine with an elegant syntax for describing common practice western music notation.
#. You can type LilyPond syntax into the editor on the left side of the interface, and 
#. render that as music notation on the right side of the interface, after which 
#. you can click and drag notes and menus (or use keyboard shortcuts) to tweak the pitches and rhythms, and finally
#. output your notation as an .svg or .pdf file.

II. Make and tweak a new score by coding in Python.
---------------------------------------------------
#. Abjad is an API that allows you to model common practice western music notation, and many compositional operations on notation objects, by coding in the Python programming language.
#. You can type some Abjad Python code into the Abjad tab on the left side of the interface, and 
#. Call `show()` on an Abjad object, such as a staff or score, which
#. renders as music notation on the right side of the interface, after which 
#. you can click and drag notes and menus (or use keyboard shortcuts) to tweak the pitches and rhythms, and finally
#. output your notation as an .svg or .pdf file.

III. Collaborate on a new composition or edition of an existing work with a team.
---------------------------------------------------------------------------------
#. Create a new project and invite team members to join, who can
#. contribute LilyPond or Python code to the project (in the manner of I. and II.) -- imagine hundreds of people crowdsourcing an opera score by each entering a single measure -- while
#. nCoda automatically tracks and collates team member contributions and project versions with the Mercurial Version Control System, thus enabling you to return to any past state of your project, and to
#. socially engage a distributed team of contributors by commenting on multiple proposed versions of a musical section, uploading or linking a variety of inspiring media, or even describing music in words before it exists.
