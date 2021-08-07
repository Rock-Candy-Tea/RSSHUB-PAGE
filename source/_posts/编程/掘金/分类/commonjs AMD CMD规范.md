
---
title: 'common.js AMD CMD规范'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9112'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 20:05:24 GMT
thumbnail: 'https://picsum.photos/400/300?random=9112'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong>”</p>
<h2 data-id="heading-0">1、AMD:</h2>
<p>Require.js，一个强大的工具包，它能够自动的把混乱的前端脚本加载的规整而有序，Require.js主要用于客户端的模块管理，和其他js库类似，首先你需要引入，如下：</p>
<p>data-main:指定主代码所在的脚本文件，对应JS目录下的main.js,requireJs在读取本地JS文件时，可以省略.js后缀，如果是第三方JS，则需要.js后缀，async="true" defer=“defer" 主要是屏蔽浏览器的差异，延迟加载脚本</p>
<p>require.js 主要提供define和require两个方法来进行模块化编程，前者来定义模块，后者用来调用模块,这种模块定义的方法不会污染全局环境，能够清晰的显示依赖关系。</p>
<p>require方法本身也是一个对象，可以使用自带的config方法，进行模块的运行参数配置，config接收任意对象作为参数，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">require</span>.config(&#123;

    <span class="hljs-attr">baseUrl</span> : “/“ <span class="hljs-comment">//配置文件的访问路径</span>

    <span class="hljs-attr">paths</span> :&#123;

    “jquery”: “js/jquery-<span class="hljs-number">1.90</span><span class="hljs-string">"

    &#125;
&#125;);
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>对jquery的调用也较为方便，使用require方法，传入2个参数，模块名以及回调函数,如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">require</span>( [‘jquery’,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">$</span>)</span>&#123;

        <span class="hljs-comment">// you jquery code</span>

        $(‘#id’).click(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;);

        &#125;]);

        <span class="hljs-comment">//   文件名: foo.js</span>

        define([‘jquery<span class="hljs-string">'],function($)&#123;

          //方法

        function myFunc()&#123;&#125;;

        //   暴露公共方法

        return myFunc;

        &#125;);

        //复杂点的例子

        //文件名:foo.js 

        define([‘jquery’,’underscore'</span>],<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">$, _</span>)</span>&#123;
        <span class="hljs-comment">//  方法</span>

        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>)</span>&#123;&#125;; <span class="hljs-comment">//私有方法，因为没有被返回</span>

        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span>(<span class="hljs-params"></span>)</span>&#123;&#125;;  <span class="hljs-comment">//公共方法，因为被返回了</span>

        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">c</span>(<span class="hljs-params"></span>)</span>&#123;&#125;; <span class="hljs-comment">//公共方法，因为被返回了</span>

        <span class="hljs-comment">//  暴露公共方法</span>

        <span class="hljs-keyword">return</span> &#123;

        <span class="hljs-attr">b</span>: b,

        <span class="hljs-attr">c</span>: c

        &#125;

&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2、common Js  通用JS模块化规范-适用于server端 //一个模块对应一个文件</h2>
<p>eg：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//    文件名：foo.js</span>

<span class="hljs-comment">//  依赖</span>

<span class="hljs-keyword">var</span> $ = <span class="hljs-built_in">require</span>(‘jquery’);

<span class="hljs-comment">// 方法</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myFunc</span>(<span class="hljs-params"></span>)</span>&#123;&#125;;

<span class="hljs-comment">//暴露公共方法(一个)</span>

<span class="hljs-built_in">module</span>.exports = myFunc;

<span class="hljs-comment">//复杂例子</span>

<span class="hljs-comment">//    文件名 foo.js</span>

<span class="hljs-keyword">var</span> $ = <span class="hljs-built_in">require</span>(‘jquery’);

<span class="hljs-keyword">var</span> _ = <span class="hljs-built_in">require</span>(‘underscore’);

<span class="hljs-comment">// methods</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>)</span>&#123;&#125;; <span class="hljs-comment">//私有方法 因为没有在下面公共方法里面暴露出来</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">b</span>(<span class="hljs-params"></span>)</span>&#123;&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">c</span>(<span class="hljs-params"></span>)</span>&#123;&#125;;

<span class="hljs-comment">//暴露公共方法</span>

<span class="hljs-built_in">module</span>.exports = &#123;

<span class="hljs-attr">b</span>: b,

<span class="hljs-attr">c</span>: c

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、UMD（通用模块规范） 兼容AMD和CommonJs，同时还支持老式的”全局”变量规范</p>
<pre><code class="hljs language-js copyable" lang="js">( <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">root, factory</span>)</span>&#123;

<span class="hljs-keyword">if</span>( <span class="hljs-keyword">typeof</span> define === ‘<span class="hljs-function"><span class="hljs-keyword">function</span>’ && <span class="hljs-title">define</span>.<span class="hljs-title">amd</span>)</span>&#123;

<span class="hljs-comment">//AMD</span>

define([‘jquery’],factory);

&#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>( <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">exports</span> == ‘object<span class="hljs-string">' )&#123;

//Node、CommonJs之类的

mode.exports = factory(require(‘query'</span>));

&#125;<span class="hljs-keyword">else</span>&#123;

<span class="hljs-comment">//浏览器全局变量( root 即window)</span>

root.returnExports = factory(root.jQuery);

&#125;

&#125;(<span class="hljs-built_in">this</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">$</span>)</span>&#123;

<span class="hljs-comment">//方法 </span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myFunc</span>(<span class="hljs-params"></span>)</span>&#123;&#125;;

<span class="hljs-comment">//暴露公共方法</span>

<span class="hljs-keyword">return</span> myFunc;s

&#125;))
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            