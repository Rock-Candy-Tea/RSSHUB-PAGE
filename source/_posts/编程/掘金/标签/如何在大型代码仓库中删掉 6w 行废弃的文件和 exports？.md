
---
title: '如何在大型代码仓库中删掉 6w 行废弃的文件和 exports？'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74f7539d1a594f40b08ddb50f51421de~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 18:54:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74f7539d1a594f40b08ddb50f51421de~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>作者：ssh，字节跳动 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebinfra.org%2Fbytedance%2Fweb-infra" target="_blank" rel="nofollow noopener noreferrer" title="https://webinfra.org/bytedance/web-infra" ref="nofollow noopener noreferrer">Web Infra 团队</a>成员，内推欢迎联系 sshsunlight</p>
<p>本文是我最近在公司内部写的<strong>废弃代码删除工具</strong>的一篇思考总结，目前在多个项目中已经删除约 <strong>6w</strong> 行代码。</p>
<p>首发于公众号<a href="https://link.juejin.cn/?target=https%3A%2F%2Fp1-jj.byteimg.com%2Ftos-cn-i-t2oaga2asx%2Fgold-user-assets%2F2020%2F4%2F5%2F17149cbcaa96ff26~tplv-t2oaga2asx-image.image" target="_blank" rel="nofollow noopener noreferrer" title="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2020/4/5/17149cbcaa96ff26~tplv-t2oaga2asx-image.image" ref="nofollow noopener noreferrer">前端从进阶到入院</a>，欢迎关注。</p>
</blockquote>
<h2 data-id="heading-0">起因</h2>
<p>很多项目历史悠久，其中很多 <strong>文件或是 export 出去的变量</strong> 已经不再使用，非常影响维护迭代。
举个例子来说，后端问你：“某某接口统计一下某接口是否还有使用？”你在项目里一搜，好家伙，还有好几处使用呢，结果那些定义或文件是从未被引入的，这就会误导你们去继续维护这个文件或接口，影响迭代效率。</p>
<p><strong>先从删除废弃的 exports 讲起，后文会讲删除废弃文件。</strong></p>
<p>删除 exports，有几个难点：</p>
<ol>
<li>
<p>怎么样稳定的 <strong>找出 export 出去，但是其他文件未 import 的变量</strong> ？</p>
</li>
<li>
<p>如何确定步骤 1 中变量在 <strong>本文件内部没有用到</strong> （作用域分析）？</p>
</li>
<li>
<p>如何稳定的 <strong>删除这些变量</strong> ？</p>
</li>
</ol>
<h2 data-id="heading-1">整体思路</h2>
<p>先给出整体的思路，公司内的小伙伴推荐了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpzavolinsky%2Fts-unused-exports" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pzavolinsky/ts-unused-exports" ref="nofollow noopener noreferrer">pzavolinsky/ts-unused-exports</a> 这个开源库，并且已经在项目中稳定使用了一段时间，这个库可以搞定上述<strong>第一步</strong>的诉求，也就是<strong>找出 export 出去，但是其他文件未 import 的变量。</strong>
但下面两步依然很棘手，先给出我的结论：</p>
<ol>
<li><strong>如何确定步骤 1 中变量在本文件内部没有用到（作用域分析）？</strong></li>
</ol>
<p>对分析出的文件调用 ESLint 的 API，<code>no-unused-vars</code> 这个 ESLint rule 天生就可以分析出文件内部某个变量是否使用，但默认情况下它是不支持对 export 出去的变量进行分析的，因为既然你 export 了这个变量，那其实 ESLint 就认为你这个变量会被外部使用。对于这个限制，其实只需要 fork 下来稍微改写即可。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74f7539d1a594f40b08ddb50f51421de~tplv-k3u1fbpfcp-watermark.image" alt title="屏幕截图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li><strong>如何稳定的删除这些变量？</strong></li>
</ol>
<p>自己编写 <code>rule fixer</code> 删除掉分析出来的无用变量，之后就是<strong>格式化</strong>，由于 ESLint 删除代码后格式会乱掉，所以手动调用 prettier API 让代码恢复美观即可。</p>
<p>接下来我会对上述每一步详细讲解。</p>
<h3 data-id="heading-2">导出导入分析</h3>
<p>使用测试下来， <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpzavolinsky%2Fts-unused-exports" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pzavolinsky/ts-unused-exports" ref="nofollow noopener noreferrer">pzavolinsky/ts-unused-exports</a> 确实可以靠谱的分析出 <strong>未使用的 export 变量</strong> ，但是这种分析 <code>import、export</code> 关系的工具，只是局限于此，不会分析 <code>export</code> 出去的这个变量 <strong>在代码内部是否有使用到</strong> 。</p>
<h3 data-id="heading-3">文件内部使用分析</h3>
<p>第二步的问题比较复杂，这里最终选用 <code>ESLint</code> 配合自己 fork 改写 <code>no-unused-vars</code> 这个 <code>rule</code> ，并且自己提供规则对应的修复方案 <code>fixer</code> 来实现。</p>
<h4 data-id="heading-4">为什么是 ESLint？</h4>
<ol>
<li>
<p>社区广泛使用，经过无数项目验证。</p>
</li>
<li>
<p>基于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Feslint.org%2Fdocs%2Fdeveloper-guide%2Fworking-with-rules%23contextgetscope" target="_blank" rel="nofollow noopener noreferrer" title="https://eslint.org/docs/developer-guide/working-with-rules#contextgetscope" ref="nofollow noopener noreferrer">作用域分析</a> ，准确的找出未使用的变量。</p>
</li>
<li>
<p>提供的 AST 符合 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Festree%2Festree" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/estree/estree" ref="nofollow noopener noreferrer">estree/estree</a> 的通用标准，易于维护拓展。</p>
</li>
<li>
<p>ESLint 可以解决 <strong>删除之后引入新的无用变量的问题</strong> ，最典型的就是删除了某个函数，这个函数内部的某个函数也可能会变成无效代码。ESLint 会 <strong>重复执行</strong> <code>fix</code> 函数，直到不再有新的可修复错误为止。</p>
</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74a693da325e4b6087da09b6abbc5395~tplv-k3u1fbpfcp-watermark.image" alt title="屏幕截图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">为什么要 fork 下来改写它？</h4>
<ol>
<li>
<p>官方的 <code>no-unused-vars</code> 默认是不考虑 <code>export</code> 出去的变量的，而经过我对源码的阅读发现，仅仅 <strong>修改少量的代码</strong> 就可以打破这个限制，让 <code>export</code> 出去的变量也可以被分析，在模块内部是否使用。</p>
</li>
<li>
<p>第一步的改写后，很多 <code>export</code> 出去的变量 <strong>被其他模块引用</strong> ，但由于在 <strong>模块内部未使用</strong> ，也会 <strong>被分析为未使用变量</strong> 。所以需要给 <code>rule</code> 提供一个 <code>varsPattern</code> 的选项，把分析范围限定在 <code>ts-unused-exports</code> 给出的 <strong>导出未使用变量</strong> 中，如 <code>varsPattern: '^foo$|^bar$'</code> 。</p>
</li>
<li>
<p>官方的 <code>no-unused-vars</code> 只给出提示，没有提供 <strong>自动修复</strong> 的方案，需要自己编写，下面详细讲解。</p>
</li>
</ol>
<h3 data-id="heading-6">如何删除变量</h3>
<p>当我们在 IDE 中编写代码时，有时会发现保存之后一些 ESLint 飘红的部分被自动修复了，但另一部分却没有反应。
这其实是 ESLint 的 <code>rule fixer</code> 的作用。
参考官方文档的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Feslint.org%2Fdocs%2Fdeveloper-guide%2Fworking-with-rules%23applying-fixes" target="_blank" rel="nofollow noopener noreferrer" title="https://eslint.org/docs/developer-guide/working-with-rules#applying-fixes" ref="nofollow noopener noreferrer">Apply Fixer</a> 章节，每个 ESLint Rule 的编写者都可以决定自己的这条规则 <strong>是否可以自动修复，以及如何修复。</strong>
修复不是凭空产生的，需要作者自己对相应的 AST 节点做分析、删除等操作，好在 ESLint 提供了一个 <code>fixer</code> 工具包，里面封装了很多好用的节点操作方法，比如 <code>fixer.remove()</code> ， <code>fixer.replaceText()</code> 。
官方的 <code>no-unused-vars</code> 由于稳定性等原因未提供代码的自动修复方案，需要自己对这个 <code>rule</code> 写对应的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Feslint.org%2Fdocs%2Fdeveloper-guide%2Fworking-with-rules%23applying-fixes" target="_blank" rel="nofollow noopener noreferrer" title="https://eslint.org/docs/developer-guide/working-with-rules#applying-fixes" ref="nofollow noopener noreferrer">fixer</a> 。官方给出的解释在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feslint%2Feslint%2Fissues%2F14585" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eslint/eslint/issues/14585" ref="nofollow noopener noreferrer">Add fix/suggestions to <code>no-unused-vars</code> rule · Issue #14585 · eslint/eslint</a> 。</p>
<h2 data-id="heading-7">核心改动</h2>
<p>把 ESLint Plugin 单独拆分到一个目录中，结构如下：</p>
<pre><code class="hljs language-plain%20text copyable" lang="plain%20text">packages/eslint-plugin-deadvars
├── ast-utils.js
├── eslint-plugin.js
├── eslint-rule-typescript-unused-vars.js
├── eslint-rule-unused-vars.js
├── eslint-rule.js
└── package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p><code>eslint-plugin.js</code> : 插件入口，外部引入后才可以使用 <code>rule</code></p>
</li>
<li>
<p><code>eslint-rule-unused-vars.js</code> : ESLint 官方的 <code>eslint/no-unused-vars</code> 代码，主要的核心代码都在里面。</p>
</li>
<li>
<p><code>eslint-rule-typescript-unused-vars</code> : <code>typescript-eslint/no-unused-vars</code> 内部的代码，继承了 <code>eslint/no-unused-vars</code> ，增加了一些 TypeScript AST 节点的分析。</p>
</li>
<li>
<p><code>eslint-rule.js</code> ：规则入口，引入了 <code>typescript rule</code> ，并且利用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnot-an-aardvark%2Feslint-rule-composer" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/not-an-aardvark/eslint-rule-composer" ref="nofollow noopener noreferrer">eslint-rule-composer</a> 给这个规则增加了自动修复的逻辑。</p>
</li>
</ul>
<h3 data-id="heading-8">ESLint Rule 改动</h3>
<p>我们的分析涉及到删除，所以必须有一个严格的限定范围，就是 <strong>exports 出去</strong> 且被 ts-unused-exports 认定为 <strong>外部未使用</strong> 的变量。
所以考虑增加一个配置 <code>varsPattern</code> ，把 ts-unused-exports 分析出的未使用变量名传入进去，限定在这个名称范围内。
主要改动逻辑是在 <code>collectUnusedVariables</code> 这个函数中，这个函数的作用是 <strong>收集作用域中没有使用到的变量</strong> ，这里把 <strong>exports 且不符合变量名范围</strong> 的全部跳过不处理。</p>
<pre><code class="hljs language-diff copyable" lang="diff">else if (
  config.varsIgnorePattern &&
  config.varsIgnorePattern.test(def.name.name)
) &#123;
  // skip ignored variables
  continue;
<span class="hljs-addition">+ &#125; else if (</span>
<span class="hljs-addition">+  isExported(variable) &&</span>
<span class="hljs-addition">+  config.varsPattern &&</span>
<span class="hljs-addition">+  !config.varsPattern.test(def.name.name)</span>
<span class="hljs-addition">+) &#123;</span>
<span class="hljs-addition">+  // 符合 varsPattern</span>
<span class="hljs-addition">+  continue;</span>
<span class="hljs-addition">+ &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样外部就可以这样使用这样的方式来限定分析范围：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">rules: &#123;
  <span class="hljs-string">'@deadvars/no-unused-vars'</span>: [
    <span class="hljs-string">'error'</span>,
    &#123; <span class="hljs-attr">varsPattern</span>: <span class="hljs-string">'^foo$|^bar$'</span> &#125;,
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着删除掉原版中 <strong>收集未使用变量时</strong> 对 <code>isExported</code> 的判断，把 <strong>exports 出去但文件内部未使用</strong> 的变量也收集起来。由于上一步已经限定了变量名，所以这里只会收集到 ts-unused-exports 分析出来的变量。</p>
<pre><code class="hljs language-diff copyable" lang="diff">if (
  !isUsedVariable(variable) &&
<span class="hljs-deletion">- !isExported(variable) &&</span>
  !hasRestSpreadSibling(variable)
) &#123;
  unusedVars.push(variable);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">ESLint Rule Fixer</h3>
<p>接下来主要就是增加自动修复，这部分的逻辑在 <code>eslint-rule.js</code> 中，简单来说就是对上一步分析出来的各种未使用变量的 AST 节点进行判断和删除。
贴一下简化的函数处理代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = ruleComposer.mapReports(rule, <span class="hljs-function">(<span class="hljs-params">problem, context</span>) =></span> &#123;
  problem.fix = <span class="hljs-function"><span class="hljs-params">fixer</span> =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; node &#125; = problem;
    <span class="hljs-keyword">const</span> &#123; parent &#125; = node;

    <span class="hljs-comment">// 函数节点</span>
    <span class="hljs-keyword">switch</span> (parent.type) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">'FunctionExpression'</span>:
      <span class="hljs-keyword">case</span> <span class="hljs-string">'FunctionDeclaration'</span>:
      <span class="hljs-keyword">case</span> <span class="hljs-string">'ArrowFunctionExpression'</span>:
        <span class="hljs-comment">// 调用 fixer 进行删除</span>
        <span class="hljs-keyword">return</span> fixer.remove(parent);
      ...
      ...
      <span class="hljs-attr">default</span>:
        <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
    &#125;
  &#125;;
  <span class="hljs-keyword">return</span> problem;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目前会对以下几种节点类型进行删除：</p>
<ul>
<li>
<p>FunctionExpression</p>
</li>
<li>
<p>FunctionDeclaration</p>
</li>
<li>
<p>ArrowFunctionExpression</p>
</li>
<li>
<p>ImportSpecifier</p>
</li>
<li>
<p>ImportDefaultSpecifier</p>
</li>
<li>
<p>ImportNamespaceSpecifier</p>
</li>
<li>
<p>VariableDeclarator</p>
</li>
<li>
<p>TSEnumDeclaration</p>
</li>
</ul>
<p>后续新增节点的删除逻辑，只需要维护这个文件即可。</p>
<h2 data-id="heading-10">无用文件删除</h2>
<p>之前基于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMQuy%2Fwebpack-deadcode-plugin" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MQuy/webpack-deadcode-plugin" ref="nofollow noopener noreferrer">webpack-deadcode-plugin</a> 做了一版无用代码删除，但是在实际使用的过程中，发现一些问题。</p>
<p>首先是 <strong>速度太慢</strong> ，这个插件会基于 webpack 编译的结果来分析哪些文件是无用的，每次使用都需要编译一遍项目。</p>
<p>而且前几天加入了 fork-ts-checker-webpack-plugin 进行类型检查之后， <strong>这个删除方案突然失效了</strong> ，检测出来的只有 .less 类型的无用文件，经过和排查后发现是这个插件的锅，它会把 <strong>src</strong> <strong>目录下的所有</strong> <strong>ts</strong> <strong>文件</strong> 都加入到 webpack 的依赖中，也就是 <code>compilation.fileDependencies</code> （可以尝试开启这个插件，在开发环境试着手动改一个完全未导入的 ts 文件，一样会触发重新编译）</p>
<p>而 deadcode-plugin 就是依赖 <code>compilation.fileDependencies</code> 这个变量来判断哪些文件未被使用，所有 ts 文件都在这个变量中的话，扫描出来的无用文件自然就只有其他类型了。</p>
<p>这个行为应该是插件的官方有意而为之，考虑如下情况：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 直接导入一个 TS 类型</span>
<span class="hljs-keyword">import</span> &#123; IProps &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./type.ts"</span>;

<span class="hljs-comment">// use IProps</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在使用旧版的 fork-ts-checker-webpack-plugin 时，如果此时改动了 IProps 造成了类型错误，是不会触发 webpack 的编译报错的。</p>
<p>经过排查，目前官方的行为好像是把 tsconfig 中的 <code>include</code> 里的所有 ts 文件加入到依赖中，方便改动触发编译，而我们项目中的 <code>include</code> 是 <code>["src/**/*.ts"]</code> ，所以……</p>
<p>具体讨论可以查看这个 Issue： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FTypeStrong%2Ffork-ts-checker-webpack-plugin%2Fissues%2F502" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/TypeStrong/fork-ts-checker-webpack-plugin/issues/502" ref="nofollow noopener noreferrer">Files that provide only type dependencies for main entry and unused files are not being checked for</a></p>
<h3 data-id="heading-11">方案</h3>
<p>首先尝试在 deadcode 模式中手动删除 fork-ts-checker-webpack-plugin，这样可以扫描出无用依赖，但是上文中那样从文件中只导入类型的情况，还是会被认为是无用的文件而误删。</p>
<p>考虑到现实场景中单独建一个 type.ts 文件书写接口或类型的情况比较多，只好先放弃这个方案。</p>
<p>转而一想， <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpzavolinsky%2Fts-unused-exports" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pzavolinsky/ts-unused-exports" ref="nofollow noopener noreferrer">pzavolinsky/ts-unused-exports</a> 这个工具既然都能分析出
所有文件的 <strong>导入导出变量的依赖关系</strong> ，那分析出未使用的文件应该也是小意思才对。</p>
<p>经过源码调试，大概梳理出了这个工具的原理：</p>
<ol>
<li>通过 TypeScript 内置的 <code>ts.parseJsonConfigFileContent</code> API 扫描出项目内完整的 ts 文件路径。</li>
</ol>
<pre><code class="hljs language-json copyable" lang="json"> &#123;
    <span class="hljs-attr">"path"</span>: <span class="hljs-string">"src/component/A"</span>,
    <span class="hljs-attr">"fullPath"</span>: <span class="hljs-string">"/Users/admin/works/test/src/component/A.tsx"</span>,
  &#123;
    <span class="hljs-attr">"path"</span>: <span class="hljs-string">"src/component/B"</span>,
    <span class="hljs-attr">"fullPath"</span>: <span class="hljs-string">"/Users/admin/works/test/apps/app/src/component/B.tsx"</span>,
  &#125;
  ...
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>通过 TypeScript 内置的一些 compile API 分析出文件之间的 exports 和 imports 关系。</li>
</ol>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"path"</span>: <span class="hljs-string">"src/component/A"</span>,
  <span class="hljs-attr">"fullPath"</span>: <span class="hljs-string">"/Users/admin/works/test/src/component/A.tsx"</span>,
  <span class="hljs-attr">"imports"</span>: &#123;
    <span class="hljs-attr">"styled-components"</span>: [<span class="hljs-string">"default"</span>],
    <span class="hljs-attr">"react"</span>: [<span class="hljs-string">"default"</span>],
    <span class="hljs-attr">"src/components/B"</span>: [<span class="hljs-string">"TestComponentB"</span>]
  &#125;,
  <span class="hljs-attr">"exports"</span>: [<span class="hljs-string">"TestComponentA"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>根据上述信息来分析出每个文件中每个变量的使用次数，筛选出未使用的变量并且输出。</li>
</ol>
<p>到此思路也就有了，把所有文件中的 <code>imports</code> 信息取一个合集，然后从第一步的文件集合中找出未出现在 <code>imports</code> 里的文件即可。</p>
<h2 data-id="heading-12">一些值得一提的改造</h2>
<h3 data-id="heading-13">循环删除文件</h3>
<p>在第一次检测出无用文件并删除后，很可能会暴露出一些新的无用文件。
比如以下这样的例子：</p>
<pre><code class="hljs language-json copyable" lang="json">[
  &#123;
    <span class="hljs-attr">"path"</span>: <span class="hljs-string">"a"</span>,
    <span class="hljs-attr">"imports"</span>: <span class="hljs-string">"b"</span>
  &#125;,
  &#123;
    <span class="hljs-attr">"path"</span>: <span class="hljs-string">"b"</span>,
    <span class="hljs-attr">"imports"</span>: <span class="hljs-string">"c"</span>
  &#125;,
  &#123;
    <span class="hljs-attr">"path"</span>: <span class="hljs-string">"c"</span>
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>文件 a 引入了文件 b，文件 b 引入了文件 c。</p>
<p>第一轮扫描的时候，没有任何文件引入 a，所以会把 a 视作无用文件。</p>
<p>由于 a 引入了 b，所以不会把 b 视作无用的文件，同理 c 也不会视作无用文件。</p>
<p>所以 <strong>第一轮删除只会删掉 a 文件</strong> 。</p>
<p>只要在每次删除后，把 files 范围缩小，比如第一次删除了 a 以后，files 只留下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">[
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"b"</span>,
    <span class="hljs-attr">imports</span>: <span class="hljs-string">"c"</span>,
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">"c"</span>,
  &#125;,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时会发现没有文件再引入 b 了，b 也会被加入无用文件的列表，再重复此步骤，即可删除 c 文件。</p>
<h3 data-id="heading-14">支持 Monorepo</h3>
<p>原项目只考虑到了单个项目和单个 tsconfig 的处理，而如今 monorepo 已经非常流行了，monorepo 中每个项目都有自己的 tsconfig，形成一个自己的 project，而经常有项目 A 里的文件或变量被项目 B 所依赖使用的情况。</p>
<p>而如果单独扫描单个项目内的文件，就会把很多被子项目使用的文件误删掉。</p>
<p>这里的思路也很简单：</p>
<ol>
<li>
<p>增加 <code>--deps</code> 参数，允许传入多个子项目的 tsconfig 路径。</p>
</li>
<li>
<p>过滤子项目扫描出的 <code>imports</code> 部分，找出从别名为 <code>@main</code>的主项目中引入的依赖（比如 <code>import &#123; Button &#125; from '@main/components'</code>）</p>
</li>
<li>
<p>把这部分 <code>imports</code> 合并到主项目的依赖集合中，共同进行接下来的扫描步骤。</p>
</li>
</ol>
<h3 data-id="heading-15">支持自定义文件扫描</h3>
<p>TypeScript 提供的 API，默认只会扫描 <code>.ts, .tsx</code> 后缀的文件，在开启 <code>allowJS</code> 选项后也会扫描 <code>.js, .jsx</code> 后缀的文件。
而项目中很多的 <code>.less, .svg</code> 的文件也都未被使用，但它们都被忽略掉了。</p>
<p>这里我断点跟进 <code>ts.parseJsonConfigFileContent</code> 函数内部，发现有一些比较隐蔽的参数和逻辑，用比较 hack 的方式支持了自定义后缀。</p>
<p>当然，这里还涉及到了一些比较麻烦的改造，比如这个库原本是没有考虑 <code>index.ts, index.less</code> 同时存在这种情况的，通过源码的一些改造最终绕过了这个限制。</p>
<p><strong>目前默认支持了</strong> <code>.less, .sass, .scss</code> <strong>这些类型文件的扫描</strong> ，只要你确保该后缀的引入都是通过 <code>import</code> 语法，那么就可以通过增加的 <code>extraFileExtensions</code> 配置来增加自定义后缀。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> ts <span class="hljs-keyword">from</span> <span class="hljs-string">"typescript"</span>;

<span class="hljs-keyword">const</span> result = ts.parseJsonConfigFileContent(
  parseJsonResult.config,
  ts.sys,
  basePath,
  <span class="hljs-literal">undefined</span>,
  <span class="hljs-literal">undefined</span>,
  <span class="hljs-literal">undefined</span>,
  extraFileExtensions?.map(<span class="hljs-function">(<span class="hljs-params">extension</span>) =></span> (&#123;
    extension,
    <span class="hljs-attr">isMixedContent</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-comment">// hack ways to scan all files</span>
    <span class="hljs-attr">scriptKind</span>: ts.ScriptKind.Deferred,
  &#125;))
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">其他方案：ts-prune</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnadeesha%2Fts-prune" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nadeesha/ts-prune" ref="nofollow noopener noreferrer">ts-prune</a> 是完全基于 TypeScript 服务实现的一个 dead exports 检测方案。</p>
<h3 data-id="heading-17">背景</h3>
<p>TypeScript 服务提供了一个实用的 API： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FTypeScript%2Fblob%2Fmain%2Fsrc%2Fservices%2FfindAllReferences.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/microsoft/TypeScript/blob/main/src/services/findAllReferences.ts" ref="nofollow noopener noreferrer">findAllReferences</a> ，我们平时在 VSCode 里右键点击一个变量，选择 “Find All References” 时，就会调用这个底层 API 找出所有的引用。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdsherret%2Fts-morph" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dsherret/ts-morph" ref="nofollow noopener noreferrer">ts-morph</a> 这个库封装了包括 <code>findAllReferences</code> 在内的一些底层 API，提供更加简洁易用的调用方式。</p>
<p>ts-prune 就是基于 ts-morph 封装而成。</p>
<p>一段最简化的基于 ts-morph 的检测 dead exports 的代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// this could be improved... (ex. ignore interfaces/type aliases that describe a parameter type in the same file)</span>
<span class="hljs-keyword">import</span> &#123; Project, TypeGuards, Node &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"ts-morph"</span>;

<span class="hljs-keyword">const</span> project = <span class="hljs-keyword">new</span> Project(&#123; <span class="hljs-attr">tsConfigFilePath</span>: <span class="hljs-string">"tsconfig.json"</span> &#125;);

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> file <span class="hljs-keyword">of</span> project.getSourceFiles()) &#123;
  file.forEachChild(<span class="hljs-function">(<span class="hljs-params">child</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (TypeGuards.isVariableStatement(child)) &#123;
      <span class="hljs-keyword">if</span> (isExported(child)) child.getDeclarations().forEach(checkNode);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isExported(child)) checkNode(child);
  &#125;);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isExported</span>(<span class="hljs-params">node: Node</span>) </span>&#123;
  <span class="hljs-keyword">return</span> TypeGuards.isExportableNode(node) && node.isExported();
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkNode</span>(<span class="hljs-params">node: Node</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!TypeGuards.isReferenceFindableNode(node)) <span class="hljs-keyword">return</span>;

  <span class="hljs-keyword">const</span> file = node.getSourceFile();
  <span class="hljs-keyword">if</span> (
    node.findReferencesAsNodes().filter(<span class="hljs-function">(<span class="hljs-params">n</span>) =></span> n.getSourceFile() !== file)
      .length === <span class="hljs-number">0</span>
  )
    <span class="hljs-built_in">console</span>.log(
      <span class="hljs-string">`[<span class="hljs-subst">$&#123;file.getFilePath()&#125;</span>:<span class="hljs-subst">$&#123;node.getStartLineNumber()&#125;</span>: <span class="hljs-subst">$&#123;
        TypeGuards.hasName(node) ? node.getName() : node.getText()
      &#125;</span>`</span>
    );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">优点</h3>
<ol>
<li>
<p>TS 的服务被各种 IDE 集成，经过无数大型项目检测，可靠性不用多说。</p>
</li>
<li>
<p>不需要像 ESLint 方案那样，额外检测变量在文件内是否使用， <code>findAllReferences</code> 的检测范围包括文件内部，开箱即用。</p>
</li>
</ol>
<h3 data-id="heading-19">缺点</h3>
<ol>
<li>
<p><strong>速度慢</strong> ，TSProgram 的初始化，以及 <code>findAllReferences</code> 的调用，在大型项目中速度还是有点慢。</p>
</li>
<li>
<p><strong>文档和规范比较差</strong> ，ts-morph 的文档还是太简陋了，挺多核心的方法没有文档描述，不利于维护。</p>
</li>
<li>
<p><strong>模块语法不一致</strong> ，TypeScript 的 <code>findAllReferences</code> 并不识别 Dynamic Import 语法，需要额外处理 <code>import()</code> 形式导入的模块。</p>
</li>
<li>
<p><strong>删除方案难做</strong> ，ts-prune 封装了相对完善的 dead exports 检测方案，但作者似乎没有做自动删除方案的意思。这时 <strong>第二点的劣势</strong>就出来了，按照文档来探索删除方案非常艰难。看起来有个德国的小哥 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnadeesha%2Fts-prune%2Fpull%2F67" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nadeesha/ts-prune/pull/67" ref="nofollow noopener noreferrer">好不容易说服作者</a> 提了一个自动删除的 MR：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnadeesha%2Fts-prune%2Fpull%2F104" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nadeesha/ts-prune/pull/104" ref="nofollow noopener noreferrer">Add a fix mode that automatically fixes unused exports (revival)</a> ，但是最后因为内存溢出没通过 GithubCI，不了了之了。我个人把这套代码 fork 下来在公司内部的大型项目中跑了一下，也确实是<strong>内存溢出</strong> ，看了下自动修复方案的代码，也都是很常规的基于 ts-morph 的 API 调用，猜测是底层 API 的性能问题？</p>
</li>
</ol>
<p>所以综合评估下来，最后还是选择了 ts-unused-exports + ESLint 的方案。</p>
<h2 data-id="heading-20">最后</h2>
<p>我们是字节跳动的 Web Infrastructure Team，作为公司的基础技术团队，我们的目标是提供优秀的技术解决方案，助力公司业务成长，同时打造开放的技术生态，推动公司和业界前端技术的发展。目前团队主要专注的方向包括 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F88616149" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/88616149" ref="nofollow noopener noreferrer">现代 Web 开发解决方案、低代码搭建</a>、Serverless、<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftzxhy.github.io%2F2020%2F02%2F19%2F%25E5%2585%25B3%25E4%25BA%258E%25E8%25B7%25A8%25E7%25AB%25AF%25E6%2596%25B9%25E6%25A1%2588%25E7%259A%2584%25E8%25B0%2583%25E7%25A0%2594%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://tzxhy.github.io/2020/02/19/%E5%85%B3%E4%BA%8E%E8%B7%A8%E7%AB%AF%E6%96%B9%E6%A1%88%E7%9A%84%E8%B0%83%E7%A0%94/" ref="nofollow noopener noreferrer">跨端解决方案</a>、终端基础体验、ToB 等等，已经在多个地方设立了研发团队，包括 北京、上海、杭州、广州、深圳、新加坡。</p>
<p>团队专栏：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fbytedancer" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/bytedancer" ref="nofollow noopener noreferrer">zhuanlan.zhihu.com/bytedancer</a></p>
<p>投递 wx：sshsunlight</p>
<p><strong>部分团队成员：</strong></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fleeight" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/leeight" ref="nofollow noopener noreferrer">github.com/leeight</a> (Team Leader)</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdexteryy" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/dexteryy" ref="nofollow noopener noreferrer">github.com/dexteryy</a> (JS Hacker, SF/F Nerd)</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Funderfin" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/underfin" ref="nofollow noopener noreferrer">github.com/underfin</a> (Vue.js Core Contributor)</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FAmour1688" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Amour1688" ref="nofollow noopener noreferrer">github.com/Amour1688</a> (Vue.js Contributor)</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Foyyd" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/oyyd" ref="nofollow noopener noreferrer">github.com/oyyd</a> (Node.js Core Contributor)</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftheanarkh" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/theanarkh" ref="nofollow noopener noreferrer">github.com/theanarkh</a> (Node.js Advocate)</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fleizongmin" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/leizongmin" ref="nofollow noopener noreferrer">github.com/leizongmin</a> (Node.js Advocate)</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flosfair" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/losfair" ref="nofollow noopener noreferrer">github.com/losfair</a> (WebAssembly)</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FBrooooooklyn" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Brooooooklyn" ref="nofollow noopener noreferrer">github.com/Brooooookly…</a> (Rust & <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnapi.rs%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://napi.rs/" ref="nofollow noopener noreferrer">napi.rs/</a>)</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Famio" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/amio" ref="nofollow noopener noreferrer">github.com/amio</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fniudai" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/niudai" ref="nofollow noopener noreferrer">github.com/niudai</a> & <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhihu.com%2Fpeople%2Fniu-dai-68-44" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhihu.com/people/niu-dai-68-44" ref="nofollow noopener noreferrer">www.zhihu.com/people/niu-…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fprotoman92" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/protoman92" ref="nofollow noopener noreferrer">github.com/protoman92</a></li>
</ul></div>  
</div>
            