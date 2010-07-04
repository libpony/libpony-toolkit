libpony Toolkit
===============

What is libpony?
----------------

libpony is a project aiming at providing an alternative aspect of
documentation for the django community. If you know the site listapart and
the django advent project, think about a combination of these two. Now add
translations and localizations into the mix and you know what kind of content
libpony is all about.

libpony also lives from your contribution. All content lives inside a git
repository on github which you can fork make pull requests when you want your
article to be part of the library. For details regarding this process please
stay tuned. The basic stuff is still work in progress :-) There is just one
thing for certain: The license.

Authors submitting work to this project by sending one of the editors a
pull-request or a patch agree that all their work is placed under a Creative
Commons (Share alike, non-commercial) license. Every change on the files is
documented thanks to git so it should also always be clear who contributed
what :-)

What is this toolkit?
---------------------

This toolkit project is effectively the technological heart of libpony. It's
first of all a set of tools to help authors create articles and preview them
in the same format as they would appear on the website.

And since DRY is nice the templates and compilation code provided here, is
also used on libpony.org itself.

What can I do with it?
----------------------

For now you can do two things with libponytk:

1. Create a new article with `libponytk create_article ARTICLES_FOLDER
   SLUG LANGCODE`

2. Compile an article in order to get a preview with `libponytk build_article
   ARTICLES_FOLDER/SLUG`

