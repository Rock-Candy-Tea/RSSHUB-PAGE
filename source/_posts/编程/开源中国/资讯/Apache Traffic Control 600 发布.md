
---
title: 'Apache Traffic Control 6.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3150'
author: 开源中国
comments: false
date: Fri, 15 Oct 2021 06:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3150'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Apache Traffic Control 可以用于建立一个大规模的内容交付网络。围绕 Apache Traffic Server 作为缓存软件，Traffic Control 实现了现代 CDN 的所有核心功能。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Apache Traffic Control 6.0.0 更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新增</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F4982" target="_blank">#4982</a> 增加了支持按服务器类型和配置文件排队更新的功能</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F5412" target="_blank">#5412</a> 在用户 API（<span> </span><code>GET /user/current、GET /users、GET /user?id=</code><span> </span>）响应有效载荷中增加了最后认证时间</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F5451" target="_blank">#5451</a> 在用户 API 的响应有效载荷中增加了变更日志计数，在日志 API 中增加了查询参数（用户名）。</li> 
 <li><strong>CDN Locks</strong>: 一个操作级别的用户现在可以锁定一个 CDN，以防止其他用户试图同时修改它。</li> 
 <li><strong>Postgres Traffic Vault backend</strong>: Traffic Ops 现在支持 Postgres Traffic Vault 后端，可选择从 HashiCorp Vault 获取 Traffic Vault 的密匙</li> 
 <li>Python client: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fpull%2F5611" target="_blank">#5611</a> 添加了 server_detail 端点</li> 
 <li>将 Postinstall 脚本移植到 Python，Perl 版本已被移至<span> </span><code>install/bin/_postinstall.pl</code>并被弃用，将在未来版本中移除。 CDN-in-a-Box。使用Postinstall脚本生成配置文件</li> 
 <li>CDN-in-a-Box: 使用 Postinstall 脚本生成配置文件</li> 
 <li>Traffic Ops: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F3577" target="_blank">#3577</a> - 为 servercheck API 增加了一个查询参数（服务器 host_name 或 ID）</li> 
 <li>……</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcve.mitre.org%2Fcgi-bin%2Fcvename.cgi%3Fname%3DCVE-2021-42009" target="_blank"><strong>CVE-2021-42009</strong></a>: 发送到<span> </span><code>/deliveryservices/request</code><span> </span>Traffic Ops API 端点的有效载荷中的 customer name 不能再包含除字母数字、<span> </span><code>@</code>、<span> </span><code>！</code>、<span> </span><code>#</code>、<span> </span><code>$</code>、<span> </span><code>%</code>、<span> </span><code>^</code>、<span> </span><code>&</code>、<span> </span><code>*</code>、<span> </span><code>（、）</code>、<span> </span><code>[、]</code>、<span> </span><code>.</code><span> </span>和<span> </span><code>-</code>。这修复了一个允许电子邮件内容注入的漏洞。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F2471" target="_blank">#2471</a> - 一个 PR 检查，确保添加的 db 迁移文件是最新的。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F5609" target="_blank">#5609</a> - 修正了 GET /servercheck 过滤器的一个额外的查询参数。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F5954" target="_blank">#5954</a> - Traffic Ops HTTP 响应写入错误被忽略</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F6104" target="_blank">#6104</a> - PUT /api/x/federations 只遵循请求有效载荷中的第一项内容</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F5407" target="_blank">#5407</a> - 确保你不能添加两个内容相同的服务器</li> 
 <li>……</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">变更</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>更新了 Traffic Ops Python 客户端到 3.0</li> 
 <li>apache/trafficcontrol 现在是一个Go模块</li> 
 <li>更新了 Traffic Ops 支持的数据库版本，从 PostgreSQL 9.6 到 13.2</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F3342" target="_blank">#3342</a> - 更新了<span> </span><code>db/admin</code><span> </span>工具，以使用 Migrate 而不是Goose，并将迁移转换为 Migrate 格式。</li> 
 <li>重构了 Traffic Ops - Traffic Vault 的集成，以更容易地支持新的 Traffic Vault 后端开发。</li> 
 <li>……</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Freleases%2Ftag%2FRELEASE-6.0.0" target="_blank">https://github.com/apache/trafficcontrol/releases/tag/RELEASE-6.0.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            