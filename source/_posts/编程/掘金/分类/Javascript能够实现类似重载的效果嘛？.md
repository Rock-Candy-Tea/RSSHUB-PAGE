
---
title: 'Javascript能够实现类似重载的效果嘛？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2564eab51644e239e3ed961901bc1dd~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 01 May 2021 02:41:12 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2564eab51644e239e3ed961901bc1dd~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0"><strong>！！！首先javascript没有传统意义上的函数重载</strong></h1>
<p>另外我们要先清楚什么是函数重载</p>
<p>函数重载就是函数名相同，函数的参数列表不同(包括参数个数和参数类型)，根据参数的不同去执行不同的操作。</p>
<p>我们来看一个具体的例子：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2564eab51644e239e3ed961901bc1dd~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-01 下午3.52.14.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1"><strong>第一种实现重载的方法通过判断arguments长度来实现</strong></h1>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72a2bfff87574cbdb83705a9a5591534~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-01 下午3.56.49.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>先来看一个需求，我们有一个 people 对象，people 对象的values 属性中存着一些名字。</p>
<pre><code class="copyable">let people = &#123;
  values: ["Michael Jackson", "Michael Jordan", "Kobe Bryant", "Klay Thompson"],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个需求中 selfName方法 需要根据参数的个数不同而执行不同的操作，下来我们通过一个 addMethod 函数，来在 people 对象中添加这个 selfName 方法。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45ba1fc5141d495d9809ca62f638f474~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-01 下午6.09.49.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面是完整的代码</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/942dd3fa3f9d49e0b45d72eadf528ec3~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-01 下午6.11.47.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/659be6a144d24ef5a893d40cd2705156~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-01 下午6.12.06.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d50edacc43f94c6bb1cc7120bf3a0146~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-01 下午6.12.18.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>addMethod 函数是利用了闭包的特性，通过变量 old 将每个函数连接了起来，让所有的函数都留在内存中。</p>
<p>每调用一次 addMethod 函数，就会产生一个 old，形成一个闭包。</p>
<p>我们通过console.dir(people.selfName);在控制台来看一下</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13438fa7152e4191bc83f434f55cd1af~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-01 下午6.19.37.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当我们在末尾执行的时候，首先会去调用最后保存的people里面的selfName，结果这时候selfName里面的fn需要两个参数不匹配，就会去调用old，这样层层查找最终就会找到不带参数的函数，结果就执行来第一次执行addMethod里面的函数内容，最终输出了一个完整的数组，其他的打印类似这样的流程。</p></div>  
</div>
            