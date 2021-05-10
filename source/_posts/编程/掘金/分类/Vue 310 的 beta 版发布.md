
---
title: 'Vue 3.1.0 的 beta 版发布'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8953'
author: 掘金
comments: false
date: Sun, 09 May 2021 08:10:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=8953'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>以往都是翻译给大家，这次换个形式为大家介绍。</p>
<p>本文由 <a href="https://github.com/QC-L" target="_blank" rel="nofollow noopener noreferrer">QC-L</a> 和 <a href="https://github.com/KnowsCount" target="_blank" rel="nofollow noopener noreferrer">KnowsCount</a> 完成编写和编辑工作。</p>
</blockquote>
<p>本次 beta 版本带来了一些有趣的新特性和错误修复。</p>
<h2 data-id="heading-0">新特性</h2>
<ul>
<li><code>onServerPrefetch</code>：composition-api 版本的 serverPrefetch</li>
<li>组件级别的 <code>compilerOptions</code></li>
<li><code>@vue/compiler-core</code> 支持了空白字符处理策略</li>
<li>支持通过 <code>app.config.compilerOptions</code> 配置运行时的编译器</li>
<li>devtools 改进了对 KeepAlive 的支持</li>
<li>支持通过 <code>is="vue:xxx"</code> 将普通元素转换为组件</li>
</ul>
<h3 data-id="heading-1"><code>onServerPrefetch</code></h3>
<p>具体请参见 <a href="https://github.com/vuejs/vue-next/pull/3070" target="_blank" rel="nofollow noopener noreferrer">PR 3070</a> 和 <a href="https://github.com/vuejs/vue-next/pull/2902" target="_blank" rel="nofollow noopener noreferrer">PR 2902</a></p>
<p>此特性主要解决在 <code>composition-api</code> 情况下没有提供 serverPrefetch 生命周期钩子函数的问题。</p>
<p>这个钩子函数名为 <code>onServerPrefetch</code>。</p>
<p>如果你也这方面的需求，可以尝试升级至 <code>3.1.0-beta</code> 版</p>
<p>相关讨论:</p>
<ul>
<li><a href="https://github.com/vuejs/vue-apollo/issues/1102" target="_blank" rel="nofollow noopener noreferrer">vue-apollo</a></li>
<li><a href="https://github.com/quasarframework/app-extension-apollo/issues/51#issuecomment-791977057" target="_blank" rel="nofollow noopener noreferrer">app-extension-apollo</a></li>
</ul>
<h3 data-id="heading-2"><code>@vue/complier-core</code> 支持了空白字符处理策略</h3>
<p>具体内容请参阅 <a href="https://github.com/vuejs/vue-next/pull/1600" target="_blank" rel="nofollow noopener noreferrer">PR 1600</a> 和 <a href="https://github.com/vuejs/vue/blob/dev/flow/compiler.js#L10" target="_blank" rel="nofollow noopener noreferrer">v2 原有效果</a>。</p>
<h4 data-id="heading-3">应用</h4>
<p>我们来测试下此策略：</p>
<p>先装个 beta 版本的 <code>@vue/compiler-core</code></p>
<pre><code class="hljs language-bash copyable" lang="bash">yarn add @vue/compiler-core@beta
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新建 <code>index.js</code> 文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> core = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@vue/compiler-core'</span>)

<span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">baseCompile</span>: complie &#125; = core

<span class="hljs-keyword">const</span> &#123; ast &#125; = complie(<span class="hljs-string">`      foo \n bar baz      `</span>, &#123;
  <span class="hljs-attr">whitespace</span>: <span class="hljs-string">'preserve'</span> <span class="hljs-comment">// condense</span>
&#125;)

<span class="hljs-built_in">console</span>.log(ast.children[<span class="hljs-number">0</span>])
<span class="hljs-built_in">console</span>.log(ast.children[<span class="hljs-number">0</span>].content)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大概效果如示例所示：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 源代码 --></span>
      foo \n bar baz     

<span class="hljs-comment"><!-- whitespace: 'preserve' --></span>
      foo \n bar baz     

<span class="hljs-comment"><!-- whitespace: 'condense' --></span>
 foo bar baz 
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">源码</h4>
<p>原本只在 <code>compiler-core</code> 的 <code>parse</code> 文件中的 <code>defaultParserOptions</code> 提供了默认的 <code>condense</code> 情况</p>
<pre><code class="hljs language-ts copyable" lang="ts">whitespace: <span class="hljs-string">'condense'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>compiler-core</code> 的 options 文件中新增了 <code>whitespace</code>：</p>
<pre><code class="hljs language-ts copyable" lang="ts">whitespace?: <span class="hljs-string">'preserve'</span> | <span class="hljs-string">'condense'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相关链接：</p>
<ul>
<li><a href="https://github.com/vuejs/vue-next/pull/1600" target="_blank" rel="nofollow noopener noreferrer">PR 1600</a></li>
<li><a href="https://stackoverflow.com/questions/64432182/vue-3-removes-white-space-between-inline-block-elements" target="_blank" rel="nofollow noopener noreferrer">stackoverflow</a></li>
<li><a href="https://github.com/vuejs/vue/blob/dev/flow/compiler.js#L10" target="_blank" rel="nofollow noopener noreferrer">vue 2.0/compiler</a></li>
<li><a href="https://github.com/vuejs/vue/issues/9208#issuecomment-450012518" target="_blank" rel="nofollow noopener noreferrer">vue 2.0 的 <code>whitespace</code></a></li>
<li><a href="https://github.com/vuejs/vue/commit/e1abedb9e66b21da8a7e93e175b9dabe334dfebd" target="_blank" rel="nofollow noopener noreferrer">vue 2.0 的 PR</a></li>
</ul>
<h3 data-id="heading-5">通过 <code>is="vue:xxx"</code> 支持普通元素的转换</h3>
<p>这条特性的更新，从源码上看，兼容了两种类型。</p>
<ol>
<li>弃用的 <code>v-is</code> 指令</li>
<li><code>is="vue:xxx"</code> 的属性</li>
</ol>
<h4 data-id="heading-6">源码</h4>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">let</span> &#123; tag &#125; = node

<span class="hljs-comment">// 1. 动态组件</span>
<span class="hljs-keyword">const</span> isExplicitDynamic = isComponentTag(tag)
<span class="hljs-keyword">const</span> isProp =
  findProp(node, <span class="hljs-string">'is'</span>) || (!isExplicitDynamic && findDir(node, <span class="hljs-string">'is'</span>))
<span class="hljs-keyword">if</span> (isProp) &#123;
  <span class="hljs-keyword">if</span> (!isExplicitDynamic && isProp.type === NodeTypes.ATTRIBUTE) &#123;
    <span class="hljs-comment">// <button is="vue:xxx"></span>
    <span class="hljs-comment">// 如果不是 <component>，仅仅是 "vue:" 开头</span>
    <span class="hljs-comment">// 在解析阶段会被视为组件，并在此处进行</span>
    <span class="hljs-comment">// tag 被重新赋值为 "vue:" 以后的内容</span>
    tag = isProp.value!.content.slice(<span class="hljs-number">4</span>)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">const</span> exp =
      isProp.type === NodeTypes.ATTRIBUTE
        ? isProp.value && createSimpleExpression(isProp.value.content, <span class="hljs-literal">true</span>)
        : isProp.exp
    <span class="hljs-keyword">if</span> (exp) &#123;
      <span class="hljs-keyword">return</span> createCallExpression(context.helper(RESOLVE_DYNAMIC_COMPONENT), [
        exp
      ])
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 当 tag 为 <component>，或者 is="vue:xxx"，跳过后续处理</span>
<span class="hljs-keyword">if</span> (
  name === <span class="hljs-string">'is'</span> &&
  (isComponentTag(tag) || (value && value.content.startsWith(<span class="hljs-string">'vue:'</span>)))
) &#123;
  <span class="hljs-keyword">continue</span>
&#125;
<span class="hljs-comment">// ...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码中有几个点：</p>
<ol>
<li>首先 <code>isComponentTag</code>，用以判断是否为动态组件：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 此方法用于判断是否为动态组件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isComponentTag</span>(<span class="hljs-params">tag: string</span>) </span>&#123;
  <span class="hljs-keyword">return</span> tag[<span class="hljs-number">0</span>].toLowerCase() + tag.slice(<span class="hljs-number">1</span>) === <span class="hljs-string">'component'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>查找是否含有 <code>is</code> 属性</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 先查属性</span>
findProp(node, <span class="hljs-string">'is'</span>)
<span class="hljs-comment">// 否则判断是不是动态组件，如果不是，判断是不是指令</span>
!isExplicitDynamic && findDir(node, <span class="hljs-string">'is'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其主要原因是，两者的 AST 结构不同。</p>
<p>相关链接：</p>
<ul>
<li><a href="https://github.com/vuejs/vue-next/commit/af9e6999e1779f56b5cf827b97310d8e4e1fe5ec" target="_blank" rel="nofollow noopener noreferrer">Support casting plain element</a></li>
<li><a href="https://v3.vuejs.org/guide/migration/custom-elements-interop.html" target="_blank" rel="nofollow noopener noreferrer">Custom Elements Interop</a></li>
</ul>
<h3 data-id="heading-7">Bug 修复</h3>
<ul>
<li><strong>兼容：</strong> 处理并针对 config.optionMergeStrategies 实现告警 (<a href="https://github.com/vuejs/vue-next/commit/94e69fd3896214da6ff8b9fb09ad942c598053c7" target="_blank" rel="nofollow noopener noreferrer">94e69fd</a>)</li>
<li><strong>compiler-core:</strong> 当注释选项启用时，在生产环境下将保留注释 (<a href="https://github.com/vuejs/vue-next/commit/e4862544310a4187dfc8b3a49944700888bb60e3" target="_blank" rel="nofollow noopener noreferrer">e486254</a>)</li>
<li><strong>hmr:</strong> 禁止从组件类型中移除 __file 的 key 值 (<a href="https://github.com/vuejs/vue-next/commit/9db3cbbfc1a072675a8d0e53edf3869af115dc60" target="_blank" rel="nofollow noopener noreferrer">9db3cbb</a>)</li>
<li><strong>hydration:</strong> 修复 asnyc 组件 hydrated 前的更新 (<a href="https://github.com/vuejs/vue-next/issues/3563" target="_blank" rel="nofollow noopener noreferrer">#3563</a>) (<a href="https://github.com/vuejs/vue-next/commit/c8d96837b871d7ad34cd73b4669338be5fdd59fd" target="_blank" rel="nofollow noopener noreferrer">c8d9683</a>), closes <a href="https://github.com/vuejs/vue-next/issues/3560" target="_blank" rel="nofollow noopener noreferrer">#3560</a></li>
<li><strong>reactivity:</strong> 修复 readonly + reactive Map 的追溯 (<a href="https://github.com/vuejs/vue-next/issues/3604" target="_blank" rel="nofollow noopener noreferrer">#3604</a>) (<a href="https://github.com/vuejs/vue-next/commit/5036c51cb78435c145ffea5e82cd620d0d056ff7" target="_blank" rel="nofollow noopener noreferrer">5036c51</a>), closes <a href="https://github.com/vuejs/vue-next/issues/3602" target="_blank" rel="nofollow noopener noreferrer">#3602</a></li>
<li><strong>runtime-core:</strong> 确保声明 props 的 key 永远存在 (<a href="https://github.com/vuejs/vue-next/commit/4fe4de0a49ffc2461b0394e74674af38ff5e2a20" target="_blank" rel="nofollow noopener noreferrer">4fe4de0</a>), closes <a href="https://github.com/vuejs/vue-next/issues/3288" target="_blank" rel="nofollow noopener noreferrer">#3288</a></li>
<li><strong>runtime-core:</strong> 监听多源: computed (<a href="https://github.com/vuejs/vue-next/issues/3066" target="_blank" rel="nofollow noopener noreferrer">#3066</a>) (<a href="https://github.com/vuejs/vue-next/commit/e7300eb47960a153311d568d7976ac5256eb6297" target="_blank" rel="nofollow noopener noreferrer">e7300eb</a>), closes <a href="https://github.com/vuejs/vue-next/issues/3068" target="_blank" rel="nofollow noopener noreferrer">#3068</a></li>
<li><strong>Teleport:</strong> 避免改变对 vnode.dynamicChildren 的引用 (<a href="https://github.com/vuejs/vue-next/issues/3642" target="_blank" rel="nofollow noopener noreferrer">#3642</a>) (<a href="https://github.com/vuejs/vue-next/commit/43f78151bfdff2103a9be25e66e3f3be68d03a08" target="_blank" rel="nofollow noopener noreferrer">43f7815</a>), closes <a href="https://github.com/vuejs/vue-next/issues/3641" target="_blank" rel="nofollow noopener noreferrer">#3641</a></li>
<li><strong>watch:</strong> 避免遍历 non-plain 对象 (<a href="https://github.com/vuejs/vue-next/commit/62b8f4a39ca56b48a8c8fdf7e200cb80735e16ae" target="_blank" rel="nofollow noopener noreferrer">62b8f4a</a>)</li>
<li><strong>watch:</strong> this.$watch 应该支持监听键路径 (<a href="https://github.com/vuejs/vue-next/commit/870f2a7ba35245fd8c008d2ff666ea130a7e4704" target="_blank" rel="nofollow noopener noreferrer">870f2a7</a>)</li>
</ul>
<h3 data-id="heading-8">特性</h3>
<ul>
<li>onServerPrefetch (<a href="https://github.com/vuejs/vue-next/issues/3070" target="_blank" rel="nofollow noopener noreferrer">#3070</a>) (<a href="https://github.com/vuejs/vue-next/commit/349eb0f0ad78f9cb491278eb4c7f9fe0c2e78b79" target="_blank" rel="nofollow noopener noreferrer">349eb0f</a>)</li>
<li>运行时编译器支持了组件级 <code>compilerOptions</code> (<a href="https://github.com/vuejs/vue-next/commit/ce0bbe053abaf8ba18de8baf535e175048596ee5" target="_blank" rel="nofollow noopener noreferrer">ce0bbe0</a>)</li>
<li><strong>compiler-core:</strong> whitespace 处理策略 (<a href="https://github.com/vuejs/vue-next/commit/dee3d6ab8b4da6653d15eb148c51d9878007f6b6" target="_blank" rel="nofollow noopener noreferrer">dee3d6a</a>)</li>
<li><strong>config:</strong> 利用 <code>app.config.compilerOptions</code> 支持配置运行时编译器 (<a href="https://github.com/vuejs/vue-next/commit/091e6d67bfcc215227d78be578c68ead542481ad" target="_blank" rel="nofollow noopener noreferrer">091e6d6</a>)</li>
<li><strong>devtools:</strong> 升级对 KeepAlive 的支持 (<a href="https://github.com/vuejs/vue-next/commit/03ae3006e1e678ade4377cd10d206e8f7b4ad0cb" target="_blank" rel="nofollow noopener noreferrer">03ae300</a>)</li>
<li>支持利用 is="vue:xxx" 将 plain 元素 cast 到组件 (<a href="https://github.com/vuejs/vue-next/commit/af9e6999e1779f56b5cf827b97310d8e4e1fe5ec" target="_blank" rel="nofollow noopener noreferrer">af9e699</a>)</li>
</ul>
<h3 data-id="heading-9">性能提升</h3>
<ul>
<li>仅当实际改变时才会触发 $attrs 的更新 (<a href="https://github.com/vuejs/vue-next/commit/5566d39d467ebdd4e4234bc97d62600ff01ea28e" target="_blank" rel="nofollow noopener noreferrer">5566d39</a>)</li>
<li><strong>compiler:</strong> 解析结束标签时跳过不必要的检查 (<a href="https://github.com/vuejs/vue-next/commit/048ac299f35709b25ae1bc1efa67d2abc53dbc3b" target="_blank" rel="nofollow noopener noreferrer">048ac29</a>)</li>
</ul></div>  
</div>
            