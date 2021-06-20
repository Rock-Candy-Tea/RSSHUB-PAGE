
---
title: '前端脚手架开发，Lerna'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06107abfa47947beb5350a75249f79bf~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 18 Jun 2021 04:49:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06107abfa47947beb5350a75249f79bf~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第 18 天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h1 data-id="heading-0">前端脚手架开发，Lerna</h1>
<p><a href="https://github.com/lerna/lerna/" target="_blank" rel="nofollow noopener noreferrer">lerna</a>是一个优化基于git+npm的多package项目管理工具</p>
<h2 data-id="heading-1">1. Lerna所解决的问题</h2>
<ul>
<li>
<p>复杂项目的重复操作,例如:<code>多package的本地link</code>、<code>多package的单元测试</code>，<code>多package的代码发布</code>，关于这个点，如果看过并实践过[前端脚手架开发，实践出真知]这篇文章的内容的话，可能理解会更加深入</p>
</li>
<li>
<p>复杂项目的版本一致性问题</p>
<ul>
<li>发布时的版本一致性</li>
<li>发布后相互依赖版本升级</li>
</ul>
</li>
</ul>
<h2 data-id="heading-2">2. lerna 开发脚手架流程</h2>
<p>看这这张图，实践一下吧！创建一个<code>lerna-test-cli</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06107abfa47947beb5350a75249f79bf~tplv-k3u1fbpfcp-watermark.image" alt="3-1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2.1 动手实践</h3>
<ol>
<li>先创建一个项目文件，例如lerna-test-cli，先用<code>npm init</code> 去初始化你的项目</li>
<li><code>cnpm i lerna -D</code>安装lerna的相关依赖</li>
<li><code>npx lerna -v</code>查看一下版本号，看看是否安装成功，然后使用<code>npx lerna init</code>去初始化你的项目,然后会出现一个<code>lerna.json</code>的文件</li>
</ol>
<pre><code class="hljs language-json copyable" lang="json">
&#123;
  <span class="hljs-attr">"packages"</span>: [
    <span class="hljs-string">"packages/*"</span>
  ],
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.0.0"</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里值得注意的就一个地方，就是里面的<code>packages</code>,意思就是以后我们在项目当中其他子的<code>package</code>都要放入这里面去管理</p>
<ol start="4">
<li><code>npx lerna create 你的包</code>，创建一个package包</li>
</ol>
<p>这里有一个点要特别注意: 就是我们的包都是要发布在npm上去的，所以在创建之前先看看这个包名被注册了没有，最好是在其创建一个组织然后放包，避免和其他用户注册的产生冲突</p>
<h2 data-id="heading-4">3. Lerna核心操作</h2>
<p>其他常用操作可以<code>npx lerna -h</code> 去查看帮助手册，以下讲重点</p>
<h3 data-id="heading-5">3.1 <code>lerna add</code></h3>
<ul>
<li>对所有的<code>package</code>安装相关的依赖,<code>npx lerna add <package>[@version] [--dev] [--exact] [--peer]</code></li>
<li>对某个特定的包安装相关依赖，<code>npx lerna add <package> <特定包的路径名></code>，</li>
</ul>
<h3 data-id="heading-6">3.2 <code>lerna link</code></h3>
<p>项目包建立软链，类似npm link,但是很重要的一点是，他是给包有相互引用包进行软链接</p>
<h3 data-id="heading-7">3.3 <code>lerna exec</code></h3>
<p>运行任意命令在每个包</p>
<h3 data-id="heading-8">3.4 lerna run</h3>
<p>运行某个包的某个指令</p>
<h2 data-id="heading-9">4. lerna 发布流程</h2>
<h3 data-id="heading-10">4.1 运行<code>lerna version</code></h3>
<p>这个命令 识别出修改的包 --> 创建新的版本号 --> 修改package.json --> 提交修改 打上版本的tag --> 推送到git上。版本号 遵循 <code>semver</code>,关于这个请戳这个<a href="https://semver.org/lang/zh-CN/?spm=a219a.7629140.0.0.GUJMXE" target="_blank" rel="nofollow noopener noreferrer">链接</a></p>
<h3 data-id="heading-11">4.2 <code>lerna changed</code></h3>
<p>列出下次发版lerna publish 要更新的包。</p>
<pre><code class="copyable">...
xxx-one
xxx-two
lerna success found 2 packages ready to publish
# 俩个改过的包，下次发布publish将发布这俩个

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">4.3 <code>lerna publish</code></h3>
<p>特点：会打tag，上传git,上传npm。</p>
<p>如果你的包名是带scope的例如："name": "@xxxx/xxx",那需要在packages.json添加</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"publishConfig"</span>: &#123;
    <span class="hljs-attr">"access"</span>: <span class="hljs-string">"public"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>知识点补充，什么是scope包？</strong></p>
<p><code>scope</code>意为范围或作用域，也值命名空间。所以带<code>scope</code>的包表示包带命名空间。假设待发布包<code>package.json</code>中<code>name</code>属性如下：</p>
<pre><code class="hljs language-json copyable" lang="json">
&#123;
<span class="hljs-attr">"name"</span>:<span class="hljs-string">"@username/project-name"</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>username</code> 就是命名空间，是登录账户名。</p></div>  
</div>
            