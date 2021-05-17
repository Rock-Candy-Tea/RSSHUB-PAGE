
---
title: '《从 0 到 1 手写 babel》思路分享'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63717d7589cf415680373ede5f4f7089~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 16 May 2021 04:21:53 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63717d7589cf415680373ede5f4f7089~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>周末我在开心地写着小册的时候，不小心碰倒了饮料，撒了一些在键盘上，虽然我很快的收拾了一下，但电脑却突然关机了。我尝试着重启了一下发现启动不了了，最终确认它坏掉了。</p>
<p>电脑坏掉倒不是我最担心的，主要是我答应了很多读者要下周上线小册，不能再鸽了，可是现在不得不鸽了，因为代码全在那台电脑。</p>
<p>我在想着怎么弥补比较好，想起不少人期待最后的《手写简易的 babel》那个案例的，正好我最近也在写那个案例了，我想着要不提前分享下思路吧。算是一些补偿（也公布下再鸽几天的消息）。</p>
<h2 data-id="heading-1">整体思路</h2>
<h3 data-id="heading-2">babel 的编译流程</h3>
<p>我们知道，babel 的主要编译流程是 parse、transform、generate。</p>
<ul>
<li>parse 是把源码转成 AST</li>
<li>transform 是对 AST 做增删改</li>
<li>generate 是打印 AST 成目标代码并生成 sourcemap</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63717d7589cf415680373ede5f4f7089~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">babel7 内置的包</h3>
<p>babel 7 把这些功能的实现放到了不同的包里面：</p>
<ul>
<li><code>@babel/parser</code> 解析源码成 AST，对应 parse 阶段</li>
<li><code>@babel/traverse</code> 遍历 AST 并调用 visitor 函数，对应 transform 阶段</li>
<li><code>@babel/generate</code> 打印 AST，生成目标代码和 sorucemap，对应 generate 阶段</li>
</ul>
<p>其中，遍历过程中需要创建 AST，会用到：</p>
<ul>
<li><code>@babel/types</code> 创建、判断 AST</li>
<li><code>@babel/template</code>  根据模块批量创建 AST</li>
</ul>
<p>上面是每一个阶段的功能， babel 整体功能的入口是在：</p>
<ul>
<li><code>@babel/core</code> 解析配置、应用 plugin、preset，整体整体编译流程</li>
</ul>
<p>插件和插件之间有一些公共函数，这些都是在：</p>
<ul>
<li><code>@babel/helpers</code> 用于转换 es next 代码需要的通过模板创建的 AST，比如 _typeof、_defineProperties 等</li>
<li><code>@babel/helper-xxx</code> 其他的插件之间共享的用于操作 AST 的公共函数</li>
</ul>
<p>当然，除了编译期转换的时候会有公共函数以外，运行时也有，这部分是放在：</p>
<ul>
<li><code>@babel/runtime</code> 主要是包含 corejs、helpers、regenerator 这 3 部分：
<ul>
<li>helper： helper 函数的运行时版本（不是通过 AST 注入了，而是运行时引入代码）</li>
<li>corejs： es next 的 api 的实现，corejs 2 只支持静态方法，corejs 3 还支持实例方法</li>
<li>regenerator：async await 的实现，由 facebook 维护</li>
</ul>
</li>
</ul>
<p>（babel 做语法转换是自己实现的 helper，但是做 polyfill 都不是自己实现的，而是借助了第三方的 corejs、regenerator）</p>
<h3 data-id="heading-4">我们要实现哪些包</h3>
<p>上面介绍的是 babel 完成功能所内置的一些包，我们如果要写一个简易的 babel，也得实现这些包，但可以做一些简化。</p>
<ul>
<li><code>parser 包</code>是肯定要实现的，babel parser 是基于 acorn fork 的，我们也基于 acorn，做一点扩展。完成从源码到 AST 的转换。</li>
<li><code>traverse 包</code>是对 AST 的遍历，需要知道不同类型的 AST 都遍历哪些 key，这些是在 @babel/types 包里面定义的，我们也用类似的实现方式，并且会调用对应的 visitor，实现 path 和 path.scope 的一些 api 然后传入。</li>
<li><code>generate 包</code>是打印 AST 成目标代码，生成 sourcemap。打印这部分每个 AST 类型都要写一个对应的函数来处理，生成 sourcemap 使用 source-map 这个包，关联 parse 时记录的 loc 和打印时计算的位置来生成每一个 mapping。</li>
<li><code>types 包</code>用于创建 AST，会维护创建和判断各种 AST 的 api，并且提供每种 AST 需要遍历的属性是哪些，用于 traverse 的过程</li>
<li><code>template 包</code>是批量创建 AST 的，这里我们实现一个简单的版本，传入字符串，parse 成 AST 返回。</li>
<li><code>core 包</code>是整体流程的串联，支持 plugins 和 presets，调用插件，合并成最终的 visitors，然后再 traverse。</li>
<li><code>helper 包</code>我们也会实现一个，因为支持了 plugin，那么中有一些公共的函数可以复用</li>
<li><code>runtime 包</code>我们也提供一下，不过只加入一些用于做语法转换的辅助函数就好了</li>
</ul>
<p>这是我们大概会做的事情，把这些都实现一遍就算一个比较完整的 babel 了。实现的过程中更能加深我们对 babel、对转译器的认识，不只是掌握 babel 本身。</p>
<p>下面我们来详细分析一下每一步的具体思路：</p>
<h2 data-id="heading-5">代码实现</h2>
<p>(因为代码在那台坏掉的电脑拿不出来，加上这也不是小册里，所以只会提供思路，等小册上线会提供完整源码的)</p>
<p>为了简化，我们不做分包了，把代码都放在一个包里实现。</p>
<h3 data-id="heading-6">parser</h3>
<p>主流的 parser 有 esprima、acorn 等，acorn 是最流行的，babel parser 是 fork 自 acorn，做了很多修改。我们不需要 fork，基于 acorn 的插件机制做一些扩展即可。</p>
<p>比如 acorn 所 parse 出的 AST 只有 Literal （字面量）类型，不区分具体是字符串、数字或者布尔等字面量，而 babel parser 把它们细化成了 StringLiteral、NumericLiteral、BooleanLiteral 等 AST。</p>
<p>我们就实现一下对 AST 做了这种扩展的 parser。</p>
<p>我们先用一下原本的 acorn parser：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> acorn = <span class="hljs-built_in">require</span>(<span class="hljs-string">"acorn"</span>);

<span class="hljs-keyword">const</span> Parser = acorn.Parser;

<span class="hljs-keyword">const</span> ast = Parser.parse(<span class="hljs-string">`
    const a = 1;
`</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">JSON</span>.stringify(ast, <span class="hljs-literal">null</span>, <span class="hljs-number">2</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/457ac0aa40e341f1b3210515e1b6b72e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到数字字面量 parse 的结果是 Literal，这样判断类型还需要去看下值的类型，才能确定是什么字面量，比较麻烦。这也是为什么 babel 把它们做了细化。</p>
<p>我们也细化一下：</p>
<p>acorn 扩展的方式是继承 + 重写，继承之前的 parser，重写一些方法，返回新 parser。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> acorn = <span class="hljs-built_in">require</span>(<span class="hljs-string">"acorn"</span>);

<span class="hljs-keyword">const</span> Parser = acorn.Parser;

<span class="hljs-keyword">var</span> literalExtend = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">Parser</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Parser</span> </span>&#123;
    parseLiteral (...args) &#123;
        <span class="hljs-keyword">const</span> node = <span class="hljs-built_in">super</span>.parseLiteral(...args);
        <span class="hljs-keyword">switch</span>(<span class="hljs-keyword">typeof</span> node.value) &#123;
            <span class="hljs-keyword">case</span> <span class="hljs-string">'number'</span>:
                node.type = <span class="hljs-string">'NumericLiteral'</span>;
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> <span class="hljs-string">'string'</span>:
                node.type = <span class="hljs-string">'StringLiteral'</span>;
                <span class="hljs-keyword">break</span>;
        &#125;
        <span class="hljs-keyword">return</span>  node;
    &#125;
  &#125;
&#125;
<span class="hljs-keyword">const</span> newParser = Parser.extend(literalExtend);

<span class="hljs-keyword">const</span> ast = newParser.parse(<span class="hljs-string">`
    const a = 1;
`</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">JSON</span>.stringify(ast, <span class="hljs-literal">null</span>, <span class="hljs-number">2</span>));

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在 parse 的时候就判断了字面量的类型，然后设置了 type。</p>
<p>试下效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac926af7d2194423b7855bb2d0ba05fb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样，我们就实现了类似 babel parser 对 acorn 的扩展。</p>
<p>当然，babel parser 的扩展有很多，这里我们只是简单实现，理清思路即可。</p>
<h3 data-id="heading-7">traverse</h3>
<p>遍历 AST 是一个深度优先搜索的过程，当处理到具体的 AST 节点我们要知道怎么继续遍历子 AST 节点。</p>
<p>在 babel types 包中定义了不同 AST 怎么遍历（visitor）、怎么创建（builder）、怎么判断（fidelds.validate）以及别名（alias）。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f9a7fd766f84365969108c9bb72a733~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里我们也需要维护每种 AST 怎么遍历的数据：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> AST_DEFINATIONS_MAP = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();

AST_DEFINATIONS_MAP.set(<span class="hljs-string">'Program'</span>, &#123;
    <span class="hljs-attr">visitor</span>: [<span class="hljs-string">'body'</span>]
&#125;);
AST_DEFINATIONS_MAP.set(<span class="hljs-string">'VariableDeclaration'</span>, &#123;
    <span class="hljs-attr">visitor</span>: [<span class="hljs-string">'declarations'</span>]
&#125;);
AST_DEFINATIONS_MAP.set(<span class="hljs-string">'VariableDeclarator'</span>, &#123;
    <span class="hljs-attr">visitor</span>: [<span class="hljs-string">'id'</span>, <span class="hljs-string">'init'</span>]
&#125;);
AST_DEFINATIONS_MAP.set(<span class="hljs-string">'Identifier'</span>, &#123;&#125;);
AST_DEFINATIONS_MAP.set(<span class="hljs-string">'NumericLiteral'</span>, &#123;&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后基于这些数据对 AST 进行深度优先遍历：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">traverse</span>(<span class="hljs-params">node</span>) </span>&#123;
    <span class="hljs-keyword">const</span> defination = astDefinationsMap.get(node.type);

    <span class="hljs-built_in">console</span>.log(node.type);

    <span class="hljs-keyword">if</span> (defination.visitor) &#123;
        defination.visitor.forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
            <span class="hljs-keyword">const</span> prop = node[key];
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(prop)) &#123; <span class="hljs-comment">// 如果该属性是数组</span>
                prop.forEach(<span class="hljs-function"><span class="hljs-params">childNode</span> =></span> &#123;
                    traverse(childNode);
                &#125;)
            &#125; <span class="hljs-keyword">else</span> &#123;
                traverse(prop);
            &#125;
        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印结果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38268e5c690f47589819bdc1a61c3862~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>对照下刚才的 AST 结构，确实实现了深度优先遍历。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07baf7a0e64a41feb00feff4c25d5bff~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">visitor</h4>
<p>遍历之后，我们要实现 visitors 的功能，在遍历的过程中对 AST 做增删改。这个就是遍历的过程中根据 node.type 来调用对应的 visitor 函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">traverse</span>(<span class="hljs-params">node, visitors</span>) </span>&#123;
    <span class="hljs-keyword">const</span> defination = astDefinationsMap.get(node.type);

    <span class="hljs-keyword">const</span> visitorFunc = visitors[node.type];

    <span class="hljs-keyword">if</span>(visitorFunc && <span class="hljs-keyword">typeof</span> visitorFunc === <span class="hljs-string">'function'</span>) &#123;
        visitorFunc(node);
    &#125;


    <span class="hljs-keyword">if</span> (defination.visitor) &#123;
        defination.visitor.forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
            <span class="hljs-keyword">const</span> prop = node[key];
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(prop)) &#123; <span class="hljs-comment">// 如果该属性是数组</span>
                prop.forEach(<span class="hljs-function"><span class="hljs-params">childNode</span> =></span> &#123;
                    traverse(childNode, visitors);
                &#125;)
            &#125; <span class="hljs-keyword">else</span> &#123;
                traverse(prop, visitors);
            &#125;
        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来试验一下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">traverse(ast, &#123;
    <span class="hljs-function"><span class="hljs-title">Identifier</span>(<span class="hljs-params">node</span>)</span> &#123;
        node.name = <span class="hljs-string">'b'</span>;
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后再次查看 AST，发现 Identifier 的 name 已经从 a 变成了 b</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce0ec5498e5042dcb017ffe963f561d4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>babel 的 visitor 也支持指定 enter、exit 来选择在遍历子节点之前和之后调用，如果传入的是函数，那么就被当做 enter：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">traverse</span>(<span class="hljs-params">node, visitors</span>) </span>&#123;
    <span class="hljs-keyword">const</span> defination = astDefinationsMap.get(node.type);

    <span class="hljs-keyword">let</span> visitorFuncs = visitors[node.type] || &#123;&#125;;

    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> visitorFuncs === <span class="hljs-string">'function'</span>) &#123;
        visitorFuncs = &#123;
            <span class="hljs-attr">enter</span>: visitorFuncs
        &#125;
    &#125;

    visitorFuncs.enter && visitorFuncs.enter(node);

    <span class="hljs-keyword">if</span> (defination.visitor) &#123;
        defination.visitor.forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
            <span class="hljs-keyword">const</span> prop = node[key];
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(prop)) &#123; <span class="hljs-comment">// 如果该属性是数组</span>
                prop.forEach(<span class="hljs-function"><span class="hljs-params">childNode</span> =></span> &#123;
                    traverse(childNode, visitors);
                &#125;)
            &#125; <span class="hljs-keyword">else</span> &#123;
                traverse(prop, visitors);
            &#125;
        &#125;)
    &#125;
    visitorFuncs.exit && visitorFuncs.exit(node);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们传入的 visitor 也可以这样写：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">traverse(ast, &#123;
    <span class="hljs-attr">Identifier</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">exit</span>(<span class="hljs-params">node</span>)</span> &#123;
            node.name = <span class="hljs-string">'b'</span>;
        &#125;
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会在遍历完子节点之后被调用。</p>
<h4 data-id="heading-9">path</h4>
<p>我们实现的 visitor 是直接传入的 node，但是 AST 中并没有父节点的信息，所以我们要把父节点也传进去。</p>
<p>babel 提供了 path 的功能，它是从当前节点到根节点的一条路径，通过 parent 串联。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5bc0df4c61a4060948684ca07c49fc6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们封装一个 NodePath 的类：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NodePath</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">node, parent, parentPath</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.node = node;
        <span class="hljs-built_in">this</span>.parent = parent;
        <span class="hljs-built_in">this</span>.parentPath = parentPath;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用 visitor 的时候创建 path 对象传入：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">traverse</span>(<span class="hljs-params">node, visitors, parent, parentPath</span>) </span>&#123;
    <span class="hljs-keyword">const</span> defination = astDefinationsMap.get(node.type);

    <span class="hljs-keyword">let</span> visitorFuncs = visitors[node.type] || &#123;&#125;;

    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> visitorFuncs === <span class="hljs-string">'function'</span>) &#123;
        visitorFuncs = &#123;
            <span class="hljs-attr">enter</span>: visitorFuncs
        &#125;
    &#125;
    <span class="hljs-keyword">const</span> path = <span class="hljs-keyword">new</span> NodePath(node, parent, parentPath);

    visitorFuncs.enter && visitorFuncs.enter(path);

    <span class="hljs-keyword">if</span> (defination.visitor) &#123;
        defination.visitor.forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
            <span class="hljs-keyword">const</span> prop = node[key];
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(prop)) &#123; <span class="hljs-comment">// 如果该属性是数组</span>
                prop.forEach(<span class="hljs-function"><span class="hljs-params">childNode</span> =></span> &#123;
                    traverse(childNode, visitors, node, path);
                &#125;)
            &#125; <span class="hljs-keyword">else</span> &#123;
                traverse(prop, visitors, node, path);
            &#125;
        &#125;)
    &#125;
    visitorFuncs.exit && visitorFuncs.exit(path);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们可以在 visitor 中拿到父节点，父节点的父节点，我们来试一下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">traverse(ast, &#123;
    <span class="hljs-attr">Identifier</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">exit</span>(<span class="hljs-params">path</span>)</span> &#123;
            path.node.name = <span class="hljs-string">'b'</span>;
            <span class="hljs-keyword">let</span> curPath = path;
            <span class="hljs-keyword">while</span> (curPath) &#123;
                <span class="hljs-built_in">console</span>.log(curPath.node.type);
                curPath = curPath.parentPath;
            &#125;
        &#125;
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印结果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a885b74011a4d1ab1092f55b53a7623~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从当前节点到根节点的 AST 都可以获取到。</p>
<h4 data-id="heading-10">path 的 api</h4>
<p>parent 可以保存，同理 sibling 也可以，也就是说我们可以通过 path 拿到所有的 AST。但是直接操作 AST 有点麻烦，所以我们要提供一些 api 来简化操作。</p>
<p>首先我们要把遍历到的 AST 的属性对应的 key 和如果是数组时对应的 listKey 都保存下来。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NodePath</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">node, parent, parentPath, key, listKey</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.node = node;
        <span class="hljs-built_in">this</span>.parent = parent;
        <span class="hljs-built_in">this</span>.parentPath = parentPath;
        <span class="hljs-built_in">this</span>.key = key;
        <span class="hljs-built_in">this</span>.listKey = listKey;
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">traverse</span>(<span class="hljs-params">node, visitors, parent, parentPath, key, listKey</span>) </span>&#123;
    <span class="hljs-keyword">const</span> defination = astDefinationsMap.get(node.type);

    <span class="hljs-keyword">let</span> visitorFuncs = visitors[node.type] || &#123;&#125;;

    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> visitorFuncs === <span class="hljs-string">'function'</span>) &#123;
        visitorFuncs = &#123;
            <span class="hljs-attr">enter</span>: visitorFuncs
        &#125;
    &#125;
    <span class="hljs-keyword">const</span> path = <span class="hljs-keyword">new</span> NodePath(node, parent, parentPath, key, listKey);

    visitorFuncs.enter && visitorFuncs.enter(path);

    <span class="hljs-keyword">if</span> (defination.visitor) &#123;
        defination.visitor.forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
            <span class="hljs-keyword">const</span> prop = node[key];
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(prop)) &#123; <span class="hljs-comment">// 如果该属性是数组</span>
                prop.forEach(<span class="hljs-function">(<span class="hljs-params">childNode, index</span>) =></span> &#123;
                    traverse(childNode, visitors, node, path, key, index);
                &#125;)
            &#125; <span class="hljs-keyword">else</span> &#123;
                traverse(prop, visitors, node, path, key);
            &#125;
        &#125;)
    &#125;
    visitorFuncs.exit && visitorFuncs.exit(path);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后基于 key 和 listKey 来实现 replaceWith 和 remove 的 api：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NodePath</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">node, parent, parentPath, key, listKey</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.node = node;
        <span class="hljs-built_in">this</span>.parent = parent;
        <span class="hljs-built_in">this</span>.parentPath = parentPath;
        <span class="hljs-built_in">this</span>.key = key;
        <span class="hljs-built_in">this</span>.listKey = listKey;
    &#125;
    <span class="hljs-function"><span class="hljs-title">replaceWith</span>(<span class="hljs-params">node</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.listKey) &#123;
            <span class="hljs-built_in">this</span>.parent[<span class="hljs-built_in">this</span>.key].splice(<span class="hljs-built_in">this</span>.listKey, <span class="hljs-number">1</span>, node);
        &#125;
        <span class="hljs-built_in">this</span>.parent[<span class="hljs-built_in">this</span>.key] = node
    &#125;
    remove () &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.listKey) &#123;
            <span class="hljs-built_in">this</span>.parent[<span class="hljs-built_in">this</span>.key].splice(<span class="hljs-built_in">this</span>.listKey, <span class="hljs-number">1</span>);
        &#125;
        <span class="hljs-built_in">this</span>.parent[<span class="hljs-built_in">this</span>.key] = <span class="hljs-literal">null</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>试验下效果：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">traverse(ast, &#123;
    <span class="hljs-function"><span class="hljs-title">NumericLiteral</span>(<span class="hljs-params">path</span>)</span> &#123;
        path.replaceWith(&#123; <span class="hljs-attr">type</span>: <span class="hljs-string">'Identifier'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'bbbbbbb'</span> &#125;);
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果为：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da883136a8494a6e8d703ec27911be0e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>NumericLiteral 被替换为了 Identifier。我们成功的实现了 path.replaceWith。</p>
<h5 data-id="heading-11">path.scope</h5>
<p>path.scope 是作用域的信息，记录声明的变量的 binding、它们的引用 reference、在哪里被修改  （constantViolations），以及父作用域等。是静态作用域链的实现。</p>
<p>实现思路：</p>
<p>首先函数、块、模块都会生成作用域，当处理到这些 AST 时要创建一个 Scope 对象，它有 bindings 属性，每一个声明都会创建一个 binding（比如变量声明语句 VariableDeclaration、函数声明语句 FuncitonDeclaration 以及参数、import 等）</p>
<p>通过 Identifier 引用这些作用域中的 binding 的时候就会记录 references，如果被修改，则记录修改的语句的 AST 对应的 path，比如赋值语句。</p>
<p>同样需要提供一系列 api 来简化作用域的分析和操作，比如查找 getBinding、删除 removeBinding、重命名 rename 等。</p>
<p>篇幅关系，这里就不做实现了，《babel 插件通关秘籍》小册中会有完整的实现。</p>
<h3 data-id="heading-12">types</h3>
<p>在 traverse 的时候我们实现了 path.replaceWith 的 api，用于替换 AST 成新的 AST，我们是直接传入了字面量对象，这种方式比较麻烦。 babel 是通过 types 包来提供创建 AST 的能力，我们来分析一下实现思路：</p>
<p>其实创建 AST 节点也是一个递归的过程，需要保证每一部分都是正确的，我们在遍历的时候保存了 visitor 的 key，在创建的时候仍然是创建这些 key 对应的 AST，不过需要对传入的参数做一下检验。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">defineType(<span class="hljs-string">"BinaryExpression"</span>, &#123;
    <span class="hljs-attr">builder</span>: [<span class="hljs-string">"operator"</span>, <span class="hljs-string">"left"</span>, <span class="hljs-string">"right"</span>],
    <span class="hljs-attr">fields</span>: &#123;
      <span class="hljs-attr">operator</span>: &#123;
        <span class="hljs-attr">validate</span>: assertOneOf(...BINARY_OPERATORS),
      &#125;,
      <span class="hljs-attr">left</span>: &#123;
        <span class="hljs-attr">validate</span>: assertNodeType(<span class="hljs-string">"Expression"</span>),
      &#125;,
      <span class="hljs-attr">right</span>: &#123;
        <span class="hljs-attr">validate</span>: assertNodeType(<span class="hljs-string">"Expression"</span>),
      &#125;,
    &#125;,
    <span class="hljs-attr">visitor</span>: [<span class="hljs-string">"left"</span>, <span class="hljs-string">"right"</span>],
    <span class="hljs-attr">aliases</span>: [<span class="hljs-string">"Binary"</span>, <span class="hljs-string">"Expression"</span>],
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>babel 内部通过 defineType 方法定义 AST 类型的创建逻辑，其中 fileds 属性包含了这个 AST 需要什么属性，每种属性怎么校验。通过校验之后会根据相应的参数创建 AST。</p>
<h3 data-id="heading-13">template</h3>
<p>babel template 是通过字符串批量创建 AST，我们可以基于 parser 实现一个简单的 template</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">template</span>(<span class="hljs-params">code</span>) </span>&#123;
    <span class="hljs-keyword">return</span> parse(code);
&#125;
template.expression = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">code</span>) </span>&#123;
    <span class="hljs-keyword">return</span> template(code).body[<span class="hljs-number">0</span>].expression;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码就可以变成：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">traverse(ast, &#123;
    <span class="hljs-function"><span class="hljs-title">NumericLiteral</span>(<span class="hljs-params">path</span>)</span> &#123;     
        path.replaceWith(template.expression(<span class="hljs-string">'bbb'</span>));
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">generate</h3>
<p>上面都是对 AST 的增删改，接下来我们来实现下 generate，把 AST 打印成目标代码。</p>
<p>其实就是一个拼接字符串的过程：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Printer</span> </span>&#123;
    <span class="hljs-title">constructor</span> (<span class="hljs-params"></span>) &#123;
        <span class="hljs-built_in">this</span>.buf = <span class="hljs-string">''</span>;
    &#125;

    <span class="hljs-function"><span class="hljs-title">space</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.buf += <span class="hljs-string">' '</span>;
    &#125;

    <span class="hljs-function"><span class="hljs-title">nextLine</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.buf += <span class="hljs-string">'\n'</span>;
    &#125;

    Program (node) &#123;
        node.body.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
            <span class="hljs-built_in">this</span>[item.type](item) + <span class="hljs-string">';'</span>;
            <span class="hljs-built_in">this</span>.nextLine();
        &#125;);

    &#125;
    <span class="hljs-function"><span class="hljs-title">VariableDeclaration</span>(<span class="hljs-params">node</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.buf += node.kind;
        <span class="hljs-built_in">this</span>.space();
        node.declarations.forEach(<span class="hljs-function">(<span class="hljs-params">declaration, index</span>) =></span> &#123;
            <span class="hljs-keyword">if</span> (index != <span class="hljs-number">0</span>) &#123;
                <span class="hljs-built_in">this</span>.buf += <span class="hljs-string">','</span>;
            &#125;
            <span class="hljs-built_in">this</span>[declaration.type](declaration);
        &#125;);
        <span class="hljs-built_in">this</span>.buf += <span class="hljs-string">';'</span>;
    &#125;
    <span class="hljs-function"><span class="hljs-title">VariableDeclarator</span>(<span class="hljs-params">node</span>)</span> &#123;
        <span class="hljs-built_in">this</span>[node.id.type](node.id);
        <span class="hljs-built_in">this</span>.buf += <span class="hljs-string">'='</span>;
        <span class="hljs-built_in">this</span>[node.init.type](node.init);
    &#125;
    <span class="hljs-function"><span class="hljs-title">Identifier</span>(<span class="hljs-params">node</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.buf += node.name;
    &#125;
    <span class="hljs-function"><span class="hljs-title">NumericLiteral</span>(<span class="hljs-params">node</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.buf += node.value;
    &#125;

&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Generator</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Printer</span></span>&#123;

    <span class="hljs-function"><span class="hljs-title">generate</span>(<span class="hljs-params">node</span>)</span> &#123;
        <span class="hljs-built_in">this</span>[node.type](node);
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.buf;
    &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">generate</span> (<span class="hljs-params">node</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Generator().generate(node);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来试验一下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> sourceCode = <span class="hljs-string">`
const a = 1,b=2,c=3;
const d=4,e=5;
`</span>;

ast = parse(sourceCode);
traverse(ast, &#123;
    <span class="hljs-function"><span class="hljs-title">NumericLiteral</span>(<span class="hljs-params">path</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (path.node.value === <span class="hljs-number">2</span>) &#123;
            path.replaceWith(template.expression(<span class="hljs-string">'aaaaa'</span>));
        &#125;
    &#125; 
&#125;)
<span class="hljs-built_in">console</span>.log(generate(ast));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印结果如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> a=<span class="hljs-number">1</span>,b=aaaaa,c=<span class="hljs-number">3</span>;
<span class="hljs-keyword">const</span> d=<span class="hljs-number">4</span>,e=<span class="hljs-number">5</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们成功的实现了 generate 方法。</p>
<h4 data-id="heading-15">sourcemap</h4>
<p>generator 除了打印目标代码外还要生成 sourcemap，这个是转译器很重要的一个功能。</p>
<p>sourcemap 的实现思路也比较简单：</p>
<p>parse 之后的 AST 中保留了源码中的位置信息（行列号），在打印成目标代码的时候计算新的行列号，这样有了新旧行列号，就可以用 source-map  包的 api 生成 sourcemap 了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> map = <span class="hljs-keyword">new</span> SourceMapGenerator(&#123;
  <span class="hljs-attr">file</span>: <span class="hljs-string">"source-mapped.js"</span>
&#125;);

map.addMapping(&#123;
  <span class="hljs-attr">generated</span>: &#123;
    <span class="hljs-attr">line</span>: <span class="hljs-number">10</span>,
    <span class="hljs-attr">column</span>: <span class="hljs-number">35</span>
  &#125;,
  <span class="hljs-attr">source</span>: <span class="hljs-string">"foo.js"</span>,
  <span class="hljs-attr">original</span>: &#123;
    <span class="hljs-attr">line</span>: <span class="hljs-number">33</span>,
    <span class="hljs-attr">column</span>: <span class="hljs-number">2</span>
  &#125;,
  <span class="hljs-attr">name</span>: <span class="hljs-string">"christopher"</span>
&#125;);

<span class="hljs-built_in">console</span>.log(map.toString());
<span class="hljs-comment">// '&#123;"version":3,"file":"source-mapped.js",</span>
<span class="hljs-comment">//   "sources":["foo.js"],"names":["christopher"],"mappings":";;;;;;;;;mCAgCEA"&#125;'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">core</h3>
<p>上面我们已经实现了全流程的功能，但是平时我们平时很少使用 api，更多还是使用全流程的包 @babel/core，所以要基于上面的包实现 core 包，然后支持 plugin 和 preset。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">transformSync</span>(<span class="hljs-params">code, options</span>) </span>&#123;
    <span class="hljs-keyword">const</span> ast = parse(code);

    <span class="hljs-keyword">const</span> pluginApi = &#123;
        template
    &#125;
    <span class="hljs-keyword">const</span> visitors = &#123;&#125;;
    options.plugins.forEach(<span class="hljs-function">(<span class="hljs-params">[plugin, options]</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> res = plugin(pluginApi, options);
        <span class="hljs-built_in">Object</span>.assign(visitors, res.visitor);
    &#125;)

    traverse(ast, visitors);
    <span class="hljs-keyword">return</span> generate(ast);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>plugin 支持传入 options，并且在 plugin 里面可以拿到 api 和 options，返回值是 visitor 函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> sourceCode = <span class="hljs-string">`
const a = 1;
`</span>;

<span class="hljs-keyword">const</span> code = transformSync(sourceCode, &#123;
    <span class="hljs-attr">plugins</span>: [
        [
            <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">plugin1</span>(<span class="hljs-params">api, options</span>) </span>&#123;
                <span class="hljs-keyword">return</span> &#123;
                    <span class="hljs-attr">visitor</span>: &#123;
                        <span class="hljs-function"><span class="hljs-title">Identifier</span>(<span class="hljs-params">path</span>)</span> &#123;
                                <span class="hljs-comment">// path.node.value = 2222;</span>
                                path.replaceWith(api.template.expression(options.replaceName));
                        &#125;
                    &#125;
                &#125;
            &#125;,
            &#123;
                <span class="hljs-attr">replaceName</span>: <span class="hljs-string">'ddddd'</span>
            &#125;
        ]
    ]
&#125;);
<span class="hljs-built_in">console</span>.log(code);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果为:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> ddddd=<span class="hljs-number">1</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此我们完成了 babel 所有内置功能的简易版本实现。 (helper 就是一个放公共函数的包， runtime 是用于运行时引入的 api，这两个包比较简单，就不实现了。在《babel 插件通关秘籍》的小册里面会详细实现）</p>
<h2 data-id="heading-17">总结</h2>
<p>我们梳理了 babel 的编译流程和内置的包的各自的功能，然后明确了我们要实现的包：parser、traverse、generate、types、template、core。接下来依次做了实现或梳理了实现思路。</p>
<p>parser 包基于 acorn，babel 是 fork 自 acorn，我们是直接基于 acorn 插件来修改 AST。我们实现了 Literal 的 AST 的扩展。</p>
<p>traverse 包负责遍历 AST，我们通过记录 visitor key 实现了 AST 的深度优先遍历，并且在遍历的过程中调用 visitor，而且还支持 enter 和 exit 两个阶段的调用。 visitor 传入的参数支持了 path，可以拿到 parent，可以调用 replaceWith 和 remove 等 api。我们还梳理了实现 scope 的思路。</p>
<p>types 和 template 都是用于创建 AST 的，我们梳理了 types 的实现思路，就是递归创建 AST 然后组装，实现了简单的 template，使用直接从字符串 parse 的方式。</p>
<p>generate 包负责把修改以后的 AST 打印成目标代码以及生成 sourcemap，我们实现了代码的打印。梳理了 sourcemap 的思路。</p>
<p>core 包是整个编译流程的集成，而且支持 plugins 和 preset，我们实现了 transformSync 的 api，也支持了 plugin 的调用。</p>
<p>上面就是 babel 的实现思路，细化一下是能够实现一个完整功能的 babel 的。</p>
<p>这个是《babel 插件通关秘籍》 的最后一个案例，小册中的实现思路和代码会更清晰，也会提供源码。</p>
<p>这周末电脑突然坏了，代码可能也有丢失，所以不得不鸽一段时间。但是挺多人挺期待这本小册上线的，我实在过意不过，所以把大家感兴趣的《手写简易的 babel》的实现思路分享了出来，希望能够帮大家更好的掌握 babel 以及类似的编译器。（小册在我电脑修好后也会尽快写完的）</p></div>  
</div>
            