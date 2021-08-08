
---
title: 'JavaScript数组API汇总'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9144'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 01:44:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=9144'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">数组中的API（方法）</h1>
<p>在学习JavaScript的道路上，数组是一个非常重要的部分，数组中的API很多，也容易混淆，每次对数组操作的时候都要去查文档，学习的路上也不能一直前进，有时候要停下来做一下总结，我总结了平时比较常用的一些数组API，希望也可以帮到你。</p>
<h4 data-id="heading-1"><code>arry.push()</code></h4>
<p>把一个元素增加到数组的末尾，返回的值为新数组的长度<code>arry.length</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arry = [<span class="hljs-number">2</span>, <span class="hljs-number">9</span>, <span class="hljs-number">5</span>]
<span class="hljs-keyword">let</span> returnValue = arry.push(<span class="hljs-number">4</span>)
<span class="hljs-built_in">console</span>.log(returnValue) <span class="hljs-comment">// 4</span>
<span class="hljs-built_in">console</span>.log(arry) <span class="hljs-comment">// [2, 9, 5, 4]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2"><code>arry.pop()</code></h4>
<p>删除数组中最后一个元素，返回值为删除的元素，实例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arry = [<span class="hljs-number">2</span>, <span class="hljs-number">9</span>, <span class="hljs-number">5</span>]
<span class="hljs-keyword">let</span> returnValue = arry.pop()
<span class="hljs-built_in">console</span>.log(returnValue) <span class="hljs-comment">// 5</span>
<span class="hljs-built_in">console</span>.log(arry) <span class="hljs-comment">// [2, 9]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3"><code>arry.unshift()</code></h4>
<p>与<code>push</code>方法类似，区别在于它是在数组的前面添加元素，返回值为新数组的长度<code>arry.length</code>，示例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arry = [<span class="hljs-number">2</span>, <span class="hljs-number">9</span>, <span class="hljs-number">5</span>]
<span class="hljs-keyword">let</span> returnValue = arry.unshift(<span class="hljs-number">4</span>)
<span class="hljs-built_in">console</span>.log(returnValue) <span class="hljs-comment">// 4</span>
<span class="hljs-built_in">console</span>.log(arry) <span class="hljs-comment">// [4, 2, 9, 5]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由此可知，使用<code>push</code>和<code>shift</code>组合可以实现数据的‘先进先出’当然也可以使用<code>unshift</code>和<code>pop</code></p>
<h4 data-id="heading-4"><code>arry.reverse()</code></h4>
<p>把数组反向排序，这里要注意它会改变原来的数组，而不会创建新的数组，示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arry = [<span class="hljs-number">2</span>, <span class="hljs-number">9</span>, <span class="hljs-number">5</span>]
arry.reverse()
<span class="hljs-built_in">console</span>.log(arry) <span class="hljs-comment">// [ 5, 9, 2 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5"><code>arry.sort()</code></h4>
<p>对数组进行排序，可接受参数，参数必须是函数，如果不没有参数 则是按照字符编码的顺序进行排序，示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arry = [<span class="hljs-number">10</span>, <span class="hljs-number">5</span>, <span class="hljs-number">40</span>, <span class="hljs-number">1000</span>]
<span class="hljs-built_in">console</span>.log(arry.sort()) <span class="hljs-comment">// [ 10, 1000, 40, 5 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果数字想要按大小排列，可写入参数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">3</span>, <span class="hljs-number">1</span>, <span class="hljs-number">7</span>]
<span class="hljs-built_in">console</span>.log(arr.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a - b)) <span class="hljs-comment">// [ 1, 3, 7 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6"><code>arry.forEach(item, index)</code>与<code>arry.map(item, index)</code></h4>
<p>两者都是对数组遍历，index表示数组索引，不是必须的参数区别在于<code>map</code>方法会返回一个新的数组，示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arry = [<span class="hljs-number">1</span>, <span class="hljs-number">5</span>, <span class="hljs-number">10</span>, <span class="hljs-number">15</span>];
<span class="hljs-keyword">let</span> arry1 = arry.map( <span class="hljs-function"><span class="hljs-params">x</span> =></span> x + <span class="hljs-number">2</span>);
<span class="hljs-built_in">console</span>.log(arry1) <span class="hljs-comment">// [ 3, 7, 12, 17 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7"><code>arry.some()</code></h4>
<p>用于检测数组中的元素是否满足指定条件,参数也是函数如果有一个元素满足条件，则表达式返回true , 剩余的元素不会再执行检测。如果没有满足条件的元素，则返回false。</p>
<pre><code class="hljs language-js- copyable" lang="js-">let arry = [1, 5, 10, 15];
console.log(arry.some(item => item > 10)) // true
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8"><code>arry.every()</code></h4>
<p>用于检测数组中的所有元素是否满足指定条件,只有当数组中灭一个元素都满足条件时，表达式返回true , 否则返回false，示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arry = [<span class="hljs-number">5</span>, <span class="hljs-number">10</span>, <span class="hljs-number">15</span>];
<span class="hljs-built_in">console</span>.log(arry.every(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item > <span class="hljs-number">2</span>)) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9"><code>arry.filter()</code></h4>
<p>它创建一个新的数组，原数组不变，新数组中的元素是通过检查指定数组中符合条件的所有元素，示例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arry = [<span class="hljs-number">1</span>, <span class="hljs-number">5</span>, <span class="hljs-number">10</span>, <span class="hljs-number">15</span>];
<span class="hljs-keyword">let</span> arry1 = arry.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item > <span class="hljs-number">5</span>)
<span class="hljs-built_in">console</span>.log(arry) <span class="hljs-comment">// [ 1, 5, 10, 15 ]</span>
<span class="hljs-built_in">console</span>.log(arry1) <span class="hljs-comment">// [ 10, 15 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10"><code>arry.join()</code></h4>
<p>把数组元素合并为一个字符串，如果不带参数，默认用逗号分隔</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arry = [<span class="hljs-number">5</span>, <span class="hljs-number">10</span>, <span class="hljs-number">15</span>];
<span class="hljs-built_in">console</span>.log(arry.join()) <span class="hljs-comment">// 5,10,15</span>
<span class="hljs-comment">// 添加参数</span>
<span class="hljs-keyword">let</span> arry = [<span class="hljs-number">5</span>, <span class="hljs-number">10</span>, <span class="hljs-number">15</span>];
<span class="hljs-built_in">console</span>.log(arry.join(<span class="hljs-string">'.'</span>)) <span class="hljs-comment">// 5.10.15</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11"><code>arry.splice(index, hm, add)</code></h4>
<p>它既可以删除特定的元素，也可以在特定位置增加元素，也可以删除增加同时搞定，<code>index</code>是起始位置，<code>hm</code>是要删除元素的个数，<code>add</code>是要增加的元素，上例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> myFish = [<span class="hljs-string">'angel'</span>, <span class="hljs-string">'clown'</span>, <span class="hljs-string">'mandarin'</span>, <span class="hljs-string">'sturgeon'</span>]
myFish.splice(<span class="hljs-number">2</span>, <span class="hljs-number">0</span>, <span class="hljs-string">'drum'</span>) <span class="hljs-comment">// hm为0 表示不删除任何元素</span>
<span class="hljs-built_in">console</span>.log(myFish) <span class="hljs-comment">// [ 'angel', 'clown', 'drum', 'mandarin', 'sturgeon' ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> myFish = [<span class="hljs-string">'angel'</span>, <span class="hljs-string">'clown'</span>, <span class="hljs-string">'mandarin'</span>, <span class="hljs-string">'sturgeon'</span>]
myFish.splice(<span class="hljs-number">2</span>, <span class="hljs-number">1</span>, <span class="hljs-string">'drum'</span>)
<span class="hljs-built_in">console</span>.log(myFish)  <span class="hljs-comment">// [ 'angel', 'clown', 'drum', 'sturgeon' ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12"><code>arry.concat()</code></h4>
<p>用于连接两个或多个数组，返回值为连接后的新数组，原数组不变，示例：</p>
<pre><code class="copyable">let arry1 = [1, 2, 3]
let arry2 = [4, 5, 6]
arry1.concat(arry2)
console.log(arry1.concat(arry2)) // [ 1, 2, 3, 4, 5, 6 ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这些就是关于数组常用的api，可以大胆地添加收藏，以备不时之需～</p></div>  
</div>
            