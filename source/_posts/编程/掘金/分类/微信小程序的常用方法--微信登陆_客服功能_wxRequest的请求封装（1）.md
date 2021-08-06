
---
title: '微信小程序的常用方法--微信登陆_客服功能_wxRequest的请求封装（1）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5051'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 08:09:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=5051'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">微信登录</h2>
<p>在开发微信小程序的时候，我们经常需要用到微信登录，通过<code>wx</code>的接口来获取微信用户的信息，然后存储到我们数据库来创建属于我们系统的用户信息。</p>
<p>所以我们就要使用到<code>wx.login()，wx.getUserProfile()</code>，这两个方法。</p>
<p><code>wx.login()</code></p>
<p><code>wx.login()</code>，是调用接口获取登录凭证（code）。通过凭证进而换取用户登录态信息，包括用户在当前小程序的唯一标识（<code>openid</code>）、微信开放平台帐号下的唯一标识（<code>unionid</code>，若当前小程序已绑定到微信开放平台帐号）及本次登录的会话密钥（session_key）等。用户数据的加解密通讯需要依赖会话密钥完成。</p>
<p>我们通过获取到的code，传给后端，由后端通过调用 auth.code2Session 接口，来获取用户唯一标识 <code>OpenID</code>、 用户在微信开放平台帐号下的唯一标识<code>UnionID</code>（若当前小程序已绑定到微信开放平台帐号） 和 会话密钥 session_key。</p>
<pre><code class="copyable">wx.login(&#123;
      success (res) &#123;
        console.log(res);
        if (res.code) &#123;  //获取到code之后，传给后端，接口
          wx.request(&#123;
            url: url,
            data: &#123;
              code: res.code,
              user_name:e.nickName
            &#125;,
            success: (res) => &#123;
              console.log(res.data);
              if(res.data.ret)&#123;
                let userInfo = Object.assign(e,res.data)
                console.log(userInfo);
                wx.setStorage(&#123;
                  key:"userInfo",
                  data:JSON.stringify(userInfo) 
                &#125;)
              &#125;else&#123;
                wx.showToast(&#123;title: '登录失败',icon:'error',duration:2000&#125;)
              &#125;
            &#125;
          &#125;)
          
        &#125; else &#123;
          console.log('登录失败！' + res.errMsg)
        &#125;
      &#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>wx.getUserProfile()</strong></p>
<p><code>wx.getUserProfile()</code>，获取用户信息。页面产生点击事件（例如 <code>button</code> 上 <code>bindtap</code> 的回调中）后才可调用，每次请求都会弹出授权窗口，用户同意后返回 <code>userInfo</code>。该接口用于替换 <code>wx.getUserInfo</code></p>
<p>这个是新的微信获取用户的方法了，之前的<code>wx.getUserInfo()</code>，已经不能弹窗了。</p>
<pre><code class="copyable">getUserProfile(e)&#123;
      let that = this
      wx.getUserProfile(&#123;
        desc: '展示用户信息', // 声明获取用户个人信息后的用途，后续会展示在弹窗中，请谨慎填写
        success: (res) => &#123;
          console.log(res);
        &#125;,
        fail:(res)=>&#123;
          console.log(res);
        &#125;
      &#125;)
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>两者合一</strong></p>
<p>但是在实际的使用的时候，我们之后点击一次来获取这些信息，所以就会出现一个问题，<code>wx.getUserProfile()</code>，是不能通过API调用，所以只能先调用<code>wx.getUserProfile()</code>，然后再去调用<code>wx.login()</code>。</p>
<p>这样就可以完美获取用户的信息了，并且转化为系统需要的用户和信息</p>
<h2 data-id="heading-1">客服</h2>
<p>微信小程序有个自带的客服功能，在小程序的后台管理，添加</p>
<p>因为客服功能是必须要用户自己触发的，不能使用<code>api</code>触发的，但是有时候我们使用，单元格来做点击联系客服的时候就有点麻烦了，因为不能使用<code>openType: 'contact'</code></p>
<p>所以使用了，点击之后，出现一个弹窗，再由用户去触发</p>
<pre><code class="copyable"><van-cell title="联系客服" is-link bind:click='getContact'>
            <view slot='icon' class="center">
               <van-icon name="service-o" color="#1c91e0" class="center" style="margin-right:5px;font-size:16px;" />
            </view>
        </van-cell>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">getContact()&#123;
      Dialog.alert(&#123;
        message: '是否联系在线客服？',
        theme: 'round-button',
        confirmButtonOpenType:'contact',//这个是弹框的自带的属性，可以触发客服的会话弹框
        showCancelButton:'false'
      &#125;)
      .then(() => &#123;
        // on confirm
      &#125;)
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是我发现一个问题，这个Dialog的功能，必须还要再额外的引入一次，才可以使用</p>
<p>import Dialog from '@vant/weapp/dist/dialog/dialog';</p>
<p>具体的客服功能可以去参考文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fdoc%2Foffiaccount%2FMessage_Management%2FService_Center_messages.html%237" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Service_Center_messages.html#7" ref="nofollow noopener noreferrer">developers.weixin.qq.com/doc/offiacc…</a></p>
<h2 data-id="heading-2">wxRequest的请求</h2>
<p>设置全局请求URL</p>
<pre><code class="copyable">   urlData:&#123;
     URL: 'http://182.61.13.123:8080'
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>封装wx.request请求；
method： 请求方式；
url: 请求地址；
data： 要传递的参数；
callback： 请求成功回调函数；
errFun： 请求失败回调函数；</p>
<pre><code class="copyable">wxRequest(method, url, data, callback, errFun) &#123;
     wx.request(&#123;
      url: url,
      method: method,
      data: data,
      header: &#123;
       'content-type': method == 'GET'?'application/json':'application/x-www-form-urlencoded',
       'Accept': 'application/json'
      &#125;,
      dataType: 'json',
      success: function (res) &#123;
       callback(res.data);
      &#125;,
      fail: function (err) &#123;
       errFun(res);
      &#125;
     &#125;)
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            