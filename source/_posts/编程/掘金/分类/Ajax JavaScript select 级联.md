
---
title: 'Ajax JavaScript select 级联'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5621'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 01:27:31 GMT
thumbnail: 'https://picsum.photos/400/300?random=5621'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、创建Ajax</h1>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> req = <span class="hljs-keyword">new</span> XMLHttpRequest();
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">二、发送请求</h1>
<pre><code class="hljs language-javascript copyable" lang="javascript"> req.open(<span class="hljs-string">'POST'</span>,<span class="hljs-string">'asses/test/city.json'</span>,<span class="hljs-literal">false</span>);<span class="hljs-comment">//发送请求</span>
 req.send();<span class="hljs-comment">//将请求发送到服务器上</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>open(method，ul，async)有三个参数；
1、请求类型：GET和POST。
2、请求文件的地址。
3、true（异步）或 false（同步）</p>
<h1 data-id="heading-2">三、请求得到响应返回数据</h1>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (req.readyState === <span class="hljs-number">4</span> && req.status === <span class="hljs-number">200</span>)&#123;
        <span class="hljs-keyword">let</span> tes = <span class="hljs-built_in">JSON</span>.parse(req.responseText);<span class="hljs-comment">//处理返回的数据</span>
        <span class="hljs-built_in">console</span>.log(tes);
    &#125;<span class="hljs-keyword">else</span> &#123;
        <span class="hljs-built_in">document</span>.write(<span class="hljs-string">'错误'</span>);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1、responseText:获得字符串形式的相应数据。
2、responsXML:获得XML形式的相应数据。
3、status：以数字和文本形式返回http状态码。
（1）200：成功。
（2）404：页面未找到。
4、readyState属性：响应返回成功的时候得到通知。
（1）0：请求未初始化，open还没有调用。
（2）1：服务器连接已建立，open已经调用了。
（3）2：请求已经接收，也就是接收到头信息了。
（4）3：请求处理中，也就是接收到响应主体了。
（5）4：请求已完成，且响应已就绪，也就是响应完成了。</p>
<h1 data-id="heading-3">四、jQuery方法</h1>
<pre><code class="hljs language-javascript copyable" lang="javascript">$.ajax(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'post'</span>,<span class="hljs-comment">//请求类型</span>
        <span class="hljs-attr">url</span>: <span class="hljs-string">'asses/test/city.json'</span>,<span class="hljs-comment">//文件地址</span>
        <span class="hljs-attr">async</span>: <span class="hljs-literal">false</span>,<span class="hljs-comment">//异步（同步）</span>
        <span class="hljs-attr">dataType</span>: <span class="hljs-string">'json'</span>,<span class="hljs-comment">//文件类型（json）</span>
        <span class="hljs-attr">success</span>:<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;<span class="hljs-comment">//成功执行函数</span>
            data = value;
        &#125;,
        <span class="hljs-attr">error</span>:<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;<span class="hljs-comment">//失败执行函数</span>
            <span class="hljs-built_in">console</span>.error(e);
        &#125;
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很方便，代码简单，但还是支持写原生的。</p>
<p><strong>html</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 610px;margin: 20px auto;"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"margin-bottom: 10px;"</span>></span><span class="hljs-tag"><<span class="hljs-name">h3</span>></span>选择所在地<span class="hljs-tag"></<span class="hljs-name">h3</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">select</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"capital"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">option</span>></span>请选择省会<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">select</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">select</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"cit"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">option</span>></span>请先选择省会<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">select</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">select</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"county"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">option</span>></span>请先选择区县<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">select</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>js</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> capital = $(<span class="hljs-string">'#capital'</span>);
    <span class="hljs-keyword">let</span> cit = $(<span class="hljs-string">'#cit'</span>);
    <span class="hljs-keyword">let</span> county = $(<span class="hljs-string">'#county'</span>);
    <span class="hljs-keyword">let</span> data = [];
    <span class="hljs-keyword">let</span> arr;
    
    <span class="hljs-comment">// 原生js创建Ajax请求</span>
    <span class="hljs-comment">/*let req = new XMLHttpRequest();//创建Ajax对象
    req.open('POST','asses/test/city.json',false);//发送请求
    req.send();//将请求发送到服务器上
    if (req.readyState === 4 && req.status === 200)&#123;
        let tes = JSON.parse(req.responseText);//处理返回的数据
        console.log(tes);
    &#125;else &#123;
        document.write('错误');
    &#125;*/</span>

    <span class="hljs-comment">// jQuery创建Ajax请求</span>
    $.ajax(&#123;
        <span class="hljs-attr">type</span>: <span class="hljs-string">'post'</span>,
        <span class="hljs-attr">url</span>: <span class="hljs-string">'asses/test/city.json'</span>,
        <span class="hljs-attr">async</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">dataType</span>: <span class="hljs-string">'json'</span>,
        <span class="hljs-attr">success</span>:<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
            data = value;
        &#125;,
        <span class="hljs-attr">error</span>:<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
            <span class="hljs-built_in">console</span>.error(e);
        &#125;
    &#125;);

    <span class="hljs-comment">//生成第一个select的option</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<=data.length-<span class="hljs-number">1</span>;i++)&#123;
        <span class="hljs-keyword">let</span> op = $(<span class="hljs-string">'<option value="'</span> + i + <span class="hljs-string">'">'</span> + data[i].name + <span class="hljs-string">'</option>'</span>);
        capital.append(op);
    &#125;
    <span class="hljs-comment">//根据第一个点击来生成第二个select的option</span>
    capital.change(<span class="hljs-function">() =></span>&#123;<span class="hljs-comment">//省会改变</span>
        cit.empty();<span class="hljs-comment">//清空cit的option</span>
        county.empty();<span class="hljs-comment">//清空county的option</span>
        <span class="hljs-keyword">if</span> (capital.val() == <span class="hljs-string">'请选择省会'</span>)&#123;
            <span class="hljs-keyword">let</span> op = $(<span class="hljs-string">'<option>请先选择省会</option>'</span>);
            <span class="hljs-keyword">let</span> op2 = $(<span class="hljs-string">'<option>请先选择城市</option>'</span>);
            cit.append(op);
            county.append(op2);
        &#125;<span class="hljs-keyword">else</span> &#123;
            arr = data[capital.val()].city;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<=arr.length-<span class="hljs-number">1</span>;i++)&#123;
                <span class="hljs-keyword">let</span> op = $(<span class="hljs-string">'<option value="'</span> + i + <span class="hljs-string">'">'</span> + arr[i].name + <span class="hljs-string">'</option>'</span>);
                cit.append(op);
            &#125;
            <span class="hljs-keyword">let</span> b = arr[cit.val()].area;
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<=b.length-<span class="hljs-number">1</span>;i++)&#123;
                <span class="hljs-keyword">let</span> op = $(<span class="hljs-string">'<option value="'</span> + i + <span class="hljs-string">'">'</span> + b[i] + <span class="hljs-string">'</option>'</span>);
                county.append(op);
            &#125;
        &#125;
    &#125;);
    <span class="hljs-comment">//根据第二个点击来生成第三个select的option</span>
    cit.change(<span class="hljs-function">() =></span>&#123;<span class="hljs-comment">//城市改变</span>
        county.empty();
        <span class="hljs-keyword">let</span> b = arr[cit.val()].area;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<=b.length-<span class="hljs-number">1</span>;i++)&#123;
            <span class="hljs-keyword">let</span> op = $(<span class="hljs-string">'<option value="'</span> + i + <span class="hljs-string">'">'</span> + b[i] + <span class="hljs-string">'</option>'</span>);
            county.append(op);
        &#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是我在学习js的时候做的一些小练习，我把它分享给大家，谢谢！</p></div>  
</div>
            