
---
title: 'Koa的上下文实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db6e18688d23467d97b79b74e2d011f9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 00:06:40 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db6e18688d23467d97b79b74e2d011f9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>Koa和Express 都是基于 Node.js 平台的下一代 web 开发框架，由 Express 幕后的原班人马打造，</p>
<h2 data-id="heading-1">express和Koa的两者区别简述：</h2>
<ul>
<li>Express 源码是 es5 写的，koa 源码基于 es6 写的</li>
<li>Express 比较全 内置了很多功能；koa 内部核心非常小巧（我们可以通过拓展的插件进行扩展）</li>
<li>Express 和 Koa 都是可以自己去使用实现 mvc 功能的，没有约束</li>
<li>Express 处理异步的方式是回调函数，函数处理异步的方式是 async+await</li>
</ul>
<h1 data-id="heading-2">Koa的启动</h1>
<h2 data-id="heading-3">初始化项目</h2>
<p><code>npm init -y</code></p>
<h2 data-id="heading-4">Koa 的安装</h2>
<p><code> npm install koa</code></p>
<h2 data-id="heading-5">Koa 的use 方法</h2>
<ul>
<li>use 是一个中间件，每次执行（请求）会产生一个上下文 ctx</li>
<li>可以通过ctx.body 来实现node 中res.en()的效果</li>
<li>上下文 ctx包含了主要部分
<ol>
<li>app 当前应用实例，</li>
<li>req，res对应 原生 node 中的 req，res</li>
<li>koa 自己封装的 request 和 response 是对原生的 req 和 res 进行的一层抽象，和扩展，功能更多</li>
</ol>
</li>
</ul>
<pre><code class="copyable">const Koa = require("koa");
const app = new Koa();
app.use((ctx) => 
   ctx.body = "hello1111"; //ctx.body 相当于node 里sever中 res.en()的功能 给浏览器写入数据
   console.log(ctx);//打印ctx，查看属性
&#125;);
app.listen(3000, function () &#123;
  console.log("server start 3000");
&#125;); //监听端口号 ，同我们的的node中http的listen方法

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">ctx上下的打印结果：
&#123;
request: &#123;
method: 'GET',
url: '/',
header: &#123;
host: 'localhost:3000',
connection: 'keep-alive',
'cache-control': 'max-age=0',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
'sec-ch-ua-mobile': '?0',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,_/_;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
cookie: '\_uab_collina=161916550781026855009784; zoe=27'
&#125;
&#125;,
response: &#123;
status: 404,
message: 'Not Found',
header: [Object: null prototype] &#123;&#125;
&#125;,
app: &#123; subdomainOffset: 2, proxy: false, env: 'development' &#125;,
originalUrl: '/',
req: '<original node req>',
res: '<original node res>',
socket: '<original node socket>'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>话不多说 从上下文入手开始Koa的实现</p>
<h1 data-id="heading-6">Koa上下文的实现</h1>
<h2 data-id="heading-7">目录创建</h2>
<p>参考下 koa 的源码 lib 下的文件结构 依次新建对应文
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db6e18688d23467d97b79b74e2d011f9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">package.json</h3>
<p>设置入口文件</p>
<pre><code class="copyable">&#123;
    "main":"lib/application.js"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">context.js，request.js，response.js 依次创建</h3>
<pre><code class="copyable">const response = &#123;&#125;;
module.exports = response;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">application.js</h3>
<pre><code class="copyable">const http = require("http");
const context = require("./context");
const request = require("./request");
const response = require("./response");
class Application &#123;
  constructor() &#123;
  &#125;
&#125;
module.exports = Application;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">koa启动server时listen实现</h2>
<h3 data-id="heading-12">思路：</h3>
<ol>
<li>接收两个参数 端口号和callback</li>
<li>内部封装node的 listen 并将实例上listen参数传入</li>
</ol>
<h3 data-id="heading-13">实现：</h3>
<pre><code class="copyable">//handleRequest待实现
  listen(...args) &#123;
    const server = http.createServer(this.handleRequest);
    server.listen(...args);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>调用：同Koa框架相同</li>
</ul>
<pre><code class="copyable">app.listen(3000, function () &#123;
  console.log("server start 3000");
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">use实现</h2>
<h3 data-id="heading-15">use的作用</h3>
<p>每次执行（请求）会产生一个上下文 ctx</p>
<h3 data-id="heading-16">思路：</h3>
<ul>
<li>use用于保存用户写入的函数</li>
<li>服务启动时候 触发用户保存的use，创建上下文ctx</li>
<li>每一个实例每一个请求对应的use里的ctx都要相互独立</li>
<li>ctx 里要包含 node 原生的req和res 还有ctx自己扩展的request和response</li>
</ul>
<h3 data-id="heading-17">实现：</h3>
<ul>
<li>application.js</li>
</ul>
<pre><code class="copyable">    constructor() &#123;
        // 初始化 创建实每一个实例自己的上下文，原理是用了原型继承
        this.context = Object.create(context);
        //同理 初始化request和response
        this.request = Object.create(request);
        this.response = Object.create(response);
     &#125;
    use(fn) &#123;
        // 保存用户写的函数
        this.fn = fn;
      &#125;
   // 上下文的实现
    createContext(req, res) &#123;
    let ctx = Object.create(this.context);
    // 注意这里 为什么不用 ctx=context  怕上下文相互影响
    // Object.create 做中间层包装（隔离） ，可以保证每一个请求产生的上下文是独立空间是自己的上下文，但又可以获取同一个公共上下文
    // 同理 创建每次请求自己的request 和response
    let request = Object.create(this.request);
    let response = Object.create(this.response);
    // ctx自己扩展的请求和响应
    ctx.request = request;
    ctx.response = response;

    // 原生请求
    ctx.req = ctx.request.req = req; //默认上下文包含原生的req，且自己的requst需要可以取到原生的req
    ctx.res = res; //默认上下文包含原生的res
    return ctx;
  &#125;
   handleRequest = (req, res) => &#123;
    //每次请求都会执行次方法，然后创建自己的上下文
    let ctx = this.createContext(req, res);
    // 服务启动时候 触发用户保存的use
    this.fn(ctx); 
  &#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>request.js</li>
</ul>
<p>用于实现上下文ctx的request</p>
<pre><code class="copyable">const url = require("url");

const request = &#123;
  get url() &#123;
  //application里 request 是被上下文ctx调用的 所以此处this指向上下文 通过上下文去取到node 原生的re.url就ok
    return this.req.url; 
  &#125;,
  //同理实现 通过request 获取请求path和请求query
  get path() &#123;
    return url.parse(this.req.url).pathname;
  &#125;,
  get query() &#123;
    return url.parse(this.req.url).query;
  &#125;,
&#125;;
module.exports = request;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">测试</h3>
<h4 data-id="heading-19">调用</h4>
<ul>
<li>1.server.js</li>
</ul>
<pre><code class="copyable">const Koa = require("./koa");

// 使用koa就是创造一个应用实例
const app = new Koa();
app.use((ctx) => &#123;
console.log(ctx.req.url)
console.log(ctx.request.req.url)
console.log(ctx.request.url)//app里request 被Object.create 包了两次 寻找url 相当于：ctx.request.__proto__.__proto__
console.log(ctx.url)
console.log('--------本次console end')
&#125;);
app.listen(3000, function () &#123;
  console.log("server start 3000");
&#125;); //监听端口号 ，同我们的的node中http的listen方法

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">测试结果</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d291d27d2da4afb9e14feaecd5317d9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c64be84cb6fc4c8f87dae7e938a84df6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>console.log(ctx.url)</code> 没有打印成功</p>
<h5 data-id="heading-21">ctx.url实现</h5>
<ul>
<li>context.js</li>
</ul>
<ol>
<li>同request.js的实现思想相同 我们这里的this指向的是最终调用的那个对象 也就是我们的上下文ctx</li>
<li>url 就去取我们的this上的request的url 属性</li>
</ol>
<pre><code class="copyable">const context = &#123;
  get url() &#123;
    return this.request["url"];
  &#125;,
&#125;;
module.exports = context;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>console.log(ctx.url)的打印结果</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1048b6560af04b9a87256a085759fab3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>但是目前context的实现 如果 要实现其他path或者query的获取 就要复制粘帖，这。。不能忍。于是参考了下 koa的源码里 context 获取的实现</p>
</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2bc7cd3fbc14cccb805f7dbf0445f74~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
1.<code>核心</code>：  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FObject%2F__defineGetter__" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/__defineGetter__" ref="nofollow noopener noreferrer"><strong>defineGetter</strong> </a>不过 mdn已经提示被废弃,将来可能停止支持。但 主要 研究 koa 的实现 此处不对该接口深入探讨</p>
<ul>
<li>参考源码后做调整</li>
</ul>
<pre><code class="copyable">const context = &#123;

&#125;
function defienGetter(target,key) &#123;
  context.__defineGetter__(key, function () &#123;
    // tips :这里的function 不能是 箭头函数 ，否则 this 就变成指向 context了,就变成了一个空对象
    // this 应该指向调用它的对象，也就是实例中每次请求方法中自己对应的那个ctx
    return this[target][key];
  &#125;);
&#125;
defienGetter("request", "url");
defienGetter("request", "path");

module.exports = context;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>测试url，path的console结果</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ec1d6987cd14ccb9fe73bd9e53c6942~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            