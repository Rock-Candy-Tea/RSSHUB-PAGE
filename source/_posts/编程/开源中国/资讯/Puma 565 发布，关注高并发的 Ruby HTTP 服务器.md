
---
title: 'Puma 5.6.5 发布，关注高并发的 Ruby HTTP 服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4839'
author: 开源中国
comments: false
date: Wed, 24 Aug 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4839'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px"><span style="color:#333333">Puma 是一个简单、快速、线程化并且关注高并发的 HTTP 1.1 服务器，适用于开发和生产中的 Ruby/Rack 应用。</span></p> 
<p style="margin-left:0px">Puma 5.6.5 发布了，这是一个修复版本，带来如下变更：</p> 
<ul> 
 <li>NullIO#close 应该返回 false  [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2883" target="_blank">#2883</a> ]</li> 
 <li>Puma::ControlCLI - 允许将 refork 命令作为请求发送 [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2868" target="_blank">#2868</a> ]，[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2866" target="_blank">#2866</a> ]</li> 
 <li>[jruby] 修复 TLS 验证挂起  ([ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2890" target="_blank">#2890</a> ], [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2729" target="_blank">#2729</a> ])</li> 
 <li>extconf.rb - 如果使用 '--with-openssl-dir'，则不使用 pkg_config('openssl')  [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2885" target="_blank">#2885</a> ], [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2839" target="_blank">#2839</a> ]</li> 
 <li>MiniSSL - 检测 SSL_CTX_set_dh_auto  [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2864" target="_blank">#2864</a> ], [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2863" target="_blank">#2863</a> ]</li> 
 <li>修复 rack.after_reply 异常中断连接[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2861" target="_blank">#2861</a> ]，[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2856" target="_blank">#2856</a> ]</li> 
 <li>转义 SSL 证书和文件名 [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2855" target="_blank">#2855</a> ]</li> 
 <li>如果 SSL 证书或密钥无效  [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2848" target="_blank">#2848</a> ]</li> 
 <li>如果用户无法读取 SSL 证书或密钥，则会失败 [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2847" target="_blank">#2847</a> ]</li> 
 <li>在 LibreSSL 3.5 中使用 Opaque DH 修复构建。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2838" target="_blank">#2838</a> ]</li> 
 <li>在 USR2 之后发出 TERM 时，删除预先存在的套接字文件（如果 puma 在集群模式下运行）[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2817" target="_blank">#2817</a> ]</li> 
 <li>修复 Puma::StateFile#load 不兼容等情况 [ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2810" target="_blank">#2810</a> ]</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Freleases%2Ftag%2Fv5.6.5" target="_blank">https://github.com/puma/puma/releases/tag/v5.6.5</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            