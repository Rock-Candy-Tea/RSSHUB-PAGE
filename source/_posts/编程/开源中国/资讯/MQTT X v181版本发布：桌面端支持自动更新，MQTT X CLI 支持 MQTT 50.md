
---
title: 'MQTT X v1.8.1版本发布：桌面端支持自动更新，MQTT X CLI 支持 MQTT 5.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e8df1149085933f04e8c2d4f992297b9ca9.png'
author: 开源中国
comments: false
date: Thu, 11 Aug 2022 02:46:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e8df1149085933f04e8c2d4f992297b9ca9.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>近日，MQTT X 发布了最新的 1.8.1 版本（下载地址：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femqx%2FMQTTX%2Freleases%2Ftag%2Fv1.8.1" target="_blank">https://github.com/emqx/MQTTX/releases/tag/v1.8.1</a></span><span>），MQTT X 桌面端版本已支持自动更新，并对 MQTT X Web 页面进行了优化。目前已完成了 MQTT X CLI 对于 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fmqtt%2Fmqtt5" target="_blank"><span>MQTT 5.0</span></a></span><span> 的连接支持及用户属性设置支持，并新增了一个 conn 命令来快速测试连接，后续还将添加 bench 命令，将支持部分场景下的 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fmqtt" target="_blank"><span>MQTT 协议</span></a></span><span>性能测试。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1129" src="https://oscimg.oschina.net/oscnet/up-e8df1149085933f04e8c2d4f992297b9ca9.png" width="1520" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start"><span>MQTT X 桌面客户端</span></h2> 
<h3 style="text-align:start"><span>自动更新功能</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>在之前每次的版本发布中，用户可以通过升级提示框的下载按钮跳转到最新版本下载页面，手动下载安装包完成对软件的更新。从 v1.8.1 开始，用户不再需要手动下载安装，只需在收到升级提示点击按钮，软件后台即可自动将版本升级至最新。自动更新功能可以让用户更快体验到最新功能，提升使用体验。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1111" src="https://oscimg.oschina.net/oscnet/up-8d2574db04a02ebc61de4ad50f93eb4f7b0.jpg" width="1520" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>更新完成后，可以在弹出框内查看最新的发布日志，快速了解到当前版本的更新内容，提升使用体验。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1113" src="https://oscimg.oschina.net/oscnet/up-b8b11865c669ca24e48ddbc8656db2816ac.png" width="1520" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start"><span>默认 MQTT 5.0 连接</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>在之前的版本中，MQTT X 默认是 MQTT 3.1.1 连接。作为目前支持 MQTT 5.0 特性最为完整的 MQTT 客户端工具，我们在最新版本中将 MQTT X 默认连接时的 MQTT 版本修改为了 5.0，方便更多的用户快速使用和体验 MQTT 5.0 的新特性。</span></p> 
<h3 style="text-align:start"><span>对 Topic 进行发布前的验证</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>当用户向带有通配符 +，# 这样的通配符的 Topic 发送消息时，会导致连接断开，很多新用户在不了解 MQTT 协议的时候，会经常出现这样的问题，导致断开连接而产生使用上的疑惑。在 1.8.1 版本中，为避免了这样的情况发生，我们在发布前对 Topic 进行了验证，只有在发布时使用这些不包含通配符的 Topic，才可以发布成功。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="233" src="https://oscimg.oschina.net/oscnet/up-4f9b28e780c66ddca211b534cbebc1096bf.png" width="1520" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start"><span>MQTT X CLI</span></h2> 
<h3 style="text-align:start"><span>MQTT 5.0 支持</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>MQTT X CLI 1.8.1 目前已经完成了对于 MQTT 5.0 的连接支持，并在使用时默认使用 MQTT 5.0 连接。同时还新增了一个用户属性参数 </span><span><code>--user-properties</code></span><span>，支持在连接、发布、订阅时设置用户属性。例如：</span></p> 
<pre style="text-align:left"><span><span style="color:#117700">mqttx pub</span> <span style="color:#117700">-t</span> <span style="color:#aa1111">'hello'</span> <span style="color:#117700">-h</span> <span style="color:#aa1111">'broker.emqx.io'</span> <span style="color:#117700">-p</span> <span style="color:#117700">1883 -m</span> <span style="color:#aa1111">'from MQTTX CLI'</span> <span style="color:#117700">-up</span> <span style="color:#aa1111">"name: mqttx"</span> <span style="color:#aa1111">"company: EMQ"</span></span></pre> 
<h3 style="text-align:start"><span>新增 conn 命令</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>在当前 1.8.0 版本中，只支持 pub 和 sub 两个命令，即支持快速的发布与订阅。而对于一些只需要测试 MQTT 服务连通性的简单场景来说， conn 命令则更加便捷。</span></p> 
<pre style="text-align:left"><span><span style="color:#117700">mqttx conn</span> <span style="color:#117700">-h</span> <span style="color:#aa1111">'broker.emqx.io'</span> <span style="color:#117700">-p</span> <span style="color:#117700">1883 -u</span> <span style="color:#aa1111">'admin'</span> <span style="color:#117700">-P</span> <span style="color:#aa1111">'public'</span></span></pre> 
<h2 style="text-align:start"><span>MQTT X Web</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>MQTT X Web 目前在线地址已修改为：</span><span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.emqx.io%2Fonline-mqtt-client" target="_blank">http://www.emqx.io/online-mqtt-client</a></span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>只需要访问上述地址，即可快速使用这款在线的 MQTT 5.0 客户端工具，通过 MQTT over WebSocket 连接到 MQTT Broker 并在浏览器中测试消息发布和接收，快速开发和调试您的 MQTT 服务与应用。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>在 1.8.1 版本中，优化了页面样式，完善测试功能等。后续还将继续完善 MQTT 5.0 的属性配置功能。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1004" src="https://oscimg.oschina.net/oscnet/up-487b903bfaa0eb7e129e7f70ae9b33a7542.png" width="1520" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start"><span>修复及优化</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>除添加上述新特性外，本次更新还修复了很多已知问题，稳定性得到了进一步提升。</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>修复 MQTT X 在 macOS 系统中，意外退出的弹框提醒</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>修复 MQTT X 在消息列表中展示用户属性时的样式问题</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>修复 MQTT X CLI 下无效的 </span><span><code>--clean</code></span><span> 参数，使用 </span><span><code>--no-clean</code></span><span> 参数替代</span></p> </li> 
</ul> 
<h2 style="text-align:start"><span>未来规划</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>MQTT X 还在持续增强完善中，以期为用户带来更多实用、强大的功能，为物联网平台的测试和开发提供便利。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>接下来我们将重点关注以下方面：</span></p> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>使用体验升级</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>MQTT X CLI 将支持 bench 命令</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>插件系统（例如支持 SparkPlug B、集成 MQTT X CLI）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>脚本功能优化</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>推出 MQTT X Mobile 移动端应用</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>完善 MQTT X Web 功能</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>MQTT Debug 功能</span></p> </li> 
</ul> 
<h2 style="text-align:start"><span>附：连接命令的使用帮助</span></h2> 
<h3 style="text-align:start"><span>连接</span></h3> 
<pre style="text-align:left"><span>mqttx conn --help</span></pre> 
<p><img alt height="789" src="https://oscimg.oschina.net/oscnet/up-1f274f1aafdad66613f7509287ce21267d4.png" width="630" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            