
---
title: '基于nexus3搭建npm私服'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f6ff6db260e43c797a46648f61f5d34~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 01:40:44 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f6ff6db260e43c797a46648f61f5d34~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.  nexus repository oss是什么?</h2>
<p>是用来存储仓库的免费工具，可以用来存储jar, docker, npm等软件包，也可以存储其他文件格式，不依赖mysql等，下载包可直接运行。支持的列表见下图
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f6ff6db260e43c797a46648f61f5d34~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">2.  下载&运行（以docker为例）</h2>
<h3 data-id="heading-2">2.1 拉取nexus3镜像</h3>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 运行指令</span>
docker pull sonatype/nexus3
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb0e48c0ec8c430b80d94ae43e8a2cfe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2.2 建立volume持久化数据</h3>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 运行指令</span>
docker volume create --name nexus-data
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59d3b2f271964da5a69df4cb094debd7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">2.3 运行容器</h3>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 运行指令</span>
docker run --privileged=true -d -p 8801:8081 --name nexus -v nexus-data:/nexus-data sonatype/nexus3 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78fda05c235a40a9b01949bd1eb460d1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以看到容器已经在8801端口运行 \</p>
<p>tip：<br>
-id 创建守护式容器<br>
--privileged=true 授予root权限（挂载多级目录必须为true，否则容器访问宿主机权限不足）<br>
--name=名字 给你的容器起个名字<br>
-p 宿主机端口：容器端口映射<br>
-v 宿主机目录：容器目录 目录挂载</p>
<h2 data-id="heading-5">3 登录 & 创建 Host (私有的) proxy(代理) group(对外开放的)仓库</h2>
<h3 data-id="heading-6">3.1 获取登录密码</h3>
<p>打开/var/lib/docker/volumes/nexus-data/_data下的admin.password，复制密码，然后登录后重置密码
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/957bf38f1a6a4641905108ba41c56fe9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed48cd5d12e3426a911210be2ad2d68e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">3.2 创建Host (私有的) proxy(代理) group(对外开放的)仓库</h3>
<h4 data-id="heading-8">3.2.1 npm-host</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bf96de76c154085a16a5807b840f55a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">3.2.2 npm-proxy</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/075631010d5a41a09380a32c29798c34~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">3.2.3 npm-group</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98d7d16e69204712b2f9733682c182c2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">4 添加角色</h2>
<p>npm发布包是需要先登录的，这里我们只是想把包发布到自己私有的服务器上。</p>
<h3 data-id="heading-12">4.1. 添加权限认证</h3>
<p>设置权限, Realms 菜单, 将 npm Bearer Token Realm 添加到右边
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf34671f1a5d4d02b7854996a1319bf1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">4.2. 创建nx-deploy角色</h3>
<p>给角色赋予以下权限/
nx-repository-view-<em>-</em>-*
nx-repository-admin-npm-npm-group-*
nx-repository-admin-npm-npm-proxy-*
nx-repository-admin-npm-npm-host-*
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/263dacb9ba1b4747842467a11bf9fb04~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">4.3. 创建角色，同时设置角色为nx-deploy</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b59af168a4c481a919e6a7d51004a41~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">5.创建第一个npm包</h2>
<h3 data-id="heading-16">5.1 创建客户端的.npmrc配置 （目录文件下创建）</h3>
<p>该文件的作用是避免每次npm publish都用登录</p>
<pre><code class="copyable"># 配置
registry=http://10.7.4.11:8801/repository/npm-group/
email=18813295951@163.com
always-auth=true
_auth="TWljaGFlbEpvcmRhbjoxMjM0NTY="
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7187fd9b43934ab186208778a52c937f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17">5.2 初始化npm项目、并添加publishConfig.registry的配置</h3>
<pre><code class="copyable"># 运行指令
npm init
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"># 配置
&#123;
  "name": "gdpg-utils",
  "version": "1.0.1",
  "description": "",
  "main": "index.js",
  "scripts": &#123;
    "test": "echo \"Error: no test specified\" && exit 1"
  &#125;,
  "publishConfig": &#123;
    "registry": "http://10.7.4.11:8801/repository/npm-host/"
  &#125;,
  "author": "",
  "license": "ISC",
  "dependencies": &#123;
    "gdpg-utils": "http://10.7.4.11:8801/repository/npm-host/gdpg-utils/-/gdpg-utils-1.0.1.tgz"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f4a996ee0e34e3db1df0d5d6411df86~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18">5.3 创建index.js，并通过npm publish上传npm包</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b12bb70bbe97478a93c7607143e1ba14~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0772837c7236481091d8bbb43d54de57~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19">5.4 在项目中引用发布在nexus中的gdpg-utils包进行测试</h3>
<p>这里使用直接链接包地址的方式，更多npm包的引用方式可以看下面这篇文章<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Ffightjianxian%2Fp%2F12550591.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/fightjianxian/p/12550591.html" ref="nofollow noopener noreferrer">常用的几类npm依赖包管理 - 剑仙6 - 博客园 (cnblogs.com)</a></p>
<pre><code class="copyable"># 配置
"dependencies": &#123;
    "gdpg-utils": "http://10.7.4.11:8801/repository/npm-host/gdpg-utils/-/gdpg-utils-1.0.1.tgz"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"># 运行指令
npm install
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9d1e14e8e604a1999285a8e3a4c734a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以看到已经成功下载刚刚上传到私服的npm包</p>
<h3 data-id="heading-20">5.5 用npm-proxy的缓存效果，缓存下载过的npm包，保证第二次加载同一版本的npm包时，直接加载nexus中npm包缓存</h3>
<pre><code class="copyable"># 设置项目的仓库地址
npm config set registry http://10.7.4.11:8801/repository/npm-group/
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"># 安装axios
npm install axios
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a18e27caf7794667886c72094bf7a68f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24bcce0ad0124cb491ba96b64f13d3ca~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-21">6 参考文档</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fqdhxhz%2Fp%2F9801325.html" title="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fqdhxhz%2Fp%2F9801325.html" target="_blank">linux搭建Nexus3.x私服</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F1674a6bc1c12" title="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F1674a6bc1c12" target="_blank">使用 Nexus3 Repository Manager 搭建 npm 私服</a></p>
<h2 data-id="heading-22">7 总结</h2>
<p>npm私服搭建只是第一步，npm版本号如何管理？npm包如何管理多个依赖？如何处理各系统npm包版本号不同的问题？如何在开发环境高效开发npm组件？等这些问题都是需要在npm私服管理落地时需要去思考的。</p></div>  
</div>
            