
---
title: 'Cloudreve 自建云盘实践，我说了没人能限得了我的容量和速度！'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70ab3125d9f24f70a2f23d23bb6db78b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Apr 2021 17:22:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70ab3125d9f24f70a2f23d23bb6db78b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者：小傅哥
<br>博客：<a href="https://bugstack.cn/" target="_blank" rel="nofollow noopener noreferrer">bugstack.cn</a></p>
<blockquote>
<p>沉淀、分享、成长，让自己和他人都能有所收获！😄</p>
</blockquote>
<h2 data-id="heading-0">一、前言</h2>
<p><code>为啥要用自建网盘，市面上的云盘不香了？</code></p>
<p>每一个用户需求的背后都是因为有场景存在，而这些差异化的场景也都是因为不同的用户类型产生的。</p>
<p>就像我作为技术号主想分享一些自己总结的资料，放到一些云盘以后有时候会被其他不知道从哪冒出来的小伙伴给举报，举报链接就取消了，取消了链接也就影响了我的资料分享。同时我可能还希望我的分享内容能被记录到下载次数、允许几次下载、下载时是否要做一些引流动作等等。</p>
<p>所以类似这样的特殊场景下就需要自建网盘来维护个人需要的资料，与之类似的还有一些公司或者组织都会建相对私域的网盘功能服务功能，给予内部用户使用。</p>
<p><strong>所以</strong>，也并不一定市面的网盘不香了，只是因为我有需要自建网盘。在这条路上我尝试过自建、kodexplorer、Owncloud等，恰巧最近发现了 Cloudreve 尝试体验后感觉更香，支持的功能更多。所以准备给小伙伴分享下关于 Cloudreve 的安装、配置和使用，也让有需要的小伙伴可以尝尝鲜。</p>
<h2 data-id="heading-1">二、Cloudreve 介绍</h2>
<p><strong>Cloudreve</strong>，帮助您以最低的成本快速搭建公私兼备的网盘系统。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70ab3125d9f24f70a2f23d23bb6db78b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">🔉 功能</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba0f9e64c5604460a1a711370e0cb5f4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">✨ 特性</h3>
<ul>
<li>☁️ 支持本机、从机、七牛、阿里云 OSS、腾讯云 COS、又拍云、OneDrive (包括世纪互联版) 作为存储端</li>
<li>📤 上传/下载 支持客户端直传，支持下载限速</li>
<li>💾 可对接 Aria2 离线下载</li>
<li>📚 在线 压缩/解压缩、多文件打包下载</li>
<li>💻 覆盖全部存储策略的 WebDAV 协议支持</li>
<li>⚡ 拖拽上传、目录上传、流式上传处理</li>
<li>🗃️ 文件拖拽管理</li>
<li>👩‍👧‍👦 多用户、用户组</li>
<li>🔗 创建文件、目录的分享链接，可设定自动过期</li>
<li>👁️‍🗨️ 视频、图像、音频、文本、Office 文档在线预览</li>
<li>🎨 自定义配色、黑暗模式、PWA 应用、全站单页应用</li>
<li>🚀 All-In-One 打包，开箱即用</li>
</ul>
<h3 data-id="heading-4">📌 资料</h3>
<ol>
<li>官网：<a href="https://cloudreve.org/" target="_blank" rel="nofollow noopener noreferrer">cloudreve.org</a></li>
<li>文档：<a href="https://docs.cloudreve.org/getting-started/install" target="_blank" rel="nofollow noopener noreferrer">docs.cloudreve.org/getting-sta…</a></li>
<li>社区：<a href="https://forum.cloudreve.org/" target="_blank" rel="nofollow noopener noreferrer">forum.cloudreve.org</a></li>
<li>源码：<a href="https://github.com/cloudreve/Cloudreve" target="_blank" rel="nofollow noopener noreferrer">github.com/cloudreve/C…</a></li>
<li>演示：<a href="https://demo.cloudreve.org/" target="_blank" rel="nofollow noopener noreferrer">demo.cloudreve.org</a></li>
</ol>
<h2 data-id="heading-5">三、环境准备</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ffbf76d0ada49ef8d058a7ef87f54d6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>云服务器资源或本地服务器，推荐腾讯云轻量服务器，内含宝塔组件，算是是几个云服务里最简单的：<a href="https://console.cloud.tencent.com/lighthouse/instance/index" target="_blank" rel="nofollow noopener noreferrer">console.cloud.tencent.com/lighthouse/…</a></li>
<li>已备案过的域名，如果不需要域名访问，可以直接使用云服务提供的公网IP</li>
<li>Cloudreve安装包：<a href="https://github.com/cloudreve/Cloudreve/releases" target="_blank" rel="nofollow noopener noreferrer">github.com/cloudreve/C…</a></li>
</ol>
<p><em>本章节的案例是基于腾讯云的，如果你使用的是其他云服务器，找到对应的位置配置即可。这些云服务使用方式基本大同小异，遇到问题可以联系对应的云服务客服，不要联系我哈哈哈😄</em></p>
<h2 data-id="heading-6">四、宝塔配置</h2>
<p>宝塔是一个简单好用的Linux/Windows服务器运维管理面板，在宝塔后台页面上可以非常方便的安全软件和配置环境。一般可以在云服务器上安装宝塔，有一些厂商也把宝塔集成到自己的云服务器上了。</p>
<h3 data-id="heading-7">1. 获取用户名和密码</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13307c173dd3477daa385dd2ad59a7a8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>地址：<a href="https://console.cloud.tencent.com/lighthouse/instance/detail?rid=8&id=lhins-90pixwzq&tab=application" target="_blank" rel="nofollow noopener noreferrer">console.cloud.tencent.com/lighthouse/…</a></li>
<li>进入服务的应用管理会看到<code>应用内软件信息：宝塔</code>，在这里点击<strong>登录</strong>按钮后，会获取到宝塔的登录地址、用户名和密码信息「<em>这些信息可以后期在宝塔后台修改</em>」。
<pre><code class="hljs language-java copyable" lang="java"> * Socket connection established *
 Last login: Sat Apr <span class="hljs-number">10</span> 09:<span class="hljs-number">33</span>:<span class="hljs-number">50</span> <span class="hljs-number">2021</span> from <span class="hljs-number">119.29</span><span class="hljs-number">.96</span><span class="hljs-number">.147</span>
 [lighthouse<span class="hljs-meta">@VM</span>-<span class="hljs-number">8</span>-<span class="hljs-number">9</span>-centos ~]$ sudo /etc/init.d/bt <span class="hljs-keyword">default</span>
 ==================================================================
 BT-Panel <span class="hljs-keyword">default</span> info!
 ==================================================================
 外网面板地址: http:<span class="hljs-comment">//80.71.255.122:8888/cloudtencent</span>
 内网面板地址: http:<span class="hljs-comment">//10.0.8.9:8888/cloudtencent</span>
 *以下仅为初始默认账户密码，若无法登录请执行bt命令重置账户/密码登录
 username: 3kkjecc3
 password: 3f7d2743018b
 If you cannot access the panel,
 release the following panel port [<span class="hljs-number">8888</span>] in the security group
 若无法访问面板，请检查防火墙/安全组是否有放行面板[<span class="hljs-number">8888</span>]端口
 ==================================================================
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-8">2. 8888 端口授权</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52c205c0ad7442ea9ecd27acb0242d0b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>在获取到面板的用户名和密码后，还不能直接访问，因为你的端口还没有授权开通。</li>
<li>这时可以在云服务平台上，点击<code>防火墙</code>这个配置，添加 8888 端口。</li>
</ul>
<h3 data-id="heading-9">3. 登录宝塔后台</h3>
<p>地址：<a href="http://80.71.255.122:8888/cloudtencent" target="_blank" rel="nofollow noopener noreferrer">http://80.71.255.122:8888/cloudtencent</a> - <code>你需要更换为自己的地址</code>
说明：在初次进入宝塔时会有一些提示和软件安装，选择自己需要的安装即可。
页面：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba595a1a7a764333ad7d27a99ef34feb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">五、服务安装</h2>
<p>在宝塔面板的左侧菜单栏有一个终端菜单，点击进入是一个黑窗口，接下来我们就在这里安装整个服务。</p>
<h3 data-id="heading-11">1. 在宝塔终端查看服务内核</h3>
<p>因为不同云服务下可能是 adm 或者 arm 架构，对应下载的 Cloudreve 也会有所不同 <code>cloudreve_版本号_操作系统_CPU架构.tar.gz</code>，所以这里我们需要使用 <code>arch</code> 命令查看下服务信息。</p>
<pre><code class="hljs language-java copyable" lang="java">Last failed login: Sat Apr <span class="hljs-number">10</span> <span class="hljs-number">11</span>:<span class="hljs-number">38</span>:<span class="hljs-number">41</span> CST <span class="hljs-number">2021</span> from <span class="hljs-number">194.165</span><span class="hljs-number">.16</span><span class="hljs-number">.68</span> on ssh:notty
There were <span class="hljs-number">8</span> failed login attempts since the last successful login.
Last login: Sat Apr <span class="hljs-number">10</span> 09:<span class="hljs-number">57</span>:<span class="hljs-number">33</span> <span class="hljs-number">2021</span> from <span class="hljs-number">127.0</span><span class="hljs-number">.0</span><span class="hljs-number">.1</span>
[root<span class="hljs-meta">@VM</span>-<span class="hljs-number">8</span>-<span class="hljs-number">9</span>-centos ~]# arch
x86_64
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>x86_64：代表 amd64</li>
<li>aarch64：代表 arm64</li>
</ul>
<h3 data-id="heading-12">2. 下载和安装</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5853e46e7f61472db95b0afda7825d3e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>确定好我们的云服务架构后，选择对应的 Cloudreve 版本，复制地址。我的是：<a href="https://github.com/cloudreve/Cloudreve/releases/download/3.3.1/cloudreve_3.3.1_linux_amd64.tar.gz" target="_blank" rel="nofollow noopener noreferrer">github.com/cloudreve/C…</a></p>
<p><strong>安装命令</strong></p>
<pre><code class="hljs language-java copyable" lang="java">mkdir /www/wwwroot/cloudreve    # 创建一个新文件夹存放程序
cd /www/wwwroot/cloudreve           # 进入这个文件夹
wget https:<span class="hljs-comment">//github.com/cloudreve/Cloudreve/releases/download/3.3.1/cloudreve_3.3.1_linux_amd64.tar.gz # 下载你复制的链接</span>
tar -zxvf cloudreve_3<span class="hljs-number">.3</span>.1_linux_amd64.tar.gz   # 解压获取到的主程序
chmod +x ./cloudreve                           # 赋予执行权限
./cloudreve                                  # 启动 Cloudreve

# 运行信息截取
[Info]    <span class="hljs-number">2021</span>-<span class="hljs-number">04</span>-<span class="hljs-number">10</span> <span class="hljs-number">10</span>:<span class="hljs-number">39</span>:<span class="hljs-number">59</span> 初始化数据库连接
[Info]    <span class="hljs-number">2021</span>-<span class="hljs-number">04</span>-<span class="hljs-number">10</span> <span class="hljs-number">10</span>:<span class="hljs-number">39</span>:<span class="hljs-number">59</span> 开始进行数据库初始化...
[Info]    <span class="hljs-number">2021</span>-<span class="hljs-number">04</span>-<span class="hljs-number">10</span> <span class="hljs-number">10</span>:<span class="hljs-number">39</span>:<span class="hljs-number">59</span> 初始管理员账号：admin<span class="hljs-meta">@cloudreve</span>.org
[Info]    <span class="hljs-number">2021</span>-<span class="hljs-number">04</span>-<span class="hljs-number">10</span> <span class="hljs-number">10</span>:<span class="hljs-number">39</span>:<span class="hljs-number">59</span> 初始管理员密码：U4BfStlm
[Info]    <span class="hljs-number">2021</span>-<span class="hljs-number">04</span>-<span class="hljs-number">10</span> <span class="hljs-number">10</span>:<span class="hljs-number">40</span>:<span class="hljs-number">00</span> 数据库初始化结束
[Info]    <span class="hljs-number">2021</span>-<span class="hljs-number">04</span>-<span class="hljs-number">10</span> <span class="hljs-number">10</span>:<span class="hljs-number">40</span>:<span class="hljs-number">00</span> 初始化任务队列，WorkerNum = <span class="hljs-number">10</span>
[Info]    <span class="hljs-number">2021</span>-<span class="hljs-number">04</span>-<span class="hljs-number">10</span> <span class="hljs-number">10</span>:<span class="hljs-number">40</span>:<span class="hljs-number">00</span> 初始化定时任务...
[Info]    <span class="hljs-number">2021</span>-<span class="hljs-number">04</span>-<span class="hljs-number">10</span> <span class="hljs-number">10</span>:<span class="hljs-number">40</span>:<span class="hljs-number">00</span> 当前运行模式：Master
[Info]    <span class="hljs-number">2021</span>-<span class="hljs-number">04</span>-<span class="hljs-number">10</span> <span class="hljs-number">10</span>:<span class="hljs-number">40</span>:<span class="hljs-number">00</span> 开始监听 :<span class="hljs-number">5212</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>wget，替换为你的 Cloudreve 地址</li>
<li>tar，是对应名称一起替换</li>
<li>最后把这些命令复制到你的终端黑窗口，它就开始运行安装了。<strong>安装完成以后你会得到一个初始的用户名和密码，复制粘贴保存起来</strong></li>
</ul>
<h3 data-id="heading-13">3. 开放端口 5212</h3>
<ul>
<li>Cloudreve 安装完成以后，访问地址为你的服务IP:5212，但此时5212并不能直接访问还需要授权。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05728953f6ff44d0b549dfd0e9d69fb6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></li>
<li>仅在宝塔后台授权还不够，还需要在云服务平台的防火墙进行授权，如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1537ace8ef0045c99709aa50e21276f1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
<h3 data-id="heading-14">4. 登录服务</h3>
<ul>
<li>地址：<a href="http://80.71.255.122:5212/" target="_blank" rel="nofollow noopener noreferrer">http://80.71.255.122:5212</a></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e9dc46c8c2b45c2aeb0ef3340071d32~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>如果一切顺利现在你就可以使用自己的网盘了，但有一点要知道如果你还需要设置域名，那么这个时候先不要使用，先去设置域名，否则一些图片在IP下上传和在域名下上传，分享是有问题的。</li>
</ul>
<h2 data-id="heading-15">六、进程守护</h2>
<p>其实在服务安装完成后就已经可以正常使用了，但我们很难保证宝塔面板不被重启或者出现异常时也难免要我们自己再启动云盘服务。那么，就需要一个守护进程来自动重启服务。</p>
<p>在宝塔面板的软件商店中，找到 <code>Supervisor</code> 安装。Supervisor是用Python开发的一套通用的进程管理程序，能将一个普通的命令行进程变为后台daemon，并监控进程状态，异常退出时能自动重启。</p>
<h3 data-id="heading-16">1. Supervisor 配置</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa15af94d9d146b1866762344939d9ed~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>名称：Cloudreve</li>
<li>启动用户：root <em>默认的</em></li>
<li>运行目录：/www/wwwroot/cloudreve/</li>
<li>启动命令：/www/wwwroot/cloudreve/cloudreve</li>
</ul>
<h3 data-id="heading-17">2. Supervisor 启动</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e78a1bfc7e34a6186af125ea9189f86~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>配置守护进程后，点开宝塔面板右上角的重启，进入后<code>重启服务</code></li>
<li>重启后再进入到宝塔面板就会看到守护进程已经在启动了，现在启动这个事就交给了 Supervisor 管理</li>
</ul>
<h2 data-id="heading-18">七、配置域名</h2>
<h3 data-id="heading-19">1. 解析域名</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b5adccf52c44c5bab11bdd84396fd8b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>在配置域名之前，需要在你已经准备好的域名下配置一个A记录解析，这样后面才能配置反向代理。</li>
</ul>
<h3 data-id="heading-20">2. 反向代理</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56aea748dfcc4262ba1f61c110f56d3f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>点击宝塔面板左侧菜单中的<code>网站</code>按钮，添加一个站点。站点里的域名就是配置解析域名时的信息，我的是<code>pan.itedus.cn</code></li>
<li>配置完站点后就需要给这个站点设置一个反向代理，点击它的设置即可进入。在反向代理中添加并设置目标URL：127.0.0.1:5212</li>
<li>最后，如果你的域名已经解析完成，那么现在你就可以通过域名访问你的云盘服务了，还可以上传和分享文件。例如我分享的文件：<a href="http://pan.itedus.cn/s/qofO" target="_blank" rel="nofollow noopener noreferrer">pan.itedus.cn/s/qofO</a></li>
</ul>
<h2 data-id="heading-21">八、数据库切换</h2>
<p>系统默认的数据库是自带的 SQLite，你可改为 Mysql，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af4561b8f8374326998d37889185569d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>数据库类型，目前支持 sqlite | mysql</li>
</ol>
<p>Type = mysql
2. 用户名
User = Cloudreve
3. 密码
Password = Cloudreve
4. 数据库地址
Host = 127.0.0.1
5. 数据库名称
Name = Cloudreve
6. 数据表前缀
TablePrefix = cd_</p>
<ul>
<li>切换完记得使用命令的方式进行重启，因为此时它需要重新创建账号和密码</li>
<li>如果你没有看见账号和密码，那么可以把创建的数据库删掉，重新来一次</li>
</ul>
<h2 data-id="heading-22">九、总结</h2>
<ul>
<li>关于 Cloudreve 云盘的安装和使用就演示到这里了，如果你感兴趣也可以自己搭建一个。另外 Cloudreve 可以获取到它的源码，在源码的基础上可以添加一些想要的功能，比如在下载的时候设置为关注某些东西在下载等等。</li>
<li>除了 Cloudreve 云盘还可以尝试下有道云，这个云盘直接在简单的服务器上就可以直接安装，也可以自动升级，使用起来会简单一些。</li>
<li>无论是云服务还是各类工具，多尝试一些这样的东西，可以给自己增加很多其他知识面的理解。也许弄着弄着，你就不只是一个简单的CRUD开发工程师了，可能还是运维、产品、业务！</li>
</ul>
<h2 data-id="heading-23">十、系列推荐</h2>
<ul>
<li><a href="https://bugstack.cn/itstack-demo-any/2020/05/10/%E8%87%AA%E5%BB%BA%E4%BA%91%E7%9B%98%E5%AD%98%E5%82%A8PDF%E4%B9%A6%E7%B1%8D%E6%94%AF%E6%8C%81%E5%9C%A8%E7%BA%BF%E9%A2%84%E8%A7%88%E5%92%8C%E4%B8%8B%E8%BD%BD.html" target="_blank" rel="nofollow noopener noreferrer">另外一种可道云网盘的搭建，也很不错</a></li>
<li><a href="https://bugstack.cn/itstack-code-life/2021/01/24/%E4%B8%80%E5%A4%A9%E5%BB%BA4%E4%B8%AA-%E5%B0%8F%E5%82%85%E5%93%A5%E6%95%99%E4%BD%A0%E6%90%AD%E5%8D%9A%E5%AE%A2.html" target="_blank" rel="nofollow noopener noreferrer">一天建4个，小傅哥教你搭博客！</a></li>
<li><a href="https://bugstack.cn/itstack-code-life/2020/10/11/%E4%B8%BA%E4%BA%86%E7%9C%81%E9%92%B1-%E6%88%91%E7%94%A81%E5%A4%A9%E6%97%B6%E9%97%B4%E6%8A%8APHP%E5%AD%A6%E4%BA%86.html" target="_blank" rel="nofollow noopener noreferrer">为了省钱，我用1天时间把PHP学了！</a></li>
<li><a href="https://bugstack.cn/itstack-code-life/2020/03/28/GithubAndMyBlogAttacked.html" target="_blank" rel="nofollow noopener noreferrer">Github被攻击。我的GitPage博客也挂了，紧急修复之路，也教会你搭建 Jekyll 博客！</a></li>
<li><a href="https://bugstack.cn/itstack-demo-netty-3/2020/03/04/Netty+JavaFx%E5%AE%9E%E6%88%98-%E4%BB%BF%E6%A1%8C%E9%9D%A2%E7%89%88%E5%BE%AE%E4%BF%A1%E8%81%8A%E5%A4%A9.html" target="_blank" rel="nofollow noopener noreferrer">Netty+JavaFx实战：仿桌面版微信聊天</a></li>
</ul></div>  
</div>
            