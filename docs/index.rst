Welcome to libnmap's documentation!
===================================

About libnmap
-------------

libnmap is a python toolkit for manipulating nmap. It currently offers the following modules:

- parse: enables you to parse nmap reports or scan results (only XML so far) from a file, a string,...
- report: enables you to manipulate a parsed scan result and de/serialize scan results in a json format
- diff: enables you to see what changed between two scans
- objects: contains basic nmap objects like NmapHost and NmapService. It is to note that each object can be "diff()ed" with another similar object.

  - report: contains NmapReport class definition
  - host: contains NmapHost class definition
  - service: contains NmapService class definition
  - os: contains NmapOSFingerprint class definition and some other classes like NmapOSMatch, NmapOSClass,...
  - cpe: contains CPE class defdinition


libnmap's modules
-----------------

The full `source code <https://github.com/natlas/python-nmap-lib>`_ is available on GitHub. Please, do not hesitate to fork it and issue pull requests.

The different modules are documented below:

.. toctree::
   :maxdepth: 2
   :glob:

   parser
   objects
   objects/*
   diff

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
