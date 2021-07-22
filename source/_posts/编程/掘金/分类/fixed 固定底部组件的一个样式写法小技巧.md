
---
title: 'fixed 固定底部组件的一个样式写法小技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/733b9107f645401a9a2c5a24377a905e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 01:55:26 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/733b9107f645401a9a2c5a24377a905e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">正文</h2>
<p>某次修改一个页面的逻辑，页面布局比较简答，整个页面 <code>overflow-y: auto;</code>，页面的底部放置一个 <code>position: fixed;</code>的固定按钮，如下：</p>
<img width="300" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/733b9107f645401a9a2c5a24377a905e~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<p>为了避免页面主体内容被底部的固定按钮遮挡，页面使用了一个 <code>padding-bottom</code> 的样式属性，大概关键布局代码和样式代码是这么写的：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main"</span>></span>...<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"footer"</span>></span>这是固定在底部的按钮<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-pseudo">:root</span> &#123;
--<span class="hljs-selector-tag">footer</span>-<span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
&#125;
<span class="hljs-selector-class">.main</span> &#123;
<span class="hljs-attribute">padding-bottom</span>: <span class="hljs-built_in">var</span>(--header-height);
  <span class="hljs-attribute">overflow-y</span>: auto;
&#125;
<span class="hljs-selector-class">.footer</span> &#123;
  <span class="hljs-attribute">position</span>: fixed;
  <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-built_in">var</span>(--header-height);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我需要加一个<code>A</code>逻辑，当满足我这个 <code>A</code>逻辑的时候，底部固定按钮就不展示了，其他情况则展示</p>
<p>这么一来样式布局就变化了，如果符合我加的<code>A</code>逻辑，那么 <code>.main</code>的 <code>padding-bottom</code> 属性就得删掉了，所以我还得额外再加样式的逻辑</p>
<p>加这个额外的样式逻辑倒是没问题，但实际上这本来是没必要的，况且在页面业务逻辑比较复杂、测试覆盖不够全面的时候，再加上如果这个页面大部分逻辑都不是你写的，那么是很容易遗忘这一点的</p>
<p>一般而言，在一个项目中，为了起到复用组件的目的，底部固定按钮作为一个明显存在固定UI规范、明显可以被复用的组件，都是会被设计为通用组件的，通用组件是为了配合主体业务页面的，如果变成反过来，我为了使用你这个通用组件还得专门在主体业务页面里写额外的判断样式逻辑，那说明这个通用组件是不够通用的</p>
<p>我希望在使用这个底部固定按钮的时候，这个组件不应该影响到我主体页面的其他部分，例如整体的样式布局，但是实际上，针对底部固定按钮这个具体组件而言，我发现很多人都是这么设计组件的</p>
<p>如果换做是我来做这个组件，我会这么写：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main"</span>></span>...<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"footer"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"footer-content"</span>></span>这是固定在底部的按钮<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-pseudo">:root</span> &#123;
--<span class="hljs-selector-tag">footer</span>-<span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
&#125;
<span class="hljs-selector-class">.main</span> &#123;
  <span class="hljs-attribute">overflow-y</span>: auto;
&#125;
<span class="hljs-selector-class">.footer</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-built_in">var</span>(--header-height);
&#125;
<span class="hljs-selector-class">.footer-content</span> &#123;
<span class="hljs-attribute">position</span>: fixed;
  <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-built_in">var</span>(--header-height);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根本不需要 <code>.main</code> 元素专门写一个 <code>padding-bottom</code>来配合底部固定按钮组件，因为组件自己会撑开高度</p>
<p>相比于文章开头的那种写法，我后面的写法，是多套了一层元素，这多出来的一层元素并不设置 <code>position: fixed;</code>，是一个位于文档流中占据实际空间的元素，且其高度与其子元素相同，其子元素才是真正有展示效果的且 <code>fixed</code> 固定的元素，即父元素负责撑开高度，子元素负责底部固定展示</p>
<p>这种方法的缺点在于，因为底部固定子元素是 <code>position: fixed;</code>，所以无法撑开高度，必须要确定底部固定的子元素高度才能设置父元素的高度</p>
<p>但一般来说这并不算是个问题，底部固定元素基本上都是以按钮的形式出现，而底部固定按钮这种通用组件，一般而言其尺寸、圆角、字号大小都是固定的，无非是颜色和文案可能需要换一换，总之高度大概率是可以提前确定的是不会变的，直接硬编码一个高度就完事</p>
<p>如果真的是存在高度需要变化，那么也不是问题，无非是即时测量一下罢了</p>
<p>当然，这个方法不仅是针对于底部固定元素，顶部固定元素也是同样的道理</p>
<h2 data-id="heading-1">小结</h2>
<p>第二种方法的小技巧其实是我很久之前的一个个人思考的结果（当然你可能也想到了），当时我和大多数人一样，都习惯使用 <code>padding-bottom</code>来维持主体页面和底部固定按钮的关系，但有一次我觉得总是写 <code>padding-bottom</code> 很烦，而且觉得这不合理，所以思考了一下如何将其变得更好，于是我就多会了一个小技巧</p>
<p>写业务代码也是需要有思考的，业务代码没有什么技术上的难度，思考的是如何保证代码项目的可维护性，技术的选型、组件的设计、结构的解耦等都是可思考的方向，这些东西可能很难在绩效上体现出来，但最起码自己写起来更舒服了不是吗？</p></div>  
</div>
            