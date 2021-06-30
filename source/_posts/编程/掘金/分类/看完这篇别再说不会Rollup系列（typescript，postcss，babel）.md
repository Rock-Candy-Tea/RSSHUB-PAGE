
---
title: '看完这篇别再说不会Rollup系列（typescript，postcss，babel）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66ccc68b495946c1aa6d28aca039f49a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 29 Jun 2021 05:59:33 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66ccc68b495946c1aa6d28aca039f49a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>在前端领域摸爬滚打这些年，大部分时间都花在了组件上，但大多是做着做着就放弃了，例如去年疫情期间闲来无聊用<code>stencil</code>写了个webcomponent组件库<a href="https://github.com/swimly/mui" target="_blank" rel="nofollow noopener noreferrer">【mui】</a>，组件基本上都完善的差不多，可最后由于公司还接受不了这种形式，最后就被遗忘在脑后。后来的<code>uni-app</code>组件库<a href="https://github.com/swimly/miui-uni" target="_blank" rel="nofollow noopener noreferrer">【miui-uni】</a>也避免不了这种结局。接下来的一年多时间基本上都沉醉于各种形式的组件库编写，由最开始的傻瓜式写法（没用任何打包工具），每次总是写着写着就感觉写不下去了，知道今年一个偶然的机会了解到<code>rollup</code>，再次寻找到了写组件库的最佳姿势。</p>
<p>话不多说，</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66ccc68b495946c1aa6d28aca039f49a~tplv-k3u1fbpfcp-watermark.image" alt="20190509394748_OQcJLN.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">基础架构</h3>
<p>首先，打开<code>win11</code>的 <code>Powersheel</code>，按照下面的步骤一顿操作。</p>
<pre><code class="hljs language-bash copyable" lang="bash">mkdir xxx
npm init -y
cnpm i -D rollup @rollup/plugin-node-resolve @rollup/plugin-commonjs @rollup/plugin-json
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不出意外，你的package.json应该长这样。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"devDependencies"</span>: &#123;
    <span class="hljs-attr">"@rollup/plugin-commonjs"</span>: <span class="hljs-string">"^19.0.0"</span>,
    <span class="hljs-attr">"@rollup/plugin-json"</span>: <span class="hljs-string">"^4.1.0"</span>,
    <span class="hljs-attr">"@rollup/plugin-node-resolve"</span>: <span class="hljs-string">"^13.0.0"</span>,
    <span class="hljs-attr">"rollup"</span>: <span class="hljs-string">"^2.52.3"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>皮包公司已创立，接下来就要建立一个<code>粗糙</code>的公司制度了。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0097865c5a9648aabdc3385951762e75~tplv-k3u1fbpfcp-watermark.image" alt="20200529732665_TnolBy.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>公司制度范本（<code>rollup.config.js</code>）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> json <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-json'</span>
<span class="hljs-keyword">import</span> resolve <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-node-resolve'</span>
<span class="hljs-keyword">import</span> commonjs <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-commonjs'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">input</span>: <span class="hljs-string">'src/index.js'</span>,
  <span class="hljs-attr">output</span>: [&#123;
    <span class="hljs-attr">file</span>: <span class="hljs-string">'dist/bundle.js'</span>,
    <span class="hljs-attr">format</span>: <span class="hljs-string">'cjs'</span>,
    <span class="hljs-attr">exports</span>: <span class="hljs-string">'auto'</span>
  &#125;],
  <span class="hljs-attr">plugins</span>: [
    json(),
    resolve(),
    commonjs()
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下一步，弄个<code>REN</code>组件来试试这套制度可行不。</p>
<p><code>src/index.js</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> name = <span class="hljs-string">'ren'</span>;
  <span class="hljs-built_in">console</span>.log(name)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来在人力资源总部<code>package.json</code>添加一条咒语<code>scripts</code></p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"dev"</span>: <span class="hljs-string">"rollup -c"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然如果全局安装了<code>rollup</code>，不用通知人力资源也行，直接发布指令即可。</p>
<pre><code class="hljs language-bash copyable" lang="bash">yarn dev && rollup -c
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面就是这条指令的产出</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-meta">'use strict'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">index</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> name = <span class="hljs-string">'ren'</span>;
  <span class="hljs-built_in">console</span>.log(name);
&#125;

<span class="hljs-built_in">module</span>.exports = index;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，如果仅仅是如此，何以体现<code>rollup</code>的强大呢？至于更为详细的配置清单，请大家自行<code>百度</code>。</p>
<h3 data-id="heading-2">Postcss</h3>
<p>一个好的组件库肯定不可能只有<code>javascript</code>吧，网页三剑客（<code>html</code>，<code>css</code>，<code>javaScript</code>）那是缺一不可。</p>
<p>目前比较流行的<code>css</code>预处理无非还是那三位：<code>sass</code>，<code>less</code>，<code>postcss</code>，<code>less</code>鄙人从未用过，就不在这班门弄斧了，<code>scss</code>也写了好久，可就觉得差了那么一点味道，不用说也知道了吧，接下来要介绍<code>postcss</code>的配置了，啥都不说，干就是了。</p>
<p>主角：<a href="https://www.npmjs.com/package/rollup-plugin-postcss" target="_blank" rel="nofollow noopener noreferrer">rollup-plugin-postcss</a>，地址已贴，请大家细细品味。</p>
<pre><code class="hljs language-bash copyable" lang="bash">cnpm i -D rollup-plugin-postcss postcss
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> postcss <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-postcss'</span>
<span class="hljs-attr">plugins</span>: [
    json(),
    resolve(),
    commonjs(),
    <span class="hljs-comment">//添加</span>
    postcss(&#123;
      <span class="hljs-attr">extract</span>: <span class="hljs-literal">true</span>  <span class="hljs-comment">//true：分离出css文件，false：会在style里插入css</span>
    &#125;)
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面对<code>src/index.js</code>稍作修改，在该目录创建<code>main.css</code>，并在<code>index.js</code>进入。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">'./main.css'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次轻声念叨那句咒语！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0043c49dcda6438e8465e6768559df1a~tplv-k3u1fbpfcp-watermark.image" alt="20200614089263_XSiuoa.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不出意外，你会看到下面这两货。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c03ab3e107a946dd88d5e10215f61a1b~tplv-k3u1fbpfcp-watermark.image" alt="微信截图_20210629210515.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>postcss</code>算是可以了，可还什么插件都木有，这跟手写<code>css</code>有啥区别，接下来安装的插件有些许多，到了这一步可根据需求自行安装相应的插件。</p>
<pre><code class="hljs language-bash copyable" lang="bash">cnpm i -D postcss-color-mod-function postcss-functions postcss-import postcss-mixins postcss-modules postcss-nested postcss-prepend-imports postcss-pxtorem postcss-simple-vars
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建一个postcss配置文件<code>postcss.config.js</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">// 预先加载这里面的css，常用来配置主题变量</span>
    <span class="hljs-comment">// require('postcss-prepend-imports')(&#123;</span>
    <span class="hljs-comment">//   path: `./src/themes/default`,</span>
    <span class="hljs-comment">//   files: ['variable.css']</span>
    <span class="hljs-comment">// &#125;),</span>
    <span class="hljs-built_in">require</span>(<span class="hljs-string">'postcss-import'</span>)(),
    <span class="hljs-built_in">require</span>(<span class="hljs-string">'postcss-nested'</span>)(),
    <span class="hljs-built_in">require</span>(<span class="hljs-string">'postcss-pxtorem'</span>)(&#123;
      <span class="hljs-attr">rootValue</span>: <span class="hljs-number">20</span>,
      <span class="hljs-attr">propList</span>: [<span class="hljs-string">'*'</span>, <span class="hljs-string">'!border'</span>],
      <span class="hljs-attr">replace</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">mediaQuery</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">minPixelValue</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/i</span>
    &#125;),
    <span class="hljs-built_in">require</span>(<span class="hljs-string">'postcss-color-mod-function'</span>)(),
    <span class="hljs-built_in">require</span>(<span class="hljs-string">'autoprefixer'</span>)(&#123;
      <span class="hljs-attr">overrideBrowserslist</span>: [
        <span class="hljs-string">"last 2 version"</span>,
        <span class="hljs-string">">1%"</span>,
        <span class="hljs-string">"ios 7"</span>
      ]
    &#125;),
    <span class="hljs-built_in">require</span>(<span class="hljs-string">'postcss-functions'</span>)(&#123;
      <span class="hljs-comment">// 这里可以写js方法供postcss调用</span>
      <span class="hljs-attr">functions</span>: &#123;&#125;
    &#125;),
    <span class="hljs-built_in">require</span>(<span class="hljs-string">'postcss-simple-vars'</span>)(),
    <span class="hljs-built_in">require</span>(<span class="hljs-string">'cssnano'</span>)
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改<code>rollup.config.js</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> postcssConfig = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./postcss.config'</span>)

postcss(&#123;
  <span class="hljs-attr">extract</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-comment">//新增</span>
  <span class="hljs-attr">plugins</span>: postcssConfig.plugins
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里，就可以毫无顾忌肆无忌惮的写<code>scss</code>了，不对，是<code>postcss</code>。</p>
<h3 data-id="heading-3">Babel</h3>
<p>接下来，为了适应某些（<code>微软</code>）公司的浏览器还停留在远古时代，压根就听不懂我们现在的日常用语，这时候我们就需要一个翻译。</p>
<pre><code class="hljs language-bash copyable" lang="bash">cnpm i -D rollup-plugin-babel @babel/core @babel/plugin-proposal-object-rest-spread babel-plugin-transform-object-assign @babel/runtime-corejs2 @babel/plugin-transform-runtime @babel/preset-env babel-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改<code>src/index.js</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-string">'./main.css'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> </span>&#123;
  <span class="hljs-title">constructor</span> (<span class="hljs-params"></span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'helloworld'</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次打包，会自动翻译成<code>ie</code>能辨识的语言。</p>
<h3 data-id="heading-4">Typescript</h3>
<p>在<code>babel</code>的基础上要支持<code>typescript</code>很简单。</p>
<pre><code class="hljs language-bash copyable" lang="bash">cnpm i -D @babel/preset-typescript typescript tslib
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改<code>rollup.config.js</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">babel(&#123;
  <span class="hljs-attr">exclude</span>: [<span class="hljs-regexp">/\/core-js\//</span>],
  <span class="hljs-attr">runtimeHelpers</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'.js'</span>, <span class="hljs-string">'.jsx'</span>, <span class="hljs-string">'.es6'</span>, <span class="hljs-string">'.es'</span>, <span class="hljs-string">'.mjs'</span>, <span class="hljs-string">'.vue'</span>, <span class="hljs-string">'.ts'</span>],
  <span class="hljs-attr">presets</span>: [
    [<span class="hljs-string">"@babel/env"</span>, &#123;
      <span class="hljs-attr">modules</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">useBuiltIns</span>: <span class="hljs-string">'usage'</span>,
      <span class="hljs-attr">corejs</span>: <span class="hljs-number">2</span>,
      <span class="hljs-attr">forceAllTransforms</span>: <span class="hljs-literal">true</span>
    &#125;],
    <span class="hljs-comment">// 添加</span>
    [
      <span class="hljs-string">"@babel/preset-typescript"</span>,
      &#123;
        <span class="hljs-attr">extensions</span>: [<span class="hljs-string">".ts"</span>]
      &#125;
    ]
  ],
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-string">"babel-plugin-transform-object-assign"</span>,
    <span class="hljs-string">"@babel/plugin-proposal-object-rest-spread"</span>
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然你还可以单独使用<a href="https://www.npmjs.com/package/rollup-plugin-typescript2" target="_blank" rel="nofollow noopener noreferrer"><code>rollup-plugin-typescript2</code></a>，用法其实也就和一般的<code>rollup</code>插件一样。</p>
<h3 data-id="heading-5">Pug</h3>
<p>还记得当年那种拼接字符串或者<code>document.createElement</code>，写起来简直要命，<code>rollup</code>同样支持pug模板引擎。</p>
<pre><code class="hljs language-bash copyable" lang="bash">cnpm i -D rollup-plugin-pug
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在<code>rollup.config.js</code>中常规引入即可。</p>
<p>具体用法请参照<a href="https://www.npmjs.com/package/rollup-plugin-pug" target="_blank" rel="nofollow noopener noreferrer">rollup-plugin-pug</a></p>
<blockquote>
<p>友情提示：<code>pug</code>可配合<code>postcss-modules</code>，会有不一样的烟火，这里不细讲，后期请大家通过<code>github</code>查看详细用法。</p>
</blockquote>
<p>最后在此贴上<a href="https://gitee.com/swimly/typescript" target="_blank" rel="nofollow noopener noreferrer">gitee</a>，更为详细的配置供大家参考。</p>
<p>这篇主要讲解<code>rollup</code>的基础打包，以及一些常用<code>plugin</code>搭建的一套 ui组件库的基础结构，后面会更新<code>rollup</code>打包其他组件库的相关教程（<code>vue2</code>，<code>vue3</code>），以及<code>storybook</code>系列。</p></div>  
</div>
            