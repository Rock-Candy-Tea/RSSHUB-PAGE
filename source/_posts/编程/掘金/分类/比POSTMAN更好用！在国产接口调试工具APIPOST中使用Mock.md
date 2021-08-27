
---
title: '比POSTMAN更好用！在国产接口调试工具APIPOST中使用Mock'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acb2776f237d4e44965f01887767a93e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 22:40:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acb2776f237d4e44965f01887767a93e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">在APIPOST中使用Mock</h1>
<p>APIPOST可以让你在没有后端程序的情况下能真实地返回接口数据，你可以用APIPOST实现项目初期纯前端的效果演示，也可以用APIPOST实现开发中的数据模拟从而实现前后端分离。在使用APIPOST之前，你的团队实现数据模拟可能是下面的方案中的一种或者多种：</p>
<ul>
<li>本地手写数据模拟，在前端代码中产生一大堆的mock代码。</li>
<li>利用mockjs或者canjs的can-fixture实现ajax拦截，本地配置必要的json规则。</li>
<li>后端在Controller层造假数据返回给前端。</li>
</ul>
<p>上面的方式中，不管哪一种方式，都会要求开发人员写一些跟项目本无任何关联的代码，第一个和第二个方式还会需要前端项目在本地引入不必要的js文件。</p>
<h2 data-id="heading-1">使用APIPOST 的Mock 服务</h2>
<p>您可以通过APIPOST 提供的Mock 服务实现上述功能。</p>
<h2 data-id="heading-2">编写Mock 规则</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acb2776f237d4e44965f01887767a93e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在APIPOST中，Mock 规则模板支持类型丰富（5.4版本起）。</p>
<h3 data-id="heading-3">基本数据(固定json结构)</h3>
<pre><code class="copyable">&#123;
  "code": "0",
  "data": &#123;
    "name": "张三丰",
    "age": 100
  &#125;,
  "desc": "成功"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">基本数据(Mock随机json结构)</h3>
<pre><code class="copyable">&#123;
  "code": "0",
  "data": &#123;
    "list|20": [&#123;
      "name": "@name",
      "age": "@integer(2)"
    &#125;],
    "url": "https://echo.apipost.cn"
  &#125;,
  "desc": "成功"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">RESTFUL逻辑数据</h3>
<p>某些场景中，我们可能需要根据接口的入参规则，加入适当的逻辑处理后再返回数据。一个简单的场景就是登录场景，需要根据用户名密码，判断是否登录成功。再或者，我们需要根据产品ID动态返回产品信息，等等。</p>
<p>现在，ApiPost 的Mock 服务提供了这种场景的解决方案。<br>
以下示例中，我们用到了 _req.body对象，其含义是：</p>
<blockquote>
<p>当 post 请求以 x-www-form-urlencoded 或者application/json 方式提交时，我们可以拿到请求的参数对象。</p>
</blockquote>
<pre><code class="copyable">&#123;
  "code": "0000",
  "data": &#123;
    "verifySuccess": function() &#123;
      let body = _req.body;
      return body.username === 'admin' && body.password === '123456';
    &#125;,
    "userInfo": function() &#123;
      let body = _req.body;
      if (body.username === 'admin' && body.password === '123456') &#123;
        return Mock.mock(&#123;
          username: "admin",
          email: "@email",
          address: "@address"
        &#125;);
      &#125; else &#123;
        return null;
      &#125;
    &#125;,
  &#125;,
  "desc": "成功"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">填写Mock URL 相对地址</h2>
<p>Mock URL相对地址是必填项（如果不填写的话，无法正常得到响应结果）。您可以通过在设置里开启“自动获取Mock URL地址”来自动获取Mock URL。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afec946f01024bbd999f634276c24b80~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此项开启后，APIPOST将根据您输入的接口URL自动截取PATH部分作为Mock URL的相对路径。</p>
<h2 data-id="heading-7">利用APIPOST发送Mock URL</h2>
<p>完成以上2步后，您可以通过在APIPOST中切换到“Mock 环境”来发送查看mock返回的详细数据。<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8431e6e56c6c4e978d8f6f3abcc3b1bb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">将生成的mock URL地址发给前端</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96a3f0de7d9148409a88d98cd1f39764~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>您可以将APIPOST生成的mock URL地址发给前端来代替您的接口地址，这样前端就可以使用您模拟的数据进行先一步的调试开发了。当您的接口完成后，再替换回来即可。</p>
<p>APIPOST的 mock 是基于mock.js 开发的。具体文档可以 参见 mock.js 详细文档。</p></div>  
</div>
            