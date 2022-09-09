
---
title: 'AbpVnext 框架解读系列（一）_ 模块化'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0ccaec551674544a2fe608c9b55b5ee~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 01:20:02 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0ccaec551674544a2fe608c9b55b5ee~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:var(--cyanosis-base-color);transition:color .35s;--cyanosis-base-color:#353535;--cyanosis-title-color:#005bb7;--cyanosis-strong-color:#2196f3;--cyanosis-em-color:#4fc3f7;--cyanosis-del-color:#ccc;--cyanosis-link-color:#3da8f5;--cyanosis-linkh-color:#007fff;--cyanosis-border-color:#bedcff;--cyanosis-border-color-2:#ececec;--cyanosis-bg-color:#fff;--cyanosis-blockquote-color:#8c8c8c;--cyanosis-blockquote-bg-color:#f0fdff;--cyanosis-code-color:#c2185b;--cyanosis-code-bg-color:#fff4f4;--cyanosis-code-pre-color:#f8f8f8;--cyanosis-table-border-color:#c3e0fd;--cyanosis-table-th-color:#dff0ff;--cyanosis-table-tht-color:#005bb7;--cyanosis-table-tr-nc-color:#f7fbff;--cyanosis-table-trh-color:#e0edf7;--cyanosis-slct-title-color:#005bb7;--cyanosis-slct-titlebg-color:rgba(175,207,247,0.25);--cyanosis-slct-text-color:#c80000;--cyanosis-slct-bg-color:rgba(175,207,247,0.25);--cyanosis-slct-del-color:#999;--cyanosis-slct-elbg-color:#e8ebec;--cyanosis-slct-codebg-color:#ffeaeb;--cyanosis-slct-prebg-color:rgba(160,200,255,0.25)&#125;.markdown-body.__dark&#123;--cyanosis-base-color:#cacaca;--cyanosis-title-color:#ddd;--cyanosis-strong-color:#fe9900;--cyanosis-em-color:#ffd28e;--cyanosis-del-color:#ccc;--cyanosis-link-color:#ffb648;--cyanosis-linkh-color:#fe9900;--cyanosis-border-color:#ffe3ba;--cyanosis-border-color-2:#ffcb7b;--cyanosis-bg-color:#2f2f2f;--cyanosis-blockquote-color:#c7c7c7;--cyanosis-blockquote-bg-color:rgba(255,199,116,0.1);--cyanosis-code-color:#000;--cyanosis-code-bg-color:#ffcb7b;--cyanosis-code-pre-color:rgba(255,227,185,0.5);--cyanosis-table-border-color:#fe9900;--cyanosis-table-th-color:#ffb648;--cyanosis-table-tht-color:#000;--cyanosis-table-tr-nc-color:#6d5736;--cyanosis-table-trh-color:#947443;--cyanosis-slct-title-color:#000;--cyanosis-slct-titlebg-color:#fe9900;--cyanosis-slct-text-color:#00c888;--cyanosis-slct-bg-color:rgba(175,207,247,0.25);--cyanosis-slct-del-color:#999;--cyanosis-slct-elbg-color:#000;--cyanosis-slct-codebg-color:#ffcb7b;--cyanosis-slct-prebg-color:rgba(160,200,255,0.25)&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:var(--cyanosis-title-color);transition:color .35s&#125;.markdown-body h2&#123;position:relative;padding-left:10px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid var(--cyanosis-border-color-2)&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-14px&#125;.markdown-body h2:after&#123;content:"」";position:relative;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:var(--cyanosis-strong-color)&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,var(--cyanosis-link-color),rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),var(--cyanosis-link-color));border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background-color:var(--cyanosis-bg-color);background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center;transition:background-color .5s&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:var(--cyanosis-code-color);word-break:break-word;overflow-x:auto;background-color:var(--cyanosis-code-bg-color);border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:var(--cyanosis-code-pre-color)&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:var(--cyanosis-border-color)&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:var(--cyanosis-strong-color);border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:var(--cyanosis-link-color);border-bottom:1px solid var(--cyanosis-border-color)&#125;.markdown-body a:hover&#123;border-bottom-color:var(--cyanosis-linkh-color)&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:var(--cyanosis-linkh-color)&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid var(--cyanosis-border-color);transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:var(--cyanosis-linkh-color)&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid var(--cyanosis-table-border-color);border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:var(--cyanosis-table-tr-nc-color)&#125;.markdown-body table tr:hover&#123;background-color:var(--cyanosis-table-trh-color)&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid var(--cyanosis-table-border-color)&#125;.markdown-body table th&#123;color:var(--cyanosis-table-tht-color);background-color:var(--cyanosis-table-th-color)&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:var(--cyanosis-blockquote-color);border-left:4px solid var(--cyanosis-strong-color);background-color:var(--cyanosis-blockquote-bg-color);padding:1px 20px;margin:22px 0;transition:color .35s&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:var(--cyanosis-strong-color)&#125;.markdown-body em,.markdown-body i&#123;color:var(--cyanosis-em-color)&#125;.markdown-body del&#123;color:var(--cyanosis-del-color)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:var(--cyanosis-title-color);font-size:20px;font-weight:bolder;border-bottom:1px solid var(--cyanosis-border-color);cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:var(--cyanosis-blockquote-bg-color);border:2px dashed var(--cyanosis-strong-color)&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:var(--cyanosis-slct-title-color);background-color:var(--cyanosis-slct-titlebg-color)&#125;.markdown-body ol li::selection,.markdown-body p::selection,.markdown-body ul li::selection&#123;color:var(--cyanosis-slct-text-color);background-color:var(--cyanosis-slct-bg-color)&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:var(--cyanosis-slct-elbg-color)&#125;.markdown-body del::selection&#123;color:var(--cyanosis-slct-del-color);background-color:var(--cyanosis-slct-elbg-color)&#125;.markdown-body table thead th::selection&#123;background-color:transparent&#125;.markdown-body table tbody td::selection&#123;background-color:var(--cyanosis-slct-bg-color)&#125;.markdown-body code::selection&#123;background-color:var(--cyanosis-slct-codebg-color)&#125;.markdown-body pre>code::selection&#123;background-color:var(--cyanosis-slct-prebg-color)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>谁适合阅读本文 ❓</p>
<ul>
<li>想使用ABP框架进行开发的同学⭐</li>
<li>对ABP框架感兴趣的同学⭐</li>
<li>已经使用了ABP框架开发，想了解其中的一些原理或者设计⭐</li>
<li>一起学习新知识⭐</li>
</ul>
</blockquote>
<p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第6篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a></p>
<h1 data-id="heading-0">前言</h1>
<blockquote>
<p>使用过的同学应该都知道，ABP是一个模块一个单独的解决方案，整个模块的设计都遵循了领域驱动设计！每个模块都应该定义一个模块类，定义模块类的最简单方法是创建一个派生自<code>AbpModule</code>，ABP的整个分层模块如下图！</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0ccaec551674544a2fe608c9b55b5ee~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">AbpModule详解</h2>
<blockquote>
<p>为什么要设计成模块化，使用模块化又能为系统带来什么？模块化作为ABP框架的核心，它是怎么实现的？</p>
</blockquote>
<h3 data-id="heading-2">模块化的意义</h3>
<ul>
<li>模块化开发的意义我觉得在于<code>高内聚，低耦合</code>，模块与模块之间相互独立，但又可以自由组合，能使系统灵活性非常强，提高了代码的可维护性，复用性。</li>
</ul>
<h3 data-id="heading-3">ABP模块化详解</h3>
<blockquote>
<p>模块的初始化动作是在 <code>AbpApplicationBase</code> 基类开始的，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fabpframework%2Fabp%2Fblob%2Fdev%2Fframework%2Fsrc%2FVolo.Abp.Core%2FVolo%2FAbp%2FAbpApplicationBase.cs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/abpframework/abp/blob/dev/framework/src/Volo.Abp.Core/Volo/Abp/AbpApplicationBase.cs" ref="nofollow noopener noreferrer">源码地址</a>。主要是注入模块相关的基础设施，还包括了<code>LoadModules()</code>方法，以及遍历所有模块，并按照预加载、初始化、初始化完成的顺序执行其生命周期方法</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1114d802da5a41fc8a040187e567e971~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">virtual</span> <span class="hljs-title">IReadOnlyList</span><<span class="hljs-title">IAbpModuleDescriptor</span>> <span class="hljs-title">LoadModules</span>(<span class="hljs-params">IServiceCollection services, AbpApplicationCreationOptions options</span>)</span>
&#123;
    <span class="hljs-keyword">return</span> services
        .GetSingletonInstance<IModuleLoader>()
        .LoadModules(
            services,
            StartupModuleType,
            options.PlugInSources
        );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>模块的初始化在<code>IModuleLoader</code> 的默认实现 <code>ModuleLoader</code> 主要做了哪些事情呢？
<ul>
<li>参数校验</li>
<li>查找所有的模块类型，并创建模块描述。主要是通过<code>AbpModuleHelper.FindAllModuleTypes()</code>方法</li>
<li>解析依赖关系，对列表进行拓扑排序。</li>
</ul>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ceaaa881badb4da281112cb5f307f912~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1950bec7db3a4a69b96a988db71ea78a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>执行完上述操作之后我们可以看到<code>AbpApplicationBase</code>类的最后一个操作执行模块的三个生命周期方法，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fabpframework%2Fabp%2Fblob%2Ff68670a94e%2Fframework%2Fsrc%2FVolo.Abp.Core%2FVolo%2FAbp%2FAbpApplicationBase.cs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/abpframework/abp/blob/f68670a94e/framework/src/Volo.Abp.Core/Volo/Abp/AbpApplicationBase.cs" ref="nofollow noopener noreferrer">源码地址</a></li>
</ul>
<pre><code class="hljs language-scss copyable" lang="scss">if (!options.SkipConfigureServices)
&#123;
    <span class="hljs-built_in">ConfigureServices</span>();<span class="hljs-comment">//执行模块的三个生命周期方法</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>AbpModule</code>提供一些方法来管理模块的生命周期
<ul>
<li>ConfigureServices将你的服务添加到依赖注入系统并配置其他模块的主要方法</li>
<li>OnApplicationInitialization初始化所有模块</li>
<li>OnApplicationShutdown应用关闭执行</li>
<li>. . . 还有一些如配置前后执行方法、初始化前后执行方法等等</li>
</ul>
</li>
</ul>
<h3 data-id="heading-4">模块的两种类型</h3>
<ul>
<li><strong>框架模块</strong>:如缓存, 邮件, 主题, 安全, 序列化, 验证... 等. 它们没有应用/业务功能,它们提供了日常开发经常用到的通用基础设施,集成和抽象.</li>
<li><strong>应用程序模块</strong>: 这些模块实现了 <strong>特定的应用/业务功能</strong> 像博客, 文档管理, 身份管理, 租户管理... 等等. 它们通常有自己的实体,服务,API和UI组件. 请参阅 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.abp.io%2Fzh-Hans%2Fabp%2Flatest%2FModules%2FIndex" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.abp.io/zh-Hans/abp/latest/Modules/Index" ref="nofollow noopener noreferrer">预构建的应用程序模块</a>.</li>
</ul>
<h3 data-id="heading-5">如何使用自定义模块</h3>
<blockquote>
<p>既然我们上文中提到，模块之间可以灵活组合配置，那么我们在应用程序中如何使用呢？<br>
只需要声明 <strong>[DependsOn]</strong> 特性，ABP在启动时会调查应用程序的依赖关系,并以正确的顺序初始化/关闭模块</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59269efceb6e4683904684e8be273352~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">总结</h1>
<blockquote>
<p>第一次读ABP源码，读了好几天，也看了不少文章，但是总感觉有一些似懂非懂的感觉。本文如果有一些补充不够的可以指出来，我会虚心学习。<br>
Abp vNext的模块化设计，提供了高扩展性、高可用性、高效率开发框架。要实现高效率前提还需要熟练了解使用 Abp中的所有模块功能。</p>
</blockquote></div>  
</div>
            