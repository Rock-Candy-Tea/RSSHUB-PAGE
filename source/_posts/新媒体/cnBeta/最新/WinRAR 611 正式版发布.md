
---
title: 'WinRAR 6.11 正式版发布'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2020/1022/ad85085b6d0cda6.png'
author: cnBeta
comments: false
date: Fri, 04 Mar 2022 08:31:47 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2020/1022/ad85085b6d0cda6.png'
---

<div>   
流行好用的压缩工具，支持鼠标拖放及外壳扩展，完美支持 ZIP 档案，内置程序可以解开
CAB、ARJ、LZH、TAR、GZ、UUE、BZ2、JAR、ISO
等多种类型的压缩文件。重要提示：因ACE模块重大漏洞，WinRAR从5.70 beta 1始不再支持ACE格式压缩档。<br>
 <p><strong>下载地址：</strong></p><p><a href="https://www.rarlab.com/download.htm" _src="https://www.rarlab.com/download.htm" target="_blank">https://www.rarlab.com/download.htm</a></p><p><img src="https://static.cnbetacdn.com/article/2020/1022/ad85085b6d0cda6.png" alt="MZW3&#125;&#123;Y45@F~&#123;`L])&#125;XB&#123;&#123;D.png" referrerpolicy="no-referrer"><br></p><p><strong> Version 6.11</strong></p><p>1. Added support for Gz archives with large archive comments.</p><p>Previously the extraction command failed to unpack gz archives</p><p>if comment size exceeded 16 KB.</p><p>2. Archive comments in gz archives are displayed in the comment window</p><p>and recognized by"Show information"command. Large comments are</p><p>shown partially.</p><p>Previous versions didn't display Gzip comments.</p><p>3. Reserved device names followed by file extension, such as aux.txt,</p><p>are extracted as is in <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 even without"Allow potentially</p><p>incompatible names"option or -oni command line switch.</p><p>Unlike previous Windows versions, Windows 11 treats such names</p><p>as usual files.</p><p>Device names without extension, such as aux, still require these</p><p>options to be unpacked as is regardless of Windows version.</p><p>4. Switch -mes can be also used to suppress the password prompt</p><p>and abort when adding files to encrypted solid archive.</p><p>5. Additional measures to prevent extracting insecure links are</p><p>implemented.</p><p>6. Bugs fixed:</p><p>a) if password exceeding 127 characters was entered when unpacking</p><p>an encrypted archive with console RAR, text after 127th character</p><p>could be erroneously recognized as user's input by different</p><p>prompts issued later;</p><p>b) wrong archived file time could be displayed in overwrite prompt</p><p>when extracting a file from ZIP archive. It happened if such</p><p>archive included extended file times and was created in another</p><p>time zone. It didn't affect the actual file time, which was set</p><p>properly upon extraction.</p>   
</div>
            