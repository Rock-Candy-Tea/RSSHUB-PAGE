
---
title: 'Newbe.McrMirror Windows 镜像加速已实装'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/202011/12095713_9lNZ.png'
author: 开源中国
comments: false
date: Mon, 09 Aug 2021 01:37:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/202011/12095713_9lNZ.png'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:start"> 
 <h1>更新内容</h1> 
</div> 
<div style="text-align:start"> 
 <div style="text-align:left"> 
  <p style="text-align:left">添加了 Windows 操作系统的主要镜像。</p> 
  <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2F_%2Fmicrosoft-windows" target="_blank">https://hub.docker.com/_/microsoft-windows</a></p> 
  <h2 style="text-align:justify">使用方法</h2> 
  <p style="text-align:justify"><img alt="下载方式" src="https://static.oschina.net/uploads/img/202011/12095713_9lNZ.png" referrerpolicy="no-referrer"></p> 
  <p style="text-align:justify">存在至少三种方法进行加速：</p> 
  <ul> 
   <li>使用 docker-mcr （推荐）</li> 
   <li>拉取国内服务器上的镜像</li> 
   <li>使用 DockerHub 加速器</li> 
  </ul> 
  <p style="text-align:justify">注意，无论采用什么方式，请先确保本地的 docker 已经正常可用。</p> 
  <h3 style="text-align:justify">使用 docker-mcr</h3> 
  <p style="text-align:justify">docker-mcr 是一个 dotnet core global tool，简单几步，便可以进行安装和使用。</p> 
  <p style="text-align:justify"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdotnet.microsoft.com%2Fdownload" target="_blank">进入 dotnet 页面，下载并安装 netcore 3.1 或 5 SDK</a>。</p> 
  <p style="text-align:justify">安装完毕后打开控制台运行以下命令:</p> 
  <pre style="text-align:left"><code class="language-bash"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">dotnet</span></span></span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">tool install newbe.mcrmirror -g</span></span></span></span></span></code></pre> 
  <p style="text-align:justify">现在，假如需要拉取 mcr.microsoft.com/dotnet/aspnet:5.0-buster-slim ，则运行以下命令：</p> 
  <pre style="text-align:left"><code class="language-bash"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">docker-mcr</span></span></span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">-i</span></span></span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">mcr</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.microsoft</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.com</span></span></span></span></span>/<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">dotnet</span></span></span></span></span>/<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">aspnet</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">:5.0-buster-slim</span></span></span></span></span></code></pre> 
  <p style="text-align:justify">等待完成之后，便可以在本地看到已经拉取完毕的镜像。</p> 
  <p style="text-align:justify">如果您曾经安装过 newbe.mcrmirror ,您需要使用以下命令来进行升级，确保最佳的体验。</p> 
  <pre style="text-align:left"><code class="language-bash"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">dotnet</span></span></span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">tool update newbe.mcrmirror -g</span></span></span></span></span></code></pre> 
  <h3 style="text-align:justify">拉取国内服务器上的镜像</h3> 
  <p style="text-align:justify">加速的本质是因为我将镜像推送到了国内的服务器，目前在以下服务器均存在镜像:</p> 
  <ul> 
   <li>阿里云 registry.cn-hangzhou.aliyuncs.com/newbe36524</li> 
  </ul> 
  <p style="text-align:justify">假设需要拉取 aspnet:5.0-buster-slim</p> 
  <p style="text-align:justify"><a href="https://gitee.com/yks/Newbe.McrMirror/raw/master/src/GithubActionGeneration/config-v2.json" target="_blank">点击此处打开配置文件</a>，搜索 mcr.microsoft.com/dotnet/core/aspnet:5.0-buster-slim 会找到以下节点</p> 
  <pre style="text-align:left"><code class="language-json">&#123;
  <span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">"tag"</span></span></span></span></span>: <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"aspnet:5.0-buster-slim"</span></span></span></span></span>,
  <span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">"source"</span></span></span></span></span>: <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">"mcr.microsoft.com/dotnet/aspnet:5.0-buster-slim"</span></span></span></span></span>
&#125;</code></pre> 
  <p style="text-align:justify">则说明在国内镜像的 tag 为 aspnet:5.0-buster-slim。</p> 
  <p style="text-align:justify">则拼接上面的前缀，则得到地址 registry.cn-hangzhou.aliyuncs.com/newbe36524/aspnet:5.0-buster-slim</p> 
  <p style="text-align:justify">然后，为了不修改默认的 Dockerfile 您可以运行以下命令:</p> 
  <pre style="text-align:left"><code class="language-bash"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">docker</span></span></span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">pull</span></span></span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">registry</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.cn-hangzhou</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.aliyuncs</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.com</span></span></span></span></span>/<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">newbe36524</span></span></span></span></span>/<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">aspnet</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">:5.0-buster-slim</span></span></span></span></span>
<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">docker</span></span></span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">tag</span></span></span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">registry</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.cn-hangzhou</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.aliyuncs</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.com</span></span></span></span></span>/<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">newbe36524</span></span></span></span></span>/<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">aspnet</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">:5.0-buster-slim</span></span></span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">mcr</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.microsoft</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.com</span></span></span></span></span>/<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">dotnet</span></span></span></span></span>/<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">aspnet</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">:5.0-buster-slim</span></span></span></span></span></code></pre> 
  <p style="text-align:justify">这样你就成功的在本地得到了 mcr.microsoft.com/dotnet/aspnet:5.0-buster-slim 镜像。</p> 
  <p style="text-align:justify">当然，你也可以直接把 registry.cn-hangzhou.aliyuncs.com/newbe36524/aspnet:5.0-buster-slim 写入到你的 Docker file 中。</p> 
  <h3 style="text-align:justify">使用 DockerHub 加速器</h3> 
  <p style="text-align:justify">我也将镜像推送到了 dockerhub ，所以正常来说，在中国大陆使用 dockerhub 加速器也可以达到加速的效果。</p> 
  <p style="text-align:justify">规则，mcr.microsoft.com/dotnet/&#123;name&#125;:&#123;tag&#125; -> newbe36524/&#123;name&#125;:&#123;tag&#125;</p> 
  <p style="text-align:justify">例如，您可以运行以下命令:</p> 
  <pre style="text-align:left"><code class="language-bash"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">docker</span></span></span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">pull</span></span></span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">newbe36524</span></span></span></span></span>/<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">aspnet</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">:5.0-buster-slim</span></span></span></span></span>
<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">docker</span></span></span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">tag</span></span></span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">newbe36524</span></span></span></span></span>/<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">aspnet</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">:5.0-buster-slim</span></span></span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">mcr</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.microsoft</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.com</span></span></span></span></span>/<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">dotnet</span></span></span></span></span>/<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">aspnet</span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">:5.0-buster-slim</span></span></span></span></span></code></pre> 
  <p style="text-align:justify">这样你就成功的在本地得到了 mcr.microsoft.com/dotnet/aspnet:5.0-buster-slim 镜像。</p> 
  <p style="text-align:justify">当然，你也可以直接把 newbe36524/aspnet:5.0-buster-slim 写入到你的 Docker file 中。</p> 
  <p style="text-align:justify">在此之前，请确保你正确配置了本地的加速器。</p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            