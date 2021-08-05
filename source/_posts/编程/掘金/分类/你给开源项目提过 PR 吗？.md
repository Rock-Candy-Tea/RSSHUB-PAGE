
---
title: '你给开源项目提过 PR 吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00e4a392e8ff4f63aa75d457a5f78057~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 16:45:52 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00e4a392e8ff4f63aa75d457a5f78057~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>”</p>
<p>你有给开源的库或者框架提过 PR 吗？</p>
<p>如果没有，那么今天的文章会教你怎么给开源库提 PR。</p>
<h2 data-id="heading-0">为什么要给开源项目提 PR？</h2>
<p>这件事还得从好几年前（2019年）说起，那时候在折腾一个虚拟 DOM 的玩具（参考之前的文章：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.shenfq.com%2Fposts%2F2019%2F%25E8%2599%259A%25E6%258B%259FDOM%25E5%2588%25B0%25E5%25BA%2595%25E6%2598%25AF%25E4%25BB%2580%25E4%25B9%2588%25EF%25BC%259F.html" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.shenfq.com/posts/2019/%E8%99%9A%E6%8B%9FDOM%E5%88%B0%E5%BA%95%E6%98%AF%E4%BB%80%E4%B9%88%EF%BC%9F.html" ref="nofollow noopener noreferrer">🔗虚拟DOM到底是什么？</a>），作为一个标准的前端工程，构建工具、Lint 工具、代码格式化都是必不可少的。</p>
<p>在构建工具上我选择了 <code>Rollup</code>，希望每次构建的时候都能自动进行代码的 Lint，所以引入了 <code>Rollup</code> 的一个插件：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FShenfq%2Frollup-plugin-eslint" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Shenfq/rollup-plugin-eslint" ref="nofollow noopener noreferrer"><code>rollup-plugin-eslint</code></a>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00e4a392e8ff4f63aa75d457a5f78057~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在使用这个插件的过程中，发现和 <code>Webpack</code> 对应的插件 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack-contrib%2Feslint-webpack-plugin" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack-contrib/eslint-webpack-plugin" ref="nofollow noopener noreferrer"><code>eslint-webpack-plugin</code></a> 还是有一些差距的。我在使用 <code>Webpack</code> 的 <code>eslint-webpack-plugin</code> 时候，只需要配置 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack-contrib%2Feslint-webpack-plugin%23fix" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack-contrib/eslint-webpack-plugin#fix" ref="nofollow noopener noreferrer"><code>fix</code> 属性</a>，就能够在保存代码的时候，自动对代码进行 fix。</p>
<pre><code class="copyable">// webpack.config.js
const ESLintPlugin = require('eslint-webpack-plugin');
​
module.exports = &#123;
  // ...
  plugins: [
    new ESLintPlugin(&#123;
      fix: true,
      extensions: ['js', 'jsx']
    &#125;)
&#125;;
​
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f70afee95040484283144205c8adc981~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>而在使用 <code>rollup-plugin-eslint</code> 的时候，看文档上，好像没有提到这个选项，也就是说 <code>rollup-plugin-eslint</code> 根本不支持这个功能。然后，搜索了一下 Issues，不搜不要紧，一搜吓一跳，发现有人在 2016 年就提出了这个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FTrySound%2Frollup-plugin-eslint%2Fissues%2F1" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/TrySound/rollup-plugin-eslint/issues/1" ref="nofollow noopener noreferrer">疑问😳</a>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7db2d6241faa4ed49e47fa466ef3ddbf~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>作者的回复也很简单，欢迎提交 PR。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3dc78fd076c9464cbc7c43c8607a3e4f~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我当时心想，这个功能这么久了都没人实现想必很难吧。但是隔壁的 <code>eslint-webpack-plugin</code> 明明支持这个功能，我去看看它怎么实现的不就行了🐶。</p>
<p>于是，我就把 <code>eslint-webpack-plugin</code> 的代码 clone 下来一顿搜索，发现它实现这个功能就用了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack-contrib%2Feslint-webpack-plugin%2Fblob%2FHEAD%2Fsrc%2FgetESLint.js%23L38-L40" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack-contrib/eslint-webpack-plugin/blob/HEAD/src/getESLint.js#L38-L40" ref="nofollow noopener noreferrer">三行代码</a>。</p>
<pre><code class="copyable">if (options.fix) &#123;
  await ESLint.outputFixes(results);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>激动的心，颤抖的手，我赶忙就去 <code>rollup-plugin-eslint</code> 那里提了个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FTrySound%2Frollup-plugin-eslint%2Fpull%2F27%2Ffiles%23diff-e727e4bdf3657fd1d798edcd6b099d6e092f8573cba266154583a746bba0f346" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/TrySound/rollup-plugin-eslint/pull/27/files#diff-e727e4bdf3657fd1d798edcd6b099d6e092f8573cba266154583a746bba0f346" ref="nofollow noopener noreferrer">PR</a>。</p>
<blockquote>
<p>🔗PR: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FTrySound%2Frollup-plugin-eslint%2Fpull%2F27" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/TrySound/rollup-plugin-eslint/pull/27" ref="nofollow noopener noreferrer">github.com/TrySound/ro…</a></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01a159d9f7c249bd82d432db2425db25~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>关键是，作者都没想到这个东西居然这么简单就实现了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ca6f7fe20e9495e9d50ea848d01f321~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">如何在 GitHub 上提 PR？</h2>
<p>上面是我第一次提 PR 的一个心路历程，如果你也发现了你现在使用的什么开源框架有待优化的地方，这里再教大家怎么在 GitHub 上提交一个 PR。</p>
<h4 data-id="heading-2">对开源项目进行 Fork</h4>
<p>首先把你要提交 PR 的项目 Fork 到自己的仓库。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5280290a89e34652a61dacace2abf21b~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后到自己的仓库中，将 Fork 的项目 clone 到本地。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b73e734557d2472da1d27b4f7381bcaf~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">$ git clone git@github.com:Shenfq/rollup-plugin-eslint.git
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">切换到新分支，提交变更，推送到远程</h4>
<p>代码 clone 到本地之后，先切换一个新的分支，分支名最好紧贴这次更新的内容。</p>
<pre><code class="copyable">$ git checkout -b feature/add-fix-option
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在新分支修改代码：</p>
<pre><code class="copyable">+  if (options.fix && report) &#123;
+    CLIEngine.outputFixes(report);
+  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提交变更：</p>
<pre><code class="copyable">$ git add .
$ git commit -m "feat: add options.fix"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后将新的分支推送到远程：</p>
<pre><code class="copyable">$ git push --set-upstream origin feature/add-fix-option
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">新建 PR</h4>
<p>在自己的 GitHub 仓库中找到对应项目，打开 <code>Pull requests</code> Tab，点击 <code>New pull request</code> 按钮，新建一个 PR。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1446fa24e4a64e8e801db2964511fb9f~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后，在下面的界面中，选择刚刚提交的分支，最后点击 <code>Create pull request</code> 即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8184c71bf73944dc98f0427805687d92~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击之后，就在对应的项目中提交了一个属于你的 PR 了。如果顺利的话，你就能『混』 到一个开源项目贡献者的头衔。</p>
<p>\</p></div>  
</div>
            