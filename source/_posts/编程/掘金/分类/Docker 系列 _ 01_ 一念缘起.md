
---
title: 'Docker 系列 _ 01_ 一念缘起'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff404c4bcd684d818ee52e1c57ad544d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 07:07:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff404c4bcd684d818ee52e1c57ad544d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第27天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<blockquote>
<p>人们只有在经历过诸多痛苦之后，才会相信这“缘分”的存在。
而所有的“缘分”，只不过是事物发展的必然结果罢了。</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>在生产环境配置日益复杂的今天，一套统一的、可移植的环境可能是很多从业人员梦寐以求的。所谓“需求引领市场”，在需求的催动下，解决方案的诞生也只是时间问题而已。</p>
<h2 data-id="heading-1">开发测试的苦</h2>
<ul>
<li>
<ol>
<li>搭环境</li>
</ol>
</li>
<li>
<ol start="2">
<li>换电脑</li>
</ol>
</li>
<li>
<ol start="3">
<li>写文档</li>
</ol>
</li>
<li>
<ol start="4">
<li>搞适配</li>
</ol>
</li>
</ul>
<p>所有程序代码的执行都需要依赖于具体的系统环境，所以，在项目开发之初，搭建相应的开发环境是必不可少的步骤。任何不以环境为根据的代码开发都是耍流氓。</p>
<p>如果是一开始就跟着项目走的话，那还好，至少环境都是逐步完善过来的。但要是中途加入的话，遇到复杂项目，那就别提了，说多了都是泪，光一个环境搭建都能搞得你腰酸背痛外加腿抽筋。</p>
<blockquote>
<p>本人亲历：在项目做到一大半的时候，被借调去支援其他项目，历时大概三个月左右。回来后的状况可以用一句话来概括——一顿操作猛如虎，一看结果二百五！啥？！单点登录？时候加的？PG库，怎么来的......配！配！配！当项目终于能正常跑起来的时候，我脑海中只有一个念头：项目别三月，见面不相识！</p>
</blockquote>
<p>哎，听说最近有种新技术挺火的......试问你能忍得了这诱惑？我只相信，没有不喜欢“偷腥”的程序猿，忍得住才怪了（手动白眼）。又到了搭环境的时候了，左手npm，右手brew，还有什么搞不定的，“偷腥”成功的成就感那是相当爆棚啊！</p>
<p>等等，先别急着兴奋，骚年！我且问你两个问题：</p>
<pre><code class="copyable">- 1. 你主机中现在装了多少包？
- 2. 有同事要跟你协同开发，你怎么给他搭建出一个跟你这一模一样的环境？
<span class="copy-code-btn">复制代码</span></code></pre>
<p>嘿，我这主机中各种各样的包和服务都有，具体数目我都数不过来（一脸嘚瑟样）！至于协同开发，那还不简单，我写一个文档，只要按照文档一步步走下去，保证能配置出来！再或者，我配置一个虚拟机，有谁需要开发环境，我只要给他拷出一份虚拟机镜像不就完了。</p>
<p>嗯，我且不怀疑你永远能及时更新文档的毅力，也不质疑有些公司的电脑配置，在运行虚拟机之后，除了卡顿不知道还能干啥......我只想问你：你不觉得你主机目前的状态有点类似于“大杂烩”吗？说好的程序猿的条理性呢？有了条理，我们至少还能当斑马（搬码），没了条理，那只能作一团乱麻了！</p>
<h2 data-id="heading-2">运维管理的累</h2>
<ol>
<li>易出错</li>
<li>不一致</li>
<li>启动杂</li>
<li>效率低</li>
</ol>
<p>作为运维人员，最常听到的一句话是什么？要我来说，绝对是“在我这里好好的，到你那里怎么就不行了呢？”最常说的一句话是什么？我想大概或许也是这句吧。</p>
<p>累死累活、加班加点地才搞定了部署的问题，还没来得及歇一口气，又有新的补丁包发过来了。得，还得拼命！</p>
<p>很多运维人员的真实写照大概是：不是在调环境，就是在调环境的路上。</p>
<h2 data-id="heading-3">出路</h2>
<p>由于各种各样的原因，我们常常会把一件脑力活给干成体力活。愉悦感成就感没了不说，还得搭上黑眼圈和“地中海”。</p>
<p>直到这时，我们或许会感慨：还是”CV 大法“好！</p>
<p>古话说：穷则变，变则通。人啊，只有被逼到一定地步了，才会想着去改变，寻找出路，安逸的环境基本不可能滋养出”思变“的野心和欲望。眼看这体力跟不上了，头顶的光芒越发耀眼了，就知道该到了寻求改变的时候了。</p>
<p>那到底有没有”一次配置，终生受益“的解决方案呢？</p>
<h3 data-id="heading-4">虚拟机</h3>
<p>首先，最容易想到的和接触最多的非虚拟机莫属。</p>
<p>虚拟机（virtual machine）就是带环境安装的一种解决方案。它可以在一种操作系统里面运行另一种操作系统，比如在 Windows 系统里面运行 Linux 系统。应用程序对此毫无感知，因为虚拟机看上去跟真实系统一模一样，而对于底层系统来说，虚拟机就是一个普通文件，不需要了就删掉，对其他部分毫无影响。</p>
<p>虽然用户可以通过虚拟机还原软件的原始环境。但是，这个方案有几个缺点。</p>
<p>（1）资源占用多</p>
<p>虚拟机会独占一部分内存和硬盘空间。它运行的时候，其他程序就不能使用这些资源了。哪怕虚拟机里面的应用程序，真正使用的内存只有 1MB，虚拟机依然需要几百 MB 的内存才能运行。</p>
<p>（2）冗余步骤多</p>
<p>虚拟机是完整的操作系统，一些系统级别的操作步骤，往往无法跳过，比如用户登录。</p>
<p>（3）启动慢</p>
<p>启动操作系统需要多久，启动虚拟机就需要多久。可能要等几分钟，应用程序才能真正运行。</p>
<p>既然虚拟机存在这么多缺点，那还有没有更好的解决方案呢？还真有，那就是 Docker 技术。</p>
<p>一念缘起，我与 Docker 的故事从此开始……</p>
<h2 data-id="heading-5">初识 Docker</h2>
<p>就因为这样一个念头，我懵懵懂懂的走进了 Docker 的世界。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff404c4bcd684d818ee52e1c57ad544d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">Docker 是什么？</h3>
<p>Docker 是一个开源的应用容器引擎，让开发者可以打包他们的应用以及依赖包到一个可移植的镜像中，然后发布到任何流行的 Linux 或Windows 机器上，也可以实现虚拟化。容器是完全使用沙箱机制，相互之间不会有任何接口。总结一下就是：</p>
<ul>
<li>Docker 是一个开源的软件部署解决方案；</li>
<li>Docker 也是轻量级的应用容器框架；</li>
<li>Docker 可以打包、发布、运行任何的应用。</li>
</ul>
<h3 data-id="heading-7">Docker 的组成</h3>
<p>一个完整的 Docker 由以下几个部分组成：</p>
<ol>
<li>DockerClient客户端</li>
<li>Docker Daemon守护进程</li>
<li>Docker Image镜像</li>
<li>DockerContainer容器</li>
</ol>
<h3 data-id="heading-8">Docker 的作用</h3>
<p>Docker 的主要用途，目前有三大类。</p>
<p>**（1）提供一次性的环境。**比如，本地测试他人的软件、持续集成的时候提供单元测试和构建的环境。</p>
<p>**（2）提供弹性的云服务。**因为 Docker 容器可以随开随关，很适合动态扩容和缩容。</p>
<p>**（3）组建微服务架构。**通过多个容器，一台机器可以跑多个服务，因此在本机就可以模拟出微服务架构。</p>
<h2 data-id="heading-9">总结</h2>
<p>以上就是我和 Docker “结识”的过程，以及对 Docker 的简单认知，也欢迎大家分享自己和 Docker 结缘的过程。</p>
<p>~</p>
<p>~ 本文完，感谢阅读！</p>
<p>~</p>
<blockquote>
<p>学习有趣的知识，结识有趣的朋友，塑造有趣的灵魂！</p>
<p>大家好，我是〖<a href="https://juejin.cn/user/2893570333750744/posts" target="_blank" title="https://juejin.cn/user/2893570333750744/posts">编程三昧</a>〗的作者 <strong>隐逸王</strong>，我的公众号是『<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fyinyiwang%2FblogImages%2Fraw%2Fmaster%2Fimages%2F20210604%2520%2F19-26-03-txvEvM.png" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/yinyiwang/blogImages/raw/master/images/20210604%20/19-26-03-txvEvM.png" ref="nofollow noopener noreferrer">编程三昧</a>』，欢迎关注，希望大家多多指教！</p>
<p>你来，怀揣期望，我有墨香相迎！ 你归，无论得失，唯以余韵相赠！</p>
<p>知识与技能并重，内力和外功兼修，理论和实践两手都要抓、两手都要硬！</p>
</blockquote></div>  
</div>
            