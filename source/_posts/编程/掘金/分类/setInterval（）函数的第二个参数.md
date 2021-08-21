
---
title: 'setInterval（）函数的第二个参数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e67110b248441c1983d1da823c2f7e9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 02:25:00 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e67110b248441c1983d1da823c2f7e9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">setInterval定时器函数的第二个参数为变量</h1>
<p>当第二个参数为变量的时候，变量改变了，但是我发现执行的等待时间并没有什么变化，还是等待原本第一次设置的时长，于是我就写了几句代码测试了一下。发现了确实是这样子，好像是setInterval()函数一旦启动这个设置的时间就是固定了，不会再改变。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 初始等待时间</span>
<span class="hljs-keyword">let</span> waitDate = <span class="hljs-number">1000</span>;

<span class="hljs-comment">// 成长的小明</span>
<span class="hljs-keyword">const</span> GrowingPeople = &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'小明'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">14</span>, <span class="hljs-attr">sex</span>: <span class="hljs-string">'男'</span>&#125;;

<span class="hljs-comment">// 年纪增长函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ageIncrease</span>(<span class="hljs-params">people</span>) </span>&#123;
    <span class="hljs-keyword">const</span> &#123; age &#125; = people;
    <span class="hljs-keyword">if</span>(age && age >= <span class="hljs-number">18</span>)&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
        people.age = people.age + <span class="hljs-number">1</span>;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    &#125;;
&#125;

<span class="hljs-comment">// 提示成年函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">promptAdulthood</span>(<span class="hljs-params">people</span>) </span>&#123;
    <span class="hljs-keyword">const</span> &#123; name=<span class="hljs-string">'小刚'</span>, age=<span class="hljs-number">15</span>, sex=<span class="hljs-string">'女'</span> &#125; = people;
    <span class="hljs-keyword">const</span> information = <span class="hljs-string">`我叫<span class="hljs-subst">$&#123;name&#125;</span>,是个<span class="hljs-subst">$&#123;sex&#125;</span>生, 今年<span class="hljs-subst">$&#123;age&#125;</span>岁啦，
        成年啦，可以去上网啦
    `</span>;
    <span class="hljs-built_in">console</span>.log(information);
&#125;

<span class="hljs-comment">// 版本1，发现设置的时间不生效</span>
 <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">simplePoller</span>(<span class="hljs-params">queryFn, callback</span>) </span>&#123;
     <span class="hljs-keyword">const</span> stop = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
     <span class="hljs-keyword">const</span> res = queryFn(GrowingPeople);
         <span class="hljs-keyword">if</span>(res)&#123;
             callback(GrowingPeople);
             <span class="hljs-built_in">clearInterval</span>(stop);
         &#125; <span class="hljs-keyword">else</span> &#123;
             <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`我才<span class="hljs-subst">$&#123;GrowingPeople.age&#125;</span>岁，还没有成年`</span>);
         &#125;
     &#125;, waitDate * <span class="hljs-number">1.5</span>);
 &#125;
 simplePoller(ageIncrease, promptAdulthood);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>本来是想每执行一次，下次执行时间是上次执行时间的1.5倍，但是开始以后每次执行时间都是1秒，我觉得应该是setInterval()在初始化的时候就固定了这个执行时间，不管你这个变量之后怎么变化，它还是按初始化的时候给的值去定时执行，所以想要改变这个定时的时间，这个方式就不太合适了，换一种方式，改递归调用吧。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 初始等待时间</span>
<span class="hljs-keyword">let</span> waitDate = <span class="hljs-number">1000</span>;

<span class="hljs-comment">// 成长的小明</span>
<span class="hljs-keyword">const</span> GrowingPeople = &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'小明'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">14</span>, <span class="hljs-attr">sex</span>: <span class="hljs-string">'男'</span>&#125;;

<span class="hljs-comment">// 年纪增长函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ageIncrease</span>(<span class="hljs-params">people</span>) </span>&#123;
    <span class="hljs-keyword">const</span> &#123; age &#125; = people;
    <span class="hljs-keyword">if</span>(age && age >= <span class="hljs-number">18</span>)&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
        people.age = people.age + <span class="hljs-number">1</span>;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    &#125;;
&#125;

<span class="hljs-comment">// 提示成年函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">promptAdulthood</span>(<span class="hljs-params">people</span>) </span>&#123;
    <span class="hljs-keyword">const</span> &#123; name=<span class="hljs-string">'小刚'</span>, age=<span class="hljs-number">15</span>, sex=<span class="hljs-string">'女'</span> &#125; = people;
    <span class="hljs-keyword">const</span> information = <span class="hljs-string">`我叫<span class="hljs-subst">$&#123;name&#125;</span>,是个<span class="hljs-subst">$&#123;sex&#125;</span>生, 今年<span class="hljs-subst">$&#123;age&#125;</span>岁啦，
        成年啦，可以去上网啦
    `</span>;
    <span class="hljs-built_in">console</span>.log(information);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">simplePoller</span>(<span class="hljs-params">queryFn, callback, waitDate</span>) </span>&#123;
    <span class="hljs-keyword">const</span> stop = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> res = queryFn(GrowingPeople);
        <span class="hljs-keyword">if</span>(res)&#123;
            <span class="hljs-built_in">clearInterval</span>(stop);
            callback(GrowingPeople);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">clearInterval</span>(stop);
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`下一次询问等待时间，<span class="hljs-subst">$&#123;waitDate&#125;</span>`</span>);
            simplePoller(queryFn, callback, waitDate*<span class="hljs-number">1.5</span>)
        &#125;
    &#125;, waitDate);
&#125;

simplePoller(ageIncrease, promptAdulthood, waitDate);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的写法确实实现了每次等待时间，按1.5倍增加了，但是这每次函数执行都会新建一个定时器，然后再把它销毁，感觉是在浪费性能，既然setInterval()函数第二个参数既然不能使用改变的值，那么使用它的意义也不大了。还不如使用递归和setTimeout()。这样也不用每次去清除定时器了</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">simplePoller</span>(<span class="hljs-params">queryFn, callback, waitDate</span>) </span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">const</span> res = queryFn(GrowingPeople);
        <span class="hljs-keyword">if</span>(res)&#123;
            callback(GrowingPeople);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`下一次询问等待时间，<span class="hljs-subst">$&#123;waitDate&#125;</span>`</span>);
            simplePoller(queryFn, callback, waitDate*<span class="hljs-number">1.5</span>)
        &#125;
    &#125;, waitDate);
&#125;

simplePoller(ageIncrease, promptAdulthood, waitDate);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>附上最后一次执行打印记录。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e67110b248441c1983d1da823c2f7e9~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样看起来代码简洁多了，虽然没有从本质上解决setInterval函数参数设置变量的问题，但是换了一种思路，也是可以实现的。</p>
<p>目前还是个前端小菜鸡，没有找到setInterval这个函数的源码，希望有大佬看到可以帮忙看看，是不是我的写法有问题，有什么更好的办法，也可以留言，交流一下呀。</p></div>  
</div>
            