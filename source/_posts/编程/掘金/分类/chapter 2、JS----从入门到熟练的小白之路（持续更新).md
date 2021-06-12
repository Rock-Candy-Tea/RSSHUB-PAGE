
---
title: 'chapter 2、JS----从入门到熟练的小白之路（持续更新....)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7565'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 04:01:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=7565'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、操作语句</h1>
<h2 data-id="heading-1">1、if/else if/else</h2>
<p>只要满足其中一个条件，后面的条件就不再执行</p>
<ul>
<li><strong>1.1 单独一个if</strong></li>
</ul>
<pre><code class="copyable">var num=10;
if(num>2)&#123;
    alert("你很优秀")；
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>1.2 if/else</strong></li>
</ul>
<pre><code class="copyable">var num=5;
if(num>0)&#123;
   alert("你好")
&#125;else&#123;
   alert("你坏")
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>1.3 if/else if/else</strong></li>
</ul>
<pre><code class="copyable">var num=0;
if(num>0)&#123;
   alert("正数")
&#125;else if(num<0)&#123;
   alet("负数”)
&#125;else&#123;
    alert(0)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>1.4 if/ eles if   else if .../else</strong></li>
</ul>
<blockquote>
<p>if 条件语句，只要满足其中一个条件，后面的条件就不再执行</p>
</blockquote>
<pre><code class="copyable">var num=6;
    if(num>0)&#123;
       num--;
       alert("1:"+num);
    &#125;else if(num>0 && num<10)&#123;
        num++;
        alert("2:"+num);
    &#125;else &#123;
        num--;
    &#125;
    console.log(num)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">2、判断条件</h2>
<ul>
<li>&& 表示并且，左右两边的条件必须同时满足</li>
<li>||   表示或，左右两边的条件只要满足其一即可</li>
<li>如果是单独的一个值，先把它转换成布尔类型，如果是真，条件 成立，如果假，条件不成立。</li>
</ul>
<blockquote>
<p>回忆其它值转换为布尔值，只有哪几种情况是false；</p>
</blockquote>
<ul>
<li>0</li>
<li>NaN</li>
<li>null</li>
<li>“”</li>
<li>undefined</li>
</ul>
<pre><code class="copyable">if(true)&#123;
   alert("刷碗去！")
&#125;
if(false)&#123;
    alert("去刷剧")
&#125;else&#123;
   alert("去睡觉")
&#125;
if(0)&#123;
   
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">二、在js中用来检测数据类型的四种方式</h1>
<ul>
<li>typeof</li>
<li>instanceof</li>
<li>constructor</li>
<li>Object.prototype.toString.call()</li>
</ul>
<h2 data-id="heading-4">1、typeof 运算符 详解</h2>
<pre><code class="copyable">  typeof 首先返回的是一个字符串，它返回的类型.
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>'number'</li>
<li>'string'</li>
<li>'boolean'</li>
<li>'undefined'</li>
<li>'object'</li>
<li>'function'</li>
</ul>
<p><code>注意：typeof null 返回的是'object' 需要特殊记忆， 另外typeof 检测数组、正则、普通对象，返回的都是“object”，所以用typeof 检测的话，并不能细分。</code></p>
<pre><code class="copyable">typeof 12  ===> "number"
typeof "zhufeng" ====》 'string'
typeof false   ===>'boolean'
typeof true ====>  'boolean'
typeof null ====> 'object'
typeof undefined ====>'undefined'
typeof [1,2] =====>"object"
typeof function()&#123;&#125; =>"function"
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">2、BAT面试题</h2>
<p>2-1、</p>
<pre><code class="copyable">typeof []
typeof typeof []
2.2 
var num=parseInt("px35.5");
if(num==35.5)&#123;
    alert(0)
&#125;else if(num==35)&#123;
    alert(1)
&#125;else if(num==NaN)&#123;
    alert(3)
&#125;else if(typeof num=='number')&#123;
    alert(4)
&#125;else&#123;
   alert(5)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">三、三元运算符</h1>
<h2 data-id="heading-7">1、【语法】：</h2>
<blockquote>
<p>条件?条件成立执行的语句：条件不成立执行的语句</p>
</blockquote>
<pre><code class="copyable">var num=5
if(num>=5)&#123;
   num++
&#125;else&#123;
   num--
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>改写成三元运算符</strong></p>
<blockquote>
<p>num>=5?num++:num--</p>
</blockquote>
<h2 data-id="heading-8">2、【特殊情况】</h2>
<blockquote>
<p>条件成立，我想做一件事情，不成立我什么不做，可以用 undefined/null/void 0来做占位符</p>
</blockquote>
<pre><code class="copyable">var num=5;
num>=5?num++:undefinde;
num>=5?num++:null;
num>=5?num++:void 0;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">3、【多条语句】</h2>
<blockquote>
<p>如果条件成立之后，想同时执行多条语句，我们可以用“小括号”把执行语句包起来，并且语句与语句之间用“逗号”进行分割</p>
</blockquote>
<pre><code class="copyable">var num=5;
var a=3;
num>=5?(num++,a--):null;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">4、【思考题】</h2>
<p>把下面的代码改成三元运算符</p>
<pre><code class="copyable">var num=12;
if(num>0)&#123;
   if(num<10)&#123;
     num++;
   &#125;else&#123;
     num--;
   &#125;
&#125;else&#123;
    if(num==0)&#123;
       num++;
       num=num/10;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">四、switch case 操作语句</h1>
<ul>
<li>把表达式的值与每个 case 的值进行对比</li>
<li>如果存在匹配，则执行关联代码</li>
</ul>
<pre><code class="copyable">switch(表达式) &#123;
     case n:
        代码块
        break;
     case n:
        代码块
        break;
     default:
        默认代码块
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">1、[初识]</h2>
<pre><code class="copyable">var num=6;
if(num==5)&#123;
    num++;
&#125;else if(num==6)&#123;
    num--;
&#125;else &#123;
    num=0;
&#125;
console.log(num);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>把上面的改成switch case 语句</p>
<pre><code class="copyable">var num=6;
switch (num)&#123;
    case 5:
      num++;
      break;
    case 6:
      num--;
      break;
    default:
      num=0;    
&#125;
console.log(num);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">2、switch case 和if elese 的区别</h2>
<p>如果把上面的案例，num的值改为字符串的6，用if else  和switch case 会出现什么样的结果呢，答案是否还相同呢？</p>
<pre><code class="copyable">在if  else 条件判断中，两个== 进行比较的时候，如果数据类型不同，会先转换为相同的数据类型再比较
在switch case 中，条件判断 其实是三个===，绝对等于，不仅要值相同，类型也要相同，所以才会出现上面不同的情况。
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">3、巧用switch case 中的break</h2>
<p>switch case 中的break 表示条件终止，如果不加break 的时候，会继续往下执行。 但是我们可以巧用这个特点，来做条件或当num等于6或者num=10 的时候，让num的值都加加：</p>
<pre><code class="copyable">var num=6;
switch (num)&#123;
     case 6:
     case 10:    
         num++;
         break;
     default:
         num=0;    
&#125;
console.log(num);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            