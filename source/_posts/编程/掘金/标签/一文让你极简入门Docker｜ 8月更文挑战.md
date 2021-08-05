
---
title: '一文让你极简入门Docker｜ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1429fc6dbaf84e2081eb88cff9170a40~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 16:10:49 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1429fc6dbaf84e2081eb88cff9170a40~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h3 data-id="heading-0">Docker介绍</h3>
<p>Docker 是一个开源的应用容器引擎，基于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fgo%2Fgo-tutorial.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/go/go-tutorial.html" ref="nofollow noopener noreferrer">Go 语言</a> 并遵从 Apache2.0 协议开源。</p>
<p>Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。</p>
<p>容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。</p>
<h3 data-id="heading-1">Docker的应用场景</h3>
<ul>
<li>Web 应用的自动化打包和发布。</li>
<li>自动化测试和持续集成、发布。</li>
<li>在服务型环境中部署和调整数据库或其他的后台应用。</li>
<li>从头编译或者扩展现有的 OpenShift 或 Cloud Foundry 平台来搭建自己的 PaaS 环境。</li>
</ul>
<h3 data-id="heading-2">如何使用docker</h3>
<p>docker中有这样几个概念：</p>
<ul>
<li>dockerfile</li>
<li>image</li>
<li>container</li>
</ul>
<p>实际上你可以简单的把image理解为可执行程序，container就是运行起来的进程。</p>
<p>那么写程序需要源代码，那么“写”image就需要dockerfile，dockerfile就是image的源代码，docker就是"编译器"。</p>
<p>因此我们只需要在dockerfile中指定需要哪些程序、依赖什么样的配置，之后把dockerfile交给“编译器”docker进行“编译”，也就是docker build命令，生成的可执行程序就是image，之后就可以运行这个image了，这就是docker run命令，image运行起来后就是docker container。</p>
<p>具体的使用方法就不再这里赘述了，大家可以参考docker的官方文档，那里有详细的讲解。</p>
<h3 data-id="heading-3">docker是如何工作的</h3>
<p>实际上docker使用了常见的CS架构，也就是client-server模式，docker client负责处理用户输入的各种命令，比如docker build、docker run，真正工作的其实是server，也就是docker demon，值得注意的是，docker client和docker demon可以运行在同一台机器上。</p>
<p>接下来我们用几个命令来讲解一下docker的工作流程：</p>
<p><strong>1，docker build</strong></p>
<p>当我们写完dockerfile交给docker“编译”时使用这个命令，那么client在接收到请求后转发给docker daemon，接着docker daemon根据dockerfile创建出“可执行程序”image。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1429fc6dbaf84e2081eb88cff9170a40~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>2，docker run</strong></p>
<p>有了“可执行程序”image后就可以运行程序了，接下来使用命令docker run，docker daemon接收到该命令后找到具体的image，然后加载到内存开始执行，image执行起来就是所谓的container。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b11b0391b69545f09a8586025dee6510~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer">
<strong>3，docker pull</strong></p>
<p>其实docker build和docker run是两个最核心的命令，会用这两个命令基本上docker就可以用起来了，剩下的就是一些补充。</p>
<h3 data-id="heading-4">Docker中关于容器的基本操作</h3>
<p>在前边镜像的章节中，我们已经看到了如何基于镜像启动一个容器，即docker run操作。</p>
<pre><code class="copyable">[root@xxx ~]# docker run -it centos:latest /bin/bash
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里-it是两个参数：-i和-t。前者表示打开并保持stdout，后者表示分配一个终端（pseudo-tty）。此时如果使用exit退出，则容器的状态处于Exit，而不是后台运行。如果想让容器一直运行，而不是停止，可以使用快捷键 ctrl+p ctrl+q 退出，此时容器的状态为Up。</p>
<p>除了这两个参数之外，run命令还有很多其他参数。其中比较有用的是-d后台运行：</p>
<pre><code class="copyable">[root@xxx ~]# docker run centos:latest /bin/bash -c "while true; do echo hello; sleep 1; done"
[root@xxx ~]# docker run -d centos:latest /bin/bash -c "while true; do echo hello; sleep 1; done"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里第二条命令使用了-d参数，使这个容器处于后台运行的状态，不会对当前终端产生任何输出，所有的stdout都输出到log，可以使用docker logs container_name/container_id查看。</p>
<p>启动、停止、重启容器命令：</p>
<pre><code class="copyable">[root@xxx ~]# docker start container_name/container_id
[root@xxx ~]# docker stop container_name/container_id
[root@xxx ~]# docker restart container_name/container_id
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后台启动一个容器后，如果想进入到这个容器，可以使用attach命令：</p>
<pre><code class="copyable">[root@xxx ~]# docker attach container_name/container_id
<span class="copy-code-btn">复制代码</span></code></pre>
<p>删除容器的命令前边已经提到过了：</p>
<pre><code class="copyable">[root@xxx ~]# docker rm container_name/container_id
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            