
---
title: '如何做到修改了node_module中的包，却不受重新安装的影响'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/969fdd2d03024b92be31997817d3a435~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 26 Apr 2021 23:32:17 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/969fdd2d03024b92be31997817d3a435~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">背景</h1>
<blockquote>
<p>我们常常会遇到一个问题，网上现有的开源插件并不能满足我们实际项目的预期。但如果只需要对源码进行小小的改动就能满足我们的需求，那改源码一定是首选</p>
</blockquote>
<h1 data-id="heading-1">前言</h1>
<p>修改别人的源码往往有这几个方式：</p>
<ol>
<li>直接在项目的node_modules下找到插件的源码直接修改；
<ul>
<li>优点：简单直接、快速见效</li>
<li>缺点：不能持久化，一旦重新安装就失效；不方便团队成员使用修改后的代码</li>
</ul>
</li>
<li>去github上fork代码到自己的仓库进行修改，并将自己修改过后的代码发布到npm上使用；
<ul>
<li>优点：团队成员都可以使用到这份修改的代码</li>
<li>缺点：麻烦、十分麻烦</li>
</ul>
</li>
</ol>
<p>显而易见，上面这两种方法既不优雅，也不可靠。作为程序员的我们岂能被这事儿给难住，开源社区早已给我们准备好了解决方案：<a href="https://github.com/ds300/patch-package" target="_blank" rel="nofollow noopener noreferrer">patch-package</a></p>
<h1 data-id="heading-2">使用补丁</h1>
<p>通过cra开启一个项目</p>
<pre><code class="hljs language-shell copyable" lang="shell">npx create-react-app my-app
cd my-app
npm start
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给项目@alifd/next（ui库）、patch-package、postinstall-postinstall（使用yarn安装时需要安装，npm无需安装此依赖）</p>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add @alifd/next patch-package postinstall-postinstall -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给 package.json文件中添加脚本命令（<strong>非常重要</strong>）</p>
<pre><code class="hljs language-json copyable" lang="json"> <span class="hljs-string">"scripts"</span>: &#123;
+  <span class="hljs-attr">"postinstall"</span>: <span class="hljs-string">"patch-package"</span>
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们引入组件button，并查看组件当前结构</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/969fdd2d03024b92be31997817d3a435~tplv-k3u1fbpfcp-watermark.image" alt="situation.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们去node_module中修改button源码</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/380985cd1ddf4083ac31cab1692a8642~tplv-k3u1fbpfcp-watermark.image" alt="revise.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们在看看页面情况（如果没有效果的话，可以重启一下服务 ）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a4c6d7f2488439795a878253467d95f~tplv-k3u1fbpfcp-watermark.image" alt="result.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>修改完并且也生效了，我们就要开始打补丁了，运行命令<code>yarn patch-package package-name</code></p>
<pre><code class="hljs language-shell copyable" lang="shell">yarn patch-package @alifd/next
<span class="copy-code-btn">复制代码</span></code></pre>
<p>成功后你会看到根目录多了一个patches文件夹，里面包含了你修改的npm包的patch文件。点开可以很清楚的看到你都做了哪些修改</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/675c574a8ec74c5b94542b7a1c23f059~tplv-k3u1fbpfcp-watermark.image" alt="patch.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">测试</h1>
<p>删除node_module并重新安装</p>
<pre><code class="hljs language-shell copyable" lang="shell">rm -rf node_modules/ && yarn
<span class="copy-code-btn">复制代码</span></code></pre>
<p>依赖包安装时候可以在命令行中看到补丁的应用</p>
<pre><code class="hljs language-shell copyable" lang="shell">yarn install v1.22.4
[1/4] 🔍  Resolving packages...
[2/4] 🚚  Fetching packages...
[3/4] 🔗  Linking dependencies...
warning " > @testing-library/user-event@12.8.3" has unmet peer dependency "@testing-library/dom@>=7.21.4".
warning "react-scripts > @typescript-eslint/eslint-plugin > tsutils@3.21.0" has unmet peer dependency "typescript@>=2.8.0 || >= 3.2.0-dev || >= 3.3.0-dev || >= 3.4.0-dev || >= 3.5.0-dev || >= 3.6.0-dev || >= 3.6.0-beta || >= 3.7.0-dev || >= 3.7.0-beta".
warning " > @alifd/next@1.22.21" has unmet peer dependency "@alifd/meet-react@^2.0.0".
warning " > @alifd/next@1.22.21" has unmet peer dependency "moment@^2.22.1".
warning " > @alifd/next@1.22.21" has incorrect peer dependency "react@^16.0.0".
warning " > @alifd/next@1.22.21" has incorrect peer dependency "react-dom@^16.0.0".
[4/4] 🔨  Building fresh packages...
<span class="hljs-meta">$</span><span class="bash"> patch-package</span>
patch-package 6.4.7
Applying patches...
@alifd/next@1.22.21 ✔
✨  Done in 20.10s.
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>yarn start</code>重新启动，查看审查元素，依旧是a标签！</p>
<h1 data-id="heading-4">结束</h1>
<p>这篇文章非常的简短，但是实用性非常高，如果这篇文章给了你启发或帮助，那就点个赞吧！😊</p></div>  
</div>
            