
---
title: '为什么必须在主线程操作UI'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=5758'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 00:52:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=5758'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">从 UIKit 说起</h2>
<p>我们首先先了解一下 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.apple.com%2Fdocumentation%2Fuikit" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.apple.com/documentation/uikit" ref="nofollow noopener noreferrer">UIKit | Apple Developer Documentation</a> ，简单概括就是在 <strong>主线程</strong> 响应用户事件、展示视图。文档里面特别强调了一段话：</p>
<blockquote>
<p><strong>Important</strong><br>
Use UIKit classes only from your app’s main thread or main dispatch queue, unless otherwise indicated. This restriction particularly applies to classes derived from UIResponder or that involve manipulating your app’s user interface in any way.</p>
</blockquote>
<p>这段话强调了 UIKit 所有类（尤其是 UIResponder 的派生类），除非另有说明，否则只能在以下两个场景里面调用：</p>
<ul>
<li>main thread - 主线程</li>
<li>main dispatch queue - 主调度队列</li>
</ul>
<h2 data-id="heading-1"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fyeziahehe.com%2F2020%2F01%2F19%2FUIKit_in_main_thread%2F%23Why%25EF%25BC%259F" title="https://yeziahehe.com/2020/01/19/UIKit_in_main_thread/#Why%EF%BC%9F" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer"></a>Why？</h2>
<p>我们思考一下，在主线程来执行 UIKit 类，目的是为了保证线程安全。那么，从而就能知道 UIKit 一定 <strong>不是线程安全</strong> 的类，如果我们同时在多个线程来进行 UI 的异步操作，肯定造成读写问题，但是为了保证 UI 的流畅性，对 UIKit 做加锁则会导致大量的性能消耗，从而影响运行、渲染速度。</p>
<p>另外还有一点，根据事件响应机制（UIResponder）知道，所有的事件响应一定是在主线程。所以文档中规定 UI 操作一定要在主线程中串行执行，其实就是人为的加锁，既高效又同时保证了线程安全。</p></div>  
</div>
            