
---
title: '我用 Mac M1 玩转 Spring Cloud｜Java 开发实战'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/862369df047f484d88de3cb12962a021~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 31 May 2021 16:13:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/862369df047f484d88de3cb12962a021~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第 1 天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>”</p>
<p>本文正在参加「Java主题月 - Java 开发实战」，详情查看 <a href="https://juejin.cn/post/6968267217121050660/" target="_blank">活动链接</a></p>
<p>我的开源 Spring Cloud 项目 <code>PassJava</code> 一直可以在 Windows 上正常运行，最近不是换 <code>Mac M1</code> 了么，想把这个项目在 M1 上跑起来，毕竟我的那台 Windows 用起来发烫，是该体验下 M1 的性能了。</p>
<p>因为 <code>M1</code> 的<strong>兼容性不好</strong>，所以在从 0 开始跑这个项目的遇到了很多问题，比如 MySQL 工具经常打不开，前端 Vue 项目起不来，所以专门针对这些疑难杂症，我也做好了记录，相信对使用 M1 的同学有帮助。</p>
<p>我把后端、前端、小程序都上传到同一个仓库里面了，大家可以通过 <code>github</code> 或 <code>码云</code>访问。地址如下：</p>
<blockquote>
<p><strong>Github</strong>: <a href="https://github.com/Jackson0714/PassJava-Platform" target="_blank" rel="nofollow noopener noreferrer">github.com/Jackson0714…</a></p>
<p><strong>码云</strong>：<a href="https://gitee.com/jayh2018/PassJava-Platform" target="_blank" rel="nofollow noopener noreferrer">gitee.com/jayh2018/Pa…</a></p>
<p><strong>配套教程</strong>：<a href="http://www.passjava.cn/" target="_blank" rel="nofollow noopener noreferrer">www.passjava.cn</a></p>
</blockquote>
<p>整体的架构图如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/862369df047f484d88de3cb12962a021~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>本文主要内容如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e8c24f798ad4909b1a52707b5772fed~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">一、配置 Nacos</h2>
<p>Nacos 作为配置中心和注册中心，是必须要启动的。</p>
<h3 data-id="heading-1">1.1 下载地址</h3>
<p>Nacos 下载地址：</p>
<pre><code class="hljs language-http copyable" lang="http">https://github.com/alibaba/nacos/releases
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最新版是 2.0.0-bugfix，我下载后，启动成功了，但是无法访问 Nacos 后台，怀疑是本地环境有问题，所以换了一个低版本的 1.4.1，可以正常工作。另外我之前在 windows 机器上使用的 1.2.1 的版本，拷贝到 Mac 上也能正常运行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7ab3bfdc87248cf8a56b8579fa4bcf1~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210415202053473" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">1.2 启动 Nacos</h3>
<p>进入 nacos 根目录，执行命令：</p>
<pre><code class="hljs language-sh copyable" lang="sh">sh startup.sh -m standalone
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行后的结果如下图所示：</p>
<p>看到 nacos is starting withi standalone 就表示启动成功。注意：启动成功不代表正常运行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0780d94fc4b442259f963149d232fbe0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来访问 nacos 的后台管理系统：</p>
<pre><code class="hljs language-http copyable" lang="http">http://127.0.0.1:8848/nacos/#/login
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31a77c74904f4d22944ba00fd81cfdc5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>账号和密码都是 <code>nacos</code>。</p>
<h3 data-id="heading-3">1.3 添加命名空间</h3>
<p>添加 7 个微服务的命名空间：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/876a2553545a4f918405204271b85137~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>新建命名空间时需要填写的字段：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3ad1af287204419bc669f7634ca6b74~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">1.4 添加 question 微服务配置</h3>
<p>在配置列表添加几个微服务的配置，目前保证 question 微服务和 thirdparty 微服务有配置即可。</p>
<p>如下图所示，添加三个配置项：数据源，mybatis 配置，其他配置。详细的配置参数参照这篇来配置：<code>《SpringCloud整合Nacos配置中心》</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa8c43ebd2e64141b005fc26a34f65e0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">1.5 添加 thirdparty 微服务配置</h3>
<p>主要是配置阿里云 OSS，用来保存图片的。配置如下图所示，key 需要大家到自己登陆到阿里云并申请 OSS 才能获取到。参照这篇<code>《SpringCloud整合OSS对象存储》</code>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99be43148052447f9d1d176fed84fa7d~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210419211116806" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">二、初始化数据</h2>
<p>创建数据库、表、初始化数据这些工作都需要做，下载一个 MySQL 客户端还是要方便点，然后找 Mac 上好用的客户端软件，下面是安装软件的艰辛历程。</p>
<h3 data-id="heading-7">1.1 安装 Mac 版 MySQL</h3>
<p>首先需要安装 mac 版的 MySQL，下载地址：</p>
<pre><code class="hljs language-http copyable" lang="http">https://dev.mysql.com/downloads/mysql/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>选择第一个就可以了，官网已经提示该版本兼容 Mac M1</p>
<pre><code class="copyable">Packages for Catalina (10.15) are compatible with Big Sur (11)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14c83d1d39664e39ad0806267e7eefc1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下载后点击安装，安装成功后，到系统偏好配置里面找到 MySQL，并单击打开。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d2637b1baa643928eb5cbaa65d08351~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到运行的 MySQL 实例是 MySQL 8.0.23，且默认开机运行。</p>
<p>![]<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8214754cf844e849b2a80ce9ba94b4f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">2.2 安装 Mac 版图形化 MySQL 界面</h3>
<h4 data-id="heading-9">2.2.1 Workbench 在 M1 上不能运行</h4>
<p>我试过安装 workbench 后，不能运行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8abba6f5cb9c4978bd95dfd0cfdfc57b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">2.2.2  Squel Pro 在 M1 上不能运行</h4>
<p>安装 Squel Pro 后，切换数据库的时候程序崩溃。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c041fa2ef7841a791736d3a9dea805c~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210416173839710" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">2.2.3 Navicat</h4>
<p>经过上面两个软件的崩溃后，我最后还是下载了试用版的 Navicat，可以免费用 14 天，对于初始化数据足够了。</p>
<p>下载地址：</p>
<pre><code class="hljs language-sh copyable" lang="sh">http://www.navicat.com.cn/download/navicat-for-mysql
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下载 macOS 的最新版 15，它是兼容 M1 芯片的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0eca074e6d81402d98488f05f762bbac~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后需要执行三个 SQL 文件，文件我已经上传到仓库上了，</p>
<pre><code class="hljs language-sh copyable" lang="sh">/passjava-platform/data/sql
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acaf5478cfa1406aaba2682f0c0ac5aa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>依次执行上面的三个文件后，会生成 6 个数据库，一个系统数据库，五个业务数据库。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61a153c2cb764131b0acd27a7ed6cc21~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">三、启动微服务</h2>
<p>主要启动 4 个核心服务：<code>网关微服务</code>、<code>题目微服务</code>、<code>第三方微服务</code>、<code>系统管理微服务</code>。</p>
<p>架构图如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1e1fffcb80c48f7867853ab89416742~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>目前这几个微服务已经整合了 Nacos、OpenFeign、Gateway、统一异常处理、链路追踪，Redis 等。</p>
<p>启动都是基于 IDEA 开发工具直接启动的，所以需要下载 IDEA。</p>
<h3 data-id="heading-13">3.1 下载安装 IDEA</h3>
<p>我安装的 IDEA 是旗舰版 2020.3 的，试用版 30 天。大家可以下载免费的社区版 Community，功能上也能满足。</p>
<p>性能非常快，我的 Windows 的配置：ThinkPad、 32 G 内存、1T 固态硬盘，启动一个微服务需要 10 秒以上。而 <code>Mac 只需要 3 秒</code>。</p>
<p>官网下载地址：</p>
<pre><code class="hljs language-sh copyable" lang="sh">https://www.jetbrains.com/idea/download/<span class="hljs-comment">#section=mac</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f83ab4ac75534ba5a4ee4c6a15450f24~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">3.2 启动系统管理服务</h3>
<p>我们的后台框架是用的人人框架，主要的功能就是后台的登陆、系统管理功能、所以必须启动 <code>renren-fast</code> 服务才能使用后台管理。</p>
<p>大家可以启动 RenrenApplication 这个 Service，启动成功后，会提示以下信息：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2824be838a94f76bccacae0023557b7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>renren-fast 服务暴露的端口是 8080，但是这个端口对前端是不可见的，前端 API 都是走网关的 8060 端口。将前端的请求转发到 renren-fast 的8060 端口，比如登陆请求。注意：一定要初始化完数据才能启动成功。</p>
<h3 data-id="heading-15">3.3 启动网关</h3>
<p>网关微服务没有什么特殊要求，我都配置好了，直接启动就好了。另外如果遇到端口被占用的情况，可以通过如下命令解决：</p>
<pre><code class="hljs language-sh copyable" lang="sh">lsof -i:8060
<span class="hljs-built_in">kill</span> -9 <进程 id>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>网关微服务暴露的端口是 8060，启动后如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef8d6d2ca86948cf870a38f2cefb329f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">3.4 启动题目服务</h3>
<p>题目服务是核心模块，很多实战案例都是基于这个模块进行讲解的。启动服务之前，需要配置数据库 MySQL 的连接。</p>
<h4 data-id="heading-17">3.4.1 配置数据库连接</h4>
<pre><code class="copyable">文件路径：/passjava-question/src/main/resources/application.yml
spring:
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://127.0.0.1:3306/passjava_qms?useUnicode=true&characterEncoding=utf-8&useSSL=false&serverTimezone=GMT
    username: root
    password: xxx
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外我们也可以通过 nacos 来配置：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/644e64ac55354e24b5027609d7d63a2c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-18">3.4.2 启动题目服务</h4>
<p>IDEA 工具中直接启动就可以了，暴露的端口是 11000，启动后如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40f374bf5a8a4c88aaff02b9a3e71010~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-19">3.4.3 测试题目服务</h4>
<p>用 postman 测试网关+题目微服务是否正常工作：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db689179e2e549678ac01b409f379c1f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于我的数据库中是有数据的，所以会返回很多数据，大家后面可自行添加数据。</p>
<h3 data-id="heading-20">3.5 启动第三方服务</h3>
<p>这个第三方不是指另外一方的服务，而是我把与第三方中间件交互的服务都归在这个服务里面了，比如对阿里云 OSS（对象存储） 的操作。</p>
<p>这个服务的名字叫做：<code>passjava-thirdparty</code>。另外需要注意，OSS 需要大家到阿里云官网申请，有免费额度哦～配置方式可以参照这篇：<code>《SpringCloud整合OSS对象存储》</code></p>
<p>启动成功后，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab1b950c5a0b4cbfa1a78ccd0b1ba00e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-21">四、启动 Admin 后台</h2>
<p>Admin 管理后台的技术选型还是用的 Vue，所以需要使用 npm 工具来安装依赖。</p>
<h3 data-id="heading-22">4.1 安装 npm、nvm</h3>
<p>使用 homebrew 安装 npm</p>
<pre><code class="hljs language-sh copyable" lang="sh">brew install npm
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8b13b18c94c495eb1ed1667014c7a6f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用 homebrew 安装 nvm</p>
<pre><code class="copyable">brew install nvm
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1e6787d70e643bc85e3783141878157~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-23">4.2 切换镜像源</h3>
<p>默认的 npm 使用的是官方的镜像源，我们切换为国内的淘宝镜像源。</p>
<pre><code class="hljs language-sh copyable" lang="sh">npm install -g cnpm --registry=https://registry.npm.taobao.org --verbose
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d14b9df23f34798a32600165f7db055~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-24">4.3 安装 node_module</h3>
<p>仓库里面并没有将依赖包一起上传，因为依赖包太大了，所以可在本地通过如下命令安装依赖包，这个是一次性的，后面不需要再执行。</p>
<p>进入到 passjava-platform/passjava-portal 目录，执行如下命令来安装依赖：</p>
<pre><code class="hljs language-sh copyable" lang="sh">cnpm install
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/006094ce95c04e5996792c6f69cee857~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>启动前端portal</p>
<pre><code class="hljs language-sh copyable" lang="sh">npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>报错，提示 Node Sass 不兼容当前的系统：</p>
<pre><code class="hljs language-sh copyable" lang="sh">Node Sass does not yet support your current environment: OS X Unsupported architecture (arm64) with Unsupported runtime (88)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ec6c6fff85e42849473b4da448156e4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>根据网上提供的解决方案，要先卸载 Node Saas</p>
<pre><code class="hljs language-sh copyable" lang="sh">cnpm uninstall node-sass
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是又提示 chromedriver 安装失败（当前操作系统不兼容），根据网上的解决方案，单独安装，但依旧提示 64 位系统不兼容，于是我把 package.json 文件中的 "chromedriver": "2.27.2" 删掉了，问题迎刃而解！最新的代码已删除该依赖项配置。</p>
<p>先删除之前安装 node_modules</p>
<pre><code class="hljs language-sh copyable" lang="sh">rm -rf ./node_modules/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次执行卸载 node-sass 的命令：</p>
<pre><code class="hljs language-sh copyable" lang="sh">cnpm uninstall node-sass
<span class="copy-code-btn">复制代码</span></code></pre>
<p>卸载成功后，安装 node-sass</p>
<pre><code class="hljs language-sh copyable" lang="sh">cnpm install node-sass  --unsafe-perm --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc439dfeda3b46b4ae14281b35640e3a~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210416224957858" loading="lazy" referrerpolicy="no-referrer"></p>
<p>重新安装依赖</p>
<pre><code class="hljs language-sh copyable" lang="sh">cnpm install
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bba75194685949b7aa13f0b37fe2c86f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-25">4.4 启动后台</h3>
<p>在根目录执行如下命令就可以启动后台了：</p>
<pre><code class="hljs language-sh copyable" lang="sh">npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>启动成功后，会自动打开浏览器，访问的地址是 <a href="http://localhost:8081/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:8081</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/107680fa533943b697ff200b30a11bca~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-26">4.5 登陆后台</h3>
<p>账号密码都是 admin，输入验证码即可登录。注意：如果验证码没有出现，说明 RenrenApplication 微服务有异常，请查看 IDEA 中打印出的 log。</p>
<p>登录后台界面如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2fafe0b6ecd4284be50c0e83924596e~tplv-k3u1fbpfcp-zoom-1.image" alt="PassJava后台" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-27">4.6 添加题目分类</h3>
<p>首先需要给题目进行分类，在后台点击新增类型，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/674d8408e5c74011bef3cda3d8faaa92~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意：上传图片前需要启动 thirdparty 微服务，且 OSS 配置正确。</p>
<h3 data-id="heading-28">4.7 添加面试题</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f401b466f299401587f1cc7255d1ff1a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-29">五、其他</h2>
<h3 data-id="heading-30">5.1 未适配的镜像</h3>
<p>我的开源项目中要用 Elasticsearch 和 Kibana 需要运行在 docker 上，目前这些镜像在 M1 上还未适配。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6b42f23937643b098d221f9729db407~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-31">5.2 前端小程序</h3>
<p>小程序的开发和测试在这里也不演示了， M1 上开发小程序完全没问题～</p>
<h3 data-id="heading-32">5.3 未添加的中间件</h3>
<p>因本篇只是出于核心功能的演示，所以还有些中间件未提及，比如配置 Redis、链路追踪等，这些功能不影响 M1 上使用 Spring Cloud，所以会放在后续的文章中做进一步说明。</p>
<p>下一篇实战 Redis 也安排上了，敬请期待。</p></div>  
</div>
            