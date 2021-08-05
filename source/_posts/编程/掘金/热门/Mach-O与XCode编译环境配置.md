
---
title: 'Mach-O与XCode编译环境配置'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f18412e691e84290b76baa677e424ee7~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 01:53:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f18412e691e84290b76baa677e424ee7~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">什么是Mach-O？</h1>
<p><code>Mach-O(Mach Object)</code>是<code>macOS、iOS、iPadOS</code>存储<strong>程序</strong>和<strong>库</strong>(动态库，静态库)的文件格式。对应系统通过应用二进制接口(<code>application binary interface</code>，缩写为<code>ABI</code>)来运行该格式的文件。<code>ABI</code>说明了<code>Mach-O</code>的文件格式
<code>Mach-O</code>格式用来替代<code>BSD</code>系统的<code>a.out</code>格式。<code>Mach-O</code>文件格式保存了在编译过程和链接过程中产生的机器代码和数据，从而为<strong>静态链接</strong>和<strong>动态链接</strong>的代码提供了单一文件格式。</p>
<h2 data-id="heading-1">APP 是怎么跑起来的？</h2>
<p>Application run的过程，其实就是加载我们application folder里面的可执行文件，那这个过程是怎样的呢？</p>
<ol>
<li>调用<code>fork</code>函数，创建一个<code>process</code></li>
<li>调用<code>execve</code>或其衍生函数，在该进程上加载，执行我们的<code>Mach-O</code>文件</li>
</ol>
<p>当我们调用时<code>execve</code>(程序加载器)，内核实际上在执行以下操作:</p>
<ol>
<li>将文件加载到内存</li>
<li>开始分析<code>Mach-O</code>中的<code>mach_header</code>，以确认它是有效的<code>Mach-O</code>文件</li>
</ol>
<h2 data-id="heading-2">分析Mach-O</h2>
<p>使用如下命令</p>
<pre><code class="copyable">objdump -macho -private-headers &#123;可执行文件路径&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f18412e691e84290b76baa677e424ee7~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以看到<code>private headers</code>里有很多<code>load command</code>. 可以理解<code>Mach-O</code>文件就是<code>配置文件() + 二进制代码</code>，<code>Mach-O</code>中都是二进制. 我们的程序为什么入口是<code>main</code>? 是因为在<code>Mach-O</code>文件中指定了程序入口是<code>main</code>，
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0a1b1fa68a5407cae9f74673023f775~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这个<code>LC_MAIN</code>是告诉动态链接器（<code>dyld</code>）去加载可执行文件的入口，并不一定是<code>main</code>, 可以自己指定.</p>
<p>为了理解<code>Mach-O</code>本质上就是一个二进制文件，<code>Mach-O</code>本质上是可读可写的，在网上找了一些资料去分析<code>Mach-O</code>内容<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmeilin0413%2Fmachinfo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/meilin0413/machinfo" ref="nofollow noopener noreferrer">详见</a>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ad403933e404a73bdd15d6f178cfb5a~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<code>Mach-O</code>中的数据是按照一定的规则排列的，最前面是<code>mach_header_64</code>的结构体，后面依次存放的是<code>load_command</code>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83a63bb202af445994c1a50f2a053328~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bef3cd200284e58950e81d740f10583~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">编译与链接</h1>
<p>当我们编译生成目标文件会有一个<code>.o</code>文件生成，那么这个<code>.o</code>文件是什么呢？为什么要生成一个<code>.o</code>文件？编译过程到底发生了什么事情？在此推荐一本书<code>程序员的自我修养</code>.
编译其实就是将我们所写的代码放到对应的配置文件里面. 比如对于一个符号，是全局的还是本地的，是外部的还是内部的？比如<code>NSLog</code>的调用，<code>NSLog</code>其实是一个外部符号. 根据这些符号的特性，将这些符号在编译的过程中进行分类. 当然我们编译的时候，肯定不止一个<code>.o</code>文件，简单来说，链接的本质就是多个目标文件组合成一个文件.</p>
<h2 data-id="heading-4">查看符号的命令</h2>
<ol>
<li><code>Symbol Table</code>:就是用来保存符号。</li>
<li><code>String Table</code>:就是用来保存符号的名称。</li>
<li><code>Indirect Symbol Table</code>:间接符号表。保存使用的外部符号。更准确一点就是使 用的外部动态库的符号。是<code>Symbol Table</code>的子集。</li>
</ol>
<p><code>tty</code>命令：输出当前<code>terminal</code>的标识.
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e14050e469ba401298e38026363c0748~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d17d26f0a69a44ffb052625c857070e0~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
在<code>Build Phase</code>中配置<code>run script</code>如上，当我们编译的时候，就会输出<code>hello mmm</code>到<code>terminal</code>中.
怎样在我们编译之后，直接执行一个<code>shell</code>脚本呢？
我们在<code>xconfig</code>中定义的变量，也可以在<code>build phases</code>中的<code>run script</code>使用.</p>
<p>当然我们也可以build 通过之后，直接在<code>terminal</code>中执行<code>nm -pa &#123;可执行文件路径&#125;</code>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/404bfe44e312457b8c7358b68ced0650~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
我们可以看到，输出了符号表的内容，但是把一些我们没必要关心的<code>Debug</code>符号也包含了，当然后面我们可以通过<code>strip</code>命令剥离<code>Debug</code>符号.
我们可以看下build的过程
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24314bb71588412e96ceadb6901b42a0~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
我们发现<code>run script</code>是在编译完整，<code>sign</code>之前去<code>run</code>的.</p>
<h3 data-id="heading-5">strip 命令</h3>
<p>在<code>build setting</code>中可以设置<code>strip</code>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9a26adbd71d481eb5eb44127cee8786~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<code>strip</code>命令可以剥离符号表，符号占用的控件还是挺大的. 但是<code>strip</code>命令是在<code>sign</code>之前，<code>run script</code>之后.</p>
<p>我们查看下<code>ld</code>命令有什么 <code>option</code>可以剥离<code>Debug</code>符号
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eda2f7805383456dbe71c43fe1bffade~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
因此我们可以在<code>xconfig</code>中配置<code>other link flag</code> 如下：</p>
<pre><code class="copyable">OTHER_LDFLAGS = -Xlinker -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以剥离掉<code>Debug</code>符号，再次执行<code>nm -pa &#123;可执行文件路径&#125;</code>命令, 可以得到如下结果
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/887222f785f24ad59baeeef7d3245aa5~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
上述输出结果，是我们的目标文件中，除了<code>Debug</code>符号的所有符号.
只有了解了符号，后续才能知道怎么对动态库进行瘦身.</p>
<h3 data-id="heading-6">对库瘦身</h3>
<ol>
<li>编译选项<code>-O1</code> <code>-Oz</code>之类的</li>
<li><code>dead code strip</code>死代码剥离 (链接的过程中)</li>
<li><code>strip</code>命令进行剥离符号（修改<code>mach-o</code>）</li>
</ol></div>  
</div>
            