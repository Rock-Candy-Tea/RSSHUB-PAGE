
---
title: 'Component inside _Transition_ renders non-element root node that cannot be ani..'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8161b2d60c704d6da98e0c04fe85b59b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 01:16:26 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8161b2d60c704d6da98e0c04fe85b59b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>问题现象，如下图所示，左侧“发版配置”菜单对应的路由是/release-config/index，在这个路径上刷新页面时候</p>
<p>右侧的内容（组件）是可以加载出来的。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8161b2d60c704d6da98e0c04fe85b59b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是当点击左侧的其他菜单，比如“消息通知”时，消息通知所对应的右侧内容（组件）就加载不出来了，</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0da2532a60e42e0b53abcce82b8223a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>而且点回“发版配置”菜单时，发版配置对应的右侧内容（组件）也加载不出来了。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a02ff27a4db41f3b03e1070516793a0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在控制台可以看到如下的Vue warn：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6983f5f1c257404289d983cc8217897b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>Component inside <Transition> renders non-element root node that cannot be animated.</strong></p>
<p>这个warn是因为组件中包裹的不是一个单节点元素。</p>
<p>确实，我们在<code><router-view></code>中使用了<code><transition></code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><router-view v-slot=<span class="hljs-string">"&#123; Component, route &#125;"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">transition</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"zoom-fade"</span> <span class="hljs-attr">mode</span>=<span class="hljs-string">"out-in"</span> <span class="hljs-attr">appear</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">keep-alive</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">:is</span>=<span class="hljs-string">"Component"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">keep-alive</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">transition</span>></span></span>
</router-view>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code><keep-alive></code>、<code><component></code>都不会创建真实的DOM元素，直接包裹在<code><transition></code>中的，就是我们自己写的组件，也就是传给<code><component></code>的<code>is</code>属性的<code>Component</code>。</p>
<p>出现问题的“发版配置”菜单所对应的右侧内容组件是这样的：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8188216bf124bc4b455ffb733389b04~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了方便看，我把代码折叠了，<code><template></code>模板中等于使用了vue3的<code>Fragments</code>特性，存在两个root节点。这就是<code><transition></code>报错的原因。</p>
<p>既然是<code><transition></code>中不能有多个root元素，那解决方法就有两个，</p>
<ol>
<li>不使用<code><transition></code></li>
<li>把我们的组件都包裹成单root节点</li>
</ol>
<p>但是还是想用<code><transition></code>带来的动画效果，因此采用办法2。</p>
<p>最后再重新看下vue3文档关于<code><transition></code>的介绍：</p>
<p><code><transition></code> serve as transition effects for <strong>single</strong> element/component. The <code><transition></code> only applies the transition behavior to the wrapped content inside;</p>
<p><code><transition></code>只能用于<strong>单元素/组件</strong>之上。</p></div>  
</div>
            