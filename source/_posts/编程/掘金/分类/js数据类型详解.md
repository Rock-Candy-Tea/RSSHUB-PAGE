
---
title: 'js数据类型详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2936'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 05:05:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=2936'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“这是我参与更文挑战的第4天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>”
#js的数据类型分类</p>
<ul>
<li>
<p>基本数据类型</p>
<ul>
<li>number</li>
<li>string</li>
<li>boolean</li>
<li>null</li>
<li>undefined</li>
<li>symbol</li>
</ul>
<p>1.static.Symbol
2.Symbol.prototype</p>
</li>
<li>
<p>引用数据类型</p>
<ul>
<li>object
1.普通对象
2.数组对象
3.正则对象
4.日期对象
5.JSON对象
6.Set
7.Map</li>
</ul>
</li>
<li>
<p>函数
1.普通函数
2.构造函数
3.箭头函数
4.生成器函数</p>
</li>
</ul>
<p>##首先我们先来说一下number类型
number类型包括的是正数 0 负数 小数，还有一个NaN(非数字)</p>
<pre><code class="copyable">typeof (NaN) // number
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后需要注意的是NaN!=NaN,因此当我们执行下面的判断是不会生效的。</p>
<pre><code class="copyable">let value  = NaN;  //注意这个NaN一般是经过转化之后得到的比如说 Number('string')
if(value==NaN)&#123;
// operate sth
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那这样我们怎么去判断一个变量的value是不是NaN的值呢？
有两种方法：
第一种：</p>
<pre><code class="copyable"> let value  =  NaN;
 isNaN(value)// true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二种方法是通过Object.is()</p>
<pre><code class="copyable">object.is(NaN, NaN) // Object.is(),是判断两个值是否相等的 ，如果是对象的话那么就是判断两个对象是不是共用一个存储空间 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于NaN一般是经过转化获取的 ， 所以我们来讲一下如果将其他数据类型转化成number类型
<strong>显示转化</strong> 有下面几种方法</p>
<pre><code class="copyable"> let  a ='String'
// (1) Number()
Number(a)
//  (2) parseInt()/ parseFloat()
parseInt(a)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意注意的是这集中方法虽然都可以将其他数据类型转化成number类型的，但是他们的转化规则和机制都是不相同的。
首先说一下Number转换
如果是boolean，那么true 和false会被分别转换成1， 0 。
null → 0
undefined→ NaN
如果是字符串的话：
(1)如果字符串是‘’， 那么会被转化成0；
(2)如果字符串前面包含空格，会去掉空格进行转换</p>
<pre><code class="copyable">let  str  ='     11111';
Number(str)//1111
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(3)字符串包含有效地十六进制， 如'0xf', 那么会转化为相大小的十进制</p>
<pre><code class="copyable">let str  ='0xf'
Number(str)// 15
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(4)字符串前面有0的话，会忽略前面的0，进行转换</p>
<pre><code class="copyable">let str  ="000033333"
 Number(str) //33333
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(5)数字中混入其他非数字，那么都会被转化成NaN</p>
<pre><code class="copyable">let str  ='1111 ddd'
 Number(str) // NaN
let str1  ='ddd1111 '
 Number(str1) // NaN
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于parseInt的转换规则主要是：
(1)如果是数字开头的话， 会一直解析到遇到非数字的character停止, 如果是小数比如1.1，那么会解析到小数点前面的， 返回1</p>
<pre><code class="copyable">parseInt('11111dddddd222222') //11111
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(2)如果字符串前面包含空格，会去掉空格进行转换。</p>
<pre><code class="copyable">parseInt('     11111dddddd222222') //11111
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(3)其他情况都会被转化为NaN</p>
<pre><code class="copyable"> parseInt(true)// NaN;
parseInt('ddddd111111')//NaN
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(4)使用parseInt的时候还可以把二进制把金卮十六进制或者其他任何禁止的字符串转化成整数</p>
<pre><code class="copyable">var num1 = parseInt("AF",16);　　　　　　 　　　　//175
var num2 = parseInt("AF");　　　　　　　　　　　　//NaN
var num3 = parseInt("10",2);　　　　　　　 　　　//2　　(按照二进制解析)
var num4 = parseInt("sdasdad");　　　　　　　　　//NaN

<span class="copy-code-btn">复制代码</span></code></pre>
<p>parseFloat()与parseInt转换规则类似， 不一样的地方是 ， 他不能转化成对应的进制
并且他遇到小数点的话可以继续解析 。</p>
<p><strong>隐式转换</strong>
主要有三种，
(1)+  (1+true)
(2) == 比较的时候
(3) isNaN() 也会先进行转化成数字在进行比较</p>
<p>##String类型
(1)"",
(2)``
把其他类型的值转化成String类型。
<strong>显式转换</strong>
(1) toString()
(2)String()
<strong>隐式转换</strong>
(1)+加号除了数学运算还可以拼接字符串 。
下面我们来说下加号的拼接规则。
(1)如果加号两边， 其中一边出现了字符串的话 ， 那么会出现拼接字符串 。</p>
<pre><code class="copyable"> let n  = 10
let res  = n  + '10' // 1010
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(2) 加号两边， 其中一边是一个对象的话 ，则也可能成为字符串拼接
_ 对象出现在右边</p>
<pre><code class="copyable"> let m  =  10
 let res  =  m +  &#123;&#125; //  "10[object Object]"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>_ 对象处在左边</p>
<pre><code class="copyable">&#123;&#125; + 10 // 10  像这种不加上括号的， 浏览器会认为前面的对象是一个代码块 ， 不参与运算的 ， 所以返回的时候后面的数字
(&#123;&#125; + 10 ) // "[object Object]10" // 这里浏览器会认为这个&#123;&#125;参与运算， 所以返回的是字符串拼接
<span class="copy-code-btn">复制代码</span></code></pre>
<p>_ 对象 是new Number类型的 ， new Nnumber会转化成Number类型的来计算</p>
<pre><code class="copyable"> let m  = 10, 
let obj  = new Number(10)
 obj+ m  // 20
<span class="copy-code-btn">复制代码</span></code></pre>
<p>_对象里面属性中含有的是value的属性</p>
<pre><code class="copyable">let test  = &#123;
value: 10
&#125;
test+ 10 // "[object Object]10"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看了上面的例子， 那如果加号的一边是对象计算底层机制是什么呢 ？
检测对象的 Symbol.toPrimitive的属性是否存在， 如果是存在的话，基于这个值进行计算， 如果没有话 ，
检测对象的valueOf(), 如果这个值是基本类型值 的话， 则基于这个值来计算 ， 如果这个值不是基本类型值的话，获取对象的toString(), 然后进行拼接。
例如我们写一个 对象含有Symbol.primitive属性：</p>
<pre><code class="copyable">let obj  =&#123;
[Symbol.toPrimitive]: function ()&#123;
return 10 
&#125;
&#125;
obj+ 10 // 20
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们的new Number(10) + 10 之所以为20 是因为 new Number(10).valueOf()//10， 所以可以直接计算 。<br>
其他转化成字符串的就是通过了toString()</p>
<p>(3)如果加号之后只有一边， 如果是字符串的话就会被转换成数字</p>
<pre><code class="copyable">let m  = '10'
console.log(+m) // 10
console.log(++m) // 11
<span class="copy-code-btn">复制代码</span></code></pre>
<p>##Symbol类型
这种 类型的作用是创建唯一值。
(1)给对象设置一个Symbol属性， 这是一个唯一属性来减少属性上面的冲突 。
例如给一个对象创造唯一属性 我们可以使用</p>
<pre><code class="copyable">let obj  = &#123;
[Symbol()]: '11111'

&#125;
obj[Symbol] // undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是我们不能够拿出这个唯一属性的值 ， 所以我们可以事先 定义一个变量名叫 x</p>
<pre><code class="copyable">let x  =  Symbol()
let obj  = &#123;
[x]: 1
&#125;
 obj[x] // 1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(2)来宏观管理一些唯一标识的时候，也是用的唯一值。比如说上面的Symbol.toPrimiteve。类似的还有
Symbol.hasInstance、 Symbol.toStringTag()、Symbol.iterator
需要注意的是 ： Symbol是一个构造函数， 但是我们不能使用new  Symbol()来创建 ，并且 两个Symbol是不相同的</p>
<pre><code class="copyable">Symbol('a') ===Symbol('a') // false
<span class="copy-code-btn">复制代码</span></code></pre>
<p>##BigInt类型
大数类型 主要是用来解决当数字超过Number.MAX_SAFE_INTEGER， 或者是 Number.MIN_SAFE_INTEGER， 发生溢出， 导致计算错误的问题的 。</p>
<pre><code class="copyable">let a  =  Number.MAX_SAFE_INTEGER // 9007199254740991
a+ 10 // 9007199254741000 
//尾数应该是1， 但是现在的结果还是 0， 所以说是有问题的 ， 我们可以利用大数类型来解决的

<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先说下 如何创建BigInt类型，
第一种是直接BigInt(10)
第二种是  10n, 后面直接加上n</p>
<pre><code class="copyable"> let  b  = BigInt(9007199254740991)
let d  = 10n
b +d //9007199254741001n
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            