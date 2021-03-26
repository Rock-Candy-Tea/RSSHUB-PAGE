
---
title: 'App路由模块设计'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=3780'
author: 掘金
comments: false
date: Sun, 28 Feb 2021 22:38:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=3780'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>开发客户端路由，一是为了管理客户端内部的模块通信，二是为客户端外部提供与客户端通信的渠道。</p>
<p>内部通信的使用目的是解耦模块之间的依赖，避免引入模块导致的多余维护工作，也可以解决在可能出现循环依赖的模块之间通信问题。同时，引入路由方案，能更好的维护与管理模块的API。</p>
<p>外部通信的使用目的是为产品打造通用的客户端通信协议，比如从推送跳转到用户聊天界面，从浏览器的网页唤起客户端，打开指定内容页面，为小程序的H5端提供Native能力。外部协议更可以统一整个平台客户端的通信API，统一不同平台客户端（如Win、Mac、Android、iOS）的能力。</p>
<h2 data-id="heading-1">架构设计</h2>
<h3 data-id="heading-2">反射跳转管理模块（Performer）</h3>
<p>借鉴CTMediator的实现思路，利用OC的Runtime机制，调用函数动态生成来解决模块依赖的问题。</p>
<p>通过TargetClassName（String）、SeletorName（String）、Params（Map）、UserInfo（Map）、Callback（Block）来发起一次函数调用，异步调用通过Callback实现。</p>
<p>在调用前，需要先对函数的各个参数进行基本校验。校验都通过后，使用NSInvocation来组装函数的调用。</p>
<blockquote>
<p>需要注意的是，接收NSInvocation的返回值时，返回值的引用计数是需要手动管理的。</p>
</blockquote>
<h3 data-id="heading-3">路由规则模型（RuleModel）</h3>
<p>参考传统的URL规则，抽象出路由的基本信息。</p>
<p>基本结构：scheme://host/path?arg1=aa&arg2=bb</p>
<p>比如：pluto://charon/im/session?id=123&name=ginhoor</p>
<p>分解后 scheme：pluto，host：charon，path：/im/session，params：&#123;id:123,name:ginhoor&#125;</p>
<p>为了方便客户端使用，增加特定参数（不同的平台会使用不同的字段）：</p>
<ol>
<li>vcClassName，iOS的视图控制器类名。</li>
<li>paramsClassName，视图控制器参数接收器的类名。</li>
<li>openType，视图打开方式（模态打开或者导航器打开，是否带有动画）。</li>
<li>isPrivate，指定该规则是否对外使用，如果为False，则只有客户端内部发起才能成功。</li>
</ol>
<p>为了增强规则的可读性，还增加了几个参数：</p>
<ol>
<li>demo，填写用于演示的URL字符串。</li>
<li>remark，填写用于描述该规则功能的字符串。</li>
</ol>
<p>如下，最终将这些规则整理程JSON文件，统一管理维护。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"version"</span>:<span class="hljs-string">"1.0.0"</span>,
    <span class="hljs-attr">"rules"</span>:[
        &#123;
            <span class="hljs-attr">"iOSVCClassName"</span>:<span class="hljs-string">"MCGlobalCategorySearchVC"</span>,
            <span class="hljs-attr">"iOSParamsClassName"</span>:<span class="hljs-string">"MCGlobalCategorySearchVCInputParams"</span>,
            <span class="hljs-attr">"params"</span>:&#123;
                <span class="hljs-attr">"type"</span>:<span class="hljs-number">1</span>,
                <span class="hljs-attr">"keywords"</span>:<span class="hljs-string">"kw"</span>,
                <span class="hljs-attr">"fromVC"</span>:<span class="hljs-string">"IMSessionVC"</span>
            &#125;,
            <span class="hljs-attr">"host"</span>:<span class="hljs-string">"route"</span>,
            <span class="hljs-attr">"path"</span>:<span class="hljs-string">"/home/category_search"</span>,
            <span class="hljs-attr">"demo"</span>:<span class="hljs-string">"daqun://route/home/category_search?type=1&keywords=kw&fromVC=IMSessionVC"</span>,
            <span class="hljs-attr">"isPrivate"</span>:<span class="hljs-number">0</span>,
            <span class="hljs-attr">"remark"</span>:<span class="hljs-string">"MCGlobalCategorySearchVC"</span>
        &#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">路由规则配置（Rule Configuration）</h3>
<p>维护与管理客户端整个路由规则的配置。</p>
<ol>
<li>客户端路由、HTTP Host白名单</li>
<li>公域Scheme、私域Scheme白名单</li>
<li>用于客户端生成路由URL的公域Scheme域与客户端路由Host。</li>
</ol>
<p>客户端启动时，会将本地预埋的JSON路由规则加载到客户端中。同时，需要为服务端提供配置下发方案，当服务端推送新的路由规则时，需要对本地路由规则进行更新。</p>
<p>最后需要为路由规则创建不同字段的索引，优化路由的解析耗时。</p>
<h3 data-id="heading-5">URL跳转管理模块 （Open URL）</h3>
<p>URL分为三种，一种由客户端生成的本地URL，一种客户端以外途径生成的远程URL了，这两种可以通过路由规则中的isPrivate可以对URL的入口进行权限控制。最后一种是比较特别的HTTP URL，是纯HTTP的请求链接，但除去Scheme与Host，是可以与配置中的路由规则对应的，这也是一种有效的URL。</p>
<p>如果使用客户端路由URL生成二维码，用户当微信扫了这个二维码，而手机上没有安装我们的客户端，那么这次URL唤醒动作将失败，但如果使用中转页面的URL，微信扫了二维码，中转页面会判断是否可以直接唤起我们的客户端，如果不行，则可以引导用户进行下载。</p>
<p>所以HTTP URL这种形式，是为了在生成业务分享二维码时，可以使用中转页面的URL，同时中转页的URL维护规则又与客户端路由规则相兼容，做到最大程度的复用。</p>
<p>在客户端内部的模块间通信时，可以用反射模块直接通信（比如，注销IM用户，跳转会话界面）。也可以根据路由规则，先组装成URL字符串，经业务模块传递后，再后路由模块解析跳转（比如通过卡片消息转发H5分享路由地址）。</p>
<p>最后，如果URL无法通过合法性校验时，路由模块会调用系统的OpenURL来接管后续操作。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            