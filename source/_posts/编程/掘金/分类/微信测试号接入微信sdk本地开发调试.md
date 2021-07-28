
---
title: '微信测试号接入微信sdk本地开发调试'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3274'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 23:55:46 GMT
thumbnail: 'https://picsum.photos/400/300?random=3274'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>H5开发的网页在微信端需要调用微信sdk的录音功能,自己摸索下来总结的一些经验。</p>
<blockquote>
<p>由于用户体验和安全性方面的考虑，微信公众号的注册有一定门槛，某些高级接口的权限需要微信认证后才可以获取。所以，为了帮助开发者快速了解和上手微信公众号开发，熟悉各个接口的调用，我们推出了微信公众帐号测试号，通过手机微信扫描二维码即可获得测试号。</p>
</blockquote>
<h2 data-id="heading-0">申请测试号</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fdebug%2Fcgi-bin%2Fsandbox%3Ft%3Dsandbox%2Flogin" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login" ref="nofollow noopener noreferrer">点此去申请微信测试号</a></p>
<h2 data-id="heading-1">获取jssdk签名配置</h2>
<ol>
<li>在测试号管理界面绑定<code>JS接口安全域名</code><strong>(可以用本地的ip，方便在真机预览调试)</strong></li>
<li>扫码关注自己的测试号</li>
<li>要引入微信<code>jssdk</code>需要<strong>通过config接口注入权限验证配置</strong>
<pre><code class="hljs language-js copyable" lang="js">wx.config(&#123;
  <span class="hljs-attr">debug</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。</span>
  <span class="hljs-attr">appId</span>: <span class="hljs-string">''</span>, <span class="hljs-comment">// 必填，公众号的唯一标识</span>
  <span class="hljs-attr">timestamp</span>: , <span class="hljs-comment">// 必填，生成签名的时间戳</span>
  nonceStr: <span class="hljs-string">''</span>, <span class="hljs-comment">// 必填，生成签名的随机串</span>
  <span class="hljs-attr">signature</span>: <span class="hljs-string">''</span>,<span class="hljs-comment">// 必填，签名</span>
  <span class="hljs-attr">jsApiList</span>: [] <span class="hljs-comment">// 必填，需要使用的JS接口列表</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p><strong>获取signature</strong></p>
<ol>
<li>
<p>访问<a href="https://link.juejin.cn/?target=https%3A%2F%2Fapi.weixin.qq.com%2Fcgi-bin%2Ftoken%3Fgrant_type%3Dclient_credential%26appid%3D%24%257Bappid%257D%26secret%3D%24%257Bsecret%257D" target="_blank" rel="nofollow noopener noreferrer" title="https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=$%7Bappid%7D&secret=$%7Bsecret%7D" ref="nofollow noopener noreferrer">此链接</a>获取<code>access_token</code>,参数就是测试号的<code>appid</code>和<code>appsecret</code></p>
</li>
<li>
<p>通过获取到的<code>access_token</code>采用http GET方式请求获得jsapi_ticket（有效期7200秒，开发者必须在自己的服务全局缓存jsapi_ticket）：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fapi.weixin.qq.com%2Fcgi-bin%2Fticket%2Fgetticket%3Faccess_token%3DACCESS_TOKEN%26type%3Djsapi" target="_blank" rel="nofollow noopener noreferrer" title="https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=ACCESS_TOKEN&type=jsapi" ref="nofollow noopener noreferrer">api.weixin.qq.com/cgi-bin/tic…</a><br>
成功返回如下JSON：</p>
<pre><code class="copyable">&#123;
  "errcode":0,
  "errmsg":"ok",
  "ticket":"bxLdikRXVbTPdHSM05e5u5sUoXNKd8-41ZO3MhKoyN5OfkWITDGgnr2fwJ0m9E8NYzWKVZvdVtaUgWvsdshFKA",
  "expires_in":7200
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>获得<code>jsapi_ticket</code>之后，就可以生成<code>JS-SDK</code>权限验证的签名了。我是使用官方提供的<code>python</code>版的<code>demo</code>生成的签名，调试前生成签名，填入配置，在微信开发者工具的公众号网页调试地址栏输入我们本地的开发<code>ip</code>再点击预览即可在手机上进行调试</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fdemo.open.weixin.qq.com%2Fjssdk%2Fsample.zip" target="_blank" rel="nofollow noopener noreferrer" title="http://demo.open.weixin.qq.com/jssdk/sample.zip" ref="nofollow noopener noreferrer">示例代码</a></p>
</blockquote>
<blockquote>
<p>备注：链接中包含php、java、nodejs以及python的示例代码供第三方参考，第三方切记要对获取的accesstoken以及jsapi_ticket进行缓存以确保不会触发频率限制。</p>
</blockquote>
</li>
</ol>
<h2 data-id="heading-2">python3的需要对官方提供的代码进行一定的修改</h2>
<pre><code class="hljs language-sing.py copyable" lang="sing.py">import time
import random
import string
import hashlib


class Sign:
    def __init__(self, jsapi_ticket, url):
        self.ret = &#123;
            'nonceStr': self.__create_nonce_str(),
            'jsapi_ticket': jsapi_ticket,
            'timestamp': self.__create_timestamp(),
            'url': url
        &#125;

    def __create_nonce_str(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

    def __create_timestamp(self):
        return int(time.time())

    def sign(self):
        string = '&'.join(['%s=%s' % (key.lower(), self.ret[key]) for key in sorted(self.ret)])
        print(string)
        string=string.encode("utf8")//需要先编码 不然运行会报错
        self.ret['signature'] = hashlib.sha1(string).hexdigest()
        return self.ret


if __name__ == '__main__':
    # 注意 URL 一定要动态获取，不能 hardcode
    sign = Sign('jsapi_ticket','url')//url 可以用本地开发地址(本机ip)方便调试
    print(sign.sign())
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            