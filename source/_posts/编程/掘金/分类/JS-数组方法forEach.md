
---
title: 'JS-数组方法forEach'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8835'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 22:59:57 GMT
thumbnail: 'https://picsum.photos/400/300?random=8835'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">重要数组的方法有哪些</h2>
<ol>
<li>forEach：用于遍历数组，没有返回值，可以对遍历出的数组项进行后续操作</li>
<li>filter：用于遍历数组，且筛选出符合条件的数组项，可以对筛选出的数组项进行后续操作</li>
<li>every：需要在回调函数中使用return true/false来返回单圈的执行，当所有都true才返回最终的true，否则返回false</li>
<li>some：和every差不多的原理和使用，最终返回布尔值，只要有一次循环为true，则true</li>
<li>reduce：（后续添加）</li>
</ol>
<blockquote>
<p>本篇章主要对forEach进行解析，一个例子，一个手写myForEach</p>
</blockquote>
<blockquote>
<p>本篇章不对其他函数做笔记，手写方式大同小异，reduce有所区别，后续补充</p>
</blockquote>
<h2 data-id="heading-1">forEach</h2>
<h3 data-id="heading-2">一、使用说明</h3>
<blockquote>
<p>在目标数组arr遍历出数组的每一项currentValue，在回调函数中操作数组项等</p>
</blockquote>
<p>格式：
目标数组.forEach(function(currentValue, index, arr) &#123;</p>
<p>&#125;,thisValue)</p>
<p>参数：</p>
<pre><code class="copyable">currentValue：数组项

index：数组下标

arr：目标数组本身

thisValue：this指向的目标，不填则指向window
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">二、例子</h3>
<p>将arr数组的name用无序列表方式呈现到页面中</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr = [
    &#123;<span class="hljs-string">"id"</span>:<span class="hljs-number">1</span>,<span class="hljs-string">"name"</span>:<span class="hljs-string">"zanshan"</span>,<span class="hljs-string">"sex"</span>:<span class="hljs-string">"m"</span>&#125;,
    &#123;<span class="hljs-string">"id"</span>:<span class="hljs-number">2</span>,<span class="hljs-string">"name"</span>:<span class="hljs-string">"lisi"</span>,<span class="hljs-string">"sex"</span>:<span class="hljs-string">"w"</span>&#125;,
    &#123;<span class="hljs-string">"id"</span>:<span class="hljs-number">3</span>,<span class="hljs-string">"name"</span>:<span class="hljs-string">"wangwu"</span>,<span class="hljs-string">"sex"</span>:<span class="hljs-string">"m"</span>&#125;,
]
arr.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">ele,index,taget</span>) </span>&#123;
    <span class="hljs-comment">//console.log(ele,index,taget,this)</span>
    <span class="hljs-built_in">this</span>[index].innerHTML = ele.name
&#125;,<span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">"li"</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例子说明：
第二个参数的传入使得this的指向document.getElementsByTagName("li")，所以可以直接操作this来操作dom树，在li标签中添加名字。</p>
<h3 data-id="heading-4">三、手写MyForEach</h3>
<p>先附代码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr = [
    &#123;<span class="hljs-string">"id"</span>:<span class="hljs-number">1</span>,<span class="hljs-string">"name"</span>:<span class="hljs-string">"zanshan"</span>,<span class="hljs-string">"sex"</span>:<span class="hljs-string">"m"</span>&#125;,
    &#123;<span class="hljs-string">"id"</span>:<span class="hljs-number">2</span>,<span class="hljs-string">"name"</span>:<span class="hljs-string">"lisi"</span>,<span class="hljs-string">"sex"</span>:<span class="hljs-string">"w"</span>&#125;,
    &#123;<span class="hljs-string">"id"</span>:<span class="hljs-number">3</span>,<span class="hljs-string">"name"</span>:<span class="hljs-string">"wangwu"</span>,<span class="hljs-string">"sex"</span>:<span class="hljs-string">"m"</span>&#125;,
]
<span class="hljs-comment">//MyForEach内容</span>
<span class="hljs-built_in">Array</span>.prototype.MyForEach = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">fun</span>)</span>&#123;
    <span class="hljs-keyword">let</span> _arr = <span class="hljs-built_in">this</span>,length = _arr.length,pram2 = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">1</span>]||<span class="hljs-built_in">window</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;i<length;i++)&#123;
        fun.call(pram2,_arr[i],i,_arr)
    &#125;
&#125;
<span class="hljs-comment">//测试MyForEach和forEach是否功能上一致</span>
arr.MyForEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">ele,index,taget</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(ele,index,taget,<span class="hljs-built_in">this</span>)
    <span class="hljs-built_in">this</span>[index].innerHTML = ele.name
&#125;,<span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">"li"</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意</strong>：
测试MyForEach使用箭头函数，第二个参数就失效了</p>
<p><strong>手写原理</strong></p>
<pre><code class="copyable">1. 需要将taget指代对象arr，所以在API实现内部将this传给回调函数fun的第三个参数（由于此处使用到了call，所以表现为第四个参数），通过_arr=this，后将_arr传递进fun
2. 通过_arr.length获取到循环的总次数
3. call改变了调用fun方法的this指向，如果不传递MyForEach的第二个参数，则默认是window在调用fun函数，在API使用时，打印this，this就是window；如果传递MyForEach的第二个参数，在API使用时，打印this，this就是MyForEach的第二个参数，通过操作this，来操作dom
4. 对上面的两个this进行说明，一个是指向arr的，一个是fun的调用者，两者有啥区别：前者的this环境是MyForEach函数刚进去，遵循谁调用则指向谁，因此测试MyForEach时，arr.MyForEach就象征着this指向了MyForEach；后者this环境是fun函数的。以上即使区别
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            