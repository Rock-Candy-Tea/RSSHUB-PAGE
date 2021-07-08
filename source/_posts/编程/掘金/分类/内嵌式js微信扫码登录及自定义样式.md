
---
title: '内嵌式js微信扫码登录及自定义样式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7b3cf69239742e5aa4b520cb1f913c5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 00:44:15 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7b3cf69239742e5aa4b520cb1f913c5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>关于微信扫码登录网站的功能介绍，请阅读官方文档【<a href="https://link.juejin.cn/?target=https%3A%2F%2Fopen.weixin.qq.com%2Fcgi-bin%2Fshowdocument%3Faction%3Ddir_list%26t%3Dresource%2Fres_list%26verify%3D1%26id%3Dopen1419316505%26token%3D%26lang%3Dzh_CN" target="_blank" rel="nofollow noopener noreferrer" title="https://open.weixin.qq.com/cgi-bin/showdocument?action=dir_list&t=resource/res_list&verify=1&id=open1419316505&token=&lang=zh_CN" ref="nofollow noopener noreferrer">网站应用微信登录开发指南</a>】</p>
<p>根据官方文档我们知道微信扫码登录有两种方式</p>
<p>一种是跳转到一个大黑屏二维码界面进行扫码登录：</p>
<p>（参见博客：<a href="https://juejin.cn/post/6982470602288267295" target="_blank" title="https://juejin.cn/post/6982470602288267295">PHP实现跳转式微信扫码登录网站</a> ）</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7b3cf69239742e5aa4b520cb1f913c5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>另外一种是把二维码内嵌到页面中，这样可以自定义一些样式，例如二维码的大小、是否有标题等，默认效果如下：</p>
<p>（官方文档说的挺好，JS微信登录主要用途：网站希望用户在网站内就能完成登录，无需跳转到微信域下登录后再返回，提升微信登录的流畅性与成功率）</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a471536e4b14fd6acc9d8a07f0f7330~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>实现代码如下：</p>
<pre><code class="copyable"><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>内嵌式 - 微信扫码登录</title>
<!-- 引入微信扫码登录js文件 -->
<script type="text/javascript" src="http://res.wx.qq.com/connect/zh_CN/htmledition/js/wxLogin.js"></script>
</head>
<body>
  <!-- 放置二维码的div -->
  <div id="login_container"></div>
</body>
<script type="text/javascript">
var obj = new WxLogin(&#123;
  self_redirect:true,
  id:"login_container", 
  appid: "wxbdc5610cc59c1631", 
  scope: "snsapi_login", 
  redirect_uri: encodeURIComponent("http://"+window.location.host+"/..."), 
  state: Math.ceil(Math.random()*1000), 
  style: "black",
  href: ""
&#125;);
</script>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数说明（摘自官方文档）：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9dfd9059c3a455aa2134c6280bc0ddc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里的href参数可以自定义扫码样式，一种据说是引入一个https地址的css文件例如：href: "<a href="https://link.juejin.cn/?target=https%3A%2F%2Flws.com%2Ftest.css%2522%25EF%25BC%258C%25E7%2594%25B1%25E4%25BA%258E%25E6%25B2%25A1%25E6%259C%2589%25E9%2585%258D%25E7%25BD%25AEhttps%25E6%2589%2580%25E4%25BB%25A5%25E6%25B2%25A1%25E6%259C%2589%25E5%25AE%259E%25E8%25B7%25B5%25EF%25BC%258C%25E5%258F%25A6%25E4%25B8%2580%25E7%25A7%258D%25E6%2598%25AF%25E6%258A%258A%25E6%25A0%25B7%25E5%25BC%258F%25E4%25BB%25A3%25E7%25A0%2581%25E8%25BF%259B%25E8%25A1%258Cbase64%25E5%258A%25A0%25E5%25AF%2586%25E6%2594%25BE%25E5%2588%25B0href%25E5%258F%2582%25E6%2595%25B0%25E4%25B8%25AD%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://lws.com/test.css%22%EF%BC%8C%E7%94%B1%E4%BA%8E%E6%B2%A1%E6%9C%89%E9%85%8D%E7%BD%AEhttps%E6%89%80%E4%BB%A5%E6%B2%A1%E6%9C%89%E5%AE%9E%E8%B7%B5%EF%BC%8C%E5%8F%A6%E4%B8%80%E7%A7%8D%E6%98%AF%E6%8A%8A%E6%A0%B7%E5%BC%8F%E4%BB%A3%E7%A0%81%E8%BF%9B%E8%A1%8Cbase64%E5%8A%A0%E5%AF%86%E6%94%BE%E5%88%B0href%E5%8F%82%E6%95%B0%E4%B8%AD%E3%80%82" ref="nofollow noopener noreferrer">lws.com/test.css"，由…</a></p>
<p> 官方文档给的样式代码如下：</p>
<pre><code class="copyable">.impowerBox .qrcode &#123;width: 200px;&#125;
.impowerBox .title &#123;display: none;&#125;
.impowerBox .info &#123;width: 200px;&#125;
.status_icon &#123;display: none&#125;
.impowerBox .status &#123;text-align: center;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们用<a href="https://link.juejin.cn/?target=http%3A%2F%2Ftool.chinaz.com%2FTools%2FBase64.aspx" target="_blank" rel="nofollow noopener noreferrer" title="http://tool.chinaz.com/Tools/Base64.aspx" ref="nofollow noopener noreferrer">站长工具</a>对样式代码进行base64加密：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e6f97ccb4f24548a388977ec6ff85ee~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>修改href参数，格式：href: "data:text/css;base64,base64加密后的字符串"</p>
<pre><code class="copyable">href:"data:text/css;base64,LmltcG93ZXJCb3ggLnFyY29kZSB7d2lkdGg6IDIwMHB4O30NCi5pbXBvd2VyQm94IC50aXRsZSB7ZGlzcGxheTogbm9uZTt9DQouaW1wb3dlckJveCAuaW5mbyB7d2lkdGg6IDIwMHB4O30NCi5zdGF0dXNfaWNvbiB7ZGlzcGxheTogbm9uZX0NCi5pbXBvd2VyQm94IC5zdGF0dXMge3RleHQtYWxpZ246IGNlbnRlcjt9"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>样式如下，二维码变小了，默认的标题去掉了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17a5b071c2e34b5483ca5d6df99ce9b3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            