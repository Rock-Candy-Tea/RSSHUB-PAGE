
---
title: '如何实现一款支持浏览器和 Node.js 的通用 SDK'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77d0e3d081b247d7a9fc7b75b85a6dba~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 16:57:12 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77d0e3d081b247d7a9fc7b75b85a6dba~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;color:rgba(46,36,36,.87);overflow-x:hidden&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;margin-bottom:5px;font-size:30px;font-weight:500&#125;.markdown-body h1:before&#123;content:"#";margin-right:10px;color:#1976d2&#125;.markdown-body h2&#123;font-size:28px;font-weight:400;border-left:5px solid #454545;margin-top:20px;padding-left:10px;transition:all .3s ease-in-out&#125;.markdown-body h2:hover&#123;border-color:#1976d2&#125;.markdown-body h3&#123;font-size:24px;font-weight:400;margin-top:15px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:20px;font-weight:500&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body h2:first-letter,.markdown-body h3:first-letter,.markdown-body p:first-letter&#123;text-transform:capitalize&#125;.markdown-body em&#123;text-emphasis:dot;text-emphasis-position:under&#125;.markdown-body img&#123;display:block;margin:0 auto!important;max-width:100%;border-radius:2px;box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)!important&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#ddd,#999,#ddd);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;font-weight:900;word-break:break-word;border-radius:2px;overflow-x:auto;font-size:.87em;padding:.065em .4em;background-color:#fbe5e1;color:#c0341d&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:0 4px&#125;.markdown-body pre>code&#123;font-weight:400;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;margin:0 4px;text-decoration:none;color:#027fff;transition:all .3s ease-in-out;padding-bottom:4px;border-bottom:2px solid transparent&#125;.markdown-body a:after&#123;content:"";display:inline-block;width:18px;height:18px;margin-left:4px;vertical-align:middle;background-image:url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMiIgaGVpZ2h0PSIyMiI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIiBzdHJva2U9IiMwMjdGRkYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PHBhdGggZD0iTTkuODE1IDYuNDQ4bDEuOTM2LTEuOTM2YzEuMzM3LTEuMzM2IDMuNTgtMS4yNTkgNS4wMTMuMTczIDEuNDMyIDEuNDMyIDEuNTEgMy42NzYuMTczIDUuMDEzbC0xLjQ1MiAxLjQ1Mi0uOTY4Ljk2OGMtMS4zMzcgMS4zMzYtMy41ODEgMS4yNTktNS4wMTMtLjE3MyIvPjxwYXRoIGQ9Ik0xMS4yNjcgMTUuMzY3bC0xLjkzNiAxLjkzNmMtMS4zMzYgMS4zMzctMy41OCAxLjI2LTUuMDEyLS4xNzMtMS40MzItMS40MzItMS41MS0zLjY3Ni0uMTczLTUuMDEybDEuNDUyLTEuNDUyLjk2OC0uOTY4YzEuMzM2LTEuMzM3IDMuNTgtMS4yNiA1LjAxMi4xNzMiLz48L2c+PC9zdmc+);background-size:cover;background-repeat:no-repeat&#125;.markdown-body a:hover&#123;border-color:#027fff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body a.footnote-backref:after,.markdown-body a.footnote-ref:after,.markdown-body sup a:after&#123;display:none!important&#125;.markdown-body table&#123;margin:0 auto 10px;font-size:12px;width:auto;max-width:100%;overflow:auto;border:2px solid #c6c6c6&#125;.markdown-body table img&#123;box-shadow:none!important&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body del&#123;color:rgba(0,0,0,.6)&#125;.markdown-body blockquote&#123;position:relative;color:#666;padding:5px 23px 1px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:hsla(0,0%,78.4%,.12);transition:all .2s ease-in-out&#125;.markdown-body blockquote:hover&#123;border-color:#1976d2&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;font-size:24px;font-weight:800;line-height:24px;color:#cbcbcb;opacity:.6&#125;.markdown-body blockquote:before&#123;content:"“";top:4px;left:6px&#125;.markdown-body blockquote:after&#123;content:"”";right:8px;bottom:-8px&#125;.markdown-body blockquote>p,.markdown-body blockquote blockquote&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #1976d2;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary:hover::-webkit-details-marker&#123;color:#1976d2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">TL;DR</h1>
<p>本文对应的 SDK 项目仓库为 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx" ref="nofollow noopener noreferrer">universal-sdk-by-tsdx</a>。</p>
<p>本文主要记录实现一款通用 SDK 时遇到的问题，以及解决方案，如果你需要快速创建一个 SDK，那么你可以复制该项目建立你自己的 SDK，并在遇到问题的时候再回头阅读本文。</p>
<p>如果你更愿意通过阅读代码的方式了解实现原理，那么克隆该项目并阅读源码将非常适合你。在该项目中执行 <code>git log</code>，将展示详细的实践步骤，这对理解该 SDK 的迭代过程非常有帮助。</p>
<h1 data-id="heading-1">背景</h1>
<p>项目中需要实现一款 SDK，该 SDK 需要满足的条件有：</p>
<ol>
<li>使用 TS 语言，支持 lint 和 test。</li>
<li>支持 Node.js 端运行并且最低版本为 v10。</li>
<li>支持浏览器端运行且可以通过 browserslist 对支持的浏览器进行配置。</li>
</ol>
<h1 data-id="heading-2">选择 tsdx</h1>
<p>选择 tsdx 的原因是它能快速搭建 TS 的配置，其中包括：</p>
<ul>
<li>lint 和 test</li>
<li>prettier 格式化</li>
<li>vscode 可以友好的提示 lint 错误</li>
<li>可以直接构建出 cjs/esm/umd 格式的输出文件</li>
</ul>
<h2 data-id="heading-3">通过 tsdx 创建项目</h2>
<pre><code class="hljs language-shell copyable" lang="shell">npx tsdx create universal-sdk-by-tsdx
<span class="hljs-meta">#</span><span class="bash"> 选择 basic 即可</span>

cd universal-sdk-by-tsdx
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>创建后的项目参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2Ff0ef56d62c995279b9d67846fb598ede8930e62b" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/f0ef56d62c995279b9d67846fb598ede8930e62b" ref="nofollow noopener noreferrer">Commit</a>。</p>
</blockquote>
<p>创建完项目后，我们需要验证下需要的功能。</p>
<h2 data-id="heading-4">验证 eslint 😑</h2>
<p>当把 <code>src/index.ts</code> 中的 <code>'boop'</code> 字符串的单引号改成双引号时，vscode 并没有报错。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77d0e3d081b247d7a9fc7b75b85a6dba~tplv-k3u1fbpfcp-watermark.image" alt="no-eslint-error.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要执行 <code>yarn lint --write-file</code>，这个命令将在项目更目录生成 <code>.eslintrc.js</code> 文件。重启 vscode，将看到 eslint 提示的报错信息。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/854dca88016e4e2abd4610e19bcad0c1~tplv-k3u1fbpfcp-watermark.image" alt="eslint-error.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">验证 vscode 代码格式化 ✅</h2>
<p>将 vscode 中的代码格式化配置为 prettier 插件，格式化可以生效。因为 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fblob%2Ff0ef56d62c995279b9d67846fb598ede8930e62b%2Fpackage.json%23L28-L33" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/blob/f0ef56d62c995279b9d67846fb598ede8930e62b/package.json#L28-L33" ref="nofollow noopener noreferrer"><code>package.json#prettier</code></a> 字段定义了项目的 prettier 的配置，所以 vscode 不会使用默认的 prettier 配置。</p>
<h1 data-id="heading-6">构建产物同时支持浏览器和 Node.js</h1>
<p>SDK 同时支持浏览器和 Node.js 环境，存在以下几个问题。</p>
<ol>
<li>暴露的 API 不同。通常浏览器环境支持的 API 比 Node.js 环境少。例如 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fali-sdk%2Fali-oss%23browser-usage" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ali-sdk/ali-oss#browser-usage" ref="nofollow noopener noreferrer">OSS 在浏览器端就存在一些限制</a>。</li>
<li>浏览器端需要构建 umd 格式，以便用户直接在 <code><script /></code> 标签中使用。</li>
<li>根据运行环境执行不同的代码逻辑。例如，希望在浏览环境使用该 SDK 时，在控制台中打印 <code>Hello World</code>，但是在 Node.js 环境不打印。</li>
<li>Native 能力不同。假设该 SDK 需要依赖 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2Fapi%2Fcrypto.html" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/api/crypto.html" ref="nofollow noopener noreferrer">crypto</a> 做加解密。在浏览器环境，由于浏览器没有提供 crypto 的能力，所以需要依赖三方包实现，例如：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fbrowser-crypto" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/browser-crypto" ref="nofollow noopener noreferrer">browser-crypto</a>。但在 Node.js 环境，不能使用三方库，因为 Node.js 的 crypto 是通过 C++ 实现的，它的性能更高。</li>
</ol>
<p>接下来分别讨论这几个问题，并给出解决方案。</p>
<h2 data-id="heading-7">问题 1：暴露的 API 不同</h2>
<p>这个问题可以通过为浏览器环境设置不同的入口文件实现该功能。</p>
<ol>
<li>创建 <code>src/browser-index.ts</code>，其导出和 <code>src/index.ts</code> 不同，参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2Fa0b955b0aebd682fe212b78e7b27d32be27a7a7e%23diff-2e0de53017b430c0ed6e6157560df73d1e4c7059ea2aa8736fc9e8a9a97ab856R1-R6" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/a0b955b0aebd682fe212b78e7b27d32be27a7a7e#diff-2e0de53017b430c0ed6e6157560df73d1e4c7059ea2aa8736fc9e8a9a97ab856R1-R6" ref="nofollow noopener noreferrer">代码</a>。</li>
<li>在 <code>package.json</code> 中增加 <code>build:node</code> 和 <code>build:browser</code> 脚本，参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2Fa0b955b0aebd682fe212b78e7b27d32be27a7a7e%23diff-7ae45ad102eab3b6d7e7896acd08c427a9b25b346470d7bc6507b6481575d519R16-R17" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/a0b955b0aebd682fe212b78e7b27d32be27a7a7e#diff-7ae45ad102eab3b6d7e7896acd08c427a9b25b346470d7bc6507b6481575d519R16-R17" ref="nofollow noopener noreferrer">代码</a>。</li>
<li>创建 <code>tsdx.config.js</code>，如果构建目标是浏览器，则修改构建的入口文件 <code>config.input</code>，参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2Fa0b955b0aebd682fe212b78e7b27d32be27a7a7e%23diff-7eb32cb816db9aefed03469f59ccfcd4985b0a1e98fe5da291b0ec33ff7748d9R1-R16" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/a0b955b0aebd682fe212b78e7b27d32be27a7a7e#diff-7eb32cb816db9aefed03469f59ccfcd4985b0a1e98fe5da291b0ec33ff7748d9R1-R16" ref="nofollow noopener noreferrer">代码</a>。</li>
</ol>
<p>修改后，执行 <code>yarn build:browser</code> 和 <code>yarn build:node</code> 将生成不同的产物。</p>
<blockquote>
<p>解决该问题对应的修改，参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2Fa0b955b0aebd682fe212b78e7b27d32be27a7a7e%23" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/a0b955b0aebd682fe212b78e7b27d32be27a7a7e#" ref="nofollow noopener noreferrer">Commit</a>。</p>
</blockquote>
<blockquote>
<p>由于在 TypeScript 语言中，一个包只能有一个类型定义，所以不能为浏览器环境和 Node.js 环境指定不同的类型定义（参考 issue - <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMicrosoft%2FTypeScript%2Fissues%2F29128" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Microsoft/TypeScript/issues/29128" ref="nofollow noopener noreferrer">Typings for the main and browser property in package.json</a>）。</p>
</blockquote>
<h2 data-id="heading-8">问题 2：浏览器环境需构建 UMD 格式</h2>
<p>tsdx 的 format 参数可以配置构建产物的格式，修改 <code>build:browser</code> 脚本即可。</p>
<blockquote>
<p>解决该问题对应的修改，参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F58755dcc9082c88849d4b74431ae7a573ef09b40" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/58755dcc9082c88849d4b74431ae7a573ef09b40" ref="nofollow noopener noreferrer">Commit</a>。</p>
</blockquote>
<h2 data-id="heading-9">问题 3：根据运行环境执行不同的代码</h2>
<p>通常我们通过判断 <code>process.env.NODE_ENV</code> 实现在 development 和 production 环境执行不同的代码。例如，仅在在 development 环境才打印错误信息的代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (<span class="hljs-string">"development"</span> === process.env.NODE_ENV) &#123;
  <span class="hljs-built_in">console</span>.error(err)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也可以利用这种方式来区分构建产物的运行环境。基于构建时的目标环境，给 <code>process.env</code> 增加一个变量 <code>TARGET_ENVIRONMENT</code>，然后通过 <code>@rollup/plugin-replace</code> 将该变量替换为字符串常量，之后便可以通过 <code>process.env.TARGET_ENVIRONMENT</code> 区分环境了。</p>
<p>这种方式有个非常强大的优点，它将去除死代码（dead code），即 Node 环境的代码不会出现在浏览器环境的产物中。</p>
<blockquote>
<p>解决该问题对应的修改，参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F3b6d02d6f9b75c48a1e0014a3a084b21efd8f1da" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/3b6d02d6f9b75c48a1e0014a3a084b21efd8f1da" ref="nofollow noopener noreferrer">Commit</a>。</p>
</blockquote>
<h2 data-id="heading-10">问题 4：Native 能力不同</h2>
<p>这个问题比较有意思，我先把想到的解决方案列出来，然后再将他们进行对比。</p>
<h3 data-id="heading-11">方案一：rollup-plugin-node-builtins</h3>
<p>该方案使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcalvinmetcalf%2Frollup-plugin-node-builtins%23readme" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/calvinmetcalf/rollup-plugin-node-builtins#readme" ref="nofollow noopener noreferrer">rollup-plugin-node-builtins</a> 插件将 Node.js 内置的模块打包到 umd 产物中。在该方案下，如果用户使用的是 cjs 或 esm 的产物，那么 Node.js 的内置模块需要由使用方进行打包处理。通常 Webpack 可以很好的处理这些模块。</p>
<blockquote>
<p>解决该问题对应的修改，参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F62a586be840d78dfe48e3c5a4c3e1369be94f924" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/62a586be840d78dfe48e3c5a4c3e1369be94f924" ref="nofollow noopener noreferrer">Commit</a>。</p>
</blockquote>
<p>本次修改中，<code>src/browser-index.ts</code>、<code>src/index.ts</code>、<code>src/use-crypto.ts</code> 和 <code>index.html</code> 是为了测试目的而新增的。在浏览器中访问 <code>index.html</code> 文件，可以测试 umd 产物是否运行正常。</p>
<p>在 <code>tsdx.config.js</code> 文件中的修改点包括：</p>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F62a586be840d78dfe48e3c5a4c3e1369be94f924%23diff-7eb32cb816db9aefed03469f59ccfcd4985b0a1e98fe5da291b0ec33ff7748d9R47" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/62a586be840d78dfe48e3c5a4c3e1369be94f924#diff-7eb32cb816db9aefed03469f59ccfcd4985b0a1e98fe5da291b0ec33ff7748d9R47" ref="nofollow noopener noreferrer">修改 <code>config.external</code></a>。因为所有依赖都需要被打包到 umd 产物中，所以这个 <code>external</code> 需要始终为 <code>false</code>。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F62a586be840d78dfe48e3c5a4c3e1369be94f924%23diff-7eb32cb816db9aefed03469f59ccfcd4985b0a1e98fe5da291b0ec33ff7748d9R49-R50" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/62a586be840d78dfe48e3c5a4c3e1369be94f924#diff-7eb32cb816db9aefed03469f59ccfcd4985b0a1e98fe5da291b0ec33ff7748d9R49-R50" ref="nofollow noopener noreferrer">添加 globals 和 builtins 插件</a>，以便在浏览器环境可以使用 crypto 功能。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F62a586be840d78dfe48e3c5a4c3e1369be94f924%23diff-7eb32cb816db9aefed03469f59ccfcd4985b0a1e98fe5da291b0ec33ff7748d9R36-R45" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/62a586be840d78dfe48e3c5a4c3e1369be94f924#diff-7eb32cb816db9aefed03469f59ccfcd4985b0a1e98fe5da291b0ec33ff7748d9R36-R45" ref="nofollow noopener noreferrer">使用本地文件替换 safer-buffer</a>，其原因是：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FChALkeR%2Fsafer-buffer%2Fissues%2F7" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ChALkeR/safer-buffer/issues/7" ref="nofollow noopener noreferrer">这个 issue</a>。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F62a586be840d78dfe48e3c5a4c3e1369be94f924%23diff-7eb32cb816db9aefed03469f59ccfcd4985b0a1e98fe5da291b0ec33ff7748d9R51-R53" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/62a586be840d78dfe48e3c5a4c3e1369be94f924#diff-7eb32cb816db9aefed03469f59ccfcd4985b0a1e98fe5da291b0ec33ff7748d9R51-R53" ref="nofollow noopener noreferrer">使用 commonjs 转换本地的 safer-buffer</a>。tsdx 的 commonjs 插件配置只会对 node_modules 中的模块生效，当我们使用了本地的 <code>safer-buffer</code> 后，该模块不会被 commonjs 插件转换，导致报错（require is undefined）。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F62a586be840d78dfe48e3c5a4c3e1369be94f924%23diff-7eb32cb816db9aefed03469f59ccfcd4985b0a1e98fe5da291b0ec33ff7748d9R24-R33" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/62a586be840d78dfe48e3c5a4c3e1369be94f924#diff-7eb32cb816db9aefed03469f59ccfcd4985b0a1e98fe5da291b0ec33ff7748d9R24-R33" ref="nofollow noopener noreferrer">使用 package.json 中 browser 字段定位模块</a>，否则不符合<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSunshowerC%2Fblog%2Fissues%2F8%23browser-vs-module-vs-main" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/SunshowerC/blog/issues/8#browser-vs-module-vs-main" ref="nofollow noopener noreferrer">浏览器相关依赖的解析规则</a>。这里代码是参考了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fformium%2Ftsdx%2Fblob%2F462af2d002987f985695b98400e0344b8f2754b7%2Fsrc%2FcreateRollupConfig.ts%23L115-L122" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/formium/tsdx/blob/462af2d002987f985695b98400e0344b8f2754b7/src/createRollupConfig.ts#L115-L122" ref="nofollow noopener noreferrer">tsdx 源码</a>，增加了 <code>browser: true</code> 并修改了 mainFields。这应该算是 tsdx 的 bug 了。</li>
</ol>
<h3 data-id="heading-12">方案二：根据 TARGET_ENVIRONMENT 环境变量，动态 require</h3>
<blockquote>
<p> 本次修改的代码内容，参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F6b97a5af363f94fb185fe039082aaec7ce6af6a6" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/6b97a5af363f94fb185fe039082aaec7ce6af6a6" ref="nofollow noopener noreferrer">Commit</a>。</p>
</blockquote>
<p>先看 <code>src/use-crypto.js</code> 文件。在该文件中根据 <code>process.env.TARGET_ENVIRONMENT</code> 动态加载指定模块。</p>
<p>然后在 <code>tsdx.config.js</code> 文件中，使用 commonjs 插件对 <code>use-crypto.js</code> 进行处理。</p>
<p>根据 commonjs 插件的处理流程，如果动态 require  依赖 A 或依赖 B， 那么这两个 require 语句都会先被转换成 ES6 的 import  语句。依赖 A 和依赖 B 都会被当做依赖，打包到最后的产物中。如此便会增加产物构建时间和体积。</p>
<p>但这个问题可以被优雅地解决掉。只要把 replace 插件放到 commonjs 插件的前面，那么死代码就会先被移除，然后代码才被 commonjs 处理。如此一来就不会对构建时间造成影响了。</p>
<blockquote>
<p>参考 [replace 插件的 README.md]&#123;<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frollup%2Fplugins%2Ftree%2Fmaster%2Fpackages%2Freplace%23usage%257D%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/rollup/plugins/tree/master/packages/replace#usage%7D%E3%80%82" ref="nofollow noopener noreferrer">github.com/rollup/plug…</a>
Typically, <code>@rollup/plugin-replace</code> should be placed in <code>plugins</code> before other plugins so that they may apply optimizations, such as dead code removal.</p>
</blockquote>
<p>实际上在本次 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F6b97a5af363f94fb185fe039082aaec7ce6af6a6" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/6b97a5af363f94fb185fe039082aaec7ce6af6a6" ref="nofollow noopener noreferrer">Commit</a> 后，执行 <code>yarn build:browser</code> 并在浏览器中打开 <code>index.html</code> 文件，会发现如下报错。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/598420806f5d4234a4402e3adde4bc1c~tplv-k3u1fbpfcp-watermark.image" alt="buffer-is-undefined.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这就说明方案二还需要像方案一一样，把所有 Node.js 的内置模块都处理一下，所以方案二是依赖于方案一的。**但方案二在特定场景下还是非常有用的，比如需要在 Node.js 环境使用浏览器环境涉及的功能。**例如，如果想 Node.js 环境使用 DOM 的 API，那么可以根据环境判断是否引入在 Node.js 环境模拟 DOM 操作相关的库（如：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fjsdom" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/jsdom" ref="nofollow noopener noreferrer">jsdom</a>）。</p>
<blockquote>
<p>该方案最终能在浏览器中运行的代码，参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2Ff137094bc43139b176b2a813100df5c554152ebe" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/f137094bc43139b176b2a813100df5c554152ebe" ref="nofollow noopener noreferrer">Commit</a>。</p>
</blockquote>
<h3 data-id="heading-13">方案三：自定义 polyfill 文件</h3>
<p>类似于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fali-sdk%2Fali-oss" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ali-sdk/ali-oss" ref="nofollow noopener noreferrer">Ali OSS</a>。在项目中提供 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fali-sdk%2Fali-oss%2Ftree%2Fmaster%2Fshims%2Fcrypto" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ali-sdk/ali-oss/tree/master/shims/crypto" ref="nofollow noopener noreferrer">crypto 的 polyfill 文件</a>，然后<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fali-sdk%2Fali-oss%2Fblob%2Fbb565c202abbea2b329d4c03b0eddaed9ece9766%2Fpackage.json%23L11-L20" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ali-sdk/ali-oss/blob/bb565c202abbea2b329d4c03b0eddaed9ece9766/package.json#L11-L20" ref="nofollow noopener noreferrer">在浏览器环境打包时使用该 polyfill</a>。</p>
<p>OSS 使用的 crypto polyfill 就是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcrypto-browserify%2Fcrypto-browserify" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/crypto-browserify/crypto-browserify" ref="nofollow noopener noreferrer">crypto-browserify</a>。但是它只选择性的包含了 OSS 需要的方法（如：sha1 和 md5)，不包含其他算法（如：sha256）。使用这种方式的好处是**可以保证 polyfill 的代码量最小，减小打包体积，提升构建速度。**但即使使用这种方式，我们仍然需要处理 Node.js 的内置模块（如：buffer），因为 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fali-sdk%2Fali-oss%2Fblob%2Fmaster%2Fshims%2Fcrypto%2Fcrypto.js%23L2" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ali-sdk/ali-oss/blob/master/shims/crypto/crypto.js#L2" ref="nofollow noopener noreferrer">crypto-browserify 仍然使用了 buffer</a>。</p>
<p>自定义了 polyfill 文件后，有两种方式可以根据当前环境判断是否导入该 polyfill。</p>
<ol>
<li>通过 <code>TARGET_ENVIRONMENT</code> 环境变量动态 require。</li>
<li>通过在 tsdx.config.js 增加插件 <code>@rollup/plugin-alias</code>，并在浏览器环境将指定包映射到 polyfill 文件。</li>
</ol>
<p>第一种方式就不再赘述了，接下来使用第二种方式实现。实际上，<strong>我更推荐第一种方式，因为第一种方式从代码层面上看更加直观，而第二种方式通过 rollup 插件进行配置，需要更高的理解成本。</strong></p>
<blockquote>
<p>实现代码参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F03d6f6cda8b9830e83f9d168be219a05aeedf266" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/03d6f6cda8b9830e83f9d168be219a05aeedf266" ref="nofollow noopener noreferrer">Commit</a>。</p>
</blockquote>
<h3 data-id="heading-14">对比上述方案</h3>
<p>如果在浏览器端使用了 Node.js 的模块，那么需要把基础的内置模块进行打包，所以方案一是必选的。只是像 crypto 这种很复杂的内置模块，可以通过自定义 polyfill 的方式实现。通过对比方案一和方案三，方案一将内置的 crypto 构建到 umd 产物中，耗时 20s，UMD 产物大小为 1MB，而方案三将自定义的 polyfill 构建到 umd 产物中，耗时只有 10s，UMD 产物大小只有 70KB。</p>
<p>方案二在结合了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40rollup%2Fplugin-replace" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/@rollup/plugin-replace" ref="nofollow noopener noreferrer">replace</a> 插件后，只会导入目标环境指定的依赖，不会增加构建耗时和产物体积。在除了简单 Node.js 内置模块的场景外，方案二是非常不错的利器，例如将方案二和方案三结合使用。</p>
<p>尽管理论上可以通过方案二实现「在浏览器环境导入 Node.js 内置模块的浏览器版本」，但是这样做有有个缺点：如果第三方依赖使用了 Node.js 的内置模块（例如：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcrypto-browserify%2Fcrypto-browserify" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/crypto-browserify/crypto-browserify" ref="nofollow noopener noreferrer">crypto-browserify</a> 内部就使用了 buffer），我们不可能修改这些三方依赖的代码，使他们导入 buffer 的浏览器版本。所以实际上，仅通过方案二我们不可能实现「在浏览器环境导入 Node.js 内置模块的浏览器版本」。但可以通过 alias 插件实现，使用 alias 插件和使用 builtin 插件本质上相同。</p>
<h2 data-id="heading-15"><code>yarn build</code> 同时构建浏览器和 Node.js 环境产物</h2>
<p>先前我们已经在 <code>package.json</code> 中增加了 <code>build:node</code> 和 <code>build:browser</code> 两条脚本指令。理想情况下，两条构建语句应该并行执行。但由于 tsdx 存在以下两个限制，我们只能通过自定义脚本绕过去。</p>
<ol>
<li>构建产物只能存放到 dist 目录中（尽管可以修改 rollupConfig.output，但 tsdx 内部逻辑与默认的产物路径存在耦合）。</li>
<li>tsdx 每次执行构建时都会删除上次的构建产物（<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fformium%2Ftsdx%2Fissues%2F746%23issuecomment-643524594" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/formium/tsdx/issues/746#issuecomment-643524594" ref="nofollow noopener noreferrer">--noClean 在 build 时不会生效</a>）。</li>
</ol>
<blockquote>
<p>实现代码参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F279b05748ca128a0f5ab9058fc03d4c976e86b2f" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/279b05748ca128a0f5ab9058fc03d4c976e86b2f" ref="nofollow noopener noreferrer">Commit</a>。</p>
</blockquote>
<p>最终产物被放在 <code>browser/</code> 和 <code>dist/</code>，为什么没有把浏览器环境的产物放到 <code>dist/browser</code> 中呢？原因有以下几点：</p>
<ol>
<li><code>src/browser</code> 目录下的 TS 文件将被放到 <code>dist/browser</code> 目录中，所以存在文件冲突的可能。</li>
<li>允许使用方通过 <code>universal-sdk-by-tsdx/browser</code> 导入浏览器环境的产物，并且此时的 TS 类型文件也是使用的 <code>browser/index.d.ts</code>。</li>
<li>可以保证 sourcemap 后的源码位置不变。如果将产物放到 <code>dist/browser</code> 中，那么 sourcemap 映射后的源码路径将是 <code>dist/src/...</code>，而不是 <code>src/...</code>。</li>
</ol>
<h1 data-id="heading-16">SDK 对环境的最低版本支持</h1>
<p>SDK 需要表明自身支持的运行环境，最好可以通过配置的方式实现，以便后续升级。</p>
<h2 data-id="heading-17">Node.js 支持最低版本 v10</h2>
<p>通过查看 tsdx 的源码，发现<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fformium%2Ftsdx%2Fblob%2Fmaster%2Fsrc%2FcreateRollupConfig.ts%23L192" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/formium/tsdx/blob/master/src/createRollupConfig.ts#L192" ref="nofollow noopener noreferrer">其 hard code 了 Node.js 的最低版本为 v10</a>。</p>
<p>为了方便我们自行配置支持的 Node.js 版本，我们在 <code>tsdx.config.js</code> 文件中重写它。</p>
<blockquote>
<p>实现代码参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F97487f1b6ccb0bd61b2b2a1dccf7d559d8d12d8f" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/97487f1b6ccb0bd61b2b2a1dccf7d559d8d12d8f" ref="nofollow noopener noreferrer">Commit</a></p>
</blockquote>
<p>在 <code>src/test-node-version.ts</code> 文件中，存在 <code>nullish-coalescing-operator</code> 语法和 <code>exponentiation-operator</code> 语法。由于 <code>nullish-coalescing-operator</code> 在 node@v14 才支持，而 <code>exponentiation-operator</code> 在 node@v7 就支持了，所以执行 <code>yarn build:node</code> 后可以看到 <code>nullish-coalescing-operator</code> 语法被转译了，而 <code>exponentiation-operator</code> 语法没有被转译。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75dcfbb4e70a44c2bc6e7fb01c92fef6~tplv-k3u1fbpfcp-watermark.image" alt="support-node-v10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果把<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F97487f1b6ccb0bd61b2b2a1dccf7d559d8d12d8f%23diff-7eb32cb816db9aefed03469f59ccfcd4985b0a1e98fe5da291b0ec33ff7748d9R22" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/97487f1b6ccb0bd61b2b2a1dccf7d559d8d12d8f#diff-7eb32cb816db9aefed03469f59ccfcd4985b0a1e98fe5da291b0ec33ff7748d9R22" ref="nofollow noopener noreferrer">支持的 Node.js 版本改为 <code>'6'</code></a>，那么 <code>exponentiation-operator</code> 也会被转译。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/606e72eeb4a7471aa60c1683a0aad032~tplv-k3u1fbpfcp-watermark.image" alt="support-node-v6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><code>babel-preset-env</code> 把 ES 特性所需的的环境版本配置在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fbabel%2Fbabel%2Fblob%2Fmain%2Fpackages%2Fbabel-compat-data%2Fdata%2Fplugins.json" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/babel/babel/blob/main/packages/babel-compat-data/data/plugins.json" ref="nofollow noopener noreferrer">babel-compat-data/data/plugins.json</a> 文件中。在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnode.green%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://node.green/" ref="nofollow noopener noreferrer">node.green</a> 网站，也可以清晰地看到 ES 特性在 Node.js 环境的支持情况。</p>
</blockquote>
<h2 data-id="heading-18">配置需要支持的浏览器</h2>
<blockquote>
<p>本次修改参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2Fc5de5638c6ac9153e2cbc3890aab24aa46f880b3" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/c5de5638c6ac9153e2cbc3890aab24aa46f880b3" ref="nofollow noopener noreferrer">Commit</a>。</p>
</blockquote>
<p>通过配置 <code>package.json#browserslist</code> 字段值，即可配置 SDK 支持的浏览器。因为当前配置的值为 <code>"Chrome >= 70"</code>，所以执行 <code>yarn build:browser</code> 后，<code>nullish-coalescing-operator</code> 语法会被转译，而 <code>exponentiation-operator</code> 语法不会被转译。</p>
<p>如果把 <code>package.json#browserslist</code> 字段值改为 <code>"Chrome >= 40"</code>，那么 <code>nullish-coalescing-operator</code> 和 <code>exponentiation-operator</code> 都会被转译。</p>
<h2 data-id="heading-19">Node.js 环境和浏览器环境的 browserslist 配置会相互影响吗？</h2>
<p>因为在 Node.js 环境，我们设置了 <code>babel-preset-env</code> 的 <code>targets</code> 参数，所以在 Node.js 环境中不会使用 <code>package.json#browserslist</code> 配置。而浏览器环境我们没有设置 <code>targets</code> 参数，便只会使用 <code>package.json#browserslist</code> 配置。</p>
<blockquote>
<p>参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbabeljs.io%2Fdocs%2Fen%2Fbabel-preset-env" target="_blank" rel="nofollow noopener noreferrer" title="https://babeljs.io/docs/en/babel-preset-env" ref="nofollow noopener noreferrer">官网原文</a>。
By default @babel/preset-env will use browserslist config sources unless either the targets or ignoreBrowserslistConfig options are set.</p>
</blockquote>
<h1 data-id="heading-20">测试</h1>
<h2 data-id="heading-21">单元测试</h2>
<p>单元测试的重要性就不必多说了吧，没有单测的 SDK 是不合格的，我是不会用的。</p>
<blockquote>
<p>本次修改参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F487e50404e00012964686e9fd87e837c2251c71d" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/487e50404e00012964686e9fd87e837c2251c71d" ref="nofollow noopener noreferrer">Commit</a></p>
</blockquote>
<p>由于需要做 Node.js 环境和浏览器环境的单元测试，所以在 <code>package.json</code> 中新建了两条脚本指令 <code>test:browser</code> 和 <code>test:node</code>。修改 <code>test</code> 脚本执行两个环境的单测，并在最后通过 <code>scripts/mapCoverage.js</code> 将测试覆盖率进行合并。</p>
<h3 data-id="heading-22">测试代码可以直接引用构建后的产物吗？</h3>
<p>相较于在测试文件中引用 <code>src/</code> 中的代码，如果直接引用构建后的产物代码。有以下几个优点：</p>
<ol>
<li>直接引用产物中的代码，可以提前发现在构建环节存在的问题。毕竟是测试，那么就应该尽量模拟使用方使用该 SDK 的场景。</li>
<li>因为我们代码中使用了环境变量 <code>TARGET_ENVIRONMENT</code> 进行判断，所以如果引用 <code>src/</code> 中的文件，我们就需要在所有测试用例前设置 <code>TARGET_ENVIRONMENT</code> 环境变量，存在一定的耦合。但引用 <code>dist/</code> 中的代码就不用关心该环境变量了。</li>
</ol>
<p>但引用产物代码后，是不是代码执行报错时或调试时就不能定位到 <code>src/</code> 中的源码呢？其实并不会，即使引用的是 <code>dist/</code> 中打包的产物，<code>yarn test</code> 仍会自动使用 sourcemap 文件。当 <code>console.log()</code> 执行或运行出错时都会指向真实的 <code>src/</code> 文件。所以这并不是引用产物代码的缺点，但它有另一个更严重的缺点：<strong>测试覆盖率不准</strong>。所以如果 SDK 需要测试覆盖率报告，那么就不能引用构建后的产物代码进行测试。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b32a29fcc854822a0508bcae46773d4~tplv-k3u1fbpfcp-watermark.image" alt="yarn-test-error-for-dist.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-23">浏览器环境的 Demo</h2>
<p>前面提到如果使用方引用的是浏览器环境的 cjs 或 esm 产物，那么 SDK 使用的 Node.js 内置模块需要由使用方负责打包。但这个场景是单元测试没办法覆盖的（因为单测运行在 Node.js 环境），所以需要建立 Demo 验证 SDK 在该场景下的可用性。</p>
<blockquote>
<p>本次修改参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F08724f51fe6a5a71540840ede04d5d9b7964e3e1" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/08724f51fe6a5a71540840ede04d5d9b7964e3e1" ref="nofollow noopener noreferrer">Commit</a>。Demo 创建流程参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2Fguides%2Fgetting-started%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.js.org/guides/getting-started/" ref="nofollow noopener noreferrer">Webpack - Getting Started</a>。</p>
</blockquote>
<p>在 <code>example/webpack.config.js</code> 中，由于 webpack@5 默认不会打包 Node.js 内置模块的 polyfill，所以需要使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F08724f51fe6a5a71540840ede04d5d9b7964e3e1%23diff-7dd57a4f662248b39cb60c9020a05a60bad59359a915a5ac35b9699cf7bf1095R17" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/08724f51fe6a5a71540840ede04d5d9b7964e3e1#diff-7dd57a4f662248b39cb60c9020a05a60bad59359a915a5ac35b9699cf7bf1095R17" ref="nofollow noopener noreferrer"><code>node-polyfill-webpack-plugin</code></a>。为了能够在浏览器的 DevTools 中查看 SDK 的源码，所以使用了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F08724f51fe6a5a71540840ede04d5d9b7964e3e1%23diff-7dd57a4f662248b39cb60c9020a05a60bad59359a915a5ac35b9699cf7bf1095R7-R16" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/08724f51fe6a5a71540840ede04d5d9b7964e3e1#diff-7dd57a4f662248b39cb60c9020a05a60bad59359a915a5ac35b9699cf7bf1095R7-R16" ref="nofollow noopener noreferrer"><code>source-map-loader</code></a>。</p>
<p>在 <code>package.json</code> 中，将对外暴露的模块字段都组织到一起，并添加了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx%2Fcommit%2F08724f51fe6a5a71540840ede04d5d9b7964e3e1%23diff-7ae45ad102eab3b6d7e7896acd08c427a9b25b346470d7bc6507b6481575d519R51-R54" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx/commit/08724f51fe6a5a71540840ede04d5d9b7964e3e1#diff-7ae45ad102eab3b6d7e7896acd08c427a9b25b346470d7bc6507b6481575d519R51-R54" ref="nofollow noopener noreferrer"><code>"browser"</code> 字段</a>。如果不添加 <code>"browser"</code> 字段，则 example 使用的 SDK 将是 Node.js 的版本，不符合预期。</p>
<h2 data-id="heading-24">总结</h2>
<p>本文记录了搭建通用 SDK 的心路历程，总结了实现一款通用 SDK 遇到的问题，并给出解决方案。</p>
<p>如果你也有类似需求，那么直接复制<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMoonBall%2Funiversal-sdk-by-tsdx" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/MoonBall/universal-sdk-by-tsdx" ref="nofollow noopener noreferrer">该项目</a>，就能开始写 SDK 了。</p>
<hr>
<p>好了，我要去写 SDK 了~</p>
<p><strong>原创不易，别忘了点赞鼓励哦 ❤️</strong></p></div>  
</div>
            