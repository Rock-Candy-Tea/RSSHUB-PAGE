
---
title: '「HTML+CSS」--自定义加载动画【023】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f4b9b4765664725b5a383f35fe3d290~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 06:37:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f4b9b4765664725b5a383f35fe3d290~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第1天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557?utm_campaign=30day&utm_medium=Ccenter&utm_source=20210528" target="_blank">更文挑战</a></p>
<h1 data-id="heading-0">前言</h1>
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
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f4b9b4765664725b5a383f35fe3d290~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">思路</h1>
<h1 data-id="heading-3">Demo代码</h1>
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
    <span class="hljs-attribute">border</span>: <span class="hljs-number">2px</span> solid red;
&#125;
<span class="hljs-selector-tag">span</span> &#123;
  <span class="hljs-attribute">width</span> : <span class="hljs-number">96px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">96px</span>;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
  <span class="hljs-attribute">display</span>: inline-block;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">border-top</span>: <span class="hljs-number">10px</span> solid white;
  <span class="hljs-attribute">border-right</span>: <span class="hljs-number">10px</span> solid transparent;
  <span class="hljs-attribute">animation</span>: rotation <span class="hljs-number">2s</span> linear infinite;
&#125;
<span class="hljs-selector-tag">span</span><span class="hljs-selector-pseudo">::after</span>&#123;
  <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
      <span class="hljs-attribute">position</span>: absolute;
      <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">width</span> : <span class="hljs-number">96px</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">96px</span>;
      <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
      <span class="hljs-attribute">border-bottom</span>:<span class="hljs-number">10px</span> solid transparent;
      <span class="hljs-attribute">border-left</span>:<span class="hljs-number">10px</span> solid red;
      <span class="hljs-attribute">animation</span>: rotation <span class="hljs-number">1s</span> linear infinite reverse;
&#125;

<span class="hljs-keyword">@keyframes</span> rotation &#123;
  <span class="hljs-number">0%</span> &#123; <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0deg</span>) &#125;
  <span class="hljs-number">100%</span> &#123; <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">360deg</span>) &#125;
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">原理详解</h1>
<h3 data-id="heading-5">步骤1</h3>
<p>设置span标签</p>
<ul>
<li>宽度、高度均为96px</li>
</ul>
<pre><code class="hljs language-csharp copyable" lang="csharp">  width : <span class="hljs-number">96</span>px;
  height: <span class="hljs-number">96</span>px;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c063c4d571b4b8faffa647aaa288d76~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
span此时是没有显示出来的</p>
<p>因为没有设置颜色
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b498512787a1436b88a9aabbe9f84c46~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">步骤2</h3>
<p>span<strong>上边框</strong>设置为</p>
<ul>
<li>10px solid 白色</li>
</ul>
<p>效果图如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45a67d5c33b64958872f4755625c4cd1~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">步骤3</h3>
<p>span<strong>右边框</strong>设置为</p>
<ul>
<li>10px solid 透明色</li>
</ul>
<p>效果图如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13ce05b738994e999c23d8fa3d61a91d~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
为什么再设置右边框就会变成这样了呢？</p>
<p>这里如果设置右边框的颜色为红色</p>
<p>根据下图就可以知道上图是怎么来的了（用透明色替换下图中红色）
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/881087b97d1b44daafebcc758a2febab~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">步骤4</h3>
<p>设置span::after</p>
<ul>
<li>绝对定位 left:0 top:0</li>
<li>宽度、高度均为96px</li>
</ul>
<p>效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/edf028a2c2e44abb8d03595276f34edf~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
因为没有为span::after设置背景色</p>
<p>视觉上就没有显示出来</p>
<p>实际是存在的
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9283be903da44694989dd71da10418b2~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
这里用紫色表示一下span::after</p>
<p>就可以观察到了
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0fef1c34a2749a7a6ef5431023c8b16~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">步骤5</h3>
<p>设置span::after，使得左边框为10px solid 红色</p>
<pre><code class="hljs language-csharp copyable" lang="csharp">  border-left:<span class="hljs-number">10</span>px solid red;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b226c444bb9343d08b528a624894ec0c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">步骤6</h3>
<p>再设置span::after下边框：10px solid 透明</p>
<pre><code class="hljs language-csharp copyable" lang="csharp">border-bottom:<span class="hljs-number">10</span>px solid transparent;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f783d64fcb8245d0b872dbe5f164bf91~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注：红色部分的生成方法其实与白色部分完全相同。</p>
<h3 data-id="heading-11">步骤7</h3>
<p>span、span::after圆角化</p>
<pre><code class="hljs language-csharp copyable" lang="csharp">border-radius: <span class="hljs-number">50</span>%;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d54c9b8a6f774ae3a85245ac548df347~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">步骤8</h3>
<p>为span添加动画</p>
<ul>
<li>顺时针旋转（0-360度） 2s 无限循环</li>
</ul>
<pre><code class="hljs language-csharp copyable" lang="csharp">  animation: rotation <span class="hljs-number">2</span>s linear infinite;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-csharp copyable" lang="csharp">@keyframes rotation &#123;
  <span class="hljs-number">0</span>% &#123; transform: rotate(<span class="hljs-number">0</span>deg) &#125;
  <span class="hljs-number">100</span>% &#123; transform: rotate(<span class="hljs-number">360</span>deg) &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca3a61a0a6f84e5885d4479518a1418a~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">步骤9</h3>
<p>修改span::after的动画时间为1s，且反向动画</p>
<pre><code class="hljs language-csharp copyable" lang="csharp">animation: rotation <span class="hljs-number">1</span>s linear infinite reverse;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cf7697a7b914dda996984cf01388b24~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-14">结语</h1>
<p>文章仅作为学习笔记，记录从0到1的一个过程。希望对您有所帮助，如有错误欢迎小伙伴指正～</p>
<p>我是海轰ଘ(੭ˊᵕˋ)੭，如果您觉得写得可以的话，请点个赞吧</p>
<p>写作不易，<strong>「点赞」</strong>+<strong>「收藏」</strong>+<strong>「转发」</strong></p>
<p>谢谢支持❤️</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4801bbd8bfc148f384fe764d74d6487a~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            