
---
title: '如何优雅的解决 Qiankun 下 Sentry 异常上报无法自动区分项目的问题 _'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0537930e4c14f9a85ae832a2acc520e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 19:50:45 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0537930e4c14f9a85ae832a2acc520e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:var(--cyanosis-base-color);transition:color .35s;--cyanosis-base-color:#353535;--cyanosis-title-color:#005bb7;--cyanosis-strong-color:#2196f3;--cyanosis-em-color:#4fc3f7;--cyanosis-del-color:#ccc;--cyanosis-link-color:#3da8f5;--cyanosis-linkh-color:#007fff;--cyanosis-border-color:#bedcff;--cyanosis-border-color-2:#ececec;--cyanosis-bg-color:#fff;--cyanosis-blockquote-color:#8c8c8c;--cyanosis-blockquote-bg-color:#f0fdff;--cyanosis-code-color:#c2185b;--cyanosis-code-bg-color:#fff4f4;--cyanosis-code-pre-color:#f8f8f8;--cyanosis-table-border-color:#c3e0fd;--cyanosis-table-th-color:#dff0ff;--cyanosis-table-tht-color:#005bb7;--cyanosis-table-tr-nc-color:#f7fbff;--cyanosis-table-trh-color:#e0edf7;--cyanosis-slct-title-color:#005bb7;--cyanosis-slct-titlebg-color:rgba(175,207,247,0.25);--cyanosis-slct-text-color:#c80000;--cyanosis-slct-bg-color:rgba(175,207,247,0.25);--cyanosis-slct-del-color:#999;--cyanosis-slct-elbg-color:#e8ebec;--cyanosis-slct-codebg-color:#ffeaeb;--cyanosis-slct-prebg-color:rgba(160,200,255,0.25)&#125;.markdown-body.__dark&#123;--cyanosis-base-color:#cacaca;--cyanosis-title-color:#ddd;--cyanosis-strong-color:#fe9900;--cyanosis-em-color:#ffd28e;--cyanosis-del-color:#ccc;--cyanosis-link-color:#ffb648;--cyanosis-linkh-color:#fe9900;--cyanosis-border-color:#ffe3ba;--cyanosis-border-color-2:#ffcb7b;--cyanosis-bg-color:#2f2f2f;--cyanosis-blockquote-color:#c7c7c7;--cyanosis-blockquote-bg-color:rgba(255,199,116,0.1);--cyanosis-code-color:#000;--cyanosis-code-bg-color:#ffcb7b;--cyanosis-code-pre-color:rgba(255,227,185,0.5);--cyanosis-table-border-color:#fe9900;--cyanosis-table-th-color:#ffb648;--cyanosis-table-tht-color:#000;--cyanosis-table-tr-nc-color:#6d5736;--cyanosis-table-trh-color:#947443;--cyanosis-slct-title-color:#000;--cyanosis-slct-titlebg-color:#fe9900;--cyanosis-slct-text-color:#00c888;--cyanosis-slct-bg-color:rgba(175,207,247,0.25);--cyanosis-slct-del-color:#999;--cyanosis-slct-elbg-color:#000;--cyanosis-slct-codebg-color:#ffcb7b;--cyanosis-slct-prebg-color:rgba(160,200,255,0.25)&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:var(--cyanosis-title-color);transition:color .35s&#125;.markdown-body h2&#123;position:relative;padding-left:10px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid var(--cyanosis-border-color-2)&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-14px&#125;.markdown-body h2:after&#123;content:"」";position:relative;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:var(--cyanosis-strong-color)&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,var(--cyanosis-link-color),rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),var(--cyanosis-link-color));border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background-color:var(--cyanosis-bg-color);background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center;transition:background-color .5s&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:var(--cyanosis-code-color);word-break:break-word;overflow-x:auto;background-color:var(--cyanosis-code-bg-color);border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:var(--cyanosis-code-pre-color)&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:var(--cyanosis-border-color)&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:var(--cyanosis-strong-color);border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:var(--cyanosis-link-color);border-bottom:1px solid var(--cyanosis-border-color)&#125;.markdown-body a:hover&#123;border-bottom-color:var(--cyanosis-linkh-color)&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:var(--cyanosis-linkh-color)&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid var(--cyanosis-border-color);transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:var(--cyanosis-linkh-color)&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid var(--cyanosis-table-border-color);border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:var(--cyanosis-table-tr-nc-color)&#125;.markdown-body table tr:hover&#123;background-color:var(--cyanosis-table-trh-color)&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid var(--cyanosis-table-border-color)&#125;.markdown-body table th&#123;color:var(--cyanosis-table-tht-color);background-color:var(--cyanosis-table-th-color)&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:var(--cyanosis-blockquote-color);border-left:4px solid var(--cyanosis-strong-color);background-color:var(--cyanosis-blockquote-bg-color);padding:1px 20px;margin:22px 0;transition:color .35s&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:var(--cyanosis-strong-color)&#125;.markdown-body em,.markdown-body i&#123;color:var(--cyanosis-em-color)&#125;.markdown-body del&#123;color:var(--cyanosis-del-color)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:var(--cyanosis-title-color);font-size:20px;font-weight:bolder;border-bottom:1px solid var(--cyanosis-border-color);cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:var(--cyanosis-blockquote-bg-color);border:2px dashed var(--cyanosis-strong-color)&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:var(--cyanosis-slct-title-color);background-color:var(--cyanosis-slct-titlebg-color)&#125;.markdown-body ol li::selection,.markdown-body p::selection,.markdown-body ul li::selection&#123;color:var(--cyanosis-slct-text-color);background-color:var(--cyanosis-slct-bg-color)&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:var(--cyanosis-slct-elbg-color)&#125;.markdown-body del::selection&#123;color:var(--cyanosis-slct-del-color);background-color:var(--cyanosis-slct-elbg-color)&#125;.markdown-body table thead th::selection&#123;background-color:transparent&#125;.markdown-body table tbody td::selection&#123;background-color:var(--cyanosis-slct-bg-color)&#125;.markdown-body code::selection&#123;background-color:var(--cyanosis-slct-codebg-color)&#125;.markdown-body pre>code::selection&#123;background-color:var(--cyanosis-slct-prebg-color)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcreativecommons.org%2Flicenses%2Fby%2F4.0%2Fdeed.zh" target="_blank" rel="nofollow noopener noreferrer" title="https://creativecommons.org/licenses/by/4.0/deed.zh" ref="nofollow noopener noreferrer">「署名 4.0 国际 (CC BY 4.0)」</a> 许可协议，欢迎转载、或重新修改使用，但需要注明来源。</p>
<blockquote>
<p>作者: 百应前端团队 <a href="https://juejin.cn/post/7012772225644232741" target="_blank" title="https://juejin.cn/post/7012772225644232741">@0o华仔o0</a> 首发于 <a href="https://juejin.cn/post/7139452175088320520" target="_blank" title="https://juejin.cn/post/7139452175088320520">如何优雅的解决 Qiankun 下 Sentry 异常上报无法自动区分项目的问题 ?</a></p>
</blockquote>
<h3 data-id="heading-0">前言</h3>
<p>最近项目组决定将前端异常监控由 <code>Fundebug</code> 切换为 <code>Sentry</code>。整个切换过程可以说非常简单，部署一个后台服务，然后将 <code>Sentry SDK</code> 集成到前端应用中就完事儿了。在之后的使用过程中，小编遇到了一个问题。由于我们的项目采用的是基于 <code>qiankun</code> 的微前端架构，在应用使用过程中，常常会出现发生异常应用和上报应用不匹配的情况。</p>
<p>为了解决这个问题，小编先去 <code>qiankun</code> 的 <code>issue</code> 下翻了翻，看有没有好的解决方案。虽然也有不少人遇到了同样的问题 - <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fumijs%2Fqiankun%2Fissues%2F1088" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/umijs/qiankun/issues/1088" ref="nofollow noopener noreferrer">求教一下 主子应用的sentry应该如何实践 #1088</a></strong>，但是社区里并没有一个好的解决方案。于是乎小编决定自己去阅读 <code>Sentry</code> 源码和官方文档，期望能找到一种合理并通用的解决方案。</p>
<p>经过一番梳理，小编如愿找到了解决方案，并且效果还不错。接下来小编就带着大家一起了解一下整个解决方案的具体情况。</p>
<p>本文的目录结构如下:</p>
<ul>
<li>
<p><strong><a href="https://juejin.cn/post/7141222298622623775#1" title="#1">使用 Sentry 上报异常</a></strong></p>
</li>
<li>
<p><strong><a href="https://juejin.cn/post/7141222298622623775#2" title="#2">解决方案</a></strong></p>
<ul>
<li>
<p><strong><a href="https://juejin.cn/post/7141222298622623775#2-1" title="#2-1">失败的方案一</a></strong></p>
</li>
<li>
<p><strong><a href="https://juejin.cn/post/7141222298622623775#2-2" title="#2-2">不通用的方案二</a></strong></p>
</li>
<li>
<p><strong><a href="https://juejin.cn/post/7141222298622623775#2-3" title="#2-3">合理、优雅的方案三</a></strong></p>
</li>
<li>
<p><strong><a href="https://juejin.cn/post/7141222298622623775#2-4" title="#2-4">7.x 版本解决方案</a></strong></p>
</li>
</ul>
</li>
<li>
<p><strong><a href="https://juejin.cn/post/7141222298622623775#3" title="#3">结束语</a></strong></p>
</li>
</ul>
<h3 id="user-content-1" data-id="heading-1">使用 Sentry 上报异常</h3>
<p>在正式介绍解决方案之前，小编先带大家简单回顾一下一个前端应用是如何接入 <code>Sentry</code> 的。</p>
<ol>
<li>
<p>第一步，在 <code>Sentry</code> 管理后台构建一个项目</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0537930e4c14f9a85ae832a2acc520e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="Aug-30-2022 10-20-22.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>项目创建好以后，会自动生成一个 <code>dsn</code>，这个 <code>dsn</code> 会在前端项目接入 Sentry 时作为必填项传入。</p>
</li>
<li>
<p>第二步，前端应用接入 <code>Sentry</code></p>
<p>前端应用接入 <code>Sentry</code> 也非常简单，只要使用 <code>Sentry</code> 提供的 <code>init</code> api，传入必传的 <code>dsn</code> 就可以了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">ReactDOM</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"react-dom"</span>;
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> <span class="hljs-title class_">Sentry</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"@sentry/react"</span>;
<span class="hljs-keyword">import</span> &#123; <span class="hljs-title class_">Integrations</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@sentry/tracing"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"./App"</span>;

<span class="hljs-title class_">Sentry</span>.<span class="hljs-title function_">init</span>(&#123;
  <span class="hljs-attr">dsn</span>: <span class="hljs-string">"https://90eb5fc98bf447a3bdc38713cc253933@sentry.byai.com/66"</span>,
  <span class="hljs-attr">integrations</span>: [<span class="hljs-keyword">new</span> <span class="hljs-title class_">Integrations</span>.<span class="hljs-title class_">BrowserTracing</span>()],
  <span class="hljs-attr">tracesSampleRate</span>: <span class="hljs-number">1.0</span>,
&#125;);

<span class="hljs-title class_">ReactDOM</span>.<span class="hljs-title function_">render</span>(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">App</span> /></span></span>, <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">"root"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>经过这两步，前端应用的异常监控接入就完成了。当应用在使用时，如果发生异常，<code>Sentry</code> 会自动捕获异常，然后上报到后台管理系统。上报完成以后，我们就可以在项目的 <code>issues</code> 中查看异常并着手修复。</p>
<p>单个的 <code>Spa</code> 应用接入 <code>Sentry</code> 时按照上面的步骤无脑操作就可以了，但如果应用是基于 <code>qiankun</code> 的微前端架构，那就需要解决异常上报不匹配的问题了。</p>
<p>小编手上的项目就是采用了基于 <code>qiankun</code> 的微前端架构，一个页面会至少同时存在两个应用，有时甚至会有 3 到 4 个应用。在应用使用过程中，常常会出现异常上报不匹配的问题。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d902cf5cf3d14a049816b295fd2334e9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图所示，主应用、cc sdk 应用中的异常都会上报到 aicc 项目中，这给异常处理带来很大的困扰。</p>
<p>出现这个问题的原因也非常好理解。</p>
<p><code>Sentry</code> 在执行 <code>init</code> 方法时会通过覆写 <code>window.onerror</code>、<code>window.unhandledrejection</code> 的方式初始化异常捕获逻辑。之后不管是哪个应用发生异常，都最终会触发 <code>onerror</code>、<code>unhandledrejection</code> 的 <code>callback</code> 而被 <code>Sentry</code> 感知，然后上报到 <code>dsn</code> 指定的项目中。而且 <code>Sentry</code> 的 <code>init</code> 代码不管是放在主应用中，还是放在子应用里面，都没有质的改变，所有被捕获的异常还是会一股脑的上报到某个项目中，无法自动区分。</p>
<p>了解了异常上报无法自动区分的问题，接下来小编就给大家讲一下自己是如何解决这个问题的。</p>
<h3 id="user-content-2" data-id="heading-2">解决方案</h3>
<p>想要解决这个问题，我们必须要先找到问题的切入点，而异常上报时的接口调用就是这个切入点。</p>
<p>当 <code>Sentry</code> 捕获到应用产生的异常时，会调用一个接口来上报异常，如下:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f013f6bb47c4334a83099db720f76a9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对比这个接口的 <code>url</code> 和上报应用的 <code>dsn</code>，我们可以发现异常上报接口的 <code>url</code> 其实是由上报应用的 <code>dsn</code> 转化来的，转化过程如下:</p>
<pre><code class="hljs language-perl copyable" lang="perl">// https:<span class="hljs-regexp">//</span><span class="hljs-number">62187</span>b367e474822bb9cb733c8a89814@sentry.byai.com/<span class="hljs-number">56</span>
dsn - https:<span class="hljs-regexp">//</span><span class="hljs-string">&#123;param1&#125;<span class="hljs-subst">@&#123;param2&#125;</span></span>/<span class="hljs-string">&#123;param3&#125;</span>
                |
                |
                v
url - https:<span class="hljs-regexp">//</span><span class="hljs-string">&#123;param2&#125;</span>/api/<span class="hljs-string">&#123;param3&#125;</span>/store/?sentry_key=<span class="hljs-string">&#123;param1&#125;</span>&sentry_version=<span class="hljs-number">7</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们再来看看这个上报接口携带的参数:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1119da1835c479589ab8ecf2baac73a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在接口参数中，<code>exceptions.values[0].stacktrace.frames</code> 是异常的追踪栈信息。通过栈信息中的 <code>filename</code> 字段，我们可以知道发生异常的 <code>js</code> 文件的 <code>url</code>。通常情况下，微前端中各个子应用的 <code>js</code> 的 <code>url</code> 前缀是不相同的(各个子应用静态文件的位置是分离的)，那么根据发生异常的 <code>js</code> 的 <code>url</code> 就可以判断该异常属于哪个应用。</p>
<p>有了上面两个信息，异常上报自动区分的解决方案就清晰明了了:</p>
<ol>
<li>
<p>第一步拦截异常上报接口，拿到异常详情，根据追踪栈中的 <code>filename</code> 判断异常属于哪个应用；</p>
</li>
<li>
<p>第二步，根据匹配应用的 <code>dsn</code> 重新构建 <code>url</code>；</p>
</li>
<li>
<p>第三步，使用新的 <code>url</code> 上报异常；</p>
</li>
</ol>
<p>在这个方案中，最关键的是拦截异常上报接口。为了能实现这一步，小编进行了各种尝试。</p>
<h4 id="user-content-2-1" data-id="heading-3">失败的方案一</h4>
<p>由于 <code>Sentry</code> 异常上报是通过 <code>window.fetch(url, options)</code> 来实现的，所以我们可以通过覆写 <code>window.fetch</code> 的方式去拦截异常上报。</p>
<p>代码实现如下:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> originFetch = <span class="hljs-variable language_">window</span>.<span class="hljs-property">fetch</span>;
<span class="hljs-variable language_">window</span>.<span class="hljs-property">fetch</span> = <span class="hljs-function">(<span class="hljs-params">url, options</span>) =></span> &#123;
    <span class="hljs-comment">// 根据 options 中的异常信息，返回新的 url 和 options</span>
    <span class="hljs-keyword">const</span> [newUrl, newOptions] = <span class="hljs-title function_">sentryFilter</span>(url, options);
    <span class="hljs-comment">// 使用原生的 fetch</span>
    <span class="hljs-keyword">return</span> <span class="hljs-title function_">originFetch</span>(newUrl, newOptions);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该方案看起来很靠谱，然而在实际使用的时候并未发挥作用，原因是 <code>Sentry</code> 内部只会使用原生的 <code>fetch</code>。如果发现 <code>fetch</code> 方法被覆写，那么 <code>Sentry</code> 会通过自己的方式重新去获取原生的 <code>fetch</code>。</p>
<p>小编截取了 Sentry 的部分源码给大家看一下:</p>
<pre><code class="hljs language-ini copyable" lang="ini">// FetchTransport 是一个构造函数
// Sentry 在执行 init 方法时会构建一个 FetchTransport 实例，然后通过这个 FetchTransport 实例调用 window.fetch 方法去做异常上报
function FetchTransport(options, fetchImpl) &#123;
    if (<span class="hljs-attr">fetchImpl</span> === void <span class="hljs-number">0</span>) &#123; fetchImpl = getNativeFetchImplementation()<span class="hljs-comment">; &#125;</span>
    var <span class="hljs-attr">_this</span> = _super.call(this, options) || this<span class="hljs-comment">;</span>
    <span class="hljs-attr">_this._fetch</span> = fetchImpl<span class="hljs-comment">;</span>
    return _this<span class="hljs-comment">;</span>
&#125;

// 使用原生的 window.fetch 实现 FetchTransport
function getNativeFetchImplementation() &#123;
    if (cachedFetchImpl) &#123;
        return cachedFetchImpl<span class="hljs-comment">;</span>
    &#125;
    // 根据 isNativeFetch 来判断 window.fetch 是否被覆写
    if (isNativeFetch(global$7.fetch)) &#123;
        return (<span class="hljs-attr">cachedFetchImpl</span> = global<span class="hljs-variable">$7</span>.fetch.bind(global<span class="hljs-variable">$7</span>))<span class="hljs-comment">;</span>
    &#125;
    var <span class="hljs-attr">document</span> = global<span class="hljs-variable">$7</span>.document<span class="hljs-comment">;</span>
    var <span class="hljs-attr">fetchImpl</span> = global<span class="hljs-variable">$7</span>.fetch<span class="hljs-comment">;</span>
    // 如果被覆写，借助 iframe 获取原生的 window.fetch
    if (document && typeof <span class="hljs-attr">document.createElement</span> === <span class="hljs-string">'function'</span>) &#123;
        try &#123;
            var <span class="hljs-attr">sandbox</span> = document.createElement(<span class="hljs-string">'iframe'</span>)<span class="hljs-comment">;</span>
            <span class="hljs-attr">sandbox.hidden</span> = <span class="hljs-literal">true</span><span class="hljs-comment">;</span>
            document.head.appendChild(sandbox)<span class="hljs-comment">;</span>
            var <span class="hljs-attr">contentWindow</span> = sandbox.contentWindow<span class="hljs-comment">;</span>
            if (contentWindow && contentWindow.fetch) &#123;
                <span class="hljs-attr">fetchImpl</span> = contentWindow.fetch<span class="hljs-comment">;</span>
            &#125;
            document.head.removeChild(sandbox)<span class="hljs-comment">;</span>
        &#125;
        catch (e) &#123;
            logger.warn('Could not create sandbox iframe for pure fetch check, bailing to window.fetch: ', e)<span class="hljs-comment">;</span>
        &#125;
    &#125;
    return (<span class="hljs-attr">cachedFetchImpl</span> = fetchImpl.bind(global<span class="hljs-variable">$7</span>))<span class="hljs-comment">;</span>
&#125;

// 判断 window.fetch 是否已经被覆写
function isNativeFetch(func) &#123;
    return func && /^function fetch\(\)\s+\&#123;\s+\<span class="hljs-section">[native code\]</span>\s+\&#125;$/.test(func.toString())<span class="hljs-comment">;</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于 <code>Sentry</code> 内部有一套逻辑来保证 <code>fetch</code> 必须为原生方法，所以覆写 <code>window.fetch</code> 的方案失败， <code>pass</code> ！</p>
<h4 id="user-content-2-2" data-id="heading-4">不通用的方案二</h4>
<p>既然覆写 <code>window.fetch</code> 的方案行不通，那我们就重新想办法。</p>
<p>观察上面的 <code>FetchTransport</code> 的入参。如果没有指定 <code>fetchImpl</code>，<code>Sentry</code> 会通过 <code>getNativeFetchImplementation</code> 来实现一个 <code>fetchImpl</code>。那我们主动给 <code>FetchTransport</code> 传递覆写以后的 <code>fetch</code> 方法，不就可以做到拦截 <code>fetch</code> 调用了吗？</p>
<p>这个方案看起来也很靠谱，赶紧试一下，😄。</p>
<p>从 <code>FetchTransport</code> 追本溯源，小编找到了 <code>FetchTransport</code> 方法调用的位置:</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">BrowserBackend.prototype._setupTransport = function () &#123;
    <span class="hljs-keyword">if</span> (!<span class="hljs-keyword">this</span>._options.dsn) &#123;
        <span class="hljs-keyword">return</span> _super.prototype._setupTransport.call(<span class="hljs-keyword">this</span>);
    &#125;
    <span class="hljs-keyword">var</span> transportOptions = __assign(__assign(&#123;&#125;, <span class="hljs-keyword">this</span>._options.transportOptions), &#123; dsn: <span class="hljs-keyword">this</span>._options.dsn, tunnel: <span class="hljs-keyword">this</span>._options.tunnel, sendClientReports: <span class="hljs-keyword">this</span>._options.sendClientReports, _metadata: <span class="hljs-keyword">this</span>._options._metadata &#125;);
    <span class="hljs-keyword">var</span> api = initAPIDetails(transportOptions.dsn, transportOptions._metadata, transportOptions.tunnel);
    <span class="hljs-keyword">var</span> url = getEnvelopeEndpointWithUrlEncodedAuth(api.dsn, api.tunnel);
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">this</span>._options.transport) &#123;
        <span class="hljs-keyword">return</span> new <span class="hljs-keyword">this</span>._options.transport(transportOptions);
    &#125;
    <span class="hljs-keyword">if</span> (supportsFetch()) &#123;
        <span class="hljs-keyword">var</span> requestOptions = __assign(&#123;&#125;, transportOptions.fetchParameters);
        <span class="hljs-keyword">this</span>._newTransport = makeNewFetchTransport(&#123; requestOptions: requestOptions, url: url &#125;);
        <span class="hljs-comment">// 使用 FetchTransport 的位置</span>
        <span class="hljs-keyword">return</span> new FetchTransport(transportOptions);
    &#125;
    <span class="hljs-keyword">this</span>._newTransport = makeNewXHRTransport(&#123;
        url: url,
        headers: transportOptions.headers,
    &#125;);
    <span class="hljs-keyword">return</span> new XHRTransport(transportOptions);
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的这段代码中， <code>this._options</code> 就是我们执行 <code>Sentry.init</code> 时的入参。观看 <code>FetchTransport</code> 调用的地方，由于没有 <code>fetchImpl</code> 的入参，所以 <code>Sentry</code> 会通过 <code>getNativeFetchImplementation</code> 来实现 <code>fetchImpl</code>。</p>
<p>既然这样，那我们可以在 <code>Sentry.init</code> 方法执行的时候添加一个 <code>fetchImpl</code> 入参，然后在调用 <code>FetchTransport</code> 方法时传入。</p>
<p>改造后的代码如下:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 改动 Sentry 源码</span>
<span class="hljs-title class_">BrowserBackend</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-property">_setupTransport</span> = <span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) &#123;
    ...
    <span class="hljs-keyword">if</span> (<span class="hljs-title function_">supportsFetch</span>()) &#123;
        <span class="hljs-keyword">var</span> requestOptions = <span class="hljs-title function_">__assign</span>(&#123;&#125;, transportOptions.<span class="hljs-property">fetchParameters</span>);
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">_newTransport</span> = <span class="hljs-title function_">makeNewFetchTransport</span>(&#123; <span class="hljs-attr">requestOptions</span>: requestOptions, <span class="hljs-attr">url</span>: url &#125;);
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">FetchTransport</span>(transportOptions, <span class="hljs-variable language_">this</span>.<span class="hljs-property">_options</span>.<span class="hljs-property">fetchImpl</span>);
    &#125;
    ...

&#125;

<span class="hljs-comment">// 业务代码</span>
<span class="hljs-keyword">const</span> originFetch = <span class="hljs-variable language_">window</span>.<span class="hljs-property">fetch</span>;
<span class="hljs-comment">// Sentry.init 执行</span>
<span class="hljs-title class_">Sentry</span>.<span class="hljs-title function_">init</span>(&#123;
    <span class="hljs-attr">dsn</span>: <span class="hljs-string">'xxx'</span>,
    ...
    <span class="hljs-attr">fetchImpl</span>: <span class="hljs-function">(<span class="hljs-params">url, options</span>) =></span> &#123;
        <span class="hljs-comment">// 根据 options 中的异常信息，返回新的 url 和 options</span>
        <span class="hljs-keyword">const</span> [newUrl, newOptions] = <span class="hljs-title function_">sentryFilter</span>(url, options);
        <span class="hljs-comment">// 使用原生的 fetch</span>
        <span class="hljs-keyword">return</span> <span class="hljs-title function_">originFetch</span>(newUrl, newOptions);
    &#125;
    ...
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经验证，该方案可正常工作，捕获的异常都可自动上报到对应的应用中，问题解决，happy 😄。</p>
<p>不过兴奋过后，再回过头来看看这个方案，发现其实槽点还是蛮多的:</p>
<ol>
<li>
<p>要修改 <code>Sentry</code> 源码，重新生成一个内部 <code>npm</code> 包；</p>
</li>
<li>
<p>如果 <code>Sentry</code> 版本升级，必须再次修改源码, 很不方便；</p>
</li>
</ol>
<p>总体来说，这个方案虽然能解决问题，但是不够通用，不够优雅。作为一名有追求的 👨🏻‍💻，小编当然不能仅仅止步于实现功能，还得想办法实现的更好，于是就有了接下来的方案三。</p>
<h4 id="user-content-2-3" data-id="heading-5">合理、优雅的方案三</h4>
<p>还是看上面 <code>BrowserBackend.prototype._setupTransport</code> 源码，有这样一段逻辑:</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">...
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">this</span>._options.transport) &#123;
    <span class="hljs-keyword">return</span> new <span class="hljs-keyword">this</span>._options.transport(transportOptions);
&#125;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果在 <code>Sentry.init</code> 执行时，配置了 <code>transport</code>，那么就会使用该 <code>transport</code> 方法来初始化上报异常需要的 <code>transport</code> 实例。</p>
<p>既然这样，那我们自己定义一个 <code>CustomeTransport</code> 构造函数不就可以了么。另外，小编在 <code>Sentry</code> 暴露给外面的 <code>exports</code> 中发现了 <code>FetchTransport</code>，那么 <code>CustomeTransport</code> 就可以通过继承 <code>FetchTransport</code> 来实现。</p>
<p>具体方案如下:</p>
<pre><code class="hljs language-scala copyable" lang="scala"><span class="hljs-keyword">import</span> &#123; <span class="hljs-type">Transports</span>, init &#125; from '<span class="hljs-meta">@sentry</span>/browser';
const fetchImpl = (url, options) => &#123;
    <span class="hljs-comment">// 根据 options 中的异常信息，返回新的 url 和 options</span>
    const [newUrl, newOptions] = sentryFilter(url, options);
    <span class="hljs-comment">// 使用原生的 fetch</span>
    <span class="hljs-keyword">return</span> originFetch(newUrl, newOptions);
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CustomerTransport</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Transports</span>.<span class="hljs-title">FetchTransport</span> </span>&#123;
    constructor(options) &#123;
        <span class="hljs-keyword">super</span>(options, fetchImpl)
    &#125;
&#125;

init(&#123;
    dsn: 'xxxx',
    ...
    transport: <span class="hljs-type">CustomerTransport</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经验证，该方案可正常工作，捕获的异常都可自动上报到对应的应用中，而且不用像方案二那样修改 <code>Sentry</code> 源码，优雅、通用，问题真正解决，perfect 😄。</p>
<h4 id="user-content-2-4" data-id="heading-6">7.x 版本解决方案</h4>
<p>上面的方案三只针对 <code>6.x</code> 版本。如果大家使用的 <code>Sentry</code> 是最新的 <code>7.x</code> 版本，小编也设计了相应的解决方案。</p>
<pre><code class="hljs language-ini copyable" lang="ini">import &#123; init, makeFetchTransport &#125; from '@sentry/browser'<span class="hljs-comment">;</span>

const <span class="hljs-attr">CustomeTransport</span> = (options) => &#123;
    const <span class="hljs-attr">fetchImpl</span> = (url, options) => &#123;
        const <span class="hljs-section">[newUrl, newOptions]</span> = sentryFilter(url, options)<span class="hljs-comment">;</span>
        return window.fetch(newUrl, newOptions)<span class="hljs-comment">;</span>
    &#125;<span class="hljs-comment">;</span>
    return makeFetchTransport(options, fetchImpl)<span class="hljs-comment">;</span>
&#125;<span class="hljs-comment">;</span>

init(&#123;
    dsn: 'https://525053cc037e42bcb981670e97a0a821@sentry.byai.com/52',
    ...
    transport: CustomeTransport,
&#125;)<span class="hljs-comment">;</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>亲测可用哦！</p>
<h3 id="user-content-3" data-id="heading-7">结束语</h3>
<p>也许有小伙伴会问，如果浏览器不支持 <code>fetch</code> 的话，那上面说的方案不就没有用了吗？</p>
<p>其实大可不必担心这一点。</p>
<p>首先，当前主流浏览器，除了比较老的版本，已经实现了对 <code>fetch</code> 的支持。如果有些小伙伴的浏览器实在不支持 <code>fetch</code>，那也没有关系。由于 <code>Sentry</code> 内部没有要求 <code>xhr</code> 必须使用原生的 <code>send</code> 方法，所以我们可以通过覆写 <code>XMLHttpRequest</code> 原型链上的 <code>send</code> 方法来实现对异常上报的拦截，具体的实现过程就由小伙伴们自行研究了，哈哈。</p>
<p>最后再啰嗦一句，如果本文对大家有帮助，那就给小编点个 👍 吧。 大家的支持，是小编继续前进的动力, 😄。</p></div>  
</div>
            