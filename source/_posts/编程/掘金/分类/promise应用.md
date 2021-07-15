
---
title: 'promise应用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1897'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 02:08:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=1897'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">promise</h1>
<h2 data-id="heading-1">一.异步出现原因</h2>
<p>js是单线程的，一次只能做一件事，所有的任务都需要排队，如果任务执行事件过长会十分影响用户体验，所以js在同步机制的缺陷下设计出了异步模式</p>
<h2 data-id="heading-2">二.异步的缺陷=>回调地狱</h2>
<p>为了拿到异步任务的结果，我们不得不大量使用回调函数，导致代码看起来很混乱，甚至出现回调地狱</p>
<pre><code class="hljs language-python copyable" lang="python">函数<span class="hljs-number">1</span>(function()&#123;
   //代码执行...(ajax1)
   
   函数<span class="hljs-number">2</span>(function()&#123;
       //代码执行...(ajax2)
       
       函数<span class="hljs-number">3</span>(function(data3)&#123;
             //代码执行...(ajax3)
       &#125;);
       ...
   &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">三、回调地狱的解决方案=》promise</h2>
<p>Promise对象代表一个异步操作，有三种状态<br>
pending（等待）、resolved（成功状态）、rejected（失败状态）
两种状态改变方式：pending => resolved，pending => rejected</p>
<h3 data-id="heading-4">1、promise.then链式操作用法</h3>
<pre><code class="hljs language-python copyable" lang="python">        let getToken = function () &#123;
            <span class="hljs-keyword">return</span> new Promise((resolve, reject) => &#123;
                resolve(<span class="hljs-string">'token'</span>)
            &#125;)
        &#125;

        let getName = function (token) &#123;
            <span class="hljs-keyword">return</span> new Promise((resolve, reject) => &#123;
                    resolve(<span class="hljs-string">'小明'</span>)
            &#125;)
        &#125;
        let getAge = function (name) &#123;
            <span class="hljs-keyword">return</span> new Promise((resolve, reject) => &#123;
                <span class="hljs-keyword">if</span> (name) &#123;
                    resolve(<span class="hljs-string">'60'</span>)
                &#125;
            &#125;)
        &#125;
        getToken().then(res => &#123;
            console.log(res)
            <span class="hljs-keyword">return</span> getName(res)

        &#125;).then(res => &#123;
            console.log(res)
            <span class="hljs-keyword">return</span> getAge()
        &#125;).then(res => &#123;
            console.log(res)
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2、reject用法，当异步操作失败时reject可以把promise的状态设置为rejected</h3>
<pre><code class="hljs language-python copyable" lang="python">        let getAge = function (name) &#123;
            <span class="hljs-keyword">return</span> new Promise((resolve, reject) => &#123;
                <span class="hljs-keyword">if</span> (name) &#123;
                    resolve(<span class="hljs-string">'60'</span>)
                &#125;
                reject(<span class="hljs-string">'name=>err'</span>)
            &#125;)
        &#125;   
        getAge().then(res=>&#123;
            console.log(res,<span class="hljs-string">'res'</span>)
        &#125;,err=>&#123;
            console.log(err,<span class="hljs-string">'err'</span>)
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">3、catch用于指定发生错误的回调函数</h3>
<pre><code class="hljs language-python copyable" lang="python">        let getAge = function (name) &#123;
            <span class="hljs-keyword">return</span> new Promise((resolve, reject) => &#123;
                <span class="hljs-keyword">if</span> (name) &#123;
                    resolve(<span class="hljs-string">'60'</span>)
                &#125;
                reject(<span class="hljs-string">'name=>err'</span>)
            &#125;)
        &#125;   
        getAge().then(res=>&#123;
            console.log(res,<span class="hljs-string">'res'</span>)
        &#125;).catch(err=>&#123;
             console.error(err,<span class="hljs-string">'err'</span>)
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">4、Promise.all(),将多个promise实例包装为一个新的promise实例，返回全部结果</h3>
<pre><code class="hljs language-python copyable" lang="python">       Promise.<span class="hljs-built_in">all</span>([getToken(),getName(),getAge()]).then(res=>&#123;
            console.log(res)
        &#125;).catch(err=>&#123;
            console.error(err,<span class="hljs-string">'err'</span>)
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">5、Promise.race(),同样是将多个promise实例包装为一个新的promise实例,区别是传入的promise哪个结果获取的快，就返回哪个，不管是成功还是失败</h3>
<pre><code class="hljs language-python copyable" lang="python">        Promise.race([getToken(), getName(<span class="hljs-string">'token'</span>), getAge(<span class="hljs-string">'token'</span>)]).then(res => &#123;
            console.log(res)
        &#125;).catch(err => &#123;
            console.error(err, <span class="hljs-string">'err'</span>)
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">四、Promise封装接口请求</h2>
<pre><code class="hljs language-python copyable" lang="python">        const $http = (url, data, method) => &#123;
            method = method.toUpperCase();
            const config = &#123;
                method, url
            &#125;
            <span class="hljs-keyword">if</span> ([<span class="hljs-string">'GET'</span>, <span class="hljs-string">'DELETE'</span>].includes(method)) &#123; config.params = data &#125;
            <span class="hljs-keyword">else</span> &#123; config.data = Qs.stringify(data) &#125;
            <span class="hljs-keyword">return</span> new Promise((resolve, reject) => &#123;
                axios(config).then(response => &#123;
                    let code = response.data.code
                    <span class="hljs-keyword">if</span> (code == <span class="hljs-number">200</span>) &#123;
                        resolve(response.data)
                    &#125;<span class="hljs-keyword">else</span>&#123;
                        reject(response.data)
                    &#125;
                &#125;).catch(err => &#123;
                    reject(err)
                &#125;)
            &#125;)
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            