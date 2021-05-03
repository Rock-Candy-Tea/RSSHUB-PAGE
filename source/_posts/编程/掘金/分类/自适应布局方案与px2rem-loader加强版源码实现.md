
---
title: '自适应布局方案与px2rem-loader加强版源码实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e667a201d08745e9896cf97ba360c65a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 02 May 2021 00:54:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e667a201d08745e9896cf97ba360c65a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.核心概念</h2>
<h3 data-id="heading-1">1.1 设备物理像素</h3>
<ul>
<li>是一个物理概念，是显示器显示的最小物理单位，设备屏幕的物理像素，任何设备的物理像素的数量都是固定的</li>
<li>iPhone6的像素分辨率是750*1334</li>
</ul>
<h3 data-id="heading-2">1.2设备独立像素</h3>
<ul>
<li>
<p>是一个逻辑概念,是为web开发者创造的，在CSS和javascript中使用的一个抽象的层，用于向CSS中的宽度、高度等提供信息</p>
</li>
<li>
<p>iPhone6的逻辑分辨率是375*667</p>
</li>
<li>
<p>iPhone6:window.screen.width=375,window.screen.height=667</p>
</li>
<li>
<p>px是一个相对单位，相对的是设备像素(device pixel)</p>
<p>像素，又称画素，是图像显示的基本单位，译自英文“pixel”，pix是英语单词picture的常用简写，加上英语单词“元素”element，就得到pixel，故“像素”表示“图像元素”之意，有时亦被称为pel(picture element)
像素是网页布局的基础。一个像素就是计算机能够显示一种特定颜色的最小区域。当设备尺寸相同但像素变得更密集时，屏幕能显示的画面的过渡更细致，网站看起来更明快。</p>
<p>每一个CSS声明和几乎所有的javascript属性都使用CSS像素，因此实际上从来用不上设备像素 ，唯一的例外是screen.width/height</p>
</li>
</ul>
<h3 data-id="heading-3">1.3 设备像素比</h3>
<ul>
<li>
<p>DPR(设备像素比) = 设备像素/CSS像素</p>
</li>
<li>
<p>设备像素比 window.devicePixelRatio</p>
<p>在早先的移动设备中，并没有DPR的概念。随着技术的发展，移动设备的屏幕像素密度越来越高。从iphone4开始，苹果公司推出了所谓的retina视网膜屏幕。之所以叫做视网膜屏幕，是因为屏幕的PPI(屏幕像素密度)太高，人的视网膜无法分辨出屏幕上的像素点。iphone4的分辨率提高了一倍，但屏幕尺寸却没有变化，这意味着同样大小的屏幕上，像素多了一倍，于是DPR = 2
实际上，此时的CSS像素对应着以后要提到的理想视口，其对应的javascript属性是screen.width/screen.height而对于设备像素比DPR也有对应的javascript属性window.devicePixelRatio
以iphone5为例，iphone5的CSS像素为<code>320px*568px</code>，DPR是2，所以其设备像素为<code>640px*1136px</code></p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e667a201d08745e9896cf97ba360c65a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">1.4 移动端适配</h3>
<ul>
<li>一般由设计师按照设备像素(device pixel)为单位制作设计稿</li>
<li>然后由前端工程师参照设备像素比(device pixel ratio)进行换算</li>
</ul>
<h4 data-id="heading-5">1.4.1 rem</h4>
<ul>
<li>参照根元素的字体大小</li>
<li>适配就是让根元素的字体大小根据分辨率进行动态改变</li>
<li><a href="https://www.npmjs.com/package/px2rem-loader" target="_blank" rel="nofollow noopener noreferrer">px2rem-loader</a></li>
</ul>
<h4 data-id="heading-6">1.4.2 vw和vh</h4>
<ul>
<li>参照的是viewport视口</li>
<li>vw参照的是视口的宽度(1vw=视口宽度/100)</li>
<li>vh参照的是视口的高度(1vh=视口高度/100)</li>
<li>iPhone6 1vw=3.75px</li>
<li><a href="https://www.npmjs.com/package/postcss-px-to-viewport" target="_blank" rel="nofollow noopener noreferrer">postcss-px-to-viewport</a></li>
</ul>
<h2 data-id="heading-7">2.px2rem-loader实战</h2>
<h3 data-id="heading-8">2.1 安装</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install webpack webpack-cli html-webpack-plugin style-loader css-loader amfe-flexible px2rem-loader --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">2.2 src\index.js</h3>
<pre><code class="hljs language-javvascript copyable" lang="javvascript">import './base.css'
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">2.3 src\base.css</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"> width:750px;
  height:750px;
  background-color: red;
  font-size:12px;<span class="hljs-comment">/*px*/</span>
  border: 1px solid #ddd; <span class="hljs-comment">/*no*/</span>
  box-shadow: <span class="hljs-number">0</span> 2px <span class="hljs-number">0</span> rgb(<span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> / <span class="hljs-number">5</span>%);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">2.4 src\index.html</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>webpack<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">2.5 webpack.config.js</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">mode</span>:<span class="hljs-string">'development'</span>,
    <span class="hljs-attr">devtool</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
    <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'dist'</span>),
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].js'</span>,
    &#125;,
    <span class="hljs-attr">resolveLoader</span>: &#123;
        <span class="hljs-attr">alias</span>: &#123;
          <span class="hljs-string">"px2rem-plus-loader"</span>: path.resolve(<span class="hljs-string">'./loaders/px2rem-plus-loader.js'</span>)
        &#125;,
        <span class="hljs-attr">modules</span>: [path.resolve(<span class="hljs-string">'./loaders'</span>), <span class="hljs-string">'node_modules'</span>]
    &#125;,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
          &#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
            use: [&#123;
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'style-loader'</span>
            &#125;, &#123;
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'css-loader'</span>
            &#125;, 
            <span class="hljs-comment">// &#123;</span>
            <span class="hljs-comment">//     loader: 'px2rem-loader',</span>
            <span class="hljs-comment">//     options: &#123;</span>
            <span class="hljs-comment">//         remUni: 75,</span>
            <span class="hljs-comment">//         remPrecision: 8</span>
            <span class="hljs-comment">//     &#125;</span>
            <span class="hljs-comment">// &#125;,</span>
            &#123;
              <span class="hljs-attr">loader</span>: <span class="hljs-string">'px2rem-plus-loader'</span>, <span class="hljs-comment">//path.resolve(__dirname, 'loaders/px2rem-plus-loader.js'),</span>
              <span class="hljs-attr">options</span>: &#123;
                  <span class="hljs-attr">remUnit</span>: <span class="hljs-number">75</span>,
                  <span class="hljs-attr">remPrecision</span>: <span class="hljs-number">8</span>,
                  <span class="hljs-attr">baseDpr</span>:<span class="hljs-number">1</span>,
                  <span class="hljs-attr">exclude</span>:<span class="hljs-regexp">/antd\.css/</span>
              &#125;
            &#125;
            ]
          &#125;,
          &#123;
            <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.js$/</span>,
            use: &#123;
                <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
                <span class="hljs-attr">options</span>: &#123;
                  <span class="hljs-attr">presets</span>: [<span class="hljs-string">'@babel/preset-env'</span>,<span class="hljs-string">'@babel/preset-react'</span>],
                  <span class="hljs-attr">plugins</span>: [<span class="hljs-string">'@babel/transform-runtime'</span>]
                &#125;
              &#125;,
            <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>,        
          &#125;,
        ]
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-keyword">new</span> HtmlWebpackPlugin(
          &#123; <span class="hljs-attr">template</span>: <span class="hljs-string">'./src/index.html'</span>, 
            <span class="hljs-attr">title</span>:<span class="hljs-string">'index'</span>,
            <span class="hljs-attr">inject</span>: <span class="hljs-literal">true</span>
          &#125;
        ),
    ]
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">2.6 package.json</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
   <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"webpack"</span>
   &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">3.loader</h2>
<ul>
<li>loader 用于对模块的源代码进行转换</li>
<li>loader 可以使你在 import 模块时预处理文件</li>
<li>loader 可以将文件从不同的语言(如TypeScript)转换为 JavaScript</li>
</ul>
<p>loaders\px2rem-plus-loader.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> loaderUtils = <span class="hljs-built_in">require</span>(<span class="hljs-string">'loader-utils'</span>);
<span class="hljs-comment">//var Px2rem = require('px2rem');</span>
<span class="hljs-keyword">var</span> Px2rem = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./px2rem'</span>);
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loader</span>(<span class="hljs-params">source</span>) </span>&#123;
  <span class="hljs-keyword">var</span> options = loaderUtils.getOptions(<span class="hljs-built_in">this</span>);
  <span class="hljs-keyword">if</span>(options.exclude && options.exclude.test(<span class="hljs-built_in">this</span>.resource))&#123;
       <span class="hljs-keyword">return</span> source;
  &#125;
  <span class="hljs-keyword">var</span> px2remIns = <span class="hljs-keyword">new</span> Px2rem(options);
  <span class="hljs-keyword">let</span> targetSource = px2remIns.generateRem(source);
  <span class="hljs-keyword">return</span> targetSource;
&#125;
<span class="hljs-built_in">module</span>.exports = loader;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">4. 使用自定义loader</h2>
<p>webpack.config.js 中的配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">resolveLoader: &#123;
        <span class="hljs-attr">alias</span>: &#123;
          <span class="hljs-string">"px2rem-plus-loader"</span>: path.resolve(<span class="hljs-string">'./loaders/px2rem-plus-loader.js'</span>)
        &#125;,
        <span class="hljs-attr">modules</span>: [path.resolve(<span class="hljs-string">'./loaders'</span>), <span class="hljs-string">'node_modules'</span>]
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">5.css</h2>
<h3 data-id="heading-17">5.1 AST</h3>
<ul>
<li>
<p><a href="https://astexplorer.net/" target="_blank" rel="nofollow noopener noreferrer">astexplorer</a></p>
</li>
<li>
<p>JavaScript Parser可以把源代码转化为一颗抽象语法树（AST），这颗树定义了代码的结构</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa4c5025109e4272847ff50d7c0828b4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-18">5.2 AST工作流</h3>
<ul>
<li>Parse(解析) 将源代码转换成抽象语法树，树上有很多的estree节点</li>
<li>Transform(转换) 对抽象语法树进行转换</li>
<li>Generate(代码生成) 将上一步经过转换过的抽象语法树生成新的代码
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3da02e1cbeb54ac2af9d00922d40d673~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
<h3 data-id="heading-19">5.3 px2rem.js</h3>
<p><a href="https://www.npmjs.com/package/px2rem" target="_blank" rel="nofollow noopener noreferrer">px2rem</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/*
 * @Description: 
 * @Author: changqing
 * @Date: 2021-04-29 11:54:54
 * @LastEditTime: 2021-05-02 11:46:46
 * @LastEditors: changqing
 * @Usage: 
 */</span>
<span class="hljs-meta">'use strict'</span>;

<span class="hljs-keyword">var</span> css = <span class="hljs-built_in">require</span>(<span class="hljs-string">'css'</span>);
<span class="hljs-keyword">var</span> extend = <span class="hljs-built_in">require</span>(<span class="hljs-string">'extend'</span>);

<span class="hljs-keyword">var</span> defaultConfig = &#123;
  <span class="hljs-attr">baseDpr</span>: <span class="hljs-number">2</span>,             <span class="hljs-comment">// base device pixel ratio (default: 2)</span>
  <span class="hljs-attr">remUnit</span>: <span class="hljs-number">75</span>,            <span class="hljs-comment">// rem unit value (default: 75)</span>
  <span class="hljs-attr">remPrecision</span>: <span class="hljs-number">6</span>,        <span class="hljs-comment">// rem value precision (default: 6)</span>
  <span class="hljs-attr">forcePxComment</span>: <span class="hljs-string">'px'</span>,   <span class="hljs-comment">// force px comment (default: `px`)</span>
  <span class="hljs-attr">keepComment</span>: <span class="hljs-string">'no'</span>       <span class="hljs-comment">// no transform value comment (default: `no`)</span>
&#125;;

<span class="hljs-keyword">var</span> pxRegExp = <span class="hljs-regexp">/\b(\d+(\.\d+)?)px\b/</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Px2rem</span>(<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.config = &#123;&#125;;
  extend(<span class="hljs-built_in">this</span>.config, defaultConfig, options);
&#125;

<span class="hljs-comment">// generate @1x, @2x and @3x version stylesheet</span>
Px2rem.prototype.generateThree = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">cssText, dpr</span>) </span>&#123;
  dpr = dpr || <span class="hljs-number">2</span>;
  <span class="hljs-keyword">var</span> self = <span class="hljs-built_in">this</span>;
  <span class="hljs-keyword">var</span> config = self.config;
  <span class="hljs-keyword">var</span> astObj = css.parse(cssText);

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processRules</span>(<span class="hljs-params">rules</span>) </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < rules.length; i++) &#123;
      <span class="hljs-keyword">var</span> rule = rules[i];
      <span class="hljs-keyword">if</span> (rule.type === <span class="hljs-string">'media'</span>) &#123;
        processRules(rule.rules); <span class="hljs-comment">// recursive invocation while dealing with media queries</span>
        <span class="hljs-keyword">continue</span>;
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (rule.type === <span class="hljs-string">'keyframes'</span>) &#123;
        processRules(rule.keyframes); <span class="hljs-comment">// recursive invocation while dealing with keyframes</span>
        <span class="hljs-keyword">continue</span>;
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (rule.type !== <span class="hljs-string">'rule'</span> && rule.type !== <span class="hljs-string">'keyframe'</span>) &#123;
        <span class="hljs-keyword">continue</span>;
      &#125;

      <span class="hljs-keyword">var</span> declarations = rule.declarations;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> j = <span class="hljs-number">0</span>; j < declarations.length; j++) &#123;
        <span class="hljs-keyword">var</span> declaration = declarations[j];
        <span class="hljs-comment">// need transform: declaration && has 'px'</span>
        <span class="hljs-keyword">if</span> (declaration.type === <span class="hljs-string">'declaration'</span> && pxRegExp.test(declaration.value)) &#123;
          <span class="hljs-keyword">var</span> nextDeclaration = rule.declarations[j + <span class="hljs-number">1</span>];
          <span class="hljs-keyword">if</span> (nextDeclaration && nextDeclaration.type === <span class="hljs-string">'comment'</span>) &#123; <span class="hljs-comment">// next next declaration is comment</span>
            <span class="hljs-keyword">if</span> (nextDeclaration.comment.trim() === config.keepComment) &#123; <span class="hljs-comment">// no transform</span>
              declarations.splice(j + <span class="hljs-number">1</span>, <span class="hljs-number">1</span>); <span class="hljs-comment">// delete corresponding comment</span>
              <span class="hljs-keyword">continue</span>;
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (nextDeclaration.comment.trim() === config.forcePxComment) &#123; <span class="hljs-comment">// force px</span>
              declarations.splice(j + <span class="hljs-number">1</span>, <span class="hljs-number">1</span>); <span class="hljs-comment">// delete corresponding comment</span>
            &#125;
          &#125;
          declaration.value = self._getCalcValue(<span class="hljs-string">'px'</span>, declaration.value, dpr); <span class="hljs-comment">// common transform</span>
        &#125;
      &#125;
    &#125;
  &#125;

  processRules(astObj.stylesheet.rules);

  <span class="hljs-keyword">return</span> css.stringify(astObj);
&#125;;

<span class="hljs-comment">// generate rem version stylesheet</span>
Px2rem.prototype.generateRem = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">cssText</span>) </span>&#123;
  <span class="hljs-keyword">var</span> self = <span class="hljs-built_in">this</span>;
  <span class="hljs-keyword">var</span> config = self.config;
  <span class="hljs-keyword">var</span> astObj = css.parse(cssText);

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processRules</span>(<span class="hljs-params">rules, noDealPx</span>) </span>&#123; <span class="hljs-comment">// <span class="hljs-doctag">FIXME:</span> keyframes do not support `force px` comment</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < rules.length; i++) &#123;
      <span class="hljs-keyword">var</span> rule = rules[i];
      <span class="hljs-keyword">if</span> (rule.type === <span class="hljs-string">'media'</span>) &#123;
        processRules(rule.rules); <span class="hljs-comment">// recursive invocation while dealing with media queries</span>
        <span class="hljs-keyword">continue</span>;
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (rule.type === <span class="hljs-string">'keyframes'</span>) &#123;
        processRules(rule.keyframes, <span class="hljs-literal">true</span>); <span class="hljs-comment">// recursive invocation while dealing with keyframes</span>
        <span class="hljs-keyword">continue</span>;
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (rule.type !== <span class="hljs-string">'rule'</span> && rule.type !== <span class="hljs-string">'keyframe'</span>) &#123;
        <span class="hljs-keyword">continue</span>;
      &#125;

      <span class="hljs-keyword">if</span> (!noDealPx) &#123;
        <span class="hljs-comment">// generate 3 new rules which has [data-dpr]</span>
        <span class="hljs-keyword">var</span> newRules = [];
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> dpr = <span class="hljs-number">1</span>; dpr <= <span class="hljs-number">3</span>; dpr++) &#123;
          <span class="hljs-keyword">var</span> newRule = &#123;&#125;;
          newRule.type = rule.type;
          newRule.selectors = rule.selectors.map(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">sel</span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">'[data-dpr="'</span> + dpr + <span class="hljs-string">'"] '</span> + sel;
          &#125;);
          newRule.declarations = [];
          newRules.push(newRule);
        &#125;
      &#125;

      <span class="hljs-keyword">var</span> declarations = rule.declarations;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> j = <span class="hljs-number">0</span>; j < declarations.length; j++) &#123;
        <span class="hljs-keyword">var</span> declaration = declarations[j];
        <span class="hljs-comment">// need transform: declaration && has 'px'</span>
        <span class="hljs-keyword">if</span> (declaration.type === <span class="hljs-string">'declaration'</span> && pxRegExp.test(declaration.value)) &#123;
          <span class="hljs-keyword">var</span> nextDeclaration = declarations[j + <span class="hljs-number">1</span>];
          <span class="hljs-keyword">if</span> (nextDeclaration && nextDeclaration.type === <span class="hljs-string">'comment'</span>) &#123; <span class="hljs-comment">// next next declaration is comment</span>
            <span class="hljs-keyword">if</span> (nextDeclaration.comment.trim() === config.forcePxComment) &#123; <span class="hljs-comment">// force px</span>
              <span class="hljs-comment">// do not transform `0px`</span>
              <span class="hljs-keyword">if</span> (declaration.value === <span class="hljs-string">'0px'</span>) &#123;
                declaration.value = <span class="hljs-string">'0'</span>;
                declarations.splice(j + <span class="hljs-number">1</span>, <span class="hljs-number">1</span>); <span class="hljs-comment">// delete corresponding comment</span>
                <span class="hljs-keyword">continue</span>;
              &#125;
              <span class="hljs-keyword">if</span> (!noDealPx) &#123;
                <span class="hljs-comment">// generate 3 new declarations and put them in the new rules which has [data-dpr]</span>
                <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> dpr = <span class="hljs-number">1</span>; dpr <= <span class="hljs-number">3</span>; dpr++) &#123;
                  <span class="hljs-keyword">var</span> newDeclaration = &#123;&#125;;
                  extend(<span class="hljs-literal">true</span>, newDeclaration, declaration);
                  newDeclaration.value = self._getCalcValue(<span class="hljs-string">'px'</span>, newDeclaration.value, dpr);
                  newRules[dpr - <span class="hljs-number">1</span>].declarations.push(newDeclaration);
                &#125;
                declarations.splice(j, <span class="hljs-number">2</span>); <span class="hljs-comment">// delete this rule and corresponding comment</span>
                j--;
              &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// <span class="hljs-doctag">FIXME:</span> keyframes do not support `force px` comment</span>
                declaration.value = self._getCalcValue(<span class="hljs-string">'rem'</span>, declaration.value); <span class="hljs-comment">// common transform</span>
                declarations.splice(j + <span class="hljs-number">1</span>, <span class="hljs-number">1</span>); <span class="hljs-comment">// delete corresponding comment</span>
              &#125;
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (nextDeclaration.comment.trim() === config.keepComment) &#123; <span class="hljs-comment">// no transform</span>
              declarations.splice(j + <span class="hljs-number">1</span>, <span class="hljs-number">1</span>); <span class="hljs-comment">// delete corresponding comment</span>
            &#125; <span class="hljs-keyword">else</span> &#123;
              declaration.value = self._getCalcValue(<span class="hljs-string">'rem'</span>, declaration.value); <span class="hljs-comment">// common transform</span>
            &#125;
          &#125; <span class="hljs-keyword">else</span> &#123;
            declaration.value = self._getCalcValue(<span class="hljs-string">'rem'</span>, declaration.value); <span class="hljs-comment">// common transform</span>
          &#125;
        &#125;
      &#125;

      <span class="hljs-comment">// if the origin rule has no declarations, delete it</span>
      <span class="hljs-keyword">if</span> (!rules[i].declarations.length) &#123;
        rules.splice(i, <span class="hljs-number">1</span>);
        i--;
      &#125;

      <span class="hljs-keyword">if</span> (!noDealPx) &#123;
        <span class="hljs-comment">// add the new rules which contain declarations that are forced to use px</span>
        <span class="hljs-keyword">if</span> (newRules[<span class="hljs-number">0</span>].declarations.length) &#123;
          rules.splice(i + <span class="hljs-number">1</span>, <span class="hljs-number">0</span>, newRules[<span class="hljs-number">0</span>], newRules[<span class="hljs-number">1</span>], newRules[<span class="hljs-number">2</span>]);
          i += <span class="hljs-number">3</span>; <span class="hljs-comment">// skip the added new rules</span>
        &#125;
      &#125;
    &#125;
  &#125;

  processRules(astObj.stylesheet.rules);

  <span class="hljs-keyword">return</span> css.stringify(astObj);
&#125;;

<span class="hljs-comment">// get calculated value of px or rem</span>
Px2rem.prototype._getCalcValue = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">type, value, dpr</span>) </span>&#123;
  <span class="hljs-keyword">var</span> config = <span class="hljs-built_in">this</span>.config;
  <span class="hljs-keyword">var</span> pxGlobalRegExp = <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(pxRegExp.source, <span class="hljs-string">'g'</span>);

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getValue</span>(<span class="hljs-params">val</span>) </span>&#123;
    val = <span class="hljs-built_in">parseFloat</span>(val.toFixed(config.remPrecision)); <span class="hljs-comment">// control decimal precision of the calculated value</span>
    <span class="hljs-keyword">return</span> val == <span class="hljs-number">0</span> ? val : val + type;
  &#125;

  <span class="hljs-keyword">return</span> value.replace(pxGlobalRegExp, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">$<span class="hljs-number">0</span>, $<span class="hljs-number">1</span></span>) </span>&#123;
    <span class="hljs-keyword">return</span> type === <span class="hljs-string">'px'</span> ? getValue($<span class="hljs-number">1</span> * dpr / config.baseDpr) : getValue($<span class="hljs-number">1</span> / config.remUnit);
  &#125;);
&#125;;

<span class="hljs-built_in">module</span>.exports = Px2rem;


<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">5.4 usePx2rem.js</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> Px2rem = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./px2rem'</span>);
<span class="hljs-keyword">let</span> px2rem = <span class="hljs-keyword">new</span> Px2rem(&#123;
    <span class="hljs-attr">remUnit</span>: <span class="hljs-number">75</span>,
    <span class="hljs-attr">remPrecision</span>: <span class="hljs-number">8</span>
&#125;);
<span class="hljs-keyword">let</span> cssText = <span class="hljs-string">`
#root&#123;
    width:750px;
    height:750px;
    font-size:12px;/*px*/
    border: 1px solid #ddd; /*no*/
&#125;
`</span>;
<span class="hljs-keyword">let</span> newCSS = px2rem.generateRem(cssText);
<span class="hljs-built_in">console</span>.log(newCSS);

<span class="hljs-comment">// #root &#123;</span>
<span class="hljs-comment">//   width: 10rem;</span>
<span class="hljs-comment">//   height: 10rem;</span>
<span class="hljs-comment">//   border: 1px solid #ddd;</span>
<span class="hljs-comment">// &#125;</span>

<span class="hljs-comment">// [data-dpr="1"] #root &#123;</span>
<span class="hljs-comment">//   font-size: 6px;</span>
<span class="hljs-comment">// &#125;</span>

<span class="hljs-comment">// [data-dpr="2"] #root &#123;</span>
<span class="hljs-comment">//   font-size: 12px;</span>
<span class="hljs-comment">// &#125;</span>

<span class="hljs-comment">// [data-dpr="3"] #root &#123;</span>
<span class="hljs-comment">//   font-size: 18px;</span>
<span class="hljs-comment">// &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">6. px2rem-loader.js</h2>
<ul>
<li>
<p><a href="https://www.npmjs.com/package/loader-utils" target="_blank" rel="nofollow noopener noreferrer">loader-utils</a>是一个webpack工具类</p>
</li>
<li>
<p><a href="https://www.npmjs.com/package/px2rem-loader" target="_blank" rel="nofollow noopener noreferrer">px2rem-loader</a></p>
</li>
<li>
<p>直接写px，编译后会直接转化成rem</p>
</li>
<li>
<p>在px后面添加/no/，不会转化px，会原样输出 一般border需用这个</p>
</li>
<li>
<p>在px后面添加/px/,会根据dpr的不同，生成三套代码 一般字体需用这个</p>
</li>
</ul>
<h2 data-id="heading-22">7. lib-flexible</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">'./base.css'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'amfe-flexible/index.js'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23">8. 第三方框架样式问题</h2>
<ul>
<li>如果第三方组件已经是为移动端做了适配,px2rem又转成了rem就导致其样式变的很小</li>
</ul>
<h3 data-id="heading-24">8.1 index.js</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">'./base.css'</span>
<span class="hljs-comment">//import 'amfe-flexible/index.js';</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'lib-flexible/flexible.js'</span>
<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'antd/dist/antd.css'</span>;
<span class="hljs-keyword">import</span> &#123;Button&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;
ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    我是<span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">8.2 webpack.config.js</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-attr">loader</span>: <span class="hljs-string">'px2rem-plus-loader'</span>, <span class="hljs-comment">//path.resolve(__dirname, 'loaders/px2rem-plus-loader.js'),</span>
     <span class="hljs-attr">options</span>: &#123;
                  <span class="hljs-attr">remUnit</span>: <span class="hljs-number">75</span>,
                  <span class="hljs-attr">remPrecision</span>: <span class="hljs-number">8</span>,
                  <span class="hljs-attr">baseDpr</span>:<span class="hljs-number">1</span>,
                  <span class="hljs-attr">exclude</span>:<span class="hljs-regexp">/antd\.css/</span>
              &#125;
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>px2rem-plus-loader 增加 exclude参数排除不需要处理的css文件</p>
<p><a href="https://github.com/changqingniubi/px2rem-project" target="_blank" rel="nofollow noopener noreferrer">仓库地址</a></p></div>  
</div>
            