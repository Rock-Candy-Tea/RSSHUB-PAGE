
---
title: 'Apache APISIX 2.10.0 发布，云原生的微服务 API 网关'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1501'
author: 开源中国
comments: false
date: Sun, 03 Oct 2021 07:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1501'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Apache APISIX 2.10.0 已发布，这是一个动态、实时、高性能的 API 网关，提供负载均衡、动态上游、灰度发布、服务熔断、身份认证、可观测性等丰富的流量管理功能。从其主要功能和特点角度来看，Apache APISIX 可以替代 Nginx 来处理南北流量，也可以扮演 Istio 控制平面和 Envoy 数据平面的角色来处理东西向流量。</span></p> 
<p><span style="background-color:#ffffff; color:#333333"><strong>主要更新内容</strong></span></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#333333">将 'enable_debug' 表单 config.yaml 移动到 debug.yaml</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">在 nginx.conf 中使用新名称自定义 lua_shared_dict</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">取消对 shell 脚本安装的支持</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">添加动态调试模式</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">允许向 APISIX 的方法注入逻辑</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">允许配置回退 SNI</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">在 ip 匹配中支持 CIDR</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">允许路由从服务继承主机</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">支持配置节点监听地址</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">为 hmac auth 插件添加验证请求正文</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">支持镜像请求 sample_ratio</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">添加黑名单和消息</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">添加集群名称支持</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">添加 required_acks 选项</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">添加不区分大小写的开关</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">正确匹配主机和路径</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">区分具有相同名称但在不同组或命名空间中的服务</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">请求失败时继续处理其他服务</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">以不区分大小写的方式匹配 sni</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">不应覆盖默认的 keepalive 值</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">在服务发现中优先选择 SRV</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">延迟后重试连接</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">避免在域的 IP 更改时复制不需要的数据</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">当 plugin_config 改变时恢复插件</span></li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202109.mbox%2F%253CCAADJU12nZsvSond3hG5Z8JiDF3kC_yxjmGnUHxgorXGGemVnkg%40mail.gmail.com%253E" target="_blank">更新公告</a></span></p>
                                        </div>
                                      
</div>
            