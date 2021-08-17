
---
title: 'express——中间件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6220'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 00:57:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=6220'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">中间件</h1>
<p>express的中间件，本质上就是一个function处理函数,express中间件的格式如下:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> express=<span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>);
<span class="hljs-keyword">const</span> app=express();
app.get(<span class="hljs-string">'/'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req,res,next</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(中间件<span class="hljs-string">')
&#125;)
app.listen(80,()=>&#123;
    console.log(express server is running at http:127.0.0.1:80);
&#125;)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>**注意：**中间件函数的形参列表中，必须包含next()参数，而路由处理函数中只包含req和res</p>
<p><strong>next()函数的作用：</strong>
next函数是实现多个中间件连续调用的关键，它表示把流转关系转交给下一个中间件或路由</p>
<p>实现一个简单的中间件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> express=<span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>);

<span class="hljs-keyword">const</span> app=express();
<span class="hljs-comment">//定义一个最简单的中间件</span>
<span class="hljs-keyword">const</span> mv=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req,res,next</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'这是一个最简单的中间件'</span>)
    <span class="hljs-comment">//把流转关系转交给下一个中间件或路由</span>
    next()
&#125;
app.listen(<span class="hljs-number">80</span>,<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>。log(<span class="hljs-string">'express server is running at http://127.0.0.1:80'</span>)
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">全局生效的中间件</h2>
<p>客户端发起的任何请求，到达服务器之后，都会触发的中间件，叫做全局生效的中间件。
用过调用app.use(中间件函数)，就可以调用一个全局生效的中间件，示例代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//常量mv所指向的就是一个中间件函数</span>
<span class="hljs-keyword">const</span> mv=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req,res,next</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'这是一个最简单的中间件函数'</span>);
    next()
&#125;
<span class="hljs-comment">//全局生效的中间件</span>
app.use(mv)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>中间件的作用</strong></p>
<p>多个中间件之间，共享同一份req和res,基于这样的特性，我们可以在上游的中间件中，同意为req和res添加自定义的属性或方法，供下游的中间件或路由进行使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> express=<span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>);

<span class="hljs-keyword">const</span> app=express();
<span class="hljs-comment">//定义一个最简单的中间件</span>
<span class="hljs-keyword">const</span> mv=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">req,res,next</span>)</span>&#123;
    <span class="hljs-comment">//获取请求到达服务器的时间</span>
    <span class="hljs-keyword">const</span> time=<span class="hljs-built_in">Date</span>.now();
    <span class="hljs-comment">//为req对象挂在自定义属性，从而把时间共享给后面的所有路由</span>
    req.startTime=time;<span class="hljs-comment">//startTime是自定义属性</span>
    
    <span class="hljs-comment">//把流转关系转交给下一个中间件或路由</span>
    next()
&#125;
  app.use(mv);

  app.get(<span class="hljs-string">'/'</span>,<span class="hljs-function">(<span class="hljs-params">req,res</span>)=></span>&#123;
      res.send(<span class="hljs-string">'get>>>>>>>>>>>>>>>>'</span>+req.startTime)

  &#125;)
  app.post(<span class="hljs-string">'/'</span>,<span class="hljs-function">(<span class="hljs-params">req,res</span>)=></span>&#123;
      res.send(<span class="hljs-string">'post...............'</span>+req.startTime)
  &#125;)
app.listen(<span class="hljs-number">80</span>,<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>。log(<span class="hljs-string">'express server is running at http://127.0.0.1:80'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>定义多个全局中间件</strong></p>
<p>可以使用app.use()连续定义多个全局中间件，客户端请求到达服务器之后，
会按照中间件定义的先后顺序依次进行调用，实例代码如下</p>
<pre><code class="copyable">const express=require('express');

const app=express()

//定义中间件
app.use((req,res,next)=>&#123;
  console.log('调用了第一个全局中间件');
  next()
&#125;)

app.use((req,res,next)=>&#123;
  console.log('调用了第二个全局中间件')
  next()
&#125;)

//路由
app.get('/user',function(req,res)&#123;
  res.send("home page")
&#125;)


app.listen(80,()=>&#123;
  console.log('express server running at http://127.0.0.1:80')
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            