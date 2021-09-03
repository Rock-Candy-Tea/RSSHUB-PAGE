
---
title: 'js数据结构之有序栈'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4931'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 22:46:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=4931'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><strong>栈</strong>是一种比较常见的数据结构，虽然在js中没有原生的栈，但是实现起来也并不复杂，主要就是<code>push</code>，<code>pop</code>，<code>top</code>几个函数的实现。我这里说到的<strong>有序栈</strong>就是一种元素按照一定顺序排列的<strong>栈</strong>。主要的应用场景有：<em>求数组中最小的K个数</em>等。</p>
</blockquote>
<p>有序栈的类实现方式</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Stack</span></span>&#123;
    <span class="hljs-comment">/**
     * 构造函数，s用来存储数据，count用来记录栈的大小
     */</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.s = [];
        <span class="hljs-built_in">this</span>.count = <span class="hljs-number">0</span>;
    &#125;

    <span class="hljs-comment">/**
     * 栈的push函数，往栈中添加数据
     * <span class="hljs-doctag">@param </span>num 需要存储到栈中的数据
     */</span>
    <span class="hljs-function"><span class="hljs-title">push</span>(<span class="hljs-params">num</span>)</span> &#123;
        <span class="hljs-comment">// 如果数据为空，不做操作</span>
        <span class="hljs-keyword">if</span>(!num) <span class="hljs-keyword">return</span>;
        <span class="hljs-comment">// 找到栈中大于num的数的下标</span>
        <span class="hljs-keyword">const</span> index = <span class="hljs-built_in">this</span>.s.findIndex(<span class="hljs-function">(<span class="hljs-params">value, index</span>) =></span> value > num);
        <span class="hljs-comment">// 如果没有找到，说明栈中的元素都会小于num，直接添加到数组的最后面</span>
        <span class="hljs-keyword">if</span>(index === -<span class="hljs-number">1</span>) <span class="hljs-built_in">this</span>.s.push(num);
        <span class="hljs-keyword">else</span>&#123;
            <span class="hljs-comment">// 否则，插入第一个会大于num的元素位置</span>
            <span class="hljs-built_in">this</span>.s.splice(index, <span class="hljs-number">0</span>, num);
        &#125;
        <span class="hljs-comment">// 栈大小增加1</span>
        ++<span class="hljs-built_in">this</span>.count;
    &#125;

    <span class="hljs-comment">/**
     * 栈弹出元素，数组按从小到大排序的，直接把最大的元素弹出
     */</span>
    <span class="hljs-function"><span class="hljs-title">pop</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.s.pop();
        --<span class="hljs-built_in">this</span>.count;
    &#125;

    <span class="hljs-comment">/**
     * 返回栈顶元素
     * <span class="hljs-doctag">@returns </span>数组中最大的元素
     */</span>
    <span class="hljs-function"><span class="hljs-title">top</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.count >= <span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.s[<span class="hljs-built_in">this</span>.count-<span class="hljs-number">1</span>];
        <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span>;
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">kMin</span>(<span class="hljs-params">arr, k</span>)</span>&#123;
    <span class="hljs-keyword">const</span> st = <span class="hljs-keyword">new</span> Stack();
    arr.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
        <span class="hljs-comment">// 如果栈的元素个数小于k，直接将数据添加到栈中</span>
        <span class="hljs-keyword">if</span>(st.count < k)&#123;
            st.push(item);
        &#125;<span class="hljs-keyword">else</span>&#123;
            <span class="hljs-comment">// 否则的话，如果元素小于栈顶元素，则将栈顶元素弹出，并将数据添加到栈中</span>
            <span class="hljs-keyword">if</span>(item < st.top())&#123;
                st.pop();
                st.push(item);
            &#125;
        &#125;
    &#125;)
    <span class="hljs-keyword">return</span> st.s;
&#125;

kMin([<span class="hljs-number">7</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">8</span>,<span class="hljs-number">10</span>,<span class="hljs-number">30</span>], <span class="hljs-number">2</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在函数式编程比较流行，这里再给出函数式的实现方式。明显可以看出，函数式的实现方式更加简洁明了，对外暴露的变量和函数都通过return的方式。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fStack</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">const</span> arr = [];

    <span class="hljs-keyword">const</span> count = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">return</span> arr.length;
    &#125;

    <span class="hljs-keyword">const</span> push = <span class="hljs-function">(<span class="hljs-params">num</span>) =></span> &#123;
        <span class="hljs-comment">// 如果数据为空，不做操作</span>
        <span class="hljs-keyword">if</span>(!num) <span class="hljs-keyword">return</span>;
        <span class="hljs-comment">// 找到栈中大于num的数的下标</span>
        <span class="hljs-keyword">const</span> index = arr.findIndex(<span class="hljs-function">(<span class="hljs-params">value, index</span>) =></span> value > num);
        <span class="hljs-comment">// 如果没有找到，说明栈中的元素都会小于num，直接添加到数组的最后面</span>
        <span class="hljs-keyword">if</span>(index === -<span class="hljs-number">1</span>) arr.push(num);
        <span class="hljs-keyword">else</span>&#123;
            <span class="hljs-comment">// 否则，插入第一个会大于num的元素位置</span>
            arr.splice(index, <span class="hljs-number">0</span>, num);
        &#125;
    &#125;

    <span class="hljs-keyword">const</span> pop = <span class="hljs-function">() =></span> &#123;
        arr.pop();
    &#125;

    <span class="hljs-keyword">const</span> top = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-keyword">if</span>(count >= <span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> arr[count-<span class="hljs-number">1</span>];
        <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span>;
    &#125;

    <span class="hljs-keyword">return</span> &#123;
        arr,
        count,
        push,
        pop,
        top
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">kMin</span>(<span class="hljs-params">arr, k</span>)</span>&#123;
    <span class="hljs-keyword">const</span> st = <span class="hljs-keyword">new</span> fStack();
    arr.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
        <span class="hljs-comment">// 如果栈的元素个数小于k，直接将数据添加到栈中</span>
        <span class="hljs-keyword">if</span>(st.count() < k)&#123;
            st.push(item);
        &#125;<span class="hljs-keyword">else</span>&#123;
            <span class="hljs-comment">// 否则的话，如果元素小于栈顶元素，则将栈顶元素弹出，并将数据添加到栈中</span>
            <span class="hljs-keyword">if</span>(item < st.top())&#123;
                st.pop();
                st.push(item);
            &#125;
        &#125;
    &#125;)
    <span class="hljs-keyword">return</span> st.arr;
&#125;

<span class="hljs-keyword">const</span> res = kMin([<span class="hljs-number">7</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">8</span>,<span class="hljs-number">10</span>,<span class="hljs-number">30</span>], <span class="hljs-number">2</span>)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            