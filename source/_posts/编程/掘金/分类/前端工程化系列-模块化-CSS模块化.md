
---
title: '前端工程化系列-模块化-CSS模块化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1126'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 01:45:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=1126'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. 在中大项目编写 CSS 的普遍问题</h1>
<ul>
<li>高耦合——改样式的时候，会同时影响其他地方的样式，导致意外的样式问题</li>
<li>低复用——重复编写相同的样式，即枯燥乏味又导致 CSS 体积过大，从而影响开发体验与页面加载体验</li>
</ul>
<h1 data-id="heading-1">2.CSS 模块化能解决哪些问题</h1>
<p>样式复用、按需加载、局部作用局</p>
<h1 data-id="heading-2">3. CSS 模块化解决方案</h1>
<p><strong>原理基本</strong>：基本上目前所有的解决方案，都是通过控制样式权重、定义全局唯一的样式名称，来达到模块化、控制作用局的效果</p>
<h2 data-id="heading-3">3.1 官方方案</h2>
<p>大家都知道一个页面中的 CSS 样式的作用范围是全局的，这同时是它的优点与缺点，其样式覆盖规则是根据标签样式继承规则、样式选择器权重、样式定义顺序等来决定最终展示的样式，而 CSS 官方没有给出控制 CSS 作用域的解决方案。</p>
<p>在前端发展的早期，我们写 CSS 的进化过程大致如下：</p>
<ol>
<li><strong>style属性</strong>：最原始的时候，直接将样式通过 style 属性的方式写入标签，大量的样式充斥在 HTML 中，导致 HTML 标签与样式难以维护</li>
<li><strong><style>标签</strong>：后来,为了保持 HTML 的简洁，将 CSS 统一写在 <style> 标签里，但无法复用样式、无法缓存样式</li>
<li><strong><link>标签</strong>：然后,将样式写在 .css 文件中，通过 <link> 标签来引入 .css 文件，但没有解决 CSS 作用域问题</li>
<li><strong>@import语法</strong>：最后, @import 语法解决了更细粒度的复用问题，可以在一个 .css 文件中通过 @import 引入多个 .css 文件，但加载速度较慢，且仍未解决 CSS 作用域问题</li>
</ol>
<h2 data-id="heading-4">3.2 约定式方案</h2>
<p><strong>该类方案主要有这几种</strong>：BEM、OOCSS、MCSS、AMCSS、SMACSS、Atomic CSS、ITCSS、SUITCSS</p>
<p><strong>这类方案的基本思想：</strong></p>
<ul>
<li>通过约定来规范CSS的命名，以解决命名冲突问题</li>
<li>通过提供或推荐分层设计好的CSS代码，来达到样式复用的目的</li>
</ul>
<p><strong>典型实现方式</strong>：引入实现 Atomic CSS 思想的 Tailwind CSS 框架</p>
<h2 data-id="heading-5">3.3 工具式方案</h2>
<h3 data-id="heading-6">Scoped CSS</h3>
<p><strong>原理</strong>：通过在编译时给每个样式定义处加上全局唯一的属性选择器，并在样式使用的地方加上同样的属性名，来达到模块化CSS局部作用域的效果<br>
<strong>优点</strong>：上手简单<br>
<strong>缺点</strong>：由于属性选择器的权重不够高，导致外部样式依然能够影响其vue组件内样式，因此局部作用域的效果不够彻底<br>
<strong>典型实现方式</strong>：在 Vue 组件中 <style> 标签上添加 Scoped 属性<br></p>
<h3 data-id="heading-7">CSS Modules</h3>
<p><strong>原理</strong>：通过在编译时直接将每个样式名替换成全局唯一的名称，来达到模块化 CSS 局部作用域的效果<br>
<strong>优点</strong>：CSS Modules 能最大化地结合现有 CSS 生态 (预处理器/后处理器等) 和 JS 模块化能力<br>
<strong>缺点</strong>：与组件库难以配合<br>
<strong>典型实现方式</strong>：在 Webpack 的 css-loader 中启用 CSS Modules<br></p>
<h3 data-id="heading-8">CSS in JS</h3>
<p><strong>原理</strong>：与 CSS Modules 相似，通过在编译时直接将每个样式名替换成全局唯一的名称，来达到模块化 CSS 局部作用域的效果<br>
<strong>优点</strong>：通过将业务相关的 HTML、CSS、JS 代码写在一起，以便后期维护与移植；充分利用 JS 的编程能力来实现复杂的样式动态效果<br>
<strong>缺点</strong>：需要一些学习成本；代码复杂度增高；不能利用成熟的 CSS 预处理器（或后处理器）；无法方便地使用伪类，媒体查询等<br>
<strong>典型实现方式</strong>：引入 styled-components 插件<br></p></div>  
</div>
            