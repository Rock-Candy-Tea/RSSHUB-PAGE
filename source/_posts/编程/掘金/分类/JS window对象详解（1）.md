
---
title: 'JS window对象详解（1）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9736'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 00:26:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=9736'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>window 是客户端浏览器对象模型的基类，window 对象是客户端 JavaScript 的全局对象。一个 window 对象实际上就是一个独立的窗口，对于框架页面来说，浏览器窗口每个框架都包含一个 window 对象。</p>
<h2 data-id="heading-0"><strong>全局作用域</strong></h2>
<p>在客户端浏览器中，window 对象是访问 BOM 的接口，如引用 document 对象的 document 属性，引用自身的 window 和 self 属性等。同时 window 也为客户端 JavaScript 提供全局作用域。</p>
<p>示例</p>
<p>由于 window 是全局对象，因此所有的全局变量都被解析为该对象的属性。</p>
<pre><code class="copyable">var a = "window.a";  //全局变量
    function f () &#123;  //全局函数
    console.log(a);
&#125;
console.log(window.a);  //返回字符串“window.a”
<span class="copy-code-btn">复制代码</span></code></pre>
<p>window.f();  //返回字符串“window.a”</p>
<p>使用 delete 运算符可以删除属性，但是不能删除变量。</p>
<h2 data-id="heading-1">访问客户端对象</h2>
<p>使用 window 对象可以访问客户端其他对象，这种关系构成浏览器对象模型，window 对象代表根节点，浏览器对象关系的关系如图所示，每个对象说明如下。</p>
<p>window：客户端 JavaScript 顶层对象。每当  或  标签出现时，window 对象就会被自动创建。</p>
<p>navigator：包含客户端有关浏览器信息。</p>
<p>screen：包含客户端屏幕的信息。</p>
<p>history：包含浏览器窗口访问过的 URL 信息。</p>
<p>location：包含当前网页文档的 URL 信息。</p>
<p>document：包含整个 HTML 文档，可被用来访问文档内容及其所有页面元素</p>
<h2 data-id="heading-2">使用系统对话框</h2>
<p>window 对象定义了 3 个人机交互的方法，主要方便对 JavaScript 代码进行调试。</p>
<p>alert()：确定提示框。由浏览器向用户弹出提示性信息。该方法包含一个可选的提示信息参数。如果没有指定参数，则弹出一个空的对话框。</p>
<p>confirm()：选择提示框。。由浏览器向用户弹出提示性信息，弹出的对话框中包含两个按钮，分别表示“确定”和“取消”按钮。如果点击“确定”按钮，则该方法将返回 true；单击“取消”按钮，则返回 false。confirm() 方法也包含一个可选的提示信息参数，如果没有指定参数，则弹出一个空的对话框。</p>
<p>prompt()：输入提示框。可以接收用户输入的信息，并返回输入的信息。prompt() 方法也包含一个可选的提示信息参数，如果没有指定参数，则弹出一个没有提示信息的输入文本对话框。</p>
<p>示例1
下面示例演示了如何综合调用这 3 个方法来设计一个人机交互的对话。</p>
<pre><code class="copyable">var user = prompt("请输入您的用户名");
if (!! user) &#123;  //把输入的信息转换为布尔值
var ok = confirm ("您输入的用户名为：\n" + user + "\n 请确认。");  //输入信息确认
    if (ok) &#123;
        alert ("欢迎您：\n" + user);
    &#125; else &#123;  //重新输入信息
        user = prompt ("请重新输入您的用户名：");
        alert ("欢迎您：\n" + user);
    &#125;
&#125;else &#123;  //提示输入信息
    user = prompt ("请输入您的用户名：");
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">打开和关闭窗口</h2>
<p>使用 window 对象的 open() 方法可以打开一个新窗口。用法如下：</p>
<pre><code class="copyable">window.open (URL, name, features, replace)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数列表如下：</p>
<p>URL：可选字符串，声明在新窗口中显示网页文档的 URL。如果省略，或者为空，则新窗口就不会显示任何文档。</p>
<p>name：可选字符串，声明新窗口的名称。这个名称可以用作标记 < a > 和 < form > 的 target 目标值。如果该参数指定了一个已经存在的窗口，那么 open() 方法就不再创建一个新窗口，而只是返回对指定窗口的引用，在这种情况下，features 参数将被忽略。</p>
<p>features：可选字符串，声明了新窗口要显示的标准浏览器的特征，具体说明如下表所示。如果省略该参数，新窗口将具有所有标准特征。</p>
<p>replace：可选的布尔值。规定了装载到窗口的 URL 是在窗口的浏览历史中创建一个新条目，还是替换浏览历史中的当前条目。</p>
<p>新创建的 window 对象拥有一个 opener 属性，引用打开它的原始对象。opener 只在弹出窗口的最外层 window 对象（top）中定义，而且指向调用 window.open() 方法的窗口或框架。</p>
<p>示例</p>
<p>下面示例演示了打开的窗口与原窗口之间的关系。</p>
<pre><code class="copyable">win = window.open();  //打开新的空白窗口
win.document.write ("<h1>这是新打开的窗口</h1>");  //在新窗口中输出提示信息
win.focus ();  //让原窗口获取焦点
win.opener.document.write ("<h1>这是原来窗口</h1>");  //在原窗口中输出提示信息
console.log(win.opener == window);  //检测window.opener属性值
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 window 的 close() 方法可以关闭一个窗口。例如，关闭一个新创建的 win 窗口可以使用下面的方法实现。</p>
<pre><code class="copyable">win.close;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果在打开窗口内部关闭自身窗口，则应该使用下面的方法。</p>
<pre><code class="copyable">window.close;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            