
---
title: '一步让你区分理解call,apply,bind'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6268'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 00:10:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=6268'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作用：
call,apply,bind 都是改变this指向的</p>
<p>语法：</p>
<pre><code class="copyable"> func.call(thisagr,param1,param1,...)
 func.apply(thisagr,[param1,param1,...])
 func.bind(thisagr,param1,param1,...)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-0">1.call：</h2>
<h3 data-id="heading-1">1.1 call第一个参数，就是要变成的this的对象</h3>
<pre><code class="copyable"> var obj = &#123; name: 'psg' &#125;;
     function fn(num1, num2) &#123;
       console.log(num1 + num2);
       console.log("this指向:" + this, "num1:" + num1, "num2:" + num2)
   &#125;
   fn(100, 200);//this指向window, num1=100, num2=200
   fn.call(100, 200);////this指向100， num1=200, num2=undefined
   fn.call(obj, 100, 200);//this指向obj,  num1=100, num2=200
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">1.2严格模式，非严格模式下的this指向</h3>
<p>在非严格模式下:this为null，undefined时，this指向window
在严格模式下：传谁this就是谁，不传this就是undefined</p>
<pre><code class="copyable">  // 严格模式
  fn.call(); //this指向undefined
  fn.call(null); //this指向null
  fn.call(undefined); //this指向undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">2.apply：</h2>
<p>apply 于call 类似，只是不用于的语法</p>
<p>call传参数是逗号分割，一个一个传入：fn.call（obj，arg1,agr2)</p>
<p>apply传参数是用一个数组传：fn.apply(obj,[agr1,agr2])</p>
<pre><code class="copyable">var obj1 = &#123; name: 'psg' &#125;;
    function fn1(num1, num2) &#123;
      console.log(num1 + num2);
      console.log("this指向:" + this, "num1:" + num1, "num2:" + num2)
   &#125;
   
    fn1.call(obj1, 100, 200);
    fn1.apply(obj1, [100, 200]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">3.bind：</h2>
<p>bind 于call类似，语法一致，但是bind体现了js的预处理</p>
<p>bind 不会执行函数，会有一个返回值（返回值是函数的拷贝）</p>
<p>预处理：实现把fn的this改变成我们想要的结果，并且把对象的参数也准备了，要用的时候，直接执行就行了</p>
<pre><code class="copyable">var obj1 = &#123; name: 'psg' &#125;;
    function fn1(num1, num2) &#123;
      console.log(num1 + num2);
      console.log("this指向:" + this, "num1:" + num1, "num2:" + num2)
    &#125;
    fn1.call(obj1, 100, 200);
    fn1.bind(obj1, 100, 200);
    
    //bind只是改变了fn中的this为obj，并且给fn传递了两个参数值，但是此时并没有给fn这个函数执行。
   // 但是，执行bind会有一个返回值，这个返回值myFn就是我们把fn的this改变后的那个结果！！！


    var myFn = fn1.bind(obj1, 100, 200);
    myFn();  //执行函数
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">3.1手动实现bind</h3>
<h2 data-id="heading-6">4.小结区别：</h2>
<p>call于apply区别：</p>
<p>语法不同，传给函数的参数写法不同</p>
<p>call于bind区别：</p>
<p>1.执行：</p>
<p>call，apply改变了this执行，立马执行函数</p>
<p>bind 返回了this指向后的函数，没有执行函数</p>
<p> </p>
<h2 data-id="heading-7">5.手动模拟实现call：</h2>
<p>主要思路如上，不一样的是要通过arguments取出除第一位之外的所有参数放到一个数组里，然后通过展开运算符给要执行的函数或方法传参</p>
<p>1.改变this指向，给传递过来的对象添加属性，把this指向这个属性，然后指向方法，删除属性</p>
<p>2.用arguments接受传递过来的参数</p>
<pre><code class="copyable">Function.prototype.myCall = function (con) &#123;
 con = new Object(con) || window || global;//1.没有参数时，指向window
   con.fun = this;   //2.给目标对象新建一个属性，绑定这个函数
   let arr =[];  //3.新建一个空数组
   for (let i = 1; i < arguments.length; i++) &#123;
        arr.push(arguments[i]);
   &#125;
   con.fun(...arr);  //4.运行一下
   delete con.fun;   //5.删除目标对象上的fun属性，不删除会越来越多
 &#125;
  var obj = &#123; name: 12 &#125;
  function fn(num1, num2) &#123;
    console.log("this:" + this);
    console.log("num1:" + num1);
    console.log("num2:" + num2);
  &#125;
  fn.myCall(100, 200);
  fn.myCall(obj, 100, 200);
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<p>方法二：eval 将原始函数转换为字符串，再将其中的this替换为目标对象</p>
<p>1.arguments代指函数接收的所有参数，它是一个类数组，不能用Array的方法</p>
<p>第一位是this指向，后面的才是参数</p>
<ol start="2">
<li>eavl() 可以接受一个字符串str作为参数，并把这个参数作为脚本代码来执行</li>
</ol>
<pre><code class="copyable">  var name = 'cao1';
  var obj = &#123;name: 'cao2'&#125;;
  Function.prototype.call1_ = function (obj) &#123;
      var arr = []
      for (var i = 1, len = arguments.length; i < len; i++) &#123;
        arr.push("arguments[" + i + "]")
      &#125;
      obj.fn = this;
      eval("obj.fn(" + arr + ")");//2.执行方法  eval(string)会做运算  eval("var a=1");
      delete obj.fn;
    &#125;
    function fn2(a, b, c) &#123;
      console.log(a + b + c + this.name);
    &#125;;
    fn2.call1_(obj, 1, 2, 3);
    fn2.call1_(obj, "我的", "名字", "是");
    // 如果是args.push(arguments[i])报错，因为传递的是字符串这一步我们提前将字符串进行了解析 等于 eval("obj.fn(我的,名字,是)")
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">6.开发使用</h2>
<h4 data-id="heading-9">6.1 改变this指向</h4>
<h4 data-id="heading-10">6.2 数据类型检测</h4>
<pre><code class="copyable">function type(obj) &#123;
return  Object.prototype.toString.call(obj)[1];
&#125;;
 
type([123]);//Array
type('123');//String
type(123);//Number
type(null);//Null
type(undefined);//Undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">6.2数组取最大值，最小值</h4>
<pre><code class="copyable">var arr = [11, 1, 0, 2, 3, 5];
var max1 = Math.max.call(null, ...arr);
var max2 = Math.max.apply(null, arr);


var min1 = Math.min.call(null, ...arr);
var min2 = Math.min.apply(null, arr);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">6.3函数arguments类数组操作</h4>
<pre><code class="copyable">var fn = function () &#123;
    var arr = Array.prototype.slice.call(arguments);
    console.log(arr); //[1, 2, 3, 4]
&#125;;
fn(1, 2, 3, 4);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            