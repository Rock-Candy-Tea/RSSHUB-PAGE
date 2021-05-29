
---
title: 'Hexo 搭建教程 爬坑日记-1'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d26f7d7c48e4484905f47110f4c4cb5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 28 May 2021 04:12:15 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d26f7d7c48e4484905f47110f4c4cb5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">缘起</h2>
<p>2017年的时候就曾尝试在 githubPages上搭建自己的Blog 尝试过，当时的结果似乎成功了吧。由于年少轻狂此事也就不了了之。时光飞逝，我已快步入30，回归过去展望未来都没有一点点依据。因此我思考再三，决定打造一个属于自己的日记本，以防忘记什么，或者有什么遗憾。</p>
<h2 data-id="heading-1">构思</h2>
<p>于是乎我脑子就开始有一个理想的轮廓</p>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
step1:选择博客网站生成器 --> step2:本地搭建 --> Step3:部署至线上 --> Step4:坚持产出文章
</code></pre>
<p>好的就是这样开干！</p>
<h2 data-id="heading-2">开始整！！！</h2>
<ul>
<li><strong>google 搜索关键字  blog framework</strong></li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d26f7d7c48e4484905f47110f4c4cb5~tplv-k3u1fbpfcp-watermark.image" width="80%" height="80%" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>选择适合自己且它也喜欢我的博客网站生成器</strong>
<ul>
<li><a href="https://juejin.cn/post/6967312527990620173">Hexo</a>  这个就是google搜索排名第一的开源博客框架 早年间也是用它搭建的第一个demo博客</li>
<li><a href="https://juejin.cn/post/6967312527990620173">Jekyll</a></li>
<li><a href="https://juejin.cn/post/6967312527990620173">Hugo</a></li>
<li><a href="https://juejin.cn/post/6967312527990620173">Octopress</a></li>
<li><a href="https://juejin.cn/post/6967312527990620173">Pelican</a></li>
<li><a href="https://juejin.cn/post/6967312527990620173">Middleman</a></li>
<li><a href="https://juejin.cn/post/6967312527990620173">DocPad</a></li>
<li><a href="https://juejin.cn/post/6967312527990620173">Wintersmith</a></li>
<li><a href="https://juejin.cn/post/6967312527990620173">Cactus</a></li>
<li><a href="https://juejin.cn/post/6967312527990620173">HubPress</a></li>
</ul>
</li>
</ul>
<p>经过一番深思熟悉 就选择Hexo 8 理由 大家都用他 网上文字类 以及视频类教程居多，如果看文档依旧无法成功可以窃取他人的胜利果实</p>
<p>qq交流群：1064155906（交流经验 分享资料）
<strong>未完待续...</strong></p></div>  
</div>
            