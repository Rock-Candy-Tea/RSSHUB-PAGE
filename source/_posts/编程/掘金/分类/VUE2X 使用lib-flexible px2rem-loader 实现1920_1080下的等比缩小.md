
---
title: 'VUE2.X 使用lib-flexible px2rem-loader 实现1920_1080下的等比缩小'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54ff2afd39ac43f8aa23f0f33e910ad1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 30 May 2021 02:38:35 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54ff2afd39ac43f8aa23f0f33e910ad1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">效果</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54ff2afd39ac43f8aa23f0f33e910ad1~tplv-k3u1fbpfcp-watermark.image" alt="解决.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-1">先用脚手架安装基础框架 并实现一个水平居中的效果 如下图所示</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/777f341b49bc45eca4bd3903102ae8db~tplv-k3u1fbpfcp-watermark.image" alt="步骤1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>结构目录如下</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a956549b3830432eb66173feda489cec~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>reset.css</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, <span class="hljs-keyword">var</span>,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed, 
figure, figcaption, footer, header, hgroup, 
menu, nav, output, ruby, section, summary,
time, mark, audio, video &#123;
<span class="hljs-attr">margin</span>: <span class="hljs-number">0</span>;
padding: <span class="hljs-number">0</span>;
border: <span class="hljs-number">0</span>;
font-size: <span class="hljs-number">100</span>%;
font: inherit;
vertical-align: baseline;
&#125;
<span class="hljs-comment">/* HTML5 display-role reset for older browsers */</span>
article, aside, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section &#123;
<span class="hljs-attr">display</span>: block;
&#125;
body &#123;
line-height: <span class="hljs-number">1</span>;
&#125;
ol, ul &#123;
list-style: none;
&#125;
blockquote, q &#123;
<span class="hljs-attr">quotes</span>: none;
&#125;
<span class="hljs-attr">blockquote</span>:before, <span class="hljs-attr">blockquote</span>:after,
<span class="hljs-attr">q</span>:before, <span class="hljs-attr">q</span>:after &#123;
<span class="hljs-attr">content</span>: <span class="hljs-string">''</span>;
content: none;
&#125;
table &#123;
border-collapse: collapse;
border-spacing: <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>demo.vue</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>

  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"demo"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"bigBox"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"smallBox"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> ></span>

<span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">

  <span class="hljs-selector-class">.demo</span>&#123;
    <span class="hljs-attribute">height</span>:<span class="hljs-number">100vh</span>;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">justify-content</span>: center;
    <span class="hljs-attribute">align-items</span>: center;
  &#125;
  <span class="hljs-selector-class">.bigBox</span>&#123;
    <span class="hljs-attribute">width</span>:<span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>:<span class="hljs-number">400px</span>;
    <span class="hljs-attribute">background</span>:pink;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">justify-content</span>: center;
    <span class="hljs-attribute">align-items</span>: center;
  &#125;
  <span class="hljs-selector-class">.bigBox</span>><span class="hljs-selector-class">.smallBox</span>&#123;
    <span class="hljs-attribute">width</span>:<span class="hljs-number">200px</span>;
    <span class="hljs-attribute">height</span>:<span class="hljs-number">200px</span>;
    <span class="hljs-attribute">background</span>:blue;
  &#125;

</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在拖动屏幕是没效果的 应该是这样</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/baa19866119147258b54648711f0677a~tplv-k3u1fbpfcp-watermark.image" alt="问题1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">安装 lib-flexible(<strong>px转换成rem</strong>)</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install lib-flexible --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">引入 lib-flexible</h4>
<p>在<code>main.js</code>中引入lib-flexible</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">'lib-flexible'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'@/assets/css/reset.css'</span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来会看着这个问题</p>
<p><strong>注:html的font-size为 宽度/10 即正常</strong></p>
<p>手机端的font-size是正常的</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e189a0c48c4424782c40ff39b6579c9~tplv-k3u1fbpfcp-watermark.image" alt="手机正常1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>pc端的font-size始终不正确</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fde4b56444441e59173cfd228c8a6bf~tplv-k3u1fbpfcp-watermark.image" alt="PCbug.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>找到源码</strong></p>
<p>打开<code>./node_modules/lib-flexible/flexible.js</code>，找到如下片段源码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">refreshRem</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">var</span> width = docEl.getBoundingClientRect().width;
    <span class="hljs-keyword">if</span> (width / dpr > <span class="hljs-number">540</span>) &#123;
        width = <span class="hljs-number">540</span> * dpr;
    &#125;
    <span class="hljs-keyword">var</span> rem = width / <span class="hljs-number">10</span>;
    docEl.style.fontSize = rem + <span class="hljs-string">'px'</span>;
    flexible.rem = win.rem = rem;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">修改源码</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">refreshRem</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> width = docEl.getBoundingClientRect().width;
        <span class="hljs-keyword">if</span> (width / dpr > <span class="hljs-number">1920</span>) &#123;
            width = <span class="hljs-number">1920</span> * dpr;
        &#125;
        <span class="hljs-keyword">var</span> rem = width / <span class="hljs-number">10</span>;
        docEl.style.fontSize = rem + <span class="hljs-string">'px'</span>;
        flexible.rem = win.rem = rem;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在pc端应该是正常的</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c4f13af057c4d178ab7d09dd917e6ac~tplv-k3u1fbpfcp-watermark.image" alt="正常了.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">安装 px2rem-loader</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install px2rem-loader --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">配置 px2rem-loader</h4>
<p>1.在<code>build/utils.js</code>中，找到<code>exports.cssLoaders</code>，作出如下修改：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-built_in">exports</span>.cssLoaders = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
      
      options = options || &#123;&#125;
      
      <span class="hljs-keyword">const</span> px2remLoader = &#123;
        <span class="hljs-attr">loader</span>: <span class="hljs-string">'px2rem-loader'</span>,
        <span class="hljs-attr">options</span>: &#123;
          <span class="hljs-attr">remUint</span>: <span class="hljs-number">192</span>
        &#125;
      &#125;
  
  ....
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.继续找到<code>generateLoaders</code>中的<code>loaders</code>配置，作出如下配置：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">// const loaders = options.usePostCSS ? [cssLoader, postcssLoader] : [cssLoader]</span>
    <span class="hljs-keyword">const</span> loaders = [cssLoader, px2remLoader]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行项目 ...  新的bug来了  元素变得超级大</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1be151215d604967b26e6820a41ff4cd~tplv-k3u1fbpfcp-watermark.image" alt="新的Bug.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">继续修改源码</h3>
<p>目录:<code>node_modules/px2rem/lib/px2rem.js</code></p>
<p>修改为</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> defaultConfig = &#123;
  <span class="hljs-attr">baseDpr</span>: <span class="hljs-number">1</span>,             <span class="hljs-comment">// base device pixel ratio (default: 2)</span>
  <span class="hljs-attr">remUnit</span>: <span class="hljs-number">192</span>,            <span class="hljs-comment">// rem unit value (default: 75)</span>
  <span class="hljs-attr">remPrecision</span>: <span class="hljs-number">6</span>,        <span class="hljs-comment">// rem value precision (default: 6)</span>
  <span class="hljs-attr">forcePxComment</span>: <span class="hljs-string">'px'</span>,   <span class="hljs-comment">// force px comment (default: `px`)</span>
  <span class="hljs-attr">keepComment</span>: <span class="hljs-string">'no'</span>       <span class="hljs-comment">// no transform value comment (default: `no`)</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重启！ 正常啦</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09b49e1110ae4cb290c1a7a59120697d~tplv-k3u1fbpfcp-watermark.image" alt="正常啦.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            