
---
title: 'Spring Framework 6.0.0-M3 & 5.3.17 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3181'
author: 开源中国
comments: false
date: Tue, 22 Mar 2022 07:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3181'
---

<div>   
<div class="content">
                                                                                            <p>Spring Framework 6.0.0-M3 & 5.3.17 已发布。</p> 
<p>5.3.17 版本包含 17 项修复和改进，建议在生产环境使用的用户进行升级。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Freleases%2Ftag%2Fv5.3.17" target="_blank">5.3.17 新特性和改进</a></p> 
<ul> 
 <li>改进使用 DataClassRowMapper 时导致在日志中出现"No property found for column"调试信息的情况<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F28179" target="_blank">#28179</a></li> 
 <li>改进在 SpEL 中创建大型数组的诊断方法<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F28145" target="_blank">#28145</a></li> 
 <li>在客户端 REST 测试支持中支持自定义 HTTP 状态<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F28105" target="_blank">#28105</a></li> 
 <li>改进 AsyncRestTemplate 日志过于冗长的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F28049" target="_blank">#28049</a></li> 
 <li>升级依赖：Reactor 2020.0.17 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F28064" target="_blank">#28064</a></li> 
 <li>改进 TestContext 事件的文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F27757" target="_blank">#27757</a></li> 
</ul> 
<p>6.0 的第三个里程碑版本带来了首批从 Spring Native 迁移 AOT(Ahead Of Time) 的工作，为在更广泛的 Spring 生态系统中支持 Spring Native 提供铺垫。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Freleases%2Ftag%2Fv6.0.0-M3" target="_blank">6.0.0 M3 主要变化</a></p> 
<ul> 
 <li>添加表示 RFC 7807 问题详细信息和异常的类型 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F28187" target="_blank">#28187</a></li> 
 <li>更新 AOT 处理，以使用多个 init 或 destroy 方法 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F28151" target="_blank">#28151</a></li> 
 <li>引入 ApplicationContextAotGenerator <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F28150" target="_blank">#28150</a></li> 
 <li>添加 GeneratedType 基础设施 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F28149" target="_blank">#28149</a></li> 
 <li>添加对生成代码的运行时提示的支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F28148" target="_blank">#28148</a></li> 
 <li>用适当的 ResponseSpec 扩展替换 KotlinBodySpec <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F28144" target="_blank">#28144</a></li> 
 <li>添加 GraalVM 原生 JSON 配置生成<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fpull%2F28131" target="_blank">#28131</a></li> 
 <li>支持在测试中编译和运行生成的代码<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-framework%2Fissues%2F28120" target="_blank">#28120</a></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F03%2F17%2Fspring-framework-6-0-0-m3-and-5-3-17-available-now" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            