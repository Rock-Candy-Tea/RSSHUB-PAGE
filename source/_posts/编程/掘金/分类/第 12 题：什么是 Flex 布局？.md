
---
title: '第 12 题：什么是 Flex 布局？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7654'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 16:53:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=7654'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">为什么要使用 Flex 布局？</h2>
<ul>
<li>
<p>Flex 布局是目前比较流行的一种布局，因为它十分简单灵活，区区简单几行代码就可以实现各种页面的的布局，以前我在学习页面布局的时候我深受其 float、display、position 这些属性的困扰。使用 Flex 属性就可以写出简洁优雅复杂的页面布局</p>
</li>
<li>
<p>目前整理了一些 Flex 布局常用的一些属性，以下简单说一下容器和项目的意思</p>
<ul>
<li>
<p><strong>容器</strong>：采用 Flex 布局的元素，称为容器</p>
</li>
<li>
<p><strong>项目</strong>：指的是容器里面的子元素</p>
</li>
</ul>
</li>
</ul>
<h2 data-id="heading-1">容器的 6 个属性</h2>
<ul>
<li>
<p><strong>flex-direction</strong>：属性决定主轴的方向（即项目的排列方向）</p>
</li>
<li>
<p><strong>flex-wrap</strong>：默认情况下项目都排在一条轴线上，如果一行放不下如何处理（换行方式）</p>
</li>
<li>
<p><strong>flex-flow</strong>：flex-direction | flex-wrap（2 个属性的简写）</p>
</li>
<li>
<p><strong>justify-content</strong>：项目在主轴上的对齐方式（默认水平对齐方式）</p>
</li>
<li>
<p><strong>align-items</strong>：项目在交叉轴上如何对齐（默认垂直对齐方式）</p>
</li>
<li>
<p><strong>align-content</strong>：多根轴线的对齐方式（即多行的对齐方式）</p>
</li>
</ul>
<h2 data-id="heading-2">项目的 6 个属性</h2>
<ul>
<li>
<p><strong>order</strong>：项目的排列顺序。数值越小，排列越靠前，默认为 0</p>
</li>
<li>
<p><strong>flex-grow</strong>：项目的放大（默认指宽度）比例，默认为 0，即如果存在剩余空间，也不放大</p>
</li>
<li>
<p><strong>flex-shrink</strong>：项目的缩小（默认指宽度）比例，默认为 1，即如果空间不足，该项目将缩小</p>
</li>
<li>
<p><strong>flex-basis</strong>：项目将占据固定空间（默认设置固定宽度）</p>
</li>
<li>
<p><strong>flex</strong>：flex-grow | flex-shrink | flex-basis（3 个属性的缩写）</p>
</li>
<li>
<p><strong>align-self</strong>：允许单个项目有与其他项目不一样的对齐方式，可覆 align-items 属性</p>
</li>
</ul>
<p><em>参考资料：</em>
<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2015%2F07%2Fflex-grammar.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.ruanyifeng.com/blog/2015/07/flex-grammar.html" ref="nofollow noopener noreferrer">Flex 布局教程：语法篇 - 阮一峰的网络日志</a></p>
<h1 data-id="heading-3"></h1>
<h2 data-id="heading-4"><strong>文章的内容/灵感都从下方内容中借鉴</strong></h2>
<ul>
<li>
<p>【持续维护/更新 500+前端面试题/笔记】<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnoxussj%2FInterview-Questions%2Fissues" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/noxussj/Interview-Questions/issues" ref="nofollow noopener noreferrer">github.com/noxussj/Int…</a></p>
</li>
<li>
<p>【大数据可视化图表插件】<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fns-echarts" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/ns-echarts" ref="nofollow noopener noreferrer">www.npmjs.com/package/ns-…</a></p>
</li>
<li>
<p>【利用 THREE.JS 实现 3D 城市建模（珠海市）】<a href="https://link.juejin.cn/?target=https%3A%2F%2F3d.noxussj.top%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://3d.noxussj.top/" ref="nofollow noopener noreferrer">3d.noxussj.top/</a></p>
</li>
</ul></div>  
</div>
            