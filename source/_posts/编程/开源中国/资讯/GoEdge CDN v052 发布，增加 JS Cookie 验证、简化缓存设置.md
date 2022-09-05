
---
title: 'GoEdge CDN v0.5.2 发布，增加 JS Cookie 验证、简化缓存设置'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c1a36d3a1b69a9cc5fc276de445e9af7090.png'
author: 开源中国
comments: false
date: Mon, 05 Sep 2022 09:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c1a36d3a1b69a9cc5fc276de445e9af7090.png'
---

<div>   
<div class="content">
                                                                                            <p><strong style="color:#333333">GoEdge</strong><span style="background-color:#ffffff; color:#333333"><span> </span>是一款可以帮你快速构建 CDN & WAF 平台的工具，支持 HTTP、HTTPS、Websocket、TCP、TLS、UDP、PROXY Protocol、IPv6、WAF 等特性，支持多个第三方 DNS 服务</span><br> <br> <img alt height="352" src="https://oscimg.oschina.net/oscnet/up-c1a36d3a1b69a9cc5fc276de445e9af7090.png" width="600" referrerpolicy="no-referrer"></p> 
<p style="color:#24292f; text-align:start">GoEdge v0.5.2主要更新IP库、增加JS Cookie验证、简化缓存条件设置等。</p> 
<h2 style="text-align:start">EdgeAdmin</h2> 
<ul> 
 <li><strong>内置新版IP库，更新了最新的免费IP数据</strong></li> 
 <li><strong>WAF动作中增加Javascript Cookie验证</strong></li> 
 <li>WAF cc2阈值设置太低时提示用户“当前阈值设置的太低，有可能会影响用户正常访问”</li> 
 <li><strong>DDoS防护增加单IP TCP新连接速率黑名单，增加秒级连接速率限制</strong></li> 
 <li><strong>可以修改某个服务的CNAME</strong>，只要不跟其他服务的CNAME冲突即可</li> 
 <li><strong>简化缓存条件设置</strong>，现在不再需要层层弹窗就可设置缓存条件</li> 
 <li>服务列表中带宽使用新的算法</li> 
 <li>对运行日志和IP名单进行操作时，及时更新左侧菜单Badge数字</li> 
 <li>连接API时，自动将本地的API节点地址转换为回路地址<span> </span><code>127.0.0.1</code>，适用于将EdgeAdmin和EdgeAPI安装在同一服务器的场景</li> 
 <li>自动折叠服务设置中的访问日志中多个选项，降低配置复杂度</li> 
 <li>浏览访问日志时自动用点符号标记有数据的分表，方便管理员知悉哪些分表有相关数据</li> 
 <li>节点运行日志可以按照节点整体设置为已读</li> 
 <li>对缓存策略中的缓存句柄增加设置警告</li> 
 <li>创建用户的时候，可以设置开通默认功能还是全部功能</li> 
 <li>将“访问控制”修改为“访问鉴权”</li> 
 <li>新建WAF策略时，默认不启用SQL注释，减少错误检测</li> 
</ul> 
<h2 style="text-align:start">EdgeAPI</h2> 
<ul> 
 <li>提升访问日志、指标统计等处数据写入速度</li> 
</ul> 
<h2 style="text-align:start">EdgeNode</h2> 
<ul> 
 <li><strong>大幅提升缓存索引管理性能</strong></li> 
 <li><strong>将IP加入黑名单时，自动关闭此IP相关连接</strong></li> 
 <li>使用新版IP库，大幅提升IP库查询性能</li> 
 <li>WAF“标签”动作匹配之后可以继续尝试匹配别的分组中的规则集；以往是匹配到“标签”动作后，不再继续往下匹配</li> 
 <li>WAF优化Captcha失败计数器；以往是多个URL累计，现在改成单个URL累计，防止因为单个URL附加资源js、css等触发Captcha而引起意外的超过最大失败次数</li> 
 <li><strong>修复HTTPS连接无法记录带宽的问题</strong>，优化带宽计算方法</li> 
 <li>增加edge-node bandwidth命令查看服务实时带宽</li> 
 <li>修复HTTPS服务无法正确设置Linger的问题，WAF和其他请求关闭连接时将更加快速</li> 
 <li>如果系统安装了ntpdate，则自动尝试利用ntpdate同步时间</li> 
 <li>优化IP名单锁，避免IP列表查询阻塞</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#24292f">下载：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a><br> <span style="background-color:#ffffff; color:#24292f">文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs" target="_blank">https://goedge.cn/docs</a></p>
                                        </div>
                                      
</div>
            