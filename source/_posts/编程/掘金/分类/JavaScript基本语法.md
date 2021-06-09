
---
title: 'JavaScript基本语法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3227'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 05:36:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=3227'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">语句和表达式</h2>
<h3 data-id="heading-1">语句</h3>
<p>语句（statement）是为了完成某种任务而进行的操作，比如下面就是一行赋值语句。
<code>var a = 1 + 3;</code>
这条语句先用<code>va</code>r命令，声明了变量<code>a</code>，然后将<code>1 + 3</code>的运算结果赋值给变量a。</p>
<p>语句以分号<code>;</code>结尾，一个分号就表示一个语句结束。</p>
<h3 data-id="heading-2">表达式</h3>
<p>表达式（expression），指一个为了得到返回值的计算式。<code>1 + 3</code>算是表达式。</p>
<h3 data-id="heading-3">语句和表达式的区别</h3>
<p>语句主要为了进行某种操作，一般情况下不需要返回值；表达式则是为了得到返回值，一定会返回一个值。凡是 JavaScript 语言中预期为值的地方，都可以使用表达式。</p>
<h2 data-id="heading-4">标识符</h2>
<p>标识符（identifier）指的是用来<strong>识别值的合法名称</strong>。变量名，函数名都是标识符。</p>
<h3 data-id="heading-5">标识符的命名规则</h3>
<ul>
<li>第一个字符，可以是任意 Unicode 字母（包括英文字母和其他语言的字母），以及美元符号（<code>$</code>）和下划线（<code>_</code>）。</li>
<li>第二个字符及后面的字符，除了 Unicode 字母、美元符号和下划线，还可以用数字<code>0-9</code>。</li>
</ul>
<p>下列为合法的标识符</p>
<pre><code class="copyable">_name
$age
π
arg0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下列为不合法的标识符</p>
<pre><code class="copyable">2a  //第一个字符不可以为数字
*** // 标识符不可以含有星号
a+c // 标识符不可以含有加号
-d // 标识符不可以含有减号或者连词线
<span class="copy-code-btn">复制代码</span></code></pre>
<p>中文也是合法的标识符，可以作为变量名。<code>var 名字 = 'JS'</code></p>
<h2 data-id="heading-6">if else 语句</h2>
<p><code>if</code>结构判断一个表达式的布尔值，为真的情况就执行<code>if</code>包含的语句。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
写法<span class="hljs-number">1</span>
<span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>
<span class="hljs-keyword">if</span>(a === <span class="hljs-number">1</span>)&#123; <span class="hljs-comment">//推荐写法，方便代码的修改</span>
a++;        <span class="hljs-comment">//a=2</span>
&#125;

写法<span class="hljs-number">2</span>
<span class="hljs-keyword">if</span> (a === <span class="hljs-number">1</span>)  a++;   <span class="hljs-comment">// a=2</span>

<span class="hljs-keyword">if</span>(a === <span class="hljs-number">1</span>)   <span class="hljs-comment">//这种写法会导致if的判断跟语句2没有关系，因为if判断成功后只会执行第一句语句。</span>
a++;
语句<span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当<code>if</code>表达式的布尔值为假，<code>else</code>代码块，则是所要执行的代码。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (a === <span class="hljs-number">3</span>) &#123;
  <span class="hljs-comment">// 满足条件时，执行的语句</span>
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// 不满足条件时，执行的语句</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对同一个变量进行多次判断时，多个<code>if...else</code>语句可以连写在一起,<code>else</code>代码块总是与离自己最近的那个<code>if</code>语句配对。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (a === <span class="hljs-number">0</span>) &#123;
  <span class="hljs-comment">// ...</span>
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (a === <span class="hljs-number">1</span>) &#123;
  <span class="hljs-comment">// ...</span>
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (a === <span class="hljs-number">2</span>) &#123;
  <span class="hljs-comment">// ...</span>
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> m = <span class="hljs-number">1</span>;
<span class="hljs-keyword">var</span> n = <span class="hljs-number">2</span>;

<span class="hljs-keyword">if</span> (m !== <span class="hljs-number">1</span>)
<span class="hljs-keyword">if</span> (n === <span class="hljs-number">2</span>) <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello'</span>);
<span class="hljs-keyword">else</span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'world'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码不会有任何输出，<code>els</code>e代码块不会得到执行，因为它跟着的是最近的那个<code>if</code>语句，相当于下面这样。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (m !== <span class="hljs-number">1</span>) &#123;
  <span class="hljs-keyword">if</span> (n === <span class="hljs-number">2</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello'</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'world'</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果想让<code>else</code>代码块跟随最上面的那个<code>if</code>语句，就要改变大括号的位置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (m !== <span class="hljs-number">1</span>) &#123;
  <span class="hljs-keyword">if</span> (n === <span class="hljs-number">2</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello'</span>);
  &#125;
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'world'</span>);
&#125;
<span class="hljs-comment">// world</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">while for 循环</h2>
<h3 data-id="heading-8">while 循环</h3>
<p><code>while</code>语句包括一个循环条件和一段代码块，只要条件为真，就不断循环执行代码块。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//写法1</span>
<span class="hljs-keyword">while</span> (条件)
  语句;

<span class="hljs-comment">// 写法2</span>
<span class="hljs-keyword">while</span> (条件) 语句;

<span class="hljs-comment">//写法3 标准写法</span>
<span class="hljs-keyword">while</span> (条件) &#123;
  语句;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>小例子🌰</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>;

<span class="hljs-keyword">while</span> (i < <span class="hljs-number">100</span>) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'i 当前为：'</span> + i);
  i = i + <span class="hljs-number">1</span>;
&#125;
<span class="hljs-built_in">console</span>.log(i)  <span class="hljs-comment">//i=100</span>
<span class="hljs-comment">//循环100次，直到i等于100为止。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">for 循环</h3>
<p><code>for</code>语句（while 的语法糖）是循环命令的另一种形式，可以指定循环的起点、终点和终止条件。它的格式如下。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">for</span> (初始化表达式; 条件; 递增表达式)
  语句

<span class="hljs-comment">// 或者</span>

<span class="hljs-keyword">for</span> (初始化表达式; 条件; 递增表达式) &#123;
  语句
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>for</code>语句后面的括号里面，有三个表达式。</p>
<ul>
<li>初始化表达式（initialize）：确定循环变量的初始值，只在循环开始时执行一次。</li>
<li>条件表达式（test）：每轮循环开始时，都要执行这个条件表达式，只有值为真，才继续进行循环。</li>
<li>增表达式（increment）：每轮循环的最后一个操作，通常用来递增循环变量。</li>
</ul>
<p>修改一下上面☝的while 例子 🌰</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i<<span class="hljs-number">100</span>; i++)&#123;
 <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'i 当前为：'</span> + i); <span class="hljs-comment">// 0-99</span>
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'i 当前为：'</span> + i); <span class="hljs-comment">//100</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码运行流程</p>
<ol>
<li>声明i=0;</li>
<li>判断i<100</li>
<li>进入代码块，输出当前 i 的值</li>
<li>i+1</li>
<li>判断i<100,开始循环...</li>
</ol>
<h2 data-id="heading-10">break 语句和 continue 语句</h2>
<p><code>break</code>语句和<code>continue</code>语句都具有跳转作用，可以让代码不按既有的顺序执行。
<code>break</code>语句用于跳出代码块或循环。
<code>while</code>和<code>for</code>循环都可以使用<code>break</code>语句跳出循环。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">5</span>; i++) &#123;
  <span class="hljs-built_in">console</span>.log(i);
  <span class="hljs-keyword">if</span> (i === <span class="hljs-number">3</span>)
    <span class="hljs-keyword">break</span>;
&#125;
<span class="hljs-comment">// 0 1 2 3 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码执行到<code>i</code>等于3，就会跳出循环。
<code>continue</code>语句用于立即终止本轮循环，返回循环结构的头部，开始下一轮循环。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>;

<span class="hljs-keyword">while</span> (i < <span class="hljs-number">100</span>)&#123;
  i++;
  <span class="hljs-keyword">if</span> (i % <span class="hljs-number">2</span> === <span class="hljs-number">0</span>) <span class="hljs-keyword">continue</span>;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'i 当前为：'</span> + i);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码只有在<code>i</code>为奇数时，才会输出<code>i</code>的值。如果<code>i</code>为偶数，则直接进入下一轮循环。</p>
<p>如果存在多重循环，不带参数的<code>break</code>语句和<code>continue</code>语句都<strong>只针对最内层循环</strong>。</p>
<h2 data-id="heading-11">label(标签)</h2>
<p>JavaScript 语言允许，语句的前面有标签（label），相当于定位符，用于跳转到程序的任意位置，标签的格式如下。标签通常与<code>break</code>语句和<code>continue</code>语句配合使用，跳出特定的循环。</p>
<pre><code class="hljs language-js copyable" lang="js">label:
  语句
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看例子🌰（top是标签）
<code>break</code>与标签配合使用。</p>
<pre><code class="hljs language-js copyable" lang="js">top:
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">3</span>; i++)&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> j = <span class="hljs-number">0</span>; j < <span class="hljs-number">3</span>; j++)&#123;
      <span class="hljs-keyword">if</span> (i === <span class="hljs-number">1</span> && j === <span class="hljs-number">1</span>) <span class="hljs-keyword">break</span> top;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'i='</span> + i + <span class="hljs-string">', j='</span> + j);
    &#125;
  &#125;
<span class="hljs-comment">// i=0, j=0</span>
<span class="hljs-comment">// i=0, j=1</span>
<span class="hljs-comment">// i=0, j=2</span>
<span class="hljs-comment">// i=1, j=0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码为一个双重循环区块，<code>brea</code>k命令后面加上了<code>top</code>标签（注意，top不用加引号），满足条件时，直接跳出双层循环。如果<code>break</code>语句后面不使用标签，则只能跳出内层循环，进入下一次的外层循环。</p>
<p><code>continue</code>语句与标签配合使用。</p>
<pre><code class="hljs language-js copyable" lang="js">top:
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">3</span>; i++)&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> j = <span class="hljs-number">0</span>; j < <span class="hljs-number">3</span>; j++)&#123;
      <span class="hljs-keyword">if</span> (i === <span class="hljs-number">1</span> && j === <span class="hljs-number">1</span>) <span class="hljs-keyword">continue</span> top;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'i='</span> + i + <span class="hljs-string">', j='</span> + j);
    &#125;
  &#125;
 <span class="hljs-comment">// i=0, j=0</span>
<span class="hljs-comment">// i=0, j=1</span>
<span class="hljs-comment">// i=0, j=2</span>
<span class="hljs-comment">// i=1, j=0</span>
<span class="hljs-comment">// i=2, j=0</span>
<span class="hljs-comment">// i=2, j=1</span>
<span class="hljs-comment">// i=2, j=2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>continue</code>命令后面有一个标签名，满足条件时，会跳过当前循环，直接进入下一轮外层循环。如果<code>continue</code>语句后面不使用标签，则只能进入下一轮的内层循环。</p>
<p><code>代码块</code>语句与标签配合使用。</p>
<pre><code class="hljs language-js copyable" lang="js">foo: &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>);
  <span class="hljs-keyword">break</span> foo;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'本行不会输出'</span>);
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>);
<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码执行到<code>break foo</code>，就会跳出区块。</p>
<p>每日一语：让我们感到不开心的从来不是现实，而是欲望，过多欲望让人变得空虚和弱小，而人类真正的快乐来自于自律和自我决定，自我超越带来的坚定感受。生活的复杂和艰难往往是因为想要的太多，这是一种缺乏自知之明和对生活客观性认知的体现。</p></div>  
</div>
            