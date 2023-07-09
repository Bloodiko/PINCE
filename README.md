# PINCE
<!---
TODO: Include build status with the title when test coverage increases and Travis is maintained
[![Build Status](https://travis-ci.org/korcankaraokcu/PINCE.svg?branch=master)](https://travis-ci.org/korcankaraokcu/PINCE)
-->
PINCE is a front-end/reverse engineering tool for the GNU Project Debugger (GDB), focused on games. However, it can be used for any reverse-engineering related stuff. PINCE is an abbreviation for "PINCE is not Cheat Engine". PINCE is in development right now, read [Features](#features) part of the project to see what is done and [Roadmap](#current-roadmap) part to see what is currently planned. Also, please read [Wiki Page](https://github.com/korcankaraokcu/PINCE/wiki) of the project to understand how PINCE works.  

### [Feel free to join our discord server!](https://discord.gg/jVt3BzTSpz)  

*Disclaimer: Do not trust to any source other than [Trusted Sources](#trusted-sources) that claims to have the source code or package for PINCE and remember to report them **immediately***

*Disclaimer: **YOU** are responsible for your actions. PINCE does **NOT** take any responsibility for the damage caused by the users*

Pre-release screenshots:

![pince0](https://user-images.githubusercontent.com/5638719/219640001-b99f96a2-bffb-4b61-99a1-b187713897e2.png)
![pince1](https://user-images.githubusercontent.com/5638719/219640254-40152be1-8e97-4d26-a313-62a56b9fe1a5.png)
![pince2](https://user-images.githubusercontent.com/5638719/219706426-56c233f5-b047-4a8f-b090-ab439b98ef3a.png)
![pince3](https://user-images.githubusercontent.com/5638719/219640353-bb733c19-9ce7-4baf-81ce-4306c658fbe6.png)
![pince4](https://user-images.githubusercontent.com/5638719/219640370-a73c1796-8d2b-4d31-a63c-aa0b41f9f608.png)
![pince5](https://user-images.githubusercontent.com/5638719/219640384-62a384c8-cc32-45ef-b975-e310674302c2.png)
![pince6](https://user-images.githubusercontent.com/5638719/219640402-e03768b3-4e88-4c75-9d73-29dfbb69b3c0.png)
![pince7](https://user-images.githubusercontent.com/5638719/219640469-8b496c67-b074-4c9a-9890-9e52227cf75d.png)
![pince8](https://user-images.githubusercontent.com/5638719/219640488-61a8df17-405b-45ae-9b29-f9d214eb8571.png)
![pince9](https://user-images.githubusercontent.com/5638719/219640522-85cac1a9-e425-4b4f-abeb-a61104caa618.png)

# Features  
- **Memory searching:** PINCE uses a specialized fork of [libscanmem](https://github.com/brkzlr/scanmem-PINCE) to search the memory efficiently
- **Variable Inspection&Modification**
  * **CheatEngine-like value type support:** Currently supports all types of CE and scanmem along with extended strings(utf-8, utf-16, utf-32)
  * **Symbol Recognition:** See [here](https://github.com/korcankaraokcu/PINCE/wiki/About-GDB-Expressions)
  * **Automatic Variable Allocation:** See [here](https://github.com/korcankaraokcu/PINCE/wiki/About-GDB-Expressions)
  * **Dynamic Address Table:** Supports drag&drop, recursive copy&pasting&inserting and many more
  * **Smart casting:** PINCE lets you modify multiple different-type values together as long as the input is parsable. All parsing/memory errors are directed to the terminal
  * **Continuous Address Table Update:** You can adjust update timer or cancel updating by modifying settings
  * **Variable Locking:** PINCE lets you freeze(constantly write a value to memory cell) variables
- **Memory View**
  * **Assembler:** PINCE uses keystone engine to assemble code on the fly
  * **Dissect Code:** You can dissect desired memory regions to find referenced calls, jumps and strings. Disassemble screen will automatically handle the referenced data and show you if there's a referenced address in the current dissasemble view. It can be used from Tools->Dissect Code in the MemoryView window. Using its hotkey instead in the MemoryView window automatically dissects the currently viewed region. You can separately view referenced calls and strings after the search from View->Referenced Calls/Strings. *Note: If you decide to uncheck 'Discard invalid strings' before the search, PINCE will try to search for regular pointers as well*
  * **Bookmarking:** Bookmark menu is dynamically created when right clicked in the disassemble screen. So unlike Cheat Engine, PINCE lets you set unlimited number of bookmarks. List of bookmarks can also be viewed from View->Bookmarks in the MemoryView window. Commenting on an address automatically bookmarks it
  * **Modify on the fly:** PINCE lets you modify registers on the fly. Check [GDB expressions in the Wiki page](https://github.com/korcankaraokcu/PINCE/wiki/About-GDB-Expressions) for additional information
  * **Opcode Search:** You can search opcodes with python regular expressions. To use this feature, click Tools->Search Opcode in the MemoryView window
- **Debugging**
  * Has basic debugging features such as stepping, stepping over, execute till return, break, continue. Also has breakpoints, watchpoints and breakpoint conditions. Has advanced debugging utilities such as Watchpoint/Breakpoint Tracking and Tracing
  * **Chained Breakpoints:** Just like CE, PINCE allows you to set multiple, connected breakpoints at once. If an event(such as condition modification or deletion) happens in one of the breakpoints, other connected breakpoints will get affected as well
  * **Watchpoint Tracking:** Allows you to see which instructions have been accessing to the specified address, just like "What accesses/writes to this address" feature in CE
  * **Breakpoint Tracking:** Allows you to track down addresses calculated by the given register expressions at the specified instruction, just like "Find out what addresses this instruction accesses" feature in CE with a little addon, you can enter multiple register expressions, this allows you to check the value of "esi" even if the instruction is something irrelevant like "mov [eax],edx"
  * **Tracing:** Almost the same with CE. But unlike CE, you can stop tracing whenever you want. Created from scratch with shittons of custom features instead of using gdb's trace&collect commands because some people have too much time on their hands
  * **Collision Detection:** GDB normally permits setting unlimited watchpoints next to each other. But this behaviour leads to unexpected outcomes such as causing GDB or the inferior become completely inoperable. GDB also doesn't care about the number(max 4) or the size(x86->max 4, x64->max 8) of hardware breakpoints. Fortunately, PINCE checks for these problems whenever you set a new breakpoint and detects them before they happen and then inhibits them in a smart way. Lets say you want to set a breakpoint in the size of 32 bytes. But the maximum size for a breakpoint is 8! So, PINCE creates 4 different breakpoints with the size of 8 bytes and then chains them for future actions
- **Code Injection**
  * **Run-time injection:** Only .so injection is supported for now. In Memory View window, click Tools->Inject .so file to select the .so file. An example for creating .so file can be found in "libpince/Injection/". PINCE will be able to inject single line instructions or code caves in near future
- **GDB Console**
  * Is the power of PINCE not enough for you? Then you can use the gdb console provided by PINCE, it's on the top right in main window
- **Simplified/Optimized gdb command alternatives**
  * Custom scripts instead of using gdb's x command for reading memory
  * Custom scripts instead of using gdb's set command for modifying memory
- **libpince - A reusable python library**
  * PINCE provides a reusable python library. You can either read the code or check Reference Widget by clicking Help->libpince in Memory Viewer window to see docstrings. Contents of this widget is automatically generated by looking at the docstrings of the source files. PINCE has a unique parsing technique that allows parsing variables. Check the function get_variable_comments in SysUtils for the details. This feature might be replaced with Sphinx in the future
- **Extendable with .so files at runtime**
  * See [here](https://github.com/korcankaraokcu/PINCE/wiki/Extending-PINCE-with-.so-files)

# Installing
```
git clone --recursive https://github.com/korcankaraokcu/PINCE
cd PINCE
sh install_pince.sh
```
~~For Archlinux, you can also use the [AUR package](https://aur.archlinux.org/packages/pince-git/) as an alternative~~ Currently outdated, use the installation script

If you like to uninstall PINCE, just delete this folder, almost everything is installed locally. Config and user files of PINCE can be found in "~/.config/PINCE", you can manually delete them if you want

***Notes:***
- GDB enhancements (peda, pwndbg, etc) that use a global gdbinit file might cause PINCE to misfunction at times. Please disable them or use them locally before starting PINCE
- If you are having problems with your default gdb version, you can use the `install_gdb.sh` script to install another version locally. Read the comments in it for more information
- Check https://github.com/korcankaraokcu/PINCE/issues/116 for a possible fix if you encounter `'GtkSettings' has no property named 'gtk-fallback-icon-theme'`

# Running PINCE  
Just run ```sh PINCE.sh``` in the PINCE directory

### For developers:  
```
sudo apt-get install qt6-tools-dev (designer and pyuic6)
sudo pip3 install line_profiler (for performance testing)
```
How to use line_profiler: Add ```@profile``` tag to the desired function and run PINCE with ```sudo kernprof -l -v PINCE.py```

# Current Roadmap
- Refactor file naming conventions(decide on snake_case or camelCase for modules etc)
- Create ```CONTRIBUTING.md``` and combine all non-tutorial notes within it
- Refactorize memory write/read functions
- - ReferencedStringsWidgetForm refreshes the cache everytime the comboBox_ValueType changes, this creates serious performance issues if total results are more than 800k. Only update the visible rows to prevent this(check ```disassemble_check_viewport``` for an example)
- - Implement same system for the TrackBreakpointWidgetForm if necessary. Do performance tests
- - Consider using a class instead of primitive return types to store the raw bytes. This class should also include a method to display None type as red '??' text for Qt
- - Provide an option to cut BOM bytes when writing to memory with the types UTF-16 and UTF-32
- - Put a warning for users about replacement bytes for non UTF-8 types
- - Extend string types with LE and BE variants of UTF-16 and UTF-32
- - Change comboBox_ValueType string order to be ... String_UTF-8 String_Others
- - Implement a custom combobox class for comboBox_ValueType and create a context menu for String_Others item
- Having to stop the process to resolve symbols sucks, we already resolve base addresses of libs by ourselves, try to replace this gdb functionality with something else, like parsing from the memory
- Implement "Investigate Registers" button to gather information about the addresses registers point to(independent from other steps)
- Implement selectionChanged signal of lineEdit_HexView
- Implement multi selection for HexView
- Add the ability to track down registers and addresses in tracer(unsure)(independent from other steps)
- Implement CE's Ultimap-like feature for tracing data, dissect code data and raw instruction list. Search for calls and store their hit counts to filter out the functions that haven't or have executed specific number of times. Implement a flexible input field for the execution count. For instance, 2^x only searches for hit counts 2, 4, 8 and so on, 3x only searches for 3, 6, 9 etc.(independent from other steps)([CE#358](https://github.com/cheat-engine/cheat-engine/issues/358))
- Extend search_referenced_strings with relative search
- Consider adding type guessing for the StackView(independent from other steps)
- Move GUI classes of PINCE.py to their own files
- Use gdb python API breakpoints instead of breakpoint commands for optimization, also find a way to eliminate output coming from stepping commands such as ```stepi``` or ```nexti```(independent from other steps)
- Implement a psuedo-terminal for the inferior like edb does(independent from other steps)
- Implement libpince engine
- Implement auto-ESP&aimbot (depends on libpince engine)
- Try to optimize TrackBreakpoint and TrackWatchpoint return data structures further, adding an id field might simplify traversing of the tree, performance tests are required(independent from other steps)
- Extend tagging system to PINCE GUI functions
- Implement multi-line code injection, this will also help with previously dropped inject_with_advanced_injection
- Break on/Catch signals and syscalls
- Flowcharts based on disassembled output
- Automatic function bypassing(make it return the desired value, hook specific parts etc.)
- Implement speedhack(independent from other steps)
- Implement unrandomizer(independent from other steps)
- Implement pointer-scan
- Write at least one test for each function in libpince
- Migrate to Sphinx documentation from the custom libpince documentation(independent from other steps)
- Embedded tutorial videos
- Super-Uber-Rad credits roll with chiptune tunes
- Implement extra MemoryViewerWindow tabs(independent from other steps)
- ~~Consider removing the command file layer of IPC system for GDB_Engine.send_command to speed up things~~(independent from other steps)[Update-29/04/2018 : Delaying this until GDB/MI implements a native multiline command feature or improves ```interpreter-exec``` command to cover every single multiline command type(including ```define``` commands)]
- Implement thread info widget
- Implement developer mode in settings. Developer mode will include features like dissection of GUI elements on events such as mouse-over(independent from other steps)
- Add ability to include non-absolute calls for dissect code feature(i.e call rax). Should be considered after the first version release. Might be useful for multi-breakpoint related features
- Implement toggling of arrows for easier navigation for dissected regions(independent from other steps)
- Provide information about absolute addresses in disassemble screen(independent from other steps)
- Use type hints(py 3.5) and variable annotations(py 3.6) when support drops for older systems(independent from other steps)
- All tables that hold large amount of data should only update the visible rows(check ```disassemble_check_viewport``` for an example)(independent from other steps)
- Add different kinds of themes and the ability to change between them on runtime. Implement dark theme first. Also add the ability to create a custom theme and modify the existing ones(independent from other steps)

# License
GPLv3+. See COPYING file for details

# Contact Information
Korcan Karaokçu([korcankaraokcu](https://github.com/korcankaraokcu)) <korcankaraokcu@gmail.com>  
Çağrı Ulaş([cagriulas](https://github.com/cagriulas)) <cagriulas@gmail.com>  
Jakob Kreuze([TsarFox](https://github.com/TsarFox)) <jakob@memeware.net>  
Gibus <lilac66.dev@gmail.com>  

# Supported platforms
- Ubuntu and its flavors, actively tested on Kubuntu
- Debian and Debian-based (Kali, Mint etc.)
- Archlinux
- SUSE
- Fedora

# Trusted Sources
  * [Official github page](https://github.com/korcankaraokcu/PINCE)
  * [AUR package for Archlinux](https://aur.archlinux.org/packages/pince-git/)
