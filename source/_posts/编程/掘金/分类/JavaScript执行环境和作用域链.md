
---
title: 'JavaScript执行环境和作用域链'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62c7aac865f44e17955d51f3251b609d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 19:48:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62c7aac865f44e17955d51f3251b609d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>1</strong>执行环境（执行上下文）：执行环境是一个对象。</p>
<p><strong>2</strong>全局执行环境是window对象，每个函数也都有它的执行环境。</p>
<p><strong>3</strong>执行环境中有<strong>变量对象</strong>，变量对象保存者执行环境中定义的所有<strong>变量和函数。</strong></p>
<p><strong>4</strong>函数的内部属性[[Scope]]保存有**作用域链，**在创建函数时预先创建。函数执行环境中也有作用域链，在函数调用时创建，复制函数的作用域链并在前端加上函数的执行环境的变量对象（活动对象）。</p>
<p><strong>5this，是函数的内部属性，不是执行环境的。在函数调用时，活动对象自动取得其值。</strong></p>
<p><strong>6</strong>环境栈：JavaScript程序运行开始，创建一个空间，数据结构是栈，称为环境栈。</p>
<p>栈最初始的元素是全局执行环境，函数调用时创建函数执行环境并将其入栈，函数执行完毕之后，其执行环境会出栈。</p>
<p>环境栈有很多执行环境，执行环境中有定义了各自的变量，那么变量和函数的访问权限和顺序需要有一定的机制进行规范，那就是作用域链。</p>
<p><strong>7</strong>作用域链：以链式数据解构组织起各个执行环境中的变量对象。</p>
<p>一个执行环境的作用域链的前端是当前执行环境的变量对象，下一个变量对象来自外部（包含）环境。假设全局执行环境调用了函数1，函数1又调用了函数2，</p>
<pre><code class="copyable">var color="yellow"
function f1()&#123;
console.log("f1",color);
f2()
function f2()&#123;
console.log("f2",color);
&#125;
&#125;
f1()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么作用域链可以表示为：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62c7aac865f44e17955d51f3251b609d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>8</strong>变量的访问机制：基于作用域链，当访问某个变量时，会沿着作用域链一个个节点搜索，搜索到该变量时就停止搜索。</p>
<p><strong>9</strong>怎么理解对象的方法调用时，函数的执行环境？</p>
<pre><code class="copyable">var color="yellow"
var obj=&#123;
color:"blue",
f1:function()&#123;
console.log(color)
&#125;
&#125;
obj.f1()
输出："yellow"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，函数作为对象的方法调用，和作为普通函数调用，是一样的道理。在上面的例子中，obj.f1()的变量对象没有找到color变量，于是沿着作用域链找到全局执行环境的变量对象。</p>
<p>我想，将this指向的理解和执行环境、作用域链脱离开来，会更容易理解。this指向和执行环境无关，只和谁调用了函数有关。this的值在函数调用之前是不确定的，谁调用了函数，this就指向谁。对比下面的代码，可以看出函数的this指向和执行环境就没有必然联系。</p>
<pre><code class="copyable">var color="yellow"
var obj1=&#123;
color:"blue",
f1:function()&#123;
console.log(this.color)
&#125;
&#125;
obj1.f1()
输出：blue
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>10</strong>闭包：闭包是有权访问另一个函数作用域中变量的函数。创建闭包的常见方式，就是在函数内部创建另一个函数。</p>
<pre><code class="copyable">function createCompareFunction(propName)&#123;
return function(obj1,obj2)&#123;
var value1=obj1[propName];
var value2=obj2[propName];
if(value1<value2)&#123;
return -1
&#125;else if(value1>value2)&#123;
return 1
&#125;else&#123;
return 0
&#125;
&#125;
&#125;
var compare=createCompareFunction("name")             //1、创建函数
var result=compare(&#123;name:"Nicholas"&#125;,&#123;name:"Greg"&#125;)  //2、调用函数
compare=null                                         //3、消除对匿名函数引用
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（1）代码1createCompareFunction函数执行返回后，其执行环境和其中的作用域链会销毁，但是变量对象（活动）还是会保存，因为匿名函数的环境对象仍然被闭包函数的作用链引用着。</p>
<p>（2）代码3销毁createCompareFunction后，它的变量对象才被真正回收。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6b79bfad0254bf39517079a5dd3297a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>基于包含函数（createCompareFunction）最后留在的指示变量对象，其里面保存的就是函数执行完毕时变量中最后的镜像。下面的代码本来预期是result[0]是返回0，result[9]是返回9的，但是和预期不一样。</p>
<pre><code class="copyable">function createFunctions()&#123;
var result=new Array();
for (var i=0;i<10;i++)&#123;
result[i]=function()&#123;
return i
&#125;
&#125;
return result
&#125;
var result=createFunctions()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用完毕后，createFunctions函数留存的变量变量对象中有result和i的值，result数组保存有10个函数，每个函数形式为ƒ ()&#123; return i &#125;最后的值时10;</p>
<pre><code class="copyable">result[0]()   //输出结果是10
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用时，在函数自身活动对象中找不到i，所以就去createFunctions函数中找i，找到的i正是10。result中每个元素都是10。要想实现预期，就是以下的代码。</p>
<pre><code class="copyable">function createFunctions()&#123;
var result=new Array();
for (var i=0;i<10;i++)&#123;
result[i]=function(num)&#123;
return function()&#123;
return num;
&#125;;
&#125;(i)
&#125;
return result
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要理解这段代码，这段认识很重要：<strong>“函数的内部属性[[Scope]]保存有作用域链，在创建函数时预先创建。函数执行环境中也有作用域链，在函数调用时创建，复制函数的作用域链并在前端加上函数的执行环境的变量对象（活动对象）。”</strong></p>
<p>最内层的闭包函数function()&#123;return num&#125;有两个外层函数，而闭包函数在创建之时，就已经有作用域链，这个作用域链只有外层函数的变量对象，不包含自己的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bb5207a716247e48f861f0450ec6c07~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上代码中。result数组保存有10个闭包函数，每个函数形式为ƒ ()&#123; return num &#125;，沿着作用域链外层函数的变量对象，每个都是不一样的，num不一样，实现了预期。</p>
<p><strong>11</strong>无块级作用域</p>
<p>作用域只有全局和函数级别的，代码块没有作用域，所以代码块执行也就没有执行环境入栈出栈销毁的概念。下面的代码中，变量i是保存在output()函数的变量对象中的，在for循环外边也可以访问到。</p>
<pre><code class="copyable">function output()&#123;
for(var i=0;i<10;i++)&#123;
console.log(i)
&#125;
console.log("outside for statement",i)  
        //输出10，即时在函数内重新声明也会被忽略声明，值还是10
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>模仿块级作用域，可以使用以下形式，把块级作用域放在匿名函数中，并立即调用。函数调用就有执行环境入栈出栈销毁的概念，最终函数执行完毕，执行环境销毁、变量对象销毁，可以避免变量濡染全局执行环境的问题。</p>
<pre><code class="copyable">(function()&#123;
    //这里是块级作用域
&#125;)()

function output()&#123;
(function()&#123;
for(var i=0;i<10;i++)&#123;
console.log(i);
&#125;
&#125;)();
console.log("outside for statement",i)
        //报错Uncaught ReferenceError: i is not defined
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>12</strong>延长作用域链——with语句（严格模式下不允许使用）</p>
<pre><code class="copyable">var obj=&#123;
name:"Alice",
age:20,
&#125;
console.log(obj.name,obj.age)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等同于</p>
<pre><code class="copyable">with(obj)&#123;
console.log(name,age)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>with语句中使用的变量（name、age)，如果找不到，就会查询obj中是否有同名变量，如果有，就找到了。实际上，with语句能够延长作用域链。在下面的代码中，with的变量对象添加在函数f变量对象的前端，函数f作用域链：with的变量对象>函数f的变量对象->全局环境变量对象。所以with语句中可以使用函数f变量对象中的hobby,当然，函数f也可以使用with变量对象中的desc。</p>
<pre><code class="copyable">function f()&#123;
var obj=&#123;name:"Alice",age:20&#125;;
var hobby="singing";
with(obj)&#123;
var desc=name+age+hobby
&#125;
return desc
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            