
---
title: '如何使 commitlint 和 commitizen 共用规则配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=961'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 03:29:13 GMT
thumbnail: 'https://picsum.photos/400/300?random=961'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>规范 Git 提交信息的工具有：commitlint 和 commitizen。</p>
<p>两者各有专攻，commitlint 校验提交信息，commitizen 辅助填写提交信息；在 Git 提交工作流程中，commitlint 作用于 <code>commit-msg</code> 阶段，commitizen作用于 <code>pre-commit</code>。互不干扰，各司其职，相辅相成。</p>
<p>看似天下太平，然而，两者遵循各自的规则配置，没个统一接口各干各的。在同一流程中协作，用两套规则配置，总有些闹心。</p>
<h1 data-id="heading-0">为什么不能统一呢？</h1>
<p>好好的为什么就不能用同一份规则配置呢？因为这俩工具的机制是在是太不一样了。</p>
<h2 data-id="heading-1">commitlint</h2>
<p>先来说说 commitlint，听这名字就知道是 lint 一脉的，容易想到 eslint、stylelint，机制上也有些相似。</p>
<p>我们知道目前认同范围最广的基础规范是<a href="https://www.conventionalcommits.org/zh-hans/v1.0.0-beta.4/" target="_blank" rel="nofollow noopener noreferrer">约定式提交 (conventionalcommits)</a></p>
<pre><code class="copyable"><type>[scope]: <subject>

[body]

[footer]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它由 <code>type</code>、<code>scope</code>、<code>subject</code>、<code>body</code>、<code>footer</code> 几部分组成，commitlint 成立于这套基础规范之上，也就是说，它相信一条提交信息字符串是可以被解析成这几部分的，然后再检查各部分是否符合规定。</p>
<p>了解到 commitlint 的思路后，它的运行机制也好理解了。简单来说，它的运行过程是：解析提交信息 → 确定规则集 → 执行规则检查</p>
<h3 data-id="heading-2">解析提交信息</h3>
<p>首先它通过 <code>parserPreset</code> 解析器将提交信息字符串解析为结构对象，例如：</p>
<p>例如：如下提交信息</p>
<pre><code class="copyable">fix(package1): update title

The old title is overdated

Issues: https://github.com/conventional-changelog/commitlint/issues/2507
<span class="copy-code-btn">复制代码</span></code></pre>
<p>被解析为</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"header"</span>: <span class="hljs-string">"fix(package1): update title"</span>,
  <span class="hljs-attr">"type"</span>: <span class="hljs-string">"fix"</span>,
  <span class="hljs-attr">"scope"</span>: <span class="hljs-string">"package1"</span>,
  <span class="hljs-attr">"subject"</span>: <span class="hljs-string">"update title"</span>,
  <span class="hljs-attr">"body"</span>: <span class="hljs-string">"The old title is overdated"</span>,
  <span class="hljs-attr">"footer"</span>: <span class="hljs-string">"Issues: https://github.com/conventional-changelog/commitlint/issues/2507"</span>,
  <span class="hljs-attr">"references"</span>: [
    <span class="hljs-string">"https://github.com/conventional-changelog/commitlint/issues/2507"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">确定规则集</h3>
<p>接着，它根据规则配置文件生成规则集。commitlint 的配置文件是 <code>commitlint.config.js</code>，配置文件里有 <code>extends</code>，<code>rules</code>，<code>plugins</code> 等字段。用过 eslint 的朋友可能会觉得熟悉，和 eslint 相似配置中的 <code>extends</code> 字段继承已有配置，<code>rules</code> 定义具体规则。</p>
<p>一言概之，在这一步它把配置文件解析成后续能使用的规则集。我们截一小段看看规则集大概的样子：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    'subject-full-stop': [<span class="hljs-number">2</span>, 'never', '.'],
    'subject-case': [
        <span class="hljs-number">2</span>,
        'never',
        ['sentence-case', 'start-case', 'pascal-case', 'upper-case'],
    ],
    'subject-empty': [<span class="hljs-number">2</span>, 'never'],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>键是规则名，值是规则参数。一个规则实际上对应一个逻辑函数， commitlint 内置的规则逻辑由 <a href="https://github.com/curly210102/commitlint/blob/master/%40commitlint/rules/src/index.ts" target="_blank" rel="nofollow noopener noreferrer">一个键值对列表</a> 维护。我们取 <code>subject-full-stop</code> 的逻辑函数看看。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// subject-full-stop.ts</span>
<span class="hljs-keyword">import</span> message <span class="hljs-keyword">from</span> <span class="hljs-string">'@commitlint/message'</span>;
<span class="hljs-keyword">import</span> &#123;SyncRule&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@commitlint/types'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> subjectFullStop: SyncRule<<span class="hljs-built_in">string</span>> = <span class="hljs-function">(<span class="hljs-params">
parsed,
when = <span class="hljs-string">'always'</span>,
value = <span class="hljs-string">'.'</span>
</span>) =></span> &#123;
<span class="hljs-keyword">const</span> input = parsed.subject;

<span class="hljs-keyword">if</span> (!input) &#123;
<span class="hljs-keyword">return</span> [<span class="hljs-literal">true</span>];
&#125;

<span class="hljs-keyword">const</span> negated = when === <span class="hljs-string">'never'</span>;
<span class="hljs-keyword">const</span> hasStop = input[input.length - <span class="hljs-number">1</span>] === value;

<span class="hljs-keyword">return</span> [
negated ? !hasStop : hasStop,
message([<span class="hljs-string">'subject'</span>, negated ? <span class="hljs-string">'may not'</span> : <span class="hljs-string">'must'</span>, <span class="hljs-string">'end with full stop'</span>]),
];
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>subject-full-stop</code> 函数接受的第一个参数 <code>parsed</code> 是第一步产生的结构对象；第二个参数 <code>when</code> 是规则值中第二个元素，代表条件前缀是或者非；第三个参数 <code>value</code> 是规则值中的第三个元素，代表具体值。</p>
<p><code>subject-full-stop</code> 函数返回校验结果和错误提示信息。</p>
<p>现在再来看看规则的含义，比如</p>
<ul>
<li><code>'subject-full-stop': [2, 'never', '.']</code> ：表示标题不能以 <code>.</code> 结束</li>
<li><code>'subject-full-stop: [2, 'always', '!']'</code> ：表示标题必须以 <code>!</code> 结束</li>
</ul>
<p>回看上面 <code>subject-full-stop</code> 函数的逻辑的确可以表达这个意思。</p>
<h3 data-id="heading-4">执行规则检查</h3>
<p>拥有「规则集」和「提交信息解析对象」后，这一阶段 commitlint 遍历「规则集」并执行相对应逻辑函数，最终格式化校验结果并输出报告。</p>
<h2 data-id="heading-5">commitizen</h2>
<p>commitlint 和配置文件直接交流，不同的是，commitizen 本身与提交信息规则并无关系。commitizen 只提供与 Git 交互的框架，它传递 <code>inquirer</code> 对象给适配器（Adapter），由适配器负责描述命令行填写流程并返回用户填写的信息。因此真正起核心作用，与规则相关的是适配器。</p>
<p><em><a href="https://www.npmjs.com/package/inquirer" target="_blank" rel="nofollow noopener noreferrer">inquirer</a> 是封装了常见命令行交互界面的一个工具集，它支持快速使用 input、confirm、list、checkbox、editor 等常用命令行界面。</em></p>
<p>大多数 commitizen 适配器都是按特定的规范来描述命令行交互流程，比如基于 conventional-changelog 规范的 <a href="https://www.npmjs.com/package/cz-conventional-changelog" target="_blank" rel="nofollow noopener noreferrer">cz-conventional-changelog</a>。这样的机制下，如果开发者需要自定规则，得学习使用 inquirer 从头创造一个新的适配器，这实在是不太易用。那么有没有支持自定义的适配器存在呢？有的，<a href="https://github.com/leoforfree/cz-customizable" target="_blank" rel="nofollow noopener noreferrer">cz-customizable</a> 就是这特殊的存在。</p>
<p>cz-customizable 对外设定了一份配置文件 <code>.cz-config.js</code>，设计了一些可配置字段，cz-customizable 读入配置并将其转换为基于 inquirer 的命令行交互流程。</p>
<p>cz-customizable 的配置示例如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// type 可选列表</span>
  <span class="hljs-attr">types</span>: [
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'feat'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'feat:     A new feature'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'fix'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'fix:      A bug fix'</span> &#125;,
  ],
  <span class="hljs-comment">// scope 可选列表</span>
  <span class="hljs-attr">scopes</span>: [&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'accounts'</span> &#125;, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'admin'</span> &#125;, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'exampleScope'</span> &#125;, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'changeMe'</span> &#125;],
  <span class="hljs-comment">// 覆盖交互提示信息</span>
  <span class="hljs-attr">messages</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">"请选择你的提交类型"</span>,
    <span class="hljs-attr">scope</span>: <span class="hljs-string">'请选择 SCOPE'</span>,
    <span class="hljs-attr">subject</span>: <span class="hljs-string">'简短描述本次修改:\n'</span>,
    <span class="hljs-attr">body</span>: <span class="hljs-string">'提供关于本次修改更具体的信息（可选），使用 "|" 换行：\n'</span>,
    <span class="hljs-attr">confirmCommit</span>: <span class="hljs-string">'确定提交信息？'</span>,
  &#125;,
  <span class="hljs-comment">// skip any questions you want</span>
  <span class="hljs-attr">skipQuestions</span>: [<span class="hljs-string">'body'</span>],
  <span class="hljs-comment">// limit subject length</span>
  <span class="hljs-attr">subjectLimit</span>: <span class="hljs-number">100</span>,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">怎么实现共用？</h1>
<p>了解 commitlint 和 commitizen 的机制之后，我们来考虑核心问题：怎么使两者共用同一份规则配置。</p>
<p>有两种思路：</p>
<ol>
<li>从 commitlint 配置出发，读取 commitlint 配置并生成对应的命令行提交流程，即创造一个 commitizen 适配器，<a href="https://www.npmjs.com/package/@commitlint/cz-commitlint" target="_blank" rel="nofollow noopener noreferrer">@commitlint/cz-commitlint</a> 已实现</li>
<li>从 cz-customizable 配置出发，将 cz-customizable 配置翻译为 commitlint 规则，即创造一个 commitlint 配置，<a href="https://www.npmjs.com/package/commitlint-config-cz" target="_blank" rel="nofollow noopener noreferrer">commitlint-config-cz</a> 已实现</li>
</ol>
<h2 data-id="heading-7">cz-commitlint</h2>
<p><a href="https://www.npmjs.com/package/@commitlint/cz-commitlint" target="_blank" rel="nofollow noopener noreferrer">@commitlint/cz-commitlint</a> 配置过程很简单</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装 commitizen 和 commitlint 和 cz-commitlint</span>
npm install --save-dev @commitlint/cz-commitlint commitizen @commitlint/cli
<span class="hljs-comment"># or yarn</span>
yarn add -D @commitlint/cz-commitlint commitizen @commitlint/cli
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 package.json 中配置 commitizen 适配器</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"commit"</span>: <span class="hljs-string">"git-cz"</span>
  &#125;,
  <span class="hljs-attr">"config"</span>: &#123;
    <span class="hljs-attr">"commitizen"</span>: &#123;
      <span class="hljs-attr">"path"</span>: <span class="hljs-string">"@commitlint/cz-commitlint"</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装并配置所需的规范，比如 conventional-changelog 规范</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install --save-dev @commitlint/config-conventional
<span class="hljs-comment"># or yarn</span>
yarn add -D @commitlint/config-conventional

<span class="hljs-comment"># 配置 commitlint.config.js</span>
<span class="hljs-built_in">echo</span> <span class="hljs-string">"module.exports = &#123;extends: ['@commitlint/config-conventional']&#125;;"</span> > commitlint.config.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">commitlint-config-cz</h2>
<p><a href="https://www.npmjs.com/package/commitlint-config-cz" target="_blank" rel="nofollow noopener noreferrer">commitlint-config-cz</a>  的配置过程也不复杂</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 安装 commitizen 和 commitlint 和 cz-customizable 和 commitlint-config-cz</span>
npm install --save-dev commitlint-config-cz commitizen cz-customizable @commitlint/cli
<span class="hljs-comment"># or yarn</span>
yarn add -D commitlint-config-cz commitizen cz-customizable @commitlint/cli
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 package.json 中配置 commitizen 适配器</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"commit"</span>: <span class="hljs-string">"git-cz"</span>
  &#125;,
  <span class="hljs-attr">"config"</span>: &#123;
    <span class="hljs-attr">"commitizen"</span>: &#123;
      <span class="hljs-attr">"path"</span>: <span class="hljs-string">"node_modules/cz-customizable"</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 commitlint.config.js 中配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">extends</span>: [
        <span class="hljs-string">'cz'</span>
    ]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置 <code>.cz-config.js</code>，可以选择以 <a href="https://github.com/leoforfree/cz-customizable/blob/master/cz-config-EXAMPLE.js" target="_blank" rel="nofollow noopener noreferrer">官方模板</a> 为基础。</p>
<h2 data-id="heading-9">如何选择</h2>
<p>两者各有适用场景</p>
<p><a href="https://www.npmjs.com/package/@commitlint/cz-commitlint" target="_blank" rel="nofollow noopener noreferrer">@commitlint/cz-commitlint</a> 适合使用已有规范，或基于已有规范进行自定义扩展的情况。</p>
<p><a href="https://www.npmjs.com/package/commitlint-config-cz" target="_blank" rel="nofollow noopener noreferrer">commitlint-config-cz</a> 适合不依赖已有规范完全自定义的场景。</p>
<p>cz-commitlint 也能实现完全自定义，但需要了解 commitlint 的<a href="https://github.com/conventional-changelog/commitlint/blob/master/docs/reference-configuration.md" target="_blank" rel="nofollow noopener noreferrer">配置</a>和 <a href="https://github.com/conventional-changelog/commitlint/blob/master/docs/reference-rules.md" target="_blank" rel="nofollow noopener noreferrer">规则</a>，相较于 <code>.cz-config.js</code> 简单直观的配置会增加一点门槛，不过这对于适应 eslint 的前端开发者来说或许不是一个问题。</p></div>  
</div>
            