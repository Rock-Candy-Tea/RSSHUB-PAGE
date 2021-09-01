
---
title: '实现一个函数的compile'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3100'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 20:22:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=3100'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">AST</h3>
<p>为什么前端变得越来越复杂了，各种框架，babel,typescript,webpack,rollup,etc.<br>
但以上的工具的前提是需要编译，而javascript的编译工作主要是基于 ast 。各种框架/脚手架/语言，都会通过 ast 将代码编译生成符合自己需求的，可以在浏览器运行的js代码。编译流程如下：<br>
1 tokenizer： 分词，将所有代码分为一个个 token;<br>
2 parse: 语法解析，将一个个 token 装进语法树;<br>
3 transform: 按照一些自定义规则替换/修改语法树;<br>
4 generator: 再把语法树转化为可以正常运行的js代码;<br>
本文主要是参考 recast && the-super-tiny-compiler 实践下js代码编译的整个过程，了解下 ast 在前端的应用。</p>
<p>注：本文仅实现一个简单 sum 函数的编译过程。仓库地址： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fbinvb%2Fsimple-function-ast-demo" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/binvb/simple-function-ast-demo" ref="nofollow noopener noreferrer">github.com/binvb/simpl…</a></p>
<h3 data-id="heading-1">ast 结果</h3>
<p>在实现之前，我们先看一下现有的编译工具生成结果。通过一个 recast 工具试验下将源码编译为 ast 的效果：</p>
<pre><code class="copyable">import * as recast from 'recast'

let sourceCode = `
    function sum(a, b) &#123;
        return a + b
    &#125;
`
console.log(JSON.stringify(recast.parse(sourceCode)))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将编译出来的 JSON 字符串格式化后有接近三千行代码！但关键数据在 program.body 中，program.body的数据结构如下：</p>
<pre><code class="copyable">"type": "FunctionDeclaration", // 函数标志符  
"id":&#123;...&#125;, // 函数名等
"params": [...], // 函数传参  
"body":&#123;...&#125;, // 函数 block 里面的内容  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实这个数据结构里面还有很多东西，包括开始结束位置(行，列)，缩进等，但这些不是主要内容，所以省略了。</p>
<h3 data-id="heading-2">tokenizer</h3>
<p>在分词的阶段，我们先提取一下我们需要的关键字，以及分析关键字的分词规则：<br>
1 function: 前后空白;<br>
2 function name: 在function之前, paren之后;<br>
3 paren: 关键字'(' or ')';<br>
5 comma: 关键字 ',';<br>
6 bracket: 关键字 '&#123;' or '&#125;';<br>
7 return: 前后空白;<br>
8 plus： 特殊符号;
9 variate: 字符串变量名;<br>
10 blank: 空白;<br>
然后将源码按最小单位切割进行匹配，e.g.</p>
<pre><code class="copyable">function tokenizer(input) &#123;
    let current = 0

    while(current < input.length>) &#123;
      // 先匹配单个字符串的分词规则
      if(_char === '(' || _char === ')' ) &#123;
        tokens.push(&#123;
          type: 'paren',
          value: _char
        &#125;)
        current++
        continue
      &#125;
      ...
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">parse</h3>
<p>在解析阶段，我们需要将 token 一个个装入我们的语法树中:</p>
<pre><code class="copyable">// from 
[
    &#123;
        type: 'FunctionDeclaration',
        value: 'function'
    &#125;
    ...
]
// to
&#123;
    program: &#123;
        body: [
            &#123;
                type: 'FunctionDeclaration',
                params: [...],
                id: &#123;
                    name: 'sum'
                &#125;,
                body:[
                    &#123;
                        type: 'blockStament',
                        body: [...]
                    &#125;
                ]
            &#125;
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>处理思路，因为token是一个扁平化的数组结构，我们需要一层层将数据插入到语法树中,可以用到宽度优先算法用递归的方式进行计算：</p>
<pre><code class="copyable">function parse(tree, startIndex=0) &#123;
    let root = []
    let treeLength = tree.length

    for(let i = startIndex; i < treeLength; i++) &#123;
        // function
        if(tree[i].type === 'FunctionDeclaration') &#123;
            let blockRangeEnd = getBlockStatementList(tree, i, '&#125;').index

            root.push(&#123;
                type: 'FunctionDeclaration',
                params: [
                    ...getFunctionParams(tree, i + 1, ')')
                ],
                id: &#123;
                    name: getNextToken(tree, i + 1)
                &#125;,
                body: parse(tree.slice(i + 1, blockRangeEnd))
            &#125;)
            i = blockRangeEnd
        &#125;
        // return statement
        if(tree[i].type === 'ReturnExpressionStatement') &#123;
            let blockRangeEnd = getBlockStatementList(tree, i, '&#125;').index
            
            root.push(&#123;
                type: 'ReturnExpressionStatement',
                body: getExpressionStatement(tree.slice(i + 1, blockRangeEnd))
            &#125;)
            i = blockRangeEnd
        &#125;
        ...
    &#125;

    return root
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">transform</h3>
<p>在这个阶段，一般是框架/语言需要将一些不能在v8直接运行/或兼容版本的代码，转化为可以直接在v8上跑的代码(e.g. typescript, v8, etc.)。<br>
这里为了方便，只是做一个简单的变量转化，e.g.</p>
<pre><code class="copyable">// 将所有函数中变量名为a的变量改为数字 1
function transform(ast) &#123;
    for(let i = 0; i < ast.length; i++) &#123;
        if(ast[i].type === 'FunctionDeclaration') &#123;
            transform(ast[i].body)
        &#125;
        if(ast[i].type === 'ReturnExpressionStatement') &#123;
            transform(ast[i].body)
        &#125;
        if(ast[i].type === 'variate' && ast[i].value === 'a') &#123;
            ast[i].value = 1
        &#125;
    &#125;

    return ast
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">generator</h3>
<p>这个步骤我们需要将 transform 后的 ast 反序列化回到 tokens，再将 tokens 生成字符串即可(具体代码可到仓库查看)。最后获取到:</p>
<pre><code class="copyable">function sum(a,b)&#123;return 1 + b&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完结撒花</p>
<h3 data-id="heading-6">问题记录</h3>
<p>1 分词阶段-必须从文件最开始的地方按顺序开始分词，而且有很多的分词规则，那这个切割的方式要怎么实现？<br>
切割为最小单元，所有的字符/空白全部都切割为一个单元。先从跟最小单元一样大小的分词规则开始匹配。</p>
<p>2 分词阶段-是否需要区分函数名, 参数名, 变量?需要的话怎么区分，因为按照分词规则，是进行连续匹配的。
参照规范是需要区分的，因为后续会需要对不同类型做不一样的操作的。<br>
需要增加一个维度的匹配规则：</p>
<pre><code class="copyable">1 对于函数名，连续字符串前面是空白，空白前面是'function';  
2 对于参数名，前后面 空白/逗号/();  
3 对于变量，前后空白;  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3 语法解析阶段-对于一些特殊字符，例如函数参数之间的逗号，是否需要在语法树中存储下来，存储下来的话是放到哪个位置？
规范的结构是需要存储的，主要是需要记录位置，但这个对于这个项目来说不重要且会大大增加复杂度，所以暂时不存储。</p>
<p>4 语法解析阶段-如何从token提取当前 blockStatement 的的同级结构。e.g.</p>
<pre><code class="copyable">// a 和 b 应该是在同一层树节点上
function test() &#123;
    function a() &#123;
        //...
    &#125;
    function b() &#123;
        //...
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从 blockStament 开始符号 '&#123;' 到结束符号 '&#125;' 提取到一个同级节点上(实际上要复杂非常多，例如 &#123;&#123;...&#123;&#125;...&#125;&#125;, 但这里暂时不需要考虑太多)。</p>
<p>5 generator阶段-如何将ast转为token？<br>
因为 ast 是按照顺序生成的，所以可以通过深度优先遍历提取所有的token.</p>
<h3 data-id="heading-7">规范</h3>
<p>虽然有很多工具实现了ast， 但如果每个工具/框架都有自己的实现和规范，就会造成混乱，所以各种工具的 ast 都是一样的。
规范参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Festree%2Festree" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/estree/estree" ref="nofollow noopener noreferrer">github.com/estree/estr…</a></p>
<h3 data-id="heading-8">相关工具</h3>
<p>1 recast <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fbenjamn%2Frecast" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/benjamn/recast" ref="nofollow noopener noreferrer">github.com/benjamn/rec…</a></p>
<pre><code class="copyable">// 将源码parse为语法树
reacast.parse(sourcecode)
// 将语法树转化为源码
reacast.print(ast)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">参考文档</h3>
<p>4 the-super-tiny-compiler <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjamiebuilds%2Fthe-super-tiny-compiler" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jamiebuilds/the-super-tiny-compiler" ref="nofollow noopener noreferrer">github.com/jamiebuilds…</a><br>
5 AST抽象语法树 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000016231512" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000016231512" ref="nofollow noopener noreferrer">segmentfault.com/a/119000001…</a></p></div>  
</div>
            