
---
title: 'RUST  学习日记 第1课 ——Hello World'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b843f4e9103545c686a05db588f6ea7d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 20:31:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b843f4e9103545c686a05db588f6ea7d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">RUST  学习日记 第1课 ——Hello World</h3>
<hr>
<h4 data-id="heading-1">0x00 写在前面</h4>
<p>近几年来Rust这门语言越来越流行，我相信大部分有开发经验的“攻城狮”和“程序猿”们都有所耳闻。假如你之前没有听过那也没关系，咱们一起来学习它。如果你有Java，Kotlin，Python，Go，C++， JavaScript，C#等高级语言的编程经验，那学习Rust应该比较容易哦~即使没有任何编程经验，依然也可以学习哟，因为可以不受任何语言的影响去了解一门编程语言，我感觉也是比较容易上手的。</p>
<h4 data-id="heading-2">0x01 什么是Rust</h4>
<p>Rust语言的出生日期是在 2006 年，其本来是Mozilla员工 Graydon Hoare大神的私人项目，在2010年开始对外公布了。之后Hoare大神离开了Mozilla，大家如果想进一步了解 Hoare大神，可以百度一下。这里也有他离开Mozilla的一个解释——[<a href="http://slash-r-slash-rust.github.io/archived/2u1dme.html#co4uurq" target="_blank" rel="nofollow noopener noreferrer">strcat] : rust (slash-r-slash-rust.github.io)</a></p>
<p>话题转回来，Rust语言突然流行起来，肯定有它的优势。Rust语言具有内存安全，内存管理，所有权，类型多态等优势。简单介绍下，Rust语言不会出现内存访问的错误，为了保证内存安全，建立了严格的内存管理模型——所有权系统和类型系统。通过严格的编译器来检查代码中的每个变量和引用的每个内存指针，为所有的变量建立了清晰的生命周期。如果变量超出生命周期，变量将会自动被释放，因此其并不像Java那样需要垃圾回收机制。其中，每一个被分配的内存都有一个独占其所有权的指针。当时该指针被销毁时，相应的指针对应的内存才会被释放掉。</p>
<h4 data-id="heading-3">0x02 搭建Rust环境</h4>
<p>声明：本文所有的操作都在<code>Widnows 10</code>系统上操作。本人买不起水果本~~~</p>
<p><code>Windows</code>操作系统上搭建环境还是比较简单的</p>
<p>1.官网下载安装包</p>
<p><a href="https://www.rust-lang.org/tools/install" target="_blank" rel="nofollow noopener noreferrer">Install Rust - Rust Programming Language (rust-lang.org)</a></p>
<p>根据自己操作系统选择32位或者64位安装包即可。</p>
<p>2.<strong>安装Visual Studio (必须)</strong></p>
<p><strong>安装Visual Studio (必须)</strong></p>
<p><strong>安装Visual Studio (必须)</strong></p>
<p>Rust编译需要使用MSVC Build Tools，没有单独的安装包，最简单的方法就是安装Visual Studio咯</p>
<p>如果你不从事C#相关的开发，我这里建议安装 <code>Visual Studio 2013</code>就可以了。下面是下载地址。</p>
<pre><code class="hljs language-xml copyable" lang="xml">Visual Studio Ultimate 2013 (x86) - DVD (Chinese-Simplified) 
文件名:cn_visual_studio_ultimate_2013_x86_dvd_3175316.iso
SHA1:D6029A90916AA49F3F8F260C277DAF838DDA0612
文件大小:2.87GB
发布时间:2013-11-08
电驴:ed2k://|file|cn_visual_studio_ultimate_2013_x86_dvd_3175316.iso|3077509120|ADDA34B2BC29E1571276AE50A220EB91|/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.命令行输入<code>rustc</code>回车，出现下面的提示，即表明安装完成Rust了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b843f4e9103545c686a05db588f6ea7d~tplv-k3u1fbpfcp-zoom-1.image" alt="rustc执行命令" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">0x03 Hello World</h4>
<p>是不是等这一刻很久了，开始手撸Hello World，毕竟这是学习每一门语言的第一步~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f14a7b1eb7cf43178ff58cb9dbaf9848~tplv-k3u1fbpfcp-zoom-1.image" alt="hello world" loading="lazy" referrerpolicy="no-referrer"></p>
<p>随便创建一个文件夹，创建一个文件<code>main.rs</code>，编写上图的代码。</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">main</span></span>() &#123;
   <span class="hljs-built_in">println!</span>(<span class="hljs-string">"hello world~~"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后使用<code>rustc</code>编译这个文件。</p>
<p>注：如果这里你编译报了下面图片所示的错误，那么你肯定没有装Visual Studio~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a1fdaf04f3643b98fd1e56e39f80bc9~tplv-k3u1fbpfcp-zoom-1.image" alt="编译错误" loading="lazy" referrerpolicy="no-referrer"></p>
<p>编译成功后，会在目录下多出两个文件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e3c7b70210c4f8e93d12646b6e474cc~tplv-k3u1fbpfcp-zoom-1.image" alt="编译成功" loading="lazy" referrerpolicy="no-referrer"></p>
<p>快点击 <code>main.exe</code>运行看下...发生了什么，一闪而过。原因是程序执行太快，瞬间结束了，咱们加入下面的代码，让程序暂停~</p>
<pre><code class="hljs language-rust copyable" lang="rust"><span class="hljs-keyword">use</span> std::process::Command;

<span class="hljs-function"><span class="hljs-keyword">fn</span> <span class="hljs-title">main</span></span>() &#123;
   <span class="hljs-built_in">println!</span>(<span class="hljs-string">"hello world~~"</span>);

   <span class="hljs-comment">// 命令提示符 pause</span>
   <span class="hljs-keyword">let</span> _ = Command::new(<span class="hljs-string">"cmd.exe"</span>).arg(<span class="hljs-string">"/c"</span>).arg(<span class="hljs-string">"pause"</span>).status();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再重新编译，运行！成功了！！这是咱们写的第一个Rust程序。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/338144ed45f142de98a9d8601733893c~tplv-k3u1fbpfcp-zoom-1.image" alt="运行" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">0x04 小结</h4>
<p>咱们初步认识了Rust，也写了第一个程序—— Hello World。咱们可能不明白它的语法，但是已经运行了起来。没关系咱们后续的文章会详细介绍。通过<code>Hello World</code>程序，咱们也知道了<code>Rust</code>语言在计算机中打印信息的方法，是不是与C语言，Java，Kotlin很像呢？还有，咱们在搭建环境的时候必须要安装<code>Visual Studio</code>的原因是什么呢？有没有什么方法能跟<code>Go</code>语言那样，可以不安装Visual Studio就运行<code>Rust</code>呢？答案是有的，大家可以百度下，我在这里就不多介绍了呢？下节预告——Rust是否有其它的构建工具和包管理工具呢？</p>
<h4 data-id="heading-6">0x05 官方文档及其他资料(免费)</h4>
<ul>
<li><a href="https://www.rust-lang.org/zh-CN/learn" target="_blank" rel="nofollow noopener noreferrer">学习 Rust - Rust 程序设计语言 (rust-lang.org)</a></li>
<li><a href="https://www.runoob.com/rust/rust-tutorial.html" target="_blank" rel="nofollow noopener noreferrer">Rust 教程 | 菜鸟教程 (runoob.com)</a></li>
</ul>
<h4 data-id="heading-7">0x06 本节源码</h4>
<p><a href="https://gitee.com/haoyu3/study-rust/tree/master/001" target="_blank" rel="nofollow noopener noreferrer">001 StudyRust - 码云 - 开源中国 (gitee.com)</a></p></div>  
</div>
            