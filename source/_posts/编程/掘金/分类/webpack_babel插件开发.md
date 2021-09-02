
---
title: 'webpack_babel插件开发'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4938'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 22:26:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=4938'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">需求</h3>
<p>不同环境下前端使用不同的配置</p>
<h3 data-id="heading-1">babel插件</h3>
<h4 data-id="heading-2">Babel的工作过程</h4>
<p>Babel的处理过程主要为3个：<em><strong>解析(parse)</strong></em>、<em><strong>转换(transform)</strong></em>、<em><strong>生成(generate)</strong></em>。</p>
<ul>
<li>
<p>解析</p>
<p>解析主要包含两个过程：词法分析和语法分析，输入是代码字符串，输出是AST。</p>
</li>
<li>
<p>转换</p>
<p>处理AST。处理工具、插件等就是在这个过程中介入，将代码按照需求进行转换。</p>
</li>
<li>
<p>生成</p>
<p>遍历AST，输出代码字符串。</p>
</li>
</ul>
<p>解析和生成过程，都有Babel都为我们处理得很好了，我们要做的就是在 <em><strong>转换</strong></em> 过程中搞事情，进行个性化的定制开发。</p>
<h4 data-id="heading-3">尝试开发</h4>
<p>npm安装开发中用到的依赖 <code>@babel/core</code>(模拟运行babel)和 <code>@babel/types</code>(对语法树进行操作):</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install @babel/core @babel/types
<span class="copy-code-btn">复制代码</span></code></pre>
<p>咱们晓得<code>babel</code>能编译es6代码，例如最根底的<code>const</code>和箭头函数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// es2015 的 const 和 arrow function</span>
<span class="hljs-keyword">const</span> add = <span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a + b;

<span class="hljs-comment">// Babel 转译后</span>
<span class="hljs-keyword">var</span> add = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a + b;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>咱们能够到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fastexplorer.net%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://astexplorer.net/" ref="nofollow noopener noreferrer">astexplorer</a> 查看生成的语法树：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Program"</span>,
  <span class="hljs-attr">"body"</span>: [
    &#123;
      <span class="hljs-attr">"type"</span>: <span class="hljs-string">"VariableDeclaration"</span>, <span class="hljs-comment">// 变量申明</span>
      <span class="hljs-attr">"declarations"</span>: [ <span class="hljs-comment">// 具体申明</span>
        &#123;
          <span class="hljs-attr">"type"</span>: <span class="hljs-string">"VariableDeclarator"</span>, <span class="hljs-comment">// 变量申明</span>
          <span class="hljs-attr">"id"</span>: &#123;
            <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>, <span class="hljs-comment">// 标识符（最根底的）</span>
            <span class="hljs-attr">"name"</span>: <span class="hljs-string">"add"</span> <span class="hljs-comment">// 函数名</span>
          &#125;,
          <span class="hljs-attr">"init"</span>: &#123;
            <span class="hljs-attr">"type"</span>: <span class="hljs-string">"ArrowFunctionExpression"</span>, <span class="hljs-comment">// 箭头函数</span>
            <span class="hljs-attr">"id"</span>: <span class="hljs-literal">null</span>,
            <span class="hljs-attr">"expression"</span>: <span class="hljs-literal">true</span>,
            <span class="hljs-attr">"generator"</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">"params"</span>: [ <span class="hljs-comment">// 参数</span>
              &#123;
                <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
                <span class="hljs-attr">"name"</span>: <span class="hljs-string">"a"</span>
              &#125;,
              &#123;
                <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
                <span class="hljs-attr">"name"</span>: <span class="hljs-string">"b"</span>
              &#125;
            ],
            <span class="hljs-attr">"body"</span>: &#123; <span class="hljs-comment">// 函数体</span>
              <span class="hljs-attr">"type"</span>: <span class="hljs-string">"BinaryExpression"</span>, <span class="hljs-comment">// 二项式</span>
              <span class="hljs-attr">"left"</span>: &#123; <span class="hljs-comment">// 二项式右边</span>
                <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
                <span class="hljs-attr">"name"</span>: <span class="hljs-string">"a"</span>
              &#125;,
              <span class="hljs-attr">"operator"</span>: <span class="hljs-string">"+"</span>, <span class="hljs-comment">// 二项式运算符</span>
              <span class="hljs-attr">"right"</span>: &#123; <span class="hljs-comment">// 二项式左边</span>
                <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Identifier"</span>,
                <span class="hljs-attr">"name"</span>: <span class="hljs-string">"b"</span>
              &#125;
            &#125;
          &#125;
        &#125;
      ],
      <span class="hljs-attr">"kind"</span>: <span class="hljs-string">"const"</span>
    &#125;
  ],
  <span class="hljs-attr">"sourceType"</span>: <span class="hljs-string">"module"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以做一简单箭头函数转换成普通函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> types = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/types'</span>);
<span class="hljs-keyword">const</span> babel = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/core'</span>);

<span class="hljs-keyword">let</span> code = <span class="hljs-string">`let add = (a, b)=>&#123;return a+b&#125;`</span>;
<span class="hljs-keyword">let</span> ArrowPlugins = &#123;
<span class="hljs-attr">visitor</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">ArrowFunctionExpression</span>(<span class="hljs-params">path</span>)</span> &#123;
      <span class="hljs-keyword">let</span> &#123; node &#125; = path;
      <span class="hljs-keyword">let</span> body = node.body;
      <span class="hljs-keyword">let</span> params = node.params;
      <span class="hljs-keyword">let</span> r = types.functionExpression(<span class="hljs-literal">null</span>, params, body, <span class="hljs-literal">false</span>, <span class="hljs-literal">false</span>);
      path.replaceWith(r);
    &#125;
  &#125;
&#125;
babel.transform(code, &#123;
  <span class="hljs-attr">filename</span>: <span class="hljs-string">'test.js'</span>,
  <span class="hljs-attr">plugins</span>: [
    ArrowPlugins
  ]
&#125;, <span class="hljs-function">(<span class="hljs-params">err, result</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(err)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'++++++++++ test +++++++++'</span>);
  <span class="hljs-built_in">console</span>.log(result.code);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'++++++++++ test end +++++++++'</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行后输出结果</p>
<pre><code class="hljs language-bash copyable" lang="bash">undefined
++++++++++ <span class="hljs-built_in">test</span> end +++++++++
var add = <span class="hljs-keyword">function</span> add(a, b) &#123; <span class="hljs-built_in">return</span> a + b; &#125;;
++++++++++ <span class="hljs-built_in">test</span> +++++++++
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">需求开发</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> env = process.env.CI_FE_ENV;
<span class="hljs-keyword">const</span> importPlugin = <span class="hljs-function">(<span class="hljs-params">&#123; types &#125;</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">visitor</span>: &#123;

      <span class="hljs-function"><span class="hljs-title">ImportDeclaration</span>(<span class="hljs-params">path, source</span>)</span> &#123;
        <span class="hljs-keyword">let</span> node = path.node
        
        <span class="hljs-comment">// 判断只有导入的文件为‘@/config’的时候才进行替换</span>
        <span class="hljs-keyword">if</span> (node.source.value === <span class="hljs-string">'@/config'</span>) &#123;
          <span class="hljs-keyword">let</span> specifiers = []
          node.specifiers.map(<span class="hljs-function">(<span class="hljs-params">specifier</span>) =></span> &#123;
          
            <span class="hljs-comment">// 引入默认配置</span>
            <span class="hljs-keyword">let</span> defaultLocal = types.importDefaultSpecifier(types.identifier(<span class="hljs-string">'__default_config'</span>));
            <span class="hljs-keyword">const</span> newimport = types.importDeclaration([defaultLocal],types.stringLiteral(node.source.value+<span class="hljs-string">"/default.config.js"</span>))
            specifiers.push(newimport)
            
            <span class="hljs-comment">// 引入环境对应配置</span>
            <span class="hljs-keyword">let</span> envLocal = types.importDefaultSpecifier(types.identifier(<span class="hljs-string">'__env_config'</span>));
            <span class="hljs-keyword">const</span> newimport2 = types.importDeclaration([envLocal],types.stringLiteral(node.source.value+<span class="hljs-string">`/<span class="hljs-subst">$&#123;env&#125;</span>.config.js`</span>))
            specifiers.push(newimport2)
            
            <span class="hljs-comment">// 进行配置合并</span>
            <span class="hljs-keyword">const</span> newconfigVar = types.variableDeclaration(<span class="hljs-string">"const"</span>, [
              types.variableDeclarator(specifier.local, 
                types.objectExpression([
                  types.spreadElement(types.identifier(<span class="hljs-string">'__default_config'</span>)),
                  types.spreadElement(types.identifier(<span class="hljs-string">'__env_config'</span>)),
                ]),
              ),
            ]);
            specifiers.push(newconfigVar)
          &#125;);
          
          <span class="hljs-comment">// 替换当前绑定</span>
          path.replaceWithMultiple(specifiers)

        &#125;
      &#125;,
    &#125;,
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            