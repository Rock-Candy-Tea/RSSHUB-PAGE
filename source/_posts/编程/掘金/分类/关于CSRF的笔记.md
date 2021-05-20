
---
title: '关于CSRF的笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://cors.zfour.workers.dev/?http://www.a.com:8002/content/delete/87343'
author: 掘金
comments: false
date: Wed, 19 May 2021 22:40:57 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://www.a.com:8002/content/delete/87343'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">什么是CSRF攻击？</h2>
<p>CSRF（Cross-site request forgery）跨站请求伪造：<strong>攻击者</strong>诱导<strong>受害者</strong>进入第三方网站，在第三方网站中，向被攻击网站发送<strong>跨站</strong>请求。利用受害者在被攻击网站已经获取的注册凭证，绕过后台的用户验证，达到冒充用户对被攻击的网站执行某项操作的目的。</p>
<h2 data-id="heading-1">举例说明CSRF攻击</h2>
<p>程序员小C在登录并浏览论坛网站a.com的时候，跳出来一个广告，是关于<strong>无恢复期植发</strong>，这对于一个程序员来说是多么有诱惑性啊，小C无法控制自己就点了进去。点进去之后，发现页面只有一张加载不出来的图片，小C表示很失望，就关闭了页面，但是不知道这个操作已经实现了CSRF攻击。</p>
<p>实现CSRF攻击的两个必要条件：</p>
<ul>
<li>用户登录受攻击网站，并返回cookie保存在浏览器端</li>
<li>用户在登录期间访问了第三方网站（攻击者网站），第三方网站冒充用户向受攻击网站发送请求，代替用户执行某些操作</li>
</ul>
<p>在a.com中，当用户删除某个帖子的时候，会发起请求<a href="http://www.a.com:8002/content/delete/:id" target="_blank" rel="nofollow noopener noreferrer">www.a.com:8002/content/del…</a> ，比如发起请求<a href="http://www.c.com:8002/content/delete/87343" target="_blank" rel="nofollow noopener noreferrer">www.c.com:8002/content/del…</a> 时，就会删除id为87343的帖子。</p>
<p>当小C登录网站a.com的时候，服务器会返回一个表示登录信息的cookie
<code>res.setHeader('Set-Cookie', ['user=22333; expires=Sat, 21 Jul 2018 00:00:00 GMT;']);</code></p>
<p>攻击者现在构造了一个陷阱页面，页面的内容如下：</p>
<p><code><p>CSRF 攻击者准备的网站：</p></code></p>
<p><code><img src="https://cors.zfour.workers.dev/?http://www.a.com:8002/content/delete/87343"></code></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a29e618ac9f4e70b34a12b957edd914~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>小C点击陷阱页面，浏览到该图片时，会自动发起一个请求，该请求因为是对a.com的请求，会携带a.com域名下的cookie（包含用户登录信息的cookie），此时攻击者网站就代替小C删除了ID为87343的帖子。</p>
<p>而小C对此一无所知。</p>
<p>通过上述例子，可以看出CSRF攻击是通过cookie实现的，攻击者通过引诱用户访问第三方网站实现的冒用用户实现一些操作的行为，该攻击属于被动型攻击。</p>
<h2 data-id="heading-2">CSRF的特点</h2>
<ul>
<li>攻击者只能冒用用户的cookie身份，但是不能获取用户的cookie</li>
<li>攻击者只能去执行一些操作，但是不能获取到操作的结果</li>
<li>攻击的行为一般是发生在第三方网站，受攻击网站无法防止</li>
<li>可以用各种方式实现攻击：图片URL、超链接、CORS、Form提交等等。部分请求方式可以直接嵌入在第三方论坛、文章中，难以进行追踪。</li>
</ul>
<h2 data-id="heading-3">CSRF的防范</h2>
<p>CSRF的防范可以分成两类：</p>
<ol>
<li>阻止不明外域的访问</li>
</ol>
<ul>
<li>
<p>同源检测</p>
</li>
<li>
<p>Samesite Cookie</p>
</li>
</ul>
<ol start="2">
<li>提交时要求附加本域才能获取的信息</li>
</ol>
<ul>
<li>
<p>CSRF Token</p>
</li>
<li>
<p>验证码</p>
</li>
</ul>
<h4 data-id="heading-4">1.  阻止不明外域的访问</h4>
<h5 data-id="heading-5">同源检测</h5>
<p>http请求中有一个字段Referer，它表示该http请求的来源，用户在a.com网站中发起的请求Referer字段都是a.com，而第三方网站发出的请求都不是a.com，禁止一切Referer不为a.com的请求，即可防止CSRF攻击。</p>
<p><code>if (req.headers.referer !== 'http://www.c.com:8002/') &#123;     res.write('csrf 攻击');     return; &#125;</code></p>
<p>还有一个作用是：防止别人盗取图片链接，在自己的网站中使用。</p>
<h5 data-id="heading-6">Samesite Cookie</h5>
<p>Samesite是chrome提出的增强网络安全的cookie属性，它用来表明cookie是第一方cookie（同站cookie），即不允许携带第三方cookie。</p>
<p>Samesite 有两个属性值，分别是 Strict 和 Lax：</p>
<p>Strict:不允许携带第三方cookie，即在访问b.com网站时不允许携带a.com域名下的cookie</p>
<p>Lax:只有链接跳转和get表单提交可以携带cookie，post表单提交和跨站的异步请求则不会携带。</p>
<p>None:允许携带第三方cookie</p>
<p>Samesite的默认值从None变成了Lax，在一定程度上增强了网络的安全性，保护了用户的隐私。<a href="https://juejin.cn/post/6956527200954761247" target="_blank">更多关于该属性的内容请点击</a></p>
<p>Samesite的默认值变成Lax之后，可以很大程度上减少CSRF的攻击，但是无法避免链接跳转型的CSRF的攻击。将Samesite设置成Strict，可以避免所有的CSRF攻击，但是这样就无法同步子系统下的登录信息，很不方便。</p>
<h4 data-id="heading-7">2.  提交时要求附加本域才能获取的信息</h4>
<p>这种方式可以起作用是因为攻击者只能利用用户的cookie，却无法取到用户真正的cookie信息，在cookie的基础上附加攻击者无法取到的额外信息（不放在cookie中）就可以避免CSRF攻击。</p>
<ul>
<li>CSRF Token</li>
</ul>
<p>该方法是在请求的参数中携带一个随机生成的token，然后在服务器端加一个拦截器，如果请求中的token不正确或者没有携带token，就拒绝该请求。</p>
<ul>
<li>验证码</li>
</ul>
<p>也是利用攻击者无法取到真正的用户才能获取到的信息来验证用户身份。</p>
<p>验证码被认为是对抗 CSRF 攻击最简洁而有效的防御方法。</p>
<p>就是在用户执行一些重要行为的时候，附加验证码验证用户行为，可以有效对抗CSRF攻击，但是给网站中的所有行为加验证码当然是不可取的，可以适当取用。</p>
<h2 data-id="heading-8">CSRF用户自我防范</h2>
<p>尽量不要打开可疑链接，一定要打开时，使用不常用的浏览器。</p>
<p>参考文章：</p>
<p><a href="https://github.com/dwqs/blog/issues/68" target="_blank" rel="nofollow noopener noreferrer">github.com/dwqs/blog/i…</a>
<a href="https://juejin.cn/post/6844903689702866952#heading-28" target="_blank">juejin.cn/post/684490…</a></p></div>  
</div>
            