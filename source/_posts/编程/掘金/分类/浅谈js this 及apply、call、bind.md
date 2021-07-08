
---
title: '浅谈js this 及apply、call、bind'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90f5d9182c174f02ac86018a0b829d83~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 01:49:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90f5d9182c174f02ac86018a0b829d83~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与新手入门的第2篇文章</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90f5d9182c174f02ac86018a0b829d83~tplv-k3u1fbpfcp-watermark.image" alt="src=http___dingyue.ws.126.net_2020_0520_5b0db6afj00qaloi40023c000hs00g4c.jpg&refer=http___dingyue.ws.126.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">字节跳动中有如下两道题，借此扩展一下</h1>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff7eb3d9777d43d68f35a0bfe51d9e2b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">this</h1>
<p>this 表示当前对象的一个引用，在JavaScript中，this会随着执行环境的改变而改变。实际上 this的最终指向的是那个调用它的对</p>
<p>一般 this 的指向有这几种情况:</p>
<p>单独使用，this 指向全局对象</p>
<p>非严格模式下，函数中的 this 指向全局对象</p>
<p>严格模式下，函数中的简单调用，this 是 undfined</p>
<p>在函数内部，this 的指向在函数定义的时候是不能确定的，只有函数执行的时候才能确定</p>
<p>在方法中，this 指代该调用方法的对象</p>
<h1 data-id="heading-2">apply，call，bind</h1>
<p>apply，call，bind是可以改变函数的this对象指向的方法。</p>
<p>apply()方法
apply()方法调用一个函数, 其具有一个指定的this值，以及作为一个数组（或类似数组的对象）提供的参数。</p>
<p>fn.apply(obj, [1, 2]);</p>
<p>call方法
call方法的第一个参数也是this的指向，后面传入的是一个参数列表（注意和apply传参的区别）。当一个参数为null或undefined的时候，表示指向window（在浏览器中），和apply一样，call也只是临时改变一次this指向，并立即执行。</p>
<p>fn.call(obj, 1, 2);</p>
<p>bind方法
bind方法和call很相似，第一参数也是this的指向，后面传入的也是一个参数列表(但是这个参数列表可以分多次传入，call则必须一次性传入所有参数)，但是它改变this指向后不会立即执行，而是返回一个永久改变this指向的函数。
fn.bind(obj, 1, 2);</p>
<p>总结 apply 、 call 、bind</p>
<p>三者都是用来改变函数的this对象的指向的</p>
<p>三者第一个参数都是this要指向的对象，也就是想指定的上下文</p>
<p>三者都可以利用后续参数传参。bind 是返回对应函数，便于稍后调用；apply 、call 则是立即调用。</p>
<h1 data-id="heading-3">手写apply、call、bind</h1>
<p>apply</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e007763effd42ceaaf586a7da762420~tplv-k3u1fbpfcp-watermark.image" alt="apply.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>call</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b438e0edcc2d4fc293e7a4a71a8c47da~tplv-k3u1fbpfcp-watermark.image" alt="call.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>bind</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e66900dfe4d4c09a33cf23938d36727~tplv-k3u1fbpfcp-watermark.image" alt="bind.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            