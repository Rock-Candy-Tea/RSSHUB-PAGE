
---
title: '实现无感刷新token我是这样做的'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1889'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 00:26:57 GMT
thumbnail: 'https://picsum.photos/400/300?random=1889'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看:<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<h2 data-id="heading-0">前言</h2>
<p>最近在做需求的时候,涉及到登录token,产品提出一个问题:能不能让token过期时间长一点，我频繁的要去登录。</p>
<p>前端：后端，你能不能把token 过期时间设置的长一点。</p>
<p>后端：可以,但是那样做不安全，你可以用更好的方法。</p>
<p>前端：什么方法?</p>
<p>后端：给你刷新token的接口，定时去刷新token</p>
<p>前端：好，让我思考一下</p>
<h2 data-id="heading-1">需求</h2>
<p>当token过期的时候，刷新token,前端需要做到无感刷新token,即刷token时要做到用户无感知，避免频繁登录。
实现思路</p>
<ul>
<li>方法一</li>
</ul>
<p>后端返回过期时间，前端判断token过期时间,去调用刷新token接口</p>
<p>缺点：需要后端额外提供一个token过期时间的字段；使用了本地时间判断，若本地时间被篡改，特别是本地时间比服务器时间慢时，拦截会失败。</p>
<ul>
<li>方法二</li>
</ul>
<p>写个定时器，定时刷新token接口</p>
<p>缺点：浪费资源,消耗性能,不建议采用。</p>
<ul>
<li>方法三</li>
</ul>
<p>在响应拦截器中拦截，判断token 返回过期后，调用刷新token接口</p>
<h2 data-id="heading-2">实现</h2>
<p>axios的基本骨架,利用service.interceptors.response 进行拦截</p>
<pre><code class="copyable">import axios from 'axios'

service.interceptors.response.use(
  response => &#123;
    if (response.data.code === 409) &#123;
        return refreshToken(&#123; refreshToken: localStorage.getItem('refreshToken'), token: getToken() &#125;).then(res => &#123;
          const &#123; token &#125; = res.data
          setToken(token)
          response.headers.Authorization = `$&#123;token&#125;`
        &#125;).catch(err => &#123;
          removeToken()
          router.push('/login')
          return Promise.reject(err)
        &#125;)
    &#125;
    return response && response.data
  &#125;,
  (error) => &#123;
    Message.error(error.response.data.msg)
    return Promise.reject(error)
  &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">问题解决</h2>
<h3 data-id="heading-4">问题一：如何防止多次刷新token</h3>
<p>我们通过一个变量isRefreshing 去控制是否在刷新token的状态。</p>
<pre><code class="copyable">import axios from 'axios'

service.interceptors.response.use(
  response => &#123;
    if (response.data.code === 409) &#123;
      if (!isRefreshing) &#123;
        isRefreshing = true
        return refreshToken(&#123; refreshToken: localStorage.getItem('refreshToken'), token: getToken() &#125;).then(res => &#123;
          const &#123; token &#125; = res.data
          setToken(token)
          response.headers.Authorization = `$&#123;token&#125;`
        &#125;).catch(err => &#123;
          removeToken()
          router.push('/login')
          return Promise.reject(err)
        &#125;).finally(() => &#123;
          isRefreshing = false
        &#125;)
      &#125;
    &#125;
    return response && response.data
  &#125;,
  (error) => &#123;
    Message.error(error.response.data.msg)
    return Promise.reject(error)
  &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">问题二：同时发起两个或者两个以上的请求时，其他接口怎么解决</h3>
<p>当第二个过期的请求进来，token正在刷新，我们先将这个请求存到一个数组队列中，想办法让这个请求处于等待中，一直等到刷新token后再逐个重试清空请求队列。
那么如何做到让这个请求处于等待中呢？为了解决这个问题，我们得借助Promise。将请求存进队列中后，同时返回一个Promise，让这个Promise一直处于Pending状态（即不调用resolve），此时这个请求就会一直等啊等，只要我们不执行resolve，这个请求就会一直在等待。当刷新请求的接口返回来后，我们再调用resolve，逐个重试。最终代码：</p>
<pre><code class="copyable">import axios from 'axios'

// 是否正在刷新的标记
let isRefreshing = false
//重试队列
let requests = []
service.interceptors.response.use(
  response => &#123;
  //约定code 409 token 过期
    if (response.data.code === 409) &#123;
      if (!isRefreshing) &#123;
        isRefreshing = true
        //调用刷新token的接口
        return refreshToken(&#123; refreshToken: localStorage.getItem('refreshToken'), token: getToken() &#125;).then(res => &#123;
          const &#123; token &#125; = res.data
          // 替换token
          setToken(token)
          response.headers.Authorization = `$&#123;token&#125;`
        &#125;).catch(err => &#123;
        //跳到登录页
          removeToken()
          router.push('/login')
          return Promise.reject(err)
        &#125;).finally(() => &#123;
          isRefreshing = false
        &#125;)
      &#125; else &#123;
        // 返回未执行 resolve 的 Promise
        return new Promise(resolve => &#123;
          // 用函数形式将 resolve 存入，等待刷新后再执行
          requests.push(token => &#123;
            response.headers.Authorization = `$&#123;token&#125;`
            resolve(service(response.config))
          &#125;)
        &#125;)
      &#125;
    &#125;
    return response && response.data
  &#125;,
  (error) => &#123;
    Message.error(error.response.data.msg)
    return Promise.reject(error)
  &#125;
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">最后</h2>
<p>产品的需求就完成啦，不知道还有没有更好的解决方案，可以评论区留言，说出你的做法。</p>
<h1 data-id="heading-7">往期面试专题热门文章</h1>
<ul>
<li>HTML+CSS面试题：<a href="https://juejin.cn/post/6982186218456891423" target="_blank" title="https://juejin.cn/post/6982186218456891423">2021 6月份前端面试 | HTML +CSS</a></li>
<li>js面试题：<a href="https://juejin.cn/post/6981440373163819016" target="_blank" title="https://juejin.cn/post/6981440373163819016">30道 js面试题助我冲刺“20k”，飒飒飒</a></li>
<li>vue面试题：<a href="https://juejin.cn/post/6981049565709336590" target="_blank" title="https://juejin.cn/post/6981049565709336590">答对这些vue面试题,我是一个合格的中级前端开发工程师吗？</a></li>
<li>链表系列：<a href="https://juejin.cn/post/6983580875842093092" target="_blank" title="https://juejin.cn/post/6983580875842093092">面试官:能不能手写几道链表的基本操作</a></li>
</ul></div>  
</div>
            