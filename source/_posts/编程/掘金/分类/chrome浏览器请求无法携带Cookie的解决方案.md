
---
title: 'chrome浏览器请求无法携带Cookie的解决方案'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08cbe0a4840b4d3f8442b2ba09c4adee~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 19:59:44 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08cbe0a4840b4d3f8442b2ba09c4adee~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">遇到的问题</h3>
<p>最近在本地(localhost)开发项目的时候，遇到明明登陆了，但是接口一直返回未登陆，一查发现接口没有携带cookie。</p>
<h3 data-id="heading-1">究其原因发现：</h3>
<p>Chrome在51版本时为cookie增加了SameSite属性，用于防止跨域携带Cookie引发的用户行为跟踪和CSRF攻击，80版本以下SameSite属性默认为none，跨域请求能够携带cookie。Chrome升级到80版本之后cookie的SameSite属性默认值由None变为Lax，造成了一些访问跨域cookie无法携带的问题！</p>
<h4 data-id="heading-2">那SameSite 又是什么呢？</h4>
<p>是浏览器的Cookie用来防止CSRF攻击和用户追踪而新增的一个属性。</p>
<h4 data-id="heading-3">SameSite的值有三种：</h4>
<h5 data-id="heading-4">1、Strict 最严格，完全禁止第三方cookie。只要跨站点就会丢cookie。用户体验非常不好。</h5>
<pre><code class="copyable">Set-Cookie: CookieName=CookieValue; SameSite=Strict;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">2、Lax chrome>80 Lax是默认值） 稍微严格，大多数的情况下也是禁止第三方cookie。但是导航到目标网址的GET 请求除外。</h5>
<pre><code class="copyable">Set-Cookie: CookieName=CookieValue; SameSite=Lax;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">3、None（chrome<80 None是默认值) chrome>80的话 因为lax是默认值，只允许第三方get情况可以携带cookie，如果是post跨域请求的话就会导致 cookie丢失问题，需要手动的将SameSite设置为None(前提是必须同时设置Secure属性（Cookie 只能通过 HTTPS 协议发送）);</h5>
<p>无效代码</p>
<pre><code class="copyable">Set-Cookie: widget_session=abc123; SameSite=None
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有效代码</p>
<pre><code class="copyable">Set-Cookie: widget_session=abc123; SameSite=None; Secure
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据上述，我们不难发现只要将SameSite属性设置成None，就可以解决我们遇到的问题。</p>
<h3 data-id="heading-7">具体的解决方案如下：</h3>
<h4 data-id="heading-8">1、通过改变浏览器的设置</h4>
<h5 data-id="heading-9">MAC:</h5>
<h5 data-id="heading-10">1.1 第一种方式：手动打开chrome</h5>
<p>chrome://settings/safetyCheck</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08cbe0a4840b4d3f8442b2ba09c4adee~tplv-k3u1fbpfcp-watermark.image" alt="cookie.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>chrome://flags/</p>
<h5 data-id="heading-11">if version < 91 设置如下：</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8d0496407bf47cbac837b10db8d186b~tplv-k3u1fbpfcp-watermark.image" alt="low91.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-12">else if version >= 91 设置如下：</h5>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66873d65d15447e1b5da05d9522ec6c9~tplv-k3u1fbpfcp-watermark.image" alt="high91.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Relaunch chrome(重启chrome)</p>
<h5 data-id="heading-13">1.2 第二种方式：命令行携带cookie方式打开chrome</h5>
<p><em><strong>注：需要关闭所有的浏览器窗口并退出chrome后操作</strong></em></p>
<pre><code class="copyable">open -a "Google Chrome" --args --disable-features=SameSiteByDefaultCookies
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">open -a "Microsoft Edge" --args --disable-features=SameSiteByDefaultCookies
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注：Mac系统下通过执行命令运行浏览器如果依旧无法解决可尝试重启浏览器后再执行命令打开浏览器，该命令需要保证完全关闭并退出浏览器再执行才能生效。</strong></p>
<h5 data-id="heading-14">else if version >= 94</h5>
<pre><code class="copyable">The flags #same-site-by-default-cookies and #cookies-without-same-site-must-be-secure have been removed from chrome://flags as of Chrome 91, as the behavior is now enabled by default. In Chrome 94, the command-line flag --disable-features=SameSiteByDefaultCookies,CookiesWithoutSameSiteMustBeSecure will be removed.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>94以后 通过命令行禁用设置SameSite默认值的方式会被移除，1.1方式一和1.2方式二都会失效，这时候 只能通过3的Nginx代理或软件将跨域请求转为非跨域请求来解决。</p>
<h5 data-id="heading-15">windows</h5>
<p>打开Chrome快捷方式的属性，在目标后添加--disable-features=SameSiteByDefaultCookies，点击确定，关闭所有Chrome窗口包括Chrome浏览器后再重启浏览器运行项目即可解决。</p>
<p><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>windows</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a5df1abbc4947a19a3e39dee6f9eab0~tplv-k3u1fbpfcp-watermark.image" alt="windows.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-16">2、通过设置后端响应头</h4>
<p>Set-Cookie: widget_session=abc123; SameSite=None; Secure</p>
<h4 data-id="heading-17">3、通过改变Nginx的location配置</h4>
<p>proxy_cookie_path / "/; httponly; secure; SameSite=None";</p>
<h4 data-id="heading-18">4、闲上面三个还需要操作的话，可以直接换成 火狐等其他非chrome浏览器进行本地开发</h4></div>  
</div>
            