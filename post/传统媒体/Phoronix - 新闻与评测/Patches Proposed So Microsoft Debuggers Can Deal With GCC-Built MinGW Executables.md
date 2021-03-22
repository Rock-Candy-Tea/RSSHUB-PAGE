
---
title: 'Patches Proposed So Microsoft Debuggers Can Deal With GCC-Built MinGW Executables'
categories: 
    - 传统媒体
    - Phoronix - 新闻与评测
author: Phoronix - 新闻与评测
comments: false
date: Sun, 21 Mar 2021 10:13:40 GMT
thumbnail: 'https://www.phoronix.com/assets/categories/gnu.jpg'
---

<div>   
<div style="float: left; padding: 0 10px 10px;"><img alt="GNU -- " src="https://www.phoronix.com/assets/categories/gnu.jpg" width="100" height="100" referrerpolicy="no-referrer"></div>
Patches have been proposed for the GCC compiler to ultimately allow MinGW Windows executables to be debugged with Microsoft's debuggers.
<br>
<br>The set of two dozen patches is for allowing the GNU Compiler Collection to emit debugging information in the PE-specific CodeView format used by Microsoft's debuggers. This PE-specific CodeView format is partially documented by Microsoft and understood via header files open-sourced by Microsoft as part of their PDB (Program Database) symbol file format.
<br>
<br>Taking up this effort to allow MinGW EXEs to be handled under Microsoft debuggers is Mark Harmstone, the open-source developer also known for <a href="https://www.phoronix.com/scan.php?page=news_item&px=WinBtrfs-1.0-Released">porting Btrfs to Windows</a> as well as <a href="https://www.phoronix.com/scan.php?page=news_item&px=Quibble-Open-Source-Windows-BL">writing an open-source bootloader for Windows</a> and other similar projects.
<br>
<br>With these patches and using the new "<em>-gcodeview</em>" compiler option, the EXEs have in turn been tested under debuggers like Microsoft Visual Studio, Windbg, Radare2, and Cvdump. Testing has happened on both x86 and AMD64.
<br>
<br>Those interested in the prospects of running GCC-built Windows binaries under Microsoft Windows debugging tools can see <a href="https://gcc.gnu.org/pipermail/gcc-patches/2021-March/567030.html">this patch series</a> on the GCC mailing list.  
</div>
            