
---
title: 'Cypress 自定配置文件与环境变量定于与访问'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6834092a3204999aabf428d49ae0c0f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 23:37:37 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6834092a3204999aabf428d49ae0c0f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">指定启动命名 open</h1>
<p>默认的 cypress 的配置文件是项目根目录下：</p>
<h2 data-id="heading-1">自定义 Cypress 的环境配置文件：</h2>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-built_in">cd</span> cypress
mkdir config && <span class="hljs-built_in">cd</span> config
touch cypress.dev.json && cypress.json
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">package.json 脚本启动</h2>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"start"</span>: <span class="hljs-string">"umi dev"</span>,
    <span class="hljs-string">"cy:open:dev"</span>: <span class="hljs-string">"cypress open -C ./cypress/config/cypress.dev.json"</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">在 cypress.dev.json 中配置开发环境变量</h2>
<pre><code class="hljs language-js copyable" lang="js">&#123;
<span class="hljs-string">"baseUrl"</span>: <span class="hljs-string">"http://192.168.0.108:8000"</span>,
<span class="hljs-string">"env"</span>: &#123;
    <span class="hljs-string">"username"</span>: <span class="hljs-string">"tom"</span>,
    <span class="hljs-string">"password"</span>: <span class="hljs-string">"jerry"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">从测试用例中访问环境变量</h2>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// env.test.spec.ts</span>
<span class="hljs-comment">/// <reference types="cypress" /></span>

it(<span class="hljs-string">"测试环境变量"</span>, <span class="hljs-function">() =></span> &#123;
    cy.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;Cypress.env(<span class="hljs-string">'username'</span>)&#125;</span>`</span>);
    cy.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;Cypress.env(<span class="hljs-string">'password'</span>)&#125;</span>`</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6834092a3204999aabf428d49ae0c0f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            