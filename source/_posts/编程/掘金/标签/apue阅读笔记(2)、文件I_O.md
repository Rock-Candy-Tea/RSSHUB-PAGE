
---
title: 'apue阅读笔记(2)、文件I_O'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef50d4efb46140ce86b8e9774cf0ee61~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 00:10:58 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef50d4efb46140ce86b8e9774cf0ee61~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">文件I/O</h3>
<p>文件I/O操作大概就是打开文件，读文件，写文件，关闭文件，大部分操作只会用到open, read, write, lseek, close。</p>
<h4 data-id="heading-1">open函数</h4>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><fcntl.h></span></span>
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">open</span><span class="hljs-params">(<span class="hljs-keyword">const</span> <span class="hljs-keyword">char</span>*path, <span class="hljs-keyword">int</span> oflag, ...)</span></span>;
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">openat</span><span class="hljs-params">(<span class="hljs-keyword">int</span> fd, <span class="hljs-keyword">const</span> <span class="hljs-keyword">char</span> *path, <span class="hljs-keyword">int</span> oflag, ...)</span></span>;
<span class="hljs-comment">//成功返回文件描述符，失败返回-1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>path指定文件名字。oflag可以说明函数具体的行为</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef50d4efb46140ce86b8e9774cf0ee61~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90f0fc8a34c34863b240f581f0e454dd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f78f39d6aaaf43ecb878d170fe76cbb4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">creat函数</h4>
<p>creat函数可以创建一个新文件</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><fcntl.h></span></span>
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">create</span><span class="hljs-params">(<span class="hljs-keyword">const</span> <span class="hljs-keyword">char</span> *path, <span class="hljs-keyword">mode_t</span> mode)</span></span>;
<span class="hljs-comment">// 成功返回文件描述符，失败返回-1</span>
<span class="hljs-comment">// 等价于open(path, O_WRONLY | O_CREAT | O_TRUNC, mode);</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>create的不足是它以只写方式创建一个文件</p>
<h4 data-id="heading-3">close函数</h4>
<p>关闭一个打开的文件</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><fcntl.h></span></span>
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">close</span><span class="hljs-params">(<span class="hljs-keyword">int</span> fd)</span></span>;
<span class="hljs-comment">// 成功返回0，失败返回-1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关闭一个文件时会释放该进程加在该文件上的所有记录锁
当一个进程终止时，内核会自动关闭它打开的所有文件</p>
<h4 data-id="heading-4">lseek函数</h4>
<p>每个打开的文件都有一个与之关联的"当前文件偏移量"。它通常是一个非负整数，用以度量从文件开始处计算的字节数。通常，读写操作都从当前文件偏移量处开始，并使偏移量增加所读写的字节数。按系统默认的情况，当打开一个文件时，除非指定<code>O_APPEND</code>选项，否则该偏移量被设置成0。lseek可以显式地为一个打开文件设置偏移量。</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">off_t</span> <span class="hljs-title">lseek</span><span class="hljs-params">(<span class="hljs-keyword">int</span> fd, <span class="hljs-keyword">off_t</span> offset, <span class="hljs-keyword">int</span> whence)</span></span>;
<span class="hljs-comment">//成功返回新的文件偏移量，失败返回-1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>whence参数影响offset的解释</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d000e4d28c5646618959fc15b0c214e0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b21f4de447b4361b932cdad7f14f882~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
来测试书中的例子</p>
<pre><code class="hljs language-c copyable" lang="c">  <span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"apue.h"</span></span>
 
  <span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">main</span><span class="hljs-params">(<span class="hljs-keyword">void</span>)</span>
  </span>&#123;
      <span class="hljs-keyword">if</span> (lseek(STDIN_FILENO, <span class="hljs-number">0</span>, SEEK_CUR) == <span class="hljs-number">-1</span>)
          <span class="hljs-built_in">printf</span>(<span class="hljs-string">"cannot seek\n"</span>);
      <span class="hljs-keyword">else</span>
          <span class="hljs-built_in">printf</span>(<span class="hljs-string">"seek OK\n"</span>);
      <span class="hljs-built_in">exit</span>(<span class="hljs-number">0</span>);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70b4ae9018ec4f629375056b4b31f7b1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
编译测试一下</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ ./a.out < /etc/passwd
seek OK
$ ./a.out < /etc/passwd| ./a.out
cannot seek
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意某些偏移量可能是负值，所以比较lseek的返回值时不要测试是否小于0，而是测试是否等于-1
文件偏移量可以超出文件的长度，中间会产生文件空洞</p>
<hr>
<p>测试书中的一个例子</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"apue.h"</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><fcntl.h></span></span>

<span class="hljs-keyword">char</span>buf1[] = <span class="hljs-string">"abcdefghij"</span>;
<span class="hljs-keyword">char</span>buf2[] = <span class="hljs-string">"ABCDEFGHIJ"</span>;

<span class="hljs-function"><span class="hljs-keyword">int</span>
<span class="hljs-title">main</span><span class="hljs-params">(<span class="hljs-keyword">void</span>)</span>
</span>&#123;
<span class="hljs-keyword">int</span>fd;

<span class="hljs-keyword">if</span> ((fd = creat(<span class="hljs-string">"file.hole"</span>, FILE_MODE)) < <span class="hljs-number">0</span>)
err_sys(<span class="hljs-string">"creat error"</span>);

<span class="hljs-keyword">if</span> (write(fd, buf1, <span class="hljs-number">10</span>) != <span class="hljs-number">10</span>)
err_sys(<span class="hljs-string">"buf1 write error"</span>);
<span class="hljs-comment">/* offset now = 10 */</span>

<span class="hljs-keyword">if</span> (lseek(fd, <span class="hljs-number">16384</span>, SEEK_SET) == <span class="hljs-number">-1</span>)
err_sys(<span class="hljs-string">"lseek error"</span>);
<span class="hljs-comment">/* offset now = 16384 */</span>

<span class="hljs-keyword">if</span> (write(fd, buf2, <span class="hljs-number">10</span>) != <span class="hljs-number">10</span>)
err_sys(<span class="hljs-string">"buf2 write error"</span>);
<span class="hljs-comment">/* offset now = 16394 */</span>

<span class="hljs-built_in">exit</span>(<span class="hljs-number">0</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e16dc0c2c14a4ccbb8e2fec6046b2cff~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
测试运行一下</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ gcc hole.c -lapue                        
$ ./a.out                                  
$ ls -l file.hole                          
-rw-r--r-- 1 yuanzhihong yuanzhihong 16394 Jun  6 22:03 file.hole
$ od -c file.hole  
0000000   a   b   c   d   e   f   g   h   i   j  \0  \0  \0  \0  \0  \0
0000020  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0  \0
*
0040000   A   B   C   D   E   F   G   H   I   J
0040012
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d93880791a64b09b372da41f81ae788~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">函数read和write</h4>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span><span class="hljs-meta-string"><unistd.h></span></span>
<span class="hljs-function"><span class="hljs-keyword">ssize_t</span> <span class="hljs-title">read</span><span class="hljs-params">(<span class="hljs-keyword">int</span> fd, <span class="hljs-keyword">void</span> *buf, <span class="hljs-keyword">size_t</span> nbytes)</span></span>;
<span class="hljs-function"><span class="hljs-keyword">ssize_t</span> <span class="hljs-title">write</span><span class="hljs-params">(<span class="hljs-keyword">int</span> fd, <span class="hljs-keyword">void</span> *buf, <span class="hljs-keyword">size_t</span> nbytes)</span></span>;
<span class="hljs-comment">// 返回读或者写的字节数。出错返回-1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有时候会读不到那么多的字节数。比如网络中的缓冲，已经到达了文件末尾。</p>
<h4 data-id="heading-6">进程共享文件表项(i节点)</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06e365766f5e4d009db4f37533685fad~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">原子操作</h4>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><unistd.h></span></span>
<span class="hljs-function"><span class="hljs-keyword">ssize_t</span> <span class="hljs-title">pread</span><span class="hljs-params">(<span class="hljs-keyword">int</span> fd, <span class="hljs-keyword">void</span> *buf, <span class="hljs-keyword">size_t</span> nbytes, <span class="hljs-keyword">off_t</span> offset)</span></span>;
<span class="hljs-function"><span class="hljs-keyword">ssize_t</span> <span class="hljs-title">pwrite</span><span class="hljs-params">(<span class="hljs-keyword">int</span> fd, <span class="hljs-keyword">const</span> <span class="hljs-keyword">void</span> *buf, <span class="hljs-keyword">size_t</span> nbytes, <span class="hljs-keyword">off_t</span> offset)</span></span>;
<span class="hljs-comment">// 返回读/写的字节数，出错返回-1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">dup和dup2</h4>
<p>用来复制一个文件描述符</p>
<pre><code class="copyable">#include<unistd.h>
int dup(int fd);
int dup2(int fd, int fd2);
// 返回新的文件描述符。出错返回-1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>dup相当于复制一个原来的文件描述符，dup2相当于指定fd2为复制fd,如果fd2已经打开，就先关闭fd2。</p>
<h4 data-id="heading-9">函数sync、fsync、fdatasync</h4>
<p>这三个函数都是用来清空缓冲区的</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span><span class="hljs-meta-string"><unistd.h></span></span>
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">fsync</span><span class="hljs-params">(<span class="hljs-keyword">int</span> fd)</span></span>;
<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">fdatasync</span><span class="hljs-params">(<span class="hljs-keyword">int</span> fd)</span></span>;
<span class="hljs-comment">//返回0表示成功，返回-1表示出错</span>
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">sync</span><span class="hljs-params">(<span class="hljs-keyword">void</span>)</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">fcntl函数</h4>
<pre><code class="copyable">#include<fcntl.h>
int fcntl(int fd, int cmd, ... /* int arg */);
// 出错返回-1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>fcntl函数有5种功能</p>
<ul>
<li>1、复制一个已有的描述符，cmd=<code>F_DUPFD</code>或cmd=<code>F_DUPFD_CLOEXEC</code></li>
<li>2、获取/设置文件描述符，cmd=<code>F_GETFD</code>或者cmd=<code>F_SETFD</code></li>
<li>3、获取/设置文件描述符状态，cmd=<code>F_GETFL</code>或者cmd=<code>F_SETFL</code></li>
<li>4、获取/设置异步I/O所有权，cmd=<code>F_GETOWN</code>或者cmd=<code>F_SETOWN</code></li>
<li>5、获取/设置记录锁，cmd=<code>F_GETLK</code>或者cmd=<code>F_SETLK</code>或者cmd=<code>F_SETLKW</code></li>
</ul>
<p>来看书中的一个例子，第一个参数指定文件描述符，并对于该描述符打印其所选择的文件标志说明</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"apue.h"</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><fcntl.h></span></span>

<span class="hljs-function"><span class="hljs-keyword">int</span>
<span class="hljs-title">main</span><span class="hljs-params">(<span class="hljs-keyword">int</span> argc, <span class="hljs-keyword">char</span> *argv[])</span>
</span>&#123;
<span class="hljs-keyword">int</span>val;

<span class="hljs-keyword">if</span> (argc != <span class="hljs-number">2</span>)
err_quit(<span class="hljs-string">"usage: a.out <descriptor#>"</span>);

<span class="hljs-keyword">if</span> ((val = fcntl(atoi(argv[<span class="hljs-number">1</span>]), F_GETFL, <span class="hljs-number">0</span>)) < <span class="hljs-number">0</span>)
err_sys(<span class="hljs-string">"fcntl error for fd %d"</span>, atoi(argv[<span class="hljs-number">1</span>]));

<span class="hljs-keyword">switch</span> (val & O_ACCMODE) &#123;
<span class="hljs-keyword">case</span> O_RDONLY:
<span class="hljs-built_in">printf</span>(<span class="hljs-string">"read only"</span>);
<span class="hljs-keyword">break</span>;

<span class="hljs-keyword">case</span> O_WRONLY:
<span class="hljs-built_in">printf</span>(<span class="hljs-string">"write only"</span>);
<span class="hljs-keyword">break</span>;

<span class="hljs-keyword">case</span> O_RDWR:
<span class="hljs-built_in">printf</span>(<span class="hljs-string">"read write"</span>);
<span class="hljs-keyword">break</span>;

<span class="hljs-keyword">default</span>:
err_dump(<span class="hljs-string">"unknown access mode"</span>);
&#125;

<span class="hljs-keyword">if</span> (val & O_APPEND)
<span class="hljs-built_in">printf</span>(<span class="hljs-string">", append"</span>);
<span class="hljs-keyword">if</span> (val & O_NONBLOCK)
<span class="hljs-built_in">printf</span>(<span class="hljs-string">", nonblocking"</span>);
<span class="hljs-keyword">if</span> (val & O_SYNC)
<span class="hljs-built_in">printf</span>(<span class="hljs-string">", synchronous writes"</span>);

<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> !defined(_POSIX_C_SOURCE) && defined(O_FSYNC) && (O_FSYNC != O_SYNC)</span>
<span class="hljs-keyword">if</span> (val & O_FSYNC)
<span class="hljs-built_in">printf</span>(<span class="hljs-string">", synchronous writes"</span>);
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>

<span class="hljs-built_in">putchar</span>(<span class="hljs-string">'\n'</span>);
<span class="hljs-built_in">exit</span>(<span class="hljs-number">0</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/489969b3251d4f9999c3c6099dc3a11a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
编译运行一下</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-variable">$gcc</span> fileflags.c -lapue
$./a.out 0 < /dev/tty               <span class="hljs-comment">#0表示标准输入</span>
<span class="hljs-built_in">read</span> only
$ ./a.out 1 > temp.foo              <span class="hljs-comment">#1表示标准输出</span>
$ cat temp.foo                      
write only
$ ./a.out 2  2>>temp.foo 
write only, append
$ ./a.out 5 5<>temp.foo            <span class="hljs-comment"># 5<>表示在文件描述符5上打开文件temp.foo以供读写</span>
<span class="hljs-built_in">read</span> write
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再看看书上的另外一个函数。对于一个文件描述符设置一个或者多个文件状态标志的函数</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string">"apue.h"</span></span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><fcntl.h></span></span>

<span class="hljs-function"><span class="hljs-keyword">void</span>
<span class="hljs-title">set_fl</span><span class="hljs-params">(<span class="hljs-keyword">int</span> fd, <span class="hljs-keyword">int</span> flags)</span> <span class="hljs-comment">/* flags are file status flags to turn on */</span>
</span>&#123;
<span class="hljs-keyword">int</span>val;

<span class="hljs-keyword">if</span> ((val = fcntl(fd, F_GETFL, <span class="hljs-number">0</span>)) < <span class="hljs-number">0</span>)
err_sys(<span class="hljs-string">"fcntl F_GETFL error"</span>);

val |= flags;<span class="hljs-comment">/* turn on flags */</span>

<span class="hljs-keyword">if</span> (fcntl(fd, F_SETFL, val) < <span class="hljs-number">0</span>)
err_sys(<span class="hljs-string">"fcntl F_SETFL error"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59f39f4a03374f3cb8506aeb7a97f4f9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
就是先获取文件描述符的状态，再和要设置的标志做或运算，再设置回原来的文件描述符</p></div>  
</div>
            