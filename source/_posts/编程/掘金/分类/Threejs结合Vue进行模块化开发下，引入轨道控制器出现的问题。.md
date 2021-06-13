
---
title: 'Three.js结合Vue进行模块化开发下，引入轨道控制器出现的问题。'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/515859029fae4fd7a2ba09dfcf258623~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 01:20:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/515859029fae4fd7a2ba09dfcf258623~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">存在问题</h2>
<p><code>three@0.129.0</code>版本的轨道控制器类是在<code>three/examples/js/controls/OrbitControls.js</code>文件中定义的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// file: three/examples/js/controls/OrbitControls.js</span>
(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// ...</span>
    THREE.OrbitControls = OrbitControls;
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而当我们使用webpack+ES6模块化开发的时候：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> THREE <span class="hljs-keyword">from</span> <span class="hljs-string">'three'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'three/examples/js/controls/OrbitControls'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>控制台会报错<code>Uncaught ReferenceError: THREE is not defined</code>,说THREE变量没有定义，因为<code>OrbitControls.js</code>文件中使用的THREE是全局的，而我们全局并没有这个属性。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/515859029fae4fd7a2ba09dfcf258623~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">解决方案</h2>
<p>借助<code>imports-loader</code>，在<code>three/examples/js/controls/OrbitControls.js</code>文件中注入<code>import * as THREE from 'three'</code>.</p>
<pre><code class="hljs language-shell copyable" lang="shell">    npm i imports-loader -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下载后，对webpack.config.js文件进行修改，在module.rules中添加匹配规则</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    ...
    <span class="hljs-attr">module</span>: &#123;
        ...,
        <span class="hljs-attr">rules</span>: [
            &#123;
              <span class="hljs-attr">test</span>: <span class="hljs-built_in">require</span>.resolve(<span class="hljs-string">'three/examples/js/controls/OrbitControls'</span>),
              <span class="hljs-attr">use</span>: [
                &#123;
                  <span class="hljs-attr">loader</span>: <span class="hljs-string">'imports-loader'</span>,
                  <span class="hljs-attr">options</span>: &#123;
                    <span class="hljs-attr">imports</span>: [
                    <span class="hljs-comment">// namespace three THREE' 注入规则请自行前往https://www.npmjs.com/package/imports-loader 查看</span>
                      <span class="hljs-string">'namespace three THREE'</span>
                    ]
                  &#125;
                &#125;
              ]
            &#125;,
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重新编译之后就能愉快的使用<code>OrbitControls</code>插件了。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6c4d7e2573545fe92e4bd842e15ea61~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e16940452824c8a8decfdc99cf84c36~tplv-k3u1fbpfcp-watermark.image" alt="demo.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">注意</h2>
<p>当你项目依赖的<code>webpack</code>版本与<code>imports-loader</code>版本不兼容时，会出现下面这种情况：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a5796628ef94e86b57742fe056edd44~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">解决方法</h3>
<pre><code class="copyable">升级webpack版本，或者降低imports-loader版本
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">疑问</h4>
<pre><code class="copyable">如何知道loader对应的webpack版本呢？有没有知道的评论区告诉我一下。谢谢！！！
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            