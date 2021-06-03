
---
title: 'Syncthing 1.17.0 发布，连续文件同步工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6011'
author: 开源中国
comments: false
date: Thu, 03 Jun 2021 07:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6011'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Syncthing 是一个免费开源的工具，它能在你的各个网络计算机间同步文件/文件夹，它的同步数据是直接从一个系统中直接传输到另一个系统的，并且它是安全且私密的。</p> 
<p>Syncthing 1.17.0 现已发布，此版本弃用了用于 sync connections 的 TLS 1.2； 默认情况下，Syncthing 仅允许 TLS 1.3 或更高版本用于 sync connections。详情可查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.syncthing.net%2Fadvanced%2Foption-insecure-allow-old-tls-versions.html" target="_blank">insecureAllowOldTLSVersions</a>。具体更新内容如下：</p> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsyncthing%2Fsyncthing%2Fissues%2F7592" target="_blank">#7592</a>：Web UI 不能很好地处理长机器名称</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsyncthing%2Fsyncthing%2Fissues%2F7593" target="_blank">#7593</a> : ChaCha 优先级检测逻辑被破坏</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsyncthing%2Fsyncthing%2Fissues%2F7608" target="_blank">#7608</a>：在一个远程上忽略的文件不会同步</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsyncthing%2Fsyncthing%2Fissues%2F7649" target="_blank">#7649</a>：忽略和取消忽略文件后的 local 和 global 状态不正确</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsyncthing%2Fsyncthing%2Fissues%2F7673" target="_blank">#7673</a>：bug：cli 子命令卡在非交互式 shell 上</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsyncthing%2Fsyncthing%2Fissues%2F7677" target="_blank">#7677</a>：UTF-8 规范化在 macOS 上不起作用</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsyncthing%2Fsyncthing%2Fissues%2F7685" target="_blank">#7685</a>：CLI：通过 CLI 添加新设备时出现 strconv.ParseInt 错误</li> 
</ul> 
<p><strong>Enhancements</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsyncthing%2Fsyncthing%2Fissues%2F7471" target="_blank">#7471</a>：改进 UDP hole punching</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsyncthing%2Fsyncthing%2Fissues%2F7580" target="_blank">#7580</a>：改进服务故障的日志记录</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsyncthing%2Fsyncthing%2Fissues%2F7594" target="_blank">#7594</a>：考虑在 sync connections 上取消对 TLS<1.3 的支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsyncthing%2Fsyncthing%2Fissues%2F7600" target="_blank">#7600</a>：配置更新后快速连接到新设备</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsyncthing%2Fsyncthing%2Fissues%2F7636" target="_blank">#7636</a> : 提高 QUIC 性能</li> 
</ul> 
<p>详情可查看更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsyncthing%2Fsyncthing%2Freleases%2Ftag%2Fv1.17.0" target="_blank">https://github.com/syncthing/syncthing/releases/tag/v1.17.0</a></p>
                                        </div>
                                      
</div>
            