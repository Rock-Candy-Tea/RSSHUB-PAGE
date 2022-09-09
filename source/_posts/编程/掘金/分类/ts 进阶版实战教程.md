
---
title: 'ts 进阶版实战教程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5174'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 23:38:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=5174'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:-apple-system-font,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei UI,Microsoft YaHei,Arial,sans-serif;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:23px;margin-bottom:5px;font-weight:700;padding-left:10px;border-left:5px solid #773098&#125;.markdown-body h2&#123;font-size:19px;font-weight:700;padding-left:10px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:17px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;font-size:14px;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;display:block;max-width:100%;margin:1em 0;border-radius:6px;box-shadow:2px 4px 7px #999;user-select:none&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-family:-apple-system-font,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei UI,Microsoft YaHei,Arial,sans-serif;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-family:-apple-system-font,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei UI,Microsoft YaHei,Arial,sans-serif;font-weight:400;font-size:.9em;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8;scroll-behavior:smooth&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:14px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5;border-collapse:collapse&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;border:1px solid #916dd5&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>鉴于很多小伙伴说前段时间出的 <code>ts 教程</code>太过基础了，让我再出一期比较复杂的数据类型。今天就以我们平时开发过程中可能会遇到的类型简单讲解一下。</p>
<p>本期重点在后面的泛型，前面也是比较基础的。不想看的小伙伴可以直接定位拖到泛型的地方。</p>
<p>举例如下：</p>
<h3 data-id="heading-0">定义简单的基本数据类型：</h3>
<pre><code class="hljs language-ini copyable" lang="ini">const value:<span class="hljs-attr">string</span> = <span class="hljs-string">'北京'</span>
const index:<span class="hljs-attr">number</span> = <span class="hljs-number">1</span>
const flag:<span class="hljs-attr">boolean</span> = <span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">定义复杂数据类型：</h3>
<h4 data-id="heading-2"><strong>普通数组：</strong></h4>
<pre><code class="hljs language-less copyable" lang="less"><span class="hljs-selector-tag">const</span> <span class="hljs-selector-tag">strArr</span>:<span class="hljs-selector-tag">string</span><span class="hljs-selector-attr">[]</span> = <span class="hljs-selector-attr">[<span class="hljs-string">'0'</span>,<span class="hljs-string">'1'</span>,<span class="hljs-string">'2'</span>]</span>
<span class="hljs-selector-tag">const</span> <span class="hljs-selector-tag">numArr</span>:<span class="hljs-selector-tag">number</span><span class="hljs-selector-attr">[]</span> = <span class="hljs-selector-attr">[1,2,3]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3"><strong>包裹对象的数组：</strong></h4>
<pre><code class="hljs language-css copyable" lang="css"> const objArr:ObjArrType = [
        &#123;id:<span class="hljs-number">1</span>,name:<span class="hljs-string">'小红'</span>,age:<span class="hljs-number">18</span>&#125;
    ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种数组就比上面两个数组复杂一些， 我们需要去单独定义一个类型。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"> <span class="hljs-keyword">type</span> <span class="hljs-title class_">ObjArrType</span> = &#123;
    <span class="hljs-attr">id</span>:<span class="hljs-built_in">number</span>,
    <span class="hljs-attr">name</span>:<span class="hljs-built_in">string</span>,
    <span class="hljs-attr">age</span>:<span class="hljs-built_in">number</span>
&#125;[]
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4"><strong>树状数组：</strong></h4>
<pre><code class="hljs language-css copyable" lang="css">const treeArr:TreeArr[] = [
        &#123;id:<span class="hljs-number">1</span>,name:<span class="hljs-string">'小红'</span>,age:<span class="hljs-number">18</span>,children:[
            &#123;
                id:<span class="hljs-number">112</span>,name:<span class="hljs-string">'小兰'</span>,age:<span class="hljs-number">23</span>
            &#125;
        ]&#125;
    ]
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> <span class="hljs-title class_">TreeArr</span> = &#123;
    <span class="hljs-attr">id</span>:<span class="hljs-built_in">number</span>,
    <span class="hljs-attr">name</span>:<span class="hljs-built_in">string</span>,
    <span class="hljs-attr">age</span>:<span class="hljs-built_in">number</span>,
    children?: <span class="hljs-title class_">TreeArr</span>[]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5"><strong>对象：</strong></h4>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> <span class="hljs-attr">obj</span>:&#123;<span class="hljs-attr">id</span>:<span class="hljs-built_in">number</span>,<span class="hljs-attr">name</span>:<span class="hljs-built_in">string</span>,<span class="hljs-attr">age</span>:<span class="hljs-built_in">number</span>&#125; = &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">112</span>,<span class="hljs-attr">name</span>:<span class="hljs-string">'小兰'</span>,<span class="hljs-attr">age</span>:<span class="hljs-number">23</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者：</p>
<pre><code class="hljs language-css copyable" lang="css">const obj:ObjType = &#123;
        id:<span class="hljs-number">112</span>,name:<span class="hljs-string">'小兰'</span>,age:<span class="hljs-number">23</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> <span class="hljs-title class_">ObjType</span> = &#123;
    <span class="hljs-attr">id</span>:<span class="hljs-built_in">number</span>,
    <span class="hljs-attr">name</span>:<span class="hljs-built_in">string</span>,
    <span class="hljs-attr">age</span>:<span class="hljs-built_in">number</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6"><strong>函数：</strong></h4>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-comment">//              形参        返回值</span>
<span class="hljs-type">const</span> handle = (val:<span class="hljs-built_in">string</span>):<span class="hljs-built_in">string</span>=>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">'1'</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：如果定义返回值类型不为 <code>void</code> 或 <code>any</code>， 必须 <code>return 值</code>！</p>
<h3 data-id="heading-7">定义 useState</h3>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-keyword">const</span> [<span class="hljs-keyword">val</span>, setVal] = useState<number>(<span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义useState 的类型，需要使用到泛型，格式是 <code><类型></code>。</p>
<p>说起泛型，也是我们日常工作中会经常用到的一个类型。这个类型也是比较麻烦的一个。下面我给大家简单的讲解一下：</p>
<h3 data-id="heading-8">泛型:</h3>
<p>书写格式一般是用一对 <code><></code> 包裹起来的。 里面可以传入你需要的类型。</p>
<p>例如： <code><T></code>， 这个 T， 就是你传入的类型，他可以是 <code>string</code>， <code>number</code>、<code>boolean</code>、<code>联合类型</code>、以及自己用 <code>type </code>定义的类型。</p>
<p>我们可以使用 <code>泛型</code> 来创建可重用的组件，一个组件可以支持多种类型的数据。 这样就可以以自己的数据类型来使用组件。</p>
<p>例如：</p>
<pre><code class="hljs language-r copyable" lang="r"><span class="hljs-keyword">function</span> identity<span class="hljs-operator"><</span><span class="hljs-built_in">T</span><span class="hljs-operator">></span><span class="hljs-punctuation">(</span>arg<span class="hljs-operator">:</span> <span class="hljs-built_in">T</span><span class="hljs-punctuation">)</span><span class="hljs-operator">:</span> <span class="hljs-built_in">T</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-built_in">return</span> arg;
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们可以很清晰的知道，返回值和参数是一致的。我们把这个版本的<code>identity</code>函数叫做泛型，因为它<code>可以适用于多个类型</code>。</p>
<p>我们定义了泛型函数后，可以这样使用。传入所有的参数，包含类型参数：</p>
<pre><code class="hljs language-ini copyable" lang="ini">let <span class="hljs-attr">output</span> = identity<string>(<span class="hljs-string">"myString"</span>)<span class="hljs-comment">; </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们明确的指定了<code>T</code>是<code>string</code>类型，并做为一个参数传给函数。</p>
<p>再看下一个例子：</p>
<p>还是这个函数：</p>
<pre><code class="hljs language-r copyable" lang="r"><span class="hljs-keyword">function</span> identity<span class="hljs-operator"><</span><span class="hljs-built_in">T</span><span class="hljs-operator">></span><span class="hljs-punctuation">(</span>arg<span class="hljs-operator">:</span> <span class="hljs-built_in">T</span><span class="hljs-punctuation">)</span><span class="hljs-operator">:</span> <span class="hljs-built_in">T</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-built_in">return</span> arg;
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们想同时打印出<code>arg</code>的长度。 我们很可能会这样做：</p>
<pre><code class="hljs language-matlab copyable" lang="matlab"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loggingIdentity</span><<span class="hljs-title">T</span>><span class="hljs-params">(arg: T)</span>: <span class="hljs-title">T</span> &#123;</span>
    console.<span class="hljs-built_in">log</span>(arg.<span class="hljs-built_in">length</span>);  // Error: T doesn't have .<span class="hljs-built_in">length</span>
    <span class="hljs-keyword">return</span> arg;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里就会报错，说我们使用了<code>arg</code>的<code>.length</code>属性，但是没有地方指明<code>arg</code>具有这个属性。这里的 <code>T</code>代表的是任意类型，所以使用这个函数的人可能传入的是个数字，而数字是没有 <code>.length</code>属性的。</p>
<p>所以，如果我们想操作<code>T</code>类型的数组而不直接是<code>T</code>， 可以这么写：</p>
<pre><code class="hljs language-lua copyable" lang="lua"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loggingIdentity</span><<span class="hljs-title">T</span>><span class="hljs-params">(arg: T[])</span></span>: T[] &#123;
    console.<span class="hljs-built_in">log</span>(<span class="hljs-built_in">arg</span>.length);  
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">arg</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以这样理解这里的这个泛型<code>T</code>。泛型函数<code>loggingIdentity</code>，接收类型参数<code>T</code>和参数<code>arg</code>，这个参数 arg 它是个<code>T</code>类型的数组，并返回元素类型是<code>T</code>的数组，所以我们就可以很自然的打印 <code>.lnegth</code> 属性了。</p>
<p>再举个例子：</p>
<p>当我们发请求时，一般会封装一个请求函数，那这个请求函数的参数类型以及返回值类型怎么定义呢？</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> getDateNumList = <span class="hljs-keyword">async</span> (<span class="hljs-attr">url</span>: <span class="hljs-built_in">string</span>, params?: <span class="hljs-title class_">ParamsType</span>): <span class="hljs-title class_">Promise</span><<span class="hljs-title class_">ResultType</span><<span class="hljs-title class_">CardType</span>>> => &#123;
    <span class="hljs-keyword">const</span> &#123; data &#125; = <span class="hljs-keyword">await</span> axiosInstance.<span class="hljs-title function_">post</span>(<span class="hljs-string">`<span class="hljs-subst">$&#123;url&#125;</span>`</span>, params)
    <span class="hljs-keyword">return</span> data
&#125;
​
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数类型相比不用我再多说了，<code>url</code> 是一个字符串类型，<code>params</code> 是一个我们自己定义的类型。关键是后面的返回值。有的小伙伴可能有点看不懂为什么这么写了。为什么泛型里面再套一个泛型，这个返回值是什么格式的呢？</p>
<p>我先把上面的返回值类型给拆分一下，类型一个一个的写出来：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> <span class="hljs-title class_">ResultType</span><T> &#123;
    <span class="hljs-attr">code</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-built_in">string</span>,
    <span class="hljs-attr">data</span>: T,
&#125;
​
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> <span class="hljs-title class_">CardType</span> = &#123;
    id?: <span class="hljs-built_in">number</span> | <span class="hljs-literal">undefined</span>;
    age?: <span class="hljs-built_in">number</span> | <span class="hljs-literal">undefined</span>;
    name?: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>;
    height?: <span class="hljs-built_in">number</span> | <span class="hljs-literal">undefined</span>;
    weight?: <span class="hljs-built_in">number</span> |<span class="hljs-literal">undefined</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，我们最外面是一个 <code>Promise</code> 类型， 他是一个泛型， 泛型内容写的是 <code>ResultType</code> ,也就是我们接口返回最外层的类型，有 <code>code</code>、<code>message</code>、<code>data</code>。其中，<code>data</code> 也是一个泛型，用 <code>T</code> 来表示，就说明，这个 <code>data</code> 的类型，你传什么，他就是什么类型。</p>
<p>这里我们传的是 <code>CardType</code> 这个类型，那表示，最终 <code>data</code> 的类型就是 <code>CardType</code> 类型。</p>
<p>关于 <code>interface</code>接口，我就不再细说了，不怎么会的小伙伴们可以看看前面的基础教程，里面有写，或者看看官网。</p>
<p>官网地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.tslang.cn%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.tslang.cn/index.html" ref="nofollow noopener noreferrer">www.tslang.cn/index.html</a></p></div>  
</div>
            