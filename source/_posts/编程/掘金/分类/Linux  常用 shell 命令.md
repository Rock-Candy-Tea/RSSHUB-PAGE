
---
title: 'Linux  常用 shell 命令'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c43883f3ebfe413da4532c160f928ae3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 04:20:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c43883f3ebfe413da4532c160f928ae3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第25天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<h4 data-id="heading-0">1. 文件、目录操作</h4>
<p><strong>1.1 ls 命令; 功能：显示文件和目录的信息</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-built_in">ls</span>　      以默认方式显示当前目录文件列表
<span class="hljs-built_in">ls</span> <span class="hljs-literal">-a</span>    显示所有文件包括隐藏文件
<span class="hljs-built_in">ls</span> <span class="hljs-literal">-l</span>    显示文件属性，包括大小，日期，符号连接，是否可读写及是否可执行
<span class="hljs-built_in">ls</span> <span class="hljs-literal">-lh</span>   显示文件的大小，以容易理解的格式印出文件大小 (例如 <span class="hljs-number">1</span>K <span class="hljs-number">234</span>M2G)
<span class="hljs-built_in">ls</span> <span class="hljs-operator">-lt</span>   显示文件，按照修改时间排序
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>1.2 cd 命令；功能：改名目录</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-built_in">cd</span> <span class="hljs-built_in">dir</span>　  切换到当前目录下的<span class="hljs-built_in">dir</span>目录
<span class="hljs-built_in">cd</span> /　    切换到根目录
<span class="hljs-built_in">cd</span> ..　   切换到到上一级目录
<span class="hljs-built_in">cd</span> ../..　切换到上二级目录
<span class="hljs-built_in">cd</span> ~　    切换到用户目录，比如是root用户，则切换到/root下
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>根目录与家目录的区别：</strong></p>
<p>根目录是系统的一级文件结构，家目录只是非root用户控制目录。</p>
<p>相当于 windows 我的文档，非root用户只能完会控制家目录的文件，不能控制根目录下其它的文件。</p>
<p>根目录是设备的最顶层目录，用 / 表示</p>
<p>家目录是每个用户登录系统后所在的目录，通常在 /home 下，以用户名作为目录，可以用 ~ 表示。</p>
<p>cd /   进入根目录</p>
<p>cd ~/  进入家目录</p>
<p>可以用 /home/someone 进入 someone 的家目录</p>
<p><strong>1.3 cp 命令;    功能：复制文件</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-built_in">cp</span> source target　                   将文件source复制为target
<span class="hljs-built_in">cp</span> /root/source .　                  将/root下的文件source复制到当前目录
eg:
<span class="hljs-comment"># cp/home/open_038_dev/external_files/test/test.sh .</span>
<span class="hljs-built_in">cp</span> –av soure_dir target_dir　        将整个目录复制，两目录完全一样
<span class="hljs-built_in">cp</span> <span class="hljs-literal">-r</span> 源文件 目标文件                  复制文件夹
eg：
<span class="hljs-comment"># cp -r  views views.bak            以 views 为源文件，复制一个 views.bak 文件</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>1.4 rm 命令； 功能：删除文件或目录</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-built_in">rm</span> file　         删除文件file
<span class="hljs-built_in">rm</span> <span class="hljs-operator">-f</span> file        删除时候不进行提示。可以于<span class="hljs-built_in">r</span>参数配合使用
<span class="hljs-built_in">rm</span> <span class="hljs-literal">-rf</span> domed　    删除domed目录（文件夹）以及它所包含的所有内容
<span class="hljs-built_in">rm</span> <span class="hljs-literal">-i</span> a*          删除当前目录下所有以字母a开头的文件，并且在每次删除时，提示用户进行确认
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>1.5 mv 命令； 功能：将文件移动走，或者改名，在uinx下面没有改名的命令，如果想改名，可以使用该命令</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">命令参数：
<span class="hljs-literal">-b</span> ：若需覆盖文件，则覆盖前先行备份。 
<span class="hljs-operator">-f</span> ：force 强制的意思，如果目标文件已经存在，不会询问而直接覆盖；
<span class="hljs-literal">-i</span> ：若目标文件 (destination) 已经存在时，就会询问是否覆盖！
<span class="hljs-literal">-u</span> ：若目标文件已经存在，且 source 比较新，才会更新(update)
<span class="hljs-literal">-t</span> ：-<span class="hljs-literal">-target</span><span class="hljs-literal">-directory</span>=DIRECTORY <span class="hljs-built_in">move</span> all SOURCE arguments into DIRECTORY，
即指定 <span class="hljs-built_in">mv</span> 的目标目录，该选项适用于移动多个源文件到一个目录的情况，此时目标目录在前，源文件在后

<span class="hljs-comment"># 将文件source更名为target</span>
<span class="hljs-built_in">mv</span> source target　      
<span class="hljs-comment">#  将文件log1.txt,log2.txt,log3.txt 移动到目录test3中                                    </span>
<span class="hljs-built_in">mv</span> log1.txt log2.txt log3.txt test3   
<span class="hljs-comment">#  将文件log1.txt log2.txt  log3.txt 移动到 /opt/soft/test/test4 目录下                      </span>
<span class="hljs-built_in">mv</span> <span class="hljs-literal">-t</span> /opt/soft/test/test4/ log1.txt log2.txt  log3.txt  
<span class="hljs-comment">#  移动当前文件夹下的所有文件到上一级目录  </span>
<span class="hljs-built_in">mv</span> * ../                                                     
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>1.6 diff 命令； 功能：比较文件内容</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-comment"># 比较目录1与目录2的文件列表是否相同，但不比较文件的实际内容，不同则列出</span>
<span class="hljs-built_in">diff</span> dir1 dir2　
<span class="hljs-comment"># 比较文件1与文件2的内容是否相同，如果是文本格式的文件，则将不相同的内容显示，如果是二进制代码则只表示两个文件是不同的</span>
<span class="hljs-built_in">diff</span> file1 file2
<span class="hljs-comment"># 比较文件，显示两个文件不相同的内容　</span>
comm file1 file2　
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>1.7 ln 命令； 功能：建立链接</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">ln source_path target_path 硬连接
ln <span class="hljs-literal">-s</span> source_path target_path 软连接

ln 是 linux 中又一个非常重要命令，它的功能是为某一个文件在另外一个位置建立一个同不的链接，
这个命令最常用的参数是<span class="hljs-literal">-s</span>，具体用法是：ln –s 源文件 目标文件

当我们需要在不同的目录，用到相同的文件时，我们不需要在每一个需要的目录下都放一个必须相同的文件，
我们只要在某个固定的目录，放上该文件，然后在其它的目录下用 ln 命令链接（link）它就可以，不必重复的占用磁盘空间。
eg:
ln –s /bin/less /usr/local/bin/less


删除软连接
<span class="hljs-built_in">rm</span> –rf /target     注意：不要在后文件名后面加斜杆 “/” 否则会删除文件夹的内容
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>1.8 mkdir 命令； 功能：创建目录</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">mkdir [选项] 目录名 选项

所在路径：/bin/mkdir
执行权限：所有用户
功能描述：创建空目录
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>1.9 pwd 命令； 功能：查询所在目录</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">所在路径：/bin/<span class="hljs-built_in">pwd</span>
执行权限：所有用户。
功能描述：查询所在的工作目录
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>1.10 sz 命令； 功能：下载文件到本地下载目录</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">sz 文件路径
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>1.11 rz 命令； 功能：本地上传文件到服务器</strong>
会跳出文件选择窗口，选择好文件，点击确认即可</p>
<pre><code class="hljs language-powershell copyable" lang="powershell">rz
rz <span class="hljs-literal">-y</span>       把文件上传到Linux中，如果有相同文件名的文件，会将其覆盖;
rz <span class="hljs-literal">-E</span>       把文件上传到Linux中，如果有相同文件名的文件，不会将其覆盖，
而是会在所上传文件后面加上 .<span class="hljs-number">0</span> ，两个文件都会存在与此目录中，再次上传则会在文件名后加上 .<span class="hljs-number">1</span>，以此类推;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>ps:</strong></p>
<p>检查是否已经有该命令</p>
<p>如果没有安装对应的rpm包，则当你输入 rz、sz 则会有如下提示</p>
<pre><code class="hljs language-powershell copyable" lang="powershell">[<span class="hljs-type">root</span>@<span class="hljs-type">vdedu</span> <span class="hljs-type">test</span>]<span class="hljs-comment"># sz</span>
<span class="hljs-literal">-bash</span>: sz: command not found
[<span class="hljs-type">root</span>@<span class="hljs-type">vdedu</span> <span class="hljs-type">test</span>]<span class="hljs-comment"># rz</span>
<span class="hljs-literal">-bash</span>: /usr/bin/rz: No such file or directory
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装 lrzsz</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Ffreshmeat.sourceforge.net%2Fprojects%2Flrzsz%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://freshmeat.sourceforge.net/projects/lrzsz/" ref="nofollow noopener noreferrer">lrzsz</a> 是一个unix通信套件提供的X，Y，和ZModem文件传输协议。</p>
<pre><code class="hljs language-powershell copyable" lang="powershell">yum <span class="hljs-literal">-y</span> install lrzsz 
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">2. 解压、压缩（打包）命令</h4>
<p>减少文件大小的好处：一是可以减少存储空间；二是通过网络传输文件时，可以减少传输的时间；</p>
<p><strong>2.1 tar 命令; 功能：归档、压缩等</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">.tar
解包：tar xvf FileName.tar
打包：tar cvf FileName.tar DirName
（注：tar是打包，不是压缩！）
———————————————
.gz
解压<span class="hljs-number">1</span>：gunzip FileName.gz
解压<span class="hljs-number">2</span>：gzip <span class="hljs-literal">-d</span> FileName.gz
压缩：gzip FileName

.tar.gz 和 .tgz
解压：tar zxvf FileName.tar.gz
压缩：tar zcvf FileName.tar.gz DirName
———————————————
.bz2
解压<span class="hljs-number">1</span>：bzip2 <span class="hljs-literal">-d</span> FileName.bz2
解压<span class="hljs-number">2</span>：bunzip2 FileName.bz2
压缩： bzip2 <span class="hljs-literal">-z</span> FileName

.tar.bz2
解压：tar jxvf FileName.tar.bz2
压缩：tar jcvf FileName.tar.bz2 DirName
———————————————
.bz
解压<span class="hljs-number">1</span>：bzip2 <span class="hljs-literal">-d</span> FileName.bz
解压<span class="hljs-number">2</span>：bunzip2 FileName.bz
压缩：未知

.tar.bz
解压：tar jxvf FileName.tar.bz
压缩：未知
———————————————
.Z
解压：uncompress FileName.Z
压缩：compress FileName.tar.Z

解压：tar Zxvf FileName.tar.Z
压缩：tar Zcvf FileName.tar.Z DirName
———————————————
.zip
解压：unzip FileName.zip
压缩：zip FileName.zip DirName
———————————————
.rar
解压：rar x FileName.rar
压缩：rar a FileName.rar DirName
———————————————
.lha
解压：lha <span class="hljs-literal">-e</span> FileName.lha
压缩：lha <span class="hljs-literal">-a</span> FileName.lha FileName
———————————————
.rpm
解包：rpm2cpio FileName.rpm | cpio <span class="hljs-literal">-div</span>
———————————————
.deb
解包：ar p FileName.deb data.tar.gz | tar zxf -
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2.2 gzip 命令; 功能：压缩gz格式的文件</strong></p>
<p>gzip 属于 GNU 软件，是 linux 系统首选的压缩工具，tar 归档命令的 -z 选项压缩也是利用 gzip/gunzip 来压缩/解压文件。</p>
<p>gzip 生成 .gz 文件</p>
<pre><code class="hljs language-powershell copyable" lang="powershell">语法：
gzip [选项] [文件或目录…]
参数：
<span class="hljs-literal">-c</span> 或–stdout或 –to<span class="hljs-literal">-stdout</span> 将压缩（解压）的内容输出到标准输出设备上，并保留原有文件
<span class="hljs-literal">-d</span> 或–decompress 解压
<span class="hljs-literal">-l</span> 或–list 如果目标文件是压缩文件，则显示压缩大小，解压后大小，压缩比率，解压后文件名。
<span class="hljs-literal">-r</span> 或 –recursive 递归压缩
<span class="hljs-literal">-t</span> 或 –test 测试，检查压缩文件的完整性
<span class="hljs-literal">-v</span> 或 –verbose 对每一个文件，显示文件名和压缩比。
<span class="hljs-literal">-V</span> 或 –version 显示版本号
<span class="hljs-literal">-num</span> 指定压缩的速度<span class="hljs-literal">-1</span>或–fast表示快速（低压缩比）<span class="hljs-literal">-9</span>或–best慢（高压缩比）
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-powershell copyable" lang="powershell">eg:
<span class="hljs-number">1</span>. 压缩当前目录下的所有文件
linux@ubuntu:~/test<span class="hljs-variable">$</span> <span class="hljs-built_in">ls</span>
a  b  桃花岛.mp3   <span class="hljs-comment">#有三个文件</span>
linux@ubuntu:~/test<span class="hljs-variable">$</span> gzip *  <span class="hljs-comment">#压缩所有文件</span>
linux@ubuntu:~/test<span class="hljs-variable">$</span> <span class="hljs-built_in">ls</span>
a.gz  b.gz  桃花岛.mp3.gz  <span class="hljs-comment">#分别生成对应的.gz文件，但原始文件被删除了。</span>

<span class="hljs-number">2</span>. 解压例<span class="hljs-number">1</span>中的所有文件，并显示压缩比
linux@ubuntu:~/test<span class="hljs-variable">$</span> gzip -<span class="hljs-literal">-decompress</span> <span class="hljs-literal">-v</span> *
a.gz: <span class="hljs-number">1.3</span>% -- replaced with a
b.gz: <span class="hljs-number">1.3</span>% -- replaced with b
桃花岛.mp3.gz: <span class="hljs-number">1.3</span>% -- replaced with 桃花岛.mp3

<span class="hljs-number">3</span>. 显示例<span class="hljs-number">1</span>中的所有的压缩文件的信息
linux@ubuntu:~/test<span class="hljs-variable">$</span> gzip -<span class="hljs-literal">-list</span> *
compressed        uncompressed  ratio uncompressed_name
<span class="hljs-number">5566197</span>             <span class="hljs-number">5638272</span>   <span class="hljs-number">1.3</span>% a
<span class="hljs-number">5566197</span>             <span class="hljs-number">5638272</span>   <span class="hljs-number">1.3</span>% b
<span class="hljs-number">5566209</span>             <span class="hljs-number">5638272</span>   <span class="hljs-number">1.3</span>% 桃花岛.mp3
<span class="hljs-number">16698603</span>            <span class="hljs-number">16914816</span>   <span class="hljs-number">1.3</span>% (totals)
可以看出压缩完，未压缩时，压缩率，解压后的文件名。

<span class="hljs-number">4</span>、对test目录下的文件压缩(可以用递归的方式进行压缩)
linux@ubuntu:~<span class="hljs-variable">$</span> <span class="hljs-built_in">ls</span> test
a  b  桃花岛.mp3
linux@ubuntu:~<span class="hljs-variable">$</span> gzip -<span class="hljs-literal">-recursiv</span> test  <span class="hljs-comment">#对目录下的文件进行压缩</span>
linux@ubuntu:~<span class="hljs-variable">$</span> <span class="hljs-built_in">ls</span> test
a.gz  b.gz  桃花岛.mp3.gz   <span class="hljs-comment">#</span>

可以看出并没生成一个压缩文件，而是对目录下的文件分别压缩，这表示并不是生成一个包，
那就是说不能对目录进行压缩，可以用tar打包，之后再进行压缩。
tar <span class="hljs-literal">-cf</span> test.tar test/ tar <span class="hljs-literal">-zcf</span> test.tar.gz test/ 也是可以的,用tar <span class="hljs-literal">-zxf</span>解压
之后再进行gzip test.tar进行压缩
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意：</strong></p>
<ol>
<li>指定压缩文件必须存在。</li>
<li>不对目录进行压缩，但可以递归目录下的文件进行压缩。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c43883f3ebfe413da4532c160f928ae3~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">3. 查看文件内容命令</h4>
<p><strong>3.1 cat 命令;  功能：显示文件的内容</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-built_in">cat</span> file　
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3.2 tail 命令;  功能：显示文件的最后几行</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">eg:
tail <span class="hljs-literal">-n</span> <span class="hljs-number">100</span> aaa.txt       显示文件aaa.txt文件的最后<span class="hljs-number">100</span>行
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3.3 more 命令;  功能：分页显示命令</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">more　file
more 命令也可以通过管道符 | 与其他的命令一起使用
eg:
<span class="hljs-built_in">ps</span> ux|more
<span class="hljs-built_in">ls</span>|more
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3.4 vi 命令;</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">输入命令的方式（步骤）：
<span class="hljs-number">1</span>. 执行 vi FileName  进入编辑器（默认命令模式），
<span class="hljs-number">2</span>. 点击a或i进入编辑模式，敲入内容：如 hello linux world !
<span class="hljs-number">3</span>. 然后按键盘上的esc键退出编辑模式（进入到命令模式），
<span class="hljs-number">4</span>. 最后敲冒号 ：，
<span class="hljs-number">5</span>. 再敲 wq! 保存并退出。
-------
wq 解释为：<span class="hljs-built_in">write</span> quite
不想保存，q
强制退出 q!
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3.5 touch 命令;   功能：创建一个空文件</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">touch aaa.txt               创建一个空文件，文件名为 aaa.txt
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">4. 基本系统命令</h4>
<p><strong>4.1 man 命令; 功能：查看某个命令的帮助</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">eg:
<span class="hljs-built_in">man</span> <span class="hljs-built_in">ls</span>          显示<span class="hljs-built_in">ls</span>命令的帮助内容
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4.2 w 命令;  功能：显示登录用户的详细信息</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">w
eg:
<span class="hljs-number">22</span>:<span class="hljs-number">06</span>:<span class="hljs-number">51</span> up <span class="hljs-number">43</span> min,  <span class="hljs-number">1</span> user,  load average: <span class="hljs-number">0.00</span>, <span class="hljs-number">0.00</span>, <span class="hljs-number">0.00</span>
USER     TTY      FROM              LOGIN<span class="hljs-selector-tag">@</span>   IDLE   JCPU   PCPU WHAT
zhoulj   pts/<span class="hljs-number">0</span>    <span class="hljs-number">10.140</span>.<span class="hljs-number">0.109</span>     <span class="hljs-number">21</span>:<span class="hljs-number">24</span>    <span class="hljs-number">0.00</span>s  <span class="hljs-number">0.85</span>s  <span class="hljs-number">0.09</span>s sshd: zhoulj [<span class="hljs-type">priv</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4.3 who 命令;  功能：显示登录用户</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">who
eg:
zhoulj   pts/<span class="hljs-number">0</span>        Mar <span class="hljs-number">13</span> <span class="hljs-number">21</span>:<span class="hljs-number">24</span> (<span class="hljs-number">10.140</span>.<span class="hljs-number">0.109</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4.4 last 命令;  功能：查看最近那些用户登录系统</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">last
eg:
zhoulj   pts/<span class="hljs-number">0</span>        <span class="hljs-number">10.140</span>.<span class="hljs-number">0.109</span>     Mon Mar <span class="hljs-number">13</span> <span class="hljs-number">21</span>:<span class="hljs-number">24</span>   still logged <span class="hljs-keyword">in</span>   
reboot   system boot  <span class="hljs-number">2.6</span>.<span class="hljs-number">8</span><span class="hljs-literal">-2</span><span class="hljs-literal">-386</span>      Mon Mar <span class="hljs-number">13</span> <span class="hljs-number">21</span>:<span class="hljs-number">23</span>          (<span class="hljs-number">00</span>:<span class="hljs-number">43</span>)   
zhoulj   pts/<span class="hljs-number">0</span>        <span class="hljs-number">10.140</span>.<span class="hljs-number">0.105</span>     Sun Mar <span class="hljs-number">12</span> <span class="hljs-number">22</span>:<span class="hljs-number">51</span> - down   (<span class="hljs-number">00</span>:<span class="hljs-number">00</span>)   
zhoulj   pts/<span class="hljs-number">0</span>        <span class="hljs-number">10.140</span>.<span class="hljs-number">0.105</span>     Sun Mar <span class="hljs-number">12</span> <span class="hljs-number">22</span>:<span class="hljs-number">51</span> - <span class="hljs-number">22</span>:<span class="hljs-number">51</span>  (<span class="hljs-number">00</span>:<span class="hljs-number">00</span>)   
root     tty1                          Sun Mar <span class="hljs-number">12</span> <span class="hljs-number">22</span>:<span class="hljs-number">50</span> - down   (<span class="hljs-number">00</span>:<span class="hljs-number">01</span>)   
root     tty1                          Sun Mar <span class="hljs-number">12</span> <span class="hljs-number">22</span>:<span class="hljs-number">46</span> - <span class="hljs-number">22</span>:<span class="hljs-number">48</span>  (<span class="hljs-number">00</span>:<span class="hljs-number">02</span>)   
root     tty1                          Sun Mar <span class="hljs-number">12</span> <span class="hljs-number">22</span>:<span class="hljs-number">43</span> - <span class="hljs-number">22</span>:<span class="hljs-number">46</span>  (<span class="hljs-number">00</span>:<span class="hljs-number">02</span>)   
reboot   system boot  <span class="hljs-number">2.6</span>.<span class="hljs-number">8</span><span class="hljs-literal">-2</span><span class="hljs-literal">-386</span>      Mon Mar <span class="hljs-number">13</span> <span class="hljs-number">06</span>:<span class="hljs-number">34</span>          (<span class="hljs-literal">-7</span>:<span class="hljs-literal">-41</span>)   
wtmp begins Mon Mar <span class="hljs-number">13</span> <span class="hljs-number">06</span>:<span class="hljs-number">34</span>:<span class="hljs-number">11</span> <span class="hljs-number">2006</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4.5 date 命令;  功能：系统日期设定</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">date　                          显示当前日期时间
date <span class="hljs-literal">-s</span> <span class="hljs-number">20</span>:<span class="hljs-number">30</span>:<span class="hljs-number">30</span>　              设置系统时间为<span class="hljs-number">20</span>:<span class="hljs-number">30</span>:<span class="hljs-number">30</span>
date <span class="hljs-literal">-s</span> <span class="hljs-number">2002</span><span class="hljs-literal">-3</span><span class="hljs-literal">-5</span>　              设置系统时期为<span class="hljs-number">2003</span><span class="hljs-literal">-3</span><span class="hljs-literal">-5</span>
date <span class="hljs-literal">-s</span> <span class="hljs-string">"060520 06:00:00"</span>　     设置系统时期为<span class="hljs-number">2006</span>年<span class="hljs-number">5</span>月<span class="hljs-number">20</span>日<span class="hljs-number">6</span>点整
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4.6 clock 命令;  功能：时钟设置</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">clock –<span class="hljs-built_in">r</span>　   对系统Bios中读取时间参数
clock –w　   将系统时间(如由date设置的时间)写入Bios
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4.7 uname 命令;  功能：查看系统版本</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">uname <span class="hljs-literal">-a</span>　显示操作系统内核的version
eg:
Linux Sarge <span class="hljs-number">2.6</span>.<span class="hljs-number">8</span><span class="hljs-literal">-2</span><span class="hljs-literal">-386</span> <span class="hljs-comment">#1 Tue Aug 16 12:46:35 UTC 2005 i686 GNU/Linux</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4.8 关闭和重新启动系统命令</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">reboot　              重新启动计算机
shutdown <span class="hljs-literal">-r</span> now       重新启动计算机，停止服务后重新启动计算机
shutdown <span class="hljs-literal">-h</span> now       关闭计算机，停止服务后再关闭系统
halt                  关闭计算机
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4.9 su 命令;  功能:切换当前用户身份到其他用户身份，变更时须输入所要变更的用户帐号与密码</strong>
<strong>注意：-   很关键，使用 - 将使用用户的环境变量</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">su -                    切换到root用户
su - zhoulj             切换到zhoulj用户，
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">5. 监视系统状态命令</h4>
<p><strong>5.1 top 命令; 功能：查看系统cpu、内存等使用情况</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">top
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>5.2 free 命令; 功能：查看 内存 和 swap分区 使用情况</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">free <span class="hljs-literal">-tm</span>
eg:
              total        used        free      shared  buff/cache   available
Mem:          <span class="hljs-number">31980</span>        <span class="hljs-number">8478</span>         <span class="hljs-number">288</span>       <span class="hljs-number">11681</span>       <span class="hljs-number">23212</span>       <span class="hljs-number">11185</span>
Swap:         <span class="hljs-number">20479</span>         <span class="hljs-number">194</span>       <span class="hljs-number">20285</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>5.3  uptime 命令;
功能：现在的时间 ，系统开机运转到现在经过的时间，连线的使用者数量，最近一分钟，五分钟和十五分钟的系统负载</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">uptime
eg:
<span class="hljs-number">23</span>:<span class="hljs-number">27</span>:<span class="hljs-number">33</span> up <span class="hljs-number">123</span> days, <span class="hljs-number">10</span>:<span class="hljs-number">25</span>,  <span class="hljs-number">3</span> users,  load average: <span class="hljs-number">1.13</span>, <span class="hljs-number">1.10</span>, <span class="hljs-number">1.19</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>5.4 vmstat 命令; 功能：监视虚拟内存使用情况</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">vmstat 
eg
procs ----------<span class="hljs-literal">-memory</span>---------- --<span class="hljs-literal">-swap</span>-- ----<span class="hljs-literal">-io</span>---- <span class="hljs-literal">-system</span>-- -----<span class="hljs-literal">-cpu</span>-----
 <span class="hljs-built_in">r</span>  b   swpd   free   buff  cache   <span class="hljs-built_in">si</span>   so    bi    bo   <span class="hljs-keyword">in</span>   cs us sy id wa st
<span class="hljs-number">13</span>  <span class="hljs-number">0</span> <span class="hljs-number">204032</span> <span class="hljs-number">325884</span>      <span class="hljs-number">0</span> <span class="hljs-number">23746456</span>    <span class="hljs-number">0</span>    <span class="hljs-number">0</span>     <span class="hljs-number">0</span>     <span class="hljs-number">1</span>    <span class="hljs-number">0</span>    <span class="hljs-number">0</span>  <span class="hljs-number">1</span>  <span class="hljs-number">1</span> <span class="hljs-number">98</span>  <span class="hljs-number">0</span>  <span class="hljs-number">0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>5.5 ps 命令; 功能：显示进程信息</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-built_in">ps</span> ux 显示当前用户的进程
<span class="hljs-built_in">ps</span> uxwww 显示当前用户的进程的详细信息
<span class="hljs-built_in">ps</span> aux 显示所有用户的进程
<span class="hljs-built_in">ps</span> ef 显示系统所有进程信息
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>5.6 kill 命令; 功能：干掉某个进程，进程号可以通过 ps 命令得到</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-built_in">kill</span> <span class="hljs-literal">-9</span> <span class="hljs-number">1001</span>　                  将进程编号为<span class="hljs-number">1001</span>的程序干掉
<span class="hljs-built_in">kill</span> all <span class="hljs-literal">-9</span> apache　            将所有名字为apapche的程序杀死，<span class="hljs-built_in">kill</span>不是万能的，对僵死的程序则无效。
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">6. 用户和组相关命令</h4>
<p><strong>6.1 groupadd 命令; 功能：添加组</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">groupadd test1                   添加test1组
groupadd <span class="hljs-literal">-g</span> <span class="hljs-number">1111</span> test2           添加test2组，组id为<span class="hljs-number">1111</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.2 useradd 命令; 功能：添加用户</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">useradd user1                                添加用户user1，home为/home/user1，组为user1
useradd <span class="hljs-literal">-g</span> test1 <span class="hljs-literal">-m</span> <span class="hljs-literal">-d</span> /home/test1 test1     添加用户test1，home为/home/test1，组为test1
user list　                                  显示已登陆的用户列表
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.3 passwd 命令; 功能：更改用户密码</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">passwd user1　     修改用户user1的密码
passwd <span class="hljs-literal">-d</span> root　   将root用户的密码删除
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.4 userdel 命令; 功能：删除用户</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">userdel user1    　删除user1用户
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.5 chown 命令; 功能：改变文件或目录的所有者</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">chown user1 /<span class="hljs-built_in">dir</span>　             将/<span class="hljs-built_in">dir</span>目录设置为user1所有

chown <span class="hljs-literal">-R</span> user1.user1 /<span class="hljs-built_in">dir</span>　    将/<span class="hljs-built_in">dir</span>目录下所有文件和目录，设置为user1所有,组为user1。<span class="hljs-literal">-R</span>递归到下面的每个文件和目录
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.6 chgrp 命令;  功能：改变文件或目录的所有组</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">chgrp user1 /<span class="hljs-built_in">dir</span>    　将/<span class="hljs-built_in">dir</span>目录设置为user1所有
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.7 chmod 命令;  功能：改变用户的权限</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">chmod a+x file　       将file文件设置为可执行，脚本类文件一定要这样设置一个，否则得用bash file才能执行
chmod <span class="hljs-number">666</span> file　       将文件file设置为可读写
chmod <span class="hljs-number">750</span> file         将文件file设置为，所有者为完全权限，同组可以读和执行，其他无权限
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.8 id 命令;  功能：显示用户的信息，包括 uid、gid 等</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell"> id zhoulj
 eg:
 uid=<span class="hljs-number">500</span>(zhoulj) gid=<span class="hljs-number">500</span>(zhoulj) groups=<span class="hljs-number">500</span>(zhoulj)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.9 finger 命令;  功能：显示用的信息</strong></p>
<p>注意：debian 下没有该命令</p>
<pre><code class="hljs language-powershell copyable" lang="powershell">finger zhoulj
eg:
Login: zhoulj                           Name:
Directory: /home/zhoulj                 Shell: /bin/bash
On since Sun May <span class="hljs-number">21</span> <span class="hljs-number">07</span>:<span class="hljs-number">59</span> (CST) on pts/<span class="hljs-number">0</span> from <span class="hljs-number">192.168</span>.<span class="hljs-number">1.4</span>
No mail.
No Plan.
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">7. 磁盘操作命令</h4>
<p><strong>7.1 df 命令; 功能：检查文件系统的磁盘空间占用情况</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">参数 
<span class="hljs-literal">-a</span>                   列出全部目录
<span class="hljs-literal">-Ta</span>                  列出全部目录，并且显示文件类型
<span class="hljs-literal">-B</span>                   显示块信息
<span class="hljs-literal">-i</span>                   以i节点列出全部目录
<span class="hljs-literal">-h</span>                   按照日常习惯显示（如：<span class="hljs-number">1</span>K、<span class="hljs-number">100</span>M、<span class="hljs-number">20</span>G）
<span class="hljs-literal">-x</span> [<span class="hljs-type">filesystype</span>]     不显示[<span class="hljs-type">filesystype</span>]

df <span class="hljs-literal">-Th</span>
eg:
Filesystem     <span class="hljs-built_in">Type</span>      Size  Used Avail Use% Mounted on
/dev/sda3      xfs       <span class="hljs-number">259</span>G   <span class="hljs-number">53</span>G  <span class="hljs-number">206</span>G  <span class="hljs-number">21</span>% /
devtmpfs       devtmpfs   <span class="hljs-number">16</span>G     <span class="hljs-number">0</span>   <span class="hljs-number">16</span>G   <span class="hljs-number">0</span>% /dev
tmpfs          tmpfs      <span class="hljs-number">16</span>G     <span class="hljs-number">0</span>   <span class="hljs-number">16</span>G   <span class="hljs-number">0</span>% /dev/shm
tmpfs          tmpfs      <span class="hljs-number">16</span>G  <span class="hljs-number">1.6</span>G   <span class="hljs-number">15</span>G  <span class="hljs-number">10</span>% /run
tmpfs          tmpfs      <span class="hljs-number">16</span>G     <span class="hljs-number">0</span>   <span class="hljs-number">16</span>G   <span class="hljs-number">0</span>% /sys/fs/cgroup
/dev/sda1      xfs       <span class="hljs-number">497</span>M  <span class="hljs-number">169</span>M  <span class="hljs-number">329</span>M  <span class="hljs-number">34</span>% /boot
tmpfs          tmpfs     <span class="hljs-number">3.2</span>G   <span class="hljs-number">56</span>K  <span class="hljs-number">3.2</span>G   <span class="hljs-number">1</span>% /run/user/<span class="hljs-number">1000</span>
tmpfs          tmpfs     <span class="hljs-number">3.2</span>G     <span class="hljs-number">0</span>  <span class="hljs-number">3.2</span>G   <span class="hljs-number">0</span>% /run/user/<span class="hljs-number">1002</span>
tmpfs          tmpfs     <span class="hljs-number">3.2</span>G     <span class="hljs-number">0</span>  <span class="hljs-number">3.2</span>G   <span class="hljs-number">0</span>% /run/user/<span class="hljs-number">0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>7.2 du 命令; 功能：检测一个目录和（递归地）所有它的子目录中的文件占用的磁盘空间</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-literal">-s</span> [<span class="hljs-type">dirName</span>]     显示目录占用总空间
<span class="hljs-literal">-sk</span> [<span class="hljs-type">dirName</span>]    显示目录占用总空间，以k为单位
<span class="hljs-literal">-sb</span> [<span class="hljs-type">dirName</span>]    显示目录占用总空间，以b为单位
<span class="hljs-literal">-sm</span> [<span class="hljs-type">dirName</span>]    显示目录占用总空间，以m为单位
<span class="hljs-literal">-sc</span> [<span class="hljs-type">dirName</span>]    显示目录占用总空间，加上目录统计
<span class="hljs-literal">-sh</span> [<span class="hljs-type">dirName</span>]    只统计目录大小
eg:
du <span class="hljs-literal">-sh</span> views
<span class="hljs-comment"># 192K    views</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>7.3 mount 命令;  功能：使用mount命令就可在Linux中挂载各种文件系统</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">格式：<span class="hljs-built_in">mount</span> <span class="hljs-literal">-t</span>  设备名  挂载点

(<span class="hljs-number">1</span>) <span class="hljs-built_in">mount</span> /dev/sda1  /mnt/filetest
<span class="hljs-built_in">mount</span> <span class="hljs-literal">-t</span> vfat /dev/hda  /mnt/fatfile
<span class="hljs-built_in">mount</span> <span class="hljs-literal">-t</span> ntfs /dev/hda  /mnt/ntfsfile
<span class="hljs-built_in">mount</span> <span class="hljs-literal">-t</span> iso9660 /dev/cdrom  /mnt/cdrom
<span class="hljs-built_in">mount</span> <span class="hljs-literal">-o</span>  设备名 挂载点
(<span class="hljs-number">2</span>) 使用usb设备
modprobe usb<span class="hljs-literal">-storage</span>
mkdir /mnt/usb
<span class="hljs-built_in">mount</span> <span class="hljs-literal">-t</span> auto /dev/sdx1 /mnt/usb
umount /mnt/usb
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>7.4 mkswap 命令;  功能：使用 mkswap 命令可以创建 swap 空间</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">eg:
mkswap <span class="hljs-literal">-c</span> /dev/hda4
<span class="hljs-comment"># 启用新创建的swap空间，停用可使用swapoff命令</span>
swapon /dev/hda4 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>7.5 fdisk 命令;  功能：对磁盘进行分区</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">fdisk /dev/xxx       格式化xxx设备(xxx是指磁盘驱动器的名字，例如hdb，sdc)
fdisk <span class="hljs-literal">-l</span>             显示磁盘的分区表
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>7.6 mkfs 命令;  功能：格式化文件系统，可以指定文件系统的类型，如ext2、ext3、fat、ntfs等</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-literal">-b</span>    块大小
<span class="hljs-literal">-i</span>    节点大写
<span class="hljs-literal">-m</span>    预留管理空间大小
格式<span class="hljs-number">1</span>：mkfs.ext3 options /dev/xxx
格式<span class="hljs-number">2</span>：mkfs <span class="hljs-literal">-t</span> ext2 options /dev/xxx
eg:
mkfs.ext3 /dev/sdb1
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>7.7 e2fsck 命令;  功能：磁盘检测</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">e2fsck /dev/hda1　        检查/dev/hda1是否有文件系统错误，提示修复方式
e2fsck <span class="hljs-literal">-p</span> /dev/hda1　     检查/dev/hda1是否有错误，如果有则自动修复
e2fsck <span class="hljs-literal">-y</span> /dev/hda1　     检查错误，所有提问均于yes方式执行
e2fsck <span class="hljs-literal">-c</span> /dev/hda1　     检查磁盘是否有坏区
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>7.8 tune2fs 命令;  功能：调整ext2/ext3文件的参数</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell"><span class="hljs-literal">-l</span>     查看文件系统信息
<span class="hljs-literal">-c</span>     设置强制自检的挂载次数
<span class="hljs-literal">-i</span>     设置强制自检的间隔时间，单位天
<span class="hljs-literal">-m</span>     保留块的百分比
<span class="hljs-literal">-j</span>     将 ext2 文件系统转换成 ext3 格式
eg:
tune2fs <span class="hljs-literal">-l</span> /dev/sda1
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>7.9 dd 命令;  功能：把指定的输入文件拷贝到指定的输出文件中，并且在拷贝过程中可以进行格式转换</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">dd <span class="hljs-keyword">if</span> = /dev/fd0 of=floppy.img　将软盘的内容复制成一个镜像
dd <span class="hljs-keyword">if</span> = floppy.img of=/dev/fd0　将一个镜像的内容复制到软盘，做驱动盘的时候经常用。
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">8. 网络相关命令</h4>
<p><strong>8.1 ifconfig 命令; 功能：显示修改网卡的信息</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">ifconfig            显示网络信息
ifconfig eth0       显示eth0网络信息
修改网络信息：
ifconfig eth0 <span class="hljs-number">192.168</span>.<span class="hljs-number">1.1</span> netmask <span class="hljs-number">255.255</span>.<span class="hljs-number">255.0</span>   设置网卡<span class="hljs-number">1</span>的地址<span class="hljs-number">192.168</span>.<span class="hljs-number">1.1</span>，掩码为<span class="hljs-number">255.255</span>.<span class="hljs-number">255.0</span>
ifconfig eth0:<span class="hljs-number">1</span> <span class="hljs-number">192.168</span>.<span class="hljs-number">1.2</span>　                     捆绑网卡<span class="hljs-number">1</span>的第二个地址为<span class="hljs-number">192.168</span>.<span class="hljs-number">1.2</span>
ifconfig eth0:x <span class="hljs-number">192.168</span>.<span class="hljs-number">1</span>.n　                     捆绑网卡<span class="hljs-number">1</span>的第n个地址为<span class="hljs-number">192.168</span>.<span class="hljs-number">1</span>.n
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>8.2 route 命令; 功能：显示当前路由设置情况</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">route                          显示当前路由设置情况，比较慢一般不用。
route add <span class="hljs-literal">-net</span> <span class="hljs-number">10.0</span>.<span class="hljs-number">0.0</span> netmask <span class="hljs-number">255.255</span>.<span class="hljs-number">0.0</span> gw <span class="hljs-number">192.168</span>.<span class="hljs-number">1.254</span>          添加静态路由
route <span class="hljs-built_in">del</span> <span class="hljs-literal">-net</span> <span class="hljs-number">10.0</span>.<span class="hljs-number">0.0</span> netmask <span class="hljs-number">255.255</span>.<span class="hljs-number">0.0</span> gw <span class="hljs-number">192.168</span>.<span class="hljs-number">1.254</span>          添加静态路由
route add default gw <span class="hljs-number">192.168</span>.<span class="hljs-number">1.1</span> metric1　                            设置<span class="hljs-number">192.168</span>.<span class="hljs-number">1.1</span>为默认的路由
route <span class="hljs-built_in">del</span> default　                                                   将默认的路由删除
eg:
<span class="hljs-comment"># route add -net 10.0.0.0 netmask 255.255.0.0 gw 192.168.1.254</span>

<span class="hljs-comment"># netstat -nr</span>
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
<span class="hljs-number">192.168</span>.<span class="hljs-number">1.0</span>     <span class="hljs-number">0.0</span>.<span class="hljs-number">0.0</span>         <span class="hljs-number">255.255</span>.<span class="hljs-number">255.0</span>   U         <span class="hljs-number">0</span> <span class="hljs-number">0</span>          <span class="hljs-number">0</span> eth0
<span class="hljs-number">10.0</span>.<span class="hljs-number">0.0</span>        <span class="hljs-number">192.168</span>.<span class="hljs-number">1.254</span>   <span class="hljs-number">255.255</span>.<span class="hljs-number">0.0</span>     UG        <span class="hljs-number">0</span> <span class="hljs-number">0</span>          <span class="hljs-number">0</span> eth0
<span class="hljs-number">169.254</span>.<span class="hljs-number">0.0</span>     <span class="hljs-number">0.0</span>.<span class="hljs-number">0.0</span>         <span class="hljs-number">255.255</span>.<span class="hljs-number">0.0</span>     U         <span class="hljs-number">0</span> <span class="hljs-number">0</span>          <span class="hljs-number">0</span> eth0
<span class="hljs-number">0.0</span>.<span class="hljs-number">0.0</span>         <span class="hljs-number">192.168</span>.<span class="hljs-number">1.254</span>   <span class="hljs-number">0.0</span>.<span class="hljs-number">0.0</span>         UG        <span class="hljs-number">0</span> <span class="hljs-number">0</span>          <span class="hljs-number">0</span> eth0

<span class="hljs-comment"># route del -net 10.0.0.0 netmask 255.255.0.0 gw 192.168.1.254   </span>

<span class="hljs-comment"># netstat -nr</span>
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
<span class="hljs-number">192.168</span>.<span class="hljs-number">1.0</span>     <span class="hljs-number">0.0</span>.<span class="hljs-number">0.0</span>         <span class="hljs-number">255.255</span>.<span class="hljs-number">255.0</span>   U         <span class="hljs-number">0</span> <span class="hljs-number">0</span>          <span class="hljs-number">0</span> eth0
<span class="hljs-number">169.254</span>.<span class="hljs-number">0.0</span>     <span class="hljs-number">0.0</span>.<span class="hljs-number">0.0</span>         <span class="hljs-number">255.255</span>.<span class="hljs-number">0.0</span>     U         <span class="hljs-number">0</span> <span class="hljs-number">0</span>          <span class="hljs-number">0</span> eth0
<span class="hljs-number">0.0</span>.<span class="hljs-number">0.0</span>         <span class="hljs-number">192.168</span>.<span class="hljs-number">1.254</span>   <span class="hljs-number">0.0</span>.<span class="hljs-number">0.0</span>         UG        <span class="hljs-number">0</span> <span class="hljs-number">0</span>          <span class="hljs-number">0</span> eth0
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>8.3 netstat 命令; 功能：显示网络状态</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">netstat <span class="hljs-literal">-an</span>                   查看网络端口信息
netstat <span class="hljs-literal">-nr</span>                   查看路由表信息，比route快多了
netstat <span class="hljs-literal">-ntlp</span>|grep <span class="hljs-number">7007</span>       查看<span class="hljs-number">7007</span>端口信息
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>8.4 启动网络的命令; 功能：显示网络状态</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">redhat族的命令: /etc/init.d/network
debian命令: /etc/init.d/networking
eg:
/etc/init.d/network stop     停止网络
/etc/init.d/network <span class="hljs-built_in">start</span>    启动网络
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>8.5 网络排错</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">(<span class="hljs-number">1</span>) ping命令
(<span class="hljs-number">2</span>) traceroute命令; 功能：路由跟踪
traceroute
traceroute <span class="hljs-number">207.68</span>.<span class="hljs-number">173.7</span>
(<span class="hljs-number">3</span>)nslookup命令; 功能：域名解析排错
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">9. 其他命令</h4>
<p><strong>9.1 ssh 命令; 功能：远程登陆到其他UNIX主机</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">ssh <span class="hljs-literal">-l</span> user1 <span class="hljs-number">192.168</span>.<span class="hljs-number">1.2</span>     使用用户名user1登陆到<span class="hljs-number">192.168</span>.<span class="hljs-number">1.2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>9.2 scp 命令; 功能：安全copy</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">scp abc.tar.gz    将本地的 abc.tar.gz 复制到 <span class="hljs-number">192.168</span>.<span class="hljs-number">1.5</span>的 user1 用户的根(/home/user1)下。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>9.3  telnet命令; 功能：登陆到远程主机</strong></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">eg:
telnet <span class="hljs-number">192.168</span>.<span class="hljs-number">1.5</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            