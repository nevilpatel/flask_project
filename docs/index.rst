.. Learning Flask documentation master file, created by
sphinx-quickstart on Sun Dec 16 10:18:04 2018.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive.

Learning Flask!
===============

What is Flask::

   -  A micro-framework with minimal features
   -  1200 lines of code
   -  Flexible framework and does not get in way
   -  Clean, readable and well documented
   -  Mostly whole app can be done in a single file.

Whats included in Flask::

   -  Jinja 2 - template engine for building html
   -  Werkzeug(german for tools) - provides http support and routing to map urls to python functions.
   -  MVC's View & Controller are covered with these two components
   -  Flask does not provide anything for model, which helps to choose any db like sqllite, mysql, nosql
      -  Here we are using SQLAlchemy
   -  Blueprint - allows program to be organized in a nice usable packages
   -  Development server + debugger
   -  Unit testing support

Jinja
-----

   -  in code use render_template('index.html',var1=value,var2=value...)
      -  value could be string, object, method etc
   -  in html add {{var1}} {{var2.x}} {{var3.func()}]} to populate from the code
      -  for var2.x Jinja looks for attribute x in var2 if not item x in var2 if not empty
      -  var3.func() can also take arguments
   -  '<a href = "{{ url_for('x.html')}}">Add URL</a>' - adds a link
   -  Template Inheritance
      -  {% extends 'base.html'%} extends from a base template
      -  blocks {% block blockname%}...{%endblock%} defined in parent can be replaced in children.
   -  More reference at `Jinja <http://jinja.pocoo.org/>`_

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
