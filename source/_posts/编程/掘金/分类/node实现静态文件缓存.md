
---
title: 'node实现静态文件缓存'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50bdd07613a841ceafb109e173fdc618~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 01:55:57 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50bdd07613a841ceafb109e173fdc618~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">缓存</h2>
<p>浏览器缓存(Brower Caching)是浏览器对之前请求过的文件进行缓存，以便下一次访问时重复使用，节省带宽，提高访问速度，降低服务器压力</p>
<h3 data-id="heading-1">缓存位置分类</h3>
<ul>
<li>
<p>memory cache:内存中的缓存,关闭浏览器则清空，</p>
</li>
<li>
<p>disk cache：硬盘中的缓存，关闭浏览器不会马上清空</p>
</li>
<li>
<p>两者的区别：</p>
<pre><code class="copyable">  1. 读取速度 ：memory cache缓存的是当前解析过了的文件在浏览器tab进程里，下次运行使用时的可以快速读取；
              disk cache直接将缓存写入硬盘文件中，读取缓存需要对该缓存存放的硬盘文件进行I/O(读取)操作，然后重新解析缓存内容，速度比内存缓存慢
  2. 时效性：memory cache是存在tab的进程里，tab关闭，则清空；
            disk cache：被清空的时机我还不知道（希望有人可以补充）
  3. 优先级：memory cache大于disk cache
  对于大文件来说，大概率是不存储在memory中的，反之优先，代码角度目前好像也无法控制浏览器缓存位置
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-2">缓存设置header</h3>
<ul>
<li>
<p>cache-control</p>
</li>
</ul>
<pre><code class="copyable"> 1.   cache-control：max-age=10//10秒内重新发的请求都直接命中强缓存，无需向服务器发起请求，读取浏览器缓存即可
 2.   Cache-Control：no-cache //禁止强制缓存，每次都向服务器发起请求，同时也会存在浏览器缓存中 （走协商缓存了基本）
 3.   Cache-Control：no-store //每次都请求服务器，且不缓存在浏览器中，等同于没有缓存  
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Expires：</li>
</ul>
<p>兼容低版本浏览器,这个就是设置绝对时间，获取的是服务器的当前时间和浏览器当前时间做比对（通常存在偏差，是http1.0的产物），和 cache-control同时存在时，cache-control优先级更高</p>
<ul>
<li>last-modified：协商缓存的时候用 和If-Modified-Since，成对出现；If-Modified-Since请求头的值对应上一次服务器的响应头last-modified的值，拥有提供服务器比对请求资源修改时间，相等，则命中协商缓存返回304，浏览器读取缓存即可</li>
<li>Etag：资源标识（也有说时指纹，通常是一个md5值），协商缓存时候用，比较文件是否修改；和If-None-Match 成对出现</li>
</ul>
<pre><code class="copyable">Etag主要为了解决 Last-Modified 无法解决的一些问题。
1. 一些文件也许会周期性的更改，但是他的内容并不改变(仅仅改变的修改时间)，这个时候我们并不希望客户端认为这个文件被修改了，而重新GET;
2. 某些文件修改非常频繁，比如在秒以下的时间内进行修改，(比方说1s内修改了N次)，If-Modified-Since无法检查到如此精细
3. 某些服务器不能精确的得到文件的最后修改时间；
4.Etag与Last-modify同时存在 Etag优先级比较
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际项目：html不允许缓存，html里引用的js有唯一的版本号做依据，再次访问的时候 访问最新的html，引用的js或其他文件版本号未修改则直接用本地缓存</p>
<h2 data-id="heading-3">node实现静态文件缓存</h2>
<p>文件结构</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50bdd07613a841ceafb109e173fdc618~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>public对应我们测试用的静态资源</li>
</ul>
<h3 data-id="heading-4">强缓存</h3>
<h4 data-id="heading-5">思路</h4>
<ul>
<li>创建服务</li>
<li>首次请求 解析请求路径， fs.createReadStream().pipe() 读取文件</li>
<li>设置响应头Cache-Contro：max-age=10 强缓存的相对时间</li>
</ul>
<h4 data-id="heading-6">代码实现</h4>
<pre><code class="copyable">const http = require("http");
const url = require("url");
const fs = require("fs");
const path = require("path");
// 接收文件路径 返回该文件对应的文件类型格式
const mime = require("mime");//npm i mime 

const server = http.createServer((req, res) => &#123;
  let &#123; pathname, query &#125; = url.parse(req.url, true);
  //__dirname 当前文件所在的文件夹所处的绝对路径 和请求路径拼接
  let filePath = path.join(__dirname, "public", pathname);
  console.log(req.url);//10s内反复刷新页面，查看是否持续打印，命中强缓存则10s打印一次
  // 设置头部 缓存信息,规定的缓存时间内，客户端无需再向服务器发起请求
  res.setHeader("Cache-Control", "max-age=10"); // 设置缓存时常；请求的当前时间+max-age 的相对时间内，优先级比Expires高
  res.setHeader("Expires", new Date(Date.now() + 10).toUTCString()); //兼容低版本浏览器,这个就是设置绝对时间，获取的是服务器的当前时间
  // 获取请求路径 判断是文件还是文件目录
  fs.stat(filePath, function (err, statObj) &#123;
    // url解析错误，则请求错误 没有找到对应url资源 返回404
    if (err) &#123;
      res.statusCode = 404;
      res.end("NOT FOUND");
    &#125; else &#123;
      // 如果是文件,用可读流+管道 pipe 进行文件内容读取,利用mime 获取文件内容格式，并设置编码规范为utf-8
      if (statObj.isFile()) &#123;
        fs.createReadStream(filePath).pipe(res);
        res.setHeader(
          "Content-Type",
          mime.getType(filePath) + ";charset=utf-8"
        );
      &#125; else &#123;
        // 如果是文件目录 找到 目录下对应的index.html
        let htmlPath = path.join(filePath, "index.html");
        // fs.access判断拼接的路径是否可访问
        fs.access(htmlPath, function (err) &#123;
          if (err) &#123;
            // 不可访问 设置 状态码404
            res.statusCode = 404;
            res.end("NOT FOUND");
          &#125; else &#123;
            //可访问，用可读流加管道 pipe 进行文件内容读取
            fs.createReadStream(htmlPath).pipe(res);
            res.setHeader("Content-Type", "text/html;charset=utf-8");
          &#125;
        &#125;);
      &#125;
    &#125;
  &#125;);
  // 写到这里 可以 nodemon cache.js  启动服务 查看 http://localhost:3000/ 
&#125;);
server.listen(3000, () => &#123;
  console.log("server start 3000");
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">效果展示</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60b8c4cbed4c4ade96cc9b092b357eb4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">协商缓存</h3>
<p><code>成功</code></p>
<h4 data-id="heading-9">思路</h4>
<ul>
<li>创建服务</li>
<li>首次请求 解析请求路径， fs.createReadStream().pipe() 读取文件</li>
<li>设置响应头Last-modified 返回浏览器</li>
<li>再次请求，比较浏览器if-last-modified 和当前资源修改时间，相等则命中协商缓存，返回响应码304，反之返回路径对应的最新资源，和响应码200</li>
</ul>
<h4 data-id="heading-10">代码实现</h4>
<pre><code class="copyable">const http = require("http");
const url = require("url");
const fs = require("fs");
const path = require("path");
const mime = require("mime");


  let filePath = path.join(__dirname, "public", pathname);
  console.log(req.url);
  fs.stat(filePath, function (err, statObj) &#123;
    if (err) &#123;
      res.statusCode = 404;
      res.end("NOT FOUND");
    &#125; else &#123;
      if (statObj.isFile()) &#123;
        // 判断 浏览器请求的文件路径 的change 时间 通过statObj.ctime
        const ctime = statObj.ctime.toUTCString();
        // 浏览器请求头if-modified-since ===文件上次的修改时间 ，命中协商缓存，则返回 304 浏览器缓存中请求资源
        if (req.headers["if-modified-since"] === ctime) &#123;
          res.statusCode = 304; //去浏览器缓存中找
          res.end(); //
        &#125; else &#123;
          //  if-modified-since !==文件上次的修改时间,响应头Last-modified 设置 当前请求文件的 修改时间 做下次 浏览器请求的last-modify-since的对应值
          res.setHeader("Last-modified", ctime);
          fs.createReadStream(filePath).pipe(res);
          res.setHeader(
            "Content-Type",
            mime.getType(filePath) + ";charset=utf-8"
          );
        &#125;
      &#125; else &#123;
        fs.access(htmlPath, function (err) &#123;
          if (err) &#123;
            // 不可访问 设置 状态码404
            res.statusCode = 404;
            res.end("NOT FOUND");
          &#125; else &#123;
            fs.createReadStream(htmlPath).pipe(res);
            res.setHeader("Content-Type", "text/html;charset=utf-8");
          &#125;
        &#125;);
      &#125;
    &#125;
  &#125;);
  // 写到这里 可以 nodemon cache2.js       启动服务 查看 http://localhost:3000/ 
&#125;);
server.listen(3000, () => &#123;
  console.log("server start 3000");
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">效果展示</h4>
<p>每次刷新页面都会执行  console.log(req.url); 请求了服务器但服务器返回304 命中协商缓存 浏览器直接读取缓存资源即可</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61d5f96011fe44d0b1debc8f78936416~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>成功</code></p>
<h2 data-id="heading-12">小结：</h2>
<p><a href="https://juejin.cn/post/url">留给坑补Etag做协商缓存的实现</a></p>
<p><code>初学node 相互学习，最后如果觉得本文有帮助 记得点赞三连哦 十分感谢</code></p></div>  
</div>
            