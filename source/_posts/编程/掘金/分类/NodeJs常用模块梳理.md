
---
title: 'NodeJs常用模块梳理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5002'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 01:28:02 GMT
thumbnail: 'https://picsum.photos/400/300?random=5002'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">path</h4>
<p>是node中的内置模块，可以直接使用require将它导入，他的主要作用就是处理文件的目录和路径。只需要调用不同的方法。path相当于一个工具箱，只需要掌握它里面提供的工具，也就是方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>basename(); 获取路径中基础名称</p>
<pre><code class="hljs language-js copyable" lang="js">path.basename(__filename); <span class="hljs-comment">// test.js</span>
<span class="hljs-comment">// 传入第二个参数如果匹配会省略后缀，不匹配仍旧返回真实的后缀</span>
path.basename(__filename, <span class="hljs-string">'.js'</span>); <span class="hljs-comment">// test</span>
path.basename(<span class="hljs-string">'/a/b/c'</span>); <span class="hljs-comment">// c</span>
path.basename(<span class="hljs-string">'/a/b/c/'</span>); <span class="hljs-comment">// c</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>dirname(); 获取路径中的目录名称</p>
<pre><code class="hljs language-js copyable" lang="js">path.dirname(__filename); <span class="hljs-comment">// d:\Desktop\test</span>
path.dirname(<span class="hljs-string">'/a/b/c'</span>); <span class="hljs-comment">// /a/b</span>
path.basename(<span class="hljs-string">'/a/b/c/'</span>); <span class="hljs-comment">// /a/b</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>extname(); 获取路径中的扩展名称</p>
<pre><code class="hljs language-js copyable" lang="js">path.extname(__filename); <span class="hljs-comment">// .js</span>
path.extname(<span class="hljs-string">'/a/b'</span>); <span class="hljs-comment">//</span>
path.extname(<span class="hljs-string">'/a/b/index.html.js.css'</span>); <span class="hljs-comment">// .css</span>
path.extname(<span class="hljs-string">'/a/b/index.html.js.'</span>); <span class="hljs-comment">// .</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>isAbsolute(); 获取路径是否是绝对路径</p>
<pre><code class="hljs language-js copyable" lang="js">path.isAbsolute(<span class="hljs-string">'a'</span>); <span class="hljs-comment">// false</span>
path.isAbsolute(<span class="hljs-string">'/a'</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>join(); 拼接多个路径片段，还原成完整可用路径</p>
<pre><code class="hljs language-js copyable" lang="js">path.join(<span class="hljs-string">'a/b'</span>, <span class="hljs-string">'c'</span>, <span class="hljs-string">'index.html'</span>); <span class="hljs-comment">// a/b/c/index.html</span>
path.join(<span class="hljs-string">'/a/b'</span>, <span class="hljs-string">'c'</span>, <span class="hljs-string">'index.html'</span>); <span class="hljs-comment">// /a/b/c/index.html</span>
path.join(<span class="hljs-string">'a/b'</span>, <span class="hljs-string">'c'</span>, <span class="hljs-string">'../'</span>, <span class="hljs-string">'index.html'</span>); <span class="hljs-comment">// a/b/index.html</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>resove(); 返回一个绝对路径</p>
<pre><code class="hljs language-js copyable" lang="js">path.resove(); <span class="hljs-comment">// 获取绝对路径</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>parse(); 解析路径</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = path.parse(<span class="hljs-string">'/a/b/c/index.html'</span>);
<span class="hljs-comment">/**
* root: /
* dir: /a/b/c
* base: index.html
* ext: .html
* name: index
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>format(); 序列化路径，与parse功能相反, 将对象拼接成完整的路径。</p>
<pre><code class="hljs language-js copyable" lang="js">path.format(&#123;
    <span class="hljs-attr">root</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">dir</span>: <span class="hljs-string">'/a/b/c'</span>,
    <span class="hljs-attr">base</span>: <span class="hljs-string">'index.html'</span>,
    <span class="hljs-attr">ext</span>: <span class="hljs-string">'.html'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'index'</span>
&#125;);
<span class="hljs-comment">// /a/b/c/index.html</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>normalize(); 规范化路径，将不可用路径变为可用路径, 这个方法注意如果有转译字符会转译。</p>
<pre><code class="hljs language-js copyable" lang="js">path.normalize(<span class="hljs-string">'a/b/c/d'</span>); <span class="hljs-comment">// a/b/c/d</span>
path.normalize(<span class="hljs-string">'a//b/c../d'</span>); <span class="hljs-comment">// a/b/c../d</span>
path.normalize(<span class="hljs-string">'a\\/b/c\\/d'</span>); <span class="hljs-comment">// a/b/c/d </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">Buffer</h4>
<p>Buffer一般称为缓冲区，可以认为因为Buffer的存在让开发者可以使用js操作二进制。IO行为操作的就是二进制数据。NodeJS中的Buffer是一片内存空间。他的大小是不占据v8内存大小的，buffer的内存申请不是由node生成的。只是回收的时候是v8的gc进行回收的。</p>
<p>buffer是nodejs中的一个全局变量，无需require就可以直接使用。一般配合stream流使用，充当数据的缓冲区。</p>
<p>alloc可以创建指定字节大小的buffer，默认没有数据</p>
<p>allocUnsafe 创建指定大小的buffer但是不安全，使用碎片的空间创建buffer，可能存在垃圾脏数据，不一定是空的。</p>
<p>from 接收数据创建buffer</p>
<p>在v6版本之前是可以通过实例化创建buffer对象的，但是这样创建的权限太大了，为了控制权限，就限制了实例化创建的方式。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建buffer</span>
<span class="hljs-keyword">const</span> b1 = Buffer.alloc(<span class="hljs-number">10</span>);
<span class="hljs-keyword">const</span> b2 = Buffer.allocUnsafe(<span class="hljs-number">10</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>from创建buffer可以接收三种类型，字符串，数组，buffer。 第二个参数是编码类型。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> b3 = Buffer.from(<span class="hljs-string">'1'</span>);
<span class="hljs-keyword">const</span> b4 = Buffer.from([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Buffer的一些常见实例方法。</p>
<p>fill: 使用数据填充buffer，会重复写入到最后一位</p>
<p>write：向buffer中写入数据，有多少写多少，不会重复写入。</p>
<p>toString: 从buffer中提取数据</p>
<p>slice: 截取buffer</p>
<p>indexOf：在buffer中查找数据</p>
<p>copy: 拷贝buffer中的数据</p>
<p>Buffer的静态方法。</p>
<p>concat: 将多个buffer拼接成一个新的buffer</p>
<p>isBuffer: 判断当前数据是否是一个buffer</p>
<p>Buffer的split方法实现。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>.Buffer.splice = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">sep</span>) </span>&#123;
    <span class="hljs-keyword">let</span> len = Buffer.form(sep).length;
    <span class="hljs-keyword">let</span> ret = [];
    <span class="hljs-keyword">let</span> start = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> offset = <span class="hljs-number">0</span>;

    <span class="hljs-keyword">while</span>(offset = <span class="hljs-built_in">this</span>.indexOf(sep, start) !== -<span class="hljs-number">1</span>) &#123;
        ret.push(<span class="hljs-built_in">this</span>.slice(start, offset))
        start = offset + len;
    &#125;
    ret .push(<span class="hljs-built_in">this</span>.slice(start));
    <span class="hljs-keyword">return</span> ret;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">fs</h4>
<p>在Node中Buffer和Stream随处可见，他们用于操作二进制数据。</p>
<p>FS是一个内置的核心模块，所有与文件相关的操作都是通过FS来进行实现的，比如文件以及目录的创建，删除，信息的查询或者文件的读取和写入。</p>
<p>如果想要操作文件系统中的二进制数据需要使用FS模块提供的API，这个过程中Buffer和Stream又是密不可分的。</p>
<p>介绍FS模块之前我们首先需要介绍一下文件系统的基础知识，比如权限位，标识符，文件描述符等。</p>
<p>权限是指当前的操作系统内不同的用户角色对于当前的文件可以执行的不同权限操作，文件的权限操作被分为r,w,x三种, r是读权限，w是写权限，x是执行权限。如果用8进制的数字进行表示r是4，w是2，x是1，如果不具备该权限就是一个0。</p>
<p>操作系统中将用户分为三类分别是文件的所有者，一般指的是当前用户自己，再有就是文件的所属组，类似当前用户的家人，最后是其他用户也就是访客用户。</p>
<p>Node中flag表示对文件操作方式，比如是否可读可写。</p>
<p>r: 表示可读</p>
<p>w: 表示可写</p>
<p>s: 表示同步</p>
<p>+: 表示执行相反操作</p>
<p>x: 表示排他操作</p>
<p>a: 表示追加操作</p>
<p>fd就是操作系统分配给被打开文件的标识，通过这个标识符文件操作就可以识别和被追踪到特定的文件。不同操作系统之间是有差异的，node为我们抹平了这种差异。</p>
<p>node每操作一个文件，文件描述符就会递增一次，并且它是从3开始的。因为0，1，3已经被输入，输出和错误占用了。后面我们在使用fs.open打开文件的时候就会得到这个fd。</p>
<p>fs任何文件操作api都有同步和异步两种方式，这里只演示异步API，同步基本也相同</p>
<ul>
<li>文件读写</li>
</ul>
<p>readFile: 从指定文件中读取数据</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);

fs.readFile(path.resolve(<span class="hljs-string">'aaa.txt'</span>), <span class="hljs-string">'utf-8'</span>, <span class="hljs-function">(<span class="hljs-params">err, data</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err);
    <span class="hljs-built_in">console</span>.log(data);
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>writeFile: 向指定文件中写入数据</p>
<pre><code class="hljs language-js copyable" lang="js">fs.writeFile(<span class="hljs-string">'bbb.txt'</span>, <span class="hljs-string">'hello'</span>, &#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-number">438</span>, <span class="hljs-comment">// 操作位</span>
    <span class="hljs-attr">flag</span>: <span class="hljs-string">'w+'</span>,
    <span class="hljs-attr">encoding</span>: <span class="hljs-string">'utf-8'</span>
&#125;, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>appendFile: 追加的方式向指定文件中写入数据</p>
<pre><code class="hljs language-js copyable" lang="js">fs.appendFile(<span class="hljs-string">'bbb.txt'</span>, <span class="hljs-string">'hello'</span>, &#123;&#125;, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>copyFile: 将每个文件中的数据拷贝到另一个文件</p>
<pre><code class="hljs language-js copyable" lang="js">fs.copyFile(<span class="hljs-string">'aaa.txt'</span>, <span class="hljs-string">'bbb.txt'</span>, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>watchFile: 对指定文件进行监控</p>
<pre><code class="hljs language-js copyable" lang="js">fs.watchFile(<span class="hljs-string">'bbb.txt'</span>, &#123;
    <span class="hljs-attr">interval</span>: <span class="hljs-number">20</span> <span class="hljs-comment">// 20ms监控一次</span>
&#125;, <span class="hljs-function">(<span class="hljs-params">curr, prev</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(curr); <span class="hljs-comment">// 当前信息</span>
    <span class="hljs-built_in">console</span>.log(prev); <span class="hljs-comment">// 前一次信息</span>
    <span class="hljs-keyword">if</span> (curr.mtime !== prev.mtime) &#123;
        <span class="hljs-comment">// 文件被修改了</span>
    &#125;
&#125;)

fs.unwatchFile(<span class="hljs-string">'bbb.txt'</span>); <span class="hljs-comment">// 取消监控</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>文件打开与关闭</li>
</ul>
<p>前面我们使用了fs实现了文件的读写操作，既然已经读写了就证明已经实现了文件的打开，为什么node还要单独的提供打开关闭的api呢？</p>
<p>因为readFile和writeFile的工作机制是将文件里的内容一次性的全部读取或者写入到内存里，而这种方式对于大体积的文件来讲显然是不合理的，因此需要一种可以实现边读编写或者边写边读的操作方式，这时就需要文件的打开、读取、写入、关闭看做是各自独立的环节，所以也就有了open和close。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);

<span class="hljs-comment">// open</span>
fs.open(path.resolve(<span class="hljs-string">'aaa.txt'</span>), <span class="hljs-string">'r'</span>, <span class="hljs-function">(<span class="hljs-params">err, fd</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err);
    <span class="hljs-built_in">console</span>.log(fd);

    fs.close(fd, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;

    &#125;);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>目录操作</li>
</ul>
<p>access: 判断文件或目录是否具有操作权限</p>
<pre><code class="hljs language-js copyable" lang="js">fs.access(<span class="hljs-string">'aaa.txt'</span>, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err); <span class="hljs-comment">// 存在错误就是没有权限</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>stat: 获取目录及文件信息</p>
<pre><code class="hljs language-js copyable" lang="js">fs.stat(<span class="hljs-string">'aaa.txt'</span>, <span class="hljs-function">(<span class="hljs-params">err, stat</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(stat); <span class="hljs-comment">// size isFile(), isDirectory()</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>mkdir: 创建目录</p>
<pre><code class="hljs language-js copyable" lang="js">fs.mkdir(<span class="hljs-string">'a/b/c'</span>, &#123;
    <span class="hljs-attr">recursive</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 递归创建</span>
&#125;, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>rmdir: 删除目录</p>
<pre><code class="hljs language-js copyable" lang="js">fs.rmdir(<span class="hljs-string">'a'</span>, &#123;
    <span class="hljs-attr">recursive</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 递归删除</span>
&#125;, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>readdir: 读取目录中内容, 不会递归子目录</p>
<pre><code class="hljs language-js copyable" lang="js">fs.readdir(<span class="hljs-string">'a'</span>, <span class="hljs-function">(<span class="hljs-params">err, files</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(files);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>unlink: 删除指定文件</p>
<pre><code class="hljs language-js copyable" lang="js">fs.unlink(<span class="hljs-string">'a'</span>, <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>commonjs</li>
</ul>
<p>CommonJS的出现是为了解决前端模块化，他的作者希望可以倒逼浏览器们实现前端模块化，但是由于浏览器本身具备的单线程阻塞的特点，CommonJS并不能适用于浏览器平台。CommonJS是一个超集，他是语言层面的规范，模块化只是这个规范中的一个部分。</p>
<ul>
<li>Events</li>
</ul>
<p>Node中通过EventEmitter类实现事件统一管理。实际开发中基本很少引入这个类。这个类大部分供内置模块使用的, 比如fs、http都内置了这个模块。</p>
<p>Node是基于事件驱动的异步操作架构，内置events模块，模块提供了EventEmitter类，他的实例对象具备注册事件和发布事件删除事件的常规操作。</p>
<p>on：添加当事件被触发时调用的回调函数</p>
<p>emit: 触发事件，按照注册的顺序调用每个事件监听器</p>
<p>once: 注册执行一次的监听器</p>
<p>off：移除特定的监听器</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> EventEmitter = <span class="hljs-built_in">require</span>(<span class="hljs-string">'events'</span>);

<span class="hljs-keyword">const</span> ev = <span class="hljs-keyword">new</span> EventEmitter();

ev.on(<span class="hljs-string">'event'</span>, <span class="hljs-function">() =></span> &#123;

&#125;)

ev.emit(<span class="hljs-string">'event'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>事件环</li>
</ul>
<p>在浏览器中是两个任务队列，一个是宏任务一个是微任务。但是在NodeJS中一共存在六个事件队列，timers，pending callbacks，idle prepare，poll，check，close callbacks。每一个队列里面存放的都是回调函数callback。</p>
<p>timer里面存在的是setTimeout与setInterval的回调函数</p>
<p>pending callback是执行操作系统的回调，例如tcp,udp。</p>
<p>idle,prepare只在系统内部进行使用。</p>
<p>poll执行与IO相关的回调操作</p>
<p>check中存放setImmediate中的回调。</p>
<p>close callbacks执行close事件的回调。</p>
<p>在node中代码从上到下同步执行，在执行过程中会将不同的任务添加到相应的队列中，比如说setTimeout就会放在timers中, 如果遇到文件读写就放在poll里面，等到整个同步代码执行完毕之后就会去执行满足条件的微任务。可以假想有一个队列用于存放微任务，这个队列和前面的六种没有任何关系。</p>
<p>当同步代码执行完成之后会去执行满足条件的微任务，一旦所有的微任务执行完毕就会按照上面列出的顺序去执行队列当中满足条件的宏任务。</p>
<p>首先会执行timers当中满足条件的宏任务，当他将timers中满足的任务执行完成之后就会去执行队列的切换，在切换之前会先去清空微任务列表中的微任务。</p>
<p>所以微任务执行是有两个时机的，第一个时机是所有的同步代码执行完毕，第二个时机队列切换前。</p>
<p>注意在微任务中nextTick的执行优先级要高于Promise，这个只能死记了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'s1'</span>);
&#125;)

<span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'p1'</span>);
&#125;)

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'start'</span>);

process.nextTick(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'tick'</span>);
&#125;)

setImmediate(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'st'</span>);
&#125;)

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'end'</span>);

<span class="hljs-comment">// start end tick p1 s1 st</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'s1'</span>);
    <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'p1'</span>);
    &#125;)
    process.nextTick(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'t1'</span>);
    &#125;)
&#125;)

<span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'p2'</span>)
&#125;)

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'start'</span>);

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'s2'</span>);
    <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'p3'</span>);
    &#125;)
    process.nextTick(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'t2'</span>);
    &#125;)
&#125;)

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'end'</span>);

<span class="hljs-comment">// start end p2 s1 s2 t1 t2 p1 p3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Node与浏览器事件环执行是有一些不同的。</p>
<p>首先任务队列数不同，浏览器一般只有宏任务和微任务两个队列，而Node中除了微任务队列外还有6个事件队列。</p>
<p>其次微任务执行时机不同，不过他们也有相同的地方就是在同步任务执行完毕之后都会去看一下微任务是否存在可执行的。对浏览器来说每当一个宏任务执行完成之后就会清空一次微任务队列。在node中只有在事件队列切换时才会去清空微任务队列。</p>
<p>最后在Node平台下微任务执行是有优先级的，nextTick优先于Promise.then, 而浏览器中则是先进先出。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'timeout'</span>);
&#125;)

setImmediate(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'immdieate'</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在node中时而会先输出timeout时而会先输出immdieate，这是因为setTimeout是需要接收一个时间参数的，如果没写就是一个0，我们都知道无论是在node还是在浏览器，程序是不可能真的是0，他会受很多的因素影响。这取决于运行的环境。</p>
<p>如果setTimeout先执行就会放在timers队列中，这样timeout就会先输入，如果setTimeout因为某些原因后执行了，那么check队列中的immdieate就会先执行。这就是为什么时而输出timeout时而输出immdieate。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);

fs.readFile(<span class="hljs-string">'./a.txt'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'timeout'</span>);
    &#125;, <span class="hljs-number">0</span>)

    setImmediate(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'immdieate'</span>);
    &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种情况就会一直先输出immdieate后输出timeout，这是因为，代码执行的时候会在timers里面加入timeout, 在poll
中加入fs的回调，在check中加入immdieate。fs的回调执行结束之后实在poll队列，队列切换的时候首先会去看微任务，但是这里没有微任务就会继续向下，下面就是check队列而不是timers队列，所以poll清空之后会切换到check
队列，执行immdieate回调。</p>
<ul>
<li>stream</li>
</ul>
<p>流并不是Nodejs独创的内容，在linux系统中可以使用<code>ls | grep *.js</code>命令操作，其实就是将ls命令获取到的内容交给grep去处理，这就是一个流操作。</p>
<p>使用流可以从空间和时间上提升效率，NodeJS诞生之初就是为了提高IO性能，其中最常用的文件系统和网络他们就是流操作的应用者。</p>
<p>NodeJS中流就是处理流式数据的抽象接口，NodeJS中的stream对象提供了用于操作流的对象。对于流来说只有多使用才能加深了解。</p>
<p>流的分段处理可以同时操作多个数据chunk，同一时间流无须占据大内存空间。流配合管道，扩展程序会变得很简单。</p>
<p>NodeJS中内置了stream模块，它实现了流操作对象。Stream模块实现了四个具体的抽象。所有的流都继承自EventEmitter。</p>
<p>Readable: 可读流，能够实现数据的获取。</p>
<p>Writeable: 可写流，能够实现数据的写操作。</p>
<p>Duplex: 双工流，即可度又可写。</p>
<p>Tranform: 转换流，可读可写，还能实现数据转换。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);

<span class="hljs-keyword">const</span> rs = fs.createReadStream(<span class="hljs-string">'./a.txt'</span>);
<span class="hljs-keyword">const</span> ws = fs.createWriteStream(<span class="hljs-string">'./b.txt'</span>);

rs.pipe(ws);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>可读流</li>
</ul>
<p>生产供消费的数据流。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> rs = fs.createReadStream(<span class="hljs-string">'./a.txt'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; Readable &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'stream'</span>);

<span class="hljs-keyword">const</span> source = [<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>];

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyReadable</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Readable</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">super</span>();
        <span class="hljs-built_in">this</span>.source = source;
    &#125;
    <span class="hljs-function"><span class="hljs-title">_read</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> data = <span class="hljs-built_in">this</span>.source.shift() || <span class="hljs-literal">null</span>;
        <span class="hljs-built_in">this</span>.push(data);
    &#125;
&#125;

<span class="hljs-keyword">const</span> myreadable = <span class="hljs-keyword">new</span> MyReadable(source);

myreadable.on(<span class="hljs-string">'data'</span>, <span class="hljs-function">(<span class="hljs-params">chunk</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(chunk.toString());
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>可写流</li>
</ul>
<p>用于消费数据的流，响应。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ws = fs.createWriteStream(<span class="hljs-string">'./b.txt'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; Writable &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'stream'</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyWriteable</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Writable</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">super</span>();
    &#125;
    _write (chunk, en, done) &#123;
        process.stdout.write(chunk.toString());
        process.nextTick(done);
    &#125;
&#125;

<span class="hljs-keyword">const</span> mywriteable = <span class="hljs-keyword">new</span> MyWriteable();

mywriteable.write(<span class="hljs-string">'yindong'</span>, <span class="hljs-string">'utf-8'</span>, <span class="hljs-function">() =></span> &#123;
    consoel.log(<span class="hljs-string">'end'</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Duplex</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; Duplex &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'stream'</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyDuplex</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Duplex</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">source</span>)</span> &#123;
        <span class="hljs-built_in">super</span>();
        <span class="hljs-built_in">this</span>.source = source;
    &#125;
    <span class="hljs-function"><span class="hljs-title">_read</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> data = <span class="hljs-built_in">this</span>.source.shift() || <span class="hljs-literal">null</span>;
        <span class="hljs-built_in">this</span>.push(data);
    &#125;
    <span class="hljs-function"><span class="hljs-title">_write</span>(<span class="hljs-params">chunk, en, next</span>)</span> &#123;
        process.stdout.write(chunk);
        process.nextTick(next);
    &#125;
&#125;

<span class="hljs-keyword">const</span> source = [<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>];

<span class="hljs-keyword">const</span> myDuplex = <span class="hljs-keyword">new</span> MyDuplex(source);

mtDuplex.on(<span class="hljs-string">'data'</span>, <span class="hljs-function">(<span class="hljs-params">chunk</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(chunk.toString());
&#125;)

mtDuplex.write(<span class="hljs-string">'yindong'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'end'</span>);
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Transform</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> &#123; Transform &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'stream'</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyTransform</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Transform</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">super</span>();
    &#125;
    <span class="hljs-function"><span class="hljs-title">_transform</span>(<span class="hljs-params">chunk, en, cb</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.push(chunk.toString().toUpperCase());
        cb(<span class="hljs-literal">null</span>);
    &#125;
&#125;

<span class="hljs-keyword">const</span> t = <span class="hljs-keyword">new</span> MyTransform();

t.write(<span class="hljs-string">'a'</span>);

t.on(<span class="hljs-string">'data'</span>, <span class="hljs-function">(<span class="hljs-params">chunk</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(chunk.toString());
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>链表</li>
</ul>
<p>链表是一种数据存储结构。</p>
<p>在文件可写流的write方法工作的时候，有些被写入的内容需要在缓冲区排队等待的，而且遵循的是先进先出的规则，为了保存这些排队的数据，在新版的Node中就采用了链表的结构来存储这些数据。</p>
<p>相比较数组来说，链表的优势更明显，在多个语言下，数组存放数据的长度是有上限的，数组在执行插入或者删除操作的时候会移动其他元素的位置，并且在JS中数组被实现成了一个对象。所以在使用效率上会低一些。</p>
<p>当然这都是相对的，实际应用中数组的作用还是很强大的。</p>
<p>链表是由一系列节点组成的集合。这里的节点都称为node节点，每个节点的身上都有一个对象的引用是指向下一个节点，将这些指向下一个节点的引用组合到一起也就形成了一个链，对于链表结构来说我们常听到的会有不同类型，双向链表，单向链表，循环链表。常用的一般是双向链表。</p></div>  
</div>
            