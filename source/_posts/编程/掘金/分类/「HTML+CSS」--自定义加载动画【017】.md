
---
title: '「HTML+CSS」--自定义加载动画【017】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6842c0cfd1b41ff8ba6190584db87cf~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 29 May 2021 02:46:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6842c0cfd1b41ff8ba6190584db87cf~tplv-k3u1fbpfcp-zoom-1.image'
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
<p>日常分享：微信公众号【海轰Pro】记录生活、学习点滴，分享一些源代码或者学习资料，欢迎关注～</p>
</blockquote>
<h1 data-id="heading-1">效果展示</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6842c0cfd1b41ff8ba6190584db87cf~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
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
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">html</span>,<span class="hljs-selector-tag">body</span>&#123;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
&#125;
<span class="hljs-selector-tag">body</span>&#123;
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

<span class="hljs-selector-tag">span</span>&#123;
  <span class="hljs-attribute">width</span> : <span class="hljs-number">96px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">96px</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">5px</span> solid ;
  <span class="hljs-attribute">border-color</span>: white ;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>; 
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">justify-content</span>: center;
  <span class="hljs-attribute">animation</span>: rotation <span class="hljs-number">2s</span> linear infinite;
&#125;
<span class="hljs-selector-tag">span</span><span class="hljs-selector-pseudo">::before</span>&#123;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
  <span class="hljs-attribute">background</span>: red;
  <span class="hljs-attribute">width</span>:  <span class="hljs-number">3px</span>;
  <span class="hljs-attribute">height</span>:  <span class="hljs-number">48px</span>;
&#125;

<span class="hljs-keyword">@keyframes</span> rotation &#123;
  <span class="hljs-number">0%</span> &#123; <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0deg</span>) &#125;
  <span class="hljs-number">100%</span> &#123; <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">360deg</span>)
  &#125;
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">原理详解</h1>
<h3 data-id="heading-4">步骤1</h3>
<p>使用span标签作为表盘的白色部分，并设置</p>
<ul>
<li>宽度、高度均为96px</li>
<li>边框：5px 白色 solid</li>
</ul>
<pre><code class="hljs language-csharp copyable" lang="csharp"> width : <span class="hljs-number">96</span>px;
  height: <span class="hljs-number">96</span>px;
  border: <span class="hljs-number">5</span>px solid ;
  border-color: white ;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a6b2981501d4ff2a7fc5e415d82b122~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">步骤2</h3>
<p>使用span::before伪类作为红色的指针，并设置</p>
<ul>
<li>span::before位于span水平居中，上部与span靠齐（对span使用flex布局，并设置justify-content: center; ）</li>
<li>宽度为3px 高度为48px</li>
<li>背景色：红色</li>
<li>相对定位</li>
</ul>
<pre><code class="hljs language-csharp copyable" lang="csharp">  position: relative;
  content: <span class="hljs-string">''</span>;
  background: red;
  width:  <span class="hljs-number">3</span>px;
  height:  <span class="hljs-number">48</span>px;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07a77660e2a845f59aaabb577e958e5b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">步骤3</h3>
<p>span圆角化</p>
<pre><code class="hljs language-csharp copyable" lang="csharp">border-radius: <span class="hljs-number">50</span>%; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e100f0a71c74931a789ad15d746625b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">步骤4</h3>
<p>对span添加动画</p>
<ul>
<li>顺时针 2s 无限循环</li>
</ul>
<pre><code class="hljs language-csharp copyable" lang="csharp"> animation: rotation <span class="hljs-number">2</span>s linear infinite;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-csharp copyable" lang="csharp">span::before&#123;
  position: relative;
  content: <span class="hljs-string">''</span>;
  background: red;
  width:  <span class="hljs-number">3</span>px;
  height:  <span class="hljs-number">48</span>px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68d5554f91b14c8fab692181dedb022d~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-8">结语</h1>
<p>学习来源：</p>
<blockquote>
<p><a href="https://codepen.io/bhadupranjal/pen/vYLZYqQ" target="_blank" rel="nofollow noopener noreferrer">codepen.io/bhadupranja…</a></p>
</blockquote>
<p>文章仅作为学习笔记，记录从0到1的一个过程。希望对您有所帮助，如有错误欢迎小伙伴指正～</p>
<p>我是海轰ଘ(੭ˊᵕˋ)੭，如果您觉得写得可以的话，请点个赞吧</p>
<p>写作不易，<strong>「点赞」</strong>+<strong>「收藏」</strong>+<strong>「转发」</strong></p>
<p>谢谢支持❤️</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f5a09c424e445eb9527698e1929f23c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            