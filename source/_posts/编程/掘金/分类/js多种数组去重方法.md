
---
title: 'js多种数组去重方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4796'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 19:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4796'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>1.将数组的每一个元素依次与其他元素做比较，发现重复元素，删除</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">23</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-number">23</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">9</span>,<span class="hljs-number">9</span>,<span class="hljs-number">8</span>,<span class="hljs-number">5</span>,<span class="hljs-number">5</span>,<span class="hljs-number">5</span>,<span class="hljs-number">5</span>];
<span class="hljs-built_in">console</span>.log(arr);    <span class="hljs-comment">//[1, 23, 1, 1, 1, 3, 23, 5, 6, 7, 9, 9, 8, 5, 5, 5, 5]</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">noRepeat1</span>(<span class="hljs-params">arr</span>) </span>&#123;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < arr.length-<span class="hljs-number">1</span>; i++)&#123;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> j = i+<span class="hljs-number">1</span>; j < arr.length; j++)&#123;
            <span class="hljs-keyword">if</span>(arr[i]===arr[j])&#123;
                arr.splice(j,<span class="hljs-number">1</span>);
                j--;
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> arr;
&#125;
<span class="hljs-keyword">var</span> arr2 = noRepeat1(arr);
<span class="hljs-built_in">console</span>.log(arr2);    <span class="hljs-comment">//[1, 23, 3, 5, 6, 7, 9, 8]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.借助indexOf()方法判断此元素在该数组中首次出现的位置下标与循环的下标是否相等</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">23</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-number">23</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">9</span>,<span class="hljs-number">9</span>,<span class="hljs-number">8</span>,<span class="hljs-number">5</span>,<span class="hljs-number">5</span>,<span class="hljs-number">5</span>];
<span class="hljs-built_in">console</span>.log(arr);    <span class="hljs-comment">//[1, 23, 1, 1, 1, 3, 23, 5, 6, 7, 9, 9, 8, 5, 5, 5]</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">noRepeat2</span>(<span class="hljs-params">arr</span>) </span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
        <span class="hljs-keyword">if</span> (arr.indexOf(arr[i]) != i) &#123;
            arr.splice(i,<span class="hljs-number">1</span>);<span class="hljs-comment">//删除数组元素后数组长度减1后面的元素前移</span>
            i--;<span class="hljs-comment">//数组下标回退</span>
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> arr;
&#125;
<span class="hljs-keyword">var</span> newArr = noRepeat2(arr);
<span class="hljs-built_in">console</span>.log(newArr);    <span class="hljs-comment">//[1, 23, 3, 5, 6, 7, 9, 8]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.利用数组中的filter方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'apple'</span>,<span class="hljs-string">'banana'</span>,<span class="hljs-string">'pear'</span>,<span class="hljs-string">'apple'</span>,<span class="hljs-string">'orange'</span>,<span class="hljs-string">'orange'</span>];
<span class="hljs-built_in">console</span>.log(arr)    <span class="hljs-comment">//["apple", "banana", "pear", "apple", "orange", "orange"]</span>
<span class="hljs-keyword">var</span> newArr = arr.filter(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value,index,self</span>)</span>&#123;
<span class="hljs-keyword">return</span> self.indexOf(value) === index;
&#125;);
<span class="hljs-built_in">console</span>.log(newArr);    <span class="hljs-comment">//["apple", "banana", "pear", "orange"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.借助新数组 通过indexOf方判断当前元素在数组中的索引如果与循环的下标相等则添加到新数组中</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">23</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-number">23</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">9</span>,<span class="hljs-number">9</span>,<span class="hljs-number">8</span>,<span class="hljs-number">5</span>,<span class="hljs-number">5</span>,<span class="hljs-number">5</span>];
<span class="hljs-built_in">console</span>.log(arr)    <span class="hljs-comment">//[1, 23, 1, 1, 1, 3, 23, 5, 6, 7, 9, 9, 8, 5, 5, 5]</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">noRepeat4</span>(<span class="hljs-params">arr</span>) </span>&#123;
    <span class="hljs-keyword">var</span> ret = [];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
        <span class="hljs-keyword">if</span> (arr.indexOf(arr[i]) == i) &#123;
            ret.push(arr[i]);
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> ret;
&#125;
<span class="hljs-keyword">var</span> arr2 = noRepeat4(arr);
<span class="hljs-built_in">console</span>.log(arr2);    <span class="hljs-comment">//[1, 23, 3, 5, 6, 7, 9, 8]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.利用空对象来记录新数组中已经存储过的元素</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">23</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-number">23</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">9</span>,<span class="hljs-number">9</span>,<span class="hljs-number">8</span>,<span class="hljs-number">5</span>];
<span class="hljs-built_in">console</span>.log(arr)    <span class="hljs-comment">//[1, 23, 1, 1, 1, 3, 23, 5, 6, 7, 9, 9, 8, 5]</span>
<span class="hljs-keyword">var</span> obj=&#123;&#125;;
<span class="hljs-keyword">var</span> newArr=[];
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>;i<arr.length;i++)&#123;
    <span class="hljs-keyword">if</span>(!obj[arr[i]])&#123;
        obj[arr[i]]=<span class="hljs-literal">true</span>;
        newArr.push(arr[i]);
    &#125;
&#125;
<span class="hljs-built_in">console</span>.log(newArr);    <span class="hljs-comment">//[1, 23, 3, 5, 6, 7, 9, 8]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6.借助新数组，判断新数组中是否存在该元素如果不存在则将此元素添加到新数组中</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">23</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-number">23</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">9</span>,<span class="hljs-number">9</span>,<span class="hljs-number">8</span>,<span class="hljs-number">5</span>];
<span class="hljs-built_in">console</span>.log(arr);    <span class="hljs-comment">//[1, 23, 1, 1, 1, 3, 23, 5, 6, 7, 9, 9, 8, 5]</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">noRepeat6</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">var</span> newArr = [];
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < arr.length; i++)&#123;
        <span class="hljs-keyword">if</span>(newArr.indexOf(arr[i]) == -<span class="hljs-number">1</span>)&#123;
            newArr.push(arr[i]);
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> newArr;
&#125;
<span class="hljs-keyword">var</span> arr2 = noRepeat6(arr);
<span class="hljs-built_in">console</span>.log(arr2);    <span class="hljs-comment">//[1, 23, 3, 5, 6, 7, 9, 8]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>7.借助新数组，判断新数组中是否存在该元素如果不存在则将此元素添加到新数组中（原数组长度不变但被按字符串顺序排序）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">23</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-number">23</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">9</span>,<span class="hljs-number">9</span>,<span class="hljs-number">8</span>,<span class="hljs-number">5</span>];
<span class="hljs-built_in">console</span>.log(arr);    <span class="hljs-comment">//[1, 23, 1, 1, 1, 3, 23, 5, 6, 7, 9, 9, 8, 5]</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">noRepeat7</span>(<span class="hljs-params">arr</span>) </span>&#123;
    <span class="hljs-keyword">var</span> ret = [],
        end;<span class="hljs-comment">//临时变量用于对比重复元素</span>
    arr.sort();<span class="hljs-comment">//将数重新组排序</span>
    end = arr[<span class="hljs-number">0</span>];
    ret.push(arr[<span class="hljs-number">0</span>]);
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i < arr.length; i++) &#123;
        <span class="hljs-keyword">if</span> (arr[i] != end) &#123;<span class="hljs-comment">//当前元素如果和临时元素不等则将此元素添加到新数组中</span>
            ret.push(arr[i]);
            end = arr[i];
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> ret;
&#125;
<span class="hljs-keyword">var</span> arr2 = noRepeat7(arr);
<span class="hljs-built_in">console</span>.log(arr2);    <span class="hljs-comment">//[1, 23, 3, 5, 6, 7, 8, 9]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>8.此方法没有借助新数组直接改变原数组,并且去重后的数组被排序</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">23</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-number">23</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">9</span>,<span class="hljs-number">9</span>,<span class="hljs-number">8</span>,<span class="hljs-number">5</span>];
<span class="hljs-built_in">console</span>.log(arr);    <span class="hljs-comment">//[1, 23, 1, 1, 1, 3, 23, 5, 6, 7, 9, 9, 8, 5]</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">noRepeat8</span>(<span class="hljs-params">arr</span>) </span>&#123;
    <span class="hljs-keyword">var</span> end;<span class="hljs-comment">//临时变量用于对比重复元素</span>
    arr.sort();<span class="hljs-comment">//将数重新组排序</span>
    end = arr[<span class="hljs-number">0</span>];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i < arr.length; i++) &#123;
        <span class="hljs-keyword">if</span> (arr[i] == end) &#123;<span class="hljs-comment">//当前元素如果和临时元素相等则将此元素从数组中删除</span>
            arr.splice(i,<span class="hljs-number">1</span>);
            i--;
        &#125;<span class="hljs-keyword">else</span>&#123;
            end = arr[i];
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> arr;
&#125;
<span class="hljs-keyword">var</span> arr2 = noRepeat8(arr);
<span class="hljs-built_in">console</span>.log(arr2);    <span class="hljs-comment">//[1, 23, 3, 5, 6, 7, 8, 9]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>9.双层循环改变原数组</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">5</span>,<span class="hljs-number">4</span>,<span class="hljs-number">3</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">6</span>,<span class="hljs-number">6</span>,<span class="hljs-number">6</span>,<span class="hljs-number">6</span>];
<span class="hljs-built_in">console</span>.log(arr);    <span class="hljs-comment">//[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 4, 3, 1, 2, 6, 6, 6, 6]</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">noRepeat9</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> j = <span class="hljs-number">0</span>; j < arr.length; j++) &#123;
            <span class="hljs-keyword">if</span> (arr[i] == arr[j] && i != j) &#123;<span class="hljs-comment">//将后面重复的数删掉</span>
                arr.splice(j, <span class="hljs-number">1</span>);
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> arr;
&#125;
<span class="hljs-keyword">var</span> arr2  = noRepeat9(arr);
<span class="hljs-built_in">console</span>.log(arr2);    <span class="hljs-comment">//[1, 2, 3, 4, 5, 6]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>10.借助新数组</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">5</span>,<span class="hljs-number">4</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>];
<span class="hljs-built_in">console</span>.log(arr);    <span class="hljs-comment">//[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 4, 3, 2, 1, 1, 1]</span>
<span class="hljs-keyword">var</span> newArr = [];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
    <span class="hljs-keyword">var</span> repArr = [];<span class="hljs-comment">//接收重复数据后面的下标</span>
    <span class="hljs-comment">//内层循环找出有重复数据的下标</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> j = i + <span class="hljs-number">1</span>; j < arr.length; j++) &#123;
        <span class="hljs-keyword">if</span> (arr[i] == arr[j]) &#123;
            repArr.push(j);<span class="hljs-comment">//找出后面重复数据的下标</span>
        &#125;
    &#125;
    <span class="hljs-comment">//console.log(repArr);</span>
    <span class="hljs-keyword">if</span> (repArr.length == <span class="hljs-number">0</span>) &#123;<span class="hljs-comment">//若重复数组没有值说明其不是重复数据</span>
        newArr.push(arr[i]);
    &#125;
&#125;
<span class="hljs-built_in">console</span>.log(newArr);    <span class="hljs-comment">//[5, 4, 3, 2, 1]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>11.借助ES6提供的Set结构</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">5</span>,<span class="hljs-number">4</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">1</span>];
<span class="hljs-built_in">console</span>.log(arr);    <span class="hljs-comment">//[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 4, 3, 2, 1, 1, 1]</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">noRepeat11</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">var</span> newArr = [];
    <span class="hljs-keyword">var</span> myset = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(arr);<span class="hljs-comment">//利用了Set结构不能接收重复数据的特点</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> val <span class="hljs-keyword">of</span> myset)&#123;
        newArr.push(val)
    &#125;
    <span class="hljs-keyword">return</span> newArr;
&#125;
<span class="hljs-keyword">var</span> arr2 = noRepeat11(arr)
<span class="hljs-built_in">console</span>.log(arr2);    <span class="hljs-comment">//[1, 2, 3, 4, 5]</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            