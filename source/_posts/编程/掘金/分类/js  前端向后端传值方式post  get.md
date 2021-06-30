
---
title: 'js  前端向后端传值方式post  get'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3553'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 00:52:01 GMT
thumbnail: 'https://picsum.photos/400/300?random=3553'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1.首先后端<code>request</code>获取请求参数</h3>
<h3 data-id="heading-1">2.前端提交参数</h3>
<p>最为常见的客户端传递参数方式有两种：post  get</p>
<pre><code class="copyable">浏览器地址栏直接输入：一定是GET请求；可以直接在ajax中url拼接数据
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//url传值</span>
 <span class="hljs-attr">url</span>: <span class="hljs-string">"TestJsonServlet?id="</span>+id+<span class="hljs-string">"&gender="</span>+<span class="hljs-string">"男"</span>, <span class="hljs-comment">//提价的路径</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">超链接：一定是GET请求；
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//通过a标签提交数据，通过a标签的href属性提交数据，和js提交数据类似。</span>
<a href=<span class="hljs-string">"DeleteUserServlet?id='3'&gender='男'"</span>></a>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">表单：可以是GET，也可以是POST，这取决与<form>的method属性值；
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//form表单把所有属于表单中的内容提交给后台，例如输入框，单选框，多选框，文本域，文件域等。</span>
<span class="hljs-comment">//1.在后台可通过对应的name属性获取相应的值。</span>
<span class="hljs-comment">//2.from表单中的action属性标识提交数据的地址。</span>
<span class="hljs-comment">//3.method属性指明表单提交的方式。</span>
<form action=<span class="hljs-string">"demo.do"</span> method=<span class="hljs-string">"post"</span>>
        用户名：<br>
        <input type="text" name="username"><br>
        密码:<br>
        <input type="password" name="password" ><br><br>
        <input type="submit" value="提交">
    </form>

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">JS提交数据，通过window.location.href指定路径提交数据。
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> deleteUser = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">deleteId</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (confirm(<span class="hljs-string">"确认删除编号是【"</span>+deleteId+<span class="hljs-string">"】的成员吗?"</span>))&#123;
            <span class="hljs-built_in">window</span>.location.href=<span class="hljs-string">"DeleteUserServlet?deleteId="</span>+deleteId;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">JQuery中的ajax提交（常用）</h3>
<p>JavaScript中也有ajax提交，但是代码太多，所以JQuery对JS中的ajax进行了简化。引入JQuery相应的包即可使用。一般格式为：</p>
<pre><code class="hljs language-js copyable" lang="js">.ajax(&#123;
            <span class="hljs-attr">url</span>: <span class="hljs-string">"TestJsonServlet"</span>, <span class="hljs-comment">//提价的路径</span>
            <span class="hljs-attr">type</span>: <span class="hljs-string">"post"</span>,       <span class="hljs-comment">//提交方式</span>
            <span class="hljs-attr">data</span>: &#123;
                <span class="hljs-comment">//向后台提交的数据</span>
            &#125;,
            <span class="hljs-attr">dataType</span>: <span class="hljs-string">"JSON"</span>,       <span class="hljs-comment">//规定请求成功后返回的数据</span>
            <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">data</span>) </span>&#123;
                <span class="hljs-comment">//请求成功之后进入该方法，data为成功后返回的数据</span>
            &#125;,
            <span class="hljs-attr">error</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">errorMsg</span>) </span>&#123;
                <span class="hljs-comment">//请求失败之后进入该方法，errorMsg为失败后返回的错误信息</span>
            &#125;
        &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>总结：</strong> 以上两种方式如果不显示的指定post提交方式，则默认的提交方式为get方式提交。此外，ajax中的url也可以直接通过字符串拼接，然后向后台提交数据，这种方式为get方式提交。</p></div>  
</div>
            