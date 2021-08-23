
---
title: '学好shell 函数跟工具必不🉑少'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=714'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 00:03:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=714'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">第9章 函数</h2>
<h3 data-id="heading-1">9.1 系统函数</h3>
<p>1．basename基本语法</p>
<p>basename [string / pathname] [suffix] （功能描述：basename命令会删掉所有的前缀包括最后一个（‘/’）字符，然后将字符串显示出来。</p>
<p>选项：</p>
<p>suffix为后缀，如果suffix被指定了，basename会将pathname或string中的suffix去掉。</p>
<p>2．案例实操</p>
<p>（1）截取该/home/aowin/banzhang.txt路径的文件名称</p>
<p>touch:wq</p>
<ol start="3">
<li>dirname基本语法</li>
</ol>
<p>dirname 文件绝对路径 （功能描述：从给定的包含绝对路径的文件名中去除文件名（非目录的部分），然后返回剩下的路径（目录的部分））</p>
<p>4．案例实操</p>
<p>（1）获取banzhang.txt文件的路径</p>
<h3 data-id="heading-2">9.2 自定义函数</h3>
<p>1．基本语法</p>
<p>[ function ] funname[()]</p>
<p>&#123;</p>
<p>Action;</p>
<p>[return int;]</p>
<p>&#125;</p>
<p>funname</p>
<p>2．经验技巧</p>
<p>（1）必须在调用函数地方之前，先声明函数，shell脚本是逐行运行。不会像其它语言一样先编译。</p>
<p>（2）函数返回值，只能通过$?系统变量获得，可以显示加return返回，如果不加，将以最后一条命令运行结果，作为返回值。return后跟数值n(0-255)</p>
<p>3．案例实操</p>
<p>（1）计算两个输入参数的和</p>
<p>$ touch fun.sh</p>
<p>$ vim fun.sh</p>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-meta">#!/bin/bash</span>
<span class="hljs-keyword">function</span> <span class="hljs-function"><span class="hljs-title">sum</span></span>()

&#123;

  s=0

  s=$[ <span class="hljs-variable">$1</span> + <span class="hljs-variable">$2</span> ]

  <span class="hljs-built_in">echo</span> <span class="hljs-string">"<span class="hljs-variable">$s</span>"</span>

&#125;

<span class="hljs-built_in">read</span> -p <span class="hljs-string">"Please input the number1: "</span> n1;

<span class="hljs-built_in">read</span> -p <span class="hljs-string">"Please input the number2: "</span> n2;

sum <span class="hljs-variable">$n1</span> <span class="hljs-variable">$n2</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>$ chmod 777 fun.sh</p>
<p>$ ./fun.sh</p>
<h2 data-id="heading-3">第10章 Shell工具（重点）</h2>
<h3 data-id="heading-4">10.1 cut</h3>
<p>cut的工作就是“剪”，具体的说就是在文件中负责剪切数据用的。cut 命令从文件的每一行剪切字节、字符和字段并将这些字节、字符和字段输出。</p>
<p>1.基本用法</p>
<p>cut [选项参数] filename</p>
<p>说明：默认分隔符是制表符</p>
<p>2.选项参数说明</p>
<p>表1-55</p>





















<table><thead><tr><th>选项参数</th><th>功能</th></tr></thead><tbody><tr><td>-f</td><td>列号，提取第几列</td></tr><tr><td>-d</td><td>分隔符，按照指定分隔符分割列</td></tr><tr><td>-c</td><td>指定具体的字符</td></tr></tbody></table>
<p>3.案例实操</p>
<p>（0）数据准备</p>
<p>$ touch cut.txt</p>
<p>$ vim cut.txt</p>
<pre><code class="hljs language-sh copyable" lang="sh">dong shen

guan zhen

wo wo

lai lai

le le
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（1）切割cut.txt第一列</p>
<p>$ cut -d " " -f 1 cut.txt</p>
<p>（2）切割cut.txt第二、三列</p>
<p>$ cut -d " " -f 2,3 cut.txt</p>
<p>（3）在cut.txt文件中切割出guan</p>
<p>$ cat cut.txt | grep "guan" | cut -d " " -f 1</p>
<p>（4）选取系统PATH变量值，第2个“：”开始后的所有路径：</p>
<p>$ echo $PATH</p>
<p>$ echo $PATH | cut -d : -f 2-</p>
<p>（5）切割ifconfig 后打印的IP地址</p>
<p>$ ifconfig eth0 | grep "inet addr" | cut -d: -f 2 | cut -d" " -f1</p>
<h3 data-id="heading-5">10.2 sed</h3>
<p>sed是一种流编辑器，它一次处理一行内容。处理时，把当前处理的行存储在临时缓冲区中，称为“模式空间”，接着用sed命令处理缓冲区中的内容，处理完成后，把缓冲区的内容送往屏幕。接着处理下一行，这样不断重复，直到文件末尾。文件内容并没有改变，除非你使用重定向存储输出。</p>
<ol>
<li>基本用法</li>
</ol>
<p>sed [选项参数] ‘command’ filename</p>
<ol start="2">
<li>选项参数说明</li>
</ol>
<p>表1-56</p>

















<table><thead><tr><th>选项参数</th><th>功能</th></tr></thead><tbody><tr><td>-e</td><td>直接在指令列模式上进行sed的动作编辑。</td></tr><tr><td>-i</td><td>直接编辑文件</td></tr></tbody></table>
<ol start="3">
<li>命令功能描述</li>
</ol>
<p>表1-57</p>





















<table><thead><tr><th>命令</th><th>功能描述</th></tr></thead><tbody><tr><td><em>a</em></td><td>新增，a的后面可以接字串，在下一行出现</td></tr><tr><td>d</td><td>删除</td></tr><tr><td>s</td><td>查找并替换</td></tr></tbody></table>
<ol start="4">
<li>案例实操</li>
</ol>
<p>（1）数据准备</p>
<p>$ touch sed.txt</p>
<p>$ vim sed.txt</p>
<pre><code class="hljs language-sh copyable" lang="sh">dong shen

guan zhen

wo wo

lai lai

le le
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（2）将“mei nv”这个单词插入到sed.txt第二行下，打印。</p>
<p>$ sed '2a mei nv' sed.txt</p>
<p>$ cat sed.txt</p>
<p>注意：文件并没有改变</p>
<p>（3）删除sed.txt文件所有包含wo的行</p>
<p>$ sed '/wo/d' sed.txt</p>
<p>（4）将sed.txt文件中wo替换为ni</p>
<p>$ sed 's/wo/ni/g' sed.txt</p>
<p>注意：‘g’表示global，全部替换</p>
<p>（5）将sed.txt文件中的第二行删除并将wo替换为ni</p>
<p>$ sed -e '2d' -e 's/wo/ni/g' sed.txt</p>
<h3 data-id="heading-6">10.3 awk</h3>
<p>一个强大的文本分析工具，把文件逐行的读入，以空格为默认分隔符将每行切片，切开的部分再进行分析处理。</p>
<ol>
<li>基本用法</li>
</ol>
<p>awk [选项参数] ‘pattern1&#123;action1&#125; pattern2&#123;action2&#125;...’ filename</p>
<p>pattern：表示AWK在数据中查找的内容，就是匹配模式</p>
<p>action：在找到匹配内容时所执行的一系列命令</p>
<ol start="2">
<li>选项参数说明</li>
</ol>
<p>表1-55</p>

















<table><thead><tr><th>选项参数</th><th>功能</th></tr></thead><tbody><tr><td>-F</td><td>指定输入文件折分隔符</td></tr><tr><td>-v</td><td>赋值一个用户定义变量</td></tr></tbody></table>
<ol start="3">
<li>案例实操</li>
</ol>
<p>（1）数据准备</p>
<p>$ sudo cp /etc/passwd ./</p>
<p>（2）搜索passwd文件以root关键字开头的所有行，并输出该行的第7列。</p>
<p>$ awk -F: '/^root/&#123;print $7&#125;' passwd</p>
<p>（3）搜索passwd文件以root关键字开头的所有行，并输出该行的第1列和第7列，中间以“，”号分割。</p>
<p>$ awk -F: '/^root/&#123;print <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><mi mathvariant="normal">"</mi><mo separator="true">,</mo><mi mathvariant="normal">"</mi></mrow><annotation encoding="application/x-tex">1","</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord">1</span><span class="mord">"</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord">"</span></span></span></span></span>7&#125;' passwd</p>
<p>注意：只有匹配了pattern的行才会执行action</p>
<p>（4）只显示/etc/passwd的第一列和第七列，以逗号分割，且在所有行前面添加列名user，shell在最后一行添加"dahaige，/bin/zuishuai"。</p>
<p>$ awk -F : 'BEGIN&#123;print "user, shell"&#125; &#123;print <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><mi mathvariant="normal">"</mi><mo separator="true">,</mo><mi mathvariant="normal">"</mi></mrow><annotation encoding="application/x-tex">1","</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord">1</span><span class="mord">"</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord">"</span></span></span></span></span>7&#125; END&#123;print "dahaige,/bin/zuishuai"&#125;' passwd</p>
<p>注意：BEGIN 在所有数据读取行之前执行；END 在所有数据执行之后执行。</p>
<p>（5）将passwd文件中的用户id增加数值1并输出</p>
<p>$ awk -v i=1 -F: '&#123;print $3+i&#125;' passwd</p>
<ol start="4">
<li>awk的内置变量</li>
</ol>
<p>表1-56</p>





















<table><thead><tr><th>变量</th><th>说明</th></tr></thead><tbody><tr><td>FILENAME</td><td>文件名</td></tr><tr><td>NR</td><td>已读的记录数</td></tr><tr><td>NF</td><td>浏览记录的域的个数（切割后，列的个数）</td></tr></tbody></table>
<ol start="5">
<li>案例实操</li>
</ol>
<p>（1）统计passwd文件名，每行的行号，每行的列数</p>
<p>$ awk -F: '&#123;print "filename:" FILENAME ", linenumber:" NR ",columns:" NF&#125;' passwd</p>
<p>（2）切割IP</p>
<p>$ ifconfig enp0s3 | grep "inet " | awk -F " " '&#123;print $2&#125;'</p>
<p>（3）查询sed.txt中空行所在的行号</p>
<p>$ awk '/^$/&#123;print NR&#125;' sed.txt</p>
<h3 data-id="heading-7">10.4 sort</h3>
<p>sort命令是在Linux里非常有用，它将文件进行排序，并将排序结果标准输出。</p>
<ol>
<li>基本语法</li>
</ol>
<p>sort(选项)(参数)</p>
<p>表1-57</p>

























<table><thead><tr><th>选项</th><th>说明</th></tr></thead><tbody><tr><td>-n</td><td>依照数值的大小排序</td></tr><tr><td>-r</td><td>以相反的顺序来排序</td></tr><tr><td>-t</td><td>设置排序时所用的分隔字符</td></tr><tr><td>-k</td><td>指定需要排序的列</td></tr></tbody></table>
<p>参数：指定待排序的文件列表</p>
<ol start="2">
<li>案例实操</li>
</ol>
<p>（1）数据准备</p>
<p>$ touch sort.sh</p>
<p>$ vim sort.sh</p>
<pre><code class="hljs language-sh copyable" lang="sh">bb:40:5.4

bd:20:4.2

xz:50:2.3

cls:10:3.5

ss:30:1.6
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（2）按照“：”分割后的第三列倒序排序。</p>
<p>$ sort -t : -nrk 3 sort.sh</p></div>  
</div>
            