
---
title: 'elementUI组件样式引入源码阅读笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2221'
author: 掘金
comments: false
date: Thu, 27 May 2021 02:58:38 GMT
thumbnail: 'https://picsum.photos/400/300?random=2221'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>主要是在阅读elementUI组件源码时，对其样式的统一封装学习笔记。从中可以学习了解到scss在一个大型项目如何应用以及封装。</p>
<h1 data-id="heading-1">目录结构</h1>
<p>element的样式存放在element的<strong>packages/theme-chalk</strong>中,目录结构如下所示:</p>
<pre><code class="copyable">│  alert.scss //组件样式
│  aside.scss
│  autocomplete.scss
│  avatar.scss
│  backtop.scss
│  badge.scss
│  base.scss
│  breadcrumb-item.scss
│  breadcrumb.scss
│  button-group.scss
│  button.scss
|  // 省略部分组件样式
├─common // 组件共用样式
│      popup.scss //弹层类组件共用样式
│      transition.scss //主要定义了element组件中使用vue的 transition 组件时用到的动态效果样式
│      var.scss // 定义了element各组件UI的基本样式的变量,包括颜色,文本大小,边框大小,组件不同尺寸对应的不同样式
│      
├─date-picker // date组件使用样式
│      date-picker.scss
│      date-range-picker.scss
│      date-table.scss
│      month-table.scss
│      picker-panel.scss
│      picker.scss
│      time-picker.scss
│      time-range-picker.scss
│      time-spinner.scss
│      year-table.scss
│      
├─fonts // 字体文件
│      element-icons.ttf
│      element-icons.woff
│      
└─mixins // scss复用函数
       config.scss // 样式名的全局配置
       function.scss // 组件样式使用到的sccss函数
       mixins.scss // 共用的mixins函数
       utils.scss // 工具类函数样式, 如禁用用户选择
       _button.scss // 按钮基本样式
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">主要文件分析</h1>
<h2 data-id="heading-3">config.scss</h2>
<p><strong>config.scss</strong> 文件定义了element样式的全局配置,如样式名前缀,,样式名分割符等</p>
<pre><code class="hljs language-css copyable" lang="css">// 这四个样式名配置是element所有样式名定义的基础
// 如: el-button, el-select, is-disabled等样式名
$namespace: <span class="hljs-string">'el'</span>;
$element-separator: <span class="hljs-string">'__'</span>;
$modifier-separator: <span class="hljs-string">'--'</span>;
$state-prefix: <span class="hljs-string">'is-'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">mixins.scss</h2>
<p><strong>mixins.scss</strong> 文件定义了element各组件样式使用的基本mixins,这里对最主要的mixinx做分析</p>
<ol>
<li><a href="https://juejin.cn/post/6966922638660730916#">@mixin</a> b() 混入el</li>
</ol>
<pre><code class="copyable">@mixin b($block) &#123;
// 假如 $block为button
  $B: $namespace+'-'+$block !global;  $namespace在config.scss中定义为el,故$B为el-blutton
  .#&#123;$B&#125; &#123;    // .#&#123;&#125; 为scss变量插值,编译后为.el-button
    @content;
  &#125;
&#125;
// @content`用在mixin里面的，当定义一个mixin后，并且设置了@content
// @include的时候可以传入相应的内容到mixin里面
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><a href="https://juejin.cn/post/6966922638660730916#">@mixin</a> e() 混入__</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@mixin</span> e($element) &#123;
  <span class="hljs-comment">/**假设$element为disabled **/</span>
  $E: $element !global;
  $selector: &;  // 父选择器
  $currentSelector: <span class="hljs-string">""</span>; // 要生成的选择器
  <span class="hljs-comment">/** 遍历$element //可能有多个
  /* $B 为 mixin b()混入中的变量名
  /* 这里使用$B是因为在element组件样式中e的混入必定是在b混入下的
  /* 如果是在el-button下使用e混入,则生成 .el-button__disabked
  **/</span>
  <span class="hljs-keyword">@each</span> $unit in $element &#123;
    $currentSelector: #&#123;$currentSelector + <span class="hljs-string">"."</span> + $B + $element-separator + $unit + <span class="hljs-string">","</span>&#125;;
  &#125;
  <span class="hljs-comment">/** hitAllSpecialNestRule 判断$elector是否包含--, is-, 在function.scc 中定义
  /* 这里判断是否包含is--,--是因为使用了 @at-root
  /* @at-root指令可以使一个或多个规则被限定输出在文档的根层级上，而不是被嵌套在其父选择器下
  /* 包含有is--等前缀的样式名,在组件中一般是可移除的,所以在输出在文档的根层级上时要加上父选择器
  **/</span>
  <span class="hljs-keyword">@if</span> hitAllSpecialNestRule($selector) &#123;
    <span class="hljs-keyword">@at-root</span> &#123;
      #&#123;$selector&#125; &#123;
        #&#123;$currentSelector&#125; &#123;
          <span class="hljs-keyword">@content</span>;
        &#125;
      &#125;
    &#125;
  &#125; <span class="hljs-keyword">@else</span> &#123;
    <span class="hljs-keyword">@at-root</span> &#123;
      #&#123;$currentSelector&#125; &#123;
        <span class="hljs-keyword">@content</span>;
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li><a href="https://juejin.cn/post/6966922638660730916#">@mixin</a> m() 混入--</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/** 
/* 该方法与混入e基本相同,不同的是没有判断hitAllSpecialNestRule
/* 因为混入 -- 一般的是组件的尺寸样式,如 el-radio--medium,el-radio--small等,父选择器一般为el-radio等,
/* 故不需要判断
**/</span>
<span class="hljs-keyword">@mixin</span> m($modifier) &#123;
  $selector: &;
  $currentSelector: <span class="hljs-string">""</span>;
  <span class="hljs-keyword">@each</span> $unit in $modifier &#123;
    $currentSelector: #&#123;$currentSelector + & + $modifier-separator + $unit + <span class="hljs-string">","</span>&#125;;
  &#125;

  <span class="hljs-keyword">@at-root</span> &#123;
    #&#123;$currentSelector&#125; &#123;
      <span class="hljs-keyword">@content</span>;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li><a href="https://juejin.cn/post/6966922638660730916#">@mixin</a> w() 混入 is</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/** 假设$state为check
/* 则编译后为在文档的根层级(在组件中使用时,为组件根样式)为.el-radio.is-checked
**/</span>
<span class="hljs-keyword">@mixin</span> when($state) &#123;
  <span class="hljs-keyword">@at-root</span> &#123;
    &.#&#123;$state-prefix + $state&#125; &#123;
      <span class="hljs-keyword">@content</span>;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">functon.scss</h2>
<p><strong>function.scss</strong> 主要是定义了 <strong>hitAllSpecialNestRule</strong> 函数方法，主要用来判断选择器是否含有'is-', '--', ':' 等字符。主要代码如下:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@import</span> <span class="hljs-string">"config"</span>;

<span class="hljs-comment">/* BEM support Func
 -------------------------- */</span>
<span class="hljs-keyword">@function</span> selectorToString($selector) &#123;
  //字符化
  $selector: <span class="hljs-built_in">inspect</span>($selector);
  <span class="hljs-comment">/** str-slice 
  /* 从 $string 中截取子字符串，通过 $start-at 和 $end-at 
  /* 设置始末位置，未指定结束索引值则默认截取到字符串末尾。
  /* 这里主要是去除第一个字符和最后一个字符,避免如 --el, el：等的干扰
  **/</span>
  $selector: <span class="hljs-built_in">str-slice</span>($selector, <span class="hljs-number">2</span>, -<span class="hljs-number">2</span>);
  <span class="hljs-keyword">@return</span> $selector;
&#125;

<span class="hljs-keyword">@function</span> containsModifier($selector) &#123;
  $selector: <span class="hljs-built_in">selectorToString</span>($selector);
    <span class="hljs-comment">/** str-index($string, $substring)
    /* 返回一个下标，标示 $substring 在 $string 中的起始位置。没有找到的话，则返回 null 值。
    /* $modifier-specarator --
  **/</span>
  <span class="hljs-keyword">@if</span> str-index($selector, $modifier-separator) &#123;
    <span class="hljs-keyword">@return</span> true;
  &#125; <span class="hljs-keyword">@else</span> &#123;
    <span class="hljs-keyword">@return</span> false;
  &#125;
&#125;

<span class="hljs-keyword">@function</span> containWhenFlag($selector) &#123;
  $selector: <span class="hljs-built_in">selectorToString</span>($selector);
<span class="hljs-comment">/** $state-prefix: 'is-'; **/</span>
  <span class="hljs-keyword">@if</span> str-index($selector, <span class="hljs-string">'.'</span> + $state-prefix) &#123;
    <span class="hljs-keyword">@return</span> true
  &#125; @else &#123;
    <span class="hljs-keyword">@return</span> false
  &#125;
&#125;

@function containPseudoClass($selector) &#123;
  $selector: <span class="hljs-built_in">selectorToString</span>($selector);

  <span class="hljs-keyword">@if</span> str-index($selector, <span class="hljs-string">':'</span>) &#123;
    <span class="hljs-keyword">@return</span> true
  &#125; @else &#123;
    <span class="hljs-keyword">@return</span> false
  &#125;
&#125;
//** 对上述四种情况进行判断，有一种存在就返回true **/
@function hitAllSpecialNestRule($selector) &#123;

  <span class="hljs-keyword">@return</span> containsModifier($selector) <span class="hljs-keyword">or</span> containWhenFlag($selector) <span class="hljs-keyword">or</span> containPseudoClass($selector);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            