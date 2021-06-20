
---
title: 'console.log的那些事'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7283'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 07:18:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=7283'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第19天，活动详情查看: <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><strong>控制台 console.log() 打印很多日志，会不会影响浏览器卡顿？</strong></p>
<blockquote>
<p>为什么要写这篇文章，接手了一个老项目，需要对项目的性能进行优化，打开F12发现，console.log()写的内容太多，多到你不敢想象，这还是次要的，上线的代码，debugger,到处都是，整个系统，每天用户使用到下午三四点的时候开始卡顿，CTRL+SHIFT+DELETE之后，速度又快了，种种迹象表明，肯定是有内存泄露的情况，因为是老系统，前后端不分离，首先要说服负责人，上线代码删除console.log, 今天不讲解怎么删除线上代码console.log,  先分析一下，为什么线上代码要删除console.log</p>
</blockquote>
<p>console.log() 目的是向浏览器控制台打印信息， 常用来在开发的时候调试分析，但是很多人在上线的代码里面忘记关闭了， 导致打印信息不停的输出。</p>
<pre><code class="copyable">（1） console.log:   可能导致内存泄露

（2） console.log:   在传递给console.log的对象是不能被垃圾回收

（3） console.log:   它属于宏任务，在执行的时候，也是需要耗时
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结合Chrome的 F12中的Performance 进行一些分析， 勾选上Memory,  通过带有console.log的输出和没有console.log的输出，对比分析结果： 最好不要在页面中进行console.log的大对象输出，会影响到页面的整体性能。</p>
<h4 data-id="heading-0">1, console.time</h4>
<p>​    通常我们查看一段代码的执行时间，用来作性能调试分析所用。</p>
<pre><code class="copyable">首先记住：console.log 对象不会被浏览器垃圾回收机制回收 会造成浏览器卡顿
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">console.time()相当于秒表中的开始按钮
console.timeLog()相当于秒表中的按圈计时/按点计时
console.timeEnd()相当于计时结束
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">console.time('time')
console.log(JSON.parse(JSON.stringify(new Object())))
console.timeEnd('time')
打印：time: 1.572021484375ms
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.time(<span class="hljs-string">'time'</span>)
setTimeOut(<span class="hljs-function">() =></span> &#123;
   <span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">'wait'</span>)
&#125;, <span class="hljs-number">1000</span>)

<span class="hljs-attr">wati</span>: 1000ms
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">2, console.count</h4>
<p>这是一个计数器， 传递一个函数的名称，可以打印出这个函数被调用的次数</p>
<pre><code class="copyable">let a = () => &#123;
     console.count('调用a')
&#125;
let b = () => &#123;
     console.count('调用b')
&#125;
a()
b()
输入： 调用a:1
      调用b:1
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">3, console.assert</h4>
<p>断言， 可以理解为： 才猜错了这个表达式的真假，那我就可以打出我的信息</p>
<p>console.assert(参数1，参数2)， 这里面有两个参数：</p>
<p>第一个参数：是断言条件，即应该发生的情况；</p>
<p>第二个参数：是不满足断言条件时，打印出来的提示信息。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.assert(a === <span class="hljs-number">3</span>, <span class="hljs-string">"a 的值不是3！"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>断言函数还是挺有用的，就算不是为了做单元测试，自己平时在写代码时为了保证程序正确性，也可以使用一下。可以让我们的输出更加干净。当然，你也可以写if判断语句。</p>
<h4 data-id="heading-3">4, console.clear</h4>
<p>这个函数也是经常用，在多人开发的项目里面，特别是很多项目小组成员都喜欢打印console.log的时候，你在调试的时候，特别不想看到他们的结果，统统都可以用console.clear清楚干净，那后输出自己的调试信息。</p>
<pre><code class="copyable">console.clear()
console.log(data)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">5, console.dir</h4>
<p>在大多数情况下，console.dir()和console.log() 看起来很像，在打印DOM元素信息的时候，你会发现，dir会输出的更加详细</p>
<pre><code class="copyable">举个列子：查看element信息
let element = document.getElementById('root')
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>console.log(element)</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"root"</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"ssse"</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https:/xxxx"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">itemprop</span>=<span class="hljs-string">"commentCount"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"24"</span>></span><span class="hljs-tag"></<span class="hljs-name">meta</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"ble"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"Rtr"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"Rix"</span>></span>Vue<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"p"</span>></span>,<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    </div
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>   
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>console.dir(element)</strong></p>
<pre><code class="copyable">div#root
accessKey: ""
align: ""
assignedSlot: null
attributeStyleMap: StylePropertyMap &#123;size: 0&#125;
attributes: NamedNodeMap &#123;0: id, id: id, length: 1&#125;
autocapitalize: ""
baseURI: "https://www.zhihu.com/question/61986999"
childElementCount: 1
childNodes: NodeList [div]
children: HTMLCollection [div]
classList: DOMTokenList [value: ""]
className: ""
clientHeight: 2763
clientLeft: 0
clientTop: 0
clientWidth: 743
contentEditable: "inherit"
dataset: DOMStringMap &#123;&#125;
dir: ""
draggable: false
firstChild: div
firstElementChild: div
hidden: false
id: "root"
innerHTML: "<div><div class="LoadingBar"></div><div><header ro"
inputMode: ""
isConnected: true
isContentEditable: false
lang: ""
lastChild: div
lastElementChild: div
localName: "div"
namespaceURI: "http://www.w3.org/1999/xhtml"
nextElementSibling: script#js-clientConfig
nextSibling: script#
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">6, console.warn</h4>
<p>可以直接替换console.log，他们都是输出，唯一的区别就是：输出的文字颜色是黄色， 具体来说，如果给日志定义错误级别的话，它的输出属于警告级别，而不是信息级别， 使其在众多日志中输出会显示的更加明显，突出</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.warn(<span class="hljs-string">'这是一个警告'</span>)
输出是：黄色字体，这是一个警告⚠️
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">7, console.log, debugger的区别</h4>
<p>这些都可以用来调试。</p>
<p>debuuger: 在指定的代码处，添加debugger, 或者打开浏览器的F12， 在指点的地方添加F12，通过执行项目，一步步观察变量和函数的执行过程</p>
<p>Console.log： 在指点的函数和变量的地方添加console.log， 把向查看的结果dayin 在浏览器控制台上，进行过程分析， 两者都能加快我们的开发</p>
<p>在准确率上来说， console..log的准确率要高于debugger， 因为在我们的代码中，有很多异步事件，也有很多监听方法，或者是生命周期函数，他们的执行顺序或决定这变量值的存储，影响到不同的执行结果，debugger无法查看代码的执行顺序， 可能会给自己带来无法想象的问题，本人就在这个问题上吃过几次亏， 因为打来debugger 会加快一些异步请求的速度，实际上，如果没有这些debugger, 异步请求是没有完成的。<strong>这样会导致我们开发的时候，功能都是正常的，为什么上了测试或者上生产就会有问题的原因</strong></p>
<pre><code class="copyable">个人建议： 简单功能，可以通过浏览器debugger断点查看
         复杂功能，涉及到一些异步请求，事件监听或者是生命周期函数，最好是用console.log就行调试，当然，
         调试完成之后，一定要养成删掉的习惯。
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">8, 总结</h4>
<p>测试通过的代码，即将发到生产环境上的代码，要避免有大量的console.log日志输出，它会影响到页面的性能，有可能会造成内存泄露， 开发的过程中可以养成用console.log的习惯， 在有异步接口请求，或者多个事件监听发送的代码中，尽量不要用debugger排查问题。</p></div>  
</div>
            