
---
title: 'Vue-router 的原理介绍以及使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2936'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 00:51:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=2936'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>vue-router通过<code>hash</code>与<code>History</code>两种方式实现前端路由
更新视图但不重新请求页面”是前端路由原理的核心之一，目前在浏览器环境中这一功能的实现主要有两种方式</p>
<ul>
<li><code>hash</code>：通过URL中的hash（“#”）实现路由变更</li>
<li><code>History</code>： 使用<code>HTML5</code>提供的History API对<code>history</code>栈中内容进行操作</li>
</ul>
<p>那么两种方式有什么区别呢：</p>
<p><code>hash</code>模式：</p>
<p>URL的hash URL的hash也就是锚点(#), 本质上是改变window.location的href属性. 我们可以通过直接赋值location.hash来改变href, 但是页面不发生刷新.
这种模式下会在链接中增加#</p>
<p>例如：</p>
<pre><code class="hljs language-js copyable" lang="js">    http:<span class="hljs-comment">//localhost:8080/#/pageName</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>hash虽然出现在URL中，但不会被包括在HTTP请求中，对后端完全没有影响，因此改变hash不会重新加载页面。</p>
<p><code>History</code>模式：</p>
<p>history使用<code>HTML5</code>提供的History API操作页面路由</p>
<p>例如：</p>
<pre><code class="hljs language-js copyable" lang="js">    http:<span class="hljs-comment">//localhost:8080/pageName</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>history.pushState()</li>
<li>history.replaceState()</li>
<li>history.go()</li>
<li>history.back() 等价于 history.go(-1)</li>
<li>history.forward() 等价于 history.go(1)</li>
</ul>
<p><code>hash</code>和<code>History</code>这两个方法应用于浏览器的历史记录栈，在当前已有的back、forward、go的基础上，它们提供了对历史记录进行修改的功能。只是当它们执行修改时，虽然改变了当前的URL，但浏览器不会即向后端发送请求。</p>
<p>因此可以说，hash模式和histoury模式都是属于浏览器自身的特性，Vue-Router只是利用了这两个特性（通过调用浏览器提供的接口）来实现前端路由。</p>
<p>使用场景:</p>
<p>一般情景下，hash和histoury都可以，如果不想要链接里出现#，可以选择使用路由的history模式，这种模式充分利用history。pushState API来完成URL跳转，无须重新加载页面。</p>
<p>调用history.pushState()相比于直接修改hash ，存在以下优势：</p>
<ul>
<li>pushState()设置的新URL可以是与当前URL同源的任意URL；而hash只可修改#后面的部分，因此只能设置与当前URL同文档的URL；</li>
<li>pushState()设置的新URL可以与当前URL一模一样，这样也会把记录添加到栈中；而hash设置的新值必须与原来不一样才会触发动作将记录添加到栈中；</li>
<li>pushState()通过stateObject参数可以添加任意类型的数据到记录中；而hash只可添加短字符串；</li>
<li>pushState()可额外设置title属性供后续使用。</li>
</ul>
<p>但是当需要通过URL向后端发起HTTP请求时，两者的差异就来了。尤其在用户手动输入URL后回车，或者刷新（重启）浏览器的时候。</p>
<ul>
<li>hash 模式下，仅hash符号之前的内容会被包含在请求中，如:<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.aa.com" target="_blank" rel="nofollow noopener noreferrer" title="http://www.aa.com" ref="nofollow noopener noreferrer">www.aa.com</a>,
因此对于后端来说，即使没有做到对路由的全覆盖，也不会返回404错误。</li>
<li>history模式下，前端的URL必须和实际向后端发起请求的URL一致。如:htttp://<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.abc.com%2Fbook%2Fid" target="_blank" rel="nofollow noopener noreferrer" title="http://www.abc.com/book/id" ref="nofollow noopener noreferrer">www.abc.com/book/id</a>,
如果后端缺少对/book/id 的路由处理，将返回404错误</li>
</ul></div>  
</div>
            