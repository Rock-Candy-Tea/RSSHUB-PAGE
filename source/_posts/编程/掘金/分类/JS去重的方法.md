
---
title: 'JS去重的方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7297'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 04:23:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=7297'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第5天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">1. 利用双重for循环去重</h2>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">//定义一个新数组，先存放不可能与arr重复的第一个元素</span>
<span class="hljs-keyword">let</span> newArr = [arr1[<span class="hljs-number">0</span>]]
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < arr.length; i++) &#123;
    <span class="hljs-comment">//设置标记flag</span>
    <span class="hljs-keyword">let</span> flag = <span class="hljs-literal">true</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < newArr.length; j++) &#123;
        <span class="hljs-comment">//如果两个相等，标记该i为false(重复),并退出该循环</span>
        <span class="hljs-keyword">if</span> (arr[i] == newArr[j]) &#123;
            flag = <span class="hljs-literal">false</span>
            <span class="hljs-keyword">break</span>
        &#125;
    &#125;
    <span class="hljs-comment">//第二个for遍历完成后，flag为true(无重复)加进新数组</span>
    <span class="hljs-keyword">if</span> (flag == <span class="hljs-literal">true</span>) &#123;
        newArr.push(arr[i])
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2.利用includes去重</h2>
<blockquote>
<p>includes() 存在该值返回true，反之false</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">let</span> newArr = []
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>, len = arr.length; i < len; i++) &#123;
    <span class="hljs-keyword">if</span> (!newArr.includes(arr[i])) &#123;
        newArr.push(arr[i]);
    &#125;
&#125;
<span class="hljs-built_in">console</span>.log(newArr)


<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3.利用数组的filter方法去重</h2>
<blockquote>
<p>原理：</p>
<p>filter() 使用指定的函数测试所有元素，并返回一个包含所有通过测试元素的新数组</p>
<p>indexof() 可返回某个指定的字符串值在字符串中首次出现的位置。如果没有检索到指定字符串，则返回-1</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">let</span> newArr = arr.filter(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> arr.indexOf(item) === index
&#125;)
<span class="hljs-built_in">console</span>.log(newArr)


<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4.利用ES6中的 Set 方法去重（最常用）</h2>
<blockquote>
<p>原理：</p>
<p>Set数据结构中所有元素都是</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">// new Set(arr) 得到一个去重的set对象</span>
<span class="hljs-comment">// 通过 [] + 展开运算符 变成数组格式</span>
<span class="hljs-built_in">console</span>.log([...new <span class="hljs-built_in">Set</span>(arr)])


<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">5.利用indexOf去重</h2>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">let</span> newArr = []
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
    <span class="hljs-comment">// 检索新数组中是否有重复元素，没有就push进新数组</span>
    <span class="hljs-keyword">if</span> (newArr.indexOf(arr[i]) === -<span class="hljs-number">1</span>)
        newArr.push(arr[i])
&#125;
<span class="hljs-built_in">console</span>.log(newArr)


<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">6.利用ES6中的 Map 方法去重</h2>
<blockquote>
<p>原理：</p>
<p>创建一个空Map数据结构，遍历需要去重的数组，把数组的每一个元素作为key存到Map中</p>
<p>由于Map中不会出现相同的key值，所以最终得到的就是去重后的结果</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">let</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>
<span class="hljs-keyword">let</span> newArr = []
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
    <span class="hljs-keyword">if</span> (map.has(arr[i])) &#123;
        map.set(arr[i], <span class="hljs-literal">true</span>)<span class="hljs-comment">// true 或 false都没影响</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
        map.set(arr[i], <span class="hljs-literal">false</span>);
        newArr.push(arr[i]);
    &#125;
&#125;
<span class="hljs-built_in">console</span>.log(newArr)


<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            