
---
title: '2021 年了，你不还来试试 TailwindCSS 吗'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a47f0cf5a7c4152abbaeec16a1b081a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 28 May 2021 00:40:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a47f0cf5a7c4152abbaeec16a1b081a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://tailwindcss.com/" target="_blank" rel="nofollow noopener noreferrer">TailwindCSS</a> 是 CSS 框架，旨在快速编写样式。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a47f0cf5a7c4152abbaeec16a1b081a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我第一感觉看到官网的介绍时，我寻思这不就是一个包含了很多样式的样式表吗，和以前 bootstrap 这种那样，他自带了很多样式，完了之后你直接用他自带的就行了。</p>
<p>但是 TailwindCSS 并不只是这么简单。TailwindCSS 不仅是内置了很多样式，也支持通过配置文件去配置，覆盖掉内置的样式，或者扩展自己的样式，一般定制颜色居多。</p>
<p>TailwindCSS 最基本的使用方式，就是和之前 bootstarp 等 CSS 库用法没什么两样，就是 class 上加各种类名。TailwindCSS 的类名都是由 属性缩写 + 属性程度 + [属性值]。比如在默认情况下，TailwindCSS 对于数值分成几个程度，每个程度为 0.25rem。如： <code>mt-2</code> 表示 <code>margin-top: 0.5rem</code> 。对于 opacity 等属性还有属性值，如<code>bg-opacity-30</code> 表示 <code>--tw-bg-opacity: 0.3; // e.g. background-color: rgba(0, 0, 0, var(--tw-bg-opacity));</code>。（对于颜色、变换等，都会使用变量。）还提供了一些字面量，如 <code>md</code> <code>sm</code> 等用于响应式布局。</p>
<p>以上都是最基本的东西，好像看起来不过如此？而且根本记不住。没事，有 <a href="https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss" target="_blank" rel="nofollow noopener noreferrer">Tailwind CSS IntelliSense</a> ，写类名飞快。对加练习，铁定比 Emmet 写得快。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90d39d63a56b49f6b8a2d9ff9d348d74~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过配置 TailwindCSS，可以自定义很多属性，如颜色。比如上图的 <code>bg-background-regular</code> regluar 就是自定义的颜色，只要定义一次，之后在各个颜色样式都能使用。如 <code>text-regular</code> <code>border-regular</code>。直 TailwindCSS 2.1 之后，开启 JIT，还可以生成 raw 属性的样式。如 <code>h-[40px]</code> 就是把 40px 作为值了，是实时生成的。</p>
<p>那么，说了这么多了。写了这么多 class 到一个标签上不会很乱吗。这个时候，PostCSS + TailwindCSS 登场了。TailwindCSS 其实一个 PostCSS 的插件。PostCSS 都不陌生，用来对 CSS 进行各种预处理的。配置 PostCSS，就可以使用一些特殊语法了。比如在 css 文件里使用 <code>@apply</code> 附加 TailwindCSS 样式。如：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.test</span> &#123;
  <span class="hljs-keyword">@apply</span> relative w-full h-[<span class="hljs-number">40px</span>] bg-background-regular flex items-center justify-between px-<span class="hljs-number">4</span> truncate;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注：需要安装 PostCSS Language Server 才能使用针对于 PostCSS 的补全。PostCSS 也是一种格式，扩展名为 <code>.css</code> <code>.pcss</code></p>
<p>还有 <code>@screen</code> <code>@components</code> 等方法具体不再展开。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@screen</span> desktop &#123; <span class="hljs-comment">/* @media(max-width: 1024px), 需要单独配置 */</span>
  <span class="hljs-selector-class">.test</span> &#123;
    <span class="hljs-keyword">@apply</span> bg-white;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，PostCSS 也支持插件，可以扩展近似 SCSS 的语法。</p>
<p>好像，以上都没有用？</p>
<p>最后，放大招了。相信很多切图仔，每天就是对着图稿切切图。</p>
<p>打开 Figma，随便找一个区域，选中，插件，Figma to Code, Tailwind 2。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bb3989a08294753a583e371ba10b8e3~tplv-k3u1fbpfcp-zoom-1.image" alt="¡爽！" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            