
---
title: '使用 makefile 压缩 JavaScript 代码'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3783'
author: 掘金
comments: false
date: Sat, 01 May 2021 23:44:13 GMT
thumbnail: 'https://picsum.photos/400/300?random=3783'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、makefile 初探</h2>
<h3 data-id="heading-1">1.  什么是 make指令 和 makefile？</h3>
<p>make 指令就像它的名字一样 ，用于制作某个文件（<code>make filename</code>），或者根据 <code>makefile target</code> 自动化编译、打包、生成一个文件（可执行文件或压缩文件）。</p>
<p>例如，我们想根据 <code>a.txt</code> 和 <code>b.txt</code> 文件合成 <code>output.txt</code> 文件，可以书写如下 makefile 文件：</p>
<pre><code class="hljs language-makefile copyable" lang="makefile"><span class="hljs-section">output.txt: a.txt b.txt</span>
@<span class="hljs-comment"># 根据 a.txt b.txt 文件合成 output.txt 文件</span>
@cat a.txt b.txt > output.txt
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 制作 output.txt 文件</span>
make output.txt
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通常我们用 make 指令构建 c/c++ 项目，当然，我们也可以用 make 指令构建 go 语言项目、java项目及 node.js 项目。</p>
<p>例如，我们用 make 指令编译 hello.cpp 文件</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><iostream></span></span>
<span class="hljs-keyword">using</span> <span class="hljs-keyword">namespace</span> std;
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span>&#123;
   cout << <span class="hljs-string">"Hello World!"</span>;
   <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>makefile 文件：</p>
<pre><code class="hljs language-makefile copyable" lang="makefile"><span class="hljs-section">hellocpp:hello.o</span>
echo <span class="hljs-string">"开始编译"</span>
g++ -o hello hello.o
rm -f hello.o
echo <span class="hljs-string">"编译结束"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 make 指令</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 使用 makefile 执行 hello.cpp</span>
make
<span class="hljs-meta">
#</span><span class="bash"> 执行生成的 hello文件</span>
./hello
<span class="hljs-meta">></span><span class="bash"> Hello World!</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>没玩过 makefile 的同学肯定以为 makefile 和 shell 脚本很像，没错，makefile 确实可以当做 shell 脚本使用（bushi），接下来我就简单介绍一下 makefile 的基本规则和常见写法。</p>
<h3 data-id="heading-2">2、makefile 的结构</h3>
<p>makefile 文件是由一系列的规则（rules） 组成的，每条规则的写法如下：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><target> : <prerequisites> 
[tab]  <commands>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，冒号前面的部分表示目标（target），表示执行的动作。目标可以是一个文件名（如上文中的 output.txt），也可以是多个文件名，中间用空格隔开。目标除了是文件名，也可以是操作名，这种在 makefile 中，叫伪目标（phony target），用 <code>.PHONY</code> 声明目标操作。</p>
<blockquote>
<p>如果我们想执行 <code>make clean</code> 操作，但是恰好目录中有一个 clean 的文件，那么我们在执行 make clean 的时候，是不会触发 clean 操作的，这个时候我们就要用 <code>.PHONY</code> 声明伪目标</p>
<pre><code class="hljs language-makefile copyable" lang="makefile">.PHONY clean
<span class="hljs-section">clean: </span>
rm -f *.o
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<p>我们在 makefile 中一般有一些约定俗成的目标，如：</p>
<ul>
<li>make all：编译所有文件</li>
<li>make install：安装编译好的应用程序</li>
<li>make clean：清理应用程序，可执行文件，目标文件等。</li>
</ul>
<p>冒号后面的部分表示前置条件（prerequisites），之间用空格分隔。声明的目标指定了前置条件，如果没有该前置条件匹配的文件，那么就要先生成该前置条件所需要的文件，才能执行目标。</p>
<p>命令（commands）表示如何构建目标文件，每个命令前必须以 tab 开头，可以和 prerequisites 写在一行，不过要用分号做分隔。</p>
<p>前置条件和命令为非必填项，不过其中一个没写另一个就必须要写。</p>
<p>makefile 里主要包含了五个东西：</p>
<ul>
<li>变量的定义</li>
<li>显式规则：根据上文的 target-prerequisites-commands 的书写方式，就是显示规则</li>
<li>隐晦规则：由于 makefile 具有自动推到的功能，所以隐晦规则可以让我们粗糙的书写makefile。用makefile 内置的变量和函数编写的规则就是隐晦规则。</li>
<li>文件指示：可以用 include 指令嵌套引入 makefile</li>
<li>注释</li>
</ul>
<p>变量的定义一般都是字符串，和C语言中的宏比较类似，所以我们有的时候也管makefile中的变量称作宏。</p>
<p>和 vue 的差值模板以及 shell、php 的变量一样，我们一般用<code>$&#123;VARIABLE&#125;</code> 或 <code>$(VARIABLE)</code> 的方式去使用一个变量。</p>
<p>在 makefile 中，变量有四种声明方式：</p>
<pre><code class="hljs language-bash copyable" lang="bash">VARIABLE = value <span class="hljs-comment"># 惰性赋值，在执行时扩展，可以递归扩展</span>

VARIABLE := value <span class="hljs-comment"># 立即赋值</span>

VARIABLE ?= value <span class="hljs-comment"># 只有在该变量为空时才设置值</span>

VARIABLE += value <span class="hljs-comment"># 将值追加到变量的尾端</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这四种赋值方式的具体区别可以查看 <a href="https://stackoverflow.com/questions/448910/what-is-the-difference-between-the-gnu-makefile-variable-assignments-a" target="_blank" rel="nofollow noopener noreferrer">Stack Overflow</a>，因为这四种赋值方式的区别不是本文讨论的重点，所以我就不过多赘述。</p>
<p>除了用户声明的变量外，makefile 中还有内置变量和自动变量。</p>
<p>内置变量分为两类，作为程序名称的变量（如CC），包含程序参数的变量（如CFLAGS）。关于makefile 所有的内置变量可以查看<a href="https://www.gnu.org/software/make/manual/html_node/Implicit-Variables.html" target="_blank" rel="nofollow noopener noreferrer">官方文档</a>。</p>
<p>自动变量的值与当前的规则有关。</p>
<p>一般常用的有以下几个：</p>
<ul>
<li><code>$@</code>：当前目标</li>
<li><code>$?</code>：比目标更新的前置条件</li>
<li><code>$<</code>：第一个前置条件</li>
<li><code>$*</code>：与通配符匹配的部分</li>
<li><code>$^</code>：所有前置条件</li>
<li><code>$(@D)</code>和<code>$(@F)</code>：<code>$@</code> 的目录名和文件名</li>
<li><code>$(<D)</code>和<code>$(<F)</code>：<code>$<</code> 的目录名和文件名</li>
</ul>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="normal">@</mi><mtext>指代的是当前的目标文件，如下面这个例子中，</mtext></mrow><annotation encoding="application/x-tex">@ 指代的是当前的目标文件，如下面这个例子中，</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord">@</span><span class="mord cjk_fallback">指</span><span class="mord cjk_fallback">代</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">是</span><span class="mord cjk_fallback">当</span><span class="mord cjk_fallback">前</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">目</span><span class="mord cjk_fallback">标</span><span class="mord cjk_fallback">文</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">如</span><span class="mord cjk_fallback">下</span><span class="mord cjk_fallback">面</span><span class="mord cjk_fallback">这</span><span class="mord cjk_fallback">个</span><span class="mord cjk_fallback">例</span><span class="mord cjk_fallback">子</span><span class="mord cjk_fallback">中</span><span class="mord cjk_fallback">，</span></span></span></span></span>@ 就表示 a.txt 和 b.txt 两个目标文件的文件名；</p>
<pre><code class="hljs language-makefile copyable" lang="makefile"><span class="hljs-comment"># 下面两种写法等价</span>
<span class="hljs-comment"># 写法一</span>
a.txt b.txt: 
    touch <span class="hljs-variable">$@</span>
<span class="hljs-comment"># 写法二</span>
<span class="hljs-section">a.txt:</span>
    touch a.txt
<span class="hljs-section">b.txt:</span>
    touch b.txt
<span class="copy-code-btn">复制代码</span></code></pre>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo><</mo><mtext>表示第一个前置条件，如下面这个例子中，</mtext></mrow><annotation encoding="application/x-tex">< 表示第一个前置条件，如下面这个例子中，</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.5782em;vertical-align:-0.0391em;"></span><span class="mrel"><</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord cjk_fallback">表</span><span class="mord cjk_fallback">示</span><span class="mord cjk_fallback">第</span><span class="mord cjk_fallback">一</span><span class="mord cjk_fallback">个</span><span class="mord cjk_fallback">前</span><span class="mord cjk_fallback">置</span><span class="mord cjk_fallback">条</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">如</span><span class="mord cjk_fallback">下</span><span class="mord cjk_fallback">面</span><span class="mord cjk_fallback">这</span><span class="mord cjk_fallback">个</span><span class="mord cjk_fallback">例</span><span class="mord cjk_fallback">子</span><span class="mord cjk_fallback">中</span><span class="mord cjk_fallback">，</span></span></span></span></span>< 就表示 b.txt</p>
<pre><code class="hljs language-makefile copyable" lang="makefile"><span class="hljs-comment"># 下面两种写法等价</span>
<span class="hljs-comment"># 写法一</span>
<span class="hljs-section">a.txt: b.txt c.txt</span>
    cp <span class="hljs-variable">$<</span> <span class="hljs-variable">$@</span> 
<span class="hljs-comment"># 写法二</span>
<span class="hljs-section">a.txt: b.txt c.txt</span>
    cp b.txt a.txt 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了内置变量和自动变量，makefile 还可以使用内置函数，使用方法和变量一样。<a href="https://www.gnu.org/software/make/manual/html_node/Functions.html" target="_blank" rel="nofollow noopener noreferrer">官方文档</a>总共列举了总共14种函数，常用的主要有以下几种：</p>
<ul>
<li>shell，shell 函数可以执行shell 命令，个人觉得和 shell 里的管道作用很像。例如 <code>dir:=$(shell pwd)</code></li>
<li>subst，用于文本替换，用法如下：<code>$(subst from,to,text)</code></li>
<li>patsubst，patsubst 函数用于模式匹配的替换，主要用于替换通配符。用法为 <code>$(patsubst pattern,replacement,text)</code> 。例如 <code>$(patsubst %.c,%.o,a.c.c b.c)</code> 可以将 a.c.c 和 b.c 替换成 a.c.o 和 b.o。</li>
<li>wildcard，wildcard 函数可以用空格分格所有匹配此格式的文件列表。例如，<code>$(wildcard *.c)</code> 可以获取工作目录下的所有的*.c*文件列表。</li>
</ul>
<p>makefile 还有一些其他的语法需要值得注意：</p>
<p><strong>回声：@</strong></p>
<p>正常情况下，make 在执行的过程中会打印每条 command，包括注释，这种现象在 makefile 中叫做回声。如果不想打印回声的话，可以用 <code>@</code> 操作符来关闭回声。如：</p>
<pre><code class="hljs language-makefile copyable" lang="makefile">@<span class="hljs-comment"># 关闭注释</span>
<span class="hljs-section">test:</span>
@echo <span class="hljs-string">"编译中。。。"</span>
@npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>通配符（wildcard）</strong></p>
<p>make 的通配符和 shell 一样，主要有<code>*</code>、<code>?</code>。</p>
<p><strong>模式匹配</strong></p>
<p>make 的模式匹配主要的操作符是<code>%</code>，允许对文件名进行类似正则的匹配</p>
<p><strong>注释</strong></p>
<p>makefile 的注释和 shell 脚本l 一样，都是 <code>#</code></p>
<p><strong>循环和判断指令</strong></p>
<p>makefile的循环判断指令和 shell 脚本一样，主要有以下几种：</p>
<ul>
<li><strong>ifeq</strong> （if eqaul）指令。它包含两个参数，用逗号分隔并用圆括号包围。变量替换在两个参数上执行，然后进行比较。如果两个参数匹配，则遵循 ifeq 后面的命令行；否则会被忽略。</li>
<li><strong>ifneq</strong> （if not eqaul）指令。它包含两个参数，用逗号分隔并用圆括号包围。变量替换在两个参数上执行，然后进行比较。如果两个参数不匹配，则遵循ifneq后面的makefile行；否则会被忽略。</li>
<li><strong>ifdef</strong> （if defined）指令。它包含单个参数。如果给定的参数为真，则条件成立。</li>
<li><strong>ifndef</strong> （if not defined）指令。它包含单个参数。如果给定的参数为假，则条件成立。</li>
<li><strong>else</strong> 指令。</li>
<li><strong>endif</strong> 指令结束的语句，每个 if 条件必须以 endif 结尾。</li>
<li><strong>for-in-do-done</strong>，循环</li>
</ul>
<p><strong>include 指令</strong></p>
<p>include 指令可以引入其他的 makefile 文件。语法如下</p>
<pre><code class="hljs language-makefile copyable" lang="makefile"><span class="hljs-keyword">include</span> <filename>
<span class="hljs-comment"># 文件名可以包含 shell 格式的文件名匹配。额外的空格是允许的，并且在行的开始处被忽略，但不允许使用制表符 tab（\t）</span>

<span class="hljs-keyword">-include</span> <filename>
<span class="hljs-comment"># 无论include过程中出现什么错误，都不要报错继续执行。上面那条指令若是找不到include的目标文件，会报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>override 指令</strong></p>
<p>如果想要重新赋值一个变量，则要使用 override 指令。如</p>
<pre><code class="hljs language-makefile copyable" lang="makefile"><span class="hljs-keyword">override</span> VARIABLE = value
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">二、使用 make 构建 JavaScript 代码</h2>
<p>前面已经简单介绍了下 make 的用法及 makefile 的一些规则，接下来我们讲一讲如何用 make 压缩 JavaScript 代码。</p>
<p>废话不多说，直接上代码：</p>
<pre><code class="hljs language-makefile copyable" lang="makefile">src_files := <span class="hljs-variable">$(<span class="hljs-built_in">shell</span> find src -name '*.js')</span>
dist_files := <span class="hljs-variable">$(<span class="hljs-built_in">patsubst</span> src/%.js, dist/%.min.js, <span class="hljs-variable">$(src_files)</span>)</span>

<span class="hljs-section">node_modules: package.json package-lock.json</span>
@npm i uglifyjs 

<span class="hljs-variable">$(dist_files)</span>: <span class="hljs-variable">$(src_files)</span>
@rm -rf dist
@mkdir dist
@npx uglifyjs <span class="hljs-variable">$^</span> -cmo <span class="hljs-variable">$@</span>

<span class="hljs-section">all: node_modules <span class="hljs-variable">$(dist_files)</span> </span>

<span class="hljs-meta"><span class="hljs-meta-keyword">.PHONY</span>: all</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了方便测试，我们用零宽空格测试文件是否压缩成功。</p>
<p>在根目录下新建 src 目录，并新建 app.js 文件，文件内容为如下代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">​​​​​​​​​​​​​​​​​​a​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然在编辑器中，只显示一个字符a，但是该字符串的长度却是 221，文件大小是 601 字节。这是由零宽字符导致的。</p>
<p>那么什么是零宽字符（zero-width space）呢？</p>
<p>用多个字节表示的字符称之为宽字符，我们常见的 Unicode 编码就是宽字符的一种实现，但是宽字符并不一定是 Unicode。</p>
<p>零宽字符，顾名思义，就是宽度为0的字符。零宽字符在浏览器等环境是不可见的，但却是真是存在的，获取字符长度时也占有长度。常用于防止爬虫，数据隐写，也可以用于 DOS 攻击。</p>
<p>以下为浏览器中常见的特殊字符：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">零宽空格（zero-width space, ZWSP）用于可能需要换行处。
    <span class="hljs-attr">Unicode</span>: U+200B  HTML: &#<span class="hljs-number">8203</span>;
零宽不连字 (zero-width non-joiner，ZWNJ)放在电子文本的两个字符之间，抑制本来会发生的连字，而是以这两个字符原本的字形来绘制。
    <span class="hljs-attr">Unicode</span>: U+200C  HTML: &#<span class="hljs-number">8204</span>;
零宽连字（zero-width joiner，ZWJ）是一个控制字符，放在某些需要复杂排版语言（如阿拉伯语、印地语）的两个字符之间，使得这两个本不会发生连字的字符产生了连字效果。
    <span class="hljs-attr">Unicode</span>: U+200D  HTML: &#<span class="hljs-number">8205</span>;
左至右符号（Left-to-right mark，LRM）是一种控制字符，用于计算机的双向文稿排版中。
    <span class="hljs-attr">Unicode</span>: U+200E  HTML: &lrm; &#x200E; 或&#<span class="hljs-number">8206</span>;
右至左符号（Right-to-left mark，RLM）是一种控制字符，用于计算机的双向文稿排版中。
    <span class="hljs-attr">Unicode</span>: U+200F  HTML: &rlm; &#x200F; 或&#<span class="hljs-number">8207</span>;
字节顺序标记（byte-order mark，BOM）常被用来当做标示文件是以UTF-<span class="hljs-number">8</span>、UTF-<span class="hljs-number">16</span>或UTF-<span class="hljs-number">32</span>编码的标记。
    <span class="hljs-attr">Unicode</span>: U+FEFF
<span class="copy-code-btn">复制代码</span></code></pre>
<p>知道了零宽字符的含义后，我们来测试 JavaScript 的压缩功能。</p>
<p>在终端输入 <code>make all</code> 指令，打开生成的 dist 目录，查看 app.min.js 文件，发现大小被压缩到 2个字节了。</p>
<p>上面只是简单列举了用 makefile 构建前端项目的例子，在实际开发中，我们可以使用 <code>make -j</code> 开启多线程来提升我们的构建速度，但是在现代的前端构建程序上，如 webpack、rollup，我们也可以使用多进程提升我们的打包速度（如 thread-loader）。所以这里建议大家，在实际的开发场景中，最好用同构的代码来构建我们的项目。</p>
<p>代码晚些时间会长传至 Github。</p></div>  
</div>
            