
---
title: '学会这几招,轻松让你的github脱颖而出'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a34f9727f21f42a2989ddbb318c9816a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 08:47:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a34f9727f21f42a2989ddbb318c9816a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>今天分享的内容我想每一位对开源感兴趣的朋友都或多或少的知道, 也是我在做开源项目中用到的一些强大的工具, 可以让我们的开源项目和 <code>github</code> 主页更加富有展现力, 最后会分享一个我自己的 <code>github</code> 主页的 <code>readme.md</code>, 大家可以参考学习一下.</p>
<p>在读完本文之后大家可以收获:</p>
<ul>
<li>使用 <strong>readme-md-generator</strong> 快速美化你的 <strong>README.md</strong></li>
<li>使用 <strong>gitHub-readme-stats</strong> 自动生成个人统计分析报表</li>
<li>使用 <strong>git-emoji</strong> 让你的代码提交记录可视化</li>
</ul>
<h3 data-id="heading-0">一. 如何让你的开源项目有个漂亮的README.md ?</h3>
<p>逛了一圈社区之后小夕发现了 <code>readme-md-generator</code>.</p>
<blockquote>
<p><strong>readme-md-generator</strong> 通过扫描我们的 <code>package.json</code> 和 <code>git</code> 配置来帮助我们生成对应的 <strong>readme</strong> 结构。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a34f9727f21f42a2989ddbb318c9816a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>产生的 <strong>README.md</strong> 类似如下展现：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e6d9677a0d847a7800ca20f59be1c75~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>另外, 一个优秀的 <code>package.json</code> 应该包含如下几个元数据:</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"H5-Dooring"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.1.3"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">"H5-Dooring是一款功能强大，开源免费的H5可视化页面配置解决方案，致力于提供一套简单方便、专业可靠、无限可能的H5落地页最佳实践。技术栈以react为主， 后台采用nodejs开发。"</span>,
  <span class="hljs-attr">"author"</span>: <span class="hljs-string">"作者信息"</span>,
  <span class="hljs-attr">"license"</span>: <span class="hljs-string">"开源协议"</span>,
  <span class="hljs-attr">"homepage"</span>: <span class="hljs-string">"主页地址"</span>,
  <span class="hljs-attr">"repository"</span>: &#123;
    <span class="hljs-attr">"type"</span>: <span class="hljs-string">"git"</span>,
    <span class="hljs-attr">"url"</span>: <span class="hljs-string">"git仓库地址"</span>
  &#125;,
  <span class="hljs-attr">"bugs"</span>: &#123;
    <span class="hljs-attr">"url"</span>: <span class="hljs-string">"供他人提issue的地址"</span>
  &#125;,
  <span class="hljs-attr">"engines"</span>: &#123;
    <span class="hljs-attr">"npm"</span>: <span class="hljs-string">">=5.5.0"</span>,
    <span class="hljs-attr">"node"</span>: <span class="hljs-string">">=9.3.0"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大家在做开源项目的时候也可以参考如上规范, 让自己的开源项目更健壮美观, 接下来分享一个我用这个工具生成的 <strong>readme.md</strong> 效果:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8507d62fc2854217b76d0d5ab09e7e1a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>地址: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FH5-Dooring%2Fmitu-editor" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/H5-Dooring/mitu-editor" ref="nofollow noopener noreferrer">mitu-editor | 轻量且强大的图片编辑器</a></p>
<h3 data-id="heading-1">二. 使用 <strong>github-readme-stats</strong> 自动生成个人统计分析报表</h3>
<p>我们都知道 <code>github</code> 的个人主页默认的配置很单调, 但是我们看很多大佬的 <code>github </code>主页, 展现非常漂亮, 比如这位大大:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccbc761f7e3d466d85de555a48c6c1e4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是为什么呢? 实不相瞒, 上图大佬就是发明美化 <strong>github个人主页</strong> 工具的作者, 我们可以看到他的个人主页有非常漂亮的统计图, 而生成这种动态统计图的工具就是 <strong>github-readme-stats</strong>. 它可以在我们的 <strong>README</strong> 中获取动态生成的 <strong>GitHub</strong> 统计信息, 而我们的使用方法也很简单, 只需要在自己 <strong>github</strong> 主页的 <strong>README</strong> 中加入如下代码:</p>
<pre><code class="copyable">[![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=anuraghazra)](https://github.com/anuraghazra/github-readme-stats)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们只需要更改 <code>?username=</code> 的值为我们自己的 <strong>GitHub</strong> 用户名即可.</p>
<h4 data-id="heading-2">定制自己的统计数据主题</h4>
<p>同时, 我们还可以轻松定制统计卡片的主题, 该工具默认提供的主题如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57fe5471830244d993272576efcb785b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>同样, 我们只需要在 <strong>README</strong> 中加入如下代码:</p>
<pre><code class="copyable">![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=anuraghazra&show_icons=true&theme=radical)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就能轻松选择自己喜欢的主题, 更强大的是我们还可以自定义主题颜色, 大家可以在 <strong>github</strong> 上亲自体验一下.</p>
<h4 data-id="heading-3">添加自己项目的热门语言卡片</h4>
<p>热门语言卡片显示了我们在 <strong>GitHub</strong> 上的开源项目常用的编程语言, 展示如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a6c5bcf02204b4b91825a8eb1dde687~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然也可以设置成紧凑型布局:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8e7bcf66ccb417ab992dd1997c95194~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>要实现这样的效果也很简单, 只需要配置如下代码:</p>
<pre><code class="copyable">[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=anuraghazra&layout=compact)](https://github.com/anuraghazra/github-readme-stats)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多的配置大家可以在 <strong>github</strong> 慢慢挖掘, 该项目的 <strong>github</strong> 地址如下:</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fanuraghazra%2Fgithub-readme-stats" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/anuraghazra/github-readme-stats" ref="nofollow noopener noreferrer">github-readme-stats</a></p>
<p>这里也展示一下我通过配置之后的 <strong>github</strong> 个人主页的界面效果:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07a1855322a84964805a8f1674f09859~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">三. 使用 git-emoji 让你的代码提交可视化</h3>
<p><strong>git-emoji</strong> 是 <strong>git</strong> 提交信息的 <strong>emoji</strong> 指南, 我们按照它的规范提交 <strong>log</strong> 日志, 将会生成形象易懂的提交表情, 如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15f06204ce9b406791e9b6e4d16e4485~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们看到的比较有名的开源项目提交都会有形象的 <strong>emoji</strong>, 也都是遵循了对应的提交规范. 下面是它的介绍网站:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bc4f6a63eb048258c98a3245b7d4d52~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在线地址: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitmoji.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://gitmoji.js.org/" ref="nofollow noopener noreferrer">gitmoji.js.org/</a></p>
<p>我们可以使用它的指南来轻松优化我们开源的提交 <strong>log</strong>, 赶紧来试试吧~</p>
<h3 data-id="heading-5">最后</h3>
<p>这里分享一个我配置好的 <strong>github README</strong>模版, 大家可以参考一下: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMrXujiang%2FMrXujiang" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MrXujiang/MrXujiang" ref="nofollow noopener noreferrer">美化你的github个人主页</a>, 后期我会在数据可视化和工程化上输出更多实用的开源项目和框架，如果有其他问题或需求，可以和笔者交流学习。</p>
<p>如果这篇文章对你有帮助，希望能给笔者 <strong>点赞+收藏</strong> 以此鼓励作者继续创作前端硬核文章。也可以关注作者公众号 <strong>趣谈前端</strong> 第一时间推送前端好文。</p>
<ul>
<li><a href="https://juejin.cn/post/6986824393653485605" target="_blank" title="https://juejin.cn/post/6986824393653485605">如何设计可视化搭建平台的组件商店？</a></li>
<li><a href="https://juejin.cn/post/6981257575425654792" target="_blank" title="https://juejin.cn/post/6981257575425654792">从零设计可视化大屏搭建引擎</a></li>
<li><a href="https://juejin.cn/post/6976476731662139428" target="_blank" title="https://juejin.cn/post/6976476731662139428">从零使用electron搭建桌面端可视化编辑器Dooring</a></li>
<li><a href="https://juejin.cn/post/6973946702235615269" target="_blank" title="https://juejin.cn/post/6973946702235615269">(低代码)可视化搭建平台数据源设计剖析</a></li>
<li><a href="https://juejin.cn/post/6950075140906418213" target="_blank" title="https://juejin.cn/post/6950075140906418213">从零搭建一款PC页面编辑器PC-Dooring</a></li>
<li><a href="https://juejin.cn/post/6904878119724056584" target="_blank" title="https://juejin.cn/post/6904878119724056584">如何搭积木式的快速开发H5页面?</a></li>
</ul></div>  
</div>
            