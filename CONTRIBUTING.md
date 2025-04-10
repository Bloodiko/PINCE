# Code Structure
- [PINCE.py](./PINCE.py) - The main file, it contains everything from GUI logic to libpince communication. A chonky boi on a diet, see below for information about ongoing refactoring
- [PINCE.sh](./PINCE.sh) - Launch script
- [install.sh](./install.sh) - Installation script
- [compile_ts.sh](./compile_ts.sh) - Gathers translation information from various sources and compiles them into ts files
- [fix_ts.py](./fix_ts.py) - Fixes line information issue, used within [compile_ts.sh](./compile_ts.sh)
- [compile_gdb.sh](./compile_gdb.sh) - PINCE normally uses system GDB but in cases where system GDB is unavailable, this script is used to compile GDB locally
- [GUI](./GUI) - Contains Qt Designer forms and their respective codes along with utility functions and custom Qt classes
- [media](./media) - Contains media files such as logos and icons
- [tr](./tr) - Contains translation constants
- [docs](./docs) - Contains Sphinx documentation. The build files are automatically generated in the `gh-pages` branch.
- [i18n](./i18n) - Contains translation files. `ts` files are created with Qt Linguist and [compile_ts.sh](./compile_ts.sh), `qm` files are created within the last section of [install.sh](./install.sh)
- ### **[libpince](./libpince)**
  - [debugcore.py](./libpince/debugcore.py) - Everything related to communicating with GDB and debugging
  - [utils.py](./libpince/utils.py) - Contains generic utility functions such as parsing, file creation, process querying etc
  - [typedefs.py](./libpince/typedefs.py) - Contains all constants and variable definitions
  - [regexes.py](./libpince/regexes.py) - Contains regexes for parsing GDB output and other things
  - [injection](./libpince/injection) - An example for injecting .so files
  - ### **[gdb_python_scripts](./libpince/gdb_python_scripts)**
    - [gdbextensions.py](./libpince/gdb_python_scripts/gdbextensions.py) - Contains custom GDB commands
    - [gdbutils.py](./libpince/gdb_python_scripts/gdbutils.py) - Contains utility functions for GDB commands
    - [tests](./libpince/gdb_python_scripts/tests) - An example for .so extension, read more [here](https://github.com/korcankaraokcu/PINCE/wiki/Extending-PINCE-with-.so-files)

**About GUI file structure refactoring**: PINCE.py currently holds all of the GUI logic classes and this makes PINCE.py grow larger as the project progresses. To prevent this, all GUI logic will be carried to their respective folders and the GUI folder will follow this structure:
```
GUI/
|-- Settings/
|-- States/
|-- Utils/
|-- Widgets/
|   |-- Example/
│   |   |-- Form/
│   |   │   |-- ExampleWidget.ui (Designer UI file)
│   |   │   |-- ExampleWidget.py (Auto-generated from the UI file)
│   |   |-- Example.py (Form logic)
│   |   |-- CustomClass.py (Helper class)
```
A good example of the structure above can be seen in [ManageScanRegions](./GUI/Widgets/ManageScanRegions)

# Code Style
Formatting style is [Black](https://github.com/psf/black) defaults, except line length is 120. You can use Black without parameters since we already use `pyproject.toml` for this setting.

***You must format the files you changed using Black before you open a PR!*** Please do not format automatically generated files under GUI folder. Your changes will be overwritten by Qt Designer. More info at [UI Files](#ui-files)
- Max characters per line: 120
- Variable naming for libpince:
  - Classes: PascalCase
  - Class members: snake_case
  - Variables: snake_case
  - Functions: snake_case
  - Constants: SCREAMING_SNAKE_CASE
  - Modules: flatcase
  - Standalone scripts: snake_case
- Variable naming for Qt:
  - Classes: PascalCase
  - Class members:
    - non-Qt: snake_case
    - Qt: objectType + PascalCase
    For example: `keySequenceEdit_Hotkey` in [PINCE.py](./PINCE.py)
  - Variables: snake_case
  - Functions:
    - non-Qt: snake_case
    - Qt: objectName + snake_case
    Here's an example: `keySequenceEdit_Hotkey_key_sequence_changed` in [PINCE.py](./PINCE.py)
  - Constants: SCREAMING_SNAKE_CASE
  - Modules: PascalCase
  - Standalone scripts: snake_case

For convenience, I'm using auto-format tool of vscode. Any modern IDE will most likely have an auto-formatting tool.
Readability and being clear is the most important aspect, so if you decide to not follow the rules, make sure that your code still reads nice and plays well with others.
If you feel unsure to which naming convention you should use, try to check out similar patterns in the code or just ask away in the PINCE discord server!

The reason behind Qt class member naming convention is that when this project first started, supported python version didn't have type hints.
So, to have an idea about the type of the variable we are working with, I've come up with that naming idea. It's an old habit if anything.
It could maybe replaced with something else after a refactorization

About the max characters per line, I used to use PyCharm when I first started this project years ago. 120 characters is a limit brought by PyCharm, I've quit using PyCharm eventually but I think the limit makes the code look quite nice. Black suggests a limit of 88 characters, which is a bit short to be frank. So I think it's good to keep this old habit, especially considering that docstrings have also followed this rule for a long time now. This limit for docstrings however, is not strict at all. A few characters passing the limit is ok, sometimes going for a newline messes up the readability, trust your guts and decide for yourself

# Documentation
We use Google style documentation and type hints. A good example would be `get_breakpoints_in_range` function in [debugcore.py](./libpince/debugcore.py). Root folder of libpince has 100% documentation coverage so a pull request regarding libpince has to be documented. For other places, it's enough to document the parts you think that'd be confusing to read later on. You are not obliged to document everything in other places as we are also quite lax with it

We use Sphinx to automatically generate html files from the docs and napoleon extension to convert Google style docs to reStructuredText. To test locally, `cd` into the [docs](./docs) directory and execute `sh install_sphinx.sh`. This will install Sphinx and its extensions within the venv. After this, You can modify [source files](./docs/source) and then build html files with `sh build_html.sh` to test your changes. To create source files for multiple modules automatically, `sphinx-apidoc` can be used. For single modules, you can edit the source files manually (like I did with `guiutils`)

[build_docs.yml](.github/workflows/build_docs.yml) workflow is responsible for automatic html generation, it gets triggered automatically whenever there's a new release or manually whenever necessary. The workflow generates files within the `gh-pages` branch. It's an orphaned branch so it can be deleted without affecting the history

# UI Files
You need to have [Qt6 Designer](https://pkgs.org/search/?q=designer&on=files) installed. If there are no available packages for your distro, install [pyqt6-tools](https://pypi.org/project/pyqt6-tools/) instead  

Follow the steps below:
- Edit or create ui files with the designer and save them
- After saving ui files, run `sh ui_to_py.sh` within GUI folder to convert them into py files

The py files that contains the same name with the ui files are auto-generated, please edit the ui files with designer instead of messing with the py files

# Translation
You need to have [Qt6 Linguist](https://pkgs.org/search/?q=linguist&on=files) installed. If there are no available packages for your distro, install [pyqt6-tools](https://pypi.org/project/pyqt6-tools/) instead  

Follow the steps below:
- To create a new translation file, use [compile_ts.sh](./compile_ts.sh) with the locale as the parameter, such as `sh compile.sh ja_JP`. This will create a ts file with the locale you entered.
You can skip this step if you only want to edit already existing files
- Edit ts files in [/i18n/ts](./i18n/ts) with the linguist and then save them. After saving the files, run the [compile_ts.sh](./compile_ts.sh) script.
This script fixes inconsistencies between Qt6 Linguist and pylupdate6, also removes line information so the git history stays cleaner
- To test your translations, use [install.sh](./install.sh). The last part of the installation script also compiles ts files to qm files so PINCE can process them.
When asked to recompile libscanmem, enter no

Make sure that you read the comments in [tr.py](./tr/tr.py). Some of the translations have caveats that might interest you

About the untranslated parts of the code, such as context menus of libpince reference widget. You'll see that some of the code serves as a placeholder that'll be
removed or replaced in the future. These are not marked as translatable as translating them would be a waste of time

**ATTENTION:** Make sure you read this part even if you aren't a translator:  
If you create or delete any Qt related string (for example, ui forms or translation constants in [tr.py](./tr/tr.py)), you must run [compile_ts.sh](./compile_ts.sh) so it updates the translations.
Not every string has to be translatable, if it's only printed on console, it can stay as is, in English. If it's shown to the user within a form, it should be translatable

# Logo
All logo requests should be posted in `/media/logo/your_username`. Instead of opening a new issue, pull request your logo files to that folder.
Your PR must include at least one png file named pince_small, pince_medium or pince_big, according to its size. So, a minimal PR will look like this:

`/media/logo/your_username/pince_big.png`

pince_big is interchangeable with pince_medium and pince_small
A full PR will look like this:
```
/media/logo/your_username/pince_big.png
/media/logo/your_username/pince_medium.png
/media/logo/your_username/pince_small.png
```

# Notes
Here are some notes that explains some of the caveats and hacks, they also include a timestamp. As we upgrade the libraries and the methods we are working with,
some of these notes might become obsolete. You are free to test and provide solutions to these tricks

- 28/08/2018 - All QMessageBoxes that's called from outside of their classes(via parent() etc.) must use 'QApplication.focusWidget()' instead of 'self' in their first parameter.
Refer to issue #57 for more information

- 23/11/2018 - Don't use get_current_item or get_current_row within currentItemChanged or currentChanged signals.
Qt doesn't update selected rows on first currentChanged or currentItemChanged calls

- 22/05/2023 - For QTableWidget and QTableView, disabling wordWrap and using ScrollPerPixel as the horizontal scroll mode can help the user experience.
Consider doing these when creating a new QTableWidget or QTableView

- 15/02/2024 - Don't always trust the "Adjust Size" button of the Qt Designer, it might expand widgets much more than needed, especially for smaller widgets. Consider the use cases
and adjust manually. This also helps functions like `guiutils.center_to_parent` work properly

- 13/05/2024 - Monospace font and `utils.upper_hex` function greatly improve readability if the text area includes hex data, consider using those when creating new text areas. Memory Viewer is a good example for this

- 13/10/2024 - Using big integers as a `pyqtSignal` param will cause them to overflow and turn into different numbers because of the type mismatch between python and cpp. Use `object` instead of `int` as param in this case. An example for this case can be seen in [BookmarkWidget](./GUI/Widgets/Bookmark/Bookmark.py)

- 02/09/2018 - Seek methods of all file handles that read directly from the memory(/proc/pid/mem etc.) should be wrapped in a try/except block that catches both
OSError and ValueError exceptions. For instance:
```python
    try:
        self.memory.seek(start_addr)
    except (OSError, ValueError):
        break
```
OSError handles I/O related errors and ValueError handles the off_t limit error that prints "cannot fit 'int' into an offset-sized integer"

- 12/09/2018 - All namedtuples must have the same field name with their variable names. This makes the namedtuple transferable via pickle. For instance:
```python
    tuple_examine_expression = collections.namedtuple("tuple_examine_expression", "all address symbol")
```
- 06/10/2016 - HexView section of MemoryViewerWindow.ui: Changed listWidget_HexView_Address to tableWidget_HexView_Address in order to prevent possible future visual bugs.
Logically, it should stay as a listwidget considering its functionality. But it doesn't play nice with the other neighboring tablewidgets in different pyqt versions,
forcing me to use magic numbers for adjusting, which is a bit hackish

# Roadmap
So, after learning how to contribute, you are wondering where to start now. You can either search for `TODO` within the code or pick up any task from the roadmap below.
These tasks are ordered by importance but feel free to pick any of them. Further details can be discussed in the PINCE discord server
- Implement libpince engine
- Implement multi-line code injection, this will also help with previously dropped inject_with_advanced_injection
- Libpince support for Mono and Java (symbol recognition, calling functions, dissect obj tree etc.)
- Move GUI classes of PINCE.py to their own files
- Extend documentation to GUI parts. Libpince has 100% documentation coverage but GUI doesn't
- Use type hints(py 3.5) and variable annotations(py 3.6) when support drops for older systems
- Arrows for jump instructions based on disassembled output
- Flowcharts based on disassembled output
- Consider implementing a GUI for catchpoints. This is currently done via GDB Console
- Implement speedhack
- Implement unrandomizer
- Automatic function bypassing(make it return the desired value, hook specific parts etc.)
- Implement auto-ESP&aimbot
- Implement thread info widget
- Write at least one test for each function in libpince
- Refactorize memory write/read functions
- - ReferencedStringsWidgetForm refreshes the cache everytime the comboBox_ValueType changes, this creates serious performance issues if total results are more than 800k.
  Only update the visible rows to prevent this(check ```disassemble_check_viewport``` for an example)
- - Implement same system for the TrackBreakpointWidgetForm if necessary. Do performance tests
- - Consider using a class instead of primitive return types to store the raw bytes. This class should also include a method to display None type as red '??' text for Qt
- - Provide an option to cut BOM bytes when writing to memory with the types UTF-16 and UTF-32
- - Put a warning for users about replacement bytes for non UTF-8 types
- - Extend string types with LE and BE variants of UTF-16 and UTF-32
- - Change comboBox_ValueType string order to be ... String_UTF-8 String_Others if necessary
- - Implement a custom combobox class for comboBox_ValueType and create a context menu for String_Others, if it gets implemented
- Implement "Investigate Registers" button to gather information about the addresses registers point to
- Add the ability to track down registers and addresses in tracer(unsure)
- Implement CE's Ultimap-like feature for tracing data, dissect code data and raw instruction list.
Search for calls and store their hit counts to filter out the functions that haven't or have executed specific number of times.
Implement a flexible input field for the execution count. For instance, 2^x only searches for hit counts 2, 4, 8 and so on, 3x only searches for 3, 6, 9 etc.
([CE#358](https://github.com/cheat-engine/cheat-engine/issues/358))
- Extend search_referenced_strings with relative search
- Consider adding type guessing for the StackView
- Implement a psuedo-terminal for the inferior like edb does(idk if necessary, we don't usually target CLI games, up to debate)
- Try to optimize TrackBreakpoint and TrackWatchpoint return data structures further, adding an id field might simplify traversing of the tree, performance tests are required
- Implement extra MemoryViewerWindow tabs(not really critical right now, up to debate)
- ~~Consider removing the command file layer of IPC system for debugcore.send_command to speed up things~~
[Update-29/04/2018 : Delaying this until GDB/MI implements a native multiline command feature or improves ```interpreter-exec``` command to cover every single multiline command type(including ```define``` commands)]
- Implement developer mode in settings. Developer mode will include features like dissection of GUI elements on events such as mouse-over
- Add ability to include non-absolute calls for dissect code feature(i.e call rax). Should be considered after the first version release. Might be useful for multi-breakpoint related features
- Provide information about absolute addresses in disassemble screen
- All tables that hold large amount of data should only update the visible rows(check ```disassemble_check_viewport``` for an example)
