
---
title: '大型 SPA 项目架构设计与重构'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d52b837d6c0458b9e1be5c054b2fff6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 22:11:36 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d52b837d6c0458b9e1be5c054b2fff6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">大型 SPA 项目架构设计与重构</h1>
<blockquote>
<p>本文主要为分享我司 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fconsole.ucloud.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://console.ucloud.cn/" ref="nofollow noopener noreferrer">控制台</a> 最近两年的架构演进，遇到的问题和解决方案等。控制台项目包含近百个不同产品，跨部门、跨地域协作开发，是一个比较典型的大型 SPA 前端项目。</p>
</blockquote>
<p>先说下为何要做架构重构，老架构以及老架构下的一些问题。</p>
<h2 data-id="heading-1">老架构介绍</h2>
<p>控制台老架构底层为 <code>angular@1</code>，使用 <code>angular</code> 的 <code>ui-router</code> 和 <code>lazy-load</code> 来进行项目的按需加载运行。大部分项目通过 <code>angular</code> 挂载 <code>react</code> 实例，虽然很多业务代码和 <code>angular</code> 无关，但是依然有很多地方（如 services、路由等）依赖 <code>angular</code>。</p>
<h3 data-id="heading-2">老架构存在的问题</h3>
<p>老架构存在的问题主要分为两部分，运行时问题和开发时问题：</p>
<h4 data-id="heading-3">运行时问题</h4>
<h5 data-id="heading-4">老架构严重依赖 angular</h5>
<p>由于当初整套架构设计基于 <code>angular</code> 的能力，导致启动器体量大、加载慢、性能差。</p>
<h5 data-id="heading-5">老架构下的依赖体量重</h5>
<p>老架构下公共部分主要分为 <code>common</code> 和 <code>components</code>，里面存在大量的历史遗留、冗余、无效代码，历史包袱重，而且依赖混乱，无法安全清理。</p>
<h5 data-id="heading-6">耦合严重</h5>
<p>老架构下的项目，虽然大部分项目代码已经都是 <code>react</code> 代码，但是有一些 <code>services</code> 依然依赖 <code>angular</code>。启动器、公共依赖、项目间的代码耦合严重。</p>
<h5 data-id="heading-7">性能问题</h5>
<p>启动器重、依赖重、语言文件混合导致过大、初始化内容过多等各种问题导致项目加载慢、执行慢。</p>
<h4 data-id="heading-8">开发时问题</h4>
<h5 data-id="heading-9">使用麻烦、风险高</h5>
<p>老架构的项目结构为一个主项目和 N 个子项目，主项目中包含着开发脚本、开发依赖，其它的项目如依赖、启动器、项目均作为子模块（<code>git submodule</code>）管理。</p>
<p>开发时需要检查主仓库更新，检查依赖更新，执行开发脚本，还需注意启动器项目的版本、冲突、依赖更新等，使用成本高。</p>
<h5 data-id="heading-10">升级成本高</h5>
<p>开发环境无法安全升级，由于所以依赖、脚本都是全项目共享，升级会直接影响到上百个子项目，导致不能随意变动。</p>
<h2 data-id="heading-11">新架构</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d52b837d6c0458b9e1be5c054b2fff6~tplv-k3u1fbpfcp-watermark.image" alt="架构图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>控制台项目分三层，启动器、公共模块、业务模块。</p>
<h3 data-id="heading-12">启动器</h3>
<p>启动的承载着网站最基本的功能，包括：</p>
<ul>
<li>骨架屏</li>
<li>浏览器兼容处理 - 不兼容版本提示</li>
<li>项目路由管理（<code>router-service</code>） - 跨项目跳转</li>
<li>项目加载/挂载/卸载（微前端 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frapiop%2Frapiop" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/rapiop/rapiop" ref="nofollow noopener noreferrer">rapiop</a>）</li>
<li>模块管理器（<a href="https://link.juejin.cn/?target=https%3A%2F%2Frapiop.github.io%2Fmod%2F%23%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://rapiop.github.io/mod/#/" ref="nofollow noopener noreferrer">mod</a>）</li>
<li>主题 - 主题加载/切换</li>
<li>基础依赖 - <code>babel polyfill</code>、<code>reset-style</code></li>
<li><code>sentry</code> - 错误上报</li>
<li><code>matomo</code> - 用户行为分析、数据上报</li>
<li>其它的一些内部服务等</li>
</ul>
<h3 data-id="heading-13">公共模块</h3>
<h4 data-id="heading-14">services</h4>
<p><code>services</code> 为内部的一些公共服务。</p>
<ul>
<li><code>user</code> - 用户信息</li>
<li><code>intl</code> - 语言翻译</li>
<li><code>das</code> - 数据上报</li>
<li><code>region</code>、<code>project</code> 等</li>
</ul>
<h4 data-id="heading-15">libs</h4>
<p><code>libs</code> 用于输出一些常用的公共模块、开源库。</p>
<ul>
<li><code>react</code>、<code>react-dom</code>、<code>react-router</code> - <code>react</code> 相关库</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fucloud-fe.github.io%2Freact-components%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://ucloud-fe.github.io/react-components/" ref="nofollow noopener noreferrer">components</a> - 公共组件库</li>
<li><code>apexcharts</code>、<code>react-apexcharts</code> - 图标库</li>
<li><code>lodash</code> 等工具库</li>
</ul>
<h4 data-id="heading-16">components</h4>
<p><code>components</code> 包括控制台相关的一些业务组件</p>
<ul>
<li><code>common-components</code> - 常用的业务组件、布局、路由组件等</li>
<li><code>umon-components</code> - 监控相关组件</li>
<li><code>code-components</code> - 代码编辑器组件</li>
<li><code>ulog-components</code>、<code>pay-components</code> 等</li>
</ul>
<h4 data-id="heading-17">其它模块</h4>
<ul>
<li><code>sidebar</code>、<code>navbar</code> - 公共部分的 UI</li>
<li><code>styles</code> - 通用的样式</li>
<li><code>react-adapter</code> - 项目适配器，减少样板代码（注册微前端、初始化语言、依赖加载等）</li>
</ul>
<h3 data-id="heading-18">业务模块</h3>
<p>业务模块主要为各业务项目，分为老项目、新项目。</p>
<h3 data-id="heading-19">优化后</h3>
<ul>
<li>轻量无依赖启动器</li>
<li>职责明确</li>
<li>模块拆分、<a href="https://link.juejin.cn/?target=https%3A%2F%2Frapiop.github.io%2Fmod%2F%23%2Fbackground%3Fid%3D%25e6%25a8%25a1%25e5%259d%2597%25e7%259a%2584%25e8%2587%25aa%25e6%2588%2591%25e7%25ae%25a1%25e7%2590%2586" target="_blank" rel="nofollow noopener noreferrer" title="https://rapiop.github.io/mod/#/background?id=%e6%a8%a1%e5%9d%97%e7%9a%84%e8%87%aa%e6%88%91%e7%ae%a1%e7%90%86" ref="nofollow noopener noreferrer">自治</a>、依赖明确</li>
<li>无耦合</li>
</ul>
<h3 data-id="heading-20">运行流程</h3>
<p>进入页面：</p>
<ul>
<li>浏览器兼容检测，<code>polyfill</code>、基本依赖加载</li>
<li><code>reset</code> 样式加载，主题、<code>matomo</code>、<code>sentry</code> 初始化</li>
<li>灰度信息获取，未登陆则跳回登陆</li>
<li>使用灰度信息初始化微前端、模块管理器</li>
<li>根据当前 <code>url</code> 匹配项目，如果为老项目则加载老启动器，进入老项目加载流程，新项目直接加载项目、依赖</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54741111507b443c819d5ebb20b0446b~tplv-k3u1fbpfcp-watermark.image" alt="流程图" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-21">开发</h3>
<p>开发环境拆分为两部分：<code>CLI</code> 和 <code>dev-dependences</code>。</p>
<h4 data-id="heading-22">CLI</h4>
<p>提供 <code>CLI</code> 工具，提供开发、构建、打包分析、<code>codemod</code>、依赖管理等功能。</p>
<h4 data-id="heading-23">dev-dependences</h4>
<p>包含了项目的开发依赖：<code>webpack</code>、<code>eslint</code>、<code>loaders</code> 等，存在多版本，可方便后续的升级迭代，降低升级成本和风险。</p>
<p>提供依赖对应的功能脚本：开发、构建等。</p>
<h4 data-id="heading-24">开发启动</h4>
<p>通过 <code>CLI</code> 启动开发命令，会根据命令启动启动器（线上/预发步/本地），启动指定项目中的开发依赖中的开发脚本并通信，合并线上灰度信息和本地文件信息。</p>
<h4 data-id="heading-25">优势</h4>
<ul>
<li>升级维护安全</li>
<li>使用方便</li>
</ul>
<h2 data-id="heading-26">现状</h2>
<p>目前处于新架构老架构共存的状态，大部分的老项目在逐渐替换旧的 services 等，进行平滑升级。</p></div>  
</div>
            