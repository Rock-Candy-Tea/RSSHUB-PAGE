
---
title: '基于 babel 实现 typescript 类型检查'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17ac954089a84f989902a8066f83f73f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 08 May 2021 03:42:34 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17ac954089a84f989902a8066f83f73f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>typescript 给 javascript 扩展了类型的语法和语义，让我们可以给变量、函数等定义类型，然后编译期间检查，这样能够提前发现类型不匹配的错误，还能够在开发时提示可用的属性方法。</p>
<p>而且，typescript 并不像当年的 coffeescript 一样改变了语法，它是 javascript 的一个超集，只做了类型的扩展。</p>
<p>这些优点使得 typescript 迅速的火了起来。现在前端面试如果你不会 typescript，那么可能很难拿到 offer。</p>
<p>市面上关于 typescript 的教程文很多了，但是没有一篇去从编译原理的角度分析它的实现的。本文不会讲 typescript 的基础，而是会实现一个 typescript type checker，帮你理解类型检查究竟做了什么。理解了类型检查的实现思路，再去学 typescript，或许就没那么难了。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17ac954089a84f989902a8066f83f73f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">思路分析</h2>
<h3 data-id="heading-2">typescript compiler 与 babel</h3>
<p>typescript compiler 是一个 转译器，负责把 typescript 的语法转成 es2015、es5、es3 的目标 javascript，并且过程中会做类型检查。</p>
<p>babel 也是一个转译器，可以把 es next、typescript、flow 等语法转成目标环境支持的 js。</p>
<p>babel 也可以编译 typescript？ 对的，babel 7 以后就可以编译 typescript 代码，这还是 typescript 团队和 babel 团队合作一年的成果。</p>
<p>我们知道，babel 编译流程分为 3 个步骤：parse、transform、generate。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5de35e62d8324ad19a650f51b0f1f167~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>parse 阶段负责编译源码成 AST，transform 阶段对 AST 进行增删改，generate 阶段打印 AST 成目标代码并生成 sorucemap。</p>
<p>babel 可以编译 typescript 代码只是能够 parse，并不会做类型检查，我们完全可以基于 babel parse 出的 AST 来实现一下类型检查。</p>
<h3 data-id="heading-3">类型检查要做什么</h3>
<p>我们经常用 tsc 来做类型检查，有没有想过，类型检查具体做了什么？</p>
<h4 data-id="heading-4">什么是类型</h4>
<p>类型代表了变量存储的内容，也就是规定了这块内容占据多大的内存空间，可以对它做什么操作。比如 number 和 boolean 就会分配不同字节数的内存，Date 和 String 可以调用的方法也不同。这就是类型的作用。它代表了一种可能性，你可以在这块内存放多少内容，可能对它进行什么操作。</p>
<p>动态类型是指类型是在运行时确定的，而静态类型是指编译期间就知道了变量的类型信息，有了类型信息自然就知道了对它而言什么操作是合法的，什么操作是不合法的，什么变量能够赋值给他。</p>
<p>静态类型会在代码中保留类型信息，这个类型信息可能是显式声明的，也可能是自动推导出来的。想做一个大的项目，没有静态类型来约束和提前检查代码的话，太容易出 bug 了，会很难维护。这也是随着前端项目逐渐变得复杂，出现了 typescript 以及 typescript 越来越火的原因。</p>
<h4 data-id="heading-5">如何检查类型</h4>
<p>我们知道了什么是类型，为什么要做静态的类型检查，那么怎么检查呢？</p>
<p>检查类型就是检查变量的内容，而理解代码的话需要把代码 parse 成 AST，所以类型检查也就变成了对 AST 结构的检查。</p>
<p>比如一个变量声明为了 number，那么给它赋值的是一个 string 就是有类型错误。</p>
<p>再复杂一点，如果类型有泛型，也就是有类型参数，那么需要传入具体的参数来确定类型，确定了类型之后再去和实际的 AST 对比。</p>
<p>typescript 还支持高级类型，也就是类型可以做各种运算，这种就需要传入类型参数求出具体的类型再去和 AST 对比。</p>
<p>如果没有完全理解也没有关系，我们来写代码实现一下：</p>
<h2 data-id="heading-6">代码实现</h2>
<h3 data-id="heading-7">实现简单类型的类型检查</h3>
<h4 data-id="heading-8">赋值语句的类型检查</h4>
<p>比如这样一段代码，声明的值是一个 string，但是赋值为了 number，明显是有类型错误的，我们怎么检查出它的错误的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> name: string;

name = <span class="hljs-number">111</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先我们使用 babel 把这段代码 parse 成 AST：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span>  parser = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/parser'</span>);

<span class="hljs-keyword">const</span> sourceCode = <span class="hljs-string">`
    let name: string;

    name = 111;
`</span>;

<span class="hljs-keyword">const</span> ast = parser.parse(sourceCode, &#123;
    <span class="hljs-attr">plugins</span>: [<span class="hljs-string">'typescript'</span>]
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 babel parser 来 parse，启用 typescript 语法插件。</p>
<p>可以使用 <a href="https://astexplorer.net/" target="_blank" rel="nofollow noopener noreferrer">astexplerer.net</a> 来查看它的 AST：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae7a3f0df639438cb2aa5a6314bfb701~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-9">实现类型检查</h5>
<p>我们需要检查的是这个赋值语句 AssignmentExpression，左右两边的类型是否匹配。</p>
<p>右边是一个数字字面量 NumericLiteral，很容易拿到类型，而左边则是一个引用，要从作用域中拿到它声明的类型，之后才能做类型对比。</p>
<p>babel 提供了 scope 的 api 可以用于查找作用域中的类型声明（binding），并且还可以通过 getTypeAnnotation 获得声明时的类型</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-function"><span class="hljs-title">AssignmentExpression</span>(<span class="hljs-params">path, state</span>)</span> &#123;
    <span class="hljs-keyword">const</span> leftBinding = path.scope.getBinding(path.get(<span class="hljs-string">'left'</span>));
    <span class="hljs-keyword">const</span> leftType = leftBinding.path.get(<span class="hljs-string">'id'</span>).getTypeAnnotation();<span class="hljs-comment">// 左边的值声明的类型</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个返回的类型是 TSTypeAnnotation 的一个对象，我们需要做下处理：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adaad85b1de341e58d719810894bfc5c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>封装一个方法，传入类型对象，返回 number、string 等类型字符串</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolveType</span>(<span class="hljs-params">targetType</span>) </span>&#123;
    <span class="hljs-keyword">const</span> tsTypeAnnotationMap = &#123;
        <span class="hljs-string">'TSStringKeyword'</span>: <span class="hljs-string">'string'</span>
    &#125;
    <span class="hljs-keyword">switch</span> (targetType.type) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'TSTypeAnnotation'</span>:
            <span class="hljs-keyword">return</span> tsTypeAnnotationMap[targetType.typeAnnotation.type];
        <span class="hljs-keyword">case</span> <span class="hljs-string">'NumberTypeAnnotation'</span>: 
            <span class="hljs-keyword">return</span> <span class="hljs-string">'number'</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们拿到了左右两边的类型，接下来就简单了，对比下就知道了类型是否匹配：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">AssignmentExpression</span>(<span class="hljs-params">path, state</span>)</span> &#123;
    <span class="hljs-keyword">const</span> rightType = resolveType(path.get(<span class="hljs-string">'right'</span>).getTypeAnnotation());
    <span class="hljs-keyword">const</span> leftBinding = path.scope.getBinding(path.get(<span class="hljs-string">'left'</span>));
    <span class="hljs-keyword">const</span> leftType = resolveType(leftBinding.path.get(<span class="hljs-string">'id'</span>).getTypeAnnotation());
    <span class="hljs-keyword">if</span> (leftType !== rightType ) &#123;
        <span class="hljs-comment">// error: 类型不匹配</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10">错误打印优化</h5>
<p>报错信息怎么打印呢？可以使用 @babel/code-frame，它支持打印某一片段的高亮代码。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">path.get(<span class="hljs-string">'right'</span>).buildCodeFrameError(<span class="hljs-string">`<span class="hljs-subst">$&#123;rightType&#125;</span> can not assign to <span class="hljs-subst">$&#123;leftType&#125;</span>`</span>, <span class="hljs-built_in">Error</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b7f4107058d4a67ae40b7d1f23aa3ea~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个错误堆栈也太丑了，我们把它去掉，设置 Error.stackTraceLimit 为 0 就行了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Error</span>.stackTraceLimit = <span class="hljs-number">0</span>;
path.get(<span class="hljs-string">'right'</span>).buildCodeFrameError(<span class="hljs-string">`<span class="hljs-subst">$&#123;rightType&#125;</span> can not assign to <span class="hljs-subst">$&#123;leftType&#125;</span>`</span>, <span class="hljs-built_in">Error</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这里改了之后还要改回来，也就是:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> tmp = <span class="hljs-built_in">Error</span>.stackTraceLimit;
<span class="hljs-built_in">Error</span>.stackTraceLimit = <span class="hljs-number">0</span>;
<span class="hljs-built_in">console</span>.log(path.get(<span class="hljs-string">'right'</span>).buildCodeFrameError(<span class="hljs-string">`<span class="hljs-subst">$&#123;rightType&#125;</span> can not assign to <span class="hljs-subst">$&#123;leftType&#125;</span>`</span>, <span class="hljs-built_in">Error</span>));
<span class="hljs-built_in">Error</span>.stackTraceLimit = tmp;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再来跑一下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e3e18ea42dd4f3aae0e13d65756430f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>好看多了！</p>
<h5 data-id="heading-11">错误收集</h5>
<p>还有一个问题，现在是遇到类型错误就报错，但我们希望是在遇到类型错误时收集起来，最后统一报错。</p>
<p>怎么实现呢？错误放在哪？</p>
<p>babel 插件中可以拿到 file 对象，有 set 和 get 方法用来存取一些全局的信息。可以在插件调用前后，也就是 pre 和 post 阶段拿到 file 对象（这些在掘金小册《babel 插件通关秘籍》中会细讲）。</p>
<p>所以我们可以这样做：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">pre</span>(<span class="hljs-params">file</span>)</span> &#123;
    file.set(<span class="hljs-string">'errors'</span>, []);
&#125;,
<span class="hljs-attr">visitor</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">AssignmentExpression</span>(<span class="hljs-params">path, state</span>)</span> &#123;
        <span class="hljs-keyword">const</span> errors = state.file.get(<span class="hljs-string">'errors'</span>);

        <span class="hljs-keyword">const</span> rightType = resolveType(path.get(<span class="hljs-string">'right'</span>).getTypeAnnotation());
        <span class="hljs-keyword">const</span> leftBinding = path.scope.getBinding(path.get(<span class="hljs-string">'left'</span>));
        <span class="hljs-keyword">const</span> leftType = resolveType(leftBinding.path.get(<span class="hljs-string">'id'</span>).getTypeAnnotation());
        <span class="hljs-keyword">if</span> (leftType !== rightType ) &#123;
            <span class="hljs-keyword">const</span> tmp = <span class="hljs-built_in">Error</span>.stackTraceLimit;
            <span class="hljs-built_in">Error</span>.stackTraceLimit = <span class="hljs-number">0</span>;
            errors.push(path.get(<span class="hljs-string">'right'</span>).buildCodeFrameError(<span class="hljs-string">`<span class="hljs-subst">$&#123;rightType&#125;</span> can not assign to <span class="hljs-subst">$&#123;leftType&#125;</span>`</span>, <span class="hljs-built_in">Error</span>));
            <span class="hljs-built_in">Error</span>.stackTraceLimit = tmp;
        &#125; 
    &#125;
&#125;,
<span class="hljs-function"><span class="hljs-title">post</span>(<span class="hljs-params">file</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(file.get(<span class="hljs-string">'errors'</span>));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就可以做到过程中收集错误，最后统一打印：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/917ee6d6f4da4c739d4b7a0ffe742b26~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样，我们就实现了简单的赋值语句的类型检查。</p>
<h4 data-id="heading-12">函数调用的类型检查</h4>
<p>赋值语句的检查比较简单，我们来进阶一下，实现函数调用参数的类型检查</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a: number, b: number</span>): <span class="hljs-title">number</span></span>&#123;
    <span class="hljs-keyword">return</span> a + b;
&#125;
add(<span class="hljs-number">1</span>, <span class="hljs-string">'2'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们要检查的就是函数调用语句 CallExpression 的参数和它声明的是否一致。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38286e5076cf4609b0cb66bfa34b66ef~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>CallExpression 有 callee 和 arguments 两部分，我们需要根据 callee 从作用域中查找函数声明，然后再把 arguments 的类型和函数声明语句的 params 的类型进行逐一对比，这样就实现了函数调用参数的类型检查。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">pre</span>(<span class="hljs-params">file</span>)</span> &#123;
    file.set(<span class="hljs-string">'errors'</span>, []);
&#125;,
<span class="hljs-attr">visitor</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">CallExpression</span>(<span class="hljs-params">path, state</span>)</span> &#123;
        <span class="hljs-keyword">const</span> errors = state.file.get(<span class="hljs-string">'errors'</span>);
        <span class="hljs-comment">// 调用参数的类型</span>
        <span class="hljs-keyword">const</span> argumentsTypes = path.get(<span class="hljs-string">'arguments'</span>).map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
            <span class="hljs-keyword">return</span> resolveType(item.getTypeAnnotation());
        &#125;);
        <span class="hljs-keyword">const</span> calleeName = path.get(<span class="hljs-string">'callee'</span>).toString();
        <span class="hljs-comment">// 根据 callee 查找函数声明</span>
        <span class="hljs-keyword">const</span> functionDeclarePath = path.scope.getBinding(calleeName).path;
        <span class="hljs-comment">// 拿到声明时参数的类型</span>
        <span class="hljs-keyword">const</span> declareParamsTypes = functionDeclarePath.get(<span class="hljs-string">'params'</span>).map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
            <span class="hljs-keyword">return</span> resolveType(item.getTypeAnnotation());
        &#125;)

        argumentsTypes.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
            <span class="hljs-keyword">if</span> (item !== declareParamsTypes[index]) &#123;
                <span class="hljs-comment">// 类型不一致，报错</span>
            &#125;
        &#125;);
    &#125;
&#125;,
<span class="hljs-function"><span class="hljs-title">post</span>(<span class="hljs-params">file</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(file.get(<span class="hljs-string">'errors'</span>));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行一下，效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be28b2a2b76f4587ade7f6caf5d6144c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们实现了函数调用参数的类型检查！实际上思路还是挺清晰的，检查别的 AST 也是类似的思路。</p>
<h3 data-id="heading-13">实现带泛型的类型检查</h3>
<p>泛型是什么，其实就是类型参数，使得类型可以根据传入的参数动态确定，类型定义更加灵活。</p>
<p>比如这样一段代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span><<span class="hljs-title">T</span>>(<span class="hljs-params">a: T, b: T</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a + b;
&#125;
add<number>(<span class="hljs-number">1</span>, <span class="hljs-string">'2'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>怎么做类型检查呢？</p>
<p>这还是函数调用语句的类型检查，我们上面实现过了，区别不过是多了个参数，那么我们取出类型参数来传过去就行了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc23d4a6ea0c4388990fead972afe56e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>多了一步确定泛型参数的具体类型的过程。</p>
<p>执行看下效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4126833b7eed45eca7b461179aa4ecfb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们成功支持了带泛型的函数调用语句的类型检查！</p>
<h3 data-id="heading-14">实现带高级类型的函数调用语句的类型检查</h3>
<p>typescript 支持高级类型，也就是支持对类型参数做各种运算然后返回最终类型</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">type Res<Param> = Param <span class="hljs-keyword">extends</span> <span class="hljs-number">1</span> ? number : string;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span><<span class="hljs-title">T</span>>(<span class="hljs-params">a: T, b: T</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a + b;
&#125;
add<Res<<span class="hljs-number">1</span>>>(<span class="hljs-number">1</span>, <span class="hljs-string">'2'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如这段代码中，Res 就是一个高级类型，对传入的类型参数 Param 进行处理之后返回新类型。</p>
<p>这个函数调用语句的类型检查，比泛型参数传具体的类型又复杂了一些，需要先求出具体的类型，然后再传入参数，之后再去对比参数的类型。</p>
<p>那么这个 Res 的高级类型怎么求值呢？</p>
<p>我们来看一下这个 Res 类型的 AST：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d715c4b197474eea9847eae1720a6965~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>它有类型参数部分（typeParameters），和具体的类型计算逻辑部分（typeAnnotation），右边的 <code>Param extends 1 ? number : string;</code> 是一个 condition 语句，有 Params 和 1 分别对应 checkType、extendsType，number 和 string 则分别对应 trueType、falseType。</p>
<p>我们只需要对传入的 Param 判断下是否是 1，就可以求出具体的类型是 trueType 还是 falseType。</p>
<p>具体类型传参的逻辑和上面一样，就不赘述了，我们看一下根据类型参数来值的逻辑：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">typeEval</span>(<span class="hljs-params">node, params</span>) </span>&#123;
    <span class="hljs-keyword">let</span> checkType;
    <span class="hljs-keyword">if</span>(node.checkType.type === <span class="hljs-string">'TSTypeReference'</span>) &#123;
        checkType = params[node.checkType.typeName.name];<span class="hljs-comment">// 如果参数是泛型，则从传入的参数取值</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
        checkType = resolveType(node.checkType); <span class="hljs-comment">// 否则直接取字面量参数</span>
    &#125;
    <span class="hljs-keyword">const</span> extendsType = resolveType(node.extendsType);
    <span class="hljs-keyword">if</span> (checkType === extendsType || checkType <span class="hljs-keyword">instanceof</span> extendsType) &#123; <span class="hljs-comment">// 如果 extends 逻辑成立</span>
        <span class="hljs-keyword">return</span> resolveType(node.trueType);
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> resolveType(node.falseType);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们就可以求出这个 Res 的高级类型当传入 Params 为 1 时求出的最终类型。</p>
<p>有了最终类型之后，就和直接传入具体类型的函数调用的类型检查一样了。（上面我们实现过）</p>
<p>执行一下，效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04e79c469f2147d7bf9ce40733ec08ba~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>完整代码如下（有些长，可以先跳过往后看）：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; declare &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/helper-plugin-utils'</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">typeEval</span>(<span class="hljs-params">node, params</span>) </span>&#123;
    <span class="hljs-keyword">let</span> checkType;
    <span class="hljs-keyword">if</span>(node.checkType.type === <span class="hljs-string">'TSTypeReference'</span>) &#123;
        checkType = params[node.checkType.typeName.name];
    &#125; <span class="hljs-keyword">else</span> &#123;
        checkType = resolveType(node.checkType);
    &#125;
    <span class="hljs-keyword">const</span> extendsType = resolveType(node.extendsType);
    <span class="hljs-keyword">if</span> (checkType === extendsType || checkType <span class="hljs-keyword">instanceof</span> extendsType) &#123;
        <span class="hljs-keyword">return</span> resolveType(node.trueType);
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> resolveType(node.falseType);
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolveType</span>(<span class="hljs-params">targetType, referenceTypesMap = &#123;&#125;, scope</span>) </span>&#123;
    <span class="hljs-keyword">const</span> tsTypeAnnotationMap = &#123;
        <span class="hljs-attr">TSStringKeyword</span>: <span class="hljs-string">'string'</span>,
        <span class="hljs-attr">TSNumberKeyword</span>: <span class="hljs-string">'number'</span>
    &#125;
    <span class="hljs-keyword">switch</span> (targetType.type) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'TSTypeAnnotation'</span>:
            <span class="hljs-keyword">if</span> (targetType.typeAnnotation.type === <span class="hljs-string">'TSTypeReference'</span>) &#123;
                <span class="hljs-keyword">return</span> referenceTypesMap[targetType.typeAnnotation.typeName.name]
            &#125;
            <span class="hljs-keyword">return</span> tsTypeAnnotationMap[targetType.typeAnnotation.type];
        <span class="hljs-keyword">case</span> <span class="hljs-string">'NumberTypeAnnotation'</span>: 
            <span class="hljs-keyword">return</span> <span class="hljs-string">'number'</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'StringTypeAnnotation'</span>:
            <span class="hljs-keyword">return</span> <span class="hljs-string">'string'</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'TSNumberKeyword'</span>:
            <span class="hljs-keyword">return</span> <span class="hljs-string">'number'</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'TSTypeReference'</span>:
            <span class="hljs-keyword">const</span> typeAlias = scope.getData(targetType.typeName.name);
            <span class="hljs-keyword">const</span> paramTypes = targetType.typeParameters.params.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
                <span class="hljs-keyword">return</span> resolveType(item);
            &#125;);
            <span class="hljs-keyword">const</span> params = typeAlias.paramNames.reduce(<span class="hljs-function">(<span class="hljs-params">obj, name, index</span>) =></span> &#123;
                obj[name] = paramTypes[index]; 
                <span class="hljs-keyword">return</span> obj;
            &#125;,&#123;&#125;);
            <span class="hljs-keyword">return</span> typeEval(typeAlias.body, params);
        <span class="hljs-keyword">case</span> <span class="hljs-string">'TSLiteralType'</span>:
            <span class="hljs-keyword">return</span> targetType.literal.value;
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">noStackTraceWrapper</span>(<span class="hljs-params">cb</span>) </span>&#123;
    <span class="hljs-keyword">const</span> tmp = <span class="hljs-built_in">Error</span>.stackTraceLimit;
    <span class="hljs-built_in">Error</span>.stackTraceLimit = <span class="hljs-number">0</span>;
    cb && cb(<span class="hljs-built_in">Error</span>);
    <span class="hljs-built_in">Error</span>.stackTraceLimit = tmp;
&#125;

<span class="hljs-keyword">const</span> noFuncAssignLint = declare(<span class="hljs-function">(<span class="hljs-params">api, options, dirname</span>) =></span> &#123;
    api.assertVersion(<span class="hljs-number">7</span>);

    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-function"><span class="hljs-title">pre</span>(<span class="hljs-params">file</span>)</span> &#123;
            file.set(<span class="hljs-string">'errors'</span>, []);
        &#125;,
        <span class="hljs-attr">visitor</span>: &#123;
            <span class="hljs-function"><span class="hljs-title">TSTypeAliasDeclaration</span>(<span class="hljs-params">path</span>)</span> &#123;
                path.scope.setData(path.get(<span class="hljs-string">'id'</span>).toString(), &#123;
                    <span class="hljs-attr">paramNames</span>: path.node.typeParameters.params.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
                        <span class="hljs-keyword">return</span> item.name;
                    &#125;),
                    <span class="hljs-attr">body</span>: path.getTypeAnnotation()
                &#125;);
                path.scope.setData(path.get(<span class="hljs-string">'params'</span>))
            &#125;,
            <span class="hljs-function"><span class="hljs-title">CallExpression</span>(<span class="hljs-params">path, state</span>)</span> &#123;
                <span class="hljs-keyword">const</span> errors = state.file.get(<span class="hljs-string">'errors'</span>);
                <span class="hljs-keyword">const</span> realTypes = path.node.typeParameters.params.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
                    <span class="hljs-keyword">return</span> resolveType(item, &#123;&#125;, path.scope);
                &#125;);
                <span class="hljs-keyword">const</span> argumentsTypes = path.get(<span class="hljs-string">'arguments'</span>).map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
                    <span class="hljs-keyword">return</span> resolveType(item.getTypeAnnotation());
                &#125;);
                <span class="hljs-keyword">const</span> calleeName = path.get(<span class="hljs-string">'callee'</span>).toString();
                <span class="hljs-keyword">const</span> functionDeclarePath = path.scope.getBinding(calleeName).path;
                <span class="hljs-keyword">const</span> realTypeMap = &#123;&#125;;
                functionDeclarePath.node.typeParameters.params.map(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
                    realTypeMap[item.name] = realTypes[index];
                &#125;);
                <span class="hljs-keyword">const</span> declareParamsTypes = functionDeclarePath.get(<span class="hljs-string">'params'</span>).map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
                    <span class="hljs-keyword">return</span> resolveType(item.getTypeAnnotation(), realTypeMap);
                &#125;)

                argumentsTypes.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
                    <span class="hljs-keyword">if</span> (item !== declareParamsTypes[index]) &#123;
                        noStackTraceWrapper(<span class="hljs-function"><span class="hljs-params">Error</span> =></span> &#123;
                            errors.push(path.get(<span class="hljs-string">'arguments.'</span> + index ).buildCodeFrameError(<span class="hljs-string">`<span class="hljs-subst">$&#123;item&#125;</span> can not assign to <span class="hljs-subst">$&#123;declareParamsTypes[index]&#125;</span>`</span>,<span class="hljs-built_in">Error</span>));
                        &#125;);
                    &#125;
                &#125;);
            &#125;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">post</span>(<span class="hljs-params">file</span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(file.get(<span class="hljs-string">'errors'</span>));
        &#125;
    &#125;
&#125;);

<span class="hljs-built_in">module</span>.exports = noFuncAssignLint;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>就这样，我们实现了 typescript 高级类型！</p>
<h2 data-id="heading-15">总结</h2>
<p>类型代表了变量的内容和能对它进行的操作，静态类型让检查可以在编译期间做，随着前端项目越来越重，越来越需要  typescript 这类静态类型语言。</p>
<p>类型检查就是做 AST 的对比，判断声明的和实际的是否一致：</p>
<ul>
<li>简单类型就直接对比，相当于 if else</li>
<li>带泛型的要先把类型参数传递过去才能确定类型，之后对比，相当于函数调用包裹 if else</li>
<li>带高级类型的泛型的类型检查，多了一个对类型求值的过程，相当于多级函数调用之后再判断 if else</li>
</ul>
<p>实现一个完整的 typescript type cheker 还是很复杂的，不然 typescript checker 部分的代码也不至于好几万行了。但是思路其实没有那么难，按照我们文中的思路来，是可以实现一个完整的 type checker 的。</p>
<p>（关于 babel 插件和 api 的部分，如果看不懂，可以在我即将上线的小册《babel 插件通关秘籍》中来详细了解。掌握了 babel，也就掌握了静态分析的能力，linter、type checker 这些顺带也能更深入的掌握。）</p></div>  
</div>
            