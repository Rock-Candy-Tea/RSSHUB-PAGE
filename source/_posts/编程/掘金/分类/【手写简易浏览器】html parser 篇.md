
---
title: '【手写简易浏览器】html parser 篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37c319245fe941c281e6c12a598de609~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 07:44:09 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37c319245fe941c281e6c12a598de609~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第6天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>。</p>
<p><a href="https://juejin.cn/post/6969575610108772359" target="_blank">上篇文章</a>介绍了整体的思路，这篇开始写 html parser。</p>
<h2 data-id="heading-0">思路分析</h2>
<p>实现 html parser 主要分为词法分析和语法分析两步。</p>
<h3 data-id="heading-1">词法分析</h3>
<p>词法分析需要把每一种类型的 token 识别出来，具体的类型有：</p>
<ul>
<li>开始标签，如 <div></li>
<li>结束标签，如 </div></li>
<li>注释标签，如 <!--comment--></li>
<li>doctype 标签，如 <!doctype html></li>
<li>text，如 aaa</li>
</ul>
<p>这是最外层的 token，开始标签内部还要分出属性，如 id="aaa" 这种。</p>
<p>也就是有这几种情况：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37c319245fe941c281e6c12a598de609~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>第一层判断是否包含 <，如果不包含则是 text，如果包含则再判断是哪一种，如果是开始标签，还要对其内容再取属性，直到遇到 > 就重新判断。</p>
<h3 data-id="heading-2">语法分析</h3>
<p>语法分析就是对上面分出的 token 进行组装，生成 ast。</p>
<p>html 的 ast 的组装主要是考虑父子关系，记录当前的 parent，然后 text、children 都设置到当前 parent 上。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fafdccdeebe7427c85dc4378432809dd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们来用代码实现一下：</p>
<h2 data-id="heading-3">代码实现</h2>
<h3 data-id="heading-4">词法分析</h3>
<p>首先，我们要把 startTag、endTag、comment、docType 还有 attribute  的正则表达式写出来：</p>
<h4 data-id="heading-5">正则</h4>
<ul>
<li>结束标签就是 </ 开头，然后 a-zA-Z0-9 和 - 出现多次，之后是 ></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> endTagReg = <span class="hljs-regexp">/^<\/([a-zA-Z0-9\-]+)>/</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>注释标签是 <!-- 和 --> 中间夹着非 --> 字符出现任意次</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> commentReg = <span class="hljs-regexp">/^<!\-\-[^(-->)]*\-\->/</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>doctype 标签是 <!doctype 加非 > 字符出现多次，加 ></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> docTypeReg = <span class="hljs-regexp">/^<!doctype [^>]+>/</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>attribute 是多个空格开始，加 a-zA-Z0-9 或 - 出现多次，接一个 =，之后是非 > 字符出多次</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> attributeReg = <span class="hljs-regexp">/^(?:[ ]+([a-zA-Z0-9\-]+=[^>]+))/</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>开始标签是 < 开头，接 a-zA-Z0-9 和 - 出现多次，然后是属性的正则，最后是 > 结尾</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> startTagReg = <span class="hljs-regexp">/^<([a-zA-Z0-9\-]+)(?:([ ]+[a-zA-Z0-9\-]+=[^> ]+))*>/</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">分词</h4>
<p>之后，我们就可以基于这些正则来分词，第一层处理 < 和 text：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">parse</span>(<span class="hljs-params">html, options</span>) </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">advance</span>(<span class="hljs-params">num</span>) </span>&#123;
        html = html.slice(num);
    &#125;

    <span class="hljs-keyword">while</span>(html)&#123;
        <span class="hljs-keyword">if</span>(html.startsWith(<span class="hljs-string">'<'</span>)) &#123;
            <span class="hljs-comment">//...</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">let</span> textEndIndex = html.indexOf(<span class="hljs-string">'<'</span>);
            options.onText(&#123;
                <span class="hljs-attr">type</span>: <span class="hljs-string">'text'</span>,
                <span class="hljs-attr">value</span>: html.slice(<span class="hljs-number">0</span>, textEndIndex)
            &#125;);
            textEndIndex = textEndIndex === -<span class="hljs-number">1</span> ? html.length: textEndIndex;
            advance(textEndIndex);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二层处理 <!-- 和 <!doctype 和结束标签、开始标签：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> commentMatch = html.match(commentReg);
<span class="hljs-keyword">if</span> (commentMatch) &#123;
    options.onComment(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'comment'</span>,
        <span class="hljs-attr">value</span>: commentMatch[<span class="hljs-number">0</span>]
    &#125;)
    advance(commentMatch[<span class="hljs-number">0</span>].length);
    <span class="hljs-keyword">continue</span>;
&#125;

<span class="hljs-keyword">const</span> docTypeMatch = html.match(docTypeReg);
<span class="hljs-keyword">if</span> (docTypeMatch) &#123;
    options.onDoctype(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'docType'</span>,
        <span class="hljs-attr">value</span>: docTypeMatch[<span class="hljs-number">0</span>]
    &#125;);
    advance(docTypeMatch[<span class="hljs-number">0</span>].length);
    <span class="hljs-keyword">continue</span>;
&#125;

<span class="hljs-keyword">const</span> endTagMatch = html.match(endTagReg);
<span class="hljs-keyword">if</span> (endTagMatch) &#123;
    options.onEndTag(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'tagEnd'</span>,
        <span class="hljs-attr">value</span>: endTagMatch[<span class="hljs-number">1</span>]
    &#125;);
    advance(endTagMatch[<span class="hljs-number">0</span>].length);
    <span class="hljs-keyword">continue</span>;
&#125;

<span class="hljs-keyword">const</span> startTagMatch = html.match(startTagReg);
<span class="hljs-keyword">if</span>(startTagMatch) &#123;    
    options.onStartTag(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'tagStart'</span>,
        <span class="hljs-attr">value</span>: startTagMatch[<span class="hljs-number">1</span>]
    &#125;);

    advance(startTagMatch[<span class="hljs-number">1</span>].length + <span class="hljs-number">1</span>);
    <span class="hljs-keyword">let</span> attributeMath;
    <span class="hljs-keyword">while</span>(attributeMath = html.match(attributeReg)) &#123;
        options.onAttribute(&#123;
            <span class="hljs-attr">type</span>: <span class="hljs-string">'attribute'</span>,
            <span class="hljs-attr">value</span>: attributeMath[<span class="hljs-number">1</span>]
        &#125;);
        advance(attributeMath[<span class="hljs-number">0</span>].length);
    &#125;
    advance(<span class="hljs-number">1</span>);
    <span class="hljs-keyword">continue</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过词法分析，我们能拿到所有的 token：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/850a3683fe9749b08633640666d0149e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">语法分析</h3>
<p>token 拆分之后，我们需要再把这些 token 组装在一起，只处理 startTag、endTag 和 text 节点。通过 currentParent 记录当前 tag。</p>
<ul>
<li>startTag 创建 AST，挂到 currentParent 的 children 上，然后 currentParent 变成新创建的 tag</li>
<li>endTag 的时候把 currentParent 设置为当前 tag 的 parent</li>
<li>text 也挂到 currentParent 上</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">htmlParser</span>(<span class="hljs-params">str</span>) </span>&#123;
    <span class="hljs-keyword">const</span> ast = &#123;
        <span class="hljs-attr">children</span>: []
    &#125;;
    <span class="hljs-keyword">let</span> curParent = ast;
    <span class="hljs-keyword">let</span> prevParent = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">const</span> domTree = parse(str,&#123;
        <span class="hljs-function"><span class="hljs-title">onComment</span>(<span class="hljs-params">node</span>)</span> &#123;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">onStartTag</span>(<span class="hljs-params">token</span>)</span> &#123;
            <span class="hljs-keyword">const</span> tag = &#123;
                <span class="hljs-attr">tagName</span>: token.value,
                <span class="hljs-attr">attributes</span>: [],
                <span class="hljs-attr">text</span>: <span class="hljs-string">''</span>,
                <span class="hljs-attr">children</span>: []
            &#125;;
            curParent.children.push(tag);
            prevParent = curParent;
            curParent = tag;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">onAttribute</span>(<span class="hljs-params">token</span>)</span> &#123;
            <span class="hljs-keyword">const</span> [ name, value ] = token.value.split(<span class="hljs-string">'='</span>);
            curParent.attributes.push(&#123;
                name,
                <span class="hljs-attr">value</span>: value.replace(<span class="hljs-regexp">/^['"]/</span>, <span class="hljs-string">''</span>).replace(<span class="hljs-regexp">/['"]$/</span>, <span class="hljs-string">''</span>)
            &#125;);
        &#125;,
        <span class="hljs-function"><span class="hljs-title">onEndTag</span>(<span class="hljs-params">token</span>)</span> &#123;
            curParent = prevParent;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">onDoctype</span>(<span class="hljs-params">token</span>)</span> &#123;
        &#125;,
        <span class="hljs-function"><span class="hljs-title">onText</span>(<span class="hljs-params">token</span>)</span> &#123;
            curParent.text = token.value;
        &#125;
    &#125;);
    <span class="hljs-keyword">return</span> ast.children[<span class="hljs-number">0</span>];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们试一下效果：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> htmlParser = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./htmlParser'</span>);

<span class="hljs-keyword">const</span> domTree = htmlParser(<span class="hljs-string">`
<!doctype html>
<body>
    <div>
        <!--button-->
        <button>按钮</button>
        <div id="container">
            <div class="box1">
                <p>box1 box1 box1</p>
            </div>
            <div class="box2">
                <p>box2 box2 box2</p>
            </div>
        </div>
    </div>
</body>
`</span>);

<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">JSON</span>.stringify(domTree, <span class="hljs-literal">null</span>, <span class="hljs-number">4</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>成功生成了正确的 AST。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/669b57cdec0d46d7868e73ab4bf4900f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">总结</h2>
<p>这篇是简易浏览器中 html parser 的实现，少了自闭合标签的处理，就是差一个 if else，后面会补上。</p>
<p>我们分析了思路并进行了实现：通过正则来进行 token 的拆分，把拆出的 token 通过回调函数暴露出去，之后进行 AST 的组装，需要记录当前的 parent，来生成父子关系正确的 AST。</p>
<p>html parser 其实也是淘系前端的多年不变的面试题之一，而且 vue template compiler 还有 jsx 的 parser 也会用到类似的思路。还是有必要掌握的。希望本文能帮大家理清思路。</p>
<p>代码在 <a href="https://github.com/QuarkGluonPlasma/tiny-browser" target="_blank" rel="nofollow noopener noreferrer">github</a>。</p></div>  
</div>
            