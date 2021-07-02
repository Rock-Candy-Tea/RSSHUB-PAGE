
---
title: '前端开发：深入使用proxy代理解决前端的跨域问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4259cc883fb34ddfa1fc9526bd001906~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 01:53:56 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4259cc883fb34ddfa1fc9526bd001906~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<blockquote>
<p>在前端领域中，跨域指的是浏览器允许向服务器发送跨域请求，进而克服Ajax只能同源使用的局限性限制。同源策略是一种约定，而且是浏览器中最基本也是最核心的安全功能，若缺少了该策略，浏览器非常容易被攻击；同源就是指“协议+域名+端口”都一样，就算有两个不同域名指向同一个IP地址也不能是同源。同源策略只有在浏览器中存在，服务器中确不存在，所以遇到需要跨域请求的地址将其转发服务器后委托服务器去请求即可。</p>
</blockquote>
<h3 data-id="heading-0">一、实际开发中遇到的跨域问题解决方法</h3>
<p>先来举一个简单的例子说明一下。首先来看一下跨域引起的报错提示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4259cc883fb34ddfa1fc9526bd001906~tplv-k3u1fbpfcp-watermark.image" alt="001.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>解决步骤</strong>：
打开Vue项目，然后在项目中找到config文件夹里面的index.js文件，然后找到proxyTable，然后添加以下代码段即可：</p>
<pre><code class="copyable">proxyTable: &#123;
          ['/java/mgr-auth']: &#123;  //替换代理地址名称
            target: 'http://dev-cloud.bc.com/mgr-auth', //代理地址
            changeOrigin: true, //可否跨域
            pathRewrite: &#123;
              ['^/java/mgr-auth']: '', //重写接口，去掉/java/mgr-auth
            &#125;
       &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8153b545c3204996a92bd5563e283778~tplv-k3u1fbpfcp-watermark.image" alt="002.png" loading="lazy" referrerpolicy="no-referrer">
设置完毕之后，重启一下服务，根据实际情况重启项目: <strong>npm run serve</strong>或者是<strong>npm run dev</strong>。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa2e1b21caab4376ab894dcb09481187~tplv-k3u1fbpfcp-watermark.image" alt="003.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87398c2f0b194afabef2a94cbcd9e571~tplv-k3u1fbpfcp-watermark.image" alt="004.jpeg" loading="lazy" referrerpolicy="no-referrer">
重启项目之后，在接口封装和调用那里进行设置，最后就可以正常访问接口，跨域问题随之解决。</p>
<h3 data-id="heading-1">二、常见的跨域情形</h3>
<p>常见的跨域情形通过URL链接来区分主要有6种：
①同域名，不同端口；②同域名，不同文件或者路径；③同域名，不同协议；④域名和域名对应相同的IP；⑤主域名相同，子域名不同；⑥不同域名。</p>
<h3 data-id="heading-2">三、跨域解决方法汇总</h3>
<p>解决跨域问题，一般可以通过三种方式来解决：①前端项目配置代理；②服务端配置跨域访问；③使用Chrome的扩展插件。</p>
<h4 data-id="heading-3">1、前端项目配置代理的方法解决跨域问题</h4>
<p>通过前端项目配置代理的方法解决跨域问题，具体步骤参考文章开头的案例来解决。</p>
<h4 data-id="heading-4">2、服务端配置跨域访问的方法解决跨域问题</h4>
<p>这个需要在服务端进行配置，具体操作设计后台操作，这里不再具体讲解。</p>
<h4 data-id="heading-5">3、通过Chrome的扩展插件的方法解决跨域问题</h4>
<p>涉及到qiang的问题，所以在保证有网的情况下搜索使用Allow CORS: Access-Control-Allow-Origin即可。</p>
<h3 data-id="heading-6">四、代理类型</h3>
<p>常见的代理类型大概有四种：
①基本代理；
②重写路径代理；
③支持HTTPS的代理；
④把请求代理到同一目标的代理。</p>
<h4 data-id="heading-7">1、基本代理的实例</h4>
<pre><code class="copyable">module.exports = &#123;
  dev: &#123;
    proxy: &#123;
      '/api': 'http://localhost:8080’
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">2、重写路径代理的实例</h4>
<pre><code class="copyable">module.exports = &#123;
  dev: &#123;
   proxy: &#123;
     '/api': &#123;
       target: 'http://localhost:8080’,
       pathRewrite: &#123;'^/api' : ''&#125;
     &#125;
   &#125;
 &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">3、支持HTTPS代理的实例</h4>
<pre><code class="copyable">module.exports = &#123;
  dev: &#123;
   proxy: &#123;
     '/api': &#123;
       target: 'https://dev-cloud.cc.com',
       secure: false
     &#125;
   &#125;
 &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">4、请求代理到同一目标的代理的实例</h4>
<pre><code class="copyable">module.exports = &#123;
  dev: &#123;
   proxy: [&#123;
     context: ['/auth', '/api'],
     target: 'http://localhost:8080’,
   &#125;]
 &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上就是本章全部内容，欢迎关注三掌柜的微信公众号“程序猿by三掌柜”，三掌柜的新浪微博“三掌柜666”，欢迎关注！</p></div>  
</div>
            