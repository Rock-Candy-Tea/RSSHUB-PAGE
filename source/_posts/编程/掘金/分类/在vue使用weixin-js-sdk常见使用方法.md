
---
title: '在vue使用weixin-js-sdk常见使用方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1667'
author: 掘金
comments: false
date: Fri, 30 Apr 2021 07:27:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=1667'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>链接：<a href="https://qydev.weixin.qq.com/wiki/index.php?title=%E5%BE%AE%E4%BF%A1JS-SDK%E6%8E%A5%E5%8F%A3#.E6.AD.A5.E9.AA.A4.E4.B8.80.EF.BC.9A.E5.BC.95.E5.85.A5JS.E6.96.87.E4.BB.B6" target="_blank" rel="nofollow noopener noreferrer">qydev.weixin.qq.com/wiki/index.…</a></p>
<p><strong>1.导入依赖包</strong></p>
<pre><code class="copyable">npm install weixin-js-sdk
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2.判断是否是在微信浏览器中</strong></p>
<pre><code class="copyable">
env.js
 
<script>
var ua = navigator.userAgent.toLowerCase();
var isWeixin = ua.indexOf('micromessenger') != -1;
var isAndroid = ua.indexOf('android') != -1;
var isIos = (ua.indexOf('iphone') != -1) || (ua.indexOf('ipad') != -1);
if(!isWeixin) &#123;
document.head.innerHTML = '<title>抱歉，出错了</title><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=0"><link rel="stylesheet" type="text/css" href="https://res.wx.qq.com/open/libs/weui/0.4.1/weui.css">';
document.body.innerHTML = '<div class="weui_msg"><div class="weui_icon_area"><i class="weui_icon_info weui_icon_msg"></i></div><div class="weui_text_area"><h4 class="weui_msg_title">请在微信客户端打开链接</h4></div></div>';
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在main.js中引用:</p>
<pre><code class="copyable">import env from "./env";//运行环境
<span class="copy-code-btn">复制代码</span></code></pre>
<p>微信登录，通过code换取openid，在起始页使用该方法:</p>
<pre><code class="copyable"><script>
methods:&#123;
 // 微信登陆
    wxLogin() &#123;
      var that = this;
      axios
        .get("/common/loginAuth")
        .then(function(res) &#123;
          console.log("后台返回的链接地址", res.data);
          window.location.href = res.data;//跳转后台返回的链接地址
        &#125;)
        .catch(function(error) &#123;&#125;);
    &#125;,
//换取用户信息
    postCode(res) &#123;
      var that = this;
      axios
        .post("/common/getUserInfo", &#123;
          code: res
        &#125;)
        .then(function(res) &#123;
          cookie.set("openid", res.data.openid);//code像后台换取openid并存入
        &#125;)
        .catch(function(error) &#123;
          console.log(error);
        &#125;);
    &#125;&#125;,
created() &#123;
    var r = window.location.href;//获取当前链接，拆分当前链接
    //当前链接地址为后台返回的参数，有拆分得到链接中的code,通过postCode()方法获取openid，没有则通过wxLogin()方法开始微信登录
    if (r.indexOf("?") != -1) &#123;
      r = r.split("?");
      r = r[1].split("&");
      r = r[0].split("=");
      r = r[1];
    &#125; else &#123;
      this.wxLogin();
    &#125;
    if (r) &#123;
      this.postCode(r);
    &#125; else &#123;
      this.wxLogin();
    &#125;
  &#125;,
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3.前端页面使用</strong></p>
<pre><code class="copyable">import wx from 'weixin-js-sdk'
this.axios(&#123;
　　method: 'post',
　　url: 'url',
　　data:&#123; url:location.href.split('#')[0] &#125; //向服务端提供授权url参数，并且不需要#后面的部分
&#125;).then((res)=>&#123;
　　wx.config(&#123;
　　　　debug: true, // 开启调试模式,
　　　　appId: res.appId, // 必填，企业号的唯一标识，此处填写企业号corpid
　　　　timestamp: res.timestamp, // 必填，生成签名的时间戳
　　　　nonceStr: res.nonceStr, // 必填，生成签名的随机串
　　　　signature: res.signature,// 必填，签名，见附录1
　　　　jsApiList: ['scanQRCode'] // 必填，需要使用的JS接口列表，所有JS接口列
　　&#125;);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            