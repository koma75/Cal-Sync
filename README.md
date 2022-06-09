Cal Sync
========================================================================

Outlook to Google Calendar sync CLI tool

ADD MY CLI DETAIL DESCRIPTION HERE

Installation
------------------------------------------------------------------------

~~~shell
> pip install cal_sync
~~~

Usage
------------------------------------------------------------------------


Command Line tool description

~~~shell
> calsync --option1 --argopt1 arg -v
~~~

* -o, --option1
    * description
* -a, --argopt1 ARG
    * description
* -c, --config CFG
    * CFG: Path to Configuration File (default: cal_sync.yml)
* -v, --verbose
    * verbosity

### Configuration file

YAML based configuration file (default file name: cal_sync.yaml)
is used to store default settings for the tool.
The command line options will take precedence over the configuration parameters.

following shows the default settings of the configuration

~~~yaml
option1: option1param
option2: option2param
optionArray:
  - item1
  - item2
optionDict:
  key1: item1
  key2: item2
  key3: item3
~~~

Known Issues
------------------------------------------------------------------------

Need to be implemented.

Development
------------------------------------------------------------------------

### Building an Executable

Install pyinstaller and package the project.
May want to use venv when executing the pyinstaller.

First, enter venv and install the local package and pyinstaller

~~~shell
>. .venv/Scripts/activate
(.venv) D:\path\to\proj\Cal Sync>pip install .
Processing d:\path\to\proj\Cal Sync
~snip~
Installing collected packages: cal_sync
    Running setup.py install for cal_sync ... done
Successfully installed cal_sync-0.1.0

(.venv) D:\path\to\proj\Cal Sync>pip install pyinstaller
~snip~
Successfully installed pyinstaller-3.6
~~~

Use pyinstaller to build the exe file.

~~~shell
(.venv) D:\path\to\proj\Cal Sync>pyinstaller cal_sync\cli.py --onefile --name calsync
~snip~
13691 INFO: Building EXE from EXE-00.toc completed successfully.
~~~

Executable should be ready in dist/calsync.exe

### Versioning

The project will follow the [semver2.0](http://semver.org/) versioning scheme.  
With initial development phase starting at 0.1.0 and increasing
minor/patch versions until we deploy the tool to production
(and reach 1.0.0).
The interface relevant to versioning is whatever defined in this
document's "Usage" section (includes all (sub)commands, their cli arguments,
and the format of the configuration file "cal_sync.yaml").

Version History
------------------------------------------------------------------------

Date        | Version   | Changes
:--         | --:       | :--
2022.06.09  | 0.1.0     | First Release