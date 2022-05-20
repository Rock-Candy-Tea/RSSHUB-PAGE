
---
title: 'Deno 1.22 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0519/191129_5sdQ_2720166.png'
author: 开源中国
comments: false
date: Fri, 20 May 2022 07:06:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0519/191129_5sdQ_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p>Deno 1.22 已发布，主要变化如下：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.22%23default-type-checking-behavior-has-been-updated" target="_blank">更新默认的类型检查模式</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.22%23removal-of-unstable-denoemit-denoformatdiagnostics-and-denoapplysourcemap-apis" target="_blank">移除不稳定的<code>Deno.emit()</code>,<span> </span><code>Deno.formatDiagnostics()</code>和<code>Deno.applySourceMap()</code>API</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.22%23deno-namespace-is-available-in-workers-by-default" target="_blank"><code>Deno</code><span> 命名空间在 worker 中默认可用</span></a></li> 
 <li>新增<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.22%23--no-config-flag" target="_blank"><code>--no-config</code><span> </span>flag</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.22%23navigatoruseragent" target="_blank"><code>Navigator.userAgent</code></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.22%23updated-denoresolvedns-api" target="_blank">升级<code>Deno.resolveDns()</code>API</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.22%23new-responsejson-static-method" target="_blank">引入新的<code>Response.json()</code><span>静态方法</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.22%23linting-enabled-by-default-in-the-lsp" target="_blank">在 LSP 默认启用 Linting</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.22%23updates-to-the-unstable-denospawn-api" target="_blank">升级不稳定的<code>Deno.spawn()</code>API</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.22%23updates-to-the-test-runner" target="_blank">更新 test runner</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.22%23performancetimeorigin-and-performancetojson" target="_blank"><code>performance.timeOrigin</code>&<code>performance.toJSON</code></a></li> 
</ul> 
<hr> 
<p><strong>更新默认的类型检查模式</strong></p> 
<p>Deno 目前支持三种类型检查模式</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>Full</strong>：完整类型检查模式(<span style="background-color:#ffffff; color:#24292f">full type checking</span>)会检查整个项目，包括所有依赖项。如果依赖项包含类型错误，则会进行反馈。</li> 
 <li><strong>Local</strong>：局部类型检查模式(local type checking)会<span style="background-color:#ffffff; color:#24292f">检查项目中的代码是否存在类型错误，但不针对所有依赖项进行类型检查。</span></li> 
 <li><strong>None</strong>：不执行类型检查</li> 
</ul> 
<p>在这个版本之前，Deno 使用<strong> Full </strong>作为默认类型检查模式。因此开发者会收到自己能直接控制之外的代码（依赖项）所报告的类型错误。团队认为这个默认值不够合理，所以在新版本将默认模式更改为 <strong>Local</strong>。</p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0519/191129_5sdQ_2720166.png" referrerpolicy="no-referrer"></p> 
<p><strong>引入新的<code>Response.json()</code><span>静态方法</span></strong></p> 
<p>此版本为<code>Response</code>全局添加了一个新的静态<code>json()</code>方法，支持从 JSON 结构轻松创建<code>Response</code>对象。</p> 
<pre><code class="language-javascript">const json = &#123; hello: "world" &#125;;

// Previously:
const body = JSON.stringify(json);
const response = new Response(body, &#123;
  headers: &#123; "content-type": "application/json" &#125;,
&#125;);

// Now:
const response = Response.json(json);</code></pre> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>在 LSP 默认启用 Linting</strong></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span><span><span>Deno v1.22 默认启用 IDE/编辑器中<code>deno lsp</code>的 linting。此设置仍然可以禁用，但在大多数项目中，这意味着需要较少的 IDE/编辑器配置，因为大多数项目都启用了 linting。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.22" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            