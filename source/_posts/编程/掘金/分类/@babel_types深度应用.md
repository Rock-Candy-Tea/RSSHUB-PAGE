
---
title: '@babel_types深度应用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1216'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 16:39:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=1216'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前文说过，types已经集成到@babel/core里，当然也可以单独安装：</p>
<pre><code class="hljs language-sh copyable" lang="sh">npm i -D @babel/types
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-0">概述</h1>
<p><code>@babel/types</code>的用途主要有3种：</p>
<h2 data-id="heading-1">类型集合</h2>
<p>当你在<code>ts</code>中使用<code>babel</code>时，<code>types</code>可以为你提供全部节点对应的类型。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">let</span> n1: types.Identifier
<span class="hljs-keyword">let</span> n2: types.ExpressionStatement
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">类型判断</h2>
<p>每一种节点类型，都有对应的类型判断方法：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">if</span>(types.isIdentifier(n1)) &#123;
    <span class="hljs-comment">// ...</span>
&#125;

<span class="hljs-keyword">if</span>(types.isExpressionStatement(n2)) &#123;
    <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每个类型判断方法，都实现了类型保护，顺道聊一下</p>
<h3 data-id="heading-3">TypeScript 类型保护。</h3>
<p>先定义一个泛型的类型保护函数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> IsType<T> = <span class="hljs-function">(<span class="hljs-params">target: <span class="hljs-built_in">any</span></span>) =></span> target is T
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后实现一下<code>string</code>类型保护：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> isString: IsType<<span class="hljs-built_in">string</span>> = (target): target is <span class="hljs-built_in">string</span> => &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> target === <span class="hljs-string">'string'</span>
&#125;

<span class="hljs-keyword">if</span>(isString(abc)) &#123;
    <span class="hljs-comment">// 当此处调用abc时，vscode会按照string类型给予足够提示</span>
    abc.slice
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，原生值类型的类型判断比较简单，上面的代码和</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> abc === <span class="hljs-string">'string'</span>) &#123;
    <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果一样。下面对自定义复杂类型做一下类型保护：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">type</span> TComplex = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>
    <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>
&#125;

<span class="hljs-keyword">const</span> isComplex: IsType<TComplex> = (target): target is TComplex => &#123;
    <span class="hljs-keyword">return</span> (
        target
        && <span class="hljs-keyword">typeof</span> target.name === <span class="hljs-string">'string'</span>
        && <span class="hljs-keyword">typeof</span> target.age === <span class="hljs-string">'number'</span>
        && !<span class="hljs-built_in">isNaN</span>(target.age)
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至于<code>isComplex</code>内部如何实现，完全看场景和需求。这一段的关键是：通过类型保护实现的判断，在判断的内部，完全按照该变量类型结构进行提示，开发体验非常棒。</p>
<h2 data-id="heading-4">创建节点</h2>
<p>每一种节点类型，都有对应的创建方法：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> id = types.identifier(<span class="hljs-string">'abc'</span>)
<span class="hljs-keyword">const</span> str = types.stringLiteral(<span class="hljs-string">'Hello World'</span>)
<span class="hljs-keyword">const</span> num = types.numericLiteral(<span class="hljs-number">10e3</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">实践</h1>
<p>先写个<code>log</code>方法</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> types <span class="hljs-keyword">from</span> <span class="hljs-string">'@babel/types'</span>
<span class="hljs-keyword">import</span> gen <span class="hljs-keyword">from</span> <span class="hljs-string">'@babel/generator'</span>

<span class="hljs-keyword">const</span> log = <span class="hljs-function">(<span class="hljs-params">node: types.Node</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(gen(node).code)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">创建值类型</h2>
<pre><code class="hljs language-ts copyable" lang="ts">log(types.stringLiteral(<span class="hljs-string">'string'</span>))
log(types.numericLiteral(<span class="hljs-number">10e4</span>))
log(types.booleanLiteral(<span class="hljs-number">0.5</span> > <span class="hljs-built_in">Math</span>.random()))
log(types.regExpLiteral(<span class="hljs-string">'\\.jsx?$'</span>, <span class="hljs-string">'g'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-sh copyable" lang="sh">% ts-node gen.ts
<span class="hljs-string">"string"</span>
100000
<span class="hljs-literal">false</span>
/\.jsx?$/g
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">创建Array</h2>
<pre><code class="hljs language-ts copyable" lang="ts">log(
    types.arrayExpression([
        types.stringLiteral(<span class="hljs-string">'string'</span>),
        types.numericLiteral(<span class="hljs-number">10e4</span>),
        types.booleanLiteral(<span class="hljs-number">0.5</span> > <span class="hljs-built_in">Math</span>.random()),
        types.regExpLiteral(<span class="hljs-string">'\\.jsx?$'</span>, <span class="hljs-string">'g'</span>)
    ])
)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-sh copyable" lang="sh">% ts-node gen.ts
[<span class="hljs-string">"string"</span>, 100000, <span class="hljs-literal">false</span>, /\.jsx?$/g]
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">创建Object</h2>
<pre><code class="hljs language-ts copyable" lang="ts">log(
    types.objectExpression([
        types.objectProperty(
            types.identifier(<span class="hljs-string">'a'</span>),
            types.nullLiteral()
        ),
        types.objectProperty(
            <span class="hljs-comment">// 字符串类型 key</span>
            types.stringLiteral(<span class="hljs-string">'*'</span>),
            types.arrayExpression([]),
        ),
        types.objectProperty(
            types.identifier(<span class="hljs-string">'id'</span>),
            types.identifier(<span class="hljs-string">'id'</span>),
            <span class="hljs-literal">false</span>,
            <span class="hljs-comment">// shorthand 对 &#123; id: id &#125; 简写为 &#123; id &#125;</span>
            <span class="hljs-literal">true</span>
        ),
        types.objectProperty(
            types.memberExpression(
                types.identifier(<span class="hljs-string">'props'</span>),
                types.identifier(<span class="hljs-string">'class'</span>)
            ),
            types.booleanLiteral(<span class="hljs-literal">true</span>),
            <span class="hljs-comment">// 计算值 key</span>
            <span class="hljs-literal">true</span>
        )
    ])
)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-sh copyable" lang="sh">% ts-node gen.ts
&#123;
  a: null,
  <span class="hljs-string">"*"</span>: [],
  id,
  [props.class]: <span class="hljs-literal">true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">创建具名 function</h2>
<pre><code class="hljs language-ts copyable" lang="ts">log(
    types.functionDeclaration(
        types.identifier(<span class="hljs-string">'foo'</span>),
        [types.identifier(<span class="hljs-string">'arg1'</span>)],
        types.blockStatement([
            types.expressionStatement(
                types.callExpression(
                    types.identifier(<span class="hljs-string">'console.log'</span>),
                    [types.identifier(<span class="hljs-string">'arg1'</span>)]
                )
            )
        ])
    )
)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-sh copyable" lang="sh">% ts-node gen.ts
<span class="hljs-keyword">function</span> foo(arg1) &#123;
  console.log(arg1);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">创建箭头函数</h2>
<pre><code class="hljs language-ts copyable" lang="ts">log(
    <span class="hljs-comment">// 无实体代码块</span>
    types.arrowFunctionExpression(
        [types.identifier(<span class="hljs-string">'arg1'</span>)],
        types.callExpression(
            types.identifier(<span class="hljs-string">'console.log'</span>),
            [types.identifier(<span class="hljs-string">'arg1'</span>)]
        )
    )
)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-sh copyable" lang="sh">% ts-node gen.ts
arg1 => console.log(arg1)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts">log(
    <span class="hljs-comment">// 有实体代码块</span>
    types.arrowFunctionExpression(
        [types.identifier(<span class="hljs-string">'arg1'</span>)],
        types.blockStatement([
            types.expressionStatement(
                types.callExpression(
                    types.identifier(<span class="hljs-string">'console.log'</span>),
                    [types.identifier(<span class="hljs-string">'arg1'</span>)]
                )
            )
        ])
    )
)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-sh copyable" lang="sh">% ts-node gen.ts
arg1 => &#123;
  console.log(arg1);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">JSX绑定值</h2>
<pre><code class="hljs language-ts copyable" lang="ts">log(
    types.jsxExpressionContainer(types.identifier(<span class="hljs-string">'props.name'</span>))
)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-sh copyable" lang="sh">% ts-node gen.ts
&#123;props.name&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">JSX节点</h2>
<pre><code class="hljs language-ts copyable" lang="ts">log(
    types.jsxElement(
        types.jsxOpeningElement(types.jsxIdentifier(<span class="hljs-string">'Text'</span>), []),
        types.jsxClosingElement(types.jsxIdentifier(<span class="hljs-string">'Text'</span>)),
        [types.jsxExpressionContainer(types.identifier(<span class="hljs-string">'props.name'</span>))]
    )
)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-sh copyable" lang="sh">% ts-node gen.ts
<Text>&#123;props.name&#125;</Text>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">JSXFragment</h2>
<pre><code class="hljs language-ts copyable" lang="ts">log(
    types.jsxFragment(
        types.jsxOpeningFragment(),
        types.jsxClosingFragment(),
        [
            types.jsxElement(
                types.jsxOpeningElement(types.jsxIdentifier(<span class="hljs-string">'Text'</span>), []),
                types.jsxClosingElement(types.jsxIdentifier(<span class="hljs-string">'Text'</span>)),
                [types.jsxExpressionContainer(types.identifier(<span class="hljs-string">'props.name'</span>))]
            ),
            types.jsxElement(
                types.jsxOpeningElement(types.jsxIdentifier(<span class="hljs-string">'Text'</span>), []),
                types.jsxClosingElement(types.jsxIdentifier(<span class="hljs-string">'Text'</span>)),
                [types.jsxExpressionContainer(types.identifier(<span class="hljs-string">'props.age'</span>))]
            )
        ]
    )
)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-sh copyable" lang="sh">% ts-node gen.ts
<><Text>&#123;props.name&#125;</Text><Text>&#123;props.age&#125;</Text></>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">综合应用：生成React函数式组件</h2>
<pre><code class="hljs language-ts copyable" lang="ts">log(
    types.program([
        types.importDeclaration(
            [types.importDefaultSpecifier(types.identifier(<span class="hljs-string">'React'</span>))],
            types.stringLiteral(<span class="hljs-string">'react'</span>)
        ),
        types.exportDefaultDeclaration(
            types.arrowFunctionExpression(
                [types.identifier(<span class="hljs-string">'props'</span>)],
                types.jsxElement(
                    types.jsxOpeningElement(types.jsxIdentifier(<span class="hljs-string">'Component'</span>), [
                        types.jsxAttribute(
                            types.jsxIdentifier(<span class="hljs-string">'onClick'</span>),
                            types.jSXExpressionContainer(
                                types.identifier(<span class="hljs-string">'handleClick'</span>)
                            )
                        )
                    ]),
                    types.jsxClosingElement(types.jsxIdentifier(<span class="hljs-string">'Component'</span>)),
                    [
                        types.jsxElement(
                            types.jsxOpeningElement(types.jsxIdentifier(<span class="hljs-string">'Image'</span>), [
                                types.jsxAttribute(
                                    types.jsxIdentifier(<span class="hljs-string">'src'</span>),
                                    types.stringLiteral(<span class="hljs-string">'https://image1.suning.cn/uimg/cms/img/159642507148437980.png'</span>)
                                )
                            ]),
                            types.jsxClosingElement(types.jsxIdentifier(<span class="hljs-string">'Image'</span>)),
                            [],
                            <span class="hljs-literal">true</span>
                        )
                    ],
                    <span class="hljs-literal">false</span>
                )
            )
        )
    ])
)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-sh copyable" lang="sh">% ts-node gen.ts
import React from <span class="hljs-string">"react"</span>;
<span class="hljs-built_in">export</span> default (props => <Component onClick=&#123;handleClick&#125;><Image src=<span class="hljs-string">"https://image1.suning.cn/uimg/cms/img/159642507148437980.png"</span>></Image></Component>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>主要是经验总结的流水账，多用多试就对了。</p>
<p>以上。</p></div>  
</div>
            