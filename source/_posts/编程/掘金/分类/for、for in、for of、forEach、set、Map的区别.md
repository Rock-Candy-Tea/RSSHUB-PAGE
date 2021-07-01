
---
title: 'for、for in、for of、forEach、set、Map的区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7039'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 01:11:34 GMT
thumbnail: 'https://picsum.photos/400/300?random=7039'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">1、for循环</h4>
<pre><code class="copyable">var size=[1,2,3,4,5,6,7] //申明一个数组
for(var i=0，len=size.length; i<len; i++)&#123; 
    document.write(size[i] + " ");//数组元素
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">2、for in 可以循环数组和对象<code>推荐对象的时候用for in</code></h4>
<pre><code class="copyable">var x;//可以不定义，也可以在括号内定义
var size=[1,2,3,4,5,6,7] //申明一个数组
var obj=&#123;name:'liushenghua',age:24,sex:'man'&#125; //申明一个对象
for(x in size)&#123; 
    document.write(size[x] + " ");//数组元素
&#125;
for(x in obj)&#123; 
    document.write(obj[x] + " ");//对象元素
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">3、for...of是 ES6 新引入的特性。它既比传统的for循环简洁，同时弥补了forEach和for-in循环的短板,for of无法循环遍历普通对象,for in 会遍历自定义属性，for of不会<code>推荐数组的时候用for of</code></h4>
<pre><code class="copyable">var size=[1,2,3,4,5,6,7] //申明一个数组
for(var value of size)&#123; 
    document.write(value==7?value + "--":value + " ");//数组元素
&#125;
//let 循环内部有效
for(let value of size)&#123; 
    document.write(value==7?value + "--":value + " ");//数组元素
&#125;
//const 循环里的不可修改的静态变量
for(const value of size)&#123; 
    document.write(value + " ");//数组元素
&#125;
//循环一个字符串
let iterable = "boo";
for (let value of iterable) &#123;
  console.log(value);
&#125;
// 但是可以循环一个拥有enumerable属性的对象。
//如果我们按对象所拥有的属性进行循环，可使用内置的Object.keys()和方法
var obj = &#123; name: 'zhangshan', age: 23, color: 'red' &#125;
for (var item of Object.keys(obj)) &#123;
        console.log(item)
&#125;


    // for of遍历不出自定义属性,for in 可以如下：
    var arr = ['apple', 'banana', 'orange']
    arr.name = 'name';//自定义属性
    for (var key in arr) &#123;
        console.log(arr[key])//apple banana orange name
    &#125;
    for (var item of arr) &#123;
        console.log(item)//apple banana orange grape
    &#125;
   // for of不会跳过无定义的值,for in 会跳过无定义的值如下：
    var arr = [, 'apple', 'banana', 'orange']
    for (var key in arr) &#123;
        console.log(arr[key])//apple banana orange
    &#125;
    // console.log('--------')
    for (var item of arr) &#123;
        console.log(item)//undefined apple banana orange
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">4、for循环和while循环其实是可以相互转换的</h4>
<p>while</p>
<pre><code class="copyable">cars=["BMW","Volvo","Saab","Ford"];
var i=0;
while (cars[i])&#123;
document.write(cars[i] + "<br>");
i++;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>for循环</p>
<pre><code class="copyable">cars=["BMW","Volvo","Saab","Ford"];
var i=0;
for (;cars[i];)
&#123;
    document.write(cars[i] + "<br>");
    i++;
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">5、for和for in的区别</h4>
<p>定义了数组后对数组进行赋值，中间如有某些下标未被使用（即未被赋值），在遍历的时候，采用一般的 for 循环和 for...in 循环得到的结果不同。for...in 循环会自动跳过那些没被赋值的元素，而 for 循环则不会，它会显示出 undefined。</p>
<pre><code class="copyable"><p>点击下面的按钮，循环遍历</p>
<button onclick="myFunction()">点击这里</button>
<p id="demo"></p>
<script>
function myFunction()&#123;
var array = new Array();
var x;
var txt=""
array[0] = 1;
array[3] = 2;
array[4] = 3;
array[10] = 4;
for( x in array )&#123;
alert(array[x]);     // 依次显示出 1 2 3 4
&#125; 
alert(array.length);    // 结果是11
for( var i=0 ; i<4 ; i++)&#123;
alert(array[i]);     // 依次显示出 1 undefined undefined 2 
&#125;
document.getElementById("demo").innerHTML = txt;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>for循环通过break可以随时跳出循环，当花括号只有一个时，不用括号，continue可以跳过此步骤
break</p>
<pre><code class="copyable">for (i=0;i<10;i++)
&#123;
    if (i==3) break；
    x=x + "The number is " + i + "<br>";
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>continue</p>
<pre><code class="copyable">for (i=0;i<10;i++)
&#123;
    if (i==3) continue；
    x=x + "The number is " + i + "<br>";
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">6、forEach方法</h4>
<h5 data-id="heading-6">一、概念</h5>
<p>forEach()方法按升序为数组中含有效值的每一项执行一次callback 函数，那些已删除或者未初始化的项将被跳过（例如在稀疏数组上）。</p>
<p><code>注意： forEach()的返回值为undefined forEach()对于空数组是不会执行回调函数的 没有办法中止或者跳出 forEach()循环，除了抛出一个异常</code></p>
<h5 data-id="heading-7">二、语法</h5>
<p>arr.forEach(callback(currentValue, index, arr), thisArg)
参数说明：</p>
<p>callback：必须。为数组中每个元素执行的函数，该函数接受三个参数：
currentValue：必须。数组中正在处理的当前元素。
index：可选。当前元素的索引值。
arr：可选。方法正在操作的数组。
thisArg：可选。当执行回调函数时用作this的值（参考对象）。</p>
<h5 data-id="heading-8">三、实例</h5>
<p>打印出数组的内容：</p>
<pre><code class="copyable">let arr = [4, 9, 16, 25]
    arr.forEach((val, index, arr) => &#123;
        console.log(index)
    &#125;)
    var newArr = arr.map((val, index, arr) => &#123;
        return val * 2;
    &#125;)
    var roots = arr.map(Math.sqrt);
    console.log(newArr)
    console.log(roots)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">7、Map方法</h4>
<pre><code class="copyable"> var arr = ['1', '4', '3']
    var newArr = arr.map((value, index, array) => &#123;
        return value
    &#125;)
    var newArr1 = arr.map(str => parseInt(str));
    var newArr2 = arr.map(Number)
    console.log(newArr)// '1', '4', '3'
    console.log(newArr1)// 1 4 3
    console.log(newArr2)// 1 4 3
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">8.set方法</h4>
<p>Set和Map类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在Set中，没有重复的key。</p>
<pre><code class="copyable">var s = new Set([2, 3, 3, '3', 4]);
    console.log(s);//Set &#123;2, 3,'3', 4,&#125;
    //添加一个key
    s.add(5);
    //重复元素在Set中自动被过滤
    s.add(5);
    console.log(s);//Set &#123;2, 3, 4,5&#125;
    //删除一个key
    s.delete(2);
    //Set&#123;3, "3", 4, 5&#125;//注意数字3和字符串'3'是不同的元素。
    console.log(s);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            