
---
title: '实战：使用腾讯云快速搭建并部署 Serverless 应用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9202'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 12:59:02 GMT
thumbnail: 'https://picsum.photos/400/300?random=9202'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第16天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>很多开发者一定多少听过 Serverless Framework。既用更少的服务架构，甚至是无服务器，去实现整个工程的开发。开发者不需要关心底层资源、性能等问题，就可以部署完整的 Serverless 应用。这篇文章的场景，是通过腾讯云提供的 Serverless Framework 搭建并部署一个 Egg.js 应用的实战教程。</p>
<h3 data-id="heading-0">Serverless 的应用场景</h3>
<h4 data-id="heading-1">基于云函数的开发</h4>
<p>腾讯云提供的 Serverless Framework，可以让开发者通过命令行或者控制台的方式进行开发、部署和调试应用，结合腾讯云的云函数、API 网关以及数据库等资源，可以完整的开发、部署全栈应用。
腾讯云的云函数有两种，事件型和 web 型，前者支持多种触发方式，例如网关触发、定时触发、COS 资源触发和消息中间件等，而后者目前仅支持 API 网关触发。</p>
<h4 data-id="heading-2">传统项目的快速迁移</h4>
<p>倘若需要将现有的项目快速迁移至 Serverless Framework，例如 Egg、Koa 等，只需要通过几行代码的改造即可快速迁移。</p>
<h3 data-id="heading-3">快速搭建并部署</h3>
<p>这里采用的是命令行的方式进行搭建和部署，在此之前需要拥有腾讯云账号并完成实名认证，建议在开始前仔细阅读相关产品的文档。</p>
<h4 data-id="heading-4">确认环境</h4>
<p>安装腾讯云提供的 Serverless Framework，需要确保你的开发环境拥有 Node10 以上的版本和 Npm。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ node -v
v12.18.0

$ npm -v
7.0.10
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装 serverless</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install -g serverless
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">搭建 Egg 应用</h4>
<p>根据 Egg.js 官方文档，本地初始化一个项目，示例：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm init egg --<span class="hljs-built_in">type</span>=simple

npm install
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在项目根目录启动命令，运行项目</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm run dev

open http://localhost:7001
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">编写 serverless.yml</h4>
<p>Serverless Framework 通过项目配置文件 serverless.yml 完成应用的类型识别与资源配置，本地开发完成后的项目，必须先配置 yml 文件，才可以通过运行 sls deploy 命令，将 serverless.yml 中的配置文件和 inputs 中指定参数或代码目录会都被传入 Serverless Components 部署引擎中，从而完成云端部署。启动部署命令时，serverless 会根据配置自动的创建相关服务并部署，一个基础的 yml 文件如下：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#serverless.yml</span>
app: expressDemoApp <span class="hljs-comment">#  应用名称，默认为与组件实例名称</span>
stage: <span class="hljs-variable">$&#123;env:STAGE&#125;</span> <span class="hljs-comment">#  用于开发环境的隔离，默认为dev</span>

component: express <span class="hljs-comment"># (必填) 引用 component 的名称，当前用到的是 express-tencent 组件</span>
name: expressDemo <span class="hljs-comment"># (必填) 组件创建的实例名称</span>
inputs:
 src:
   src: ./ 
   exclude:
     - .env
 region: ap-guangzhou
 runtime: Nodejs10.15
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但这只是自动部署了一个 Serverless 应用，需要配置事件型的云函数，还要配置网关触发，具体如下：
配置云函数</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">functionName:</span> <span class="hljs-string">xxx</span>

<span class="hljs-attr">functionConf:</span>
    <span class="hljs-attr">eip:</span> <span class="hljs-literal">false</span> <span class="hljs-comment"># 是否固定出口 IP</span>
    <span class="hljs-attr">timeout:</span> <span class="hljs-number">10</span> <span class="hljs-comment"># 函数最长执行时间，单位为秒，可选值范围 1-900 秒，默认为 3 秒</span>
    <span class="hljs-attr">memorySize:</span> <span class="hljs-number">128</span> <span class="hljs-comment">#函数运行时内存大小，默认为 128M，可选范围 64、128MB-3072MB，并且以 128MB 为阶梯</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置 API 网关，这里额外配置了认证方式为应用认证，并关联授权对应的 app 应用，app 应用需要在腾讯云 API 网关控制台创建并获取。</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">serviceName:</span> <span class="hljs-string">xxx</span>
 
<span class="hljs-attr">apigatewayConf:</span>
    <span class="hljs-attr">isDisabled:</span> <span class="hljs-literal">false</span> <span class="hljs-comment"># 关闭自动创建 API 网关功能。默认值为否，即默认自动创建 API 网关。</span>
    <span class="hljs-attr">serviceTimeout:</span> <span class="hljs-number">60</span> <span class="hljs-comment"># Api 超时时间，单位: 秒</span>
    <span class="hljs-attr">protocols:</span> <span class="hljs-comment"># 前端请求的类型，如 http，https，http 与 https</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">http</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">https</span>
    <span class="hljs-attr">environment:</span> <span class="hljs-string">release</span> <span class="hljs-comment"># 发布环境. 目前支持三种发布环境: test（测试）, prepub（预发布） 与 release（发布）</span>
    <span class="hljs-attr">enableCORS:</span> <span class="hljs-literal">false</span><span class="hljs-string">,</span> <span class="hljs-comment"># 开启跨域。默认值为否</span>
    <span class="hljs-attr">autoCreateDns:</span> <span class="hljs-literal">false</span>
    <span class="hljs-attr">endpoints:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">path:</span> <span class="hljs-string">/</span>
        <span class="hljs-attr">method:</span> <span class="hljs-string">ANY</span>
        <span class="hljs-attr">authType:</span> <span class="hljs-string">APP</span>
        <span class="hljs-attr">responseType:</span> <span class="hljs-string">JSON</span>
        <span class="hljs-attr">function:</span>
          <span class="hljs-attr">isIntegratedResponse:</span> <span class="hljs-literal">true</span>
          <span class="hljs-attr">functionQualifier:</span> <span class="hljs-string">$LATEST</span>
          <span class="hljs-attr">functionName:</span> <span class="hljs-string">xxx</span>
        <span class="hljs-attr">app:</span>
          <span class="hljs-attr">name:</span> <span class="hljs-string">xxx</span>
          <span class="hljs-attr">id:</span> <span class="hljs-string">app-xxx</span>
          <span class="hljs-attr">description:</span> <span class="hljs-string">xxx</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">命令行部署</h4>
<p>在控制台执行以下命令即可部署上云，系统会自动配置云函数和 API 网关，部署后可以在控制台查看应用详情和网关入口。</p>
<pre><code class="hljs language-bash copyable" lang="bash">sls deploy
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果没有在 .env 中配置 Secretid 和 Secretkey，那么在部署是需要扫码授权，授权后会生成临时的 Secretid 和 Secretkey。
也可以在部署时查看具体的日志信息</p>
<pre><code class="hljs language-bash copyable" lang="bash">sls deploy --debug
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">欢迎阅读其它文章</h4>
<ul>
<li><a href="https://juejin.cn/post/6991566044674392078" target="_blank" title="https://juejin.cn/post/6991566044674392078">使用 Vite2+Vue3 实现网站国际化｜8月更文挑战</a></li>
<li><a href="https://juejin.cn/post/6991204669573824520" target="_blank" title="https://juejin.cn/post/6991204669573824520">实战：前端接口请求参数混淆</a></li>
<li><a href="https://juejin.cn/post/6975770170413776926" target="_blank" title="https://juejin.cn/post/6975770170413776926">实战：用 Vue3 实现一个 Message 消息组件</a></li>
<li><a href="https://juejin.cn/post/6981232153233195039" target="_blank" title="https://juejin.cn/post/6981232153233195039">实战：用 Vue3 实现 Image 组件，顺便支持懒加载</a></li>
<li><a href="https://juejin.cn/post/6968352814858764296" target="_blank" title="https://juejin.cn/post/6968352814858764296">One Piece，Vue.js 3.0 带来了哪些更新</a></li>
<li><a href="https://juejin.cn/post/6983625803271503886/" target="_blank" title="https://juejin.cn/post/6983625803271503886/">一篇文章消化 ES7、ES8、ES9 主要新特性</a></li>
<li><a href="https://juejin.cn/post/6979053938087723021" target="_blank" title="https://juejin.cn/post/6979053938087723021">技术团队普遍存在的问题和解决方案</a></li>
<li><a href="https://juejin.cn/post/6844903618810757128" target="_blank" title="https://juejin.cn/post/6844903618810757128">ES6中常用的10个新特性讲解</a></li>
<li><a href="https://juejin.cn/post/6983626263327932429" target="_blank" title="https://juejin.cn/post/6983626263327932429">上手后才知道 ，Vue3 的 script setup 语法糖是真的爽</a></li>
</ul></div>  
</div>
            