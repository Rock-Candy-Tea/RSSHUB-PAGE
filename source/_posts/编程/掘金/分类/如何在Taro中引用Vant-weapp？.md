
---
title: '如何在Taro中引用Vant-weapp？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61557db02d7444dfbeea018cfe9653dc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 16 Apr 2021 18:33:23 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61557db02d7444dfbeea018cfe9653dc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>作为一款小程序多端框架，Taro目前已支持React、Vue语法，这一特性使得Taro在小程序框架领域的占有率越来越高，但想要在这套框架中使用VantUI(weapp)却是十分麻烦：</p>
</blockquote>
<p>一：克隆vant-weapp源码到本地</p>
<pre><code class="hljs language-bash copyable" lang="bash">git <span class="hljs-built_in">clone</span> https://github.com/youzan/vant-weapp.git
<span class="copy-code-btn">复制代码</span></code></pre>
<p>二、将其中的dist文件夹整个拷入taro项目中</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61557db02d7444dfbeea018cfe9653dc~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>建议目录结构 src>components>vant-weapp-dist</p>
</blockquote>
<p>三、配置全局打包映射</p>
<p>在项目的config>index.js文件中更改如下代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//需要改动的地方在于config.copy.patterns</span>
<span class="hljs-comment">//原因是Taro在打包的并没有对Vant依赖进行分析，只能手动将依赖文件拷贝到打包后的目录中，copy配置项所起到的也就是这个作用。</span>

<span class="hljs-keyword">const</span> config = &#123;
  ...
  <span class="hljs-attr">copy</span>: &#123;
    <span class="hljs-attr">patterns</span>: [
      <span class="hljs-comment">/**此处为公共组件，必需--start */</span>
      &#123;
        <span class="hljs-attr">from</span>: <span class="hljs-string">'src/components/vant-weapp/dist/wxs'</span>,
        <span class="hljs-attr">to</span>: <span class="hljs-string">'dist/components/vant-weapp/dist/wxs'</span>,
      &#125;,
      &#123;
        <span class="hljs-attr">from</span>: <span class="hljs-string">'src/components/vant-weapp/dist/common/style'</span>,
        <span class="hljs-attr">to</span>: <span class="hljs-string">'dist/components/vant-weapp/dist/common/style'</span>,
      &#125;,
      &#123;
        <span class="hljs-attr">from</span>: <span class="hljs-string">'src/components/vant-weapp/dist/common/index.wxss'</span>,
        <span class="hljs-attr">to</span>: <span class="hljs-string">'dist/components/vant-weapp/dist/common/index.wxss'</span>,
      &#125;,
      <span class="hljs-comment">/**此处为公共组件，必需--end */</span>
      <span class="hljs-comment">/**此处为按需组件，可选--start */</span>
      &#123;
        <span class="hljs-attr">from</span>: <span class="hljs-string">'src/components/vant-weapp/dist/icon/index.wxml'</span>,
        <span class="hljs-attr">to</span>: <span class="hljs-string">'dist/components/vant-weapp/dist/button/index.wxml'</span>,
      &#125;,
      &#123;
        <span class="hljs-attr">from</span>: <span class="hljs-string">'src/components/vant-weapp/dist/button/index.wxs'</span>,
        <span class="hljs-attr">to</span>: <span class="hljs-string">'dist/components/vant-weapp/dist/button/index.wxs'</span>,
      &#125;,
      &#123;
        <span class="hljs-attr">from</span>: <span class="hljs-string">'src/components/vant-weapp/dist/button/index.wxss'</span>,
        <span class="hljs-attr">to</span>: <span class="hljs-string">'dist/components/vant-weapp/dist/button/index.wxss'</span>,
      &#125;
      <span class="hljs-comment">/**此处为按需组件，可选--end */</span>
    ],
    <span class="hljs-attr">options</span>: &#123;&#125;,
  &#125;,
  ...
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>分析如上代码不难发现，代码重复率很高，所以我们对此其做进一步精简</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@description</span>: 根据vant组件名，生成相应的映射地址
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>componentName：组件名
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;*&#125;</span> </span>组件映射地址
 */</span>
<span class="hljs-keyword">const</span> createVantPatterns = <span class="hljs-function">(<span class="hljs-params">componentName</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> fileTypes = [<span class="hljs-string">'wxml'</span>, <span class="hljs-string">'wxs'</span>, <span class="hljs-string">'wxss'</span>];
  <span class="hljs-keyword">return</span> fileTypes.map(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">from</span>: <span class="hljs-string">`src/components/vant-weapp/dist/<span class="hljs-subst">$&#123;componentName&#125;</span>/index.<span class="hljs-subst">$&#123;item&#125;</span>`</span>,
      <span class="hljs-attr">to</span>: <span class="hljs-string">`dist/components/vant-weapp/dist/<span class="hljs-subst">$&#123;componentName&#125;</span>/index.<span class="hljs-subst">$&#123;item&#125;</span>`</span>,
    &#125;;
  &#125;);
&#125;;
<span class="hljs-keyword">const</span> config = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">copy</span>: &#123;
    <span class="hljs-attr">patterns</span>: [
      &#123;
        <span class="hljs-attr">from</span>: <span class="hljs-string">'src/components/vant-weapp/dist/wxs'</span>,
        <span class="hljs-attr">to</span>: <span class="hljs-string">'dist/components/vant-weapp/dist/wxs'</span>,
      &#125;,
      &#123;
        <span class="hljs-attr">from</span>: <span class="hljs-string">'src/components/vant-weapp/dist/common/style'</span>,
        <span class="hljs-attr">to</span>: <span class="hljs-string">'dist/components/vant-weapp/dist/common/style'</span>,
      &#125;,
      &#123;
        <span class="hljs-attr">from</span>: <span class="hljs-string">'src/components/vant-weapp/dist/common/index.wxss'</span>,
        <span class="hljs-attr">to</span>: <span class="hljs-string">'dist/components/vant-weapp/dist/common/index.wxss'</span>,
      &#125;,
      ...createVantPatterns(<span class="hljs-string">'icon'</span>),
    ],
    <span class="hljs-attr">options</span>: &#123;&#125;,
  &#125;,
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>部分组件可能会涉及到不止一个组件依赖，需要对应的全部引入。（比如想要带有图标和加载动画的Button，除引入button之外，还需引入icon和loading才行。</p>
</blockquote>
<p>四、配置全局样式转换</p>
<p>在项目的config>index.js文件中更改如下代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//需要改动的地方在于config.mini.postcss.pxtransform.config</span>
<span class="hljs-comment">//Taro会默认将px转换为rpx,直接使用vant组件样式会有偏小的情况，故此处做禁止转换处理。</span>

<span class="hljs-keyword">const</span> config = &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">mini</span>: &#123;
    <span class="hljs-attr">postcss</span>: &#123;
      <span class="hljs-attr">pxtransform</span>: &#123;
        <span class="hljs-attr">enable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">config</span>: &#123;
          <span class="hljs-attr">selectorBlackList</span>: [<span class="hljs-regexp">/van-/</span>],
        &#125;,
      &#125;,
    &#125;,
  &#125;,
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>四、引用Vant组件</p>
<p>在页面的pages>index>index.config.js文件中更改如下代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//需要改动的地方在于usingComponents</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">navigationBarTitleText</span>: <span class="hljs-string">'首页'</span>,
  <span class="hljs-attr">usingComponents</span>: &#123;
    <span class="hljs-string">'van-icon'</span>: <span class="hljs-string">'../../components/vant-weapp/dist/icon/index'</span>,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>五、使用Vant组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//vue</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"index"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">text</span>></span>&#123;&#123; msg &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">van-icon</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"chat"</span> <span class="hljs-attr">color</span>=<span class="hljs-string">"red"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">view</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> <span class="hljs-string">'./index.less'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">msg</span>: <span class="hljs-string">'Hello world!23'</span>,
    &#125;;
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//react</span>
<span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; View &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@tarojs/components'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Index</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  render () &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">van-button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">'primary'</span> <span class="hljs-attr">loading</span> <span class="hljs-attr">loading-text</span>=<span class="hljs-string">'ing'</span>></span>Button<span class="hljs-tag"></<span class="hljs-name">van-button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参考地址：
（1）<a href="https://taro-docs.jd.com/taro/docs/vant" target="_blank" rel="nofollow noopener noreferrer">Taro官方文档</a>
（2）<a href="https://vant-contrib.gitee.io/vant-weapp/#/home" target="_blank" rel="nofollow noopener noreferrer">Vant-weapp官方文档</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            