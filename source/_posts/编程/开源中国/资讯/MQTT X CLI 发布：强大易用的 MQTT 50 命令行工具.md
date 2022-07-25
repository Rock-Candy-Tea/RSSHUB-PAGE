
---
title: 'MQTT X CLI 发布：强大易用的 MQTT 5.0 命令行工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-208730253f776f44a8f15ff416d75e6e7c8.jpg'
author: 开源中国
comments: false
date: Mon, 25 Jul 2022 11:12:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-208730253f776f44a8f15ff416d75e6e7c8.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>近日，由 EMQ 开源的 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmqttx.app%2Fzh" target="_blank"><span>MQTT 5.0 跨平台桌面客户端 MQTT X</span></a></span><span> 发布了 1.8.0 版本。MQTT X 为连接测试各类 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.io%2Fzh" target="_blank"><span>MQTT 消息服务器</span></a></span><span>而生，支持快速创建多个同时在线的 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.io%2Fzh%2Fmqtt-client" target="_blank"><span>MQTT 客户端</span></a></span><span>连接，采用一键式的连接方式和简洁的图形界面，帮助使用者便捷地测试 MQTT/TCP、MQTT/TLS、MQTT/WebSocket 的连接、发布、订阅功能，探索更多 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fmqtt" target="_blank"><span>MQTT 协议</span></a></span><span>特性。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>最新发布的 v1.8.0 除了通过新增的快速复制连接功能优化使用体验之外，还扩展了两个新的使用场景，即增加了 CLI（命令行） 和 Web 端这两种新的交互方式 。这使得 MQTT X 1.8.0 成为支持使用场景最完整的 MQTT 测试客户端。用户可以根据使用需求，自行选择下载桌面客户端、使用终端命令行或是在桌面浏览器上快速完成对 MQTT 的连接测试。</span></p> 
<h2 style="text-align:start"><span>MQTT X CLI：在终端快速开发和调试 MQTT 服务与应用</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>随着 MQTT 协议在物联网领域的广泛使用，越来越多的用户选择使用 MQTT X 进行物联网连接测试。对于部分用户如服务端开发者、服务运维人员等来说，下载桌面客户端可能会占用系统的大量磁盘空间，每次测试前都需要在带有图形化界面的操作系统中打开客户端应用来调试。在这种情况下，桌面客户端这种使用方式就变得不太友好。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>因此 MQTT X 增加了命令行这一交互形式——MQTT X CLI。这是一款全开源的 MQTT 5.0 命令行客户端工具，即命令行上的 MQTT X。</span><span><strong><span>开发者无需使用图形化界面，就能通过 MQTT X CLI 使用命令行快速开发和调试 MQTT 服务与应用。</span></strong></span><span>从而实现以下使用目标：</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>在服务器终端内就可以测试已经部署好的 MQTT 服务</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>通过编辑和使用命令行脚本完成 MQTT 服务的快速测试</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>使用命令行脚本来完成一些简单的压力测试或自动化测试</span></p> </li> 
</ul> 
<blockquote> 
 <p style="margin-left:.8em; margin-right:0"><span>MQTT X CLI 网站：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmqttx.app%2Fzh%2Fcli" target="_blank">https://mqttx.app/zh/cli</a></span></p> 
 <p style="margin-left:.8em; margin-right:.8em"><span>MQTT X CLI v1.8.0 版本下载：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femqx%2FMQTTX%2Freleases%2Ftag%2Fv1.8.0" target="_blank">https://github.com/emqx/MQTTX/releases/tag/v1.8.0</a></span></p> 
 <p style="margin-left:0; margin-right:.8em"><span>MQTT X CLI GitHub 仓库：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femqx%2FMQTTX%2Ftree%2Fmain%2Fcli" target="_blank">https://github.com/emqx/MQTTX/tree/main/cli</a></span></p> 
</blockquote> 
<p style="margin-left:0; margin-right:.8em"><img alt height="524" src="https://oscimg.oschina.net/oscnet/up-208730253f776f44a8f15ff416d75e6e7c8.jpg" width="1520" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start"><span>便捷高效：无需依赖环境即可安装使用</span></h2> 
<h3 style="text-align:start"><span>安装</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>MQTT X CLI 可以快速下载并安装到 macOS、Linux 和 Windows 系统上，</span><span><strong><span>安装前不需要任何的依赖环境准备</span></strong></span><span>，只需在终端内执行命令，即可安装和使用 MQTT X CLI。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>对于 macOS 和 Linux 系统的用户，我们提供了快捷的安装方法，使用命令行可以快速下载二进制文件，并安装最新的 MQTT X CLI 稳定版到操作系统上。Windows 用户则可以到 MQTT X 的</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femqx%2FMQTTX%2Freleases" target="_blank"><span>发布页面</span></a></span><span>内，找到对应的系统架构的 </span><span><code>exe</code></span><span> 包，手动下载后使用。</span></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>注意：下载安装时请注意区分当前使用系统环境的 CPU 架构</span></p> 
</blockquote> 
<h4 style="text-align:start"><span><strong><span>macOS</span></strong></span></h4> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><strong><span>Homebrew</span></strong></span></p> <p style="margin-left:.5rem; margin-right:.5rem"><span>macOS 用户可以通过 Homebrew 来快速安装和使用 MQTT X CLI</span></p> <pre style="text-align:left"><span>brew install emqx/mqttx/mqttx-cli</span></pre> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><strong><span>Intel Chip</span></strong></span></p> <pre style="text-align:left"><span>curl -LO https://www.emqx.com/zh/downloads/MQTTX/v1.8.0/mqttx-cli-macos-x64</span>
<span>sudo install ./mqttx-cli-macos-x64 /usr/local/bin/mqttx</span></pre> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><strong><span>Apple Silicon</span></strong></span></p> <pre style="text-align:left"><span>curl -LO https://www.emqx.com/zh/downloads/MQTTX/v1.8.0/mqttx-cli-macos-arm64</span>
<span>sudo install ./mqttx-cli-macos-arm64 /usr/local/bin/mqttx</span></pre> </li> 
</ul> 
<h4 style="text-align:start"><span><strong><span>Linux</span></strong></span></h4> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><strong><span>x86-64</span></strong></span></p> <pre style="text-align:left"><span>curl -LO https://www.emqx.com/zh/downloads/MQTTX/v1.8.0/mqttx-cli-linux-x64</span>
<span>sudo install ./mqttx-cli-linux-x64 /usr/local/bin/mqttx</span></pre> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span><strong><span>ARM64</span></strong></span></p> <pre style="text-align:left"><span>curl -LO https://www.emqx.com/zh/downloads/MQTTX/v1.8.0/mqttx-cli-linux-arm64</span>
<span>sudo install ./mqttx-cli-linux-arm64 /usr/local/bin/mqttx</span></pre> </li> 
</ul> 
<h4 style="text-align:start"><span><strong><span>Windows</span></strong></span></h4> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>Windows 用户请到 MQTT X 的下载页面内手动下载对应的 </span><span><code>exe</code></span><span> 文件来使用，下载地址：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femqx%2FMQTTX%2Freleases%2Ftag%2Fv1.8.0" target="_blank">https://github.com/emqx/MQTTX/releases/tag/v1.8.0</a></span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="341" src="https://oscimg.oschina.net/oscnet/up-4b4783cfc837d0e347da52ae708aba5ed4d.png" width="1520" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:start"><span><strong><span>NPM</span></strong></span></h4> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>除上述方法外，我们还提供了使用 </span><span><code>npm</code></span><span> 的安装方式，这样无论当前是什么操作系统环境，只要您的系统中有 </span><span><code>Node.js</code></span><span> 环境，就可以快速安装和使用。</span></p> 
<pre style="text-align:left"><span>npm install mqttx-cli -g</span></pre> 
<h3 style="text-align:start"><span>快速开始</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>在完成下载安装后，便可在终端内直接输入 </span><span><code>mqttx</code></span><span> 命令来运行和使用了。您可以加 </span><span><code>-V</code></span><span> 参数来验证 MQTT X CLI 是否安装成功，当输出一个版本号时，就证明 MQTT X CLI 已经成功安装。</span></p> 
<pre style="text-align:left"><span>$ <span style="color:#000000">mqttx</span> <span style="color:#981a1a">-</span><span style="color:#117700">V</span></span>
<span><span style="color:#116644">1.8</span><span style="color:#981a1a">.</span><span style="color:#116644">0</span></span></pre> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>为测试 MQTT X CLI 的使用，我们需要准备一个 MQTT 服务，本文将使用 EMQ 提供的 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fmqtt%2Fpublic-mqtt5-broker" target="_blank"><span>免费公共 MQTT 服务器</span></a></span><span>，该服务基于 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fcloud" target="_blank"><span>MQTT 物联网云平台 - EMQX Cloud</span></a></span><span> 创建，服务器接入信息如下：</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Broker: </span><span><code>broker.emqx.io</code></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>TCP Port: </span><span><strong><span>1883</span></strong></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>WebSocket Port: </span><span><strong><span>8083</span></strong></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>准备好 MQTT 服务后，我们就可以在终端内使用命令行来完成消息的发布与订阅了，我们先在一个终端窗口内，编辑一条订阅主题的命令。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span><strong><span>订阅</span></strong></span></p> 
<pre style="text-align:left"><span>mqttx sub -t 'mqttx/cli' -h 'broker.emqx.io' -p 1883</span></pre> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>在完成订阅后，我们再新建一个终端窗口，编辑一条发布到刚才订阅的主题的消息的命令。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span><strong><span>发布</span></strong></span></p> 
<pre style="text-align:left"><span><span style="color:#117700">mqttx pub</span> <span style="color:#117700">-t</span> <span style="color:#aa1111">'mqttx/cli'</span> <span style="color:#117700">-h</span> <span style="color:#aa1111">'broker.emqx.io'</span> <span style="color:#117700">-p</span> <span style="color:#117700">1883 -m</span> <span style="color:#aa1111">'hello from MQTTX CLI!'</span></span></pre> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>此时我们可以在订阅主题命令的窗口内，看到一条刚才发布过来的消息。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="219" src="https://oscimg.oschina.net/oscnet/up-936905f253602c68e39b13d1b6a794169fe.png" width="1520" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span><strong><span>发布多条消息</span></strong></span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>MQTT X CLI 还支持一个 </span><span><code>pub</code></span><span> 命令可以发布多条消息的功能，只需要在编辑是在命令中添加一个 </span><span><code>-M</code></span><span> 参数和 </span><span><code>-s</code></span><span> 参数，每次输入完成后换行即可。</span></p> 
<pre style="text-align:left"><span>mqttx pub -t 'mqttx/cli' -h 'broker.emqx.io' -p 1883 -s -M</span></pre> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="158" src="https://oscimg.oschina.net/oscnet/up-2dd514e8a364850c26139bef8d22939ae6c.png" width="1520" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>最后，我们再通过使用 MQTT X 的桌面客户端来和 MQTT X CLI 来连接到同一个 MQTT 服务，来测试和验证 MQTT X CLI 的功能，我们使用 MQTT X CLI 发布一条消息，通过 MQTT X 桌面客户端来接收，再反向使用 MQTT X 桌面客户端来发送一条消息到 MQTT X CLI。此时，我们可以看到两边都收到了各自收发的消息。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1151" src="https://oscimg.oschina.net/oscnet/up-2c63ad4fbae55228b5e77f9dd0a082b001b.png" width="1520" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0.8em; margin-right:0.8em; text-align:center"><span>MQTT X 桌面客户端</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="134" src="https://oscimg.oschina.net/oscnet/up-4f594b582b7d0a160d6a512478133c7ccd7.png" width="1520" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0.8em; margin-right:0.8em; text-align:center"><span>MQTT X CLI</span></p> 
<h2 style="text-align:start"><span>结语</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>至此，我们就完成了使用 MQTT X CLI 对 MQTT 消息发布订阅功能的测试和验证。除上述常用功能使用外，MQTT X CLI 还支持设置遗嘱消息、使用 SSL/TLS 来测试 mqtts 的连接等。未来还将支持 MQTT 5.0 连接。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>MQTT X CLI 的发布，为物联网开发者进行 MQTT 连接测试提供了一种新的选择。而对命令行调用、桌面客户端下载和在线浏览器这几种交互形式的完整支持，使得 MQTT X 1.8.0 可帮助不同使用场景需求的用户完成对 MQTT 服务或应用的开发与调试，从而提高用户自身相关业务能力与稳定性。简单易用的测试客户端工具 MQTT X 结合高效可靠的物联网消息服务器 EMQX，将帮助物联网开发者构建具有竞争力的物联网平台与应用。</span></p> 
<h2 style="text-align:start"><span>附：使用帮助</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>您可以在命令行内输入 </span><span><code>--help</code></span><span> 参数来获取使用帮助，或查阅下方的使用参数表来使用 MQTT X CLI。</span></p> 
<pre style="text-align:left"><span># 获取 mqttx 命令的帮助</span>
<span>mqttx --help</span>
<span><span>​</span></span>
<span># 获取订阅命令的帮助</span>
<span>mqttx sub --help</span>
<span><span>​</span></span>
<span># 获取发布命令的帮助</span>
<span>mqttx pub --help</span></pre> 
<h3 style="text-align:start"><span>使用</span><span><strong><span>参数对照表</span></strong></span></h3> 
<table cellspacing="0" class="md-table" style="border-collapse:collapse; border-spacing:0px; box-sizing:border-box; break-inside:auto; cursor:text; margin:0px; overflow:auto; padding:0px; text-align:left; white-space:pre-wrap; width:451.2px; word-break:initial"> 
 <thead> 
  <tr> 
   <th style="text-align:left"><span><span>参数</span></span></th> 
   <th style="text-align:left"><span><span>描述</span></span></th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-V, --version</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>输出当前 MQTT X CLI 的版本号</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-h, --help</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>展示 mqttx 命令的帮助信息</span></span></td> 
  </tr> 
 </tbody> 
</table> 
<table cellspacing="0" class="md-table" style="border-collapse:collapse; border-spacing:0px; box-sizing:border-box; break-inside:auto; cursor:text; margin:0px; overflow:auto; padding:0px; text-align:left; white-space:pre-wrap; width:451.2px; word-break:initial"> 
 <thead> 
  <tr> 
   <th style="text-align:left"><span><span>命令</span></span></th> 
   <th style="text-align:left"><span><span>描述</span></span></th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>pub</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>向主题发布一条消息</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>sub</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>订阅一个主题</span></span></td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span><strong><span>订阅</span></strong></span></p> 
<table cellspacing="0" class="md-table" style="border-collapse:collapse; border-spacing:0px; box-sizing:border-box; break-inside:auto; cursor:text; margin:0px; overflow:auto; padding:0px; text-align:left; white-space:pre-wrap; width:451.2px; word-break:initial"> 
 <thead> 
  <tr> 
   <th style="text-align:left"><span><span>参数</span></span></th> 
   <th style="text-align:left"><span><span>描述</span></span></th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-h, --hostname</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>MQTT Broker 的 Host 地址，默为 localhost</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-p, --port</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>MQTT Broker 的端口号</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-i, --client-id</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>客户端 ID</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-q, --qos <0/1/2></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>消息的 QoS，默认为 0</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--clean</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>clean session 的标志位，默认为 true</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-t, --topic</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>需要订阅的 Topic</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-k, --keepalive</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>MQTT 的 Keep Alive，默认为 30</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-u, --username</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>连接到 MQTT Broker 的用户名</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-P, --password</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>连接到 MQTT Broker 的密码</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-l, --protocol</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>连接时的协议，mqtt, mqtts, ws or wss</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--key</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>key 文件的路径</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--cert</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>cert 文件的路径</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--ca</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>ca 证书的文件路径</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--insecure</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>取消服务器的证书校验</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--will-topic</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>遗嘱消息的 topic</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--will-message</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>遗嘱消息的 payload</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--will-qos <0/1/2></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>遗嘱消息的 QoS</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--will-retain</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>遗嘱消息的 retain 标志位</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-v, --verbose</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>在接收到的 Payload 前显示当前 Topic</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--help</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>展示 sub 命令的帮助信息</span></span></td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span><strong><span>发布</span></strong></span></p> 
<table cellspacing="0" class="md-table" style="border-collapse:collapse; border-spacing:0px; box-sizing:border-box; break-inside:auto; cursor:text; margin:0px; overflow:auto; padding:0px; text-align:left; white-space:pre-wrap; width:451.2px; word-break:initial"> 
 <thead> 
  <tr> 
   <th style="text-align:left"><span><span>参数</span></span></th> 
   <th style="text-align:left"><span><span>描述</span></span></th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-h, --hostname</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>MQTT Broker 的 Host 地址，默为 localhost</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-p, --port</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>MQTT Broker 的端口号</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-i, --client-id</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>客户端 ID</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-q, --qos <0/1/2></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>消息的 QoS，默认为 0</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-t, --topic</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>需要发布的 Topic</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-m, --message</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>需要发布的 Payload 消息</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-r, --retain</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>设置发送消息为 Retain 消息，默认为 fasle</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-s, --stdin</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>从 stdin 中读取信息体</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-M, --multiline</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>可以通过多行发布多条消息</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-u, --username</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>连接到 MQTT Broker 的用户名</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-P, --password</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>连接到 MQTT Broker 的密码</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>-l, --protocol</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>连接时的协议，mqtt, mqtts, ws or wss</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--key</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>key 文件的路径</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--cert</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>cert 文件的路径</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--ca</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>ca 证书的文件路径</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--insecure</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>取消服务器的证书校验</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--will-topic</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>遗嘱消息的 topic</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--will-message</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>遗嘱消息的 payload</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--will-qos <0/1/2></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>遗嘱消息的 QoS</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--will-retain</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>遗嘱消息的 retain 标志位</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>--help</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; text-align:left"><span><span>展示 pub 命令的帮助信息</span></span></td> 
  </tr> 
 </tbody> 
</table> 
<p> </p>
                                        </div>
                                      
</div>
            