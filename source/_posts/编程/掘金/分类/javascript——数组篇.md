
---
title: 'javascript——数组篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=661'
author: 掘金
comments: false
date: Sun, 18 Apr 2021 01:58:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=661'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1、什么是数组？</h2>
<p>数组的标准定义为：<strong>一个存储元素的线性集合（collection），元素可以通过索引来任意存取，索引通常为数字，用来计算元素存储位置的偏移量。</strong>  如果你有了解过其他语言，就会知道所有编程语言都有类似的数据结构。但javascript的数组和其他语言有所不同。JavaScript中的数组是一种特殊的对象，索引为该对象的素性，索引可能是整数。然而，这些数字索引在内部被转换为字符串类型，这是因为JavaScript对象的属性名必须是字符串类型。 数组在JavaScript中只是一种特殊的对象，所以效率上不如其他语言中的数组高。JavaScript中的数组，严格来说应该称作对象，是特殊的JavaScript对象，在内部被归类为数组。由于Array在JavaScript中被当作对象，因此它有许多属性和方法可以在编程时使用。</p>
<h2 data-id="heading-1">2、使用数组</h2>
<p>JavaScript的数组十分的灵活有许多方法可以操作数组，在使用之前首先需要创建数组。</p>
<h3 data-id="heading-2">2.1创建数组</h3>
<h4 data-id="heading-3">法一：通过[]操作符声明一个数组变量</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> nums = []
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方式创建的数组得到的是长度为0的空数组，可以通过数组的length属性来验证这一点</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> nums = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你也可以通过在[]操作符声明数组的同时，放入一组元素</p>
<h4 data-id="heading-4">法二：通过调用Array的构造函数创建数组</h4>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> nums = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>();
 <span class="hljs-built_in">console</span>.log(nums.length)  <span class="hljs-comment">//0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同理你也可以在声明时设置初始值：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> nums = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">1</span>，<span class="hljs-number">2</span>，<span class="hljs-number">3</span>，<span class="hljs-number">4</span>，<span class="hljs-number">5</span>);
 <span class="hljs-built_in">console</span>.log(nums.length)   <span class="hljs-comment">//5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在调用Array的构造函数时，可以只传入一个参数，用来指定数组的长度：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> nums = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">20</span>);
 <span class="hljs-built_in">console</span>.log(nums.length)   <span class="hljs-comment">//20</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2.2读写数组</h3>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">let</span> arr = []  <span class="hljs-comment">//声明</span>
    <span class="hljs-keyword">let</span> sums = <span class="hljs-number">0</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">100</span>; i++) &#123;   <span class="hljs-comment">//赋值</span>
        arr[i] = i
    &#125;
    arr.map(<span class="hljs-function">(<span class="hljs-params">item, i</span>) =></span> &#123;  <span class="hljs-comment">//读取</span>
        <span class="hljs-comment">// console.log(item,i);</span>
        sums += item
    &#125;)
    <span class="hljs-built_in">console</span>.log(sums);   <span class="hljs-comment">//4950</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">2.2.1 由字符串生成数组</h4>
<p>调用字符串对象的split()方法也可以生成数组：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str=<span class="hljs-string">`we are family !`</span>
    <span class="hljs-keyword">let</span> arr=str.split(<span class="hljs-string">" "</span>)
    arr.map(<span class="hljs-function">(<span class="hljs-params">item,i</span>)=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`arr<span class="hljs-subst">$&#123;i&#125;</span>:<span class="hljs-subst">$&#123;item&#125;</span>`</span>);
        <span class="hljs-comment">/*输出：
          arr0:we
          arr1:are
          arr2:family
          arr3:!
        */</span>
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">2.2.2 对数组的整体性操作</h4>
<p>是将数组作为一个整体进行的。比如整体赋值：</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">let</span> arr = []  <span class="hljs-comment">//声明</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;   <span class="hljs-comment">//赋值</span>
        arr[i] = i
    &#125;
    <span class="hljs-keyword">let</span> arr2 = arr
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，使用这种方法把一个数组赋给另外一个数组时，只是为被赋值的数组增加了一个新的引用。当你通过原引用修改了数组的值，另外一个引用也会感知到这个变化，如：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> arr = []  <span class="hljs-comment">//声明</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;   <span class="hljs-comment">//赋值</span>
        arr[i] = i
    &#125;
    <span class="hljs-keyword">let</span> arr2 = arr
    arr[<span class="hljs-number">0</span>]=<span class="hljs-number">100</span>
    <span class="hljs-built_in">console</span>.log(arr1[<span class="hljs-number">0</span>])  <span class="hljs-comment">//100</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种行为被称为浅复制，新数组依然指向原来的数组。一个更好的方案是使用深复制，将原数组中的每一个元素都复制一份到新数组中。如可以写一个函数来深拷贝（复制）数组：</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">let</span> arr1=[<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">8</span>,<span class="hljs-number">9</span>],arr2=[]
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CopyArr</span>(<span class="hljs-params">arr1,arr2</span>)</span>&#123;
        arr1.map(<span class="hljs-function">(<span class="hljs-params">item,i</span>)=></span>&#123;
            arr2[i]=item
        &#125;)
        <span class="hljs-keyword">return</span> arr2
    &#125;
    arr2=CopyArr(arr1,arr2)
    <span class="hljs-built_in">console</span>.log(arr2);     <span class="hljs-comment">// [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]</span>
    arr1[<span class="hljs-number">0</span>]=<span class="hljs-number">100</span>
    <span class="hljs-built_in">console</span>.log(arr1[<span class="hljs-number">0</span>],arr2[<span class="hljs-number">0</span>]);  <span class="hljs-comment">//100 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">2.3数组方法</h3>
<p>1、JavaScript 方法 toString() 把数组转换为数组值（逗号分隔）的字符串。</p>
<p>2、join() 方法也可将所有数组元素结合为一个字符串。</p>
<p>3、pop() 方法从数组中删除最后一个元素。</p>
<p>4、push() 方法（在数组结尾处）向数组添加一个新的元素。</p>
<p>5、shift() 方法会删除首个数组元素，并把所有其他元素“位移”到更低的索引。</p>
<p>6、unshift() 方法（在开头）向数组添加新元素，并“反向位移”旧元素。</p>
<p>7、length 属性提供了向数组追加新元素的简易方法。</p>
<p>8、使用 delete 会在数组留下未定义的空洞。请使用 pop() 或 shift() 取而代之。</p>
<p>9、splice() 方法可用于向数组添加新项，也可删除数组中的元素。</p>
<p>10、concat() 方法通过合并（连接）现有数组来创建一个新数组。</p>
<p>11、slice() 方法用数组的某个片段切出新数组。</p>
<p>12、sort() 方法用于对数组的元素进行排序。</p>
<p>13、reverse() 方法用于颠倒数组中元素的顺序。</p>
<p>14、toLocaleString() 方法把数组转换为本地字符串。</p>
<p>15、valueOf() 方法返回 Array 对象的原始值。</p>
<p>具体用法可见：<a href="https://juejin.cn/post/url"> </a><a href="https://www.w3school.com.cn/jsref/jsref_obj_array.asp" target="_blank" rel="nofollow noopener noreferrer">www.w3school.com.cn/jsref/jsref…</a></p>
<h3 data-id="heading-9">2.4二维和多维数组</h3>
<p>JavaScript只支持一维数组，但是通过在数组里保存数组元素的方式，可以轻松创建多维数组。</p>
<h4 data-id="heading-10">2.4.1创建二维数组</h4>
<p>二维数组类似一种由行和列构成的数据表格。在JavaScript中创建二维数组，需要先创建一个数组，然后让数组的每个元素也是一个数组。我们需要知道二维数组要包含多少行，有了这个信息，就可以创建一个n行1列的二维数组了：</p>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-keyword">let</span> arr=[]
   <span class="hljs-keyword">let</span> rows=<span class="hljs-number">5</span>
   <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<rows;i++)&#123;
       arr[i]=[]
   &#125;
   <span class="hljs-built_in">console</span>.log(arr);   <span class="hljs-comment">// [Array(0), Array(0), Array(0), Array(0), Array(0)]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样做的问题是，数组中的每个元素都是undefined。更好的方式是遵照JavaScript: The Good Parts（O'Reilly）一书第64页的例子，Crockford通过扩展JavaScript数组对象，为其增加了一个新方法，该方法根据传入的参数，设定了数组的行数、列数和初始值。下面是这个方法的定义：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*@ params
       numrows:行数
       numcols:列数
       initial:行列对应下的初始值
    */</span>
    <span class="hljs-built_in">Array</span>.matrix = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">numrows, numcols, initial</span>) </span>&#123;
        <span class="hljs-keyword">let</span> arr = []
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < numrows; i++) &#123;
            <span class="hljs-keyword">let</span> columns = []
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j; j < numcols; j++) &#123;
                columns[j] = initial
            &#125;
            arr[i] = columns
        &#125;
        <span class="hljs-keyword">return</span> arr
    &#125;
    
    <span class="hljs-keyword">let</span> nums = <span class="hljs-built_in">Array</span>.matrix(<span class="hljs-number">5</span>,<span class="hljs-number">5</span>,<span class="hljs-number">0</span>);
    <span class="hljs-built_in">console</span>.log(nums[<span class="hljs-number">0</span>][<span class="hljs-number">0</span>])    <span class="hljs-comment">//0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于小规模的数据还是使用这种方式最简单，仅需一行代码即可：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> nums = [[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>], [<span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>], [<span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>]]
 <span class="hljs-built_in">console</span>.log(nums[<span class="hljs-number">2</span>][<span class="hljs-number">2</span>]);   <span class="hljs-comment">//9</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">2.4.2处理二维数组的元素</h4>
<p>处理二维数组中的元素，有两种最基本的方式：按列访问和按行访问:</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">let</span> nums = [[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>], [<span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>], [<span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>]]
    <span class="hljs-keyword">let</span> total = <span class="hljs-number">0</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < nums.length; i++) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < nums[i].length; j++) &#123;
            total += nums[i][j]
        &#125;
    &#125;
    <span class="hljs-built_in">console</span>.log(total) 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于多维数组无非是，内循环控制行，外循环控制列。</p>
<h3 data-id="heading-12">2.5对象中的数组</h3>
<p>在对象中，可以使用数组存储复杂的数据。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wageTemp</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">this</span>.dataSource = []
        <span class="hljs-built_in">this</span>.add = add
        <span class="hljs-built_in">this</span>.averag = averag
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">data</span>) </span>&#123;
        <span class="hljs-built_in">this</span>.dataSource.push(data)
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">averag</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">let</span> total = <span class="hljs-number">0</span>
        <span class="hljs-built_in">this</span>.dataSource.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
            total += item
        &#125;)
        <span class="hljs-keyword">return</span> total / <span class="hljs-built_in">this</span>.dataSource.length
    &#125;

    <span class="hljs-keyword">let</span> gzTemp = <span class="hljs-keyword">new</span> wageTemp()
    gzTemp.add(<span class="hljs-number">100</span>)
    gzTemp.add(<span class="hljs-number">90</span>)
    gzTemp.add(<span class="hljs-number">80</span>)
    gzTemp.add(<span class="hljs-number">88</span>)
    gzTemp.add(<span class="hljs-number">99</span>)
    <span class="hljs-built_in">console</span>.log(gzTemp.averag());    <span class="hljs-comment">//91.4</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>（以上内容为阅读《数据结构与算法JavaScript描述》总结笔记，如有雷同，纯属巧合...）</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            