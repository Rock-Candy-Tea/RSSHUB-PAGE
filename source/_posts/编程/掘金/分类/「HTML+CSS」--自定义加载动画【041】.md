
---
title: '「HTML+CSS」--自定义加载动画【041】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d00d15e1d3c49369e29f0eb5649c41b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 23:09:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d00d15e1d3c49369e29f0eb5649c41b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<blockquote>
<p>Hello！小伙伴！</p>
<p>首先非常感谢您阅读海轰的文章，倘若文中有错误的地方，欢迎您指出～</p>
<p>哈哈 自我介绍一下</p>
<p>昵称：海轰</p>
<p>标签：程序猿一只｜C++选手｜学生</p>
<p>简介：因C语言结识编程，随后转入计算机专业，有幸拿过国奖、省奖等，已保研。目前正在学习C++/Linux（真的真的太难了～）</p>
<p>学习经验：扎实基础 + 多做笔记 + 多敲代码 + 多思考 + 学好英语！</p>
</blockquote>
<h1 data-id="heading-1">效果展示</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d00d15e1d3c49369e29f0eb5649c41b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">Demo代码</h1>
<p>HTML</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"style.css"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">section</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">section</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CSS</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">html</span>, <span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
&#125;

<span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">justify-content</span>: center;
  <span class="hljs-attribute">align-items</span>: center;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#263238</span>;
&#125;

<span class="hljs-selector-tag">section</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">650px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">align-items</span>: center;
  <span class="hljs-attribute">justify-content</span>: center;
  <span class="hljs-comment">/* 红色边框仅作提示 */</span>
  <span class="hljs-attribute">border</span>: <span class="hljs-number">2px</span> solid red;
&#125;

<span class="hljs-selector-tag">span</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">48px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">48px</span>;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">display</span>: inline-block;
  <span class="hljs-attribute">color</span>: white;
  <span class="hljs-attribute">animation</span>: rotation <span class="hljs-number">1s</span> linear infinite;
&#125;

<span class="hljs-selector-tag">span</span><span class="hljs-selector-pseudo">::before</span>, <span class="hljs-selector-tag">span</span><span class="hljs-selector-pseudo">::after</span> &#123;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">24px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">24px</span>;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
  <span class="hljs-attribute">background-color</span>: white;
  <span class="hljs-attribute">animation</span>: scale <span class="hljs-number">1s</span> infinite ease-in-out;
&#125;

<span class="hljs-selector-tag">span</span><span class="hljs-selector-pseudo">::before</span> &#123;
  <span class="hljs-attribute">top</span>: auto;
  <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">background-color</span>: red;
  <span class="hljs-attribute">animation-delay</span>: .<span class="hljs-number">5s</span>;
&#125;

<span class="hljs-keyword">@keyframes</span> rotation &#123;
  <span class="hljs-number">0%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0deg</span>)
  &#125;
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">360deg</span>)
  &#125;
&#125;

<span class="hljs-keyword">@keyframes</span> scale &#123;
  <span class="hljs-number">0%</span>, <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">0</span>)
  &#125;
  <span class="hljs-number">50%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">1</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">原理详解</h1>
<h3 data-id="heading-4">步骤1</h3>
<p>使用span标签，设置</p>
<ul>
<li>宽度、高度均为48px</li>
<li>使用flex布局</li>
<li>其中的元素左右居中</li>
</ul>
<pre><code class="hljs language-cpp copyable" lang="cpp"> width: <span class="hljs-number">48</span>px;
  height: <span class="hljs-number">48</span>px;
  display: flex;
  justify-content: center;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a73dc89e65b454e825fd27697c738d1~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">步骤2</h3>
<p>使用span::before、span::after伪类元素</p>
<p>其中before作为红色小球，after作为白色小球</p>
<p>设置</p>
<ul>
<li>绝对定位</li>
<li>高度、宽度均为24px</li>
<li>before位于正下方 after位于正上方</li>
</ul>
<pre><code class="hljs language-cpp copyable" lang="cpp">span::before, span::after &#123;
  position: absolute;
  content: <span class="hljs-string">'';
  width: 24px;
  height: 24px;
&#125;
span::before &#123;
  bottom: 0;
  background-color: red;
&#125;
span::after&#123;
  background-color: white;
  top: 0;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/634e1cc2e8344d689cba66c50faf8806~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
span与span::before、span::after的位置关系
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccefd672b58d4010b2a7c0e4170d73b2~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">步骤3</h3>
<p>span::before、span::after圆角化</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"> border-radius: <span class="hljs-number">50</span>%;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2788fc64742d42678031792cbba5d1d6~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">步骤4</h3>
<p>为span::before和span::after添加动画</p>
<ul>
<li>初始状态：大小为0（相对于原大小）</li>
<li>最终状态：大小为1（相对于原大小）</li>
</ul>
<pre><code class="hljs language-cpp copyable" lang="cpp">span::before, span::after &#123;
  animation: scale <span class="hljs-number">1</span>s infinite ease-in-out;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-cpp copyable" lang="cpp">@keyframes scale &#123;
  <span class="hljs-number">0</span>%, <span class="hljs-number">100</span>% &#123;
    transform: <span class="hljs-built_in">scale</span>(<span class="hljs-number">0</span>)
  &#125;
  <span class="hljs-number">50</span>% &#123;
    transform: <span class="hljs-built_in">scale</span>(<span class="hljs-number">1</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c8c0e171488487aaffe69664271422e~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">步骤5</h3>
<p>对span::before的动画延时</p>
<pre><code class="hljs language-cpp copyable" lang="cpp">
span::before &#123;
  animation-delay: <span class="hljs-number">.5</span>s; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3c81be3ce4749ff8ed04d647b7136df~tplv-k3u1fbpfcp-zoom-1.image" alt="动画1" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">步骤6</h3>
<p>为span添加动画</p>
<ul>
<li>顺时针旋转 1s 无限循环</li>
</ul>
<pre><code class="hljs language-cpp copyable" lang="cpp">span &#123;
  animation: rotation <span class="hljs-number">1</span>s linear infinite;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-cpp copyable" lang="cpp">@keyframes rotation &#123;
  <span class="hljs-number">0</span>% &#123;
    transform: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>deg)
  &#125;
  <span class="hljs-number">100</span>% &#123;
    transform: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">360</span>deg)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果此时<strong>span::before、span::after设置的动画不起作用</strong></p>
<p>那么此时的效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7b1d6318ca947d7b561ee2d7eb8974f~tplv-k3u1fbpfcp-zoom-1.image" alt="动画2" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在前面的设置里</p>
<p>我们分别对span、span::before和span::after设置了动画</p>
<p>那么最后的产生的结果就是：两个动画的组合（既在执行动画1，又在执行动画2）</p>
<p><strong>最终视觉效果如下</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d3cb30b70d6477bbd7a0e5513804402~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-10">结语</h1>
<p>学习来源：</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2Fbhadupranjal%2Fpen%2FvYLZYqQ" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/bhadupranjal/pen/vYLZYqQ" ref="nofollow noopener noreferrer">codepen.io/bhadupranja…</a></p>
</blockquote>
<p>文章仅作为学习笔记，记录从0到1的一个过程。希望对您有所帮助，如有错误欢迎小伙伴指正～</p>
<p>我是海轰ଘ(੭ˊᵕˋ)੭，如果您觉得写得可以的话，请点个赞吧</p>
<p>写作不易，<strong>「点赞」</strong>+<strong>「收藏」</strong>+<strong>「转发」</strong></p>
<p>谢谢支持❤️</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c18d9709949b48e08fa45f6f10851a5d~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            