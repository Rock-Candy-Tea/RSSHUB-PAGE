
---
title: '手撕Promise'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8568'
author: 掘金
comments: false
date: Sun, 09 May 2021 02:13:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=8568'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;font-family:PingFang SC,Microsoft YaHei,sans-serif;word-break:break-word;font-size:16px;overflow-x:hidden&#125;.markdown-body li,.markdown-body p&#123;font-size:.9em;letter-spacing:2px;color:#333&#125;.markdown-body li code,.markdown-body p code&#123;font-family:PingFang SC,Microsoft YaHei,sans-serif;font-weight:500;background:rgba(119,175,156,.22);border-radius:0;padding:2px 5px;border-left:2px solid #77af9c;color:#6e7783&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;display:table;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3&#123;background:rgba(119,175,156,.22);color:#6e7783;padding:5px 10px;border:1px solid rgba(119,175,156,.22);transition:all .5s&#125;.markdown-body h1:hover,.markdown-body h2:hover,.markdown-body h3:hover&#123;border:1px solid #77af9c&#125;.markdown-body h1&#123;font-size:1.6em&#125;.markdown-body h2&#123;font-size:1.4em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;text-align:center&#125;.markdown-body h4:after,.markdown-body h5:after,.markdown-body h6:after&#123;content:"/";color:#77af9c;font-weight:400;margin-left:15px&#125;.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"/";color:#77af9c;font-weight:400;margin-right:15px&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;display:block;color:#77af9c;font-size:400;font-weight:400&#125;.markdown-body hr&#123;margin-top:20px;margin-bottom:20px;border:none;border-top:2px solid #77af9c&#125;.markdown-body blockquote&#123;position:relative;line-height:1.8;font-style:400;text-indent:0;margin:0;padding:10px;border:1px solid #fff;color:#888;background:rgba(119,175,156,.22);transition:border .5s&#125;.markdown-body blockquote:hover&#123;border-style:solid;border-color:#77af9c&#125;.markdown-body blockquote:before&#123;content:"“";display:inline;color:#6e7783;font-size:4em;font-family:Arial,serif;line-height:1em&#125;.markdown-body blockquote:after&#123;position:absolute;content:"Tips";display:inline;bottom:5px;right:15px;color:#6e7783;font-size:.9em&#125;.markdown-body blockquote p&#123;display:inline&#125;.markdown-body table&#123;border-collapse:collapse;width:auto;min-width:50%;font-size:.8em&#125;.markdown-body table tr th&#123;text-align:center;border:1px solid #77af9c;background:rgba(119,175,156,.22);font-weight:500;padding:5px&#125;.markdown-body table tr td&#123;text-align:center;border:1px solid rgba(119,175,156,.22);padding:5px&#125;.markdown-body pre&#123;font-family:Arial,serif;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-family:Arial,serif;border-left:2px solid #77af9c;display:block;padding:16px 12px;margin:0;font-size:.9em;color:#6e7783;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;color:#77af9c;font-weight:400;background:#fff;border-bottom:none;padding:2px 5px;text-decoration:none;transition:all .5s&#125;.markdown-body a:hover&#123;background:rgba(119,175,156,.22);color:#6e7783&#125;.markdown-body strong&#123;font-weight:700;color:#6e7783&#125;</style><h1 data-id="heading-0">手写一个符合Promise/A+规范的Promise</h1>
<p><a href="https://promisesaplus.com/" target="_blank" rel="nofollow noopener noreferrer">Promise/A+规范</a><br>
<a href="https://zhuanlan.zhihu.com/p/183801144?utm_source=qq&utm_medium=social&utm_oi=1108713620862693376" target="_blank" rel="nofollow noopener noreferrer">参考文献这个博主真的写的特别好</a><br>
首先我们应该知道的事情：<br>
在Promise中：<br></p>
<ul>
<li>首先我们在调用Promise的时候会返回一个Promise对象<br></li>
<li>构建Promise时，会给其传入一个函数参数executor,这个函数立即执行<br></li>
<li>当这个函数运行成功之后，会调用resolve函数，如果运行失败，会调用rejected函数</li>
<li>Promise状态不可逆，不能停止，同时调用 resolve 函数和 reject 函数，默认会采取第一次调用的结果。</li>
</ul>
<pre><code class="copyable">    const PENDING = "PENDING";
    const FULFILLED = "FULFILLED";
    const REJECTED = "REJECTED"
    class Promise &#123;
      constructor(executor) &#123;
        this.status = PENDING;
        this.value = undefined;
        this.reason = undefined;
        this.onResolvedCallbacks = [] // 专门存放成功的回调函数
        this.onRejectedCallbacks = [] // 专门存放失败的回调函数
        //成功调用的函数
        let resolved = (value) => &#123;
          if (this.status === PENDING) &#123;
            this.status = FULFILLED;
            this.value = value;
            this.onResolvedCallbacks.forEach(fn => &#123; fn() &#125;)
          &#125;
        &#125;
        //失败调用的函数
        let rejected = (reason) => &#123;
          if (this.status === PENDING) &#123;
            this.status = REJECTED;
            this.reason = reason;
            this.onRejectedCallbacks.forEach(fn => &#123; fn() &#125;)// 需要让成功的方法依次执行
          &#125;
        &#125;
        //立即执行executor
        try &#123;
          executor(resolved, rejected)
        &#125; catch (error) &#123;
          rejected(error)
        &#125;
        //then方法


      &#125;
      then(onFulfilled, onRejected) &#123;
        if (this.status === FULFILLED) &#123;
          onFulfilled(this.value)
        &#125;
        if (this.status === REJECTED) &#123;
          onRejected(this.reason)
        &#125;
        if (this.status === PENDING) &#123;//如果状态是等待，就将回调函数push到专门存放成功/失败的回调函数
          this.onResolvedCallbacks.push(() => &#123; onFulfilled(this.value) &#125;)
          this.onRejectedCallbacks.push(() => &#123; onRejected(this.reason) &#125;)
        &#125;
      &#125;
    &#125;
    const promise = new Promise((resolve, reject) => &#123;
      setTimeout(() => &#123;
        resolve('成功');
      &#125;, 1000);
    &#125;).then(
      (data) => &#123;
        console.log('success', data)
      &#125;,
      (err) => &#123;
        console.log('faild', err)
      &#125;
    )
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            