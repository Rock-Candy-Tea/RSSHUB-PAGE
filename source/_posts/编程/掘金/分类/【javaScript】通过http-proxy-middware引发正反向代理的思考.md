
---
title: '【javaScript】通过http-proxy-middware引发正反向代理的思考'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ae95f5838d84b26b04cfc369c5b7d0b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 01:44:57 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ae95f5838d84b26b04cfc369c5b7d0b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">结论</h2>
<p><strong>正向代理隐藏真实客户端，反向代理隐藏真实服务端</strong></p>
<ul>
<li>正向代理</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ae95f5838d84b26b04cfc369c5b7d0b~tplv-k3u1fbpfcp-watermark.image" alt="v2-922c89b735165f9f47db025bd77941c2_720w.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>反向代理</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7eb2a71376b24b729f36365d14442baf~tplv-k3u1fbpfcp-watermark.image" alt="v2-bf5255d84d73d10500cb9c717fac8b02_720w.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>使用<code>http-proxy-middware</code>实现正向代理达到跨域的目的</li>
</ul>
<pre><code class="copyable">const http = require('http')
const proxy = require('http-proxy-middleware')

http.createServer((req, res) => &#123;
  let url = req.url

  res.writeHead(200, &#123;
    'Access-Control-Allow-Origin': '*'
  &#125;)//使用CORS解决前端页面跨域到该8080port

 /*
 1、api:是一个暗号，进行代理
 2、pathRewrite:取消api的路径，实现的功能：
     无pathRewrite：localhost:8080/api/path ==>m.lagou.com/api/path
     有pathRewrite：localhost:8080/api/path ==>m.lagou.com/path
 */
  if (/^/api/.test(url)) &#123; 
    let apiProxy = proxy('/api', &#123; 
      target: 'https://m.lagou.com',
      changeOrigin: true,
      pathRewrite: &#123;
        '^/api': ''
      &#125;
    &#125;)

    // http-proy-middleware 在Node.js中使用的方法
    apiProxy(req, res)
  &#125; else &#123;
    switch (url) &#123;
      case '/index.html':
        res.end('index.html')
        break
      case '/search.html':
        res.end('search.html')
        break
      default:
        res.end('[404]page not found.')
    &#125;
  &#125;
&#125;).listen(8080)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            