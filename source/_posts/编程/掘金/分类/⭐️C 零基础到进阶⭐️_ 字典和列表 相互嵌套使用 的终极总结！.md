
---
title: '⭐️C# 零基础到进阶⭐️_ 字典和列表 相互嵌套使用 的终极总结！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f705e3086b9469b96c8822b3856cb8f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 02:45:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f705e3086b9469b96c8822b3856cb8f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,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")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第6天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">字典和列表 相互嵌套)</h1>
<h4 data-id="heading-1">📢前言</h4>
<ul>
<li>最近因为工作需求需要用到列表和字典嵌套使用来达成效果</li>
<li>好久不用都有点忘记咋用了，所以就去搜了搜</li>
<li>发现是有文章介绍嵌套使用，但是很零散、不齐全</li>
<li>然后我就写了一篇，自己写代码实例尝试了一下，差不多将<strong>字典</strong>和<strong>列表</strong>相互嵌套的几种方法都写出来了</li>
<li>一起来搞懂<strong>字典</strong>和<strong>列表</strong>的<strong>相互嵌套</strong>具体怎样使用吧！</li>
</ul>
<hr>
<h2 data-id="heading-2">🏳️‍🌈字典</h2>
<p>字典的含义：
字典中key只能对应一个值不能对应多个值，线性结构。</p>
<ol>
<li>实例化：Dictionary<键key,值value> 名字dic=new Dictionary<键key,值value>（）;</li>
</ol>
<pre><code class="hljs language-csharp copyable" lang="csharp">Dictionary<<span class="hljs-built_in">string</span>,<span class="hljs-built_in">string</span>> Dic=<span class="hljs-keyword">new</span> Dictionary<<span class="hljs-built_in">string</span>,<span class="hljs-built_in">string</span>>();<span class="hljs-comment">//普通创建实例化</span>

Dictionary<<span class="hljs-built_in">string</span>,<span class="hljs-built_in">string</span>> Dic1 = <span class="hljs-keyword">new</span> Dictionary<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">string</span>> &#123; &#123; <span class="hljs-string">"a"</span>, <span class="hljs-string">"1"</span> &#125;, &#123; <span class="hljs-string">"b"</span>, <span class="hljs-string">"2"</span> &#125;, &#125;;<span class="hljs-comment">//直接创建实例化并赋值</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>常见方法：</li>
</ol>
<p>添加：Dic.Add（key，value）给字典添加值
删除：Dic.Remove(key)  删除指定值
访问：Dictionary[key]表示key所对应的值
判断空：ContainsKey(key)判断key是否存在
3. 遍历字典方法：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp">        Dictionary<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">string</span>> d = <span class="hljs-keyword">new</span> Dictionary<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">string</span>>();
        
        <span class="hljs-keyword">foreach</span> (<span class="hljs-keyword">var</span> item <span class="hljs-keyword">in</span> d)
        &#123;
            Console.WriteLine(item.Key+item.Value);<span class="hljs-comment">//遍历打印链表中的值   </span>
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-3">字典嵌套字典</h3>
<ul>
<li>字典嵌套字典，在创建字典的时候，将里面一层再写一个字典，就完成字典嵌套了，里面的字典就相当于外层字典的Value值</li>
<li>在实例化的时候只是实例化了外层的字典，在给外层字典赋值的时候，需要将内层嵌套的字典再进行实例化</li>
<li>然后拿到外层字典的key之后，再给内层的字典赋值Key和Value</li>
<li>遍历的时候，双层循环，先遍历外层字典，然后在遍历外层字典的Value(也就是内层字典)</li>
</ul>
<pre><code class="hljs language-csharp copyable" lang="csharp"> Dictionary<<span class="hljs-built_in">string</span>, Dictionary<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">string</span>>> Dic1;

        Dic1 = <span class="hljs-keyword">new</span> Dictionary<<span class="hljs-built_in">string</span>, Dictionary<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">string</span>>>();
        <span class="hljs-comment">//方法一</span>
        Dic1.Add(<span class="hljs-string">"key"</span>,<span class="hljs-keyword">new</span> Dictionary<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">string</span>>());<span class="hljs-comment">//对应的内嵌字典需实例化</span>
        Dic1[<span class="hljs-string">"key"</span>].Add(<span class="hljs-string">"key"</span>, <span class="hljs-string">"value"</span>);<span class="hljs-comment">//添加外层值</span>
        
        <span class="hljs-comment">//方法二</span>
        Dic1[<span class="hljs-string">"key"</span>] = <span class="hljs-keyword">new</span> Dictionary<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">string</span>>();<span class="hljs-comment">//给外层的某个值赋值字典值</span>
        Dic1[<span class="hljs-string">"key"</span>].Add(<span class="hljs-string">"key1"</span>, <span class="hljs-string">"value"</span>);<span class="hljs-comment">//外层字典的key，赋值嵌套的字典值</span>

        Console.WriteLine(Dic1[<span class="hljs-string">"key"</span>][<span class="hljs-string">"key1"</span>]);<span class="hljs-comment">//读取嵌套字典里的某个值</span>
        <span class="hljs-comment">//打印结果：value</span>
        
        <span class="hljs-comment">//遍历嵌套字典</span>
        <span class="hljs-keyword">foreach</span> (<span class="hljs-keyword">var</span> item <span class="hljs-keyword">in</span> Dic1)
        &#123;
            Debug.Log(<span class="hljs-string">"外层字典："</span> + item);<span class="hljs-comment">//遍历打印外层字典中的值</span>
            <span class="hljs-keyword">foreach</span> (<span class="hljs-keyword">var</span> item1 <span class="hljs-keyword">in</span> item.Value)
            &#123;
                Console.WriteLine(<span class="hljs-string">"内层字典："</span> + item1);<span class="hljs-comment">//遍历外层字典的Value，来打印内层字典中的值  </span>
            &#125;
        &#125;
        <span class="hljs-comment">//打印结果：</span>
        <span class="hljs-comment">//外层字典：keySystem.Collections.Generic.Dictionary`2[System.String,System.String]</span>
        <span class="hljs-comment">//内层字典：[key1, value]</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">字典嵌套列表</h3>
<ul>
<li>字典嵌套列表跟上面的嵌套字典是一个道理</li>
<li>也是把外层字典的Value换成列表</li>
<li>然后实例化的时候也是如此，先实例化外层字典，在给字典赋值的时候在实例化列表元素</li>
<li>在遍历的时候与字典嵌套字典一模一样</li>
</ul>
<pre><code class="hljs language-csharp copyable" lang="csharp">        Dictionary<<span class="hljs-built_in">string</span>, List<<span class="hljs-built_in">string</span>>> Dic1;

        Dic1 = <span class="hljs-keyword">new</span> Dictionary<<span class="hljs-built_in">string</span>, List<<span class="hljs-built_in">string</span>>>();

        Dic1.Add(<span class="hljs-string">"key1"</span>, <span class="hljs-keyword">new</span> List<<span class="hljs-built_in">string</span>> &#123; <span class="hljs-string">"第一个"</span>, <span class="hljs-string">"第二个"</span>, <span class="hljs-string">"第三个"</span> &#125;);<span class="hljs-comment">//给字典和列表赋值</span>
        Dic1.Add(<span class="hljs-string">"key2"</span>, <span class="hljs-keyword">new</span> List<<span class="hljs-built_in">string</span>> &#123; <span class="hljs-string">"第四个"</span>, <span class="hljs-string">"第五个"</span>, <span class="hljs-string">"第六个"</span> &#125;);<span class="hljs-comment">//给字典和列表赋值</span>

        <span class="hljs-keyword">foreach</span> (<span class="hljs-keyword">var</span> item <span class="hljs-keyword">in</span> Dic1)
        &#123;
            Console.WriteLine(<span class="hljs-string">"字典："</span> + item.Key + item.Value);<span class="hljs-comment">//遍历打印字典中的值</span>
            <span class="hljs-keyword">foreach</span> (<span class="hljs-keyword">var</span> item1 <span class="hljs-keyword">in</span> item.Value)
            &#123;

                Console.WriteLine(<span class="hljs-string">"列表："</span>+item1);<span class="hljs-comment">//遍历打印链表中的值   </span>
            &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-5">🏳️‍🌈列表</h2>
<p>当我们有很多类型一样的数据时，可以使用数组来进行存储并管理，但是这样的缺点是数组的大小是提前给定的、是固定的。</p>
<ul>
<li>如果我们有许多类型一样但数量不定的数据，我们可以使用集合类来进行管理——例如列表List。我们可以使用列表List很方便的添加数据，删除数据以及其他的一些数据操作。</li>
</ul>
<ol>
<li>实例化的三种方法</li>
</ol>
<pre><code class="hljs language-csharp copyable" lang="csharp">方法<span class="hljs-number">1</span>：
List<<span class="hljs-built_in">int</span>> list = <span class="hljs-keyword">new</span> List<<span class="hljs-built_in">int</span>>();<span class="hljs-comment">//创建了一个空列表</span>
方法<span class="hljs-number">2</span>：
<span class="hljs-keyword">var</span> list = <span class="hljs-keyword">new</span> List<<span class="hljs-built_in">int</span>>();<span class="hljs-comment">//创建了一个空列表</span>
方法<span class="hljs-number">3</span>：创建并初始化赋值
<span class="hljs-keyword">var</span> list = <span class="hljs-keyword">new</span> List<<span class="hljs-built_in">int</span>> &#123;<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>&#125;;

两种遍历列表的方法
```csharp
List<<span class="hljs-built_in">int</span>> scoreList = <span class="hljs-keyword">new</span> List<<span class="hljs-built_in">int</span>>（）;
            <span class="hljs-comment">//第一种：依次获得list中的每一个元素，赋值给temp，并执行循环体</span>
            <span class="hljs-keyword">foreach</span> (<span class="hljs-built_in">string</span> s <span class="hljs-keyword">in</span> list)
            &#123;
                Console.WriteLine(s);<span class="hljs-comment">//遍历打印链表中的值</span>
                <span class="hljs-comment">//打印结果：链表2 链表3</span>
            &#125;
            
            <span class="hljs-comment">//第二种：遍历所有的索引，通过索引访问列表中的元素</span>
             <span class="hljs-keyword">for</span> (<span class="hljs-built_in">int</span> i = <span class="hljs-number">0</span>; i < list.Count; i++)
            &#123;
                Console.WriteLine(list[i]);<span class="hljs-comment">//遍历打印链表的值</span>
            &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>使用方法</li>
</ol>
<p>添加：list.Add(key)给字典添加值
删除：list.Remove(key)  删除指定值
访问：list[key]表示key所对应的值</p>
<ol start="3">
<li>列表的小知识</li>
</ol>
<p>①  列表内部数据其实是使用数组进行存储的。一个空的列表内部会有一个长度为0的数组。当对列表中添加元素时，列表的容量会扩大到4，如果添加第五个元素时，列表的大小就会重新扩大到8，以此类推。一次2倍的形式增加。
②  当列表的容量发生改变时，它会创建一个新的数组，使用Array.Copy()方法将就数组中的元素复制到新数组中。为了节省时间，如果事先知道所要存储的元素的个数，就可以利用列表的构造函数指定列表的容量大小</p>
<p>例如：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp">List<<span class="hljs-built_in">int</span>> intList = <span class="hljs-keyword">new</span> List<<span class="hljs-built_in">int</span>> (<span class="hljs-number">10</span>);
<span class="hljs-comment">//创建了一个容量为10的列表</span>
<span class="hljs-comment">//当容量不够时，每次都会按照原来的2倍进行容量的扩充</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以通过<strong>Capacity</strong>属性来获取和设置容量大小。</p>
<pre><code class="hljs language-csharp copyable" lang="csharp">intList.Capacity = <span class="hljs-number">100</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意<strong>容量</strong>和列表中的<strong>元素个数</strong>的区别。</p>
<p><strong>容量</strong>是列表中用于存储数据的数组的长度，通过<strong>Capacity</strong>进行获取。
而列表中的<strong>元素</strong>则是我们添加进去的、需要管理的数据，通过<strong>Count</strong>进行获取。</p>
<hr>
<h3 data-id="heading-6">列表嵌套列表</h3>
<ul>
<li>列表嵌套列表就相对好理解了，毕竟列表我们在添加的时候，只需要添加一个属性值</li>
<li>嵌套使用的话就是List<List>就好了，然后添加的时候把内层的列表当做一个值添加给外层列表</li>
<li>遍历的时候也是双层循环访问即可</li>
</ul>
<pre><code class="hljs language-csharp copyable" lang="csharp">        <span class="hljs-comment">//创建嵌套列表和普通列表</span>
        List<List<<span class="hljs-built_in">string</span>>> list1 = <span class="hljs-keyword">new</span> List<List<<span class="hljs-built_in">string</span>>>();
        List<<span class="hljs-built_in">string</span>> list2 = <span class="hljs-keyword">new</span> List<<span class="hljs-built_in">string</span>>();
        List<<span class="hljs-built_in">string</span>> list3 = <span class="hljs-keyword">new</span> List<<span class="hljs-built_in">string</span>>();
        <span class="hljs-comment">//普通链表赋值</span>
        list2.Add(<span class="hljs-string">"链表2"</span>);
        list3.Add(<span class="hljs-string">"链表3"</span>);
        <span class="hljs-comment">//嵌套链表赋值</span>
        list1.Add(list2);
        list1.Add(list3);
        <span class="hljs-comment">//遍历嵌套链表</span>
        <span class="hljs-keyword">foreach</span> (List<<span class="hljs-built_in">string</span>> i <span class="hljs-keyword">in</span> list1)
        &#123;
            <span class="hljs-keyword">foreach</span> (<span class="hljs-built_in">string</span> s <span class="hljs-keyword">in</span> i)
            &#123;
                Console.WriteLine(s);<span class="hljs-comment">//打印链表的值</span>
                <span class="hljs-comment">//打印结果：链表2 链表3</span>
            &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">列表嵌套字典</h3>
<ul>
<li>列表嵌套字典，就是把字典当做外层列表的一个属性值</li>
<li>然后将字典通过Add的方式添加给列表</li>
<li>遍历的时候，也是先遍历列表，然后在遍历字典就可以拿到数据了</li>
</ul>
<pre><code class="hljs language-csharp copyable" lang="csharp">        List<Dictionary<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">string</span>>> list1;<span class="hljs-comment">//创建嵌套字典的列表</span>
        Dictionary<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">string</span>> d;<span class="hljs-comment">//创建字典</span>

        d = <span class="hljs-keyword">new</span> Dictionary<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">string</span>>();<span class="hljs-comment">//实例化字典</span>
        list1 = <span class="hljs-keyword">new</span> List<Dictionary<<span class="hljs-built_in">string</span>, <span class="hljs-built_in">string</span>>>();<span class="hljs-comment">//实例化列表</span>

        list1.Add(d);<span class="hljs-comment">//将字典添加进列表，这种方式</span>

        d.Add(<span class="hljs-string">"key"</span>, <span class="hljs-string">"value"</span>);<span class="hljs-comment">//直接给字典赋值</span>

        list1[<span class="hljs-number">1</span>].Add(<span class="hljs-string">"key"</span>, <span class="hljs-string">"value"</span>);<span class="hljs-comment">//也可以通过列表给字典赋值</span>

        <span class="hljs-comment">//遍历嵌套字典</span>
        <span class="hljs-keyword">foreach</span> (<span class="hljs-keyword">var</span> item <span class="hljs-keyword">in</span> list1)
        &#123;
            <span class="hljs-keyword">foreach</span> (<span class="hljs-keyword">var</span> item1 <span class="hljs-keyword">in</span> item)
            &#123;
                Console.WriteLine(item1);<span class="hljs-comment">//打印字典的值</span>
            &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-8">👥总结</h2>
<p>字典和列表 相互嵌套使用 的几种方式，包括实例讲解，应该没有被绕晕吧，这只是介绍了双层嵌套使用</p>
<p>更多层的嵌套使用方法类似，就一直套用就好了，遍历的时候多次循环使用就好啦！</p>
<p>今天你学废了吗！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f705e3086b9469b96c8822b3856cb8f~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            