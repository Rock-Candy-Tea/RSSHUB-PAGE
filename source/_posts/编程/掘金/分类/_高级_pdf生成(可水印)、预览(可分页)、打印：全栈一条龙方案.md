
---
title: '_高级_pdf生成(可水印)、预览(可分页)、打印：全栈一条龙方案'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45b05c372a384d7793e8690c0feed55f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 01:09:41 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45b05c372a384d7793e8690c0feed55f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<h1 data-id="heading-0">前言</h1>
<p>每个前端开发者的一生中总会遇到一些与pdf有关的需求，但是搜寻网上的文章，大多都是部分功能的实现，想要获得与自身需求相契合的完整方案并不是一件容易的事情，基于此，我结合自身的相关工作经验，梳理出了一套包含pdf生成、预览、打印的完整技术方案，大家觉得有用的话可以收藏此文以便日后工作中借鉴。</p>
<p>本文demo示例代码地址：<a href="https://github.com/Alansad/pdfArticle" target="_blank" rel="nofollow noopener noreferrer">github.com/Alansad/pdf…</a></p>
<h1 data-id="heading-1">pdf生成</h1>
<h2 data-id="heading-2">方案比较</h2>
<p>生成pdf一般来说有两种方案，第一种在客户端生成，第二种是在服务端生成，<strong>我推荐在服务端生成pdf</strong>。</p>
<p>在客户端一般是基于canvas来生成：</p>
<ul>
<li>1.使用html2canvas这个库将html转为canvas对象</li>
<li>2.使用canvas.toDataURL方法将canvas转为图片</li>
<li>3.使用jsPDF这个库将图片转为pdf</li>
</ul>
<p>虽然方案看起来比较简单，但是它有两个致命缺点：</p>
<ul>
<li>1.生成的pdf模糊</li>
<li>2.客户端无法长期存储该pdf</li>
</ul>
<p>所以我推荐使用第二种方案，在服务端生成pdf：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45b05c372a384d7793e8690c0feed55f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>1.生成html字符串</li>
<li>2.无头浏览器将html打开</li>
<li>3.通过对页面的截图生成pdf</li>
</ul>
<p>有部分服务端的插件将无头浏览器打开/截图的过程做成了黑盒，开发者感受不到这个过程。
但是无论是使用java还是nodejs、python等语言，一般都是采用以上方案，<strong>该方案生成的pdf清晰度高、还原度强</strong>。</p>
<h2 data-id="heading-3">具体实现</h2>
<p>下面我介绍一个具体的案例，来详细介绍该方案的技术细节。</p>
<p><strong>需求描述：</strong> 提供一个生成pdf的接口，根据不同的请求参数来渲染出不同的pdf，并将pdf文件以url链接的形式返回。</p>
<p><strong>分析：</strong> 根据以上需求，我们首先需要制作一个html模版，然后根据请求中的参数来填充html，用无头浏览器将html转为pdf之后存储到文件服务上，最后将url返回给前端。</p>
<p><strong>具体实现：</strong>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd23329f0ca74db3b5de8540ae73f600~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
以下示例代码采用原生node语言，方便大家理解：</p>
<p>1、首先我们准备好html字符串模版:</p>
<pre><code class="copyable">// html模版，根据title变化标题
const getHtml = (params) => &#123;
  const &#123;
    title = ' ',
  &#125; = params
  return (`
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta http-equiv="content-type" content="text/html;charset=utf-8">
  <title>demo</title>
</head>
<body>
<div class="wrapper">
  <h style="color:red">$&#123;title&#125;</h>
  <div>
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn1-q.mafengwo.net%2Fs6%2FM00%2FFC%2FCC%2FwKgB4lNzI2yAK4tdAAELj6RBVtE37.jpeg%3FimageMogr2%252Fthumbnail%252F%21310x207r%252Fgravity%252FCenter%252Fcrop%252F%21310x207%252Fquality%252F90&refer=http%3A%2F%2Fn1-q.mafengwo.net&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1627634331&t=0efacd9a64806ffc74c5cdfa8f7f261f" alt="">
    <img src="https://img1.baidu.com/it/u=1361135963,570304265&fm=26&fmt=auto&gp=0.jpg" alt="">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn1-q.mafengwo.net%2Fs6%2FM00%2FFC%2FCC%2FwKgB4lNzI2yAK4tdAAELj6RBVtE37.jpeg%3FimageMogr2%252Fthumbnail%252F%21310x207r%252Fgravity%252FCenter%252Fcrop%252F%21310x207%252Fquality%252F90&refer=http%3A%2F%2Fn1-q.mafengwo.net&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1627634331&t=0efacd9a64806ffc74c5cdfa8f7f261f" alt="">
    <img src="https://img1.baidu.com/it/u=1361135963,570304265&fm=26&fmt=auto&gp=0.jpg" alt="">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn1-q.mafengwo.net%2Fs6%2FM00%2FFC%2FCC%2FwKgB4lNzI2yAK4tdAAELj6RBVtE37.jpeg%3FimageMogr2%252Fthumbnail%252F%21310x207r%252Fgravity%252FCenter%252Fcrop%252F%21310x207%252Fquality%252F90&refer=http%3A%2F%2Fn1-q.mafengwo.net&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1627634331&t=0efacd9a64806ffc74c5cdfa8f7f261f" alt="">
    <img src="https://img1.baidu.com/it/u=1361135963,570304265&fm=26&fmt=auto&gp=0.jpg" alt="">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn1-q.mafengwo.net%2Fs6%2FM00%2FFC%2FCC%2FwKgB4lNzI2yAK4tdAAELj6RBVtE37.jpeg%3FimageMogr2%252Fthumbnail%252F%21310x207r%252Fgravity%252FCenter%252Fcrop%252F%21310x207%252Fquality%252F90&refer=http%3A%2F%2Fn1-q.mafengwo.net&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1627634331&t=0efacd9a64806ffc74c5cdfa8f7f261f" alt="">
    <img src="https://img1.baidu.com/it/u=1361135963,570304265&fm=26&fmt=auto&gp=0.jpg" alt="">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn1-q.mafengwo.net%2Fs6%2FM00%2FFC%2FCC%2FwKgB4lNzI2yAK4tdAAELj6RBVtE37.jpeg%3FimageMogr2%252Fthumbnail%252F%21310x207r%252Fgravity%252FCenter%252Fcrop%252F%21310x207%252Fquality%252F90&refer=http%3A%2F%2Fn1-q.mafengwo.net&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1627634331&t=0efacd9a64806ffc74c5cdfa8f7f261f" alt="">
    <img src="https://img1.baidu.com/it/u=1361135963,570304265&fm=26&fmt=auto&gp=0.jpg" alt="">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn1-q.mafengwo.net%2Fs6%2FM00%2FFC%2FCC%2FwKgB4lNzI2yAK4tdAAELj6RBVtE37.jpeg%3FimageMogr2%252Fthumbnail%252F%21310x207r%252Fgravity%252FCenter%252Fcrop%252F%21310x207%252Fquality%252F90&refer=http%3A%2F%2Fn1-q.mafengwo.net&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1627634331&t=0efacd9a64806ffc74c5cdfa8f7f261f" alt="">
    <img src="https://img1.baidu.com/it/u=1361135963,570304265&fm=26&fmt=auto&gp=0.jpg" alt="">
    <img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn1-q.mafengwo.net%2Fs6%2FM00%2FFC%2FCC%2FwKgB4lNzI2yAK4tdAAELj6RBVtE37.jpeg%3FimageMogr2%252Fthumbnail%252F%21310x207r%252Fgravity%252FCenter%252Fcrop%252F%21310x207%252Fquality%252F90&refer=http%3A%2F%2Fn1-q.mafengwo.net&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1627634331&t=0efacd9a64806ffc74c5cdfa8f7f261f" alt="">
    <img src="https://img1.baidu.com/it/u=1361135963,570304265&fm=26&fmt=auto&gp=0.jpg" alt="">
  </div>
</div>
</html>
  `)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、然后我们使用html-pdf这个npm包来将html转换为pdf（<a href="https://www.npmjs.com/package/html-pdf" target="_blank" rel="nofollow noopener noreferrer">html-pdf文档</a>）</p>
<pre><code class="copyable">const pdf = require('html-pdf')

// 生成pdf的参数
const optionDefault = &#123;
  'format': 'A4',
  'header': &#123;
    'height': '10mm',
    'contents': '',
  &#125;
&#125;

// 将html转为pdf
const exportPdf = (html, options = optionDefault) => &#123;
  return new Promise((resolve, reject) => &#123;
    pdf.create(html, options).toBuffer((err, res) => &#123;
      if (err) &#123;
        reject(err)
      &#125; else &#123;
        resolve(res)
      &#125;
    &#125;)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、最后我们启动一个http服务，写一个接口来返回pdf：</p>
<pre><code class="copyable">const http = require('http')
const url = require('url')
const querystring = require("querystring")

const &#123;getHtml, exportPdf&#125; = require('./utils/htmlToPdf')

http.createServer(async (request, response) => &#123;
  const &#123;query, pathname&#125; = url.parse(request.url)
  const &#123;title&#125; = querystring.parse(query)
  if (pathname === '/') &#123;
    response.writeHead(200, &#123;
      'Content-Type': 'application/pdf',
      'Access-Control-Allow-Origin': '*'
    &#125;)
    const html = getHtml(&#123;title&#125;)
    const pdf = await exportPdf(html)
    response.end(pdf)
  &#125;
&#125;).listen(8888)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、此处我们的示例为直接返回buffer格式的pdf，如果需要上传到存储服务（以阿里云存储服务为例），我们可以使用<code>pdf.create(html, options).toStream</code>获取Stream格式的pdf文件，然后用post请求上传。</p>
<pre><code class="copyable">pdf.create(html, options).toStream((err, res) => &#123;
      if (err) &#123;
        reject(err)
      &#125; else &#123;
        resolve(res)
      &#125;
    &#125;)
    
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>理解了方案原理后，给pdf添加水印也变得很简单了：</strong></p>
<p>因为该方案的原理是对html页面进行截屏，那么我们只需要给html页面添加水印就可以了，网上的水印库很多，在html中添加一段script来加入水印就可以啦。</p>
<p><strong>除了以上功能实现，还有两个注意事项：</strong></p>
<ul>
<li>因为该方案基于无头浏览器实现，所以生成pdf的速度直接取决于浏览器加载html的速度，如果时间过长建议做成异步获取pdf。另外如果存在高并发的情况，加载html的数量过多，还需要注意服务的内存问题，最好与业务代码区分开部署到不同的服务器。</li>
<li>浏览器加载html的中文时依赖中文字体库，如果存在pdf中不显示中文的情况，需要在系统中安装中文字体；如果不想给系统安装中文字体，也可以自己指定中文字体：</li>
</ul>
<pre><code class="copyable">@font-face &#123;
          font-family: pdfZh;
          src: url("http://localhost:3000/pdf_zh.ttf");
        &#125;
        body&#123;
           font-family: pdfZh;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">pdf预览</h1>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79bde42aa08a4cc5abb723a65f1c5def~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
pdf预览的原理一般是将<strong>pdf转为canvas</strong>，而目前最流行的库为<strong>pdf.js</strong>，我以官方的一个例子介绍下该库，最终效果如下，可以分页对pdf进行预览。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1259d5252c94537890b11829139a4f6~tplv-k3u1fbpfcp-watermark.image" alt="预览pdf.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>完整代码如下：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Title</title>
  <!--<script src="./pdf.js"></script>-->
  <script src="//mozilla.github.io/pdf.js/build/pdf.js"></script>
  <style>
    #the-canvas &#123;
      border: 1px solid black;
      direction: ltr;
    &#125;
  </style>
</head>
<body>
<div>
  <button id="prev">上一页</button>
  <button id="next">下一页</button>
  &nbsp; &nbsp;
  <span>Page: <span id="page_num"></span> / <span id="page_count"></span></span>
</div>
<canvas id="the-canvas" style="width: 100%; height: auto"></canvas>
</body>
<script>
  // If absolute URL from the remote server is provided, configure the CORS
  // header on that server.
  // const url = 'http://localhost:8888/?title=123'
  var url = 'https://raw.githubusercontent.com/mozilla/pdf.js/ba2edeae/web/compressed.tracemonkey-pldi-09.pdf';

  // Loaded via <script> tag, create shortcut to access PDF.js exports.
  const pdfjsLib = window['pdfjs-dist/build/pdf'];

  // The workerSrc property shall be specified.
  pdfjsLib.GlobalWorkerOptions.workerSrc = '//mozilla.github.io/pdf.js/build/pdf.worker.js';

  var pdfDoc = null,
    pageNum = 1,
    pageRendering = false,
    pageNumPending = null,
    scale = 3,
    canvas = document.getElementById('the-canvas'),
    ctx = canvas.getContext('2d');
  /**
   * Get page info from document, resize canvas accordingly, and render page.
   * @param num Page number.
   */
  function renderPage(num) &#123;
    pageRendering = true;
    // Using promise to fetch the page
    pdfDoc.getPage(num).then(function(page) &#123;
      var viewport = page.getViewport(&#123;scale: scale&#125;);
      canvas.height = viewport.height;
      canvas.width = viewport.width;

      // Render PDF page into canvas context
      var renderContext = &#123;
        canvasContext: ctx,
        viewport: viewport
      &#125;;
      var renderTask = page.render(renderContext);

      // Wait for rendering to finish
      renderTask.promise.then(function() &#123;
        pageRendering = false;
        if (pageNumPending !== null) &#123;
          // New page rendering is pending
          renderPage(pageNumPending);
          pageNumPending = null;
        &#125;
      &#125;);
    &#125;);

    // Update page counters
    document.getElementById('page_num').textContent = num;
  &#125;
  /**
   * If another page rendering in progress, waits until the rendering is
   * finised. Otherwise, executes rendering immediately.
   */
  function queueRenderPage(num) &#123;
    if (pageRendering) &#123;
      pageNumPending = num;
    &#125; else &#123;
      renderPage(num);
    &#125;
  &#125;

  /**
   * Displays previous page.
   */
  function onPrevPage() &#123;
    if (pageNum <= 1) &#123;
      return;
    &#125;
    pageNum--;
    queueRenderPage(pageNum);
  &#125;
  document.getElementById('prev').addEventListener('click', onPrevPage);

  /**
   * Displays next page.
   */
  function onNextPage() &#123;
    if (pageNum >= pdfDoc.numPages) &#123;
      return;
    &#125;
    pageNum++;
    queueRenderPage(pageNum);
  &#125;
  document.getElementById('next').addEventListener('click', onNextPage);

  /**
   * Asynchronously downloads PDF.
   */
  pdfjsLib.getDocument(url).promise.then(function(pdfDoc_) &#123;
    pdfDoc = pdfDoc_;
    document.getElementById('page_count').textContent = pdfDoc.numPages;

    // Initial/first page rendering
    renderPage(pageNum);
  &#125;);
</script>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>pdf.js文档为：<a href="https://github.com/mozilla/pdf.js" target="_blank" rel="nofollow noopener noreferrer">github.com/mozilla/pdf…</a> ，需要注意的是这个scale数值，理论上设置的越大展示的越清晰，但是设置的过大有可能会导致解析的过程卡死。</p>
<h1 data-id="heading-5">打印</h1>
<p>在浏览器端，我们是没有权限直接连上打印机来打印文件的，因为这样存在很大的安全隐患。比较常见的需求是唤起浏览器的打印界面，让用户自行调整和操作打印。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a07b3d869c64fbcac75b5cb25a2575a~tplv-k3u1fbpfcp-watermark.image" alt="打印pdf.gif" loading="lazy" referrerpolicy="no-referrer">
以上动图所示的效果为：自动唤起打印pdf功能。</p>
<p><strong>实现步骤如下：</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8b2ab9f71c4411298350e7e01620ff7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
此处将pdf变为objectURL的目的是统一解决跨域问题。</p>
<p><strong>具体代码为：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Title</title>
</head>
<body>
<iframe id="frame-result" style="height: 100vh;width: 100vw;"></iframe>
</body>
<script>
  downloadRes = async () => &#123;
    let response = await fetch('http://localhost:8888/?title=123')
    // 内容转变成blob地址
    let blob = await response.blob()
    const iframeEle =  document.querySelector('#frame-result')
    iframeEle.src = URL.createObjectURL(new Blob([blob], &#123;type: 'application/pdf'&#125;))
    if (iframeEle) &#123;
      iframeEle.onload = () => &#123;
        iframeEle.contentWindow.print();
      &#125;
    &#125;
  &#125;
  downloadRes()
</script>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果需要在不展示pdf的情况下唤起打印窗口，将iframe隐藏即可</p>
<pre><code class="copyable"><iframe id="frame-result" style="display: none"></iframe>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bfb13aa4a3c4f50973f3ffd869133b0~tplv-k3u1fbpfcp-watermark.image" alt="隐藏iframe.gif" loading="lazy" referrerpolicy="no-referrer">
如果需要新增打开一个窗口来打印，则可以使用以下代码：</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Title</title>
</head>
<body>
</body>
<script>
  downloadRes = async () => &#123;
    let response = await fetch('http://localhost:8888/?title=123')
    // 内容转变成blob地址
    let blob = await response.blob()
    const newWindow = window.open(URL.createObjectURL(new Blob([blob], &#123;type: 'application/pdf'&#125;)))
    if (newWindow) &#123;
      newWindow.onload = () => &#123;
        newWindow.print();
      &#125;
    &#125;
  &#125;
  downloadRes()
</script>
</html>

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">总结</h1>
<p>本文介绍了包含pdf生成、pdf预览、pdf打印的完整方案，欢迎各位小伙伴交流和指正。另外对于<strong>文件流以及无头浏览器</strong>相关知识感兴趣的同学也可以关注我，后面我会详细介绍其在工作中相关的实际应用。</p></div>  
</div>
            