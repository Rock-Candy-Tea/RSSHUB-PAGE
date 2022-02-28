
---
title: 'Proxy-Go v11.6 发布，优化了SPS_HTTP代理，支持较大HTTP头部！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2671'
author: 开源中国
comments: false
date: Mon, 28 Feb 2022 09:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2671'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Proxy 是 golang 实现的高性能 http、https、websocket、tcp、udp、socks5 代理服务器，支持正向代理、反向代理、透明代理、内网穿透、TCP/UDP 端口映射、SSH 中转、TLS 加密传输、协议转换、DNS 防污染智能代理、前置 CDN/Nginx 反代、代理连接重定向、API动态调用上级代理、限速限连接数。提供全平台的命令行版本，友好易用的Windows&Linux&macOS控制面板，强大的安卓版。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>更新内容</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#24292f">1、优化了http/sps代理，新增</span><code>--http-header-buffer</code><span style="background-color:#ffffff; color:#24292f">参数，单位字节，设置读取http头部buffer大小，用来支持当http头部很大的时候的情况，默认是4096。</span><br> <span style="background-color:#ffffff; color:#24292f">2、优化了http/sps代理，新增</span><code>--http-header-timeout</code><span style="background-color:#ffffff; color:#24292f">参数，单位毫秒，设置读取http头部超时时间，默认是1000毫秒。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">更新： v10.7及以后版本，执行：<code>proxy update</code>，即可完成快速更新到最新版。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>特色功能</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li style="text-align:left">链式代理，程序本身可以作为一级代理，如果设置了上级代理那么可以作为二级代理，乃至N级代理。</li> 
 <li>通讯加密，如果程序不是一级代理，而且上级代理也是本程序，那么可以加密和上级代理之间的通讯，采用底层tls高强度加密，安全无特征。</li> 
 <li>智能HTTP代理，HTTPS代理，SOCKS5代理，会自动判断访问的网站是否屏蔽，如果被屏蔽那么就会使用上级代理(前提是配置了上级代理)访问网站;如果访问的网站没有被屏蔽，为了加速访问，代理会直接访问网站，不使用上级代理。</li> 
 <li>域名黑白名单，更加自由的控制网站的访问方式。</li> 
 <li>跨平台性，无论你是widows，linux，还是mac，甚至是树莓派，都可以很好的运行proxy。</li> 
 <li>多协议支持，支持HTTP(S)，TCP，UDP，Websocket，SOCKS5代理。</li> 
 <li>TCP/UDP端口转发。</li> 
 <li>游戏盾，游戏代理，高仿服务器。</li> 
 <li>内网穿透，P2P传输，协议支持TCP和UDP，针对HTTP的优化穿透。</li> 
 <li>SSH中转，HTTP(S)，SOCKS5代理支持SSH中转，上级Linux服务器不需要任何服务端，本地一个proxy即可开心上网。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxtaci%2Fkcp-go" target="_blank">KCP</a>协议支持，HTTP(S)，SOCKS5代理支持KCP协议传输数据，降低延迟，提升浏览体验。</li> 
 <li>动态选择上级代理，通过外部API，HTTP(S)，SOCKS5，SPS代理可以实现基于用户或者IP的限速，连接数限制，动态获取上级。</li> 
 <li>灵活的上级分配，HTTP(S)，SOCKS5，SPS代理可以通过配置文件实现基于用户或者IP的限速，连接数限制，指定上级。</li> 
 <li>反向代理，支持直接把域名解析到proxy监听的ip，然后proxy就会帮你代理访问需要访问的HTTP(S)网站。</li> 
 <li>透明HTTP(S)代理，配合iptables，在网关直接把出去的80，443方向的流量转发到proxy，就能实现无感知的智能路由器代理。</li> 
 <li>协议转换，可以把已经存在的HTTP(S)或SOCKS5或SS代理转换为一个端口同时支持HTTP(S)和SOCKS5和SS代理，转换后的SOCKS5和SS代理如果上级是SOCKS5代理，那么支持UDP功能，同时支持强大的级联认证功能。</li> 
 <li>自定义底层加密传输，http(s)\\\\sps\\\\socks代理在tcp之上可以通过tls标准加密以及kcp协议加密tcp数据，除此之外还支持在tls和kcp之后进行自定义加密，也就是说自定义加密和tls|kcp是可以联合使用的，内部采用AES256加密，使用的时候只需要自己定义一个密码即可。</li> 
 <li>底层压缩高效传输，http(s)\\\\sps\\\\socks代理在tcp之上可以通过自定义加密和tls标准加密以及kcp协议加密tcp数据，在加密之后还可以对数据进行压缩，也就是说压缩功能和自定义加密和tls|kcp是可以联合使用的。</li> 
 <li>安全的DNS代理，可以通过本地的proxy提供的DNS代理服务器与上级代理加密通讯实现安全防污染的DNS查询。</li> 
 <li>负载均衡，高可用，HTTP(S)\\\\SOCKS5\\\\SPS代理支持上级负载均衡和高可用，多个上级重复-P参数即可。</li> 
 <li>指定出口IP，HTTP(S)\\\\SOCKS5\\\\SPS\\\\TCP代理支持客户端用入口IP连接过来的，就用入口IP作为出口IP访问目标网站的功能。如果入口IP是内网IP，出口IP不会使用入口IP</li> 
 <li>支持限速，HTTP(S)\\\\SOCKS5\\\\SPS\\\\TCP代理支持限速。</li> 
 <li> <p style="margin-left:0; margin-right:0">支持限连接数，HTTP(S)\\\\SOCKS5\\\\SPS\\\\TCP代理支持限连接数。</p> </li> 
 <li>SOCKS5代理支持级联认证。</li> 
 <li>证书参数使用base64数据，默认情况下-C，-K参数是crt证书和key文件的路径，如果是base64://开头，那么就认为后面的数据是base64编码的，会解码后使用。</li> 
 <li>支持客户端IP黑白名单，更加安全的控制客户端对代理服务的访问，如果黑白名单同时设置，那么只有白名单生效。socks/http(s)/sps/tcp/udp/dns/内网穿透bridge/内网穿透tbridge，都支持客户端IP黑白名单。</li> 
 <li>端口范围批量监听，HTTP(S)\\\\SOCKS5\\\\SPS\\\\TCP代理支持指定端口范围监听，避免启动过多进程，提高性能。</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">下载地址:</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/snail/proxy/" target="_blank">Gitee</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsnail007%2Fgoproxy" target="_blank">Github</a></p> </li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            