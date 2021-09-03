
---
title: 'Netbox 3.0.1 发布，IP 地址与数据中心管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5132'
author: 开源中国
comments: false
date: Fri, 03 Sep 2021 06:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5132'
---

<div>   
<div class="content">
                                                                                            <p>NetBox 是一个 IP 地址管理（IP address management，IPAM）和数据中心基础设施管理（data center infrastructure management，DCIM）工具。   </p> 
<p>Netbox 3.0.1 现已完成发布，具体更新内容如下：</p> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7041" target="_blank">#7041</a> - 正确格式化从 NAPALM 设备返回的 JSON 配置对象</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7070" target="_blank">#7070</a> - 修复在 UI 中通过前缀最大长度进行过滤时的异常。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7071" target="_blank">#7071</a> - 修复从 device/VM 中删除主 IP 时的异常</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7072" target="_blank">#7072</a> - 修复前缀子对象视图下的表配置</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7075" target="_blank">#7075</a> - 修复自定义字段名称中有空格时的 UI 错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7080" target="_blank">#7080</a> - 修复丢失的图像预览</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7081" target="_blank">#7081</a> - 修复未正确请求和处理分页数据的 UI 错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7082" target="_blank">#7082</a> - 在表中引用无效内容类型时避免异常</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7083" target="_blank">#7083</a> - 正确标记 VM 内存属性</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7084" target="_blank">#7084</a> - 修复在接口上编辑访问 VLAN 时的 KeyError 异常</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7084" target="_blank">#7084</a> - 修复隐藏 VLAN 表单字段错误地包含在表单提交中的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7089" target="_blank">#7089</a> - 修复按内容类型过滤变更日志的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7090" target="_blank">#7090</a> - 批量编辑 cables 时允许在长度字段上 decimal input</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7091" target="_blank">#7091</a> - 确保来自 UI 的 API 请求知道<code>BASE_PATH</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7092" target="_blank">#7092</a> - 修复前缀 IP 地址表上丢失的批量编辑按钮</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7093" target="_blank">#7093</a> - 多选自定义字段过滤器应采用精确匹配</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7096" target="_blank">#7096</a> - 主页链接应该遵循<code>BASE_PATH</code>配置</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7101" target="_blank">#7101</a> - 强制执行<code>MAX_PAGE_SIZE</code>表和 REST API 分页</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7106" target="_blank">#7106</a> - 修复站点物理地址字段上不正确的“Map It”按钮 URL</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7107" target="_blank">#7107</a> - 修复 IP 地址分配的“Assign IP”选项卡中缺少的搜索按钮和搜索结果</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7109" target="_blank">#7109</a> - 确保在 REST API 请求中出现的异常情况的可读性</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7113" target="_blank">#7113</a> - 显示前缀子对象的批量编辑/删除操作</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7123" target="_blank">#7123</a> - 删除空 VRF 字段的“Global”占位符</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Fissues%2F7124" target="_blank">#7124</a> - 修复 API Select 中重复的静态查询参数值</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnetbox-community%2Fnetbox%2Freleases%2Ftag%2Fv3.0.1" target="_blank">https://github.com/netbox-community/netbox/releases/tag/v3.0.1</a></p>
                                        </div>
                                      
</div>
            