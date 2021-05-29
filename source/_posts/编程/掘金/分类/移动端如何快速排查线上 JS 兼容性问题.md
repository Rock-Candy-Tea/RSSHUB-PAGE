
---
title: '移动端如何快速排查线上 JS 兼容性问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cd9cd827c6e41ffa632a1698d5468fc~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 28 May 2021 06:59:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cd9cd827c6e41ffa632a1698d5468fc~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>你不可错过的 JS 兼容性排查利器 <a href="https://www.npmjs.com/package/es5-validator" target="_blank" rel="nofollow noopener noreferrer">ES5 Validator</a></p>
</blockquote>
<p>小程序或 H5 线上如果遇到『SyntaxError: Unexpected token...』通常是兼容性问题导致的，其表现很可能是进入小程序就白屏，后果很严重通常导致应用不可用。</p>
<p>那么在迅速止血回滚后，我们如何快速定位问题？</p>
<h2 data-id="heading-0">事后快速定位</h2>
<p>利用 <a href="https://www.npmjs.com/package/es5-validator" target="_blank" rel="nofollow noopener noreferrer">es5-validator</a> 检测事故线上 js bundle 文件，秒级暴露问题：发现函数默认值以及 let 等高级语法。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cd9cd827c6e41ffa632a1698d5468fc~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">事前预防</h2>
<h3 data-id="heading-2">针对无法编译的第三方依赖包</h3>
<p>当然最佳方案是升级构建器，如果不想升级可通过将 es5-validator 引入项目，在 build 后校验构建产物，即可达到提前预防的目的。</p>
<p>package.json：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
   <span class="hljs-attr">"postbuild"</span>: <span class="hljs-string">"es5-validator ./dist/index.min.js"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">针对历史遗留的不经过编译的业务源码</h3>
<p>仍然需要维护上古时期代码？还在小心翼翼胆战心惊避免使用 const、箭头函数、计算属性、属性简写、for of 吗？如果人工检测和 CR 你能确保不会有高级语法潜伏悄然上线成为一颗触发故障的定时炸弹？</p>
<p>以下通过接入 es5-validator 发现：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fca54232f2ba4621b5792f908296dbd6~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7236b91127343b68ea01547f6bdee5a~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47d571ba765f425690759f9ba4b78552~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">彻底的预防之道</h4>
<p>package.json：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"postbuild"</span>: <span class="hljs-string">"npm run validate:es5"</span>,
     <span class="hljs-attr">"validate:es5"</span>: <span class="hljs-string">"es5-validator ./app/scripts/*.js"</span>,
  &#125;,
  <span class="hljs-attr">"devDependencies"</span>: &#123;
    <span class="hljs-attr">"es5-validator"</span>: <span class="hljs-string">"^1.0.8"</span>,
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d8a25f5e6b94880bfb683aa0aa9997f~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            