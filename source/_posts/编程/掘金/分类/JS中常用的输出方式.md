
---
title: 'JS中常用的输出方式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f104634c78a748249fc5ca77f560b71d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 20:43:30 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f104634c78a748249fc5ca77f560b71d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">JS中常用的三大类输出方式</h1>
<h2 data-id="heading-1">一、console 控制在浏览器控制台输出的</h2>
<h3 data-id="heading-2">1、console.log()</h3>
<ul>
<li>console.log()在控制台输出，</li>
<li>特点：输出任意数据类型的数据,控制台展示的也是对应的数据类型</li>
</ul>
<pre><code class="copyable">     console.log('aaa');
     console.log(&#123;name:"liling"&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在控制台输出为：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f104634c78a748249fc5ca77f560b71d~tplv-k3u1fbpfcp-watermark.image" alt="8BGPA42~C(5YUR&#125;VBWZ`O_6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2、console.dir()</h3>
<ul>
<li>console.dir()输出一个对象或者一个值的详细信息。</li>
</ul>
<pre><code class="copyable">    let arr = &#123; name: '云朵', age: 20 &#125;
    console.dir(arr);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在控制台输出为：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7652f02f4a9f4dd29178fea46de011cd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>与console.log()的区别：console.log()可以一次性输出多个值，但是console.dir()不行,一次只能输出一个值。</li>
</ul>
<pre><code class="copyable">   function func()&#123;&#125;
   console.log(func,100,200);
   console.dir(func);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在控台输出为：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc3f7acfc7964daeb0b804dbe292647c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到console.dir()输出一个对象或者一个值的详细信息，并且一次只能输出一个值。</p>
<h3 data-id="heading-4">3、console.table()</h3>
<ul>
<li>console.table() 是把多维的JSCON数据以表格形式输出。</li>
</ul>
<pre><code class="copyable">      let arr=[&#123;id:1,name:'yunduo'&#125;,
            &#123;id:2,name:'云朵'&#125;];
      console.table(arr);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在控制台输出为：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53f98ffa645c47aaa4be353360b6675c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">4、console.time()/timeEnd()</h3>
<ul>
<li>计算出time和timeEnd中间所有程序执行所消耗的时间(预估时间：受到当前电脑性能的影响)。</li>
</ul>
<pre><code class="copyable">    console.time('AA');
    for(let i = 0;i < 99999;i++)&#123;&#125;
    console.timeEnd('AA');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在控制台输出为：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0e2b8f00f2044aa82e7f52ef2eb2018~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">5、console.warn()</h3>
<ul>
<li>console.warn()以警告的方式输出。</li>
</ul>
<pre><code class="copyable"> console.warn('当前操作不规范!');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在控制台输出为：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89c8ec75979945618d47c9f27a044c58~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">二、window弹出提示框</h2>
<pre><code class="copyable">  window弹出提示框在浏览器窗口中弹出一个提示框,提示框中输出指定的信息，
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">1、alert() 提示框</h3>
<ul>
<li>需要等到alert弹出框，点击确定关闭后，后面的代码才会继续执行(alert/confirm/prompt会阻碍主线程的渲染)。</li>
<li>alert弹出的内容都会默认转换为字符串。</li>
</ul>
<pre><code class="copyable">    alert('大家好!');
    console.log(100);
    alert([10,20,30]); //->数组转换为字符串的结果 "10,20,30"
    alert(&#123;name:'云朵'&#125;); //->普通对象转换为字符串的结果 "[object Object]"

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81ee56ae4bda4daaa7357aac993bb762~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
点击确定后，在控制台输出100，</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d28196e26cf74f47b4182df0c847d629~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>数组转换为字符串：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/843b25a365394af3924acdd4825613e0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>普通对象转换为字符串：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b16692cee8734b4282eb816508310f6c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">2、confirm() 确认取消提示框</h3>
<ul>
<li>confirm相对于alert来说，给用户提供了确定和取消两种选择。</li>
<li>可以创建一个变量，用来接收用户选择的结果，点击确定返回true,点击取消返回flase。</li>
</ul>
<pre><code class="copyable">    let flag = confirm('今天上课了吗？');
    console.log(flag);

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2511f1687a014db397f72bdd6ebeaf0e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击确定，在控制台输出true,</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e229f1235e9f41ffa8e65222d41b02a3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击取消，在控制台输出flase,</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1db044dcd4e42cfb339cb0f6fbdf230~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">3、prompt() 在confirm基础上多加一个原因</h3>
<ul>
<li>prompt在confirm的基础上给用户提供书写操作的原因等信息。</li>
<li>创建一个变量reason,点击的是取消,reason返回结果是null,点击确定，reason返回用户输入的原因等信息。</li>
</ul>
<pre><code class="copyable">    let reason =  prompt('确定要删除此信息吗？');
    console.log(reason);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ddedfb66df424e1b8e2839d626e3ed3a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>输入123，点击确定，输出为123.</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/310015e57eeb4d0ea4bd346115f15615~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击取消，输出为null.</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dec99e72b67947c5817eae2cdf2d88bd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">三、向页面指定容器中插入内容</h2>
<h3 data-id="heading-12">1、 document.write   向页面中输入内容</h3>
<ul>
<li>把内容写到页面当中，和alert一样，写入的内容最后都会转换为字符串，然后再写入。</li>
</ul>
<pre><code class="copyable">    document.write('AA');
    document.write(10);
    document.write(&#123;name:'云朵'&#125;);//若要写入的内容是一个对象则写入页面的内容为  AA10[object Object]

<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果为：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31fcdb4cff864aa7bf039f1f60d2fdae~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">2、 innerHTML  向页面指定容器中输入内容</h3>
<ul>
<li>innerHTML ：向指定容器中插入内容，插入的信息也会变为字符串再插入。</li>
<li>innerHTML：会把之前容器中的内容给覆盖掉，想要追加，则采用+=的方式。</li>
</ul>
<pre><code class="copyable">    
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
         #box&#123;
            border: 1px solid lightcoral;
            background-color: lightblue;
            width: 200px;
            height: 200px;
        &#125;
    </style>
</head>
<body>
    <div id="box">
    </div>
    <script>
        box.innerHTML = "彩色的";
        box.innerText  = "云朵";//=>覆盖原始的所有内容
        box.innerHTML += "彩色的";
        box.innerText  += "云朵";  //=>在原始内容上继续增加

    </script>
    
</body>
</html>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3e6502480474fa387e17314554b574c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">3、innerText 向页面指定容器中输入内容</h3>
<h5 data-id="heading-15">innerText和inner HTML有相同的特点：</h5>
<ul>
<li>向指定容器中插入内容，插入的信息也会变为字符串再插入。</li>
<li>会把之前容器中的内容给覆盖掉，想要追加，则采用+=的方式。</li>
</ul>
<h5 data-id="heading-16">innerText与innerHTML唯一的区别是：</h5>
<p>innerText把所有内容都当作普通的文本，而innerHTML能够把标签文本进行识别和渲染。</p>
<pre><code class="copyable">    
    box.innerText = "<strong>我是重点内容</strong>";
    box.innerHTML = "<strong>我是重点内容</strong>";
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">4、 value   向页面表单元素中输入内容</h3>
<ul>
<li>向页面的文本框赋值。</li>
</ul>
<pre><code class="copyable">   <input type="text" id = "userName">
   <script>
        let userName = document.getElementById('userName');
        userName.Value = "大家加油！";
   </script>   
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/789e30794c42450295b83e6a6cb1844f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            