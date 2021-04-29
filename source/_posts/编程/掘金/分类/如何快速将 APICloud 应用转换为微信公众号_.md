
---
title: '如何快速将 APICloud 应用转换为微信公众号_'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c80aff73211b47e3a8e7ff3f8a23658b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Apr 2021 01:25:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c80aff73211b47e3a8e7ff3f8a23658b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">现在,APICloud 应用,可以一键生成微信公众号！</h3>
<p>APICloud 基于积淀已久的 iOS/Android 原生引擎开发技术，结合微信公众号运行环境的特点，针对性地推出了为其量身定制的适配器环境，<strong>任何标准 APICloud 应用，都可以在不修改或极小修改之后,直接运行在微信环境中。</strong></p>
<p>基于 APICloud 应用生成的微信公众号，<strong>开发者可直接获取源码,部署到自己服务器上</strong>。核心配置文件，开发者可根据服务器环境需要，灵活修改。最重要的是: 为了便于开发者二次开发或与微信业务进一步对接，我们提供了足够开放和灵活的自定义扩展机制，开发者可根据业务需要，重写任意 APICloud 模块的内部实现。</p>
<h2 data-id="heading-1">步骤</h2>
<p>1. 登录 APICloud 网站控制台,选择或新建一个 Native 原生应用.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c80aff73211b47e3a8e7ff3f8a23658b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>2. 点击 "云编译"页面的 "一键生成微信公众号"</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1aa2557ce2f94ea9a036b2bfeb9b3be3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>3. 点击 "一键生成微信公众号"按钮,等待编译完成.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ea3b1774917406f9664a672ec65cdbe~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">4. 部署</h3>
<p>把云编译生成的压缩包,解压放到网站静态资源根目录,然后就可以通过类似</p>
<p><a href="http://www.exapmle.com/A6055344415623/web_adapter/adapter.html" target="_blank" rel="nofollow noopener noreferrer">www.exapmle.com/A6055344415…</a></p>
<p>一类的值来访问.其中 <strong>A6055344415623</strong> 要替换为自己应用的 appId.如果不想放在网站根目录,需要对应修改web_adapter/script/config.js中的相关配置.</p>
<h3 data-id="heading-3">5. 跨域访问问题</h3>
<blockquote>
<p>No 'Access-Control-Allow-Origin' header is present on the requested resource.</p>
</blockquote>
<p>如果控制台出现类似错误,说明当前预览微信公众号的网站与服务器接口不在同一个域名下,有两种解决方案:</p>
<ol>
<li>修改服务器端接口设置,允许跨域访问.</li>
<li>将云编译生成的静态资源包放置在到网络接口所在的服务器,保证二者可以在同一域名下访问.</li>
</ol>
<h3 data-id="heading-4">6. 原生模块适配问题</h3>
<p>APICloud 现在可以自动适配原 APICloud 原生 App 中标准 WEB 技术相关的逻辑.涉及到使用 APICloud 原生模块的地方,还需要开发者自行定制开发.</p>
<p>为了保持代码写法的一致,我们提供了和 APICloud 原生引擎类似的扩展机制,开发者可基于此重写 APICloud 原生模块的相关逻辑.</p>
<p>开发者原有代码一般不需要做修改,只需要依照我们提供的扩展机制,针对性地添加部分原生模块的扩展代码,即可实现微信公众号的适配.详见下文 <strong>"扩展"</strong> 部分</p>
<h2 data-id="heading-5">扩展</h2>
<p>APICloud 微信公众号适配器, 基于纯 Web 技术, 并针对微信的 Web 环境,有所优化.在接口实现上, 与 APICloud Native 引擎保持一致.基于此, 任意标准 APICloud 原生应用,都可以极低成本,迭代为微信公众号,甚至标准的网页应用.</p>
<p>APICloud 微信公众号适配器,在实现时,做了最大程度的开放性和灵活性设计.我们允许开发者重写任意 APICloud API 引擎对象或原生模块的任意方法和属性.</p>
<p>任意界面,只需要实现一个 <strong>apiadapter</strong> 方法,就可以在此方法内,拦截和重写 APICloud 模块方法的具体实现.</p>
<pre><code class="copyable">/*
当 frame, window, adapter 级别同时实现此函数时,
加载优先级为: frame > window > adapter > 内置默认实现

@payload:
@moduleName 模块名.
@method     方法名.
@isSync     是否是同步方法.
@params     调用模块方法时的参数.
@frameDom   frame 所在的 window dom对象.
@winDom     window 所在页面的 window dom 对象.
@apiDom     adapter 所在页面的 window dom 对象.
@cbId       调用模块方法时,传递的回调函数的唯一标识.
@callback   用于异步返回值的回调函数.(cbId, ret, err, del)=>&#123;&#125;
@cbId   调用模块方法时,传递的回调函数的唯一标识.
@ret    模块返回值.
@err    错误信息.
@del    调用后,是否删除此 cbId 对应的回调函数.
删除后,下一次基于同一 cbId调用callback,
将无法正确回传返回值.

@return: 不作处理.如果不想处理某个模块方法, 应该显式返回字符串 'TO_NEXT_API_ADAPTER',
以便往上传播调用.
*/
function apiadapter(payload) &#123;
/* TODO: 自定义的处理逻辑. */

/* 默认不作处理. */
return "TO_NEXT_API_ADAPTER";
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">扩展建议</h3>
<ul>
<li>异步方法的返回值,最好通过传入的callback和cbId传递.</li>
<li>同步方法的返回值,可以直接 return 返回相关值.</li>
<li>在处理 UI 类模块时,可在模块方法调用时添加一些自定义字段,以便于 apiadapter 能正确处理 UI 类模块的位置.如添加一个新的 parentDomId 字段,以便能自定义指定模块的父元素.</li>
</ul></div>  
</div>
            