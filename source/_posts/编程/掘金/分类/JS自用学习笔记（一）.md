
---
title: 'JS自用学习笔记（一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6095'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 00:25:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=6095'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">对象的属性和方法</h2>
<h3 data-id="heading-1">Array 对象属性</h3>
<p><code>Array</code>  用于单个的变量中存储多个值</p>
<pre><code class="copyable">new Array();
new Array(size);    //size是期望的数组元素个数
new Array(element0, element1, ..., elementn)   //参数列表
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<h4 data-id="heading-2">对象属性</h4>
</li>
</ul>
<ol>
<li><code>constructor</code> 返回对创建此对象的数组函数的引用。</li>
</ol>
<pre><code class="copyable">array.constructor
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>数组 constructor 属性返回 <code>function Array() &#123; [native code] &#125;</code></li>
<li>数字 constructor 属性返回 <code>function Number() &#123; [native code] &#125;</code></li>
<li>字符串 constructor 属性返回 <code>function String() &#123; [native code] &#125;</code></li>
</ul>
<ol start="2">
<li><code>length</code> 设置或返回数组中元素的数目。</li>
</ol>
<pre><code class="copyable">array.length
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li><code>prototype</code> 使您有能力向对象添加属性和方法。</li>
</ol>
<pre><code class="copyable">Array.prototype.name=value
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<h4 data-id="heading-3">对象方法</h4>
</li>
</ul>
<ol>
<li><code>concat()</code> 连接两个或更多的数组，并返回结果。</li>
</ol>
<pre><code class="copyable"><script type="text/javascript">
var a = [1,2,3];
document.write(a.concat(4,5));
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">1,2,3,4,5
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><code>join()</code> 把数组的所有元素放入一个字符串。元素通过指定的分隔符进行分隔。</li>
</ol>
<pre><code class="copyable"><script type="text/javascript">
var arr = new Array(3)
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"
arr.join()      //arr:George,John,Thomas
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li><code>pop()</code> 删除并返回数组的最后一个元素</li>
</ol>
<pre><code class="copyable">var arr = new Array(3)
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"

arr.pop()  //arr:George,John
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li><code>push()</code> 向数组的末尾添加一个或更多元素，并返回新的长度。</li>
</ol>
<pre><code class="copyable">var arr = new Array(3)
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"

arr.push("James")   //George,John,Thomas,James
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li><code>reverse()</code> 颠倒数组中元素的顺序。</li>
</ol>
<pre><code class="copyable">var arr = new Array(3)
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"

arr.reverse()  //Thomas,John,George
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li><code>shift()</code> 删除并返回数组的第一个元素</li>
</ol>
<pre><code class="copyable">var arr = new Array(3)
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"

arr.shift()     //John,Thomas
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="7">
<li><code>slice()</code> 从某个已有的数组返回选定的元素</li>
</ol>
<pre><code class="copyable">var arr = new Array(3)
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"

arr.slice(1)   //John,Thomas
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="8">
<li><code>sort()</code> 对数组的元素进行排序</li>
</ol>
<pre><code class="copyable">var arr = new Array(6)
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"
arr[3] = "James"
arr[4] = "Adrew"
arr[5] = "Martin"

document.write(arr.sort())  //Adrew,George,James,John,Martin,Thomas
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="9">
<li><code>splice()</code> 删除元素，并向数组添加新元素。</li>
</ol>
<pre><code class="copyable">var arr = new Array(6)
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"
arr[3] = "James"
arr[4] = "Adrew"
arr[5] = "Martin"

arr.splice(2,0,"William")  //George,John,William,Thomas,James,Adrew,Martin
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="10">
<li><code>toString()</code> 把数组转换为字符串，并返回结果。</li>
</ol>
<pre><code class="copyable">var arr = new Array(3)
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"

arr.toString()  //arr:George,John,Thomas
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="11">
<li><code>toLocaleString()</code> 把数组转换为本地数组，并返回结果。</li>
</ol>
<pre><code class="copyable">var arr = new Array(3)
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"

(
arr.toLocaleString()    //arr:George, John, Thomas
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="12">
<li><code>unshift()</code> 向数组的开头添加一个或更多元素，并返回新的长度。</li>
</ol>
<pre><code class="copyable">arrayObject.unshift(newelement1,newelement2,....,newelementX)
<span class="copy-code-btn">复制代码</span></code></pre>

















<table><thead><tr><th>newelement1</th><th>必需。向数组添加的第一个元素。</th></tr></thead><tbody><tr><td>newelement2</td><td>可选。向数组添加的第二个元素。</td></tr><tr><td>newelementX</td><td>可选。可添加若干个元素。</td></tr></tbody></table>
<pre><code class="copyable">var arr = new Array()
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"

arr.unshift("William")   //arr:William,George,John,Thomas
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">Boolean 对象属性</h3>
<p><code>Boolean</code> 对象表示两个值："true" 或 "false"</p>
<pre><code class="copyable">new Boolean(value);//构造函数
Boolean(value);//转换函数
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">Boolean 对象属性</h4>
<ul>
<li>constructor 返回对创建此对象的 Boolean 函数的引用</li>
<li>prototype 使您有能力向对象添加属性和方法。</li>
</ul>
<h4 data-id="heading-6">Boolean 对象方法</h4>
<ol>
<li><code>toSource()</code>  返回该对象的源代码。</li>
</ol>
<pre><code class="copyable">function employee(name,job,born)
&#123;
this.name=name;
this.job=job;
this.born=born;
&#125;

var bill=new employee("Bill Gates","Engineer",1985);

document.write(bill.toSource());
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>结果</em></p>
<pre><code class="copyable">(&#123;name:"Bill Gates", job:"Engineer", born:1985&#125;) 
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><code>toString()</code> 把逻辑值转换为字符串，并返回结果。</li>
</ol>
<pre><code class="copyable">var boo = new Boolean(true)
document.write(boo.toString())    //true
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li><code>valueOf()</code> 返回 Boolean 对象的原始值。</li>
</ol>
<pre><code class="copyable">var bool = new Boolean(false);
document.write(bool.valueOf());
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">Class类</h3>
<p>不使用关键字 function 来对其初始化，而是使用关键字 class</p>
<pre><code class="copyable">class Car &#123;  // 创建类
  constructor(brand) &#123;  // 类构造方法
    this.carname = brand;  // 类主体/属性
  &#125;
&#125;
mycar = new Car("Ford");  // 创建 Car 类的对象
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<h4 data-id="heading-8">Class 方法 (不常用)</h4>
</li>
</ul>
<ol>
<li><code>constructor()</code>用于创建和初始化在类中创建的对象的特殊方法。</li>
</ol>
<ul>
<li>
<h4 data-id="heading-9">Class关键字</h4>
</li>
</ul>
<ol>
<li><code>extends</code> 扩展类（继承）</li>
</ol>
<pre><code class="copyable"><p id="demo"></p>
<script>
class Car &#123;
  constructor(brand) &#123;
    this.carname = brand;
  &#125;
  present() &#123;
    return 'I have a ' + this.carname;
  &#125;
&#125;

class Model extends Car &#123;
  constructor(brand, mod) &#123;
    super(brand);
    this.model = mod;
  &#125;
  show() &#123;
    return this.present() + ', it is a ' + this.model;
  &#125;
&#125;

mycar = new Model("Ford", "Mustang");
document.getElementById("demo").innerHTML = mycar.show();
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><code>static</code> 为类定义静态方法。</li>
</ol>
<pre><code class="copyable"><p id="demo"></p>
<script>
class Car &#123;
  constructor(brand) &#123;
    this.carname = brand;
  &#125;
  static hello() &#123;  // static 方法
    return "Hello!!";
  &#125;
&#125;

mycar = new Car("Tesla");
document.getElementById("demo").innerHTML = Car.hello();
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li><code>super</code> 引用父类。</li>
</ol>
<pre><code class="copyable"><p id="demo"></p>
<script>
class Car &#123;
  constructor(brand) &#123;
    this.carname = brand;
  &#125;
  present() &#123;
    return 'I have a ' + this.carname;
  &#125;
&#125;

class Model extends Car &#123;
  constructor(brand, mod) &#123;
    super(brand);
    this.model = mod;
  &#125;
  show() &#123;
    return this.present() + ', it is a ' + this.model;
  &#125;
&#125;
mycar = new Model("Tesla", "Model3");
document.getElementById("demo").innerHTML = mycar.show();
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">Date 对象</h3>
<ul>
<li>
<h4 data-id="heading-11">Date 对象属性</h4>
</li>
</ul>
<p><code>constructor</code> 返回对创建此对象的 Date 函数的引用。
<code>prototype</code> 使您有能力向对象添加属性和方法。</p>
<ul>
<li>
<h4 data-id="heading-12">Date 方法</h4>
</li>
</ul>
<p>返回当前时间</p>
<ol>
<li><code>Date()</code> 返回当日的日期和时间。</li>
<li><code>getDate()</code> 从 Date 对象返回一个月中的某一天 (1 ~ 31)。</li>
<li><code>getDay()</code> 从 Date 对象返回一周中的某一天 (0 ~ 6)。</li>
<li><code>getMonth()</code> 从 Date 对象返回月份 (0 ~ 11)。</li>
<li><code>getFullYear()</code> 从 Date 对象以四位数字返回年份。</li>
<li><code>getHours()</code> 返回 Date 对象的小时 (0 ~ 23)。</li>
<li><code>getMinutes()</code> 返回 Date 对象的分钟 (0 ~ 59)</li>
<li><code>getSeconds()</code> 返回 Date 对象的秒数 (0 ~ 59)</li>
<li><code>getMilliseconds()</code> 返回 Date 对象的毫秒(0 ~ 999)。</li>
<li><code>getTime()</code> 返回 1970 年 1 月 1 日至今的毫秒数。</li>
<li><code>getTimezoneOffset()</code> 返回本地时间与格林威治标准时间 (GMT) 的分钟差。</li>
</ol>
<p>设置时间
12. <code>setDate()</code> 设置 Date 对象中月的某一天 (1 ~ 31)
13. <code>setMonth()</code> 设置 Date 对象中月份 (0 ~ 11)。
14. <code>setFullYear()</code> 设置 Date 对象中的年份（四位数字）。
15. <code>toSource()</code> 返回该对象的源代码。
转为字符串
16. <code>toString()</code> 把 Date 对象转换为字符串
17. <code>toTimeString()</code> 把 Date 对象的时间部分转换为字符串。
18. <code>toDateString()</code> 把 Date 对象的日期部分转换为字符串。
19. <code>toLocaleString()</code> 根据本地时间格式，把 Date 对象转换为字符串
20. <code>toLocaleTimeString()</code> 根据本地时间格式，把 Date 对象的时间部分转换为字符串。
21. <code>toLocaleDateString()</code> 根据本地时间格式，把 Date 对象的日期部分转换为字符串。
时间时间
22. <code>UTC()</code>  根据世界时返回 1970 年 1 月 1 日 到指定日期的毫秒数。</p>
<ul>
<li>toUTCString() 根据世界时，把 Date 对象转换为字符串</li>
</ul>
<p>关键字+UTC+方法（）</p>
<h3 data-id="heading-13">Global  全局</h3>
<ul>
<li>
<h4 data-id="heading-14">顶层函数（全局函数）</h4>
</li>
</ul>
<ol>
<li><code>decodeURI()</code> 解码某个编码的 URI。</li>
<li><code>encodeURI()</code> 把字符串编码为 URI。</li>
</ol>
<pre><code class="copyable"><script type="text/javascript">
  var test1="http://www.w3school.com.cn/My first/"
  document.write(encodeURI(test1)+ "<br />")
  document.write(decodeURI(test1))
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>结果：</em></p>
<pre><code class="copyable">http://www.w3school.com.cn/My%20first/\
http://www.w3school.com.cn/My first/
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li><code>decodeURIComponent()</code> 解码一个编码的 URI 组件。</li>
<li><code>encodeURIComponent()</code> 把字符串编码为 URI 组件。</li>
</ol>
<pre><code class="copyable"><script type="text/javascript">
  var test1="http://www.w3school.com.cn/My first/"
  document.write(encodeURIComponent(test1)+ "<br />")
  document.write(decodeURIComponent(test1))
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>结果</em></p>
<pre><code class="copyable">http%3A%2F%2Fwww.w3school.com.cn%2FMy%20first%2F
http://www.w3school.com.cn/My first/
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li><code>escape()</code> 对字符串进行编码。 十六进制的转义序列</li>
</ol>
<pre><code class="copyable"><script type="text/javascript">
  document.write(escape("Visit W3School!") + "<br />")
  document.write(escape("?!=()#%&"))
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>结果</em></p>
<pre><code class="copyable">Visit%20W3School%21
%3F%21%3D%28%29%23%25%26
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li><code>eval()</code> 计算 JavaScript 字符串，并把它作为脚本代码来执行。</li>
</ol>
<pre><code class="copyable"><script type="text/javascript">
  eval("x=10;y=20;document.write(x*y)")
      document.write(eval("2+2"))
  var x=10
  document.write(eval(x+17))
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="7">
<li><code>getClass()</code> 返回一个 JavaObject 的 JavaClass。</li>
</ol>
<pre><code class="copyable">getClass(javaobj)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="8">
<li><code>isFinite()</code> 检查某个值是否为有穷大的数。</li>
</ol>
<pre><code class="copyable">isFinite(number)    //不是返回false，是返回true
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="9">
<li><code>isNaN()</code> 检查某个值是否是数字。</li>
</ol>
<p>通常用于检测 parseFloat() 和 parseInt() 的结果，以判断它们表示的是否是合法的数字</p>
<pre><code class="copyable">isNaN(x)

document.write(isNaN(123));     //false
document.write(isNaN(Hello));  //true
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="10">
<li><code>Number()</code> 把对象的值转换为数字。</li>
</ol>
<pre><code class="copyable"><script type="text/javascript">
  var test1= new Boolean(true);
  var test2= new Boolean(false);
  var test3= new Date();
  var test4= new String("999");
  var test5= new String("999 888");
  document.write(Number(test1)+ "<br />");     //1
  document.write(Number(test2)+ "<br />");     //0
  document.write(Number(test3)+ "<br />");     //1256657776588
  document.write(Number(test4)+ "<br />");     //999
  document.write(Number(test5)+ "<br />");     //NaN
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="11">
<li><code>parseFloat()</code> 解析一个字符串并返回一个浮点数。</li>
</ol>
<pre><code class="copyable">document.write(parseFloat(" 60 "))    //60
document.write(parseFloat("40 years"))   //40
document.write(parseFloat("He was 40"))   //NaN
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="12">
<li><code>parseInt()</code> 解析一个字符串并返回一个整数。</li>
</ol>
<pre><code class="copyable">parseInt() 会根据 string 来判断数字的基数

parseInt("17",8);//返回 15 (8+7)
parseInt("1f",16);//返回 31 (16+15)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="13">
<li><code>String()</code> 把对象的值转换为字符串。</li>
</ol>
<p>第二个参数可以不写</p>
<pre><code class="copyable">String(object)

var test5= new Date();             //Wed Oct 28 00:17:40 UTC+0800 2009
var test6= new String("999 888");  //999 888
var test7=12345;                   //12345
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">Json  （很重要！！！！！）</h3>
<ul>
<li>
<h4 data-id="heading-16">Json 方法</h4>
</li>
</ul>
<pre><code class="copyable">// JavaScript 对象...：
var myObj = &#123; "name":"Bill", "age":19, "city":"Seattle" &#125;;

// ...转换为 JSON：
var myJSON = JSON.stringify(myObj);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li><code>parse()</code> 解析一个以JSON格式编写的字符串, 并返回一个JavaScript对象</li>
</ol>
<pre><code class="copyable">var obj = JSON.parse('&#123;"firstName":"Bill", "lastName":"Gates"&#125;');
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><code>stringify()</code> 将 JavaScript 对象转换为 JSON 字符串。</li>
</ol>
<pre><code class="copyable">myObj = &#123; "name":"Bill", "age":19, "city":"Seattle" &#125;;
myJSON = JSON.stringify(myObj);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">Math()</h3>
<ul>
<li>
<h4 data-id="heading-18">Math 对象属性</h4>
</li>
</ul>
<ol>
<li><code>E</code>   返回算术常量 e，即自然对数的底数（约等于2.718）。</li>
</ol>
<pre><code class="copyable"> Math.E     //2.718281828459045
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><code>LN2</code>        返回 2 的自然对数（约等于0.693）。</li>
</ol>
<pre><code class="copyable"> Math.LN2   //0.6931471805599453
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li><code>LN10</code>       返回 10 的自然对数（约等于2.302）。</li>
</ol>
<pre><code class="copyable">Math.LN10   //2.302585092994046
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li><code>LOG2E</code>     返回以 2 为底的 e 的对数（约等于 1.414）。</li>
</ol>
<pre><code class="copyable">Math.LOG2E
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li><code>LOG10E</code>  返回以 10 为底的 e 的对数（约等于0.434）。</li>
</ol>
<pre><code class="copyable">Math.LOG10E
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li><code>PI</code>         返回圆周率（约等于3.14159）。</li>
</ol>
<pre><code class="copyable">Math.PI
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="7">
<li><code>SQRT1_2</code>   返回返回 2 的平方根的倒数（约等于 0.707）。</li>
</ol>
<pre><code class="copyable">Math.SQRT1_2
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="8">
<li><code>SQRT2</code>     返回 2 的平方根（约等于 1.414）。</li>
</ol>
<pre><code class="copyable">Math.SQRT2
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">Math 对象方法</h4>
<ol>
<li><code>abs(x)</code> 返回数的绝对值。</li>
</ol>
<pre><code class="copyable">Math.abs(x)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>正余弦</em></p>
<ol start="2">
<li><code>acos(x)</code> 返回数的反余弦值。</li>
<li><code>asin(x)</code> 返回数的反正弦值。</li>
<li><code>cos(x)</code>  返回数的余弦。</li>
<li><code>sin(x)</code> 返回数的正弦。</li>
<li><code>tan(x)</code> 返回角的正切</li>
</ol>
<p><em>舍入</em></p>
<ol start="7">
<li><code>ceil(x)</code> 对数进行上舍入。</li>
</ol>
<pre><code class="copyable">Math.ceil(5.1)    //6
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="8">
<li><code>floor(x)</code> 对数进行下舍入。</li>
</ol>
<pre><code class="copyable">Math.ceil(5.9)    //5
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="9">
<li><code>round(x)</code> 把数四舍五入为最接近的整数</li>
</ol>
<p><em>对数</em>
10. <code>exp(x)</code> 返回 e 的指数。</p>
<pre><code class="copyable">Math.exp(1)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="11">
<li><code>log(x)</code>返回数的自然对数（底为e）。</li>
</ol>
<pre><code class="copyable">Math.log(x)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>最大最小值</em></p>
<ol start="12">
<li><code>max(x,y)</code> 返回 x 和 y 中的最高值</li>
<li><code>min(x,y)</code> 返回 x 和 y 中的最低值。</li>
<li><code>sqrt(x)</code> 返回数的平方根。</li>
</ol>
<p><em>弧度</em></p>
<ol start="15">
<li><code>atan(x)</code>  以介于 -PI/2 与 PI/2 弧度之间的数值来返回 x 的反正切值。</li>
<li><code>atan2(y,x)</code> 返回从 x 轴到点 (x,y) 的角度（介于 -PI/2 与 PI/2 弧度之间）。</li>
</ol>
<p><em>其他</em></p>
<ol start="17">
<li><code>pow(x,y)</code> 返回 x 的 y 次幂。</li>
<li><code>random()</code> 返回 0 ~ 1 之间的随机数。</li>
</ol></div>  
</div>
            