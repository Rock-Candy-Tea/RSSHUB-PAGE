
---
title: 'Shell环境变量'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4ac43fb0199425cbaf1220e34378384~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 24 May 2021 22:05:06 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4ac43fb0199425cbaf1220e34378384~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">关于Shell</h1>
<p>为了能对<code>shell</code>能够有整体的认识，我们需要先简单介绍下<code>Linux</code>系统 。</p>
<h2 data-id="heading-1">Linux系统</h2>
<p><code>Linux</code>系统主要分四部分：</p>
<ol>
<li><code>Linux</code>内核</li>
<li><code>GNU</code>工具</li>
<li>图形桌面化环境</li>
<li>应用软件</li>
</ol>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4ac43fb0199425cbaf1220e34378384~tplv-k3u1fbpfcp-zoom-1.image" alt="Linux系统" loading="lazy" referrerpolicy="no-referrer">
<h3 data-id="heading-2">Linux内核</h3>
<p><code>Linux</code>内核主要负责以下四种功能：</p>
<ul>
<li>系统内存管理：物理内存、虚拟内存</li>
<li>软件程序管理：<code>Linux</code>操作系统将运行中的程序称为进程。内核控制着<code>Linux</code>系统如何管理运行在系统上的所有进程。内核创建了第一个进程(称为<code>init</code>进程)来启动系统上所有其他进程，<code>Linux</code>使用一个表来管理在系统开机时要自动启动的进程。<code>Linux</code>操作系统的<code>init</code>系统采用了运行级。运行级决定了<code>init</code>进程运行<code>/etc/inittab</code>文件或 <code>/etc/rcX.d</code>目录中定义好的某些特定类型的进程（<code>X</code>代表运行级）。<code>Linux</code>操作系统有5个启动运行级。每个启动运行级便是一种启动模式。</li>
<li>硬件设备管理：内核的另一职责是管理硬件设备。任何<code>Linux</code>系统需要与之通信的设备，都需要在内核代码中加入其驱动程序代码。驱动程序代码相当于应用程序和硬件设备的中间人，允许内核与设备之 间交换数据。</li>
<li>文件系统管理：不同于其他一些操作系统，<code>Linux</code>内核支持通过不同类型的文件系统从硬盘中读写数据。</li>
</ul>
<h3 data-id="heading-3">GNU</h3>
<p>操作系统用以执行一些标准功能，比如控制文件和程序的工具。<code>Linus</code>在创建<code>Linux</code>系统内核时，没有可用的系统工具。<code>GNU</code>是由<code>GNU</code>组织(<code>GNU</code>是<code>GNU’s Not Unix</code>的缩写)开发了一套完整的<code>Unix</code>工具，是开源的，但没有运行它们的内核系统。于是将<code>Linus</code>的<code>Linux</code>内核和<code>GNU</code>操作系统工具整合起来，就产生了一款完整的、功能丰富的免费操作系统：<code>GNU/Linux</code>系统（为了感谢<code>GNU</code>组织）也称：<code>Linux</code>系统。</p>
<p><code>GNU</code>分两部分，一部分为核心<code>GNU</code>工具（<code>core utilities</code>），由处理文件、操作文本、管理进程三部分工具包组成；另一部分便是<code>Shell</code>。</p>
<h2 data-id="heading-4">Shell简介</h2>
<p><code>Shell</code>是一种特殊的交互式工具。它为用户提供了启动程序、管理文件系统中的文件以及运行在<code>Linux</code>系统上的进程的途径。也就是<code>Shell</code>负责将命令行中输入的文本命令，进行解释，并传递到内核进行执行的工具，也可称解释器。</p>
<p><code>Shell</code>的核心是命令行提示符。命令行提示符是<code>Shell</code>负责交互的部分，它允许你输入文本命令，然后解释命令，并在内核中执行。将多个<code>shell</code>命令放入文件中作为程序执行，这个文件便被称为<code>Shell</code> 脚本。</p>
<p>在<code>Linux</code>系统上，通常有好几种<code>Linux shell</code>可用。不同的<code>shell</code>有不同的特性，有些更利于创建脚本，有些则更利于管理进程。所有<code>Linux</code>发行版（完整的<code>Linux</code>系统包）默认的<code>shell</code>都是<code>bash shell</code>。</p>
<p><code>bash shell</code>由<code>GNU</code>组织开发，被当作标准<code>Unix shell——Bourne shell</code>(以创建者的名字命名)的替代品。<code>bash shell</code>的名称就是针对<code>Bourne shell</code>的拼写所玩的一个文字游戏，称为<code>Bourne again shell</code>。总结：<code>sh</code>是标准，<code>bash</code>是<code>sh</code>的替代品。除了<code>bash shell</code>，<code>Linux</code>中常见的几种不同<code>shell</code>有：</p>
<ul>
<li><code>ash</code>：一种运行在内存受限环境中简单的轻量级<code>shell</code>，但与<code>bash shell</code>完全兼容。</li>
<li><code>korn</code>：一种与<code>Bourne shell</code>兼容的编程<code>shell</code>，但支持如关联数组和浮点运算等一些高级的编程特性。</li>
<li><code>tcsh</code>：一种将<code>C</code>语言中的一些元素引入到<code>shell</code>脚本中的<code>shell</code>。</li>
<li><code>zsh</code>：一种结合了<code>bash</code>、<code>tcsh</code>和<code>korn</code>的特性，同时提供高级编程特性、共享历史文件和主题化提示符的高级 <code>shell</code>。</li>
</ul>
<p>从 <code>macOS Catalina</code> 版开始，苹果的<code>Mac</code>系统将使用<code>zsh</code>作为默认登录<code> Shell</code> 和交互式 <code>Shell</code>。具体请看<a href="https://support.apple.com/kb/HT208050" target="_blank" rel="nofollow noopener noreferrer">官网</a>。</p>
<h1 data-id="heading-5">环境变量</h1>
<p>这一部分将基于<code>bash shell</code>展开陈述。</p>
<p><code>bash shell</code>中使用环境变量在内存中存储有关<code>shell</code>会话和工作环境的数据，以便程序或<code>shell</code>中运行的脚本能够访问到它们。</p>
<p><code>bash shell</code>中的环境变量主要有两种：全局变量与局部变量。查看系统中所有全局变量，可以使用<code>env</code>或<code>printenv</code>命令；要显示个别环境变量的值，可以使用<code>printenv</code>命令，但是不能用<code>env</code>命令。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#查看shell个别全局变量</span>
printenv HOME
<span class="hljs-comment">#查看shell个别全局变量：通过echo 以变量的形式输出</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$HOME</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>系统的环境都是大写，定义属于用户自己局部变量时统一使用小写，避免冲突。</p>
<h2 data-id="heading-6">定义局部变量</h2>
<p>定义形式如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash">variable=Hello
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$variable</span> <span class="hljs-comment">#输出：Hello</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>**重要：变量名、等号和值之间没有空格。**如果在赋值表达式中加上了空格， <code>bash shell</code>就会把值当成一个单独的命令，变量值有空格需要使用引号。</p>
<pre><code class="hljs language-bash copyable" lang="bash">variable=<span class="hljs-string">"Hello word"</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$variable</span> <span class="hljs-comment">#输出：Hello word</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">定义全局变量</h2>
<p>在设定全局环境变量的进程所创建的子进程中，该全局变量都是可见的；创建全局环境变量的方法是先创建一个局部环境变量，然后再把它导出到全局环境中；父<code>shell</code>定义的全局变量，子<code>shell</code>的修改不会影响父<code>shell</code>的值。示例如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash">variable=<span class="hljs-string">"global variable ~~~~"</span>
<span class="hljs-built_in">export</span> variable
<span class="hljs-comment">#开启子shell</span>
bash
<span class="hljs-comment">#子shell 输出一下</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$variable</span> <span class="hljs-comment">#global variable ~~~~</span>
<span class="hljs-comment">#子shell修改</span>
variable=<span class="hljs-string">"子shell修改"</span>
<span class="hljs-comment">#子shell 输出一下</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$variable</span> <span class="hljs-comment">#输出：子shell修改</span>
<span class="hljs-comment">#导出</span>
<span class="hljs-built_in">export</span> variable
<span class="hljs-comment">#退出子shell</span>
<span class="hljs-built_in">exit</span>
<span class="hljs-comment">#父shell输出</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$variable</span> <span class="hljs-comment">#子shell的修改不会影响父shell:global variable ~~~~</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">删除全局变量</h2>
<p>使用如下命令：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#删除</span>
<span class="hljs-built_in">unset</span> variable
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>需要注意的是在子<code>shell</code>中是无法删除父<code>shell</code>创建的全局变量。</strong></p>
<h2 data-id="heading-9">默认全局变量</h2>
<p>默认情况下，<code>bash shell</code>会用一些特定的环境变量来定义系统环境。这些变量在你的<code>Linux</code>系统上都已经设置好了，只管放心使用。<code>bash shell</code>源自当初的<code>Unix Bourne shell</code>，因此也保留了<code>Unix Bourne shell</code>里定义的那些环境变量。
列举几个比较常见的环境变量：</p>
<ul>
<li><code>CDPATH</code>：冒号分隔的目录列表，作为<code>cd</code>命令的搜索路径</li>
<li><code>HOME</code>：当前用户的主目录</li>
<li><code>PATH</code>：<code>shell</code>查找命令的目录列表，由冒号分隔</li>
<li><code>BASH</code>：当前<code>shell</code>实例的全路径名</li>
<li><code>PWD</code>：当前工作目录</li>
</ul>
<h1 data-id="heading-10">设置PATH变量</h1>
<p>当我们在<code>shell</code>命令行界面中输入一个外部命令时，<code>shell</code>必须搜索系统来找到对应的程序。<code>PATH</code>环境变量定义了用于进行命令和程序查找的目录：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#输出下</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$PATH</span>
<span class="hljs-comment">#结果</span>
/Users/*/.rvm/gems/ruby-2.3.0/bin:
/Users/*/.rvm/gems/ruby-2.3.0@global/bin:
/Users/*/.rvm/rubies/ruby-2.3.0/bin:
/Users/*/Desktop/development/flutter/bin:
/usr/<span class="hljs-built_in">local</span>/bin:
/usr/bin:
/bin:
/usr/sbin:
/sbin:
/Users/*/.rvm/bin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出的结果中显示了有10个可供shell用来查找命令和程序的路径。<code>PATH</code>中的目录使用冒号分隔。这些路径下分别都存放了不同的命令和程序，举个<code>/bin</code>的示例：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/877c9eccd1174df7ab2bdd4d4a9590fa~tplv-k3u1fbpfcp-zoom-1.image" alt="/bin目录下的程序与命令" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果命令或者程序的路径没有包括在<code>PATH</code>变量中，则不使用绝对路径的情况下，<code>shell</code>是没法找到该程序的。</p>
<p>**问题：**应用程序放置可执行文件的目录常常不在<code>PATH</code>环境变量所包含的目录中。</p>
<p>**解决：**是保证<code>PATH</code>环境变量包含了所有存放应用程序的目录。可以把新的搜索目录添加到现有的<code>PATH</code>环境变量中，无需从头定义。<code>PATH</code>中各个目录之间是用冒号分隔的，我们只需要引用原来的<code>PATH</code>值，然后再给这个字符串添加新目录就行了。</p>
<p>举例终端启用<code>flutter</code>命令：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#查看path</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$PATH</span>
<span class="hljs-comment">#结果不包含：/Users/*/Desktop/development/flutter/bin:</span>
<span class="hljs-comment">#通过终端启用</span>
PATH=<span class="hljs-variable">$PATH</span>:~/Desktop/development/flutter/bin
<span class="hljs-comment">#再次查看</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$PATH</span>
<span class="hljs-comment">#结果包含：/Users/*/Desktop/development/flutter/bin:</span>
<span class="hljs-comment">#执行flutter</span>
flutter -v
<span class="hljs-comment">#不再提示找不到命令。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>值得注意的是：对<code>PATH</code>变量的修改只能持续到退出或重启终端系统。这种效果并不能一直持续。如何让这种效果持续？</p>
<p>为了解决这个问题，我们需要了解一些关于定位环境变量的知识。</p>
<p>在我们登入<code>Linux</code>系统启动一个<code>bash shell</code>时，默认情况下<code>bash</code>会在几个文件中查找命令。这些文件叫作<strong>启动文件或环境文件</strong>。<strong><code>bash</code>检查的启动文件取决于你启动<code>bash shell</code>的方式</strong>。启动<code>bash shell</code>有<code>3</code>种方式：</p>
<ul>
<li>登录时作为默认登录<code>shell</code></li>
<li>作为非登录<code>shell</code>的交互式<code>shell</code></li>
<li>作为运行脚本的非交互<code>shell</code></li>
</ul>
<h2 data-id="heading-11">默认登录shell</h2>
<p>当我们登录<code>Linux</code>系统时，<code>bash shell</code>会作为登录<code>shell</code>启动。登录<code>shell</code>会从5个不同的启动文件里读取命令：</p>
<ol>
<li><code>/etc/profile</code></li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#/etc/profile启动文件内容</span>

<span class="hljs-comment"># System-wide .profile for sh(1)</span>

<span class="hljs-keyword">if</span> [ -x /usr/libexec/path_helper ]; <span class="hljs-keyword">then</span>
<span class="hljs-built_in">eval</span> `/usr/libexec/path_helper -s`
<span class="hljs-keyword">fi</span>

<span class="hljs-keyword">if</span> [ <span class="hljs-string">"<span class="hljs-variable">$&#123;BASH-no&#125;</span>"</span> != <span class="hljs-string">"no"</span> ]; <span class="hljs-keyword">then</span>
[ -r /etc/bashrc ] && . /etc/bashrc
<span class="hljs-keyword">fi</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><code>$HOME/.bash_profile</code></li>
<li><code>$HOME/.bashrc</code></li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#macOS系统中.bashrc启动文件内容,非登录的交互式shell会以此为启动文件的。</span>
<span class="hljs-built_in">export</span> PATH=<span class="hljs-string">"<span class="hljs-variable">$PATH</span>:<span class="hljs-variable">$HOME</span>/.rvm/bin"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li><code>$HOME/.bash_login</code></li>
<li><code>$HOME/.profile</code></li>
</ol>
<p><code>/etc/profile</code>文件是系统上默认的<code>bash shell</code>的主启动文件。系统上的每个用户登录时都会执行这个启动文件。另外<code>4</code>个启动文件是针对用户的，提供一个用户专属的启动文件来定义该用户所用到的环境变量，可根据个人需求定制，且都是隐藏文件。它们位于用户的<code>HOME</code>目录下，所以每个用户都可以编辑这些文件并添加自己的环境变 量，这些环境变量会在每次启动<code>bash shell</code>会话时生效。其中<code>2</code>和<code>5</code>我们在<code>macOS</code>中是比较熟悉的。</p>
<p><code>shell</code>会按照下列顺序，运行第一个被找到的文件，余下的则被忽略（不会重复）:
<code>$HOME/.bash_profile</code>=><code>$HOME/.bash_login</code>=><code>$HOME/.profile</code> 注：<code>$HOME</code>和波浪号<code>~</code>作用一样，都代表用户目录。正是因为此规则的存在，我们有些时候只需要在<code>$HOME/.profile</code>中配置我们的<code>PATH</code>即可。</p>
<h2 data-id="heading-12">非登录的交互式shell</h2>
<p>不是登录时启动的<code>shell</code>称为交互式<code>shell</code>。比如：在命令行提示符下敲入<code>bash</code>时启动。
当<code>bash</code>是作为交互式<code>shell</code>启动，则不会访问<code>/etc/profile</code>文件，只会检查用户目录<code>$HOME</code>下的<code>.bashrc</code>文件。</p>
<h2 data-id="heading-13">运行脚本的非交互shell</h2>
<p>非交互shell，系统执行<code>shell</code>脚本时会使用。不同的地方在于它没有命令行提示符。但是当我们在系统上运行脚本时，可能希望运行一些特定启动的命令。为了处理这种情况，<code>bash shell</code>提供了<code>BASH_ENV</code>环境变量。当<code>shell</code>启动一个非交互式<code>shell</code>进程时，它会检查这个环境变量来查看要执行的启动文件。</p>
<p>在<code>macOS</code>系统下运行<code>echo $BASH_ENV</code>查看，这个环境变量并未被设置。如果<code>BASH_ENV</code>变量没有设置，<code>shell</code>脚本如何获得它们的环境变量呢？</p>
<ul>
<li>子<code>shell</code>可以继承父<code>shell</code>到处的环境变量；但需要注意的是父<code>shell</code>中设置但却未<code>export</code>的变量，属于局部变量，子<code>shell</code>是无法获取的。也就是说执行脚本时，采用<code>bash</code>命令开启子<code>shell</code>便可以解决这个问题。</li>
<li>不启动子<code>shell</code>的脚本，变量已经存在于当前<code>shell</code>中。</li>
</ul>
<h2 data-id="heading-14">环境变量持久化</h2>
<p>在<code>Linux</code>在大多数发行版中，存储个人用户永久性<code>bash shell</code>变量的地方是<code>$HOME/.bashrc</code>文件。这一 点适用于所有类型的<code>shell</code>进程。但如果设置了<code>BASH_ENV</code>变量，那么除非<code>BASH_ENV</code>指向的是 <code>$HOME/.bashrc</code>，否则应该将非交互式<code>shell</code>的用户变量放在别的地方。</p>
<p>在<code>macOS</code>系统中，存储个人用户永久性<code>bash shell</code>变量的地方，便是对应的环境文件：<code>~/.profile</code>、<code>~/.bash_profile</code>、<code>~/.bashrc</code>（交互式<code>shell</code>生效）。其中<code>~/.profile</code>和<code>~/.bash_profile</code>任意一个都可以定义我们的永久性<code>bash shell</code>变量。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#在`~/.profile`文件中定义</span>
<span class="hljs-built_in">export</span> LOVE=<span class="hljs-string">"全局可用的环境变量love"</span>
PEACE=<span class="hljs-string">"局部环境变量，子shell不可用"</span>
<span class="hljs-comment">#在`~/.bash_profile`文件中定义</span>
<span class="hljs-built_in">export</span> SHARE=<span class="hljs-string">"全局可用的环境变量share"</span>
QI=<span class="hljs-string">"局部环境变量，子shell不可用"</span>
<span class="hljs-comment">#终端shell，查看全局变量</span>
env
<span class="hljs-comment">#输出</span>
LOVE=全局可用的环境变量love
SHARE=全局可用的环境变量share
<span class="hljs-comment">#终端shell，查看永久局部变量</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$PEACE</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$QI</span>
<span class="hljs-comment">#输出</span>
局部环境变量，子shell不可用
<span class="hljs-comment">#开启非登陆交互式shell</span>
bash
<span class="hljs-comment">#子shell，查看可用全局变量</span>
env
<span class="hljs-comment">#输出</span>
LOVE=全局可用的环境变量love
SHARE=全局可用的环境变量share
<span class="hljs-comment">#子shell，查看可用的父Shell的局部变量</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$PEACE</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$QI</span>
<span class="hljs-comment">#输出为空</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于<code>~/.bashrc</code>，作为非登录式交互<code>shell</code>的启动文件，仅对非登录式交互<code>shell</code>生效：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#在`~/.bashrc`配置</span>
<span class="hljs-built_in">export</span> CHILD=<span class="hljs-string">"子shell可用"</span>
<span class="hljs-comment">#重新打开终端，输入</span>
env
<span class="hljs-comment">#or</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$CHILD</span>
<span class="hljs-comment">#都输出：空</span>
 
<span class="hljs-comment">#开启子shell（交互式shell）</span>
bash
<span class="hljs-comment">#查看子shell的全局变量</span>
env 
<span class="hljs-comment">#or</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$CHILD</span>
<span class="hljs-comment">#输出</span>
CHILD=子shell可用
子shell可用
<span class="hljs-comment">#再次开启子shell</span>
bash
<span class="hljs-comment">#输入</span>
env 
<span class="hljs-comment">#or</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$CHILD</span>
<span class="hljs-comment">#输出</span>
CHILD=子shell可用
子shell可用
<span class="hljs-comment">#如果`~/.bashrc`文件中配置</span>
CHILD=<span class="hljs-string">"子shell可用"</span>
<span class="hljs-comment">#输入</span>
env
<span class="hljs-comment">#输出：空</span>
<span class="hljs-comment">#输入</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$CHILD</span>
<span class="hljs-comment">#输出</span>
子shell可用
<span class="hljs-comment">#再次开启子shell，`CHILD`变量将不再生效</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">数组变量</h2>
<p>数组变量：环境变量设置多个值，放置在括号中，且值与值之间用空格隔开。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#定义数组变量</span>
ARRAY_VAR=(one two three)
<span class="hljs-comment">#输出数组变量</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$ARRAY_VAR</span>
<span class="hljs-comment">#不会全部输出，只会输出数组变量中第一个元素</span>
one
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要引用数组变量中的某个元素，就必须用代表它在数组中位置的数值索引值。索引值要用方括号括起来：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">echo</span> <span class="hljs-variable">$&#123;ARRAY_VAR[2]&#125;</span>
<span class="hljs-comment">#输出</span>
three
<span class="hljs-comment">#显示整个数组</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$&#123;ARRAY_VAR[*]&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以用<code>unset</code>命令删除数组中的某个值，但是要小心。比如：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#删除索引为1的元素</span>
<span class="hljs-built_in">unset</span> ARRAY_VAR[1]
<span class="hljs-comment">#输出整个数组</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$&#123;ARRAY_VAR[*]&#125;</span>
<span class="hljs-comment">#删除成功</span>
one three
<span class="hljs-comment">#输出数组中索引为1的元素</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$&#123;ARRAY_VAR[1]&#125;</span>
<span class="hljs-comment">#结果为：空</span>

<span class="hljs-comment">#输出索引为2的元素</span>
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$&#123;ARRAY_VAR[2]&#125;</span>
<span class="hljs-comment">#结果</span>
3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参考资料：
Linux命令行与shell脚本编程大全</p></div>  
</div>
            