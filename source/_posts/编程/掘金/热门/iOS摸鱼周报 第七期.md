
---
title: 'iOS摸鱼周报 第七期'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d483200f53f94b7aaab1431f32bc83a6~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 28 Mar 2021 18:16:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d483200f53f94b7aaab1431f32bc83a6~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d483200f53f94b7aaab1431f32bc83a6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>iOS摸鱼周报，主要分享大家开发过程遇到的经验教训及学习内容。虽说是周报，但当前内容的贡献途径还未稳定下来，如果后续的内容不足一期，可能会拖更到下一周再发。所以希望大家可以多分享自己学到的开发小技巧和解bug经历。</p>
<p>周报仓库在这里：<a href="https://github.com/zhangferry/iOSWeeklyLearning" target="_blank" rel="nofollow noopener noreferrer">github.com/zhangferry/…</a> ，可以查看README了解贡献方式；另可关注公众号：iOS成长之路，后台点击进群交流，联系我们。</p>
<h2 data-id="heading-0">开发Tips</h2>
<p>开发小技巧收录。</p>
<h3 data-id="heading-1">文件夹命名</h3>
<p>最近执行shell脚本时，发生了奇怪的问题，很简单的<code>rm</code>命令却一直执行出错。看了日志发现是文件路径路径中包含<code>&</code>符号，其中某个文件夹的命名带有这个与符号。执行命令时这被作为特殊符号，被拆成了两条命令，导致出错。</p>
<p>所以之后文件或者文件夹命名切记不要用<code>&</code>、<code>|</code> 这些特殊字符。</p>
<h3 data-id="heading-2">动态库vs静态库</h3>
<p>使用Swift的第三方库的时候我们可以选择静态或者动态库，那它们之间有什么区别呢？可以参考这篇文章</p>
<p><a href="https://acecilia.medium.com/static-vs-dynamic-frameworks-in-swift-an-in-depth-analysis-ff61a77eec65" title="Static VS dynamic frameworks in Swift: an in-depth analysis" target="_blank" rel="nofollow noopener noreferrer">Static VS dynamic frameworks in Swift: an in-depth analysis</a></p>
<p>测试项目有27个动态库，其中6个是用Carthage集成的，21个是用CocoaPods集成的。把他们全部转成静态库之后，软件Size降低了14.55%，启动时间降低了35%左右，主要是降低了动态库的加载时间，以下是各阶段详细的时间对比：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c70c756c57f1474a839b714cb3a0a5f7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里启动时间降低好理解，大小降低是因为啥呢，是因为静态库时编译器移除了无用的符号表。</p>
<p>因为应用内的动态库，不像系统动态库一样可以供别的App共享，所以它无法起到减少包体的作用。所以通常情况下我们都应该考虑优先使用静态库。</p>
<p>另外静态库可以依赖动态库，但是动态库是不能依赖静态库的。</p>
<h2 data-id="heading-3">编程概念</h2>
<h3 data-id="heading-4">什么是SSH</h3>
<p>SSH是一个网络安全协议，用于计算机之间的加密登录（非对称加密），每台Linux上都安装有SSH。它工作在传输层，能防止中间人攻击，DNS欺骗。它的用法是</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> ssh user@host</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>host可以是ip地址或者域名，还可以通过-p指定端口号。</p>
<p>ssh登录流程为：</p>
<p>1、远程主机收到用户的登录请求，把自己的公钥发给用户。</p>
<p>2、用户使用这个公钥，将登录密码加密后，发送回来。</p>
<p>3、远程主机用自己的私钥，解密登录密码，如果密码正确，就同意用户登录。</p>
<p>如果不想每次登录时都输密码，可以将本地的公钥发送到远程主机，这样登录过程就变成了：</p>
<p>1、每次远程主机发送一个随机字符串</p>
<p>2、用户用自己的私钥加密</p>
<p>3、远程主机利用公钥解密，如果成功就就同意用户登录。</p>
<h3 data-id="heading-5">什么是Nginx</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/889b8b05c3004970b7900bf97d2cff1f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Nginx是一款轻量级的Web服务器、反向代理服务器，由于其开源、内存占用少，启动快，高并发能力强，在互联网项目中广泛应用；同时它还是一个IMAP、POP3、SMTP代理服务器，还可以作为反向代理进行负载均衡的实现。</p>
<p>应用场景：在博客站点中，它担任HTTP服务器的作用，通过HTTP协议将服务器上的静态文件（HTML、图片）展现给客户端。</p>
<h3 data-id="heading-6">什么是负载均衡</h3>
<p>负载均衡是一种提高网络可用性的解决方案。当没有负载均衡时，当前服务器宕机或访问量超过服务器上限都会导致网站瘫痪无法访问。负载均衡的解决方案是，设立多台服务器，在访问服务器之前首先经过负载均衡器，由负载均衡器进行分配当前请求应该访问哪一个服务器。既提高了网站瘫痪的容错率又分摊了单个服务器的压力。</p>
<p>负载均衡的实现关键点是如何分配服务器。前置条件是定期检测服务器健康状态，维护一个健康服务器池，然后用一定的算法进行服务器分配，有三种常见分配算法：</p>
<p>轮询：按健康服务器表逐一分配</p>
<p>最小链接：优先选择连接数最少的服务器</p>
<p>Source：根据来源ip地址选择服务器，保证特定用户连接同一服务器</p>
<p>Nginx可以用于实现负载均衡，也提供了以上几种分配算法实现。</p>
<h3 data-id="heading-7">什么是Apache</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52def6eef39548ec84aaebf2cf992782~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Apache有多个含义：</p>
<p>一是Apache基金会，它是专门为支持开源软件项目而创办的一个非营利性组织，它所发行的软件都遵循Apache协议。</p>
<p>二是Apache服务器，即httpd，它是Apache团队最早开发的项目，由于它的跨平台和安全性的特点，它成为了世界上最流行的Web服务器软件之一。Apache作为服务器跟Nginx是一样的东西，他们都只支持静态网页，Nginx更轻量，Apache则更稳定。</p>
<p>三是Apache协议（Apache Licence），Apache协议的目的是为了鼓励代码共享，并达到尊重原作者的著作权的作用。你可以使用遵循Apache协议的开源框架并投入商用，但要保留其原有协议声明，如果进行了修改也需要进行说明。</p>
<h3 data-id="heading-8">什么是Tomcat</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05c608571e0548c0852407ffee81b4d4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Tomcat是由Apache基金会推出的一款开源的可实现JavaWeb程序的Web服务器框架，它是配置JSP（Java Server Page）和JAVA系统必备的一款环境。</p>
<p>它与Apache服务器的区别在于，Apache只支持静态网页，比如博客网站，而Tomcat支持JSP，Servlet，可以实现动态的web应用，像是图书管管理系统。两者也可以结合，处理既有动态又有静态的网站。</p>
<h3 data-id="heading-9">什么是Docker</h3>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66d85f83df3543eebfa216d3deaff8a2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>理解Docker之前需要知道容器的概念，容器就是一个封闭的开发环境，类似移动端的沙盒，每个沙盒都可以配置不同的程序，甚至相同程序的不同版本，我在沙盒做的操作不会影响别的沙盒程序。</p>
<p>虚拟机也是一种容器，我可以在不同虚拟机的配置里运行不同的程序，他们互不影响。但是虚拟机太占用系统资源了，不同虚拟机占用不同的内核资源，能否把其中一些共性的东西进行共享？当然是可以的，这就是Docker做的事情。</p>
<p>Docker是一家公司，它还做了一个好事情，就是供了很多配置好的镜像资源（一整套的环境搭建），存储在公共的镜像仓库，大大简化了应用的分发，部署流程。</p>
<h2 data-id="heading-10">优秀博客</h2>
<p><a href="http://tutuge.me/2016/06/19/translation-why-objcmsgsend-must-be-written-in-assembly/" title="翻译-为什么objc_msgSend必须用汇编实现" target="_blank" rel="nofollow noopener noreferrer">翻译-为什么objc_msgSend必须用汇编实现</a> -- 来自博客：土土哥的blog</p>
<p><a href="http://xelz.info/blog/2019/01/11/ios-code-signature/" title="深度长文：细说iOS代码签名" target="_blank" rel="nofollow noopener noreferrer">深度长文：细说iOS代码签名</a> -- 来自博客：xelz's blog</p>
<p><a href="https://www.jianshu.com/p/ef0ff6ee6bc6" title="从Mach-O角度谈谈Swift和OC的存储差异" target="_blank" rel="nofollow noopener noreferrer">从Mach-O角度谈谈Swift和OC的存储差异</a> -- 来自简书：皮拉夫大王在此</p>
<p><a href="https://www.jianshu.com/p/0cbbbe783ac9" title="一种Swift Hook新思路——从Swift的虚函数表说起" target="_blank" rel="nofollow noopener noreferrer">一种Swift Hook新思路——从Swift的虚函数表说起</a> -- 来自简书：皮拉夫大王在此</p>
<p><a href="https://juejin.cn/post/6844903889523884039" title="Swift5.0 的 Runtime 机制浅析" target="_blank">Swift5.0 的 Runtime 机制浅析</a> -- 来自掘金：欧阳大哥2013</p>
<p><a href="https://mp.weixin.qq.com/s/ZTxVG6KG-4vzbvclC_Q1LQ" title="编译原理初学者入门指南" target="_blank" rel="nofollow noopener noreferrer">编译原理初学者入门指南</a> -- 来自公众号：腾讯技术工程</p>
<p><a href="https://mp.weixin.qq.com/s/DN-ckM1YrPMeicN7P9FvXg" title="神秘！申请内存时底层发生了什么？" target="_blank" rel="nofollow noopener noreferrer">神秘！申请内存时底层发生了什么？</a> -- 来自公众号：码农的荒岛求生</p>
<p><a href="https://tech.meituan.com/2020/04/23/read-book-2020-04-23.html" title="推荐收藏 | 美团技术团队的书单" target="_blank" rel="nofollow noopener noreferrer">推荐收藏 | 美团技术团队的书单</a> -- 来自博客：美团技术团队</p>
<p><a href="https://tech.meituan.com/2020/05/04/meituan-0504-young-people.html" title="青年人在美团是怎样成长的？" target="_blank" rel="nofollow noopener noreferrer">青年人在美团是怎样成长的？</a> -- 来自博客：美团技术团队</p>
<h2 data-id="heading-11">学习资料</h2>
<h3 data-id="heading-12">一个人工智能的诞生</h3>
<p>地址：<a href="https://jibencaozuo.com/product/1/episode/0%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">jibencaozuo.com/product/1/e…</a></p>
<p>由回形针制作的人工智能交互视频课程，对，可交互的视频，这种可交互性作为学习还是非常棒的。视频质量很高，趣味性也很强。你可以1元体验第一个章节，如果认为很不错，需要支付49元解锁剩余内容。</p>
<p>作者在每个章节都会设计一些问题，答对了才能进到下一章节。前面几节在讲人工智能学习的一些概念和核心数学思想，最后的两个章节属于练习题，我感觉还是有点难的。但课程整体还是很有意思的，如果想了解可以买来看看。下图是课程的目录：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed1701a355284fce881468a578c258d0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">工具推荐</h2>
<p>推荐好用的工具。</p>
<h3 data-id="heading-14">P4Merge</h3>
<p><strong>推荐来源</strong>：zhangferry</p>
<p><strong>地址</strong>：<a href="https://www.perforce.com/downloads/visual-merge-tool" target="_blank" rel="nofollow noopener noreferrer">www.perforce.com/downloads/v…</a></p>
<p><strong>软件状态</strong>：对开发者免费</p>
<p><strong>使用介绍</strong></p>
<p>非常强大的可视化diff工具，如果你嫌<a href="https://kaleidoscope.app/" target="_blank" rel="nofollow noopener noreferrer">Kaleidoscope</a>太贵的话，可以用它做代替品。我们可以把它集成进git，通常diff工具有两个作用一个是作为difftool，一个是作为mergetool。配置流程如下：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> difftool</span>
<span class="hljs-meta">$</span><span class="bash"> git config --global diff.tool p4merge</span>
<span class="hljs-meta">$</span><span class="bash"> git config --global difftool.p4merge.cmd \
<span class="hljs-string">"/Applications/p4merge.app/Contents/Resources/launchp4merge \$LOCAL \$REMOTE"</span></span>
<span class="hljs-meta">#</span><span class="bash"> mergetool</span>
<span class="hljs-meta">$</span><span class="bash"> git config --global merge.tool p4merge</span>
<span class="hljs-meta">$</span><span class="bash"> git config --global mergetool.p4merge.cmd <span class="hljs-string">"/Applications/p4merge.app/Contents/MacOS/p4merge <span class="hljs-variable">$PWD</span>/<span class="hljs-variable">$BASE</span> <span class="hljs-variable">$PWD</span>/<span class="hljs-variable">$LOCAL</span> <span class="hljs-variable">$PWD</span>/<span class="hljs-variable">$REMOTE</span>"</span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以下是作为mergetool的界面，下面内容为最终合并的内容，我们可以通过右侧的扩展按钮选择当前应该选择哪个分支的内容。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d1e2bc6509c4b5e864732a78dc05871~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">ProfilesManager</h2>
<p><strong>推荐来源</strong>：<a href="https://github.com/jcexk" target="_blank" rel="nofollow noopener noreferrer">jcexk</a></p>
<p><strong>地址</strong>：<a href="https://github.com/shaojiankui/ProfilesManager/releases" target="_blank" rel="nofollow noopener noreferrer">github.com/shaojiankui…</a></p>
<p><strong>软件状态</strong>：免费，开源</p>
<p><strong>使用介绍</strong></p>
<p>一款Provisioning Profile管理工具，ProfilesManager特点如下：</p>
<ol>
<li>方便快捷：支持查看电脑中所有的描述文件</li>
<li>一目了然：通过美化描述文件名，不再是难以辨认的'uuid+ext'格式</li>
<li>功能强大：支持查看ipa中描述文件和info.plist信息</li>
<li>结构清晰：通过树状结构查看描述文件包含的详细信息，如：创建时间、失效时间和包含的移动设备信息等</li>
<li>免费使用：而在App Store上类似功能的软件居然还要收费？？？</li>
<li>可排序和过滤：通过关键词筛选过滤找到想要的文件，也可以通过头部标签排序文件</li>
</ol>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf343083f46b4e0584288bd0c9a26253~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">联系我们</h2>
<p><a href="https://zhangferry.com/2021/01/10/iOSWeeklyLearning_3/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第三期</a></p>
<p><a href="https://zhangferry.com/2021/01/24/iOSWeeklyLearning_4/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第四期</a></p>
<p><a href="https://zhangferry.com/2021/02/28/iOSWeeklyLearning_5/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第五期</a></p>
<p><a href="https://zhangferry.com/2021/03/14/iOSWeeklyLearning_6/" target="_blank" rel="nofollow noopener noreferrer">摸鱼周报第六期</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            