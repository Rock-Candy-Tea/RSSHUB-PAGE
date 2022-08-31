
---
title: 'Proxy-Go v12.1 发布，十分好用的 IP_HTTP(S)_SOCKS5 代理！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://camo.githubusercontent.com/95febdd5009412c5ee4e189e8098750e5ad30346f747825985ea6fb14b38c42f/68747470733a2f2f6d6972726f72732e686f73743930302e636f6d2f68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f736e61696c3030372f676f70726f78792f6d61737465722f646f632f696d616765732f6c6f676f2e6a7067'
author: 开源中国
comments: false
date: Wed, 31 Aug 2022 15:17:00 GMT
thumbnail: 'https://camo.githubusercontent.com/95febdd5009412c5ee4e189e8098750e5ad30346f747825985ea6fb14b38c42f/68747470733a2f2f6d6972726f72732e686f73743930302e636f6d2f68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f736e61696c3030372f676f70726f78792f6d61737465722f646f632f696d616765732f6c6f676f2e6a7067'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="GitHub - snail007/goproxy: 🔥 Proxy is a high performance HTTP(S) proxies,  SOCKS5 proxies,WEBSOCKET, TCP, UDP proxy server implemented by golang. Now,  it supports chain-style proxies,nat forwarding in different lan,TCP/UDP  port forwarding, SSH" src="https://camo.githubusercontent.com/95febdd5009412c5ee4e189e8098750e5ad30346f747825985ea6fb14b38c42f/68747470733a2f2f6d6972726f72732e686f73743930302e636f6d2f68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f736e61696c3030372f676f70726f78792f6d61737465722f646f632f696d616765732f6c6f676f2e6a7067" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Proxy 是 golang 实现的高性能 http、https、websocket、tcp、udp、socks5 代理服务器，支持正向代理、反向代理、透明代理、内网穿透、TCP/UDP 端口映射、SSH 中转、TLS 加密传输、协议转换、DNS 防污染智能代理、前置 CDN/Nginx 反代、代理连接重定向、API 动态调用上级代理、限速限连接数。提供全平台的命令行版本，友好易用的 Windows&Linux&macOS 控制面板，强大的安卓版。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>更新内容</strong><br> <span style="background-color:#ffffff; color:#24292f">1、修复dns处理转发规则顺序可能错乱的问题。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">更新： v10.7 及以后版本，执行：<code>proxy update</code>，即可完成快速更新到最新版。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>特色功能</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li style="text-align:left">链式代理，程序本身可以作为一级代理，如果设置了上级代理那么可以作为二级代理，乃至 N 级代理。</li> 
 <li>通讯加密，如果程序不是一级代理，而且上级代理也是本程序，那么可以加密和上级代理之间的通讯，采用底层 tls 高强度加密，安全无特征。</li> 
 <li>智能 HTTP 代理，HTTPS 代理，SOCKS5 代理，会自动判断访问的网站是否屏蔽，如果被屏蔽那么就会使用上级代理 (前提是配置了上级代理) 访问网站；如果访问的网站没有被屏蔽，为了加速访问，代理会直接访问网站，不使用上级代理。</li> 
 <li>域名黑白名单，更加自由的控制网站的访问方式。</li> 
 <li>跨平台性，无论你是 widows，linux，还是 mac，甚至是树莓派，都可以很好的运行 proxy。</li> 
 <li>多协议支持，支持 HTTP (S)，TCP，UDP，Websocket，SOCKS5 代理。</li> 
 <li>TCP/UDP 端口转发。</li> 
 <li>游戏盾，游戏代理，高仿服务器。</li> 
 <li>内网穿透，P2P 传输，协议支持 TCP 和 UDP，针对 HTTP 的优化穿透。</li> 
 <li>SSH 中转，HTTP (S)，SOCKS5 代理支持 SSH 中转，上级 Linux 服务器不需要任何服务端，本地一个 proxy 即可开心上网。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxtaci%2Fkcp-go" target="_blank">KCP</a><span> </span>协议支持，HTTP (S)，SOCKS5 代理支持 KCP 协议传输数据，降低延迟，提升浏览体验。</li> 
 <li>动态选择上级代理，通过外部 API，HTTP (S)，SOCKS5，SPS 代理可以实现基于用户或者 IP 的限速，连接数限制，动态获取上级。</li> 
 <li>灵活的上级分配，HTTP (S)，SOCKS5，SPS 代理可以通过配置文件实现基于用户或者 IP 的限速，连接数限制，指定上级。</li> 
 <li>反向代理，支持直接把域名解析到 proxy 监听的 ip，然后 proxy 就会帮你代理访问需要访问的 HTTP (S) 网站。</li> 
 <li>透明 HTTP (S) 代理，配合 iptables，在网关直接把出去的 80，443 方向的流量转发到 proxy，就能实现无感知的智能路由器代理。</li> 
 <li>协议转换，可以把已经存在的 HTTP (S) 或 SOCKS5 或 SS 代理转换为一个端口同时支持 HTTP (S) 和 SOCKS5 和 SS 代理，转换后的 SOCKS5 和 SS 代理如果上级是 SOCKS5 代理，那么支持 UDP 功能，同时支持强大的级联认证功能。</li> 
 <li>自定义底层加密传输，http (s)\sps\socks 代理在 tcp 之上可以通过 tls 标准加密以及 kcp 协议加密 tcp 数据，除此之外还支持在 tls 和 kcp 之后进行自定义加密，也就是说自定义加密和 tls|kcp 是可以联合使用的，内部采用 AES256 加密，使用的时候只需要自己定义一个密码即可。</li> 
 <li>底层压缩高效传输，http (s)\sps\socks 代理在 tcp 之上可以通过自定义加密和 tls 标准加密以及 kcp 协议加密 tcp 数据，在加密之后还可以对数据进行压缩，也就是说压缩功能和自定义加密和 tls|kcp 是可以联合使用的。</li> 
 <li>安全的 DNS 代理，可以通过本地的 proxy 提供的 DNS 代理服务器与上级代理加密通讯实现安全防污染的 DNS 查询。</li> 
 <li>负载均衡，高可用，HTTP (S)\SOCKS5\SPS 代理支持上级负载均衡和高可用，多个上级重复 - P 参数即可。</li> 
 <li>指定出口 IP，HTTP (S)\SOCKS5\SPS\TCP 代理支持客户端用入口 IP 连接过来的，就用入口 IP 作为出口 IP 访问目标网站的功能。如果入口 IP 是内网 IP，出口 IP 不会使用入口 IP</li> 
 <li>支持限速，HTTP (S)\SOCKS5\SPS\TCP 代理支持限速。</li> 
 <li> <p style="margin-left:0; margin-right:0">支持限连接数，HTTP (S)\SOCKS5\SPS\TCP 代理支持限连接数。</p> </li> 
 <li>SOCKS5 代理支持级联认证。</li> 
 <li>证书参数使用 base64 数据，默认情况下 - C，-K 参数是 crt 证书和 key 文件的路径，如果是 base64:// 开头，那么就认为后面的数据是 base64 编码的，会解码后使用。</li> 
 <li>支持客户端 IP 黑白名单，更加安全的控制客户端对代理服务的访问，如果黑白名单同时设置，那么只有白名单生效。socks/http (s)/sps/tcp/udp/dns/ 内网穿透 bridge / 内网穿透 tbridge，都支持客户端 IP 黑白名单。</li> 
 <li>端口范围批量监听，HTTP (S)\SOCKS5\SPS\TCP 代理支持指定端口范围监听，避免启动过多进程，提高性能。</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下载地址:</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/snail/proxy/" target="_blank">Gitee</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnail007%2Fgoproxy" target="_blank">Github</a></p> </li> 
</ul>
                                        </div>
                                      
</div>
            