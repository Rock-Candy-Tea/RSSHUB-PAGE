
---
title: '使用css变量和sass实现一键主题换肤功能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9050'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 22:33:50 GMT
thumbnail: 'https://picsum.photos/400/300?random=9050'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">需求</h2>
<p>最近做的公共模块，需要提供给不同平台，可以通过传参实现主题色的适配，目前支持<strong>模板一键换肤以及自定义换肤</strong>。</p>
<h2 data-id="heading-1">实现方案</h2>
<p>换肤方案主要是基于<strong>CSS自定义变量以及sass动态修改data-theme</strong>实现的。</p>
<h2 data-id="heading-2">模板换肤</h2>
<p>首先提供几套主题色模板，统一放在theme文件夹当中。</p>
<p>blue.scss (默认主题)</p>
<pre><code class="hljs language-css copyable" lang="css">$blue: (
    // 字体
    font_color: <span class="hljs-number">#00a5e5</span>,
    // 按钮背景
    background_color: <span class="hljs-number">#00a5e5</span>,
    // 鼠标划过
    background_hover_color: <span class="hljs-number">#0094CE</span>,
    // 禁用
    background_disable_color:<span class="hljs-number">#CCEDFA</span>,
    // 边框颜色
    border_color: <span class="hljs-number">#00a5e5</span>,
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>your.scss (你的主题)</p>
<pre><code class="hljs language-css copyable" lang="css">$ucode-website: (
    // 字体
    font_color: <span class="hljs-number">#7284fb</span>,
    // 按钮背景
    background_color: <span class="hljs-number">#7284fb</span>,
    // 鼠标划过
    background_hover_color: <span class="hljs-number">#6676E1</span>,
    // 禁用
    background_disable_color: <span class="hljs-number">#E6EAFF</span>,
    // 边框颜色
    border_color: <span class="hljs-number">#7284fb</span>,
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>adapt-theme.scss (主题适配器)</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@import</span> <span class="hljs-string">'./theme.scss'</span>;
<span class="hljs-keyword">@import</span> <span class="hljs-string">'./themes/default.scss'</span>;

// 遍历主题
<span class="hljs-keyword">@mixin</span> themeify &#123;
  <span class="hljs-keyword">@each</span> $theme-name, $theme-map in $themes &#123;
    // !global 把局部变量强升为全局变量
    $theme-map: $theme-map !global;
    <span class="hljs-selector-attr">[data-theme=<span class="hljs-string">"#&#123;$theme-name&#125;"</span>]</span> & &#123;
        <span class="hljs-keyword">@content</span>;
    &#125;
  &#125;
&#125;

// 根据Key值获取颜色
<span class="hljs-keyword">@function</span> themed($key) &#123;
    <span class="hljs-keyword">@return</span> map-get($theme-map, $key);
&#125;

// 获取字体颜色
<span class="hljs-keyword">@mixin</span> font_<span class="hljs-attribute">color</span>($<span class="hljs-attribute">color</span>) &#123;
    <span class="hljs-keyword">@include</span> themeify&#123;
        <span class="hljs-attribute">color</span>: <span class="hljs-built_in">themed</span>($color);
    &#125;
&#125;

// 获取边框颜色
<span class="hljs-keyword">@mixin</span> border_<span class="hljs-attribute">color</span>($<span class="hljs-attribute">color</span>) &#123;
    <span class="hljs-keyword">@include</span> themeify&#123;
        <span class="hljs-attribute">border-color</span>: <span class="hljs-built_in">themed</span>($color);
    &#125;
&#125;

// 获取背景颜色
<span class="hljs-keyword">@mixin</span> background_<span class="hljs-attribute">color</span>($<span class="hljs-attribute">color</span>) &#123;
    <span class="hljs-keyword">@include</span> themeify&#123;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">themed</span>($color);
    &#125;
&#125;

// 鼠标划过
<span class="hljs-keyword">@mixin</span> background_<span class="hljs-attribute">hover</span>_<span class="hljs-attribute">color</span>($<span class="hljs-attribute">color</span>) &#123;
    <span class="hljs-keyword">@include</span> themeify&#123;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">themed</span>($color);
    &#125;
&#125;

// 禁用
<span class="hljs-keyword">@mixin</span> background_disable_<span class="hljs-attribute">color</span>($<span class="hljs-attribute">color</span>) &#123;
    <span class="hljs-keyword">@include</span> themeify&#123;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">themed</span>($color);
    &#125;
&#125;



<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">调用主题模板</h2>
<p>第三方调用时传主题参数到公共模块，写入顶层元素的data-theme即可自动适配模板。</p>
<pre><code class="hljs language-css copyable" lang="css"><<span class="hljs-selector-tag">div</span> data-theme=&#123;this<span class="hljs-selector-class">.context</span><span class="hljs-selector-class">.theme</span>&#125;></<span class="hljs-selector-tag">div</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>适配公共组件</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@import</span> <span class="hljs-string">"../../../styles/adapt-theme.scss"</span>;
<span class="hljs-selector-tag">button</span> &#123;
    <span class="hljs-keyword">@include</span> background_<span class="hljs-attribute">color</span>(<span class="hljs-string">"background_color"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">自定义颜色换肤</h2>
<p>定义初始CSS变量，挂载在根元素，可以全局使用。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-pseudo">:root</span> &#123;
    --fontColor: initial; // 此处注意，<span class="hljs-attribute">initial</span>才为空值
    --backgroundColor: initial;
    --backgroundHoverColor: initial;
    --backgroundDisableColor: initial;
    --borderColor: initial;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第三方调用传参后，JS动态修改CSS变量。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> body = <span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">'body'</span>)[<span class="hljs-number">0</span>];
<span class="hljs-keyword">const</span> &#123; themeStyles &#125; = <span class="hljs-built_in">this</span>.context;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> style <span class="hljs-keyword">in</span> themeStyles) &#123;
     <span class="hljs-keyword">if</span> (themeStyles[style]) &#123;
          body.style.setProperty(<span class="hljs-string">`--<span class="hljs-subst">$&#123;style&#125;</span>`</span>, themeStyles[style]);
     &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后修改主题适配器，<strong>利用CSS无效变量，可以实现自定义变量覆盖模板，当没有自定义变量时，又不会影响模板渲染。这个是关键。</strong></p>
<pre><code class="hljs language-css copyable" lang="css">// 获取字体颜色
<span class="hljs-keyword">@mixin</span> font_<span class="hljs-attribute">color</span>($<span class="hljs-attribute">color</span>) &#123;
    <span class="hljs-keyword">@include</span> themeify&#123;
        <span class="hljs-attribute">color</span>: <span class="hljs-built_in">var</span>(--fontColor, <span class="hljs-built_in">themed</span>($color));
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            