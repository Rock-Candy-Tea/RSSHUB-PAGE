
---
title: 'chapter 6、JS----从入门到熟练的小白之路（持续更新....)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1707'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 03:09:57 GMT
thumbnail: 'https://picsum.photos/400/300?random=1707'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、验证码案例</h1>
<h2 data-id="heading-1">【1.1 】 生成有字母、数字组合成的四位验证码</h2>
<pre><code class="copyable">//随机验证码：数字和字母组合，（四个数字和字母）
/* 
===> 1先把验证码准备好
===> 2随机获取相应的索引值
===> 3获取元素
*/
function  getCode()&#123;
    var str="qwertyuiopasdfghjklzxcvbnm"+"QWERTYUIOPASDFGHJKLZXCVBNM"+"0123456789";
    var result="";
    //==> 索引值的范围：0---61
    for(var i=0;i<4;i++)&#123;
       var index=Math.round(Math.random()*61);
       var item=str[index];
       result+=item;
    &#125;
    return result;
&#125;
var code=document.getElementById("code");
var btn=document.getElementById("btn");
code.innerHTML=getCode();
btn.onclick=function()&#123;
    code.innerHTML=getCode();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>【1.2】生成不重复的验证码</p>
<pre><code class="copyable">for(var i=0;i<4;i++)&#123;
       var index=Math.round(Math.random()*61);
       var item=str[index];
       //===>新增一个判断
       if(str.indexOf(item)>-1)&#123;
          // 此次循环作废，总共四次，浪费了一次，所以需要
          i--;
          continue;
       &#125;
       result+=item;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>【1.3】 while 循环实现</p>
<p>只要条件成立，就一直执行，知道条件不成立的时候停止</p>
<p>while(条件)&#123;
执行体
&#125;</p>
<pre><code class="copyable">function  getCode()&#123;
    var str="qwertyuiopasdfghjklzxcvbnm"+"QWERTYUIOPASDFGHJKLZXCVBNM"+"0123456789";
    var result="";
    //==> 索引值的范围：0---61
    while(result.length<4)&#123;
       var index=Math.round(Math.random()*61);
       var item=str[index];
       if(result.indexOf(item)==-1)&#123;
          result+=item;
       &#125;
    &#125;
    return result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">二、dom操作</h1>
<h2 data-id="heading-3">2.1【dom树】：浏览器在加载页面的时候，首先就是dom的结构计算，它形式就像是一颗大树，有很多的分支，所以被称为 "dom tree"</h2>
<h3 data-id="heading-4">【回流和重绘】</h3>
<ul>
<li>
<p>重绘(repaint)：当元素样式的改变不影响布局时，浏览器将使用重绘对元素进行更新，此时由于只需要 UI 层面的重新像素绘制，因此损耗较少。</p>
<p>常见的重绘操作有：</p>
<ul>
<li>
<ol>
<li>改变元素颜色</li>
</ol>
</li>
<li>
<ol start="2">
<li>改变元素背景色</li>
</ol>
</li>
<li>
<ol start="3">
<li>more ……</li>
</ol>
</li>
</ul>
</li>
<li>
<p>回流(reflow)：又叫重排（layout）。当元素的尺寸、结构或者触发某些属性时，浏览器会重新渲染页面，称为回流。此时，浏览器需要重新经过计算，计算后还需要重新页面布局，因此是较重的操作。</p>
<p>常见的回流操作有：</p>
<ul>
<li>
<ol>
<li>页面初次渲染</li>
</ol>
</li>
<li>
<ol start="2">
<li>浏览器窗口大小改变</li>
</ol>
</li>
<li>
<ol start="3">
<li>元素尺寸/位置/内容发生改变</li>
</ol>
</li>
<li>
<ol start="4">
<li>元素字体大小变化</li>
</ol>
</li>
<li>
<ol start="5">
<li>添加或者删除可见的 DOM 元素</li>
</ol>
</li>
<li>
<ol start="6">
<li>激活 CSS 伪类（:hover……）</li>
</ol>
</li>
<li>
<ol start="7">
<li>more ……</li>
</ol>
</li>
</ul>
</li>
</ul>
<p><code>• 重点：回流必定会触发重绘，重绘不一定会触发回流。重绘的开销较小，回流的代价较高。</code></p>
<h2 data-id="heading-5">2.2[常用的dom操作方法]</h2>
<h3 data-id="heading-6">1）getElementById：通过元素的id获取元素.</h3>
<pre><code class="copyable">document.getElementById("box");
【document】：
     document 是上下文，限制范围的意思：在哪个范围下的 id名字是box的这个元素，不过这个上下文只能是   document
     
【id名字唯一性】：
     id名字是唯一的，一个document文档中不能同时出现多个相同的id名字，如果设置了多个相同的id，只能获取到第一个。
     
[兼容性注意]：不要让name 和id的名字一样。因为在ie6-ie7 的时候，如果设置了name属性，通过id也可以获取到
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><body>
   <input type="text" name="text">
</body>
</html>
<script>
  console.log(document.getElementById("text"));
  //  在ie6或者ie7的时候可以获取到
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">2）【context].getElementsByTagName：在特定的上下文中，通过标签名，获取一组元素。</h3>
<ul>
<li>得到的是一个类数组，不能直接用数组的方法</li>
<li>得到的是一个集合，如果想要操作其中的某一项，可以基于索引获取。</li>
</ul>
<pre><code class="copyable">    var omain=document.getElementById("main");
    var olis=omain.getElementsByTagName("li");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>// 想要获取到第二个li:olis[1]</p>
<h3 data-id="heading-8">3) [context].getElementsByCalssName:通过类名获取元素集合</h3>
<p>• 此方法在ie6--ie8下不兼容</p>
<h3 data-id="heading-9">4）document.getElementsByName:通过name名字获取一组元素集合</h3>
<ul>
<li>它的上下文也只能是document</li>
<li>另外，正常的规范中，咱们只会给表单元素起name值，如果给其它元素设置name，在ie9以下版本浏览器不兼容，是获取不到的，所以为了这种情况，咱们以后养成习惯，只给表单元素用name，非表单元素不用name</li>
</ul>
<h3 data-id="heading-10">5）【context].querySelector("选择器")</h3>
<p>通过选择器获取指定的元素，即使匹配的有多个，也只会对第一个起作用，获取到的是一个对象(给咱们平时写样式时候写选择器是一样的)</p>
<pre><code class="copyable"> <div class="main">
        <div class="box1"></div>
    </div>
    
    document.querySlector(".main>div")
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">6)【context】.querySelectorAll("选择器")</h3>
<p>通过指定的选择器获取一组节点结合
注意：querySelector 和querySelector 在ie6-ie8 下不兼容</p>
<h3 data-id="heading-12">7）document.head</h3>
<pre><code class="copyable">获取Head元素对象
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">8) document.body</h3>
<pre><code class="copyable">获取body元素对象
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">9) document.documentElement</h3>
<pre><code class="copyable">获取html元素对象
<span class="copy-code-btn">复制代码</span></code></pre>
<p>【需求：】获取一屏幕的宽度或者高度，兼容所有的浏览器</p>
<pre><code class="copyable">// 获取一屏幕的高度
var vH=document.documnentElement.clientHeight || document.body.clientHeight;
// 偶去一屏幕的宽度
var vW=document.documentElement.clientWidth || document.body.clientWidth;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">2.3 练习题：</h2>
<p>获取页面中所有name属性值为 "hehe" 的元素标签</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
       
    </style>
</head>
<body>
    
   <div class="box1">
       <input type="text" name="he1">
   </div>
   <input class="box1" name="he1">
</body>
</html>
<script>
 function getElementsByName(value)&#123;
     var allTag=document.getElementsByTagName("*");
     var names=[];
     for(var i=0;i<allTag.length;i++)&#123;
          var item=allTag[i];
          if(item.name==value)&#123;
             names.push(item);
          &#125;
     &#125;
     return names;
 &#125;
 var ary=getElementsByName("he1")
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <div id="main">
        <div class="box1">
            <input type="text" name="he1" id="input1">
            <div name="he1" id="div2">111</div>
        </div>
        <input class="box1" name="he1">
    </div>
</body>
</html>
<script>
 var omain=document.getElementById("main");   
 function getName(contex,name,attr)&#123;
    var tags=contex.getElementsByTagName("*");
    var ary=[];
    for(var i=0;i<tags.length;i++)&#123;
        if(tags[i].getAttribute(name)==attr)&#123;
           ary.push(tags[i])
        &#125;
    &#125;
    return ary;
 &#125;
 var res=getName(omain,"name","he1");
 console.log(res);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于id的一些鲜为人知的事情：
直接把id当成变量去用的时候，可以获取相应的id元素。（浏览器的机制）</p>
   <div id="user-content-box1">
   </div>
     <div id="user-content-box1">
   </div>
<pre><code class="copyable">   console.log(box1)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">2.4【节点】</h2>
<h3 data-id="heading-17">1）、文档节点</h3>
<ul>
<li>
<p>nodeType：9</p>
</li>
<li>
<p>nodeName："#document"</p>
</li>
<li>
<p>nodeValue:null
document.nodeType;</p>
<p>document.nodeName</p>
<p>document.nodeValue;</p>
</li>
</ul>
<h3 data-id="heading-18">2）、属性节点</h3>
<ul>
<li>nodeType：2</li>
<li>nodeName：属性名</li>
<li>nodeValue:属性值</li>
</ul>
<pre><code class="copyable"> <a href="http://www.baidu.com" id="a1">百度</a>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">var a1=a1.getAttributeNode("href");// 获取属性节点
console.log(a1.nodeType);//2
console.log(a1.nodeName);//"href"; 属性名
console.log(a1.nodeValue);//"http://www.baidu.com"; 属性值
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">3）、元素节点</h3>
<ul>
<li>nodeType：1</li>
<li>nodeName：大写的标签名</li>
<li>nodeValue:null</li>
</ul>
<h3 data-id="heading-20">4）、文本节点</h3>
<ul>
<li>nodeType：3</li>
<li>nodeName："#text"</li>
<li>nodeValue:文本内容</li>
<li>在标准浏览器中，换行和空格也属于文本节点</li>
</ul>
<pre><code class="copyable"><a href="http://www.baidu.com" id="a1">百度</a>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">var res=a1.childNodes[0];
console.log(res.nodeType);//3
console.log(res.nodeValue);//"百度";
console.log(res.nodeName);//"#text";
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">5）、注释节点</h3>
<ul>
<li>nodeType：8</li>
<li>nodeName："#comment"</li>
<li>nodeValue:注释的内容</li>
</ul>
<pre><code class="copyable"> <a href="http://www.baidu.com" id="a1">
    <!--a标签 -->
    百度
 </a>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">a1.childNodes; //NodeList(3) [text, comment, text]
a1.childNodes[1].nodeName;//"#comment"
a1.childNodes[1].nodeType;//8
a1.childNodes[1].nodeValue;//"a标签 "
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">2.5【节点的关系关系属性】</h2>
<h3 data-id="heading-23">1）parentNode</h3>
<p>获取当前节点唯一的父亲节点</p>
<h3 data-id="heading-24">2）childNodes</h3>
<p>获取当前节点所有的子节点</p>
<pre><code class="copyable"><ul id="main">
       <!-- 我是注释 -->
       <li>你永远是最胖的</li>
       <li>你永远是最胖的</li>
       <li>你永远是最胖的</li>
       <li>你永远是最胖的</li>
</ul>
<script>
console.log(main.childNodes);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">3)children</h3>
<p>获取当前元素所有的元素子节点，但是在ie6--ie8下不兼容</p>
<pre><code class="copyable">console.log(main.children);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">4)previousSibling</h3>
<p>获取上一个哥哥节点
main.previousSibling</p>
<h3 data-id="heading-27">5)previousElementSibling</h3>
<p>ie6-ie8 不兼容</p>
<pre><code class="copyable"><span>1</span>
   <ul id="main">
       <!-- 我是注释 -->
       <li>你永远是最胖的</li>
       <li>你永远是最胖的</li>
       <li>你永远是最胖的</li>
       <li>你永远是最胖的</li>
   </ul>
 <script>
 console.log(main.previousElementSibling);
 //<span>1</span>
 
 <script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">6）nextSibling</h3>
<p>获取当前节点的下一个兄弟节点</p>
<pre><code class="copyable"> <span id="span1">1</span>
   <ul id="main">
       <!-- 我是注释 -->
       <li>你永远是最胖的</li>
       <li>你永远是最胖的</li>
       <li>你永远是最胖的</li>
       <li>你永远是最胖的</li>
   </ul>
   <span>2</span>
   
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">7) nextElementSibling</h3>
<p>获取当前节点的下一个元素兄弟节点
ie6-ie8 不兼容</p>
<h3 data-id="heading-30">8)firstChild</h3>
<p>获取当前节点的第一个子节点</p>
<h3 data-id="heading-31">9）firstElementChild</h3>
<p>获取当前节点的第一个元素子节点
ie6-ie8 不兼容</p>
<h3 data-id="heading-32">10）lastChild</h3>
<p>获取当前节点的最后一个子节点</p>
<h3 data-id="heading-33">11） lastElementChild</h3>
<p>获取当前节点的最后一个元素子节点
ie6-ie8 不兼容</p>
<h1 data-id="heading-34">三、练习题</h1>
<h2 data-id="heading-35">1） 自己手动封装一个获取节点下面的所有子元素，要求考虑兼容性。</h2>



    
    
    
    Document
    
</style>



   <span id="user-content-span1">1</span>
   <ul id="user-content-main">
       
       <li>选择珠峰的，都是明智的！</li>
       <li>选择珠峰的，都是明智的！</li>
       <li>选择珠峰的，都是明智的！</li>
       <li>选择珠峰的，都是明智的！</li>
   </ul>
   <span>2</span>



2) 自己手动封装一个perviousElementSibling，要兼容
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
       
    </style>
</head>
<body>
   <span id="span1">1</span>
   <ul id="main">
       <!-- 我是注释 -->
       <li>你永远是最胖的</li>
       <li>你永远是最胖的</li>
       <li>你永远是最胖的</li>
       <li>你永远是最胖的</li>
   </ul>
   <span id="span2">2</span>
</body>
</html>
<script>
 function previousElmentSibling(ele)&#123;
     var pre=ele.previousSibling;
     while(pre&&pre.nodeType!==1)&#123;
         pre=pre.previousSibling;
     &#125;
     return pre;
 &#125;
 previousElmentSibling(span2)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-36">四、dom 的增删改</h1>
<h2 data-id="heading-37">1） createElement：创建一个元素</h2>
<p>documment.createElement("div");</p>
<h2 data-id="heading-38">2） createTextNode: 创建一个文本节点</h2>
<p>var otext=document.createTextNode("哈哈！");</p>
<h2 data-id="heading-39">3) appendChild:把元素追加到一个容器的末尾</h2>
<p>【context】.appendChild([元素])；</p>
<pre><code class="copyable">var odiv=documment.createElement("div");
document.body.appendChild(odiv);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-40">4）insertBefore: 把一个元素插入到另一个元素的前面</h2>
<p>把新元素添加到原有元素的前面</p>
<p>【context】.insertBefore（newEle，oldEle）；</p>
<h2 data-id="heading-41">5) cloneNode:把某一个节点进行克隆</h2>
<ul>
<li>【ele】.cloneNode();浅克隆： 只是克隆了一个节点，里面的内容还有样式都没克隆</li>
<li>【ele】.cloneNode(true);深克隆：把节点包含的所有内容进行克隆</li>
</ul>
<h2 data-id="heading-42">6）removeChild：移除某个节点</h2>
<p>【context】.removeChild(ele);</p>
<h2 data-id="heading-43">7）set/get/removeAttribute</h2>
<p>设置/获取/删除 当前元素的某一个自定义属性</p>
<ul>
<li>setAttribute</li>
<li>getAttribute</li>
<li>removeAttribute</li>
</ul>
<pre><code class="copyable"><div id="box"></div>
//=======>  setAttribute  设置
box.setAttribute("index",1);
box.getAttribute("index");
box.removeAttribute("index");
//========> 基于键值对操作
// 设置
box["aa"]=22;
// 获取
box["aa"]
//移除
delete box[aa];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基于键值对方式 增删改：修改当前对象的堆内存空间完成的（在堆内存空间可以看到）
基于Attribute dom方法增删改，是修改html结构来完成的（此种方法设置的在结构上可以看到）</p>
<p><code>以上两种方式不能混用</code></p>
<h1 data-id="heading-44">五、利用a标签的href来重新获取url参数</h1>
<blockquote>
<p>var str="<a href="http://www.zhufengpeixun.cn/?name=lili&age=18#123" target="_blank" rel="nofollow noopener noreferrer">www.zhufengpeixun.cn?name=lili&age=18#123</a>"</p>
</blockquote>
<pre><code class="copyable">/* 
 search: "?name=lili&age=18"
 hash: "#123"
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">function queryParams(str)&#123;
   var a=document.createElement("a");
   a.href=str;
   var obj=&#123;&#125;;
   console.log(a.search); //?name=lili&age=18
   console.log(a.hash); //#123
   //[name=lili,age=18]
   var search=a.search.substr(1); 
   obj.hash=a.hash?hash:null;
   if(search)&#123;
       var searchAry=search.split("&");
       for(var i=0;i<searchAry.length;i++)&#123;
             var itemAry=searchAry[i];
             //[name,lili]
             var item=itemAry.split("=");
             var key=item[0];
             var value=item[1];
             obj[key]=value;
       &#125;
   &#125;
   return obj;
&#125;
var dd=queryParams(str);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            