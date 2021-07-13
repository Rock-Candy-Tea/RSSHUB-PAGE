
---
title: '重学JS基础--数据类型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3047'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 03:01:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=3047'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一.基本数据类型</h2>
<p>js有5大基本数据类型包括：</p>
<ul>
<li>undefined</li>
<li>null</li>
<li>number</li>
<li>boolean</li>
<li>string</li>
<li>ES6新增了一种基本数据类型Symbol（用于标识唯一性）</li>
</ul>
<p>这些数据是直接存在栈空间中的，基本数据类型是<strong>按值</strong>访问的，就是说我们可以操作保存在变量中的实际的值。</p>
<h3 data-id="heading-1">基本数据类型的值是不可变的</h3>
<p>任何方法都无法改变一个基本类型的值，比如一个字符串：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> name = <span class="hljs-string">"change"</span>;
name.substr();<span class="hljs-comment">//hang</span>
<span class="hljs-built_in">console</span>.log(name);<span class="hljs-comment">//change</span>

<span class="hljs-keyword">var</span> s = <span class="hljs-string">"hello"</span>;
s.toUpperCase()<span class="hljs-comment">//HELLO;</span>
<span class="hljs-built_in">console</span>.log(s)<span class="hljs-comment">//hello</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这两个例子，我们会发现原先定义的变量name的值始终没有发生改变，而调用substr()和toUpperCase()方法后返回的是一个<strong>新的</strong>字符串，跟原先定义的变量name并没有关系</p>
<p>假如我们直接赋值改变呢，看代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> name = <span class="hljs-string">"change"</span>;
name = <span class="hljs-string">"change1"</span>;
<span class="hljs-built_in">console</span>.log(name)<span class="hljs-comment">//change1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样看起来name的值“改变了”
其实，var name = "change"，这里的基础类型是string，也就是"change",这里的"change"是不可以改变的</p>
<p>name只是指向"change"的一个指针，指针的指向可以改变，所以你可以name = "change1".此时name指向了"change1"，同理，这里的"change1"同样不可以改变.</p>
<p>也就是说这里你认为的改变只是“指针的指向改变”，这里的基础类型指的是"change"，而不是name，要区分清楚</p>
<h3 data-id="heading-2">基本数据类型不可以添加属性和方法</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> p = <span class="hljs-string">"change"</span>;
p.age = <span class="hljs-number">29</span>;
p.method = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;<span class="hljs-built_in">console</span>.log(name)&#125;;
<span class="hljs-built_in">console</span>.log(p.age)<span class="hljs-comment">//undefined</span>
<span class="hljs-built_in">console</span>.log(p.method)<span class="hljs-comment">//undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的代码，我们知道不能给基本类型添加属性和方法。</p>
<h3 data-id="heading-3">基本数据类型的比较是值的比较</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> person1 = <span class="hljs-string">'&#123;&#125;'</span>;
<span class="hljs-keyword">var</span> person2 = <span class="hljs-string">'&#123;&#125;'</span>;
<span class="hljs-built_in">console</span>.log(person1 == person2); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">二.引数据类型</h2>
<p>js中除了上面的基本类型之外就是引用类型了，也可以说就是对象了，Object,Function等（这里注意，Array.Date都被归为了Object类型），它们在栈空间中存的是一个指针，指向的是存在堆空间里面的值。</p>
<h3 data-id="heading-5">引用类型的值是可以改变的</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> o = &#123;<span class="hljs-attr">x</span>:<span class="hljs-number">1</span>&#125;;
o.x = <span class="hljs-number">2</span>;<span class="hljs-comment">//通过修改对象属性值更改对象</span>
o.y = <span class="hljs-number">3</span>;<span class="hljs-comment">//再次更改对象，给它增加一个属性</span>

<span class="hljs-keyword">var</span> a = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
a[<span class="hljs-number">0</span>] = <span class="hljs-number">0</span>;<span class="hljs-comment">//更改数组的一个元素</span>
a[<span class="hljs-number">3</span>] = <span class="hljs-number">4</span>;<span class="hljs-comment">//给数组增加一个元素</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">引用类型可以添加属性和方法</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> person = &#123;&#125;;
person.name = <span class="hljs-string">"change"</span>;
person.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;alert(<span class="hljs-string">"hello"</span>);&#125;
<span class="hljs-built_in">console</span>.log(person.name)<span class="hljs-comment">//change</span>
<span class="hljs-built_in">console</span>.log(person.say)<span class="hljs-comment">//function()&#123;alert("hello");&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">引用类型的赋值是对象引用</h3>
<p>先看以下代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">var</span> a = &#123;&#125;;
<span class="hljs-keyword">var</span> b= a;
a.name = <span class="hljs-string">"change"</span>;
<span class="hljs-built_in">console</span>.log(a.name)<span class="hljs-comment">//change;</span>
<span class="hljs-built_in">console</span>.log(b.name)<span class="hljs-comment">//change</span>
b.age = <span class="hljs-number">29</span>;
<span class="hljs-built_in">console</span>.log(a.age)<span class="hljs-comment">//29</span>
<span class="hljs-built_in">console</span>.log(b.age)<span class="hljs-comment">//29</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当从一个变量向另一个变量赋值引用类型的值时，同样也会将储存在变量中的对象的值复制一份放到为新变量分配的空间中.引用类型保存在变量中的是对象在堆内存中的地址。</p>
<p>所以，与基本数据类型的简单赋值不同，这个值的副本实际上是一个指针，而这个指针指向存储在堆内存的一个对象.那么赋值操作后，两个变量都保存了同一个对象地址，而这两个地址指向了同一个对象.因此，改变其中任何一个变量，都会互相影响。</p>
<h4 data-id="heading-8">引用类型的比较是引用的比较</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> person1 = &#123;&#125;;
<span class="hljs-keyword">var</span> person2 = &#123;&#125;;
<span class="hljs-built_in">console</span>.log(person1 == person2)<span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为什么两个对象看起来一摸一样，但是却不相等呢？</p>
<p>因为引用类型的比较是==引用==的比较，换句话说，就是比较两个对象保存在栈区的指向堆内存的地址是否相同，此时，虽然p1和p2看起来都是一个"&#123;&#125;"，但是他们保存在栈区中的指向堆内存的地址却是不同的，所以两个对象不相等。</p>
<h2 data-id="heading-9">三.基本包装类型(包装对象)：</h2>
<p>先看下以下代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> s1 = <span class="hljs-string">"helloworld"</span>;
<span class="hljs-keyword">var</span> s2 = s1.substr(<span class="hljs-number">4</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面我们说到字符串是基本数据类型，不应该有方法，那为什么这里s1可以调用substr()呢？</p>
<p>通过翻阅js权威指南第3.6章节和高级程序设计第5.6章节我们得知，ECMAScript还提供了三个特殊的引用类型Boolean,String,Number.我们称这三个特殊的引用类型为基本包装类型，也叫包装对象.</p>
<p>也就是说当读取string,boolean和number这三个基本数据类型的时候，后台就会==创建==一个对应的基本包装类型对象，从而让我们能够调用一些方法来操作这些数据.</p>
<p>所以当第二行代码访问s1的时候，后台会自动完成下列操作：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> s1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">String</span>(<span class="hljs-string">"helloworld"</span>);  <span class="hljs-comment">//创建String类型的一个实例；</span>
<span class="hljs-keyword">var</span> s2 = s1.substr(<span class="hljs-number">4</span>);          <span class="hljs-comment">//在实例上调用指定方法；</span>
s1 = <span class="hljs-literal">null</span>;                      <span class="hljs-comment">//销毁这个实例；</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正因为有第三步这个销毁的动作，所以你应该能够明白为什么基本数据类型不可以添加属性和方法，这也正是基本装包类型和引用类型主要区别：对象的生存期</p>
<ul>
<li>使用new操作符创建的引用类型的实例，在执行流离开当前作用域之前都是一直保存在内存中</li>
<li>而自动创建的基本包装类型的对象，则只存在于一行代码的执行瞬间，然后立即被销毁.</li>
</ul>
<h2 data-id="heading-10">四.常见问题梳理</h2>
<h3 data-id="heading-11">undefind,null,NaN,void 0比较</h3>
<ul>
<li>underfind ：缺少值，此处应该有一个值，转化为数字后变成 NaN</li>
<li>null : 定义了但是为空,转化为数字化后变成0</li>
<li>void 0 : 等于undefined</li>
<li>NaN : 代表非数字值的特殊值。该属性用于指示某个值不是数字。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">"undefined == null"</span>, <span class="hljs-literal">undefined</span> == <span class="hljs-literal">null</span>);     <span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"&#123;&#125; == &#123;&#125;"</span>, &#123;&#125; == &#123;&#125;);                       <span class="hljs-comment">//false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"NaN == NaN"</span>, <span class="hljs-literal">NaN</span> == <span class="hljs-literal">NaN</span>);                   <span class="hljs-comment">//false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"0 == undefined"</span>, <span class="hljs-number">0</span> == <span class="hljs-literal">undefined</span>);           <span class="hljs-comment">//false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"void 0 == null"</span>, <span class="hljs-keyword">void</span> <span class="hljs-number">0</span> == <span class="hljs-literal">null</span>);           <span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">为何使用void 0取代undefined？</h3>
<p>注意 : void是一元运算符，出现在操作数的左边，操作数可以是任意类型的值，void右边的表达式可以是带括号形式（例如：void(0)），也可以是不带括号的形式（例如：void 0）。</p>
<ul>
<li>
<p>在ES5的全局环境中，undefined是只读的。而在局部作用域中，undefined是可变的，所以推荐使用void 0获取undefind。</p>
</li>
<li>
<p>使用void 0比使用undefined能够减少3个字节</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">><span class="hljs-string">"undefined"</span>.length
<span class="hljs-comment">//9</span>
><span class="hljs-string">"void 0"</span>.length
<span class="hljs-comment">//6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>undefined并不是javascript中的保留字，我们可以使用undefined作为变量名字，然后给它赋值。void 0输出唯一的结果undefined，保证了不变性。</li>
</ul>
<h3 data-id="heading-13">为何 0.1+0.2 == 0.3 为false？</h3>
<p>JS 数字类型只有number类型，number类型相当于其他强类型语言中的double类型(双精度浮点型)，不区分浮点型和整数型。</p>
<p>由于Js的所有数字类型都是双精度浮点型(64位)采用 IEEE754 标准 64位二进制数表示一个number数字</p>
<p>其中 <strong>64位 = 1位符号位 + 11位指数位 + 52位小数位</strong></p>
<p>浮点数的运算精度丢失问题就是因为，浮点数转化为该标准的二进制的过程中，并不能直接转化，只能转化为一个近似的值，所以有精度的丢失</p>
<p>推荐解决办法</p>
<ul>
<li>将小数的运算转化为整数的运算，使用Math.floor()：向下取整，Math.ceil()：向上取整</li>
<li>检测最小精度差 console.log( Math.abs(0.1 + 0.2 - 0.3) <= Number.EPSILON);</li>
</ul>
<h3 data-id="heading-14">如何检测+0和-0？</h3>
<p>除了NaN，JS还有两个特殊的数字</p>
<ul>
<li>Infinity，无穷大；</li>
<li>-Infinity，负无穷大。</li>
</ul>
<p>JavaScript 中有 +0 和 -0，在加法类运算中它们没有区别，但是除法的场合则需要特别留意区分。
“忘记检测除以 -0，而得到负无穷大”的情况经常会导致错误，</p>
<p>而区分 +0 和 -0 的方式，正是检测 1/x 是 Infinity 还是 -Infinity。</p>
<h3 data-id="heading-15">字符串的最大长度是多少？</h3>
<p>String 用于表示文本数据。String 有最大长度是 2^53 - 1，这在一般开发中都是够用的，</p>
<p>但是有趣的是，这个所谓最大长度，并不完全是你理解中的字符数。因为 String 的意义并非“字符串”，而是字符串的 UTF16 编码，我们字符串的操作 charAt、charCodeAt、length 等方法针对的都是 UTF16 编码。所以，字符串的最大长度，实际上是受字符串的编码长度影响的。</p>
<pre><code class="copyable">Note：现行的字符集国际标准，字符是以 Unicode 的方式表示的，
每一个 Unicode 的码点表示一个字符，
理论上，Unicode 的范围是无限的。
UTF 是 Unicode 的编码方式，规定了码点在计算机中的表示方法，
常见的有 UTF16 和 UTF8。 Unicode 的码点通常用 U+??? 来表示，
其中 ??? 是十六进制的码点值。 
0-65536（U+0000 - U+FFFF）的码点被称为基本字符区域（BMP）。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是说length并不是直接返回直觉上字符串的长度，而是返回在Unicode编码状态下编码码点的长度。</p>
<p>比如说一个韩文字符的length是2。</p>
<hr>
<h3 data-id="heading-16">写在最后</h3>
<p>感谢你能看到这里，不妨点个赞再走呀~~</p></div>  
</div>
            