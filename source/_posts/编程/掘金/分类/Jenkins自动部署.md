
---
title: 'Jenkins自动部署'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/043da0ce71e3483e9abc0f8c1cba40ad~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 23 May 2021 03:32:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/043da0ce71e3483e9abc0f8c1cba40ad~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>事先确保服务器上有 Java 环境与 Maven 环境和 Git</p>
<h2 data-id="heading-0"><a href="https://juejin.cn/post/6965446813000138765#%E5%AE%89%E8%A3%85Jenkins" title="安装Jenkins"></a>安装 Jenkins</h2>
<p>这里是 Jenkins 的文档 <a href="https://jenkins.io/zh/doc/" target="_blank" rel="nofollow noopener noreferrer">jenkins.io/zh/doc/</a></p>
<p>这里是 Jenkins 的下载地址 <a href="https://jenkins.io/zh/download/" target="_blank" rel="nofollow noopener noreferrer">jenkins.io/zh/download…</a></p>
<p><strong>最好的方式应该是自己去下载 Jenkins 的 Jar 包，直接像运行 jar 包即可</strong></p>
<pre><code class="copyable">nohup java -jar jenkins.war --httpPort=80
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样直接访问<code>172.16.45.112:8080</code> 即可！</p>
<p>成功开启服务后应该是下面这个样子：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/043da0ce71e3483e9abc0f8c1cba40ad~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>登录密码：</p>
<pre><code class="copyable">cat /var/lib/jenkins/secrets/initialAdminPassword
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我直接选择推荐插件了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e54b823f710c4413a07c1cd597f8c889~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1"><a href="https://juejin.cn/post/6965446813000138765#Jenkins%E8%87%AA%E5%8A%A8%E6%9E%84%E5%BB%BA" title="Jenkins自动构建"></a>Jenkins 自动构建</h2>
<p>原文参考 <a href="https://blog.csdn.net/boling_cavalry/article/details/78943061" target="_blank" rel="nofollow noopener noreferrer">《Jenkins 自动构建》</a></p>
<p>当我们提交代码到 GitHub 后，可以在 Jenkins 上执行构建，但是每次都要动手去执行略显麻烦，今天我们就来实战 Jenkins 的自动构建功能，每次提交代码到 GitHub 后，Jenkins 会进行自动构建！</p>
<h3 data-id="heading-2"><a href="https://juejin.cn/post/6965446813000138765#%E6%B3%A8%E6%84%8F%E7%82%B9" title="注意点"></a>注意点</h3>
<p>GitHub 收到提交的代码后要主动通知 Jenkins，所以 Jenkins 所在服务器一定要有外网 IP，否则 GitHub 无法访问，我的 Jenkins 服务器是部署在腾讯云的云主机上，带有外网 IP；</p>
<h3 data-id="heading-3"><a href="https://juejin.cn/post/6965446813000138765#%E6%95%B4%E4%B8%AA%E6%B5%81%E7%A8%8B" title="整个流程"></a>整个流程</h3>
<ul>
<li>GitHub 上准备一个 spring boot 的 web 工程；</li>
<li>GitHub 上配置 Jenkins 的 webhook 地址；</li>
<li>在 GitHub 上创建一个 access token，Jenkins 做一些需要权限的操作的时候就用这个 access token 去鉴权；</li>
<li>Jenkins 安装 GitHub Plugin 插件；</li>
<li>Jenkins 配置 GitHub 访问权限；</li>
<li>Jenkins 上创建一个构建项目，对应的源码是步骤 1 中的 web 工程；</li>
<li>修改 web 工程的源码，并提交到 GitHub 上；</li>
<li>检查 Jenkins 的构建项目是否被触发自动构建，构建成功后，下载工程运行，看是不是基于最新的代码构建的</li>
</ul></div>  
</div>
            