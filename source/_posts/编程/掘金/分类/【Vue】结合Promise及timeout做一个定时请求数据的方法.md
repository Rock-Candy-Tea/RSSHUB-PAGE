
---
title: '【Vue】结合Promise及timeout做一个定时请求数据的方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f114416bdc7f4305a438c61b4b94ce54~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 18:41:11 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f114416bdc7f4305a438c61b4b94ce54~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>需求：做一个方法，每10秒拿一次数据；当数据小于等于4时，调用promise失败时的回调函数reject并输出返回结果；当数据大于4小于11时，调用promise成功时的回调函数resolve并输出返回结果，同时判断当数据大于10时，停止并清除定时器。</p>
<p>代码如下:</p>
<pre><code class="copyable">data() &#123;
    return &#123;
      timer: null,//定时器
      num: 1,//默认从1开始计数
    &#125;
&#125;

 created() &#123;
    this.promiseTest(this.num)
  &#125;,

  methods: &#123;
    promiseTest(num) &#123;
      new Promise((resolve, reject) => &#123;
        this.timer = setTimeout(() => &#123;
        /**
         * 此处只做网络请求，不对请求得到的数据进行处理
         * resolve表示请求成功后的回调，其传的参数将作为then函数中成功函数的实参
         * reject表示请求失败后的回调，其传的参数将作为then函数中失败函数的实参
         */
          if (num > 4) &#123;
            resolve('第' + num + '次网络请求，输出大于4小于11的数：' + num)
          &#125; else &#123;
            reject('第' + num + '次网络请求，输出小于等于4的数：' + num)
          &#125;
        &#125;, 10000)
      &#125;).then((data) => &#123;
        console.log(data)
        this.num++
        if (this.num > 10) &#123;
          console.log('停止并清除定时器！')
          clearTimeout(this.timer)
        &#125; else &#123;
          this.promiseTest(this.num)
        &#125;
      &#125;, (err) => &#123;
        console.log(err)
        this.num++
        this.promiseTest(this.num)
      &#125;)
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果如图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f114416bdc7f4305a438c61b4b94ce54~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            