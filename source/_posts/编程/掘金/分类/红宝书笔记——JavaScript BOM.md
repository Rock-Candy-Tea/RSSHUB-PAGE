
---
title: '红宝书笔记——JavaScript BOM'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1035'
author: 掘金
comments: false
date: Thu, 02 Sep 2021 20:26:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=1035'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">window对象</h2>
<p>在全局作用域中声明的变量、函数都会变成window对象的属性和方法。全局变量不能通过delete操作符删除，而直接在window对象上的定义的属性可以。</p>
<pre><code class="copyable">var age=29;
function sayAge()&#123;
    alert(this.age);
&#125;
alert(window.age);//29
sayAge();//29
window.sayAge();//29
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在全局作用域中定义了age变量和sayAge()方法，他们都属于window对象的。</p>
<pre><code class="copyable">var age=29;
window.color="red";
delete window.age;
delete window.color;
alert(window.age);//29
alert(window.color);//undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见全局变量age不可以删除，在window对象上的属性color可以被删除掉。</p>
<h4 data-id="heading-1">窗口位置</h4>
<p>screenLeft 和 screenTop 属性：用来表示窗口相对于屏幕左边和上边的位置。<br>
screenX 和 screenY 属性：提供相同的窗口位置信息。<br>
但两者支持的浏览器不同。下面的代码可以跨浏览器取得窗口左边和上边的位置。</p>
<pre><code class="copyable">var leftPos=(typeof window.screenLeft=='number')?window.screenLeft:window.screenX;
var topPos=(typeof window.screenTop=='number')?window.screenTop:window.screenY;
document.write(leftPos+"  "+topPos);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>全屏的情况下值为0 0。<br>
moveTo()和moveBy() 是将窗口移动到一个新位置。<br>
moveTo() 接受的是新位置的x和y坐标值，而moveBy() 接受的是在水平和垂直方向上移动的像素数。 但是现在很多浏览器已经禁用了。</p>
<h4 data-id="heading-2">窗口大小</h4>
<p>outerWidth和outerHeight返回浏览器窗口本身的尺寸；<br>
innerWidth和innerHeight则表示该容器中页面视图区的大小（减去边框宽度）。<br>
不同的浏览器支持的窗口大小的表示方式不同,因此也需要考虑浏览器兼容性。</p>
<pre><code class="copyable">var pageWidth=window.innerWidth;
var pageHeight=window.innerHeight;
if(typeof pageWidth!='number')&#123;
    if(document.compatMode=="CSS1Compat")&#123;
        pageWidth=document.documentElement.clientWidth;
        pageHeight=document.documentElement.clientHeight;
    &#125;else&#123;
        pageWidth=document.body.clientWidth;
        pageHeight=document.body.clientHeight;
    &#125;
&#125;
document.write(pageWidth+"   "+pageHeight);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>resizeTo() 和 resizeBy() 方法可以调整浏览器窗口的大小。<br>
resizeTo()接受的是窗口的新宽度和新高度，而resizeBy() 接受的是新窗口与原窗口的宽度和高度之差。不过现在有些浏览器也是禁用了的。</p>
<h4 data-id="heading-3">导航和打开窗口</h4>
<p><code>window.open()</code> 方法可以接收四个参数：要加载的url，窗口目标，一个特性字符串以及一个表示新页面是否取代浏览器历史记录中当前加载页面的布尔值。第二个参数可以是：_self,_blank,_parent,_top。第三个参数可以是窗口的一些特性，例如width，height等等。<br>
<code>window.open(" ",'myWin','width=200,height=200,top=100,left=50');</code>
<code>window.close()</code> 方法用来关闭窗口。
检验弹出窗口是否被屏蔽：</p>
<pre><code class="copyable">var bloked=false;
try&#123;
    var wroxWin=window.open("http://www.baidu.com",'_blank');
    if(wroxWin==null)&#123;
        bloked=true;
    &#125;
&#125;catch(ex)&#123;
    bloked=true;
&#125;
if(bloked)&#123;
    alert("The popup was bloked!");
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">间歇调用和超时调用</h4>
<p>setTimeout() 方法接受两个参数：要执行的代码和以毫秒表示的时间。<br>
clearTimeout() 方法是取消超时调用。</p>
<pre><code class="copyable">var oBtn=document.getElementById('btn');
var timeoutId=setTimeout(function()&#123;
    alert("hello!");
&#125;,1000);
clearTimeout(timeoutId);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置间歇调用的方法是setInterval()。它接受的参数也是：要执行的代码和以毫秒表示的时间。</p>
<pre><code class="copyable">var num=0;
var max=10;
var intervalId=null;
function incrementNumber()&#123;
    num++;
    if(num==max)&#123;
        clearInterval(intervalId);
        alert("Done!");
    &#125;
&#125;
intervalId=setInterval(incrementNumber,1000);
var num=0;
var max=10;
function incrementNumber()&#123;
    num++;
    if(num<max)&#123;
        setTimeout(incrementNumber,1000);
    &#125;else&#123;
        alert("Done!");
    &#125;
&#125;
setTimeout(incrementNumber,1000);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这两种表达方式的效果都是一样的。不过最好不要使用间歇调用。</p>
<h4 data-id="heading-5">系统对话框</h4>
<p>alert(),confirm(),prompt()方法可以调用系统对话框向用户显示信息。</p>
<pre><code class="copyable">var result=prompt("What is your name?");
if(result)&#123;
    alert("welcome,"+result);//welcome,...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">location对象</h2>
<p>查询字符串参数，在开发的时候经常用到。</p>
<pre><code class="copyable">function getQueryStringArgs()&#123;
  //取得查询字符串并去掉开头的问号
  var qs=(location.search.length >0?location.search.substring(1)：'');
  //保存数据的对象
  arg=&#123;&#125;;
  var items=qs.length?qs.split('&'):[],
      item=null,
      name=null,
      //在for循环中使用
      i=0,
      len=items.length;
  //逐个将每一项添加到args对象中
  for(i=0;i<len;i++)&#123;
     item=items[i].split("=");
     name=decodeURIComponent(item[0]);
     value=decodeURIComponent(item[1]);
     if(name.length)&#123;
        args[name]=value;
     &#125;
  &#125;
  return args;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例如：要查询的字符串是?q=javascript&num=10</p>
<pre><code class="copyable">var args=getQueryStringArgs();
alert(args["q"]);//javascript
alert(args["num"]);//10
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">位置操作</h4>
<pre><code class="copyable">location.assign("http://www.baidu.com");
window.location="http://www.baidu.com";
location.href="http://www.baidu.com";
这三种表达方式效果都是一样，打开百度的网页。
另外修改location的hash,search,hostname,pathname,port属性可以改变当前加载的页面。
假设初始的URL为http://www.baidu.com/win/
//修改为：http://www.baidu.com/win/#section1
location.hash = “#section1”;
//修改为：http://www.baidu.com/win/?q=JavaScript
location.search = “?q=javascript”;
//修改为：http://www.yahoo.com/win/
location.hostname = “www.yahoo.com”
//修改为：http://www.baidu.com/win/mydir
location.pathname = “mydir”
//修改为：http://www.baidu.com:8080/win/
location.port = “8080”
<span class="copy-code-btn">复制代码</span></code></pre>
<p>replace()函数在设置URL方面与location的href属性或assign函数完全一样，但是它会删除history对象的地址列表中的URL，从而使Go或back等函数无法导航。<br>
reload()函数是用于重新加载当前显示的页面。一般最好将reload() 放在代码的最后一行。</p>
<h2 data-id="heading-8">history对象</h2>
<p>history() 中使用最常的就是go()方法。<br>
后退一页：history.go(-1)<br>
前进一页：history.go(1)<br>
前进两页：history.go(2)<br>
也可以指定网页跳转：history.go(“url”),后退：history().back(),前进：history.forward()。</p></div>  
</div>
            