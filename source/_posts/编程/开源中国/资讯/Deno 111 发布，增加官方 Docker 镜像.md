
---
title: 'Deno 1.11 发布，增加官方 Docker 镜像'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=74'
author: 开源中国
comments: false
date: Fri, 11 Jun 2021 07:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=74'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Deno 1.11.0 已正式发布，此版本增加了不少新特性，以及修复错误。</p> 
<p>主要变化包括：</p> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.11%23official-docker-images" target="_blank">新增官方 Docker 镜像</a></strong></li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.11%23abortable-fetch" target="_blank">Abortable fetch</a>：</strong>以 Web 兼容的方式终止正在进行的 fetch 请求</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.11%23more-web-crypto-apis-supported" target="_blank">引入更多 Web Crypto APIs</a></strong>：支持<code>crypto.subtle.digest</code> 和<code>crypto.randomUUID</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.11%23deno-lint-is-now-stable" target="_blank"><strong><code>deno lint</code> 到达稳定状态</strong></a>：deno lint 比 ESLint 快一倍</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.11%23broadcastchannel" target="_blank"><strong>BroadcastChannel</strong></a>：支持浏览器 API 在 Web worker 之间广播消息</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.11%23textencoderstream-and-textdecoderstream" target="_blank"><strong><code>TextEncoderStream</code>和<code>TextDecoderStream</code></strong></a>：用于流文本的 Web 标准流组合器</li> 
</ul> 
<h1>官方 Docker 镜像</h1> 
<p>Dockerhub 现已提供 Deno 的官方 Docker 镜像。</p> 
<ul> 
 <li>Alpine Linux: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2Fr%2Fdenoland%2Fdeno" target="_blank">denoland/deno:alpine</a></li> 
 <li>Centos: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2Fr%2Fdenoland%2Fdeno" target="_blank">denoland/deno:centos</a></li> 
 <li>Debian: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2Fr%2Fdenoland%2Fdeno" target="_blank">denoland/deno:debian</a>（默认）</li> 
 <li>Distroless: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2Fr%2Fdenoland%2Fdeno" target="_blank">denoland/deno:distroless</a></li> 
 <li>Ubuntu: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2Fr%2Fdenoland%2Fdeno" target="_blank">denoland/deno:ubuntu</a></li> 
</ul> 
<h1>支持更多的 Web Crypto API</h1> 
<p>此版本标志着开发团队开始将 Web Crypto API 添加到 Deno。它可以向开发者的应用程序公开加密原语，可用于使用加密轻松构建安全系统。开发团队称从 Deno 1.0 开始就已支持<code>crypto.getRandomValues()</code> ，现在我们增加了对哈希和 UUID 生成的支持。</p> 
<p>开发团队计划于 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.land%2Fmanual%40v1.11.0%2Fcontributing%2Frelease_schedule" target="_blank">7 月 13 日</a>发布的下一个版本 Deno 1.12 中扩展 Web Crypto API。</p> 
<h1>升级<code>deno compile</code></h1> 
<p>此版本增加了对使用数据 URI 的动态导入的支持，允许从磁盘或远程位置读取源文件并执行它。</p> 
<p>示例</p> 
<pre><code>// some_source_code.js
console.log("Hello Deno!");
</code></pre> 
<pre><code>const sourceCode = await Deno.readTextFile("./some_source_code.js");
const dataUrl = "data:text/javascript;base64," + btoa(sourceCode);
const c = await import(dataUrl);
console.log(c.default); // Output: "Hello Deno!"
</code></pre> 
<h1><code>deno lint</code> 到达稳定状态</h1> 
<p style="text-align:start"><span style="color:#24292e">Deno 附带了一个内置的 linter，可通过<code>deno lint</code>子命令使用它。</span></p> 
<p style="text-align:start"><span style="color:#24292e"><code>deno lint</code>于2020 年 6 月首次引入，版本号为<code>v1.1.0</code>，但作为预防措施，它在使用时需要标记<code>--unstable</code>参数，以表明 linter 仍处于早期开发阶段并可能存在错误。不过经过几轮重构，其稳定性目前已足够。</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeno.com%2Fblog%2Fv1.11" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            