
---
title: '深入浅出DevOps：SonarQube提升代码质量'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3244199aedd439b88448648875e7686~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Wed, 07 Sep 2022 04:11:52 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3244199aedd439b88448648875e7686~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;font-family:-apple-system,system-ui,Segoe UI,Roboto,Ubuntu,Cantarell,Noto Sans,sans-serif,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial;color:#00325e&#125;.markdown-body ::selection&#123;background-color:#00325e;color:#fff&#125;.markdown-body blockquote&#123;padding:10px 20px;background-color:#fffaf0;box-shadow:0 3px 10px 0 rgba(255,172,194,.24);border:1px solid #f3ca8e;transition:all .2s;margin:1em 0;border-radius:5px&#125;.markdown-body blockquote p&#123;font-size:14px;line-height:25px;color:#795548&#125;.markdown-body blockquote p:last-child&#123;margin:0&#125;.markdown-body blockquote:hover&#123;border-color:#ff9800;background-color:#fff8e0;box-shadow:0 6px 10px -5px rgba(225,173,98,.3803921569)&#125;.markdown-body blockquote code&#123;color:#ff502c&#125;.markdown-body pre&#123;border:1px solid #8cc0f3;box-shadow:0 3px 10px 0 rgba(255,198,198,.28);border-radius:5px;transition:all .2s;overflow-x:auto;white-space:pre-wrap&#125;.markdown-body pre:hover&#123;border-color:#6d9dce&#125;.markdown-body pre>code&#123;padding:10px 20px;color:#00325e;background:#f0f8ff;font-size:12px;line-height:1.6;display:block&#125;.markdown-body code&#123;background:#f6fbff;color:#0b5393;padding:2px 4px;border-radius:4px;font-size:12px&#125;.markdown-body p&#123;font-size:14px;line-height:28px;text-align:justify;margin-bottom:17px;color:#595959&#125;.markdown-body a&#123;color:#00325e;text-decoration:none&#125;.markdown-body a:after&#123;content:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAQdJREFUKFNt0DtLA0EUBeBzZle0Eks7rcUfEfBRCha7NorYa6NmVJzgyi4smUgKtdZGCJktLMVH4Y8QeztLWyE7VyLEuNFbXj4Oh0P8c8mZm+uJrEN4BJFTeP/MUVe3bnocfALwkOlo1zS7iZAzf6Cx7oXgbaqjxiDEWCcVaGyxQ8pSWo9XhqhoQ/xUFbaKjhe5V+CmR7mnSplEEF6GSmJ+F/d0KHvbCIIJCLc85U6BC5mONgbJNM3uFag++sX7z8O8MzsWBucifMx0dDGE1kmm458KDVukAlnNdDz/exEeW3dNkbfsYC0xtmgDWP6ELLZ0/F6BJu/UoFQN5AkoeUjeJPvx6+i+X5Sjah4tA6gYAAAAAElFTkSuQmCC);margin-left:2px&#125;.markdown-body a:hover&#123;box-shadow:0 1px&#125;.markdown-body table&#123;max-width:100%;border-collapse:collapse;border-spacing:0;box-shadow:0 3px 10px 0 rgba(255,238,172,.24);transition:all .2s&#125;.markdown-body table:hover&#123;box-shadow:0 3px 10px 0 rgba(185,169,103,.24)&#125;.markdown-body table tr th&#123;border:1px solid #8cc0f3;background-color:#f0f8ff;padding:12px 15px&#125;.markdown-body table tr td&#123;border:1px solid rgba(243,202,142,.4);padding:12px 15px&#125;.markdown-body table tbody tr&#123;transition:all .2s&#125;.markdown-body table tbody tr:hover td&#123;border-color:#f3ca8e;background-color:#fff8e0;z-index:1&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body h1&#123;font-size:20px;margin-top:30px;margin-bottom:10px;padding-left:30px;position:relative&#125;.markdown-body h1>code&#123;font-size:20px&#125;.markdown-body h1:before&#123;content:"🍺";display:block;font-size:18px;width:18px;height:18px;left:0;position:absolute&#125;.markdown-body h2&#123;font-size:18px;margin-top:30px;margin-bottom:10px;padding-left:28px;position:relative&#125;.markdown-body h2>code&#123;font-size:18px&#125;.markdown-body h2:before&#123;content:"🍻";display:block;font-size:16px;width:16px;height:16px;left:0;position:absolute&#125;.markdown-body h3&#123;font-size:16px;margin-top:30px;margin-bottom:10px;padding-left:26px;position:relative&#125;.markdown-body h3>code&#123;font-size:16px&#125;.markdown-body h3:before&#123;content:"🥂";display:block;font-size:14px;width:14px;height:14px;left:0;position:absolute&#125;.markdown-body h4&#123;font-size:14px;margin-top:30px;margin-bottom:10px;padding-left:24px;position:relative&#125;.markdown-body h4>code&#123;font-size:14px&#125;.markdown-body h4:before&#123;content:"🥃";display:block;font-size:12px;width:12px;height:12px;left:0;position:absolute&#125;.markdown-body h5&#123;font-size:12px;margin-top:30px;margin-bottom:10px&#125;.markdown-body h5>code&#123;font-size:12px&#125;.markdown-body h6&#123;font-size:10px;margin-top:30px;margin-bottom:10px&#125;.markdown-body h6>code&#123;font-size:10px&#125;.markdown-body h1,.markdown-body h2&#123;color:#ff502c&#125;.markdown-body hr&#123;height:4px;border:none;margin-top:32px;margin-bottom:32px;background-size:4px 1px;background-image:linear-gradient(270deg,#6d9dce,#8cc0f3 25%,transparent 50%)&#125;.markdown-body hr:nth-child(2n)&#123;background-image:linear-gradient(270deg,#ff9800,#fff8e0 25%,transparent 50%)&#125;.markdown-body ul&#123;padding-inline-start:20px&#125;.markdown-body ul li&#123;list-style-type:"🔸"&#125;.markdown-body ul li li&#123;list-style-type:"◻️"&#125;.markdown-body ul li li li&#123;list-style-type:"▫️"&#125;.markdown-body ol&#123;padding-inline-start:20px&#125;.markdown-body ol ::marker&#123;color:#ff9800&#125;.markdown-body ol,.markdown-body ul&#123;line-height:2em&#125;.markdown-body li&#123;padding-inline-start:1ch&#125;.markdown-body li.task-list-item&#123;list-style:none;padding-inline-start:0&#125;.markdown-body li input&#123;padding-right:2px&#125;.markdown-body li input[type=checkbox i]&#123;appearance:none&#125;.markdown-body li input:before&#123;content:"🟩";display:block;width:13px;height:13px&#125;.markdown-body li input:checked:before&#123;content:"✅"&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第2篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a></p>
<blockquote>
<p>💯 作者： <strong>俗世游子</strong>【谢先生】。 8年开发3年架构。专注于Java、云原生、大数据等领域技术。<br>
💥 成就： 从CRUD入行，负责过亿级流量架构的设计和落地，解决了千万级数据治理问题。<br>
📖 同名社区： ​<a href="https://juejin.cn/user/3359725700263694" target="_blank" title="https://juejin.cn/user/3359725700263694">​掘金​</a>​、​<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.51cto.com%2Fu_14948012" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.51cto.com/u_14948012" ref="nofollow noopener noreferrer">​51CTO​</a>​、  ​<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fmr_sanq" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/mr_sanq" ref="nofollow noopener noreferrer">​gitee​</a>​。<br>
📂 清单： ​<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fmr_sanq%2Fgoku-framework" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/mr_sanq/goku-framework" ref="nofollow noopener noreferrer">​goku-framework​</a>​、​<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fmr_sanq%2Fenjoy-read-ii" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/mr_sanq/enjoy-read-ii" ref="nofollow noopener noreferrer">​【更新中】享阅读II​</a>​</p>
</blockquote>
<h1 data-id="heading-0">DevOps系列文章</h1>
<p><a href="https://juejin.cn/post/7134696448616038414" target="_blank" title="https://juejin.cn/post/7134696448616038414">深入浅出DevOps：DevOps核心思想</a></p>
<p><a href="https://juejin.cn/post/7135949075387514894" target="_blank" title="https://juejin.cn/post/7135949075387514894">深入浅出DevOps：版本控制Git&Gitlab</a></p>
<p><a href="https://juejin.cn/post/7137300017152262151" target="_blank" title="https://juejin.cn/post/7137300017152262151">深入浅出DevOps：持续集成工具Jenkins</a></p>
<p><a href="https://juejin.cn/post/7137666687872008205" target="_blank" title="https://juejin.cn/post/7137666687872008205">深入浅出DevOps：简易Docker入门</a></p>
<p><a href="https://juejin.cn/post/7139406386911248414" target="_blank" title="https://juejin.cn/post/7139406386911248414">深入浅出DevOps：Jenkins实战之CI</a></p>
<h2 data-id="heading-1">为什么要提升代码质量</h2>
<p>本人所在公司业务方面已经开发的差不多了，现在质量部门开始找事情了：开始对代码编写规范，编写质量，数据建模规范有强制要求。最近一直就在搞这个事情。</p>
<p>但其实我们想一想，不管是项目初期或者其他时间，我们为什么都在强调代码规范问题，这会为我们产生什么样的影响呢？</p>
<p>首先，在企业中开发的项目大多都是多人协作开发，每个人的技术水平和编码习惯很难保证统一，如果没有一个良好的规范和约束，那么其他人在接手项目时他们的内心一定是这样的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3244199aedd439b88448648875e7686~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其次，提升自己的代码质量也能对自己产生比较好的效果，比如：</p>
<ul>
<li>心情愉悦，不至于让自己陷入到“祖传代码”中</li>
<li>降低因为踩坑而造成的工作时长，省下来的时间摸鱼不香么</li>
</ul>
<p>上面两点都不重要，而最重要的一点是：</p>
<ul>
<li>提高自身的工程和架构能力。提高代码质量是一个持续性的工作，如何指定相应的规范、如何将重构进行延续这是一门学问。需要我们好好的探讨。</li>
</ul>
<blockquote>
<p>可以从 “工程创建”- “技术选型”- “Git规范”- “前后端协同”- “代码编写”等方面好好的对自己的项目进行检查</p>
</blockquote>
<h2 data-id="heading-2">SonarQube</h2>
<p>单有了规范还不行，还需要有检查落地情况的工具。而SonarQube就是其中的代表产品。</p>
<h3 data-id="heading-3">简介</h3>
<p><strong>SonarQube</strong>是自动代码审查工具，用于检测代码中的错误、漏洞和代码异味。它可以与您现有的工作流程集成，以实现跨项目分支和拉取请求的持续代码检查。拥有如下特性：</p>
<ul>
<li>代码覆盖：通过单元测试，将会显示哪行代码被选中</li>
<li>改善编码规则：通过特定的规则对整个项目中的代码情况进行检查，分析其中的错误、漏洞和代码异味并进行统计，生成响应的报告。并且根据Git提交记录分配到响应的提交者</li>
<li>对比数据：比较同一张表中的任何测量的趋势</li>
</ul>
<p><strong>SonarQube</strong>功能强大，适用于 29 种编程语言，包括Java，Scala，JavaScript等语言，而且能够集成在IDE、Jenkins、Git等服务中，方便随时查看代码质量分析报告。</p>
<h3 data-id="heading-4">小插曲</h3>
<p>SonarQube提供了响应的IDEA的插件，在插件中找到<strong>SonarLint</strong>并进行安装</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c9fcbc0793c4c2cb2e5fe82bd9c5cb0~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当你在代码编写的过程中，SonarLint会自动对代码进行规范检查，在SonarLint的窗口中会显示出来，并且代码块会出现灰色的波浪线</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b09299632404410b6876b20942c7baa~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">SonarQue的安装</h3>
<p>插件介绍完之后，我们就正式进入到SonarQube的安装阶段。首先先来看配置要求 ​<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.sonarqube.org%2F8.9%2Frequirements%2Frequirements%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.sonarqube.org/8.9/requirements/requirements/" ref="nofollow noopener noreferrer">​最新版环境要求​</a>​：</p>
<ul>
<li>选择安装的是SonarQube比较新的版本：<strong>8.9.3-community</strong></li>
<li>直接安装在物理机上的话需要 <strong>安装JDK11的版本，</strong> Java 11 以外的版本不受官方支持<strong>​</strong></li>
<li><strong>​</strong>服务器资源最少需要2G内存，磁盘的读写性能必须要好<strong>​</strong></li>
</ul>
<blockquote>
<p>SonarQube的检索采用的是Elasticsearch来处理，因而对服务器的要求相对比较高</p>
</blockquote>
<ul>
<li>而数据库SonarQube支持​<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.sonarqube.org%2F8.9%2Fsetup%2Finstall-server%2F%23" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.sonarqube.org/8.9/setup/install-server/#" ref="nofollow noopener noreferrer">​Microsoft SQL Server​</a>​​，​<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.sonarqube.org%2F8.9%2Fsetup%2Finstall-server%2F%23" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.sonarqube.org/8.9/setup/install-server/#" ref="nofollow noopener noreferrer">​Oracle​</a>​​，​<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.sonarqube.org%2F8.9%2Fsetup%2Finstall-server%2F%23" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.sonarqube.org/8.9/setup/install-server/#" ref="nofollow noopener noreferrer">​PostgreSQL​</a>​。并且在7.9版本后放弃了对MySQL的支持。</li>
</ul>
<blockquote>
<p>这里就采用PostgreSQL作为存储数据库</p>
</blockquote>
<h4 data-id="heading-6">Docker安装</h4>
<p>本人对PostgreSQL不熟，就直接使用Docker来安装了。点击​<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.sonarqube.org%2F8.9%2Fsetup%2Finstall-server%2F%23" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.sonarqube.org/8.9/setup/install-server/#" ref="nofollow noopener noreferrer">​官网​</a>​可以找到其他的安装方式</p>
<blockquote>
<p>设置容器在同一个网络中，容器内部就可以直接通过容器名访问</p>
</blockquote>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">version:</span> <span class="hljs-string">"3"</span>
<span class="hljs-attr">services:</span>
    <span class="hljs-attr">db:</span>
        <span class="hljs-attr">image:</span> <span class="hljs-string">postgres</span>
        <span class="hljs-attr">container_name:</span> <span class="hljs-string">db</span>
        <span class="hljs-attr">restart:</span> <span class="hljs-string">always</span>
        <span class="hljs-attr">privileged:</span> <span class="hljs-literal">true</span>
        <span class="hljs-attr">ports:</span>
            <span class="hljs-bullet">-</span> <span class="hljs-number">5432</span><span class="hljs-string">:5432</span>
        <span class="hljs-attr">networks:</span>
            <span class="hljs-bullet">-</span> <span class="hljs-string">sonarnet</span>
        <span class="hljs-attr">environment:</span>
            <span class="hljs-attr">POSTGRES_USER:</span> <span class="hljs-string">sonar</span>
            <span class="hljs-attr">POSTGRES_PASSWORD:</span> <span class="hljs-string">sonar</span>
        <span class="hljs-attr">volumes:</span>
            <span class="hljs-bullet">-</span> <span class="hljs-string">/opt/postgresql:/var/lib/postgresql</span>
    <span class="hljs-attr">sonarqube:</span>
        <span class="hljs-attr">image:</span> <span class="hljs-string">sonarqube:8.9.3-community</span>
        <span class="hljs-attr">container_name:</span> <span class="hljs-string">sonarqube</span>
        <span class="hljs-attr">restart:</span> <span class="hljs-string">always</span>
        <span class="hljs-attr">privileged:</span> <span class="hljs-literal">true</span>
        <span class="hljs-attr">depends_on:</span>
            <span class="hljs-bullet">-</span> <span class="hljs-string">db</span>
        <span class="hljs-attr">ports:</span>
            <span class="hljs-bullet">-</span> <span class="hljs-string">"9000:9000"</span>
        <span class="hljs-attr">networks:</span>
            <span class="hljs-bullet">-</span> <span class="hljs-string">sonarnet</span>
        <span class="hljs-attr">environment:</span>
            <span class="hljs-attr">SONAR_JDBC_URL:</span> <span class="hljs-string">jdbc:postgresql://db:5432/sonar</span>
            <span class="hljs-attr">SONAR_JDBC_USERNAME:</span> <span class="hljs-string">sonar</span>
            <span class="hljs-attr">SONAR_JDBC_PASSWORD:</span> <span class="hljs-string">sonar</span>
        <span class="hljs-attr">volumes:</span>
            <span class="hljs-bullet">-</span> <span class="hljs-string">/opt/sonarqube/data:/opt/sonarqube/data</span>
            <span class="hljs-bullet">-</span> <span class="hljs-string">/opt/sonarqube/extensions:/opt/sonarqube/extensions</span>
            <span class="hljs-bullet">-</span> <span class="hljs-string">/opt/sonarqube/logs:/opt/sonarqube/logs</span>
<span class="hljs-attr">networks:</span>
    <span class="hljs-attr">sonarnet:</span>
        <span class="hljs-attr">driver:</span> <span class="hljs-string">bridge</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后执行如下命令进行操作</p>
<pre><code class="hljs copyable">docker-compose up -d
<span class="copy-code-btn">复制代码</span></code></pre>
<p>镜像下载完成之后会自动启动SonarQube服务，但是首次是启动不成功的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe309ef7dcbd4a0183d4107c57fd8c13~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于在SonarQube中使用了Elasticsearch组件，所以在启动服务的时候需要设置文件的句柄数。相信使用过Elasticsearch的同学都了解这个情况。</p>
<p>那么我们就来设置一下，想要设置为永久有效，就需要对​<code>​/etc/​</code>​​<code>​sysctl.conf​</code>​文件进行编辑，根据上方提示修改指定配置</p>
<pre><code class="hljs language-ini copyable" lang="ini"><span class="hljs-attr">vm.max_map_count</span>=<span class="hljs-number">262144</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>保存好之后执行​<code>​sysctl -p​</code>​ 进行刷新，然后重新启动就好</p>
<h3 data-id="heading-7">操作</h3>
<p>接下来等待较长时间之后，我们就可以通过浏览器来访问​<a href="https://link.juejin.cn/?target=http%3A%2F%2Fip%3A9000" target="_blank" rel="nofollow noopener noreferrer" title="http://ip:9000" ref="nofollow noopener noreferrer">​http://ip:9000​</a>​进入到Web页面，其中默认账户和密码都为<strong>admin</strong></p>
<p>第一次通过默认账户密码登录成功之后，会要求你修改密码，修改成功之后就能进入到首页</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b9f1a0ebb714bafa7ec8f62c6d270b7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">插件安装</h4>
<p>SonarQube除了自身的功能之外，本身和Jenkins一样，也支持安装插件来扩展功能。在安装插件的过程中注意SonarQube的相关提示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/052d4d4b0f454d7d8c79a16aa2019435~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>插件统一管理在Administration>Marketplace位置下，然后根据自己的需要安装对应的插件即可</p>
<p>注意，插件安装完成之后需要重启服务，可以在Web上直接点击重启按钮或者通过Docker操作</p>
<h5 data-id="heading-9">Chinese Pack</h5>
<p>默认SonarQube全部是英文，安装该插件之后可以转换为中文</p>
<h3 data-id="heading-10">创建项目</h3>
<p>接下来我们回到项目页面，默认情况下这里什么都没有，接下来我们看看创建项目的N中方式</p>
<h4 data-id="heading-11">Maven提交</h4>
<p>配合Maven是最简单的一种方式，我们只需要在本地的​<code>​settings.xml​</code>​中将SonarQube的基本信息配置上就可以</p>
<blockquote>
<p>​<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.sonarqube.org%2F8.9%2Fanalysis%2Fscan%2Fsonarscanner-for-maven%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.sonarqube.org/8.9/analysis/scan/sonarscanner-for-maven/" ref="nofollow noopener noreferrer">​点击​</a>​查看更多相关信息</p>
</blockquote>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">profiles</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">profile</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">id</span>></span>sonar<span class="hljs-tag"></<span class="hljs-name">id</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">activation</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">activeByDefault</span>></span>true<span class="hljs-tag"></<span class="hljs-name">activeByDefault</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">activation</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">properties</span>></span>
           <span class="hljs-comment"><!-- 平台登录的账号的用户名 --></span>
          <span class="hljs-tag"><<span class="hljs-name">sonar.login</span>></span>admin<span class="hljs-tag"></<span class="hljs-name">sonar.login</span>></span>
          <span class="hljs-comment"><!-- SonarQube平台登录的账号的密码 --></span>
          <span class="hljs-tag"><<span class="hljs-name">sonar.password</span>></span>admin123<span class="hljs-tag"></<span class="hljs-name">sonar.password</span>></span>
          <span class="hljs-comment"><!-- SonarQube访问地址 --></span>
          <span class="hljs-tag"><<span class="hljs-name">sonar.host.url</span>></span>http://192.168.10.200:9000<span class="hljs-tag"></<span class="hljs-name">sonar.host.url</span>></span>
          <span class="hljs-comment"><!-- 代码分析包括哪些文件需要分析，英文逗号分隔  --></span>
          <span class="hljs-tag"><<span class="hljs-name">sonar.inclusions</span>></span>**/*.java,**/*.xml<span class="hljs-tag"></<span class="hljs-name">sonar.inclusions</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">properties</span>></span>   
    <span class="hljs-tag"></<span class="hljs-name">profile</span>></span>
<span class="hljs-tag"></<span class="hljs-name">profiles</span>></span>
<span class="hljs-tag"><<span class="hljs-name">activeProfiles</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">activeProfile</span>></span>sonar<span class="hljs-tag"></<span class="hljs-name">activeProfile</span>></span>
<span class="hljs-tag"></<span class="hljs-name">activeProfiles</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么接下来在项目中执行​<code>​mvn sonar:sonar​</code>​就可以完成项目的创建了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eda116050d644c2b9e7ada5f13d5bd1c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>等待一段时间之后，我们可以通过点击提示的地址去查看相关信息，首先保证项目是正常提交成功的，我们再说其他信息</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91ba9ad0638c47b8aa8fb8b4d975ede5~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/360fdb2e62164e06a8d6320ddc5a1e5f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过点击对应的信息我们都可以看到相关的说明，并且根据我们配置的质量规则会告诉你当前问题的原因和解决方式</p>
<h4 data-id="heading-12">SonarScanner</h4>
<p>除了配合Maven之外，SonarScanner也是一种方式，SonarScanner是独立的工具，专业服务与SonarQube。</p>
<p>为了之后能够和Jenkins进行整合，接下来我选择在SonarQube所在的服务器上进行操作</p>
<ul>
<li><strong>下载</strong></li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash">wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.6.0.2311-linux.zip
unzip sonar-scanner-cli-4.6.0.2311-linux.zip
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>配置文件配置</strong></li>
</ul>
<p>通过编辑​<code>​$install_directory/conf/sonar-scanner.properties​</code>​，在此处配置有关SonarQube基础环境，例如SonarQube服务器连接详细信息</p>
<pre><code class="hljs language-ini copyable" lang="ini"><span class="hljs-comment"># SonarQube访问地址,和Maven配置是一样的</span>
<span class="hljs-attr">sonar.host.url</span>=http://<span class="hljs-number">192.168</span>.<span class="hljs-number">10.200</span>:<span class="hljs-number">9000</span>
<span class="hljs-attr">sonar.login</span>=admin
<span class="hljs-attr">sonar.password</span>=admin123
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果不想这样配置的话，那么在执行命令的过程中也可以通过​<code>​-D​</code>​的方式将参数配置到启动程序中，比如</p>
<ul>
<li>-Dsonar.login=xxx</li>
<li>-Dsonar.password=xxx</li>
<li>...</li>
</ul>
<p>那配置完成之后，就需要配置项目信息了，这样才能一起玩起来，需要配置如下关键信息：</p>
<ul>
<li>项目名称和本地source</li>
</ul>
<pre><code class="hljs language-ini copyable" lang="ini"><span class="hljs-comment"># 默认为项目名</span>
sonar.projectName=
<span class="hljs-comment"># 基础目录</span>
sonar.projectBaseDir=
<span class="hljs-comment"># 相对于sonar-project.properties所在目录，默认为 . 如果没有，那就指定项目空间下的目录，比如src</span>
<span class="hljs-attr">sonar.sources</span>=.
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>推送到SonarQube的唯一标识，也可以认定为是在SonarQube项目页的展示名</li>
</ul>
<pre><code class="hljs copyable">sonar.projectKey=
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>项目编辑之后的生成目录</li>
</ul>
<pre><code class="hljs copyable">sonar.java.binaries=
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">sonar-project.properties</h4>
<p>那么，根据我们之前的DevOps_App项目来介绍，这个配置文件应该是这样的</p>
<pre><code class="hljs language-ini copyable" lang="ini"><span class="hljs-attr">sonar.projectName</span>=DevOps_App
<span class="hljs-attr">sonar.projectKey</span>=DevOps_App
<span class="hljs-attr">sonar.sources</span>=.
<span class="hljs-attr">sonar.java.binaries</span>=target/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过执行​<code>​sonar-scanner​</code>​就可以完成推送到SonarQube的流程。</p>
<p>而属性 ​<code>​project.settings​</code>​可用于指定项目配置文件的路径，这样能够替代无法在项目根目录下创建 sonar-project.properties 文件的麻烦问题</p>
<pre><code class="hljs language-ini copyable" lang="ini">sonar-scanner <span class="hljs-attr">-Dproject.settings</span>=xxx/sonar-project.properties
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">命令行</h4>
<p>如果不方便在项目下书写，那么还有其他的替代方案。</p>
<ul>
<li><strong>命令行直接带参数</strong></li>
</ul>
<p>通过执行​<code>​sonar-scanner​</code>​，在其后通过​<code>​-D​</code>​的方式跟上相对应的配置也可以完成推送到SonarQube的流程</p>
<pre><code class="hljs language-ini copyable" lang="ini">./sonar-scanner <span class="hljs-attr">-Dsonar.projectName</span>=DevOps_App -Dsonar.projectKey=DevOps_App -Dsonar.sources=. -Dsonar.java.binaries=target/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两种方式都是能看到最终的结果，完美！！！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/390fc7d09fff4b30968cd7740891412b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">最后</h2>
<p>好了，到这里关于SonarQube相关的内容就先介绍到这里，本节主要是一个抛砖引玉的过程，实际生产中还需要对SonarQube的规则和项目进行自定义，这需要大家在接下来好好的熟悉熟悉</p></div>  
</div>
            