
---
title: 'JuiceFS v0.17 发布，通过 1270 项 LTP 测试'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5776b88bad69819da1515b450416174f8e2.png'
author: 开源中国
comments: false
date: Tue, 28 Sep 2021 00:03:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5776b88bad69819da1515b450416174f8e2.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">小伙伴们大家好，JuiceFS v0.17 在国庆小长假来临之际如期发布了！这是我们在 2021 年秋季推出的第二个版本，让我们直奔主题，看看都有哪些新变化吧。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本次更新累计 80+ 提交，共有 9 位来自 JuiceFS 社区的小伙伴在 GitHub 上贡献代码。在这里，我们向每一位贡献者表示最诚挚的感谢，同时欢迎屏幕前的你也加入到 JuiceFS 开源社区，贡献代码、文档或讨论想法。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">通过 LTP 1270 项测试，Linux 系统下兼容性更完美</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">JuiceFS 的最新版本针对 Linux 系统环境做了进一步的优化，改进了 rename 和 setxattr 读其他参数的支持，顺利通过了 LTP 的<span> </span><strong>1270</strong><span> </span>项测试。</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flinux-test-project%2Fltp" target="_blank">LTP</a>（Linux Test Project）是一个由 IBM，Cisco 等多家公司联合开发维护的项目，旨在为开源社区提供一个验证 Linux 可靠性和稳定性的测试集。LTP 中包含了各种工具来检验 Linux 内核和相关特性。</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>测试结果</strong>：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-c"><span style="color:#032f62">Testcase</span>                                           <span style="color:#032f62">Result</span>     <span style="color:#032f62">Exit</span> <span style="color:#032f62">Value</span>
<span style="color:#032f62">--------</span>                                           <span style="color:#032f62">------</span>     <span style="color:#032f62">----------</span>
<span style="color:#032f62">fcntl17</span>                                            <span style="color:#032f62">FAIL</span>       <span>7</span>
<span style="color:#032f62">fcntl17_64</span>                                         <span style="color:#032f62">FAIL</span>       <span>7</span>
<span style="color:#032f62">getxattr05</span>                                         <span style="color:#032f62">CONF</span>       <span>32</span>
<span style="color:#032f62">ioctl_loop05</span>                                       <span style="color:#032f62">FAIL</span>       <span>4</span>
<span style="color:#032f62">ioctl_ns07</span>                                         <span style="color:#032f62">FAIL</span>       <span>1</span>
<span style="color:#032f62">lseek11</span>                                            <span style="color:#032f62">CONF</span>       <span>32</span>
<span style="color:#032f62">open14</span>                                             <span style="color:#032f62">CONF</span>       <span>32</span>
<span style="color:#032f62">openat03</span>                                           <span style="color:#032f62">CONF</span>       <span>32</span>
<span style="color:#032f62">setxattr03</span>                                         <span style="color:#032f62">FAIL</span>       <span>6</span>

<span style="color:#032f62">-----------------------------------------------</span>
<span style="color:#6f42c1">Total Tests:</span> <span>1270</span>
<span style="color:#6f42c1">Total Skipped Tests:</span> <span>4</span>
<span style="color:#6f42c1">Total Failures:</span> <span>5</span>
<span style="color:#6f42c1">Kernel Version:</span> <span>5.4</span><span>.0</span><span>-1029</span><span style="color:#032f62">-aws</span>
<span style="color:#6f42c1">Machine Architecture:</span> <span style="color:#032f62">x86_64</span>
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">其中，跳过和失败的项目主要是由于几个尚未支持的功能，详情见此<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjuicedata%2Fjuicefs%2Fblob%2Fmain%2Fdocs%2Fzh_cn%2Fposix_compatibility.md" target="_blank">文档</a>。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">优化存储临时数据的性能</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">针对 Spark 的 shuffle 文件等临时数据存储需求，社区贡献者<strong>祝威廉</strong>（@allwefantasy）给 JuiceFS 贡献了数据延迟上传功能，它可以让 JuiceFS 优先将数据写入到本地缓存盘中，如果这些数据在短时间内又被删除，则无需写入对象存储，可以提供接近本地盘的读写性能。而当写入数据很多时，又会自动写到对象存储来释放本地盘空间，再也不用担心 shuffle 数据把磁盘写满了。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">这个新功能让 JuiceFS 可以作为一个弹性本地盘使用，为临时数据提供无限存储空间和低延时访问。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">为了进一步提升性能，还新增了一个运行在客户端内存中的元数据引擎（<code>MemKV</code>）。与其他元数据引擎一样，MemKV 的作用也是用来保存数据相关的元信息，但它不持久化，客户端 umount 以后，MemKV 的元数据就释放了。MemKV 完全在内存中运行，有着绝对的性能优势，非常适合用作临时文件的存储场景。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">TiKV 元数据引擎在 Hadoop 场景中性能提升 5 倍</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">JuiceFS Java 客户端需要频繁做路径解析，Redis 引擎通过 Lua 实现了服务器端的多级路径解析，而 SQL 和 TiKV 引擎仍然需要多次元数据请求才能解析一个路径，尤其是当路径比较深时对影响有比较大的影响。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">为了解决这个问题，本次更新在 JuiceFS Hadoop SDK 客户端中引入了类似于 Linux 内核的元数据缓存机制，可以分别通过参数控制目录、文件和属性的过期时间。可以通过如下的方式启用：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#333333"><<span style="color:#22863a">property</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">name</span>></span>juicefs.attr-cache<span style="color:#333333"></<span style="color:#22863a">name</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">value</span>></span>3<span style="color:#333333"></<span style="color:#22863a">value</span>></span>
<span style="color:#333333"></<span style="color:#22863a">property</span>></span>
<span style="color:#333333"><<span style="color:#22863a">property</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">name</span>></span>juicefs.entry-cache<span style="color:#333333"></<span style="color:#22863a">name</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">value</span>></span>3<span style="color:#333333"></<span style="color:#22863a">value</span>></span>
<span style="color:#333333"></<span style="color:#22863a">property</span>></span>
<span style="color:#333333"><<span style="color:#22863a">property</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">name</span>></span>juicefs.dir-entry-cache<span style="color:#333333"></<span style="color:#22863a">name</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">value</span>></span>3<span style="color:#333333"></<span style="color:#22863a">value</span>></span>
<span style="color:#333333"></<span style="color:#22863a">property</span>></span>
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">以下是对 9 层目录的元数据性能测试，可以看到启用元数据缓存够大幅提升元数据操作的性能。（数值代表操作的时延，越小越好。）</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-5776b88bad69819da1515b450416174f8e2.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">但需要注意的是，开启元数据缓存后会影响多客户端之间的一致性（有限时间窗口的最终一致性），比如一个客户端删除了某个文件后，其他节点可能因为缓存未到期，仍然认为文件存在。因此，一般建议在查询场景下使用该功能。如果是混合读写的场景，建议适当开启目录和属性的缓存，而关闭文件项的缓存。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">1 分钟上手性能测试，结果一目了然</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">我们为 JuiceFS 内置的性能测试工具<span> </span><strong>bench</strong><span> </span>的结果做了进一步的优化，在简洁直观的基础上，进一步的让关键数据高亮显示，如果某项性能数据偏离正常区间，会显示为黄色甚至红色，建议特别关注下。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-cf1c16d750e5593bb855211650ecce0c2a3.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">有关 JuiceFS 新版的更多内容，欢迎访问<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjuicedata%2Fjuicefs" target="_blank">GitHub 项目主页</a>了解详情。</p>
                                        </div>
                                      
</div>
            