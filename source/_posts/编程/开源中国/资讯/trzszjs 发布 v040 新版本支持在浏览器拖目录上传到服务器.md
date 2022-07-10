
---
title: 'trzsz.js 发布 v0.4.0 新版本支持在浏览器拖目录上传到服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a36282743cf104477cc51bd9cd57d0fcd02.gif'
author: 开源中国
comments: false
date: Sun, 10 Jul 2022 20:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a36282743cf104477cc51bd9cd57d0fcd02.gif'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftrzsz%2Ftrzsz.js" target="_blank">https://github.com/trzsz/trzsz.js</a> 发布 v0.4.0 新版本：</p> 
<p style="text-align:left">1、支持 Windows 本地的 cmd、PowerShell 等。</p> 
<p style="text-align:left">2、支持目录 <span style="background-color:#dddddd">trz -d</span> 上传和 <span style="background-color:#dddddd">tsz -d xxx</span> 下载。</p> 
<p style="text-align:left">3、支持拖文件，甚至拖目录，直接上传到服务器。</p> 
<p style="text-align:left">在浏览器中使用以下代码，即可实现拖文件和目录上传。</p> 
<pre style="text-align:left"><code class="language-js">terminalHtmlElement.addEventListener(<span style="color:#b5bd68">"dragover"</span>, (event) => event.preventDefault());
terminalHtmlElement.addEventListener(<span style="color:#b5bd68">"drop"</span>, (event) => &#123;
  event.preventDefault();
  trzszFilter
    .uploadFiles(event.dataTransfer.items)
    .then(<span><span style="color:#de935f">()</span> =></span> <span style="color:#de935f">console</span>.log(<span style="color:#b5bd68">"upload success"</span>))
    .catch(<span>(<span style="color:#de935f">err</span>) =></span> <span style="color:#de935f">console</span>.log(err));
&#125;);
</code></pre> 
<p style="text-align:left">需要在服务器上安装<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftrzsz%2Ftrzsz" target="_blank">trzsz</a><span> </span>或<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftrzsz%2Ftrzsz-go" target="_blank">trzsz-go</a><span> </span>，将<span> </span><code>trz</code><span> </span>程序放到某个<span> </span><code>PATH</code><span> </span>路径下即可。</p> 
<hr> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a36282743cf104477cc51bd9cd57d0fcd02.gif" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-8f852f401a545c8490ea0aa1f45c3626b7d.gif" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            