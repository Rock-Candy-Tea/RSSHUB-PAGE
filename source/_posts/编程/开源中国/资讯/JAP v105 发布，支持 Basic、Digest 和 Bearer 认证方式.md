
---
title: 'JAP v1.0.5 发布，支持 Basic、Digest 和 Bearer 认证方式'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6556'
author: 开源中国
comments: false
date: Fri, 24 Sep 2021 14:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6556'
---

<div>   
<div class="content">
                                                                                            <ul> 
 <li>feat: 增加 <code>jap-http-api</code> 模块。 (Gitee Issue <a href="https://gitee.com/fujieid/jap/issues/I43ZS7">#I43ZS7</a>)</li> 
 <li>feat: 增加 <code>jap-ids-web</code> 模块。 将 <code>jap-ids</code> 的过滤器打包为一个单独的组件。</li> 
 <li>feat: 添加 HTTP servlet 适配器以解耦 jakarta servlet。<strong>注[1]</strong></li> 
 <li>feat: [jap-social] 支持绑定第三方平台账号，该版本将社会化登录和绑定账号独立开来，以使其更加使用与多场景。 (Gitee Issue <a href="https://gitee.com/fujieid/jap/issues/I46J6W">#I46J6W</a>)</li> 
 <li>change: [jap-ids] <code>scope</code> 在各个流程中都更改为可选，遵循 RFC6749 规范。</li> 
 <li>change: [jap-sso] 升级 <code>kisso</code> 的版本为 3.7.7, <strong>解决 jackson 的漏洞</strong>。</li> 
 <li>change: [jap-mfa] 升级 <code>googleauth</code> 的版本为 1.5.0, <strong>解决 apache httpclient 的漏洞</strong>。</li> 
 <li>change: 替换文档站主题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjustauth.plus" target="_blank">https://justauth.plus</a>，解决文档站内存暴涨的问题。（Gitee Issue <a href="https://gitee.com/fujieid/jap/issues/I4958H">#I4958H</a> | Github Issue <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffujieid%2Fjap%2Fissues%2F8" target="_blank">#8</a>）</li> 
 <li>change: 升级 <code>simple-http</code> 的版本为 1.0.5.</li> 
 <li>change: 升级 <code>JustAuth</code> 的版本为 1.16.4.</li> 
 <li>change: 优化代码，添加 package-info。</li> 
</ul> 
<p><strong>注[1]:</strong></p> 
<p>在 1.0.5 以前版本，jap 中依赖 <code>jakarta-servlet</code> 中 <code>javax.servlet.http</code> 包下的 <code>HttpServletRequest</code>、<code>Cookie</code>、<code>HttpServletResponse</code> 、<code>HttpSession</code>，比如：</p> 
<pre><code class="language-java">// jap 提供的接口
public interface JapStrategy &#123;
  default JapResponse authenticate(AuthenticateConfig config, HttpServletRequest request, HttpServletResponse response) &#123;
    return null;
  &#125;
&#125;
</code></pre> 
<pre><code class="language-java">// 在spring框架中使用 jap
XxJapStrategy.authenticate(config,request,response);
</code></pre> 
<p>为了提高框架适配性，自 1.0.5 版本开始，JAP 去掉了 <code>jakarta-servlet</code> 依赖，采用了一套全新的接口（参考：<a href="https://gitee.com/fujieid/jap-http">jap-http</a>），开发者在调用 JAP 接口时需要对原 request 进行适配。</p> 
<p>比如，开发者使用了 <code>jakarta-servlet</code>，那么需要对 <code>HttpServletRequest</code> 进行适配处理：</p> 
<pre><code class="language-java">// 在spring框架中使用 1.0.5 或更高级版本的 jap
XxJapStrategy.authenticate(config,new JakartaRequestAdapter(request),new JakartaResponseAdapter(response));
</code></pre> 
<p><code>jap-http-api</code> 更多使用帮助，请参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjustauth.plus%2Fquickstart%2Fjap-http-api%2F" target="_blank">https://justauth.plus/quickstart/jap-http-api/</a></p>
                                        </div>
                                      
</div>
            