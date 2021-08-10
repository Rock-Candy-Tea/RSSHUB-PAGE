
---
title: '玩转 Github Profile Readme：开发 Leetcode 统计卡片'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/058fe55a700b47aca0f68ff67df3053c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 07:59:54 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/058fe55a700b47aca0f68ff67df3053c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>前文<a href="https://juejin.cn/post/6992604456953053198" target="_blank" title="https://juejin.cn/post/6992604456953053198">使用篇</a>里梳理了 Github Profile Readme 的现有玩法。还在文末留下不长的 “创作” 清单，那么今天就操练起来吧，回顾一下预定的工作目标：</p>
<ul>
<li>在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fanuraghazra%2Fgithub-readme-stats" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/anuraghazra/github-readme-stats" ref="nofollow noopener noreferrer">github-readme-stats</a> 项目的基础上实现一个 Leetcode 统计卡片</li>
<li>尝试搭建一个更易扩展的 SVG 生成系统，探索能否直接应用已有的图表组件。</li>
<li>造一个 Profile Readme 可视化生成器</li>
</ul>
<p>实际工作量比我预计的要大，只好分多天完成了。这一篇文章记录实现 LeetCode 统计卡片的过程。</p>
<p><strong>开发目标</strong>：在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fanuraghazra%2Fgithub-readme-stats" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/anuraghazra/github-readme-stats" ref="nofollow noopener noreferrer">github-readme-stats</a> 项目上实现一个 leetcode 统计卡片</p>
<p><strong>涉及技术</strong>：GraphQL、TypeScript、SVG 编程</p>
<h1 data-id="heading-0">创建文件</h1>
<p>github-readme-stats 依托 vercel 运行，内部核心逻辑其实非常简单：请求触发 serverless function -> fetcher 获取数据 -> card 负责数据处理和 svg 构建。</p>
<p>项目中的几张卡片几乎都是复制粘贴的重复代码，先不考虑优化，照猫画虎复制出 api、fetcher、card 三份文件。</p>
<h1 data-id="heading-1">请求 Leetcode 数据</h1>
<p>Leetcode 没有开放 API，只能通过调试工具慢慢找请求接口。选一个数据充足的用户页，比如 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fleetcode-cn.com%2Fu%2Fint65536%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://leetcode-cn.com/u/int65536/" ref="nofollow noopener noreferrer">leetcode-cn.com/u/int65536/</a> ，刷新，在 Network 面板里一个个排查。Leetcode 用了 GraphQL 查询数据，筛选 <code>graphql</code> 路径缩小范围，仔细看看，不一会儿就能确定每个请求的用途。</p>
<p>我也要用 GraphQL 组装数据。那么问题来了：怎么复制 Request Payload？有没有类似 Postman 的 API 调试工具？</p>
<h2 data-id="heading-2">复制 Request Payload</h2>
<p>Chrome Devtool 里用快捷键复制 Request Payload 得到的是大段字符串，真正的获取方法是 「单击选中复制目标，右键选择 Copy value」。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/058fe55a700b47aca0f68ff67df3053c~tplv-k3u1fbpfcp-watermark.image" alt="Screen Shot 2021-08-05 at 10.47.02 AM.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">GraphQL 调试工具</h2>
<p>下载一个 GraphiQL 客户端 - <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.electronjs.org%2Fapps%2Fgraphiql" target="_blank" rel="nofollow noopener noreferrer" title="https://www.electronjs.org/apps/graphiql" ref="nofollow noopener noreferrer">GraphiQL | Apps | Electron (electronjs.org)</a>，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fskevy%2Fgraphiql-app" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/skevy/graphiql-app" ref="nofollow noopener noreferrer">graphiql-app</a> 是多年前的一个开源项目，有些小 Bug 但暂时够用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d911067c3df94e05ab369ec6e13a95d1~tplv-k3u1fbpfcp-watermark.image" alt="Screen Shot 2021-08-05 at 10.57.31 AM.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Leetcode 的国内和国际站点用了两套完全不同的请求，schema 结构也完全不同。只能做两套逻辑，处理后返回统一的数据结构。没有 TypeScript 和 ESLint 辅助，写起代码来确实低效，在编码阶段很难预知错误。只能通过运行 -> 检查错误信息 -> Debug 的方式排查。</p>
<h2 data-id="heading-4">Vercel Debug</h2>
<p>重复代码 + 没有语法检查 + 没有类型检查。如果没有 Debugger，只靠 console，那这开发简直是太难受了。</p>
<p>Vercel 本地开发环境通过 <code>vercel dev</code> 跑起，在 VSCode 中启动 Node.js 有好几种方式：</p>
<ol>
<li>开启 Auto Attach</li>
<li>使用 JavaScript Debug Terminal 在指定终端窗口执行 <code>vercel dev</code></li>
<li>配一个简单的 launch.json</li>
</ol>
<p>我期望能在这个项目中运行 <code>vercel dev</code> 时启动调试。于是只为这个工作区配了 Auto Attach</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// 设置 .vscode/settings.json</span>
&#123;
    <span class="hljs-attr">"debug.javascript.autoAttachFilter"</span>: <span class="hljs-string">"smart"</span>, <span class="hljs-comment">// 能匹配上 AttachSmartPattern 的命令行脚本自动启动调试器</span>
    <span class="hljs-attr">"debug.javascript.autoAttachSmartPattern"</span>: [ <span class="hljs-comment">// 指定 AttachSmartPattern </span>
        <span class="hljs-string">"**/vercel/**"</span>
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果有兴趣全面了解 VSCode 中启动 Node.js 调试，可以看这篇 <a href="https://juejin.cn/post/6992976045213220878/" target="_blank" title="https://juejin.cn/post/6992976045213220878/">VSCode 启动 Node.js 调试的几种方式 (juejin.cn)</a></p>
<h1 data-id="heading-5">重构代码</h1>
<p>解决完这一部分，发现目前的开发辅助和代码结构实在不行，效率太低并且可能有未发现的错误。我忍不了了，于是决定重构。</p>
<h2 data-id="heading-6">TypeScript</h2>
<p>由于对 TS 的掌握还不全面，更别说熟练应用了。可以说是一个新手一边实践一边躺坑的过程，躺坑的过程有点狼狈，但也是一种学习方法。</p>
<h3 data-id="heading-7">支持 TypeScript</h3>
<p>先看看 Vercel 对 TypeScript 的支持情况：</p>
<blockquote>
<p>Deploying a Node.js function with the <code>.ts</code> extension will automatically be recognized as a <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/" ref="nofollow noopener noreferrer">TypeScript</a> file and compiled to a Serverless Function.</p>
<p>You can also define a <code>tsconfig.json</code> to configure the Vercel TypeScript compiler.</p>
</blockquote>
<p>Vercel 内置 TypeScript 编译支持，能保证 TS 代码正常工作。同时，<code>tsconfig.json</code> 对 Vercel TypeScript 编译器有效。</p>
<p>TS 的支持一部分是编译支持，另一部分是 IDE 辅助（错误提醒、编码建议和修正、智能补全、跳转等等）。我所好奇的是没有 <code>tsconfig.json</code>，VSCode TypeScript 语言服务是怎么和 Vercel 默认的 TS 配置保持同步的呢？</p>
<h3 data-id="heading-8">TypeScript 中的模块</h3>
<blockquote>
<p>Error Message: Cannot redeclare block-scoped variable 'encodeHTML'.</p>
</blockquote>
<blockquote>
<p>Quick Fixes: Convert to ES6 module</p>
</blockquote>
<h3 data-id="heading-9">enum 和键值对如何选择？</h3>
<h3 data-id="heading-10">面向对象编程</h3>
<h3 data-id="heading-11">泛型</h3>
<h1 data-id="heading-12">References</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvercel.com%2Fdocs%2Fserverless-functions%2Fsupported-languages%3Fquery%3Dtypescript%23using-typescript" target="_blank" rel="nofollow noopener noreferrer" title="https://vercel.com/docs/serverless-functions/supported-languages?query=typescript#using-typescript" ref="nofollow noopener noreferrer">Vercel – Supported Languages for Serverless Functions - Vercel Documentation</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcode.visualstudio.com%2Fdocs%2Ftypescript%2Ftypescript-tutorial" target="_blank" rel="nofollow noopener noreferrer" title="https://code.visualstudio.com/docs/typescript/typescript-tutorial" ref="nofollow noopener noreferrer">TypeScript tutorial with Visual Studio Code</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcode.visualstudio.com%2FDocs%2Flanguages%2Ftypescript" target="_blank" rel="nofollow noopener noreferrer" title="https://code.visualstudio.com/Docs/languages/typescript" ref="nofollow noopener noreferrer">TypeScript Programming with Visual Studio Code</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Ftsconfig-json.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/tsconfig-json.html" ref="nofollow noopener noreferrer">TypeScript: Documentation - What is a tsconfig.json (typescriptlang.org)</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Ftsconfig" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/tsconfig" ref="nofollow noopener noreferrer">TypeScript: TSConfig Reference - Docs on every TSConfig option (typescriptlang.org)</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Fmodules.html%23export--and-import--require" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/modules.html#export--and-import--require" ref="nofollow noopener noreferrer">TypeScript: Documentation - Modules (typescriptlang.org)</a></p></div>  
</div>
            