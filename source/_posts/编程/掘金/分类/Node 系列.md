
---
title: 'Node 系列'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/225ef262c489453a9cf7638be1a582f0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Apr 2021 16:25:15 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/225ef262c489453a9cf7638be1a582f0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>什么，作为一枚前端复制粘贴工程师，你居然还不会 Node.js？</p>
<p>在日常工作中，<strong>jsliang</strong> 会用 Node.js 写写便捷小工具，优化工作流程和进行接口数据转发等。</p>
<p>本系列会由易到难，和小伙伴们一起探索 Node.js。</p>
<ul>
<li>Node 工具库（编写 ing、日更中）
<ul>
<li>commander</li>
<li>翻译</li>
<li>文件序号重排</li>
<li>获取文件头信息</li>
</ul>
</li>
</ul>

<h2 data-id="heading-0"><a name="user-content-chapter-one" id="user-content-chapter-one" href="https://juejin.cn/post/undefined"></a>一 目录</h2>
<p><strong>不折腾的前端，和咸鱼有什么区别</strong></p>






































<table><thead><tr><th>目录</th></tr></thead><tbody><tr><td><a href="https://juejin.cn/post/6951172272023404552#chapter-one">一 目录</a></td></tr><tr><td><a name="user-content-catalog-chapter-two" id="user-content-catalog-chapter-two" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6951172272023404552#chapter-two">二 Node.js 介绍</a></td></tr><tr><td> <a href="https://juejin.cn/post/6951172272023404552#chapter-two-one">2.1 什么是 Node.js？</a></td></tr><tr><td> <a href="https://juejin.cn/post/6951172272023404552#chapter-two-two">2.2 Node.js 优点？</a></td></tr><tr><td> <a href="https://juejin.cn/post/6951172272023404552#chapter-two-three">2.3 Node.js 应用？</a></td></tr><tr><td><a name="user-content-catalog-chapter-three" id="user-content-catalog-chapter-three" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6951172272023404552#chapter-three">三 Node.js 开发环境</a></td></tr><tr><td> <a href="https://juejin.cn/post/6951172272023404552#chapter-three-one">3.1 Node.js</a></td></tr><tr><td> <a href="https://juejin.cn/post/6951172272023404552#chapter-three-two">3.2 Visio Studio Code</a></td></tr><tr><td><a name="user-content-catalog-chapter-four" id="user-content-catalog-chapter-four" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6951172272023404552#chapter-four">四 参考文献</a></td></tr><tr><td></td></tr></tbody></table>
<h2 data-id="heading-1"><a name="user-content-chapter-two" id="user-content-chapter-two" href="https://juejin.cn/post/undefined"></a>二 Node.js 介绍</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6951172272023404552#chapter-one">返回目录</a></p>
</blockquote>
<h3 data-id="heading-2"><a name="user-content-chapter-two-one" id="user-content-chapter-two-one" href="https://juejin.cn/post/undefined"></a>2.1 什么是 Node.js？</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6951172272023404552#chapter-one">返回目录</a></p>
</blockquote>
<p>Node.js 是一个 JavaScript 运行环境（<code>runtime</code>）。它让 JavaScript 可以开发后端程序，实现几乎其他后端语言实现的所有功能。传说中 <strong>能与 PHP、JSP、Python、Ruby 等后端语言平起平坐</strong>。</p>
<p>但是，实际上 Node.js 一般用作中间件。例如：在浏览器端和 Java 端使用 Node.js 作为中间件，Node.js 调用 Java 后端发布的接口，同时 Node.js 可以发布 HTTP 接口给浏览器端调用。</p>
<h3 data-id="heading-3"><a name="user-content-chapter-two-two" id="user-content-chapter-two-two" href="https://juejin.cn/post/undefined"></a>2.2 Node.js 优点？</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6951172272023404552#chapter-one">返回目录</a></p>
</blockquote>
<ol>
<li>Node.js 语法完全是 JS 语法，只要你懂了 JS 基础就可以学会 Node.js 后端开发。</li>
<li>Node.js 超强的高并发能力。在 Java、PHP 或者 .Net 等服务端语言中，会为每一个客户端的连接创建一个新的线程，而每个线程需要耗费大约 2 MB 内存。也就是说，理论上一个 8GB 的服务器，可以同时连接的最大用户数为 4000 个左右。而 Node.js 不会为每个客户创建新的线程，仅仅使用一个线程。所以，使用 Node.js，一个 8GB 的服务器，可以同时处理超过 4 万用户的连接。</li>
<li>实现高性能服务器。Node.js 基于 V8 引擎，V8 引擎是 Google 公司使用 C++ 开发的一种高性能引擎。这意味着开发者编写的高端 JavaScript 脚本代码与开发者编写的低端的 C 语言具有非常相近的执行效率。</li>
<li>开发周期短、开发成本低、学习成本低。花最小的硬件成本，追求更高的并发，更高的处理性能。</li>
</ol>
<h3 data-id="heading-4"><a name="user-content-chapter-two-three" id="user-content-chapter-two-three" href="https://juejin.cn/post/undefined"></a>2.3 Node.js 应用？</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6951172272023404552#chapter-one">返回目录</a></p>
</blockquote>
<p><img alt="Node-README-01.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/225ef262c489453a9cf7638be1a582f0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5"><a name="user-content-chapter-three" id="user-content-chapter-three" href="https://juejin.cn/post/undefined"></a>三 Node.js 开发环境</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6951172272023404552#chapter-one">返回目录</a></p>
</blockquote>
<p>在你使用 Node.js 进行开发之前，一些准备条件必不可少：</p>
<ul>
<li>安装 Node.js</li>
<li>安装 Visio Studio Code</li>
</ul>
<h3 data-id="heading-6"><a name="user-content-chapter-three-one" id="user-content-chapter-three-one" href="https://juejin.cn/post/undefined"></a>3.1 Node.js</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6951172272023404552#chapter-one">返回目录</a></p>
</blockquote>
<ul>
<li><a href="http://nodejs.cn/download/" target="_blank" rel="nofollow noopener noreferrer">Node 下载 | Node.js 中文网</a></li>
<li><a href="https://www.runoob.com/nodejs/nodejs-install-setup.html" target="_blank" rel="nofollow noopener noreferrer">Node 安装步骤 | 菜鸟教程</a></li>
<li><a href="https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/00143450141843488beddae2a1044cab5acb5125baf0882000" target="_blank" rel="nofollow noopener noreferrer">Node 与 Npm | 廖雪峰</a></li>
<li><a href="https://npm.taobao.org/" target="_blank" rel="nofollow noopener noreferrer">cnpm | 淘宝 NPM 镜像</a></li>
</ul>
<p>Node.js、npm、cnpm 的关系，用一句话来概括就是：</p>
<ul>
<li>npm 是 Node.js 的包管理工具，所谓包管理工具可以理解为大佬们将一些常用的功能写成包并发布到 npm 市场上，然后别人通过 npm 直接安装即可使用（类似手机应用 app）。而因为 npm 在国内有一定限制，所以就需要用淘宝的镜像 cnpm，从而提高我们 npm 的下载安装速度（类似手机网络和 WIFI 下载手机应用 app）</li>
</ul>
<p>最后，如果小伙伴们下载安装好环境后，在控制台输入 <code>cnpm -v</code> 就可以查看到自己的 Node.js 版本：</p>
<p><img alt="Node-README-02.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38779f36d36d45759dd9d15c61463cad~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这是 18 年的一个截图，与时俱进啦大人~</p>
</blockquote>
<h3 data-id="heading-7"><a name="user-content-chapter-three-two" id="user-content-chapter-three-two" href="https://juejin.cn/post/undefined"></a>3.2 Visio Studio Code</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6951172272023404552#chapter-one">返回目录</a></p>
</blockquote>
<p>工欲善其事，必先利其器。</p>
<p>作为一枚前端开发，你怎么能没有自己的软件开发工具~</p>
<p>这里安利 Visio Studio Code（以下简称 VS Code），这是一款轻量级的代码编辑器，支持语法高亮、智能代码补全、自定义热键、括号匹配、代码片段、代码对比 diff、Git 等特性。</p>
<p>当然，开发软件不仅限于 VS Code，还有 Atom、Sublime、WebStorm 等，这里不一一介绍。</p>
<blockquote>
<p>如果小伙伴开发工具和 <strong>jsliang</strong> 不一样，帮小伙伴排查问题一般没那么容易</p>
</blockquote>
<p>下面贴上下载链接和介绍：</p>
<ul>
<li><a href="https://code.visualstudio.com/" target="_blank" rel="nofollow noopener noreferrer">Visio Studio Code 安装 | 官网</a></li>
<li><a href="https://www.cnblogs.com/huyong/p/4573041.html" target="_blank" rel="nofollow noopener noreferrer">Visio Studio Code 安装及使用技巧 | 博客园</a></li>
</ul>
<p>OK，废话那么多，小伙伴们应该将 Node.js 和 VS Code 安装完毕了，话不多说，开始探索！</p>
<h2 data-id="heading-8"><a name="user-content-chapter-four" id="user-content-chapter-four" href="https://juejin.cn/post/undefined"></a>四 参考文献</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6951172272023404552#chapter-one">返回目录</a></p>
</blockquote>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/30384677" target="_blank" rel="nofollow noopener noreferrer">知乎：浅谈前后端分离与实践之 nodejs 中间层服务(二)</a></li>
</ul>
<hr>
<p><strong>不折腾的前端，和咸鱼有什么区别！</strong></p>
<p>觉得文章不错的小伙伴欢迎点赞/点 Star。</p>
<p>如果小伙伴需要联系 <strong>jsliang</strong>：</p>
<ul>
<li><a href="https://github.com/LiangJunrong/document-library" target="_blank" rel="nofollow noopener noreferrer">Github</a></li>
<li><a href="https://juejin.im/user/3403743728515246" target="_blank" rel="nofollow noopener noreferrer">掘金</a></li>
</ul>
<p>联系方式存放在 Github 首页，坚持每天一道 LeetCode，坚持每天学习，欢迎一起折腾~</p>
<blockquote>
<p>jsliang 的文档库由 <a href="https://github.com/LiangJunrong" target="_blank" rel="nofollow noopener noreferrer">梁峻荣</a> 采用 <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="nofollow noopener noreferrer">知识共享 署名-非商业性使用-相同方式共享 4.0 国际 许可协议</a> 进行许可。<br>基于 <a href="https://github.com/LiangJunrong/document-library" target="_blank" rel="nofollow noopener noreferrer">github.com/LiangJunron…</a> 上的作品创作。<br>本许可协议授权之外的使用权限可以从 <a href="https://creativecommons.org/licenses/by-nc-sa/2.5/cn/" target="_blank" rel="nofollow noopener noreferrer">creativecommons.org/licenses/by…</a> 处获得。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            