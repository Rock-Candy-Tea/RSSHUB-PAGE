
---
title: 'Kratos v2.2.2 发布，bilibili 开源的 Go 微服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1878'
author: 开源中国
comments: false
date: Sun, 08 May 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1878'
---

<div>   
<div class="content">
                                                                                            <p>Kratos 是哔哩哔哩开源的轻量级 Go 微服务框架，包含大量微服务相关框架及工具。目前 Kratos v2..2.2 已发布，带来如下改动：</p> 
<ul> 
 <li>feat: <span style="color:#24292f">支持 </span>consul <span style="color:#24292f">注册表中的非 kratos 实例</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1892" target="_blank">#1892</a></li> 
 <li>fix: starter parent ctx   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1895" target="_blank">#1895</a></li> 
 <li>feat(contrib): 添加 eureka 注册表 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fissues%2F1792" target="_blank">#1792</a>)  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1793" target="_blank">#1793</a></li> 
 <li>feat(log): <span style="color:#24292f">仅在 Debug 级别时记录加载配置 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1899" target="_blank">#1899</a></li> 
 <li>fix(log): <span style="color:#24292f">FilterFunc keyvals 丢失记录器前缀 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1901" target="_blank">#1901</a></li> 
 <li>fix(log): GoGo Protobuf 中的输入验证不正确 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fadvisories%2FGHSA-c3h9-896r-86jm" target="_blank">CVE-2021-3121</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1902" target="_blank">#1902</a></li> 
 <li>fix(transport): <span style="color:#24292f">修复请求未正确传递的问题</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1906" target="_blank">#1906</a></li> 
 <li>feat(transport): <span style="color:#24292f">为 gRPC 添加 JSON 编解码器</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1908" target="_blank">#1908</a></li> 
 <li>fix(cmd): <span style="color:#24292f">修复 lint 问题</span>  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1919" target="_blank">#1919</a></li> 
 <li>feat(registry): consul 客户端添加 DeregisterCriticalServiceAfter 选项  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1917" target="_blank">#1917</a></li> 
 <li>feat: <span style="color:#24292f">为 statck 跟踪添加错误原因</span>  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1910" target="_blank">#1910</a></li> 
 <li>fix(cmd): 生成错误函数名称和单元测试失败  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1923" target="_blank">#1923</a></li> 
 <li>fix(metadata): 更正元数据日志文本中的函数名称  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1915" target="_blank">#1915</a></li> 
 <li>feat(selector): <span style="color:#24292f">添加节点方案</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1932" target="_blank">#1932</a></li> 
 <li>feat(discovery): 提供一个选项来禁用发现-调试日志 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1942" target="_blank">#1942</a></li> 
 <li>feat: 添加 opensergo 元数据 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1947" target="_blank">#1947</a></li> 
 <li><span style="color:#24292f">修复绑定测试错误</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1950" target="_blank">#1950</a></li> 
 <li>fix(contrib/opensergo): <span style="color:#24292f">修复索引错误</span>  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1951" target="_blank">#1951</a></li> 
 <li>fix: <span style="color:#2e3033">修复路径为 cmd/server 时选择失败的问题</span> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1954" target="_blank">#1954</a></li> 
 <li>fix: 修复 cmd 编号为 1 时 kratos 运行的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1956" target="_blank">#1956</a></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Freleases%2Ftag%2Fv2.2.2" target="_blank">https://github.com/go-kratos/kratos/releases/tag/v2.2.2</a></p>
                                        </div>
                                      
</div>
            