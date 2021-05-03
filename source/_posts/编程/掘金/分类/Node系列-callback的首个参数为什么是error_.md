
---
title: 'Node系列-callback的首个参数为什么是error_'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4814'
author: 掘金
comments: false
date: Sun, 02 May 2021 04:59:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=4814'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>原文： <a href="https://nodejs.org/en/knowledge/errors/what-are-the-error-conventions/" target="_blank" rel="nofollow noopener noreferrer">nodejs.org/en/knowledg…</a></p>
<p>对于Node.js来说，异步函数很重要的一个理念就是<code>callback</code>回调函数来处理异步操作的返回结果。</p>
<p>写过一些Node的相关同学一开始可能会好奇为什么回调函数<code>callback</code>的第一个参数总是<code>error</code>呢？</p>
<p>在Node.js中，这种实现被认为是一种处理异步操作的错误的标准操作。如果<code>errro</code>参数是一个<code>Error</code>对象，我们认为异步操作发生的错误； 反之如果正确，则为<code>null</code>。</p>
<p>光说不练假把式，下面是一个demo：</p>
<pre><code class="copyable">var isTrue = function(value, callback) &#123;
  if (value === true) &#123;
    callback(null, "Value was true.");
  &#125;
  else &#123;
    callback(new Error("Value is not true!"));
  &#125;
&#125;

var callback = function (error, retval) &#123;
  if (error) &#123;
    console.log(error);
    return;
  &#125;
  console.log(retval);
&#125;

// Note: when calling the same asynchronous function twice like this, you are in a race condition.
// You have no way of knowing for certain which callback will be called first when calling the functions in this manner.

isTrue(false, callback);
isTrue(true, callback);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果：</p>
<pre><code class="copyable">&#123; stack: [Getter/Setter],
  arguments: undefined,
  type: undefined,
  message: 'Value is not true!' &#125;
Value was true.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的例子可以看出，如果没有发生错误的时候，回调函数的第一个参数就是<code>null</code>。然而如果存在错误，第一个参数就是一个<code>Error</code>对象（此时只需要传入一个参数即可）。</p>
<p>从上面的例子其实可以看出为什么<code>error</code>需要作为回调函数的第一个参数，这里在简单总结一下：</p>
<p>通过将<code>error</code>参数作为回调函数的第一个参数，可以让开发者很容易判断是否出现的错误，从而及时截断，不再继续执行其他操作。</p>
<p>另外一个角度来看：</p>
<p>如果回调函数的第一个参数不是<code>error</code>，那开发者应该怎么样去判断异步操作的结果是否符合预期呢？答案只有一个：只能去判断回调函数的唯一参数【异步操作的返回结果】是否符合你的预期，如果不符合预期，执行对应操作；反之，执行符合预期的操作。</p>
<p>显然，这种方式对于开发者不太友好，也不太方便。</p>
<p>因此Node.js把回调函数的第一个参数作为<code>error</code>，表示异步操作返回结果是否符合预期来作为一个标准规范。</p></div>  
</div>
            