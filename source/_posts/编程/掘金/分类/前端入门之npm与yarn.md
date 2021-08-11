
---
title: '前端入门之npm与yarn'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f27f8848382d4ba6974c322daed1fc62~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 17:21:42 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f27f8848382d4ba6974c322daed1fc62~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、npm简介</h2>
<p><code>npm</code> 全称为 <code>Node Package Manager</code>，是一个基于 <code>Node.js</code> 的包管理器，也是整个 <code>Node.js</code> 社区最流行、支持的第三方模块最多的包管理器。npm的初衷：JavaScript开发人员更容易分享和重用代码。</p>
<ol start="0">
<li>nodejs = ECMAScript + 核心模块</li>
<li>自己遵循 commonjs 规范写出模块，如果写的是功能模块（日期处理datejs，数字处理numberjs）。如果可以把这些模块分享出来，以后谁要进行相关功能开发的时候，直接拿开发好的模块使用即可，没必要自己在开发。在互联网有一个网站专门收集这样的工具包。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.cn/" ref="nofollow noopener noreferrer">www.npmjs.cn/</a>。</li>
<li>如果我们要使用这个网站里面的包，则我们需要使用一个功能，叫做 npm。</li>
</ol>
<p>官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.cn/" ref="nofollow noopener noreferrer">www.npmjs.cn/</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fmd5" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/md5" ref="nofollow noopener noreferrer">www.npmjs.com/package/md5</a></p>
<p>npm可以用来：</p>
<ul>
<li>允许用户获取第三方包并使用</li>
<li>允许用户将自己编写的包或命令行程序进行发布分享</li>
</ul>
<p><strong>npm安装：</strong></p>
<p><code>npm</code>不需要单独安装。在安装 <code>Node</code> 的时候，会连带一起安装<code>npm</code>。</p>
<p>执行下面的命令可以用来查看本地安装的 npm 的版本号。</p>
<pre><code class="copyable">npm -v
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果想升级 npm ，可以这样(仅做了解，很少用)</p>
<pre><code class="copyable">npm install npm --global
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">二、npm体验</h2>
<p>以安装和使用md5模块为例：</p>
<p>1、项目目录下，执行命令 npm init，目录下会多一个package.json文件(这个文件1、记录项目相关信息，如项目名称，项目版本2、后期会记录项目中使用的第三方模块)</p>
<p>2、项目目录下，执行命令 npm install md5，这时候就会开始联网下载md5这个包，下载过程需要耐心等待，等待时间视网速而定。</p>
<p>3、看见以下代码表示下载完成：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f27f8848382d4ba6974c322daed1fc62~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
下载完后：本地项目目录下多了一个node_modules文件夹，我们刚才所下载的md5包及其相关依赖包都在这个文件夹里面了。以后我们开发中需要下载其他包，都会在下载在这个文件夹中。</p>
<p>4、下载完就可以在项目中去导入然后使用了：</p>
<pre><code class="copyable">var md5 = require('md5');
console.log(md5("12345789"));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行就会得到一个加密字符串。</p>
<h2 data-id="heading-2">三、nodemon包的使用</h2>
<p>我们前面使用node的http模块书写过web服务器，但是每次改写一点代码都需要重启服务器，开发不是很方便。nodemon可以监听代码的改动自动更新，不需要重启服务器程序就可以看效果。</p>
<p>文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fnodemon" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/nodemon" ref="nofollow noopener noreferrer">www.npmjs.com/package/nod…</a></p>
<p>下载：npm install -g nodemon</p>
<p>说明： -g 表示安装在全局， 这种安装方式不同于前面的安装，它只需要安装一次，就能一直使用。安装的时候会有一个专门的安装目录（安装完成会有提示安装位置，如果忘记了，可以通过npm root -g命令查看安装在哪里）</p>
<p>安装成功，项目目录下，通过命令<strong>nodemon 11-http模块.js</strong>启动服务器即可。</p>
<h2 data-id="heading-3">四、yarn安装与使用</h2>
<p><code>Yarn</code> 是于 2016 年 10 月 由 Facebook、Google、Exponent 和 Tilde 联合推出了一个新的 JS 包管理工具，旨在取代 npm 这种包管理工具。</p>
<p>官网： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fyarnpkg.com%2Fen%2Fdocs" target="_blank" rel="nofollow noopener noreferrer" title="https://yarnpkg.com/en/docs" ref="nofollow noopener noreferrer">yarnpkg.com/en/docs</a></p>
<p>中文参考链接： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fyarn.bootcss.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://yarn.bootcss.com/" ref="nofollow noopener noreferrer">yarn.bootcss.com/</a></p>
<p><strong>特点</strong>：</p>
<ul>
<li>速度超快</li>
</ul>
<blockquote>
<p>yarn 缓存了每个下载过的包，所以再次使用时无需重复下载。 同时利用并行下载以最大化资源利用率，因此安装速度更快。</p>
</blockquote>
<ul>
<li>超级安全</li>
</ul>
<blockquote>
<p>在执行代码之前，yarn 会通过算法校验每个安装包的完整性。</p>
</blockquote>
<ul>
<li>超级可靠</li>
</ul>
<blockquote>
<p>使用详细、简洁的锁文件格式和明确的安装算法，yarn 能够保证在不同系统上无差异的工作。</p>
</blockquote>
<p><strong>安装</strong>:</p>
<p>管理员模式运行cmd ：<strong>npm install -g yarn</strong>
<strong>常用命令</strong>：</p>

































<table><thead><tr><th>npm</th><th>yarn</th></tr></thead><tbody><tr><td>npm init -y</td><td>yarn init -y</td></tr><tr><td>npm install react --save</td><td>yarn add react</td></tr><tr><td>npm uninstall react --save</td><td>yarn remove react</td></tr><tr><td>npm install react --save-dev</td><td>yarn add react --dev</td></tr><tr><td>npm update --save</td><td>yarn upgrade</td></tr><tr><td>npm install -g @vue/cli</td><td>yarn global add @vue/cli</td></tr></tbody></table>
<p>yarn init -y</p>
<p>yarn add md5</p>
<p>yarn add nzh</p>
<p>npm i yarn</p>
<p><strong>yarn 全局安装后，命令不生效</strong></p>
<p>背景：</p>
<ul>
<li>执行 <code>yarn global add @vue/cli</code> 后，重启 <code>bash......</code>， vue 命令依然不生效</li>
<li>而 npm 全局安装（npm install -g @vue/cli）后，命令生效</li>
</ul>
<p>解决办法：</p>
<p>1.执行如下命令，得出 yarn 全局安装的命令所处的安装目录</p>
<pre><code class="copyable">yarn global bin 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.复制安装目录至电脑的环境变量中</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38eca7d5e2de4a58bde9e592c3f2cfb6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>3.重新启动终端，发现全局命令行可以生效了</p></div>  
</div>
            