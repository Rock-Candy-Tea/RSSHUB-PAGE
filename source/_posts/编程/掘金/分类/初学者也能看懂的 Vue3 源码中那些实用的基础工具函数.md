
---
title: '初学者也能看懂的 Vue3 源码中那些实用的基础工具函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0fc7a2f661942b1a6879a0e002ef8ff~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 17:20:48 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0fc7a2f661942b1a6879a0e002ef8ff~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">1. 前言</h2>
<p>大家好，我是<a href="https://link.juejin.cn/?target=https%3A%2F%2Flxchuan12.gitee.io" target="_blank" rel="nofollow noopener noreferrer" title="https://lxchuan12.gitee.io" ref="nofollow noopener noreferrer">若川</a>。欢迎关注我的<a href="https://user-gold-cdn.xitu.io/2019/12/13/16efe57ddc7c9eb3?imageView2/0/w/1280/h/960/format/webp/ignore-error/1" title="https://user-gold-cdn.xitu.io/2019/12/13/16efe57ddc7c9eb3?imageView2/0/w/1280/h/960/format/webp/ignore-error/1" target="_blank">公众号若川视野</a>，最近组织了<strong>源码共读</strong>活动，感兴趣的可以加我微信 <code>ruochuan12</code>，长期交流学习。</p>
<p>之前写的<a href="https://juejin.cn/column/6960551178908205093" target="_blank" title="https://juejin.cn/column/6960551178908205093">《学习源码整体架构系列》</a> 包含<code>jQuery</code>、<code>underscore</code>、<code>lodash</code>、<code>vuex</code>、<code>sentry</code>、<code>axios</code>、<code>redux</code>、<code>koa</code>、<code>vue-devtools</code>、<code>vuex4</code>十篇源码文章。</p>
<p>写相对很难的源码，耗费了自己的时间和精力，也没收获多少阅读点赞，其实是一件挺受打击的事情。从阅读量和读者受益方面来看，不能促进作者持续输出文章。</p>
<p>所以转变思路，写一些相对通俗易懂的文章。<strong>其实源码也不是想象的那么难，至少有很多看得懂。比如工具函数</strong>。本文通过学习<code>Vue3</code>源码中的工具函数模块的源码，学习源码为自己所用。歌德曾说：读一本好书，就是在和高尚的人谈话。
同理可得：读源码，也算是和作者的一种学习交流的方式。</p>
<p>阅读本文，你将学到：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span> 如何学习 JavaScript 基础知识，会推荐很多学习资料
<span class="hljs-number">2.</span> 如何学习调试 Vue <span class="hljs-number">3</span> 源码
<span class="hljs-number">3.</span> 如何学习源码中优秀代码和思想，投入到自己的项目中
<span class="hljs-number">4.</span> Vue <span class="hljs-number">3</span> 源码 shared 模块中的几十个实用工具函数
<span class="hljs-number">5.</span> 我的一些经验分享
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>shared</code>模块中<code>57个</code>工具函数，本次阅读其中的<code>30余个</code>。</p>
<h2 data-id="heading-1">2. 环境准备</h2>
<h3 data-id="heading-2">2.1 读开源项目 贡献指南</h3>
<p>打开 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue-next" ref="nofollow noopener noreferrer">vue-next</a>，
开源项目一般都能在 <code>README.md</code> 或者 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fblob%2Fmaster%2F.github%2Fcontributing.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue-next/blob/master/.github/contributing.md" ref="nofollow noopener noreferrer">.github/contributing.md</a> 找到贡献指南。</p>
<p>而贡献指南写了很多关于参与项目开发的信息。比如怎么跑起来，项目目录结构是怎样的。怎么投入开发，需要哪些知识储备等。</p>
<p>我们可以在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fblob%2Fmaster%2F.github%2Fcontributing.md%23project-structure" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue-next/blob/master/.github/contributing.md#project-structure" ref="nofollow noopener noreferrer">项目目录结构</a> 描述中，找到<code>shared</code>模块。</p>
<p><code>shared</code>: Internal utilities shared across multiple packages (especially environment-agnostic utils used by both runtime and compiler packages).</p>
<p><code>README.md</code> 和 <code>contributing.md</code> 一般都是英文的。可能会难倒一部分人。其实看不懂，完全可以可以借助划词翻译，整页翻译和百度翻译等翻译工具。再把英文加入后续学习计划。</p>
<p>本文就是讲<code>shared</code>模块，对应的文件路径是：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fblob%2Fmaster%2Fpackages%2Fshared%2Fsrc%2Findex.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue-next/blob/master/packages/shared/src/index.ts" ref="nofollow noopener noreferrer"><code>vue-next/packages/shared/src/index.ts</code></a></p>
<p>也可以用<code>github1s</code>访问，速度更快。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub1s.com%2Fvuejs%2Fvue-next%2Fblob%2Fmaster%2Fpackages%2Fshared%2Fsrc%2Findex.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github1s.com/vuejs/vue-next/blob/master/packages/shared/src/index.ts" ref="nofollow noopener noreferrer">github1s packages/shared/src/index.ts</a></p>
<h3 data-id="heading-3">2.2 按照项目指南 打包构建代码</h3>
<p>为了降低文章难度，我按照贡献指南中方法打包把<code>ts</code>转成了<code>js</code>。如果你需要打包，也可以参考下文打包构建。</p>
<p>你需要确保 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fnodejs.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://nodejs.org/" ref="nofollow noopener noreferrer">Node.js</a> 版本是 <code>10+</code>, 而且 <code>yarn</code> 的版本是 <code>1.x</code> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fyarnpkg.com%2Fen%2Fdocs%2Finstall" target="_blank" rel="nofollow noopener noreferrer" title="https://yarnpkg.com/en/docs/install" ref="nofollow noopener noreferrer">Yarn 1.x</a>。</p>
<p>你安装的 <code>Node.js</code> 版本很可能是低于 <code>10</code>。最简单的办法就是去官网重新安装。也可以使用 <code>nvm</code>等管理<code>Node.js</code>版本。</p>
<pre><code class="hljs language-bash copyable" lang="bash">node -v
<span class="hljs-comment"># v14.16.0</span>
<span class="hljs-comment"># 全局安装 yarn</span>
<span class="hljs-comment"># 克隆项目</span>
git <span class="hljs-built_in">clone</span> https://github.com/vuejs/vue-next.git
<span class="hljs-built_in">cd</span> vue-next

<span class="hljs-comment"># 或者克隆我的项目</span>
git <span class="hljs-built_in">clone</span> https://github.com/lxchuan12/vue-next-analysis.git
<span class="hljs-built_in">cd</span> vue-next-analysis

npm install --global yarn
yarn <span class="hljs-comment"># install the dependencies of the project</span>
<span class="hljs-comment"># yarn —ignore-scripts 忽略一些安装，更快速</span>
yarn build
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以得到 <code>vue-next/packages/shared/dist/shared.esm-bundler.js</code>，文件也就是纯<code>js</code>文件。也接下就是解释其中的一些方法。</p>
<blockquote>
<p>当然，前面可能比较啰嗦。我可以直接讲 <code>3. 工具函数</code>。但通过我上文的介绍，即使是初学者，都能看懂一些开源项目源码，也许就会有一定的成就感。
另外，面试问到被类似的问题或者笔试题时，你说看<code>Vue3</code>源码学到的，面试官绝对对你刮目相看。</p>
</blockquote>
<h3 data-id="heading-4">2.3 如何生成 sourcemap 调试 vue-next 源码</h3>
<p>熟悉我的读者知道，我是经常强调生成<code>sourcemap</code>调试看源码，所以顺便提一下如何配置生成<code>sourcemap</code>，如何调试。这部分可以简单略过，动手操作时再仔细看。</p>
<p>其实<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fblob%2Fmaster%2F.github%2Fcontributing.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue-next/blob/master/.github/contributing.md" ref="nofollow noopener noreferrer">贡献指南</a>里描述了。</p>
<blockquote>
<p>Build with Source Maps
Use the <code>--sourcemap</code> or <code>-s</code> flag to build with source maps. Note this will make the build much slower.</p>
</blockquote>
<p>所以在 <code>vue-next/package.json</code> 追加 <code>"dev:sourcemap": "node scripts/dev.js --sourcemap"</code>，<code>yarn dev:sourcemap</code>执行，即可生成<code>sourcemap</code>，或者直接 <code>build</code>。</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// package.json</span>
&#123;
    <span class="hljs-attr">"version"</span>: <span class="hljs-string">"3.2.1"</span>,
    <span class="hljs-attr">"scripts"</span>: &#123;
        <span class="hljs-attr">"dev:sourcemap"</span>: <span class="hljs-string">"node scripts/dev.js --sourcemap"</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会在控制台输出类似<code>vue-next/packages/vue/src/index.ts → packages/vue/dist/vue.global.js</code>的信息。</p>
<p>其中<code>packages/vue/dist/vue.global.js.map</code> 就是<code>sourcemap</code>文件了。</p>
<p>我们在 Vue3官网找个例子，在 <code>vue-next/examples/index.html</code>。其内容引入<code>packages/vue/dist/vue.global.js</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue-next/examples/index.html</span>
<script src=<span class="hljs-string">"../../packages/vue/dist/vue.global.js"</span>></script>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">const</span> Counter = &#123;
        <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-attr">counter</span>: <span class="hljs-number">0</span>
            &#125;
        &#125;
    &#125;

    Vue.createApp(Counter).mount(<span class="hljs-string">'#counter'</span>)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们新建一个终端窗口，<code>yarn serve</code>，在浏览器中打开<code>http://localhost:5000/examples/</code>，如下图所示，按<code>F11</code>等进入函数，就可以愉快的调试源码了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0fc7a2f661942b1a6879a0e002ef8ff~tplv-k3u1fbpfcp-watermark.image" alt="vue-next-debugger.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">3. 工具函数</h2>
<p>本文主要按照源码 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fblob%2Fmaster%2Fpackages%2Fshared%2Fsrc%2Findex.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue-next/blob/master/packages/shared/src/index.ts" ref="nofollow noopener noreferrer"><code>vue-next/packages/shared/src/index.ts</code></a> 的顺序来写。也省去了一些从外部导入的方法。</p>
<p>我们也可以通过<code>ts</code>文件，查看使用函数的位置。同时在<code>VSCode</code>运行调试JS代码，我们比较推荐韩老师写的<code>code runner</code>插件。</p>
<h3 data-id="heading-6">3.1 babelParserDefaultPlugins  babel 解析默认插件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * List of <span class="hljs-doctag">@babel</span>/parser plugins that are used for template expression
 * transforms and SFC script transforms. By default we enable proposals slated
 * for ES2020. This will need to be updated as the spec moves forward.
 * Full list at https://babeljs.io/docs/en/next/babel-parser#plugins
 */</span>
<span class="hljs-keyword">const</span> babelParserDefaultPlugins = [
    <span class="hljs-string">'bigInt'</span>,
    <span class="hljs-string">'optionalChaining'</span>,
    <span class="hljs-string">'nullishCoalescingOperator'</span>
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里就是几个默认插件。感兴趣看英文注释查看。</p>
<h3 data-id="heading-7">3.2 EMPTY_OBJ 空对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> EMPTY_OBJ = (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>)
    ? <span class="hljs-built_in">Object</span>.freeze(&#123;&#125;)
    : &#123;&#125;;

<span class="hljs-comment">// 例子：</span>
<span class="hljs-comment">// Object.freeze 是 冻结对象</span>
<span class="hljs-comment">// 冻结的对象最外层无法修改。</span>
<span class="hljs-keyword">const</span> EMPTY_OBJ_1 = <span class="hljs-built_in">Object</span>.freeze(&#123;&#125;);
EMPTY_OBJ_1.name = <span class="hljs-string">'若川'</span>;
<span class="hljs-built_in">console</span>.log(EMPTY_OBJ_1.name); <span class="hljs-comment">// undefined</span>

<span class="hljs-keyword">const</span> EMPTY_OBJ_2 = <span class="hljs-built_in">Object</span>.freeze(&#123; <span class="hljs-attr">props</span>: &#123; <span class="hljs-attr">mp</span>: <span class="hljs-string">'若川视野'</span> &#125; &#125;);
EMPTY_OBJ_2.props.name = <span class="hljs-string">'若川'</span>;
EMPTY_OBJ_2.props2 = <span class="hljs-string">'props2'</span>;
<span class="hljs-built_in">console</span>.log(EMPTY_OBJ_2.props.name); <span class="hljs-comment">// '若川'</span>
<span class="hljs-built_in">console</span>.log(EMPTY_OBJ_2.props2); <span class="hljs-comment">// undefined</span>
<span class="hljs-built_in">console</span>.log(EMPTY_OBJ_2);
<span class="hljs-comment">/**
 * 
 * &#123; 
 *  props: &#123;
     mp: "若川视野",
     name: "若川"
    &#125;
 * &#125;
 * */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>process.env.NODE_ENV</code> 是 <code>node</code> 项目中的一个环境变量，一般定义为：<code>development</code> 和<code>production</code>。根据环境写代码。比如开发环境，有报错等信息，生产环境则不需要这些报错警告。</p>
<h3 data-id="heading-8">3.3 EMPTY_ARR 空数组</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> EMPTY_ARR = (process.env.NODE_ENV !== <span class="hljs-string">'production'</span>) ? <span class="hljs-built_in">Object</span>.freeze([]) : [];

<span class="hljs-comment">// 例子：</span>
EMPTY_ARR.push(<span class="hljs-number">1</span>) <span class="hljs-comment">// 报错，也就是为啥生产环境还是用 []</span>
EMPTY_ARR.length = <span class="hljs-number">3</span>;
<span class="hljs-built_in">console</span>.log(EMPTY_ARR.length); <span class="hljs-comment">// 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">3.4 NOOP 空函数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> NOOP = <span class="hljs-function">() =></span> &#123; &#125;;

<span class="hljs-comment">// 很多库的源码中都有这样的定义函数，比如 jQuery、underscore、lodash 等</span>
<span class="hljs-comment">// 使用场景：1. 方便判断， 2. 方便压缩</span>
<span class="hljs-comment">// 1. 比如：</span>
<span class="hljs-keyword">const</span> instance = &#123;
    <span class="hljs-attr">render</span>: NOOP
&#125;;

<span class="hljs-comment">// 条件</span>
<span class="hljs-keyword">const</span> dev = <span class="hljs-literal">true</span>;
<span class="hljs-keyword">if</span>(dev)&#123;
    instance.render = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'render'</span>);
    &#125;
&#125;

<span class="hljs-comment">// 可以用作判断。</span>
<span class="hljs-keyword">if</span>(instance.render === NOOP)&#123;
 <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'i'</span>);
&#125;
<span class="hljs-comment">// 2. 再比如：</span>
<span class="hljs-comment">// 方便压缩代码</span>
<span class="hljs-comment">// 如果是 function()&#123;&#125; ，不方便压缩代码</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">3.5 NO 永远返回 false 的函数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * Always return false.
 */</span>
<span class="hljs-keyword">const</span> NO = <span class="hljs-function">() =></span> <span class="hljs-literal">false</span>;

<span class="hljs-comment">// 除了压缩代码的好处外。</span>
<span class="hljs-comment">// 一直返回 false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">3.6 isOn 判断字符串是不是 on 开头，并且 on 后首字母不是小写字母</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> onRE = <span class="hljs-regexp">/^on[^a-z]/</span>;
<span class="hljs-keyword">const</span> isOn = <span class="hljs-function">(<span class="hljs-params">key</span>) =></span> onRE.test(key);

<span class="hljs-comment">// 例子：</span>
isOn(<span class="hljs-string">'onChange'</span>); <span class="hljs-comment">// true</span>
isOn(<span class="hljs-string">'onchange'</span>); <span class="hljs-comment">// false</span>
isOn(<span class="hljs-string">'on3change'</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>onRE</code> 是正则。<code>^</code>符号在开头，则表示是什么开头。而在其他地方是指非。</p>
<p>与之相反的是：<code>$</code>符合在结尾，则表示是以什么结尾。</p>
<p><code>[^a-z]</code>是指不是<code>a</code>到<code>z</code>的小写字母。</p>
<p>同时推荐一个正则在线工具。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fregex101.com" target="_blank" rel="nofollow noopener noreferrer" title="https://regex101.com" ref="nofollow noopener noreferrer">regex101</a></p>
<p>另外正则看老姚的迷你书就够用了。</p>
<p><a href="https://juejin.cn/post/6844903501034684430" target="_blank" title="https://juejin.cn/post/6844903501034684430">老姚：《JavaScript 正则表达式迷你书》问世了！</a></p>
<h3 data-id="heading-12">3.7 isModelListener 监听器</h3>
<p>判断字符串是不是以<code>onUpdate:</code>开头</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> isModelListener = <span class="hljs-function">(<span class="hljs-params">key</span>) =></span> key.startsWith(<span class="hljs-string">'onUpdate:'</span>);

<span class="hljs-comment">// 例子：</span>
isModelListener(<span class="hljs-string">'onUpdate:change'</span>); <span class="hljs-comment">// true</span>
isModelListener(<span class="hljs-string">'1onUpdate:change'</span>); <span class="hljs-comment">// false</span>
<span class="hljs-comment">// startsWith 是 ES6 提供的方法</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fes6.ruanyifeng.com%2F%23docs%2Fstring-methods" target="_blank" rel="nofollow noopener noreferrer" title="https://es6.ruanyifeng.com/#docs/string-methods" ref="nofollow noopener noreferrer">ES6入门教程：字符串的新增方法</a></p>
<p>很多方法都在《ES6入门教程》中有讲到，就不赘述了。</p>
<h3 data-id="heading-13">3.8 extend 继承 合并</h3>
<p>说合并可能更准确些。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> extend = <span class="hljs-built_in">Object</span>.assign;

<span class="hljs-comment">// 例子：</span>
<span class="hljs-keyword">const</span> data = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'若川'</span> &#125;;
<span class="hljs-keyword">const</span> data2 = entend(data, &#123; <span class="hljs-attr">mp</span>: <span class="hljs-string">'若川视野'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'是若川啊'</span> &#125;);
<span class="hljs-built_in">console</span>.log(data); <span class="hljs-comment">// &#123; name: "是若川啊", mp: "若川视野" &#125;</span>
<span class="hljs-built_in">console</span>.log(data2); <span class="hljs-comment">// &#123; name: "是若川啊", mp: "若川视野" &#125;</span>
<span class="hljs-built_in">console</span>.log(data === data2); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">3.9 remove 移除数组的一项</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> remove = <span class="hljs-function">(<span class="hljs-params">arr, el</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> i = arr.indexOf(el);
    <span class="hljs-keyword">if</span> (i > -<span class="hljs-number">1</span>) &#123;
        arr.splice(i, <span class="hljs-number">1</span>);
    &#125;
&#125;;

<span class="hljs-comment">// 例子：</span>
<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
remove(arr, <span class="hljs-number">3</span>);
<span class="hljs-built_in">console</span>.log(arr); <span class="hljs-comment">// [1, 2]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>splice</code> 其实是一个很耗性能的方法。删除数组中的一项，其他元素都要移动位置。</p>
<p><strong>引申</strong>：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Faxios%2Faxios%2Fblob%2Fmaster%2Flib%2Fcore%2FInterceptorManager.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/axios/axios/blob/master/lib/core/InterceptorManager.js" ref="nofollow noopener noreferrer"><code>axios InterceptorManager</code> 拦截器源码</a> 中，拦截器用数组存储的。但实际移除拦截器时，只是把拦截器置为 <code>null</code> 。而不是用<code>splice</code>移除。最后执行时为 <code>null</code> 的不执行，同样效果。<code>axios</code> 拦截器这个场景下，不得不说为性能做到了很好的考虑。</p>
<p>看如下 <code>axios</code> 拦截器代码示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 代码有删减</span>
<span class="hljs-comment">// 声明</span>
<span class="hljs-built_in">this</span>.handlers = [];

<span class="hljs-comment">// 移除</span>
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.handlers[id]) &#123;
    <span class="hljs-built_in">this</span>.handlers[id] = <span class="hljs-literal">null</span>;
&#125;

<span class="hljs-comment">// 执行</span>
<span class="hljs-keyword">if</span> (h !== <span class="hljs-literal">null</span>) &#123;
    fn(h);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">3.10 hasOwn 是不是自己本身所拥有的属性</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> hasOwnProperty = <span class="hljs-built_in">Object</span>.prototype.hasOwnProperty;
<span class="hljs-keyword">const</span> hasOwn = <span class="hljs-function">(<span class="hljs-params">val, key</span>) =></span> hasOwnProperty.call(val, key);

<span class="hljs-comment">// 例子：</span>

<span class="hljs-comment">// 特别提醒：__proto__ 是浏览器实现的原型写法，后面还会用到</span>
<span class="hljs-comment">// 现在已经有提供好几个原型相关的API</span>
<span class="hljs-comment">// Object.getPrototypeOf</span>
<span class="hljs-comment">// Object.setPrototypeOf</span>
<span class="hljs-comment">// Object.isPrototypeOf</span>

<span class="hljs-comment">// .call 则是函数里 this 显示指定以为第一个参数，并执行函数。</span>

hasOwn(&#123;<span class="hljs-attr">__proto__</span>: &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125;&#125;, <span class="hljs-string">'a'</span>) <span class="hljs-comment">// false</span>
hasOwn(&#123; <span class="hljs-attr">a</span>: <span class="hljs-literal">undefined</span> &#125;, <span class="hljs-string">'a'</span>) <span class="hljs-comment">// true</span>
hasOwn(&#123;&#125;, <span class="hljs-string">'a'</span>) <span class="hljs-comment">// false</span>
hasOwn(&#123;&#125;, <span class="hljs-string">'hasOwnProperty'</span>) <span class="hljs-comment">// false</span>
hasOwn(&#123;&#125;, <span class="hljs-string">'toString'</span>) <span class="hljs-comment">// false</span>
<span class="hljs-comment">// 是自己的本身拥有的属性，不是通过原型链向上查找的。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对象API可以看我之前写的一篇文章<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FY3nL3GPcxiqb3zK6pEuycg" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/Y3nL3GPcxiqb3zK6pEuycg" ref="nofollow noopener noreferrer">JavaScript 对象所有API解析</a>，写的还算全面。</p>
<h3 data-id="heading-16">3.11 isArray 判断数组</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> isArray = <span class="hljs-built_in">Array</span>.isArray;

isArray([]); <span class="hljs-comment">// true</span>
<span class="hljs-keyword">const</span> fakeArr = &#123; <span class="hljs-attr">__proto__</span>: <span class="hljs-built_in">Array</span>.prototype, <span class="hljs-attr">length</span>: <span class="hljs-number">0</span> &#125;;
isArray(fakeArr); <span class="hljs-comment">// false</span>
fakeArr <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>; <span class="hljs-comment">// true</span>
<span class="hljs-comment">// 所以 instanceof 这种情况 不准确</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">3.12 isMap 判断是不是 Map 对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> isMap = <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> toTypeString(val) === <span class="hljs-string">'[object Map]'</span>;

<span class="hljs-comment">// 例子：</span>
<span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
<span class="hljs-keyword">const</span> o = &#123; <span class="hljs-attr">p</span>: <span class="hljs-string">'Hello World'</span> &#125;;

map.set(o, <span class="hljs-string">'content'</span>);
map.get(o); <span class="hljs-comment">// 'content'</span>
isMap(map); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>ES6 提供了 Map 数据结构。它类似于对象，也是键值对的集合，但是“键”的范围不限于字符串，各种类型的值（包括对象）都可以当作键。也就是说，Object 结构提供了“字符串—值”的对应，Map 结构提供了“值—值”的对应，是一种更完善的 Hash 结构实现。如果你需要“键值对”的数据结构，Map 比 Object 更合适。</p>
</blockquote>
<h3 data-id="heading-18">3.13 isSet 判断是不是 Set 对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> isSet = <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> toTypeString(val) === <span class="hljs-string">'[object Set]'</span>;

<span class="hljs-comment">// 例子：</span>
<span class="hljs-keyword">const</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
isSet(set); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>ES6</code> 提供了新的数据结构 <code>Set</code>。它类似于数组，但是成员的值都是唯一的，没有重复的值。</p>
</blockquote>
<p><code>Set</code>本身是一个构造函数，用来生成 <code>Set</code> 数据结构。</p>
<h3 data-id="heading-19">3.14 isDate 判断是不是 Date 对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> isDate = <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> val <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Date</span>;

<span class="hljs-comment">// 例子：</span>
isDate(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()); <span class="hljs-comment">// true</span>

<span class="hljs-comment">// `instanceof` 操作符左边是右边的实例。但不是很准，但一般够用了。原理是根据原型链向上查找的。</span>

isDate(&#123;<span class="hljs-attr">__proto__</span> : <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()); <span class="hljs-comment">// true</span>
<span class="hljs-comment">// 实际上是应该是 Object 才对。</span>
<span class="hljs-comment">// 所以用 instanceof 判断数组也不准确。</span>
<span class="hljs-comment">// 再比如</span>
(&#123;<span class="hljs-attr">__proto__</span>: [] &#125;) <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>; <span class="hljs-comment">// true</span>
<span class="hljs-comment">// 实际上是对象。</span>
<span class="hljs-comment">// 所以用 数组本身提供的方法 Array.isArray 是比较准确的。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">3.15 isFunction 判断是不是函数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> isFunction = <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> <span class="hljs-keyword">typeof</span> val === <span class="hljs-string">'function'</span>;
<span class="hljs-comment">// 判断数组有多种方法，但这个是比较常用也相对兼容性好的。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">3.16 isString 判断是不是字符串</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> isString = <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> <span class="hljs-keyword">typeof</span> val === <span class="hljs-string">'string'</span>;

<span class="hljs-comment">// 例子：</span>
isString(<span class="hljs-string">''</span>) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">3.17 isSymbol 判断是不是 Symbol</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> isSymbol = <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> <span class="hljs-keyword">typeof</span> val === <span class="hljs-string">'symbol'</span>;

<span class="hljs-comment">// 例子：</span>
<span class="hljs-keyword">let</span> s = <span class="hljs-built_in">Symbol</span>();

<span class="hljs-keyword">typeof</span> s;
<span class="hljs-comment">// "symbol"</span>
<span class="hljs-comment">// Symbol 是函数，不需要用 new 调用。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>ES6</code> 引入了一种新的原始数据类型<code>Symbol</code>，表示独一无二的值。</p>
</blockquote>
<h3 data-id="heading-23">3.18 isObject 判断是不是对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> isObject = <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> val !== <span class="hljs-literal">null</span> && <span class="hljs-keyword">typeof</span> val === <span class="hljs-string">'object'</span>;

<span class="hljs-comment">// 例子：</span>
isObject(<span class="hljs-literal">null</span>); <span class="hljs-comment">// false</span>
isObject(&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'若川'</span>&#125;); <span class="hljs-comment">// true</span>
<span class="hljs-comment">// 判断不为 null 的原因是 typeof null 其实 是 object</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">3.19 isPromise 判断是不是 Promise</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> isPromise = <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> isObject(val) && isFunction(val.then) && isFunction(val.catch);
&#125;;

<span class="hljs-comment">// 判断是不是Promise对象</span>
<span class="hljs-keyword">const</span> p1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>)</span>&#123;
  resolve(<span class="hljs-string">'若川'</span>);
&#125;);
isPromise(p1); <span class="hljs-comment">// true</span>

<span class="hljs-comment">// promise 对于初学者来说可能比较难理解。但是重点内容，JS异步编程，要着重掌握。</span>
<span class="hljs-comment">// 现在 web 开发 Promise 和 async await 等非常常用。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以根据文末推荐的书籍看<code>Promise</code>相关章节掌握。同时也推荐这本迷你书<a href="https://link.juejin.cn/?target=http%3A%2F%2Fliubin.org%2Fpromises-book%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://liubin.org/promises-book/" ref="nofollow noopener noreferrer">JavaScript Promise迷你书（中文版）</a></p>
<h3 data-id="heading-25">3.20 objectToString 对象转字符串</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> objectToString = <span class="hljs-built_in">Object</span>.prototype.toString;

<span class="hljs-comment">// 对象转字符串</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">3.21 toTypeString  对象转字符串</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> toTypeString = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> objectToString.call(value);

<span class="hljs-comment">// call 是一个函数，第一个参数是 执行函数里面 this 指向。</span>
<span class="hljs-comment">// 通过这个能获得 类似  "[object String]" 其中 String 是根据类型变化的</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">3.22 toRawType  对象转字符串 截取后几位</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> toRawType = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
    <span class="hljs-comment">// extract "RawType" from strings like "[object RawType]"</span>
    <span class="hljs-keyword">return</span> toTypeString(value).slice(<span class="hljs-number">8</span>, -<span class="hljs-number">1</span>);
&#125;;

<span class="hljs-comment">// 截取到</span>
toRawType(<span class="hljs-string">''</span>);  <span class="hljs-string">'String'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以 截取到 <code>String</code> <code>Array</code> 等这些类型</p>
<p>是 <code>JS</code> 判断数据类型非常重要的知识点。</p>
<p><code>JS</code> 判断类型也有  typeof ，但不是很准确，而且能够识别出的不多。</p>
<p>这些算是基础知识</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FOperators%2Ftypeof" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/typeof" ref="nofollow noopener noreferrer">mdn typeof 文档</a>，文档比较详细，也实现了一个很完善的<code>type</code>函数，本文就不赘述了。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// typeof 返回值目前有以下8种 </span>
<span class="hljs-string">'undefined'</span>
<span class="hljs-string">'object'</span>
<span class="hljs-string">'boolean'</span>
<span class="hljs-string">'number'</span>
<span class="hljs-string">'bigint'</span>
<span class="hljs-string">'string'</span>
<span class="hljs-string">'symobl'</span>
<span class="hljs-string">'function'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">3.23 isPlainObject 判断是不是纯粹的对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> objectToString = <span class="hljs-built_in">Object</span>.prototype.toString;
<span class="hljs-keyword">const</span> toTypeString = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> objectToString.call(value);
<span class="hljs-comment">// </span>
<span class="hljs-keyword">const</span> isPlainObject = <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> toTypeString(val) === <span class="hljs-string">'[object Object]'</span>;

<span class="hljs-comment">// 前文中 有 isObject 判断是不是对象了。</span>
<span class="hljs-comment">// isPlainObject 这个函数在很多源码里都有，比如 jQuery 源码和 lodash 源码等，具体实现不一样</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">3.24 isIntegerKey 判断是不是数字型的字符串key值</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> isIntegerKey = <span class="hljs-function">(<span class="hljs-params">key</span>) =></span> isString(key) &&
    key !== <span class="hljs-string">'NaN'</span> &&
    key[<span class="hljs-number">0</span>] !== <span class="hljs-string">'-'</span> &&
    <span class="hljs-string">''</span> + <span class="hljs-built_in">parseInt</span>(key, <span class="hljs-number">10</span>) === key;

<span class="hljs-comment">// 例子:</span>
isInegerKey(<span class="hljs-string">'a'</span>); <span class="hljs-comment">// false</span>
isInegerKey(<span class="hljs-string">'0'</span>); <span class="hljs-comment">// true</span>
isInegerKey(<span class="hljs-string">'011'</span>); <span class="hljs-comment">// false</span>
isInegerKey(<span class="hljs-string">'11'</span>); <span class="hljs-comment">// true</span>
<span class="hljs-comment">// 其中 parseInt 第二个参数是进制。</span>
<span class="hljs-comment">// 字符串能用数组取值的形式取值。</span>
<span class="hljs-comment">//  还有一个 charAt 函数，但不常用 </span>
<span class="hljs-string">'abc'</span>.charAt(<span class="hljs-number">0</span>) <span class="hljs-comment">// 'a'</span>
<span class="hljs-comment">// charAt 与数组形式不同的是 取不到值会返回空字符串''，数组形式取值取不到则是 undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">3.25 makeMap && isReservedProp</h3>
<p>传入一个以逗号分隔的字符串，生成一个 <code>map</code>(键值对)，并且返回一个函数检测 <code>key</code> 值在不在这个 <code>map</code> 中。第二个参数是小写选项。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * Make a map and return a function for checking if a key
 * is in that map.
 * IMPORTANT: all calls of this function must be prefixed with
 * \/\*#\_\_PURE\_\_\*\/
 * So that rollup can tree-shake them if necessary.
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeMap</span>(<span class="hljs-params">str, expectsLowerCase</span>) </span>&#123;
    <span class="hljs-keyword">const</span> map = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);
    <span class="hljs-keyword">const</span> list = str.split(<span class="hljs-string">','</span>);
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < list.length; i++) &#123;
        map[list[i]] = <span class="hljs-literal">true</span>;
    &#125;
    <span class="hljs-keyword">return</span> expectsLowerCase ? <span class="hljs-function"><span class="hljs-params">val</span> =></span> !!map[val.toLowerCase()] : <span class="hljs-function"><span class="hljs-params">val</span> =></span> !!map[val];
&#125;
<span class="hljs-keyword">const</span> isReservedProp = <span class="hljs-comment">/*#__PURE__*/</span> makeMap(
<span class="hljs-comment">// the leading comma is intentional so empty string "" is also included</span>
<span class="hljs-string">',key,ref,'</span> +
    <span class="hljs-string">'onVnodeBeforeMount,onVnodeMounted,'</span> +
    <span class="hljs-string">'onVnodeBeforeUpdate,onVnodeUpdated,'</span> +
    <span class="hljs-string">'onVnodeBeforeUnmount,onVnodeUnmounted'</span>);

<span class="hljs-comment">// 保留的属性</span>
isReservedProp(<span class="hljs-string">'key'</span>); <span class="hljs-comment">// true</span>
isReservedProp(<span class="hljs-string">'ref'</span>); <span class="hljs-comment">// true</span>
isReservedProp(<span class="hljs-string">'onVnodeBeforeMount'</span>); <span class="hljs-comment">// true</span>
isReservedProp(<span class="hljs-string">'onVnodeMounted'</span>); <span class="hljs-comment">// true</span>
isReservedProp(<span class="hljs-string">'onVnodeBeforeUpdate'</span>); <span class="hljs-comment">// true</span>
isReservedProp(<span class="hljs-string">'onVnodeUpdated'</span>); <span class="hljs-comment">// true</span>
isReservedProp(<span class="hljs-string">'onVnodeBeforeUnmount'</span>); <span class="hljs-comment">// true</span>
isReservedProp(<span class="hljs-string">'onVnodeUnmounted'</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">3.26 cacheStringFunction 缓存</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> cacheStringFunction = <span class="hljs-function">(<span class="hljs-params">fn</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> cache = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);
    <span class="hljs-keyword">return</span> (<span class="hljs-function">(<span class="hljs-params">str</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> hit = cache[str];
        <span class="hljs-keyword">return</span> hit || (cache[str] = fn(str));
    &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数也是和上面 MakeMap 函数类似。只不过接收参数的是函数。
《JavaScript 设计模式与开发实践》书中的第四章 JS单例模式也是类似的实现。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> getSingle = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">fn</span>)</span>&#123; <span class="hljs-comment">// 获取单例</span>
    <span class="hljs-keyword">var</span> result;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> result || (result = fn.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>));
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以下是一些正则，系统学习正则推荐<a href="https://juejin.cn/post/6844903501034684430" target="_blank" title="https://juejin.cn/post/6844903501034684430">老姚：《JavaScript 正则表达式迷你书》问世了！</a>，看过的都说好。所以本文不会过多描述正则相关知识点。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// \w 是 0-9a-zA-Z_ 数字 大小写字母和下划线组成</span>
<span class="hljs-comment">// () 小括号是 分组捕获</span>
<span class="hljs-keyword">const</span> camelizeRE = <span class="hljs-regexp">/-(\w)/g</span>;
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@private</span>
 */</span>
<span class="hljs-comment">// 首字母转大写</span>
<span class="hljs-keyword">const</span> camelize = cacheStringFunction(<span class="hljs-function">(<span class="hljs-params">str</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> str.replace(camelizeRE, <span class="hljs-function">(<span class="hljs-params">_, c</span>) =></span> (c ? c.toUpperCase() : <span class="hljs-string">''</span>));
&#125;);
<span class="hljs-comment">// \B 是指 非 \b 单词边界。</span>
<span class="hljs-keyword">const</span> hyphenateRE = <span class="hljs-regexp">/\B([A-Z])/g</span>;
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@private</span>
 */</span>

<span class="hljs-keyword">const</span> hyphenate = cacheStringFunction(<span class="hljs-function">(<span class="hljs-params">str</span>) =></span> str.replace(hyphenateRE, <span class="hljs-string">'-$1'</span>).toLowerCase());

<span class="hljs-comment">// 举例：onClick => on-click</span>
<span class="hljs-keyword">const</span> hyphenateResult = hyphenate(<span class="hljs-string">'onClick'</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hyphenateResult'</span>, hyphenateResult); <span class="hljs-comment">// 'on-click'</span>

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@private</span>
 */</span>
<span class="hljs-comment">// 首字母转大写</span>
<span class="hljs-keyword">const</span> capitalize = cacheStringFunction(<span class="hljs-function">(<span class="hljs-params">str</span>) =></span> str.charAt(<span class="hljs-number">0</span>).toUpperCase() + str.slice(<span class="hljs-number">1</span>));
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@private</span>
 */</span>
<span class="hljs-comment">// click => onClick</span>
<span class="hljs-keyword">const</span> toHandlerKey = cacheStringFunction(<span class="hljs-function">(<span class="hljs-params">str</span>) =></span> (str ? <span class="hljs-string">`on<span class="hljs-subst">$&#123;capitalize(str)&#125;</span>`</span> : <span class="hljs-string">``</span>));

<span class="hljs-keyword">const</span> result = toHandlerKey(<span class="hljs-string">'click'</span>);
<span class="hljs-built_in">console</span>.log(result, <span class="hljs-string">'result'</span>); <span class="hljs-comment">// 'onClick'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">3.27 hasChanged 判断是不是有变化</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// compare whether a value has changed, accounting for NaN.</span>
<span class="hljs-keyword">const</span> hasChanged = <span class="hljs-function">(<span class="hljs-params">value, oldValue</span>) =></span> value !== oldValue && (value === value || oldValue === oldValue);
<span class="hljs-comment">// 例子：</span>
<span class="hljs-comment">// 认为 NaN 是不变的</span>
hasChanged(<span class="hljs-literal">NaN</span>, <span class="hljs-literal">NaN</span>); <span class="hljs-comment">// false</span>
hasChanged(<span class="hljs-number">1</span>, <span class="hljs-number">1</span>); <span class="hljs-comment">// false</span>
hasChanged(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>); <span class="hljs-comment">// false</span>
<span class="hljs-comment">// 场景</span>
<span class="hljs-comment">// watch 监测值是不是变化了</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">3.28 invokeArrayFns  执行数组里的函数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> invokeArrayFns = <span class="hljs-function">(<span class="hljs-params">fns, arg</span>) =></span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < fns.length; i++) &#123;
        fns[i](arg);
    &#125;
&#125;;

<span class="hljs-comment">// 例子：</span>
<span class="hljs-keyword">const</span> arr = [
    <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">val</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(val + <span class="hljs-string">'的博客地址是：https://lxchuan12.gitee.io'</span>);
    &#125;,
    <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">val</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'百度搜索 若川 可以找到'</span> + val);
    &#125;,
    <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">val</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'微信搜索 若川视野 可以找到关注'</span> + val);
    &#125;,
]
invokeArrayFns(arr, <span class="hljs-string">'我'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么这样写，我们一般都是一个函数执行就行。</p>
<p>数组中存放函数，函数其实也算是数据。这种写法方便统一执行多个函数。</p>
<h3 data-id="heading-34">3.29 def 定义对象属性</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> def = <span class="hljs-function">(<span class="hljs-params">obj, key, value</span>) =></span> &#123;
    <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
        <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">false</span>,
        value
    &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Object.defineProperty</code> 算是一个非常重要的<code>API</code>。还有一个定义多个属性的<code>API</code>：<code>Object.defineProperties(obj, props) (ES5)</code></p>
<p><code>Object.defineProperty</code> 涉及到比较重要的知识点。<br>
在<code>ES3</code>中，除了一些内置属性（如：<code>Math.PI</code>），对象的所有的属性在任何时候都可以被修改、插入、删除。在<code>ES5</code>中，我们可以设置属性是否可以被改变或是被删除——在这之前，它是内置属性的特权。<code>ES5</code>中引入了<strong>属性描述符</strong>的概念，我们可以通过它对所定义的属性有更大的控制权。这些<strong>属性描述符</strong>（特性）包括：</p>
<blockquote>
<p><code>value</code>——当试图获取属性时所返回的值。<br>
<code>writable</code>——该属性是否可写。<br>
<code>enumerable</code>——该属性在<code>for in</code>循环中是否会被枚举。<br>
<code>configurable</code>——该属性是否可被删除。<br>
<code>set()</code>——该属性的更新操作所调用的函数。<br>
<code>get()</code>——获取属性值时所调用的函数。<br></p>
</blockquote>
<p>另外，<strong>数据描述符</strong>（其中属性为：<code>enumerable</code>，<code>configurable</code>，<code>value</code>，<code>writable</code>）与<strong>存取描述符</strong>（其中属性为<code>enumerable</code>，<code>configurable</code>，<code>set()</code>，<code>get()</code>）之间是有互斥关系的。在定义了<code>set()</code>和<code>get()</code>之后，描述符会认为存取操作已被 定义了，其中再定义<code>value</code>和<code>writable</code>会<strong>引起错误</strong>。</p>
<p>以下是<em>ES3</em>风格的属性定义方式：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;&#125;;
person.legs = <span class="hljs-number">2</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以下是等价的ES5通过<strong>数据描述符</strong>定义属性的方式：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;&#125;;
<span class="hljs-built_in">Object</span>.defineProperty(person, <span class="hljs-string">'legs'</span>, &#123;
    <span class="hljs-attr">value</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中， 除了value的默认值为<code>undefined</code>以外，其他的默认值都为<code>false</code>。这就意味着，如果想要通过这一方式定义一个可写的属性，必须显示将它们设为<code>true</code>。
或者，我们也可以通过<code>ES5</code>的存储描述符来定义：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;&#125;;
<span class="hljs-built_in">Object</span>.defineProperty(person, <span class="hljs-string">'legs'</span>, &#123;
    <span class="hljs-attr">set</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">v</span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.value = v;
    &#125;,
    <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">v</span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.value;
    &#125;,
    <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>
&#125;);
person.legs = <span class="hljs-number">2</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样一来，多了许多可以用来描述属性的代码，如果想要防止别人篡改我们的属性，就必须要用到它们。此外，也不要忘了浏览器向后兼容<code>ES3</code>方面所做的考虑。例如，跟添加<code>Array.prototype</code>属性不一样，我们不能再旧版的浏览器中使用<code>shim</code>这一特性。
另外，我们还可以（通过定义<code>nonmalleable</code>属性），在具体行为中运用这些描述符：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person = &#123;&#125;;
<span class="hljs-built_in">Object</span>.defineProperty(person, <span class="hljs-string">'heads'</span>, &#123;<span class="hljs-attr">value</span>: <span class="hljs-number">1</span>&#125;);
person.heads = <span class="hljs-number">0</span>; <span class="hljs-comment">// 0</span>
person.heads; <span class="hljs-comment">// 1  (改不了)</span>
<span class="hljs-keyword">delete</span> person.heads; <span class="hljs-comment">// false</span>
person.heads <span class="hljs-comment">// 1 (删不掉)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他本文就不过多赘述了。更多对象 <code>API</code> 可以查看这篇文章<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FY3nL3GPcxiqb3zK6pEuycg" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/Y3nL3GPcxiqb3zK6pEuycg" ref="nofollow noopener noreferrer">JavaScript 对象所有API解析</a>。</p>
<h3 data-id="heading-35">3.30 toNumber 转数字</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> toNumber = <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> n = <span class="hljs-built_in">parseFloat</span>(val);
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">isNaN</span>(n) ? val : n;
&#125;;

toNumber(<span class="hljs-string">'111'</span>); <span class="hljs-comment">// 111</span>
toNumber(<span class="hljs-string">'a111'</span>); <span class="hljs-comment">// 'a111'</span>
<span class="hljs-built_in">parseFloat</span>(<span class="hljs-string">'a111'</span>); <span class="hljs-comment">// NaN</span>
<span class="hljs-built_in">isNaN</span>(<span class="hljs-literal">NaN</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>其实 <code>isNaN</code> 本意是判断是不是 <code>NaN</code> 值，但是不准确的。</p>
</blockquote>
<p>比如：<code>isNaN('a')</code> 为 <code>true</code>。
所以 <code>ES6</code> 有了 <code>Number.isNaN</code> 这个判断方法，为了弥补这一个<code>API</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>.isNaN(<span class="hljs-string">'a'</span>)  <span class="hljs-comment">// false</span>
<span class="hljs-built_in">Number</span>.isNaN(<span class="hljs-literal">NaN</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">3.31 getGlobalThis 全局对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> _globalThis;
<span class="hljs-keyword">const</span> getGlobalThis = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> (_globalThis ||
        (_globalThis =
            <span class="hljs-keyword">typeof</span> globalThis !== <span class="hljs-string">'undefined'</span>
                ? globalThis
                : <span class="hljs-keyword">typeof</span> self !== <span class="hljs-string">'undefined'</span>
                    ? self
                    : <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">window</span> !== <span class="hljs-string">'undefined'</span>
                        ? <span class="hljs-built_in">window</span>
                        : <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">global</span> !== <span class="hljs-string">'undefined'</span>
                            ? <span class="hljs-built_in">global</span>
                            : &#123;&#125;));
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>获取全局 <code>this</code> 指向。</p>
<p>初次执行肯定是 <code>_globalThis</code> 是 <code>undefined</code>。所以会执行后面的赋值语句。</p>
<p>如果存在 <code>globalThis</code> 就用 <code>globalThis</code>。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FglobalThis" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/globalThis" ref="nofollow noopener noreferrer">MDN globalThis</a></p>
<p>如果存在<code>self</code>，就用<code>self</code>。在 <code>Web Worker</code> 中不能访问到 <code>window</code> 对象，但是我们却能通过 <code>self</code> 访问到 <code>Worker</code> 环境中的全局对象。</p>
<p>如果存在<code>window</code>，就用<code>window</code>。</p>
<p>如果存在<code>global</code>，就用<code>global</code>。<code>Node</code>环境下，使用<code>global</code>。</p>
<p>如果都不存在，使用空对象。可能是微信小程序环境下。</p>
<p>下次执行就直接返回 <code>_globalThis</code>，不需要第二次继续判断了。这种写法值得我们学习。</p>
<h2 data-id="heading-37">4. 最后推荐一些文章和书籍</h2>
<p>先推荐我认为不错的<code>JavaScript API</code>的几篇文章和几本值得读的书。</p>
<p><a href="https://juejin.cn/post/6844903476720320525" target="_blank" title="https://juejin.cn/post/6844903476720320525">JavaScript字符串所有API全解密</a></p>
<p><a href="https://juejin.cn/post/6844903476216987655" target="_blank" title="https://juejin.cn/post/6844903476216987655">【深度长文】JavaScript数组所有API全解密</a></p>
<p><a href="https://juejin.cn/post/6844903469824868365" target="_blank" title="https://juejin.cn/post/6844903469824868365">正则表达式前端使用手册</a></p>
<p><a href="https://juejin.cn/post/6844903501034684430" target="_blank" title="https://juejin.cn/post/6844903501034684430">老姚：《JavaScript 正则表达式迷你书》问世了！</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FY3nL3GPcxiqb3zK6pEuycg" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/Y3nL3GPcxiqb3zK6pEuycg" ref="nofollow noopener noreferrer">JavaScript 对象所有API解析</a> <a href="https://link.juejin.cn/?target=https%3A%2F%2Flxchuan12.gitee.io%2Fjs-object-api%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://lxchuan12.gitee.io/js-object-api/" ref="nofollow noopener noreferrer">lxchuan12.gitee.io/js-object-a…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript" ref="nofollow noopener noreferrer">MDN JavaScript</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.douban.com%2Fsubject%2F35175321%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://book.douban.com/subject/35175321/" ref="nofollow noopener noreferrer">《JavaScript高级程序设计》第4版</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.douban.com%2Fsubject%2F35396470%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://book.douban.com/subject/35396470/" ref="nofollow noopener noreferrer">《JavaScript 权威指南》第7版</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.douban.com%2Fsubject%2F26302623%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://book.douban.com/subject/26302623/" ref="nofollow noopener noreferrer">《JavaScript面向对象编程2》</a> 面向对象讲的很详细。</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fes6.ruanyifeng.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://es6.ruanyifeng.com/" ref="nofollow noopener noreferrer">阮一峰老师：《ES6 入门教程》</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.javascript.info%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.javascript.info/" ref="nofollow noopener noreferrer">《现代 JavaScript 教程》</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.douban.com%2Fsubject%2F26351021%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://book.douban.com/subject/26351021/" ref="nofollow noopener noreferrer">《你不知道的JavaScript》上中卷</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.douban.com%2Fsubject%2F26382780%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://book.douban.com/subject/26382780/" ref="nofollow noopener noreferrer">《JavaScript 设计模式与开发实践》</a></p>
<p>我也是从小白看不懂书经历过来的。到现在写文章分享。</p>
<p>我看书的方法：多本书同时看，看相同类似的章节，比如函数。看完这本可能没懂，看下一本，几本书看下来基本就懂了，一遍没看懂，再看几遍，可以避免遗忘，巩固相关章节。当然，刚开始看书很难受，看不进。这些书大部分在微信读书都有，如果习惯看纸质书，那可以买来看。</p>
<p>这时可以看些视频和动手练习一些简单的项目。</p>
<p>比如：可以自己注册一个<code>github</code>账号，分章节小节，抄写书中的代码，提交到<code>github</code>，练习了才会更有感觉。</p>
<p>再比如 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fchinese.freecodecamp.org" target="_blank" rel="nofollow noopener noreferrer" title="https://chinese.freecodecamp.org" ref="nofollow noopener noreferrer">freeCodeCamp 中文在线学习网站</a> 网站。看书是系统学习非常好的方法。后来我就是看源码较多，写文章分享出来给大家。</p>
<h2 data-id="heading-38">5. 总结</h2>
<p>文中主要通过学习 <code>shared</code> 模块下的几十个工具函数，比如有：<code>isPromise</code>、<code>makeMap</code>、<code>cacheStringFunction</code>、<code>invokeArrayFns</code>、<code>def</code>、<code>getGlobalThis</code>等等。</p>
<p>同时还分享了<code>vue</code>源码的调试技巧，推荐了一些书籍和看书籍的方法。</p>
<p>源码也不是那么可怕。平常我们工作中也是经常能使用到这些工具函数。通过学习一些简单源码，拓展视野的同时，还能落实到自己工作开发中，收益相对比较高。</p>
<hr>
<h2 data-id="heading-39">关于</h2>
<p>作者：常以<strong>若川</strong>为名混迹于江湖。前端路上 | PPT爱好者 | 所知甚少，唯善学。<br>
<a href="https://user-gold-cdn.xitu.io/2019/12/13/16efe57ddc7c9eb3?imageView2/0/w/1280/h/960/format/webp/ignore-error/1" title="https://user-gold-cdn.xitu.io/2019/12/13/16efe57ddc7c9eb3?imageView2/0/w/1280/h/960/format/webp/ignore-error/1" target="_blank">公众号若川视野</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Flxchuan12.gitee.io" title="https://link.juejin.cn?target=https%3A%2F%2Flxchuan12.gitee.io" target="_blank">若川的博客</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fblog%2Flxchuan12" title="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fblog%2Flxchuan12" target="_blank"><code>segmentfault</code>若川视野专栏</a>，开通了<strong>若川视野</strong>专栏，欢迎关注~<br>
<a href="https://juejin.im/user/1415826704971918/posts" title="https://juejin.im/user/1415826704971918/posts" target="_blank">掘金专栏</a>，欢迎关注~<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Flxchuan12" title="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Flxchuan12" target="_blank">知乎若川视野专栏</a>，开通了<strong>若川视野</strong>专栏，欢迎关注~<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flxchuan12%2Fblog" title="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flxchuan12%2Fblog" target="_blank">github blog</a>，求个<code>star</code>^_^~</p></div>  
</div>
            