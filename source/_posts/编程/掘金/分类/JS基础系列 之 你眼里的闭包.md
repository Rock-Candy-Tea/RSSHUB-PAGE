
---
title: 'JS基础系列 之 你眼里的闭包'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f62faa78971a45c788b6c79f49371613~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 00:35:01 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f62faa78971a45c788b6c79f49371613~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>⾼级程序设计三中描述：闭包是指有权访问另外⼀个函数作⽤域中的变量的函数。可以理解为(能够读取其他 函数内部变量的函数)</p>
<p>看似简单的单一概念，其实它还涉及到执行上下文 、作用域、作用链、内存管理的等其他知识点。再我们看 <strong>闭包</strong> 前，先了解一下其他与之相关的知识点。走起......</p>
<p>开胃菜 -- 脑图</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f62faa78971a45c788b6c79f49371613~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">执行上下文</h2>
<p>为什么先了解 执行上下文？我认为，只有先 摸清 执行上下文，才能更好的理解 变量提升、作用域、闭包等概念。let's go.....</p>
<p> 先 猜猜 以下代码输出结果是什么</p>
<pre><code class="copyable">myName()
var name;
function myName() &#123;
    console.log("myName is .....")
&#125;
console.log(name)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>what？感觉这是要报错的节奏哇？nonono..... 并没有， 先输出**"myName is ....."**，后输出：**undefined。**why？为什么，这不科学！</p>
<p>okay，这里其实是变量提升了。纳尼~~~<strong>变量提升</strong>，是什么鬼？</p>
<p>所谓 “变量提升” 是代码函数、变量的声明会被移动到代码的最最最最前面，<strong>在编译阶段 Javascript引擎将其存入内存中</strong>。没错，一段 js 代码在执行之前是被引擎编译，先<strong>编译</strong>阶段完成后，再进入<strong>执行</strong>阶段。</p>
<p><strong>执行上下文是</strong>Javascript<strong>执行一段代码时的运行环境</strong></p>
<p>我们看看执行流程图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/353b5c801f7c4c40924303d19a889efa~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行上下文中存在<strong>环境变量</strong>对象，该对象就是保存变量提升的内容。so，“变量提升”由此而来。让我们把上述代码拆分两段来分析。</p>
<h3 data-id="heading-2">编译阶段</h3>
<pre><code class="copyable">// 声明部分
var name = undefined;
function myName() &#123;
    console.log("myName is .....")
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们分析一下编译过程：</p>
<p>var name  通过 var 声明 Javascript引擎 创建一个名为 name 的属性，并使用 undefined 对其进行赋值；</p>
<p>function myName() Javascript引擎 发现一个通过 function 定义的函数，所以将函数存储到<strong>堆</strong>中，并在环境中创建一个 myName 的属性；</p>
<h3 data-id="heading-3">执行阶段</h3>
<pre><code class="copyable">// 可执行部分
myName()
console.log(name)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Javascript引擎开始执行  “可执行代码”， 按照顺序，逐行执行，我们看看如下执行过程：</p>
<p>myName() 执行 myName 函数时，Javascript引擎开始从变量对象环境中查找函数，变量对象中存在该函数引用，Javascript引擎执行该函数，输出： "myName is ....." 结果。</p>
<p>console.log(name)  打印 name 信息，Javascript引擎继续从变量对象环境中查找，变量对象中存在 name 变量，值为 undefined，这时候输出 undefined。</p>
<p><strong>呃.....这里有个问题，如果出现 相同 函数、变量如何是好？</strong></p>
<pre><code class="copyable">function myName() &#123;
    console.log("myName is .....")
&#125;
myName()
function myName() &#123;
    console.log("胖圈圈")
&#125;
myName()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>来分析一下执行流程：</p>
<p>**首先编译阶段。**遇到第一个 myName 函数 存到变量环境，遇到 第二个 myName 函数，发现已经存在，那就直接覆盖。环境变量只存了第一个 myName 函数。</p>
<p>**再来执行阶段。**先执行第一个 myName 函数，由于是从变量环境查找的 myName 函数 所以最终调用的是第二个函数。第二次执行走相同流程，输出结果都是 "胖圈圈"。</p>
<h2 data-id="heading-4">调用栈</h2>
<p>前面我们说 每调用一个函数， Javascript引擎会为其创建执行上下文，并把该执行上下文加入 调用栈（执行栈），然后开始执行函数代码。</p>
<p>一般来说创建执行上下文有三种情况：</p>
<ol>
<li>全局上下文，在整个页面的生命周期内，仅此一份。</li>
<li>调用函数的时候，函数体被编译，并创建执行上下文，函数执行结束之后执行上下文会被销毁。</li>
<li>当使用eval 函数的时候，eval 代码也会被编译，并创建执行上下文。</li>
</ol>
<p>我们看一段代码：</p>
<pre><code class="copyable">var lastName = "xiaotuan";
function getName() &#123;
    var firstName = "yu";
    return firstName + lastName;
&#125;
getName();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看都看了，分析一下吧：</p>
<p>首先从 <strong>全局执行上下文</strong> 中，提出 getName函数代码。</p>
<p>其次，对函数代码进行编译，并创建该函数的<strong>执行上下文</strong>和<strong>可执行代码。</strong></p>
<p>最后执行代码输出结果。</p>
<p>也就是说，Javascript引擎会管理 很多很多很多 的执行上下文，怎么管理呢？对了，就是通过**一种叫做 栈（Stack） 的数据结构来管理。**栈，我们这里不详解。 栈有什么特点呢？</p>
<p>单行线，栈中元素满足后进先出的特点。</p>
<p>我们看一段感情线略微复杂de代码：</p>
<pre><code class="copyable">var lastName = "xiaotuan";function getLastName() &#123;
    return lastName;
&#125;
function getFullName() &#123;
    var firstName = "yu";
    var res = getLastName();
    return firstName + res;&#125;
getFullName();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>来分析一下吧：</p>
<h3 data-id="heading-5">执行过程</h3>
<p>第一步，<strong>创建全局中下文，push 到 栈底</strong>，变量 lastName，函数 getLastName、函数 getFullName都保存到了全局上下文的变量环境对象中。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b0f0e280d5a4b1b942293348b83e006~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>全局执行上下文进栈后，Javascript引擎开始执行全局代码，首先执行  lastName = "xiaotuan" 赋值操作，执行语句将 全局上下文中变量环境对象中 lastName 的值设置 为 "xiaotuan"。</p>
<p>第二步，调用 getFullName 函数，当调用函数时，创建其执行上下文，将该函数上下文 push 到执行栈中。执行操作，将 firstName 变量由 undefined，变为 "yu" 。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6392e29dfad438a8c0e3470409e1c4d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>第三步，调用  getLastName 函数，同样创建执行上下文，加入执行栈中。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d19de2e5cbe344c9877c54532a302cbd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当 getLastName 函数返回时，该函数执行上下文就会从 **栈顶弹出，**并将 res 的值设置为 getLastName 函数的返回值。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6392e29dfad438a8c0e3470409e1c4d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>跟着 getFullName 函数执行相加并返回。getFullName 函数的执行上下文也会从 **栈顶弹出，**现在就剩下全局上下文了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b0f0e280d5a4b1b942293348b83e006~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>okay。到此，执行栈流程结束了。**调用栈是 JavaScript 引擎追踪函数执行的一个机制。**通过调用栈能够追踪函数之间的调用关系。</p>
<h3 data-id="heading-6">栈溢出 （Stack Overflow）</h3>
<p>注意：栈是有大小的。因为 电脑不可能把所有 内存都分配给你，JavaScript 引擎感到栈太多，有危险时，就会报 栈溢出 错误。这种情况，在循环、递归代码中最常遇到。</p>
<p><strong>超过了最大栈调用大小（Maximum call stack size exceeded）错误信息</strong></p>
<h2 data-id="heading-7">作用域 （scope）</h2>
<p>为什么 JavaScript 会存在 **“变量提升”**呢？我们需要从作用域入手。</p>
<p><strong>作用域是指在程序中定义变量的区域，作用域控制变量和函数的可见性和生命周期。</strong></p>
<p>ES6之前，ES的作用域只有两种：全局作用域 和 函数作用域。</p>
<ul>
<li><strong>全局作用域</strong> 中的对象在代码任何地方都能访问，其生命周期伴随着页面的生命周期。</li>
<li><strong>函数作用域</strong> 就是在函数内部定义的变量或者函数，并且定义的变量或者函数只能在函数内部被访问。函数执行结束之后，函数内部定义的变量会被销毁（闭包除外）。</li>
</ul>
<p>ES6之后，支持了<strong>块级作用域</strong>，块级作用域就是使用一对大括号包裹的一段代码，比如函数、if语句、循环语句，甚至单独的 &#123;&#125; 大括号都是块级作用域。</p>
<p>再回到**变量提升，**变量提升会带来如下问题：</p>
<ul>
<li>变量容易被覆盖</li>
<li>
<pre><code class="copyable">  // 变量内容覆盖
  function test() &#123;
      var name = 1;
      if (true) &#123;
          var name = 2;
          console.log(name); // 2
      &#125;
      console.log(name); // 2
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>这里在 执行上下文 变量环境中先创建 name 变量 赋值1，继续执行，发现 变量环境存在 name 变量，值为2，变量值被覆盖了，输出结果是：2，2。</p>
<ul>
<li>本应销毁的变量没有被销毁</li>
<li>
<pre><code class="copyable">  function test() &#123;
      for (var i = 0; i < 7; i++) &#123;&#125;
      console.log(i); // 7
  &#125;
  
  test()
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>这里 for 循环结束后并没有被销毁，结果打印出 7。变量提升导致，在创建执行上下文时，变量 i 已经被提升，所以 i 并没有被销毁。</p>
<p>**问题如何解决呢？**就看 ES6 带来的 let 和 const 关键字，它们的到来 有了 块级作用域。二者的区别就是 const 声明的变量值不可改变。我们将上面示例改改，看结果：</p>
<pre><code class="copyable">function test() &#123;
    let name = 1;
    if (true) &#123;
        let name = 2;
        console.log(name); // 2
    &#125;
    console.log(name); // 1
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相同的代码，我们只是 将 var 改成 let，输出结果是：2，1。JavaScript引擎不会把 if 块中通过 let 声明的变量存放到变量环境中，而是存在词法环境栈中，所以不会提升到全函数可见。</p>
<p>有一个问题，就是 ES6 如何实现即支持变量提升，又支持作用域块呢？我们到作用域链中寻找答案。</p>
<h2 data-id="heading-8">作用域链</h2>
<p>我们通过分析下面代码，来看看 JavaScript 引擎如何通过 变量环境、词法环境来查找变量。其实也就是作用域链生产过程。</p>
<pre><code class="copyable">var name = "李星星";

function a() &#123;
    var name = "饭团团";
    b();
    console.log(name) // 饭团团
&#125;

function b() &#123;
    console.log(name) // 李星星
&#125;

a();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>编译过程</strong></p>
<p>全局执行上下文的环境变量存在 name 变量值为 李星星、a 函数</p>
<p>a 函数执行上下文的环境变量存在 name变量值为 饭团团</p>
<p><strong>执行过程</strong></p>
<p>执行 a 函数，<strong>当代码使用一个变量时</strong>，JavaScript 引擎先从 <strong>“当前的执行上下文”</strong> 找变量，然后 找到 饭团团，打印出来。</p>
<p>执行 b 函数，JavaScript 引擎在 <strong>“当前的执行上下文”</strong> 中没有找到变量，这时它会去外部引用的执行上下文中查找，我们把这个外部引用称做 <strong>outer</strong>。outer 现在指向的是 全局执行上下文，所以找到 name = 李星星，打印输出。</p>
<p>由此我们可以总结出来，a 函数、b 函数的<strong>outer</strong>都是指向全局执行上下文，如果函数中使用了外部变量，那么 JavaScript 引擎会去 引用的outer，这里是全局执行上下文中查找。我们把这个查找的链条叫做<strong>作用域链。</strong></p>
<p><strong>but，<strong>a 函数调用的b函数，为什么b函数的outer是全局执行下文，而不是a函数的执行上下文呢？这里，我们有涉及到前面提过的</strong>词法作用域。</strong></p>
<h3 data-id="heading-9">词法作用域</h3>
<p><strong>词法作用域就是指作用域是由代码中函数声明的位置来决定的，所以词法作用域是静态的作用域，通过它就能够预测代码在执行过程中如何查找标识符。</strong></p>
<p>我们通过代码来看：</p>
<pre><code class="copyable">function a() &#123;
    function b() &#123;
        function c() &#123;
            ......
        &#125;    
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>****JavaScript 作用域链是由词法作用域决定的。****所以这里作用域链的顺序是：c 作用域 —> b 作用域 —> a 作用域 —> 全局作用域。**词法作用域是代码编译阶段就决定好的，和函数是怎么调用的没有关系。**c 和 b的上级作用域都是 a， 如果 c 、b 中使用了他们没有定义的变量，那么它们会去到全局作用域查找。</p>
<h2 data-id="heading-10">主角--闭包</h2>
<p>回到最开始，什么是闭包？你是否已经有答案？再来一个示例，理解一下</p>
<pre><code class="copyable">function test() &#123;
    var name = 'a';
    let b = 'b';
    const c = 'c';
    var show = &#123;
        getName: function() &#123;
            console.log(b); // b            return name;        &#125;,
        setName: function(newName) &#123;
            name = newName;
        &#125;    &#125;

    return show;
&#125;

var testObj = test();testObj.setName("闭包");
testObj.getName(); // 闭包
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先，当执行到 test 函数内部的 return show这行代码时，show 对象 包含了 getName、setName 方法，并且在方法内部使用了 name、b  这两个变量。</p>
<p>**根据词法作用域的规则，内部函数 getName、setName 总是可以访问它们外部函数 test 中的变量，**所以，当 shwo 对象返回给全局变量testObj时，虽然 test 函数已经执行结束，但getName、setName 方法依然可以使用 test 函数 中的 name、b 变量，它们保存在内存中。</p>
<p>我们把这些变量的集合称为**“闭包”。** JavaScript 引擎先从 “当前执行上下文 ---> test 函数闭包 ---> 全局执行上下文” 的顺序查找 name 变量。</p>
<p>至此，闭包的概念，经过我们都捋了一边。but，还有一个问题，闭包内的变量存在于内存中，如果使用不正确，很容易会造成内存泄露。那么，我们又需要关注一下，闭包如何回收。</p>
<h2 data-id="heading-11">内存管理</h2>
<p>这里先初略的写一下相关内容，笔者也还没深入学习这块 “姿势”，后期深入学习后再出一篇关于内存管理、垃圾回收机制的文章。</p>
<p>在我们知识体系里必须知道，闭包跟内存泄露、垃圾回收有一定关联。</p></div>  
</div>
            