
---
title: '如何解决异步接口请求快慢不均导致的数据错误问题？ - DevUI'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 07 May 2021 15:56:36 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://devui.design/" target="_blank" rel="nofollow noopener noreferrer">DevUI</a> 是一款面向企业中后台产品的开源前端解决方案，它倡导<code>沉浸</code>、<code>灵活</code>、<code>至简</code>的设计价值观，提倡设计者为真实的需求服务，为多数人的设计，拒绝哗众取宠、取悦眼球的设计。如果你正在开发 <code>ToB</code> 的<code>工具类产品</code>，DevUI 将是一个很不错的选择！</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image" alt="Kagol.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">引言</h1>
<p>搜索功能，我想很多业务都会涉及，这个功能的特点是：</p>
<ul>
<li>用户可以在输入框中输入一个关键字，然后在一个列表中显示该关键字对应的数据；</li>
<li>输入框是可以随时修改/删除全部或部分关键字的；</li>
<li>如果是实时搜索🔍（即输入完关键字马上出结果，不需要额外的操作或过多的等待），接口调用将会非常频繁。</li>
</ul>
<p>实时搜索都会面临一个通用的问题，就是：</p>
<blockquote>
<p>浏览器请求后台接口都是异步的，如果先发起请求的接口后返回数据，列表/表格中显示的数据就很可能会是错乱的。</p>
</blockquote>
<h1 data-id="heading-1">问题重现</h1>
<p>最近测试提了一个搜索（PS：此处的搜索🔍就是用 DevUI 新推出的 <a href="https://juejin.cn/post/6956612556710477860" target="_blank">CategorySearch</a> 组件实现的）相关的缺陷单，就涉及到了上述问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91022a7278ce408ba882bdda2a70d62d~tplv-k3u1fbpfcp-watermark.image" alt="1-1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个bug单大致意思是：</p>
<blockquote>
<p>搜索的时候，连续快速输入或者删除关键字，搜索结果和搜索关键字不匹配。</p>
</blockquote>
<p>从缺陷单的截图来看，本意是要搜索关键字<code>8.4.7迭代】</code>，表格中的实际搜索结果是<code>8.4.7迭代】过</code>关键字的数据。</p>
<p>缺陷单的截图还非常贴心地贴了两次请求的信息：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd4260a598914a3e924599aaa4688b86~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>作为一名“有经验的”前端开发，一看就是一个通用的技术问题：</p>
<ol>
<li>浏览器从服务器发起的请求都是异步的；</li>
<li>由于前一次请求服务器返回比较慢，还没等第一次请求返回结果，后一次请求就发起了，并且迅速返回了结果，这时表格肯定显示后一次的结果；</li>
<li>过了2秒，第一次请求的结果才慢吞吞地返回了，这时表格错误地又显示了第一次请求的结果；</li>
<li>最终导致了这个bug。</li>
</ol>
<p>怎么解决呢？</p>
<p>在想解决方案之前，得想办法必现这个问题，靠后台接口是不现实的，大部分情况下后台接口都会很快返回结果。</p>
<p>所以要必现这个问题，得先模拟慢接口。</p>
<h1 data-id="heading-2">模拟慢接口</h1>
<p>为了快速搭建一个后台服务，并模拟慢接口，我们选择 <a href="https://koajs.com/" target="_blank" rel="nofollow noopener noreferrer">Koa</a> 这个轻量的 Node 框架。</p>
<h2 data-id="heading-3">快速开始</h2>
<p>Koa 使用起来非常方便，只需要：</p>
<ol>
<li>新建项目文件夹：<code>mkdir koa-server</code></li>
<li>创建 package.json：<code>npm init -y</code></li>
<li>安装 Koa：<code>npm i koa</code></li>
<li>编写服务代码：<code>vi app.js</code></li>
<li>启动：<code>node app.js</code></li>
<li>访问：<code>http://localhost:3000/</code></li>
</ol>
<h3 data-id="heading-4">编写服务代码</h3>
<p>使用以下命令创建 app.js 启动文件：</p>
<pre><code class="copyable">vi app.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在文件中输入以下 3 行代码，即可启动一个 Koa 服务：</p>
<pre><code class="copyable">const Koa = require('koa'); // 引入 Koa
const app = new Koa(); // 创建 Koa 实例
app.listen(3000); // 监听 3000 端口
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">访问</h3>
<p>如果没有在3000端口启动任务服务，在浏览器访问：</p>
<p><a href="http://localhost:3000/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:3000/</a></p>
<p>会显示以下页面：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95abe405d5fd47f199c70b2c8db3c4f3~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>启动了我们的 Koa Server 之后，访问：</p>
<p><a href="http://localhost:3000/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:3000/</a></p>
<p>会显示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cd1ccceda0d43018528453bb15fd5fa~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">get 请求</h2>
<p>刚才搭建的只是一个空服务，什么路由都没有，所以显示了<code>Not Found</code>。</p>
<p>我们可以通过中间件的方式，让我们的 Koa Server 显示点儿东西。</p>
<p>由于要增加一个根路由，我们先安装路由依赖</p>
<pre><code class="copyable">npm i koa-router
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后引入 Koa Router</p>
<pre><code class="copyable">const router = require('koa-router')();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着是编写get接口</p>
<pre><code class="copyable">router.get('/', async (ctx, next) => &#123;
  ctx.response.body = '<p>Hello Koa Server!</p>';
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后别忘了使用路由中间件</p>
<pre><code class="copyable">app.use(router.routes());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改完代码需要重启 Koa 服务，为了方便重启，我们使用 pm2 这个 Node 进程管理工具来启动/重启 Koa 服务，使用起来也非常简单：</p>
<ul>
<li>全局安装 pm2：npm i -g pm2</li>
<li>启动 Koa Server：pm2 start app.js</li>
<li>重启 Koa Server：pm2 restart app.js</li>
</ul>
<p>重启完 Koa Server，再次访问</p>
<p><a href="http://localhost:3000/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:3000/</a></p>
<p>会显示以下内容：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d136ca6d5404485aa59d162aeda33aa5~tplv-k3u1fbpfcp-watermark.image" alt="4-1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">post 请求</h2>
<p>有了以上基础，就可以写一个 post 接口，模拟慢接口啦！</p>
<p>编写 post 接口和 get 接口很类似：</p>
<pre><code class="copyable">router.post('/getList', async (ctx, next) => &#123;
  ctx.response.body = &#123;
    status: 200,
    msg: '这是post接口返回的测试数据',
    data: [1, 2, 3]
  &#125;;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时我们可以使用 Postman 调用下这个 post 接口，如期返回：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49e6fb19f5a040adafc016d544b5e3ef~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">允许跨域</h2>
<p>我们尝试在 NG CLI 项目里调用这个 post 接口：</p>
<pre><code class="copyable">this.http.post('http://localhost:3000/getList', &#123;
  id: 1,
&#125;).subscribe(result => &#123;
  console.log('result:', result);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是在浏览器里直接调用，却得不到想要的结果：</p>
<ul>
<li>result 没有打印出来</li>
<li>控制台报错</li>
<li>Network请求也是红色的</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6616b351d65140b594f8baa476a89be0~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于本地启动的项目端口号（4200）和 Koa Server 的（3000）不同，浏览器认为这个接口跨域，因此拦截了。</p>
<p>NG CLI 项目本地链接：</p>
<p><a href="http://localhost:4200/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:4200/</a></p>
<p>Koa Server 链接：</p>
<p><a href="http://localhost:3000/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:3000/</a></p>
<p>Koa 有一个中间件可以允许跨域：<code>koa2-cors</code></p>
<p>这个中间件的使用方式，和路由中间件很类似。</p>
<p>先安装依赖：</p>
<pre><code class="copyable">npm i koa2-cors
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后引入：</p>
<pre><code class="copyable">const cors = require('koa2-cors');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再使用中间件：</p>
<pre><code class="copyable">app.use(cors());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时我们再去访问：</p>
<p><a href="http://localhost:4200/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:4200/</a></p>
<p>就能得到想要的结果啦！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41af8a8902554f608b234d21d081b348~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">慢接口</h2>
<p>post 接口已经有了，怎么模拟慢接口呢？</p>
<p>其实就是希望服务器延迟返回结果。</p>
<p>在 post 接口之前增加延迟的逻辑：</p>
<pre><code class="copyable">  async function delay(time) &#123;
    return new Promise(function(resolve, reject) &#123; 
      setTimeout(function() &#123;
        resolve();
      &#125;, time);
    &#125;);
  &#125;

  await delay(5000); // 延迟 5s 返回结果

  ctx.response.body = &#123; ... &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次访问 getList 接口，发现前面接口会一直<code>pending</code>，5s 多才真正返回结果。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad9f89986c754b1a81aa9b2549698c3f~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0023a013aa37415eab1a7874c66bc7cc~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-10">取消慢接口请求</h1>
<p>能模拟慢接口，就能轻易地必现测试提的问题啦！</p>
<blockquote>
<p>先必现这个问题，然后尝试修复这个问题，最后看下这个问题还出不出现，不出现说明我们的方案能解决这个bug，问题还有说明我们得想别的办法。</p>
</blockquote>
<p>这是修复bug正确的打开方式。</p>
<p>最直观的方案就是再发起第二次请求之后，如果第一次请求未返回，那就直接取消这次请求，使用第二次请求的返回结果。</p>
<p>怎么取消一次http请求呢？</p>
<p>Angular 的异步事件机制是基于 RxJS 的，取消一个正在执行的 http 请求非常方便。</p>
<p>前面已经看到 Angular 使用 HttpClient 服务来发起 http 请求，并调用subscribe 方法来订阅后台的返回结果：</p>
<pre><code class="copyable">this.http.post('http://localhost:3000/getList', &#123;
  id: 1,
&#125;).subscribe(result => &#123;
  console.log('result:', result);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要取消 http 请求，我们需要先把这个订阅存到组件一个变量里：</p>
<pre><code class="copyable">private getListSubscription: Subscription;

this.getListSubscription = this.http.post('http://localhost:3000/getList', &#123;
  id: 1,
&#125;).subscribe(result => &#123;
  console.log('result:', result);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在重新发起 http 请求之前，取消上一次请求的订阅即可。</p>
<pre><code class="copyable">this.getListSubscription?.unsubscribe(); // 重新发起 http 请求之前，取消上一次请求的订阅

this.getListSubscription = this.http.post(...);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">其他 http 库如何取消请求</h1>
<p>至此这个缺陷算是解决了，其实这是一个通用的问题，不管是在什么业务，使用什么框架，都会遇到异步接口慢导致的数据错乱问题。</p>
<p>那么，如果使用 fetch 这种浏览器原生的 http 请求接口或者 <a href="https://axios-http.com/" target="_blank" rel="nofollow noopener noreferrer">axios</a> 这种业界广泛使用的 http 库，怎么取消正在进行的 http 请求呢？</p>
<h2 data-id="heading-12">fetch</h2>
<p>先来看下 fetch，fetch 是浏览器原生提供的 AJAX 接口，使用起来也非常方便。</p>
<p>使用 fetch 发起一个 post 请求：</p>
<pre><code class="copyable">fetch('http://localhost:3000/getList', &#123;
   method: 'POST',
　　headers: &#123;
　　　　'Content-Type': 'application/json;charset=utf-8'
　　&#125;,
　　body: JSON.stringify(&#123;
    id: 1
　　&#125;)
&#125;).then(result => &#123;
  console.log('result', result);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以使用 <code>AbortController</code> 来实现请求取消：</p>
<pre><code class="copyable">this.controller?.abort(); // 重新发起 http 请求之前，取消上一次请求

const controller = new AbortController(); //  创建 AbortController 实例
const signal = controller.signal;
this.controller = controller;

fetch('http://localhost:3000/getList', &#123;
   method: 'POST',
　　headers: &#123;
　　　　'Content-Type': 'application/json;charset=utf-8'
　　&#125;,
　　body: JSON.stringify(&#123;
    id: 1
　　&#125;),
  signal, // 信号参数，用来控制 http 请求的执行
&#125;).then(result => &#123;
  console.log('result', result);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">axios</h2>
<p>再来看看 axios，先看下如何使用 axios 发起 post 请求。</p>
<p>先安装：</p>
<pre><code class="copyable">npm i axios
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再引入：</p>
<pre><code class="copyable">import axios from 'axios';
<span class="copy-code-btn">复制代码</span></code></pre>
<p>发起 post 请求：</p>
<pre><code class="copyable">axios.post('http://localhost:3000/getList', &#123;
  headers: &#123;
    'Content-Type': 'application/json;charset=utf-8'
  &#125;,
  data: &#123;
    id: 1,
  &#125;,
&#125;)
.then(result => &#123;
  console.log('result:', result);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>axios 发起的请求可以通过 cancelToken 来取消。</p>
<pre><code class="copyable">this.source?.cancel('The request is canceled!');

this.source = axios.CancelToken.source(); // 初始化 source 对象

axios.post('http://localhost:3000/getList', &#123;
  headers: &#123;
    'Content-Type': 'application/json;charset=utf-8'
  &#125;,
  data: &#123;
    id: 1,
  &#125;,
&#125;, &#123; // 注意是第三个参数
  cancelToken: this.source.token, // 这里声明的 cancelToken 其实相当于是一个标记或者信号
&#125;)
.then(result => &#123;
  console.log('result:', result);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">小结</h1>
<p>本文通过实际项目中遇到的问题，总结缺陷分析和解决的通用方法，并对异步接口请求导致的数据错误问题进行了深入的解析。</p>
<h1 data-id="heading-15">加入我们</h1>
<p>我们是DevUI团队，欢迎来这里和我们一起打造优雅高效的人机设计/研发体系。招聘邮箱：<a href="mailto:muyang2@huawei.com">muyang2@huawei.com</a>。</p>
<p>文/DevUI Kagol</p>
<p>往期文章推荐</p>
<p><a href="https://juejin.cn/post/6956155033410863134" target="_blank">《号外号外！DevUI Admin V1.0 发布啦！》</a></p>
<p><a href="https://juejin.cn/post/6956988395016945701" target="_blank">《让我们一起建设 Vue DevUI 项目吧！🥳 》</a></p>
<p><a href="https://juejin.cn/post/6956612556710477860" target="_blank">《CategorySearch分类搜索组件初体验》</a></p>
<p><a href="https://juejin.cn/post/6953243547621392421" target="_blank">《对DevUI组件库王哥的专访》</a></p>
<p><a href="https://juejin.cn/post/6952881796442750984" target="_blank">《2021年最值得推荐的7个Angular前端组件库》</a></p></div>  
</div>
            