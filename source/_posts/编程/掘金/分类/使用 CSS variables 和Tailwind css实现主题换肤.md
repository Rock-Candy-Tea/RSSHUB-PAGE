
---
title: '使用 CSS variables 和Tailwind css实现主题换肤'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d9bd56a311b471da9ef9ecd441603d7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 00:33:00 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d9bd56a311b471da9ef9ecd441603d7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>在2B的项目中，常常有客户（甲方爸爸）需求，定制与他们企业相同的主题的网站；随着苹果暗黑模式的推出，换肤的需求在网站开发中越来越多，也越来越重要，最近在网上看到 Tailwind Labs的实现的<a href="https://www.youtube.com/watch?v=MAtaT8BZEAo" target="_blank" rel="nofollow noopener noreferrer">换肤视频</a>，决定实践一把。</p>
<h2 data-id="heading-1">实现博客列表</h2>
<p>我们先使用Tailwind css 实现一个博客列表</p>
<ul>
<li>效果</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d9bd56a311b471da9ef9ecd441603d7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>html 代码</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"min-h-screen bg-white"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"p-10 space-y-10"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"text-gray-600"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">article</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"relative flex items-center transition-transform transform group hover:-translate-x-2"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"flex flex-col flex-grow py-8 space-y-4 text-base rounded px-8 shadow-md bg-gray-50"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"flex flex-row justify-between"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">h3</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"text-xl text-gray-900 font-bold"</span>></span>useEffect 完整指南<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">span</span>></span>2020-06-08<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"leading-8"</span>></span>你用Hooks写了一些组件，甚或写了一个小型应用。你可能很满意，使用它的API很舒服并且在这个过程中获得了一些小技巧。<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">article</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"text-gray-600"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">article</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"relative flex items-center transition-transform transform group hover:-translate-x-2"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"flex flex-col flex-grow py-8 space-y-4 text-base rounded px-8 shadow-md bg-gray-50"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"flex flex-row justify-between"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">h3</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"text-xl text-gray-900 font-bold"</span>></span>使用 CSS variables 和Tailwind csss实现主题换肤<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">span</span>></span>2020-06-08<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"leading-8"</span>></span>根据Tailwind Labs的[换肤视频]，手动实践。<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">article</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>


<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">CSS variables</h2>
<p>使用CSS variables 是实现换肤最方便的方案，按传统的方案就得加入一些css class 就可以实现，如：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-pseudo">:root</span> &#123;
    --page-bg:<span class="hljs-number">#fff</span>;
    --card-bg:<span class="hljs-number">#F9FAFB</span>; <span class="hljs-comment">/* gray-50 */</span>
    --title-<span class="hljs-attribute">color</span>:<span class="hljs-number">#111827</span>;<span class="hljs-comment">/* gray-900 */</span>
    --desc-<span class="hljs-attribute">color</span>:<span class="hljs-number">#4B5563</span>; <span class="hljs-comment">/* gray-600 */</span>
  &#125;

  <span class="hljs-selector-class">.theme-dark</span> &#123;
    --page-bg:<span class="hljs-number">#111827</span>; <span class="hljs-comment">/* gray-900 */</span>
    --card-bg:<span class="hljs-number">#1F2937</span>; <span class="hljs-comment">/* gray-800 */</span>
    --title-<span class="hljs-attribute">color</span>:<span class="hljs-number">#F3F4F6</span>;<span class="hljs-comment">/* gray-100 */</span>
    --desc-<span class="hljs-attribute">color</span>:<span class="hljs-number">#E5E7EB</span>; <span class="hljs-comment">/* gray-200 */</span>
  &#125;
<span class="hljs-selector-class">.page__bg</span>&#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">var</span>(--page-bg);
&#125;
<span class="hljs-selector-class">.post__card</span>&#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">var</span>(--card-bg);
&#125;
<span class="hljs-selector-class">.post__title</span>&#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-built_in">var</span>(--title-color);
&#125;
<span class="hljs-selector-class">.post__desc</span>&#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-built_in">var</span>(--desc-color) ;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa9dd771eb61470a88d345dd084a8c20~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样就可以实现深色皮肤了，如果想增加一套皮肤，只需增加一套颜色变量就可以了。</p>
<h2 data-id="heading-3">兼容性</h2>
<p>CSS variables 只支持现代浏览器，但是许多客户还在使用IE11，为了兼容IE11 可以使用 postcss  插件<a href="https://github.com/postcss/postcss-custom-properties" target="_blank" rel="nofollow noopener noreferrer">postcss-custom-properties</a></p>
<p>例如下面css：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-pseudo">:root</span> &#123;
  --<span class="hljs-attribute">color</span>: red;
&#125;
<span class="hljs-selector-tag">h1</span> &#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-built_in">var</span>(--color);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过postcss 的处理，得到下面的css，不支持的css属性， 浏览器会自动忽略。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">h1</span> &#123;
  <span class="hljs-attribute">color</span>: red;
  <span class="hljs-attribute">color</span>: <span class="hljs-built_in">var</span>(--color);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这个插件只对第一次编译的时候有用，动态换肤的时候就失效了，
我们可以使用js polyfill 来修复这个问题,在HTML中引入下面代码就可以解决。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript"><span class="hljs-built_in">window</span>.MSInputMethodContext && <span class="hljs-built_in">document</span>.documentMode && <span class="hljs-built_in">document</span>.write(<span class="hljs-string">'<script src="https://cdn.jsdelivr.net/gh/nuxodin/ie11CustomProperties@4.1.0/ie11CustomProperties.min.js"><\/script>'</span>);</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>😅但是这样写完全体现不出Tailwind css 的优势，Tailwind 的思想是Utility-First，写页面的时候不需要取繁琐的class名称了。</p>
<h2 data-id="heading-4">Tailwind 配置</h2>
<p>tailwind css 可以让用户在<code>tailwind.config.js</code>中配置一些自定义颜色，这样css 中就增加了与之对应颜色的class。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> colors = <span class="hljs-built_in">require</span>(<span class="hljs-string">'tailwindcss/colors'</span>)

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'jit'</span>,
  <span class="hljs-attr">theme</span>: &#123;
    <span class="hljs-attr">extend</span>: &#123;
      <span class="hljs-attr">colors</span>: &#123;
        <span class="hljs-attr">amber</span>: colors.amber,
        <span class="hljs-attr">lime</span>: colors.lime,
        <span class="hljs-attr">rose</span>: colors.rose,
        <span class="hljs-attr">orange</span>: colors.orange,
      &#125;,
    &#125;,
    <span class="hljs-attr">backgroundColor</span>: &#123;
      <span class="hljs-comment">//utilities like `bg-base` and `bg-primary`</span>
      <span class="hljs-attr">base</span>: <span class="hljs-string">'var(--color-base)'</span>,
      <span class="hljs-string">'off-base'</span>: <span class="hljs-string">'var(--color-off-base)'</span>,
      <span class="hljs-attr">primary</span>: <span class="hljs-string">'var(--color-primary)'</span>,
      <span class="hljs-attr">secondary</span>: <span class="hljs-string">'var(--color-secondary)'</span>,
      <span class="hljs-attr">muted</span>: <span class="hljs-string">'var(--color-text-muted)'</span>,
    &#125;,
    <span class="hljs-attr">textColor</span>: &#123;
      <span class="hljs-comment">//like `text-base` and `text-primary`</span>
      <span class="hljs-attr">base</span>: <span class="hljs-string">'var(--color-text-base)'</span>,
      <span class="hljs-attr">muted</span>: <span class="hljs-string">'var(--color-text-muted)'</span>,
      <span class="hljs-string">'muted-hover'</span>: <span class="hljs-string">'var(--color-text-muted-hover)'</span>,
      <span class="hljs-attr">primary</span>: <span class="hljs-string">'var(--color-primary)'</span>,
      <span class="hljs-attr">secondary</span>: <span class="hljs-string">'var(--color-secondary)'</span>,
    &#125;,
  &#125;,
  <span class="hljs-attr">variants</span>: &#123;&#125;,
  <span class="hljs-attr">plugins</span>: [],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里为了方便使用和记忆，我用来几个简单的变量名称来定义，背景和字体颜色，当然还有扩展其他样式如<code>borderColor</code></p>
<p>然后在css 中定义变量 theme 方法可以获取tailwind 内置的颜色，想要使用颜色比配置在colors 中。跟多颜色可以访问<a href="https://tailwindcss.com/docs/customizing-colors" target="_blank" rel="nofollow noopener noreferrer">customizing-colors</a>,当然</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@tailwind</span> base;
<span class="hljs-keyword">@tailwind</span> components;
<span class="hljs-keyword">@tailwind</span> utilities;


<span class="hljs-keyword">@layer</span> base &#123;
  <span class="hljs-selector-class">.theme-light</span> &#123;
    --<span class="hljs-attribute">color</span>-base: <span class="hljs-built_in">theme</span>(<span class="hljs-string">'colors.white'</span>); 
    --<span class="hljs-attribute">color</span>-text-base: <span class="hljs-built_in">theme</span>(<span class="hljs-string">'colors.black'</span>); 
    --<span class="hljs-attribute">color</span>-off-base: <span class="hljs-built_in">theme</span>(<span class="hljs-string">'colors.gray.50'</span>);
    --<span class="hljs-attribute">color</span>-text-muted: <span class="hljs-built_in">theme</span>(<span class="hljs-string">'colors.gray.600'</span>);
    --<span class="hljs-attribute">color</span>-text-muted-hover: <span class="hljs-built_in">theme</span>(<span class="hljs-string">'colors.gray.500'</span>); 
    --<span class="hljs-attribute">color</span>-primary: <span class="hljs-built_in">theme</span>(<span class="hljs-string">'colors.blue.600'</span>); 
    --<span class="hljs-attribute">color</span>-secondary:<span class="hljs-built_in">theme</span>(<span class="hljs-string">'colors.blue.300'</span>); 
  &#125;

  <span class="hljs-selector-class">.theme-dark</span> &#123;
    --<span class="hljs-attribute">color</span>-base: <span class="hljs-built_in">theme</span>(<span class="hljs-string">'colors.gray.900'</span>);
    --<span class="hljs-attribute">color</span>-text-base: <span class="hljs-built_in">theme</span>(<span class="hljs-string">'colors.gray.100'</span>); 
    --<span class="hljs-attribute">color</span>-off-base: <span class="hljs-built_in">theme</span>(<span class="hljs-string">'colors.gray.800'</span>); 
    --<span class="hljs-attribute">color</span>-text-muted:<span class="hljs-built_in">theme</span>(<span class="hljs-string">'colors.gray.300'</span>); 
    --<span class="hljs-attribute">color</span>-text-muted-hover: <span class="hljs-built_in">theme</span>(<span class="hljs-string">'colors.gray.200'</span>);
    --<span class="hljs-attribute">color</span>-primary: <span class="hljs-built_in">theme</span>(<span class="hljs-string">'colors.blue.500'</span>); 
    --<span class="hljs-attribute">color</span>-secondary: <span class="hljs-built_in">theme</span>(<span class="hljs-string">'colors.blue.200'</span>); 
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>tailwind 中有个样式是<code>text-opacity-10</code> 设置了字体颜色，还可以设置透明度，查看源码发现样式是通过rgba 实现的.</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.text-gray-900</span> &#123;
    --tw-text-<span class="hljs-attribute">opacity</span>: <span class="hljs-number">1</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">17</span>,<span class="hljs-number">24</span>,<span class="hljs-number">39</span>,<span class="hljs-built_in">var</span>(--tw-text-opacity));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如想要支持这个透明度的样式，我们还需要将颜色转成Rgb,<code>tailwind.config.js</code> 配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">withOpacity</span>(<span class="hljs-params">variableName</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">&#123; opacityValue &#125;</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (opacityValue) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">`rgba(var(<span class="hljs-subst">$&#123;variableName&#125;</span>), <span class="hljs-subst">$&#123;opacityValue&#125;</span>)`</span>;
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-string">`rgb(var(<span class="hljs-subst">$&#123;variableName&#125;</span>))`</span>;
    &#125;;
&#125;

<span class="hljs-built_in">module</span>.exports = &#123;

   ..., 

   <span class="hljs-attr">theme</span>: &#123;
        <span class="hljs-comment">// we want to extend the current colors instead of replacing them</span>
        <span class="hljs-attr">extend</span>: &#123;
         <span class="hljs-comment">//like `bg-base` and `bg-primary`</span>
            <span class="hljs-attr">backgroundColor</span>: &#123;
                <span class="hljs-attr">primary</span>: withOpacity(<span class="hljs-string">'--color-primary'</span>),
                <span class="hljs-attr">secondary</span>: withOpacity(<span class="hljs-string">'--color-secondary'</span>),
                <span class="hljs-attr">muted</span>: withOpacity(<span class="hljs-string">'--color-text-muted'</span>),
            &#125;,
        <span class="hljs-comment">//like `text-base` and `text-primary`</span>
            <span class="hljs-attr">textColor</span>: &#123;
                <span class="hljs-attr">primary</span>: withOpacity(<span class="hljs-string">'--color-primary'</span>),
                <span class="hljs-attr">secondary</span>: withOpacity(<span class="hljs-string">'--color-secondary'</span>),
            &#125;,
      &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>css 中颜色定义</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.theme-dark</span> &#123;
    --<span class="hljs-attribute">color</span>-base: <span class="hljs-number">17</span>, <span class="hljs-number">24</span>, <span class="hljs-number">39</span>;                <span class="hljs-comment">/* gray-900 */</span>
    --<span class="hljs-attribute">color</span>-text-base: <span class="hljs-number">243</span>, <span class="hljs-number">244</span>, <span class="hljs-number">246</span>;        <span class="hljs-comment">/* gray-100 */</span>
    --<span class="hljs-attribute">color</span>-off-base: <span class="hljs-number">31</span>, <span class="hljs-number">41</span>, <span class="hljs-number">55</span>;            <span class="hljs-comment">/* gray-800 */</span>
    --<span class="hljs-attribute">color</span>-text-muted: <span class="hljs-number">229</span>, <span class="hljs-number">231</span>, <span class="hljs-number">235</span>;       <span class="hljs-comment">/* gray-200 */</span>
    --<span class="hljs-attribute">color</span>-muted-offset: <span class="hljs-number">209</span>, <span class="hljs-number">213</span>, <span class="hljs-number">219</span>;     <span class="hljs-comment">/* gray-300 */</span>
    --<span class="hljs-attribute">color</span>-primary: <span class="hljs-number">147</span>, <span class="hljs-number">197</span>, <span class="hljs-number">253</span>;          <span class="hljs-comment">/* blue-300 */</span>
    --<span class="hljs-attribute">color</span>-secondary: <span class="hljs-number">96</span>, <span class="hljs-number">165</span>, <span class="hljs-number">250</span>;         <span class="hljs-comment">/* blue-400 */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">最终效果</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd81446d786448b89a25a17dff92f311~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://play.tailwindcss.com/KDVQG5ULlM" target="_blank" rel="nofollow noopener noreferrer">代码</a></li>
</ul>
<p>顺便提一下<a href="https://play.tailwindcss.com/" target="_blank" rel="nofollow noopener noreferrer">play.tailwindcss.com/</a> 必须点击share 才会保存。😂 我在联系的时候也没保存，吃过一堑。</p>
<h2 data-id="heading-6">参考</h2>
<ul>
<li>
<p><a href="https://www.youtube.com/watch?v=MAtaT8BZEAo" target="_blank" rel="nofollow noopener noreferrer">www.youtube.com/watch?v=MAt…</a></p>
</li>
<li>
<p><a href="https://css-tricks.com/color-theming-with-css-custom-properties-and-tailwind/" target="_blank" rel="nofollow noopener noreferrer">css-tricks.com/color-themi…</a></p>
</li>
<li>
<p><a href="https://dev.to/austincrim/how-i-added-themes-to-my-website-using-tailwind-3ig3" target="_blank" rel="nofollow noopener noreferrer">dev.to/austincrim/…</a></p>
</li>
</ul></div>  
</div>
            