
---
title: 'Spring Batch 5.0 M1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5701'
author: 开源中国
comments: false
date: Sat, 22 Jan 2022 07:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5701'
---

<div>   
<div class="content">
                                                                                            <p>Spring Batch 5.0 的首个里程碑版本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F01%2F19%2Fspring-batch-5-0-m1-released" target="_blank">已发布</a>，新版本可从 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo.spring.io%2Fmilestone" target="_blank">https://repo.spring.io/milestone</a> 获取。</p> 
<p><span style="background-color:#ffffff; color:#333333">Spring Batch 是一个轻量级且功能全面的批处理框架，使用 Spring 和 Java 编写离线和批处理应用程序，旨在为开发对企业系统日常运行至关重要的批处理应用程序提供支持。</span></p> 
<p>此版本主要变化：</p> 
<ul> 
 <li>将最低的 Java 版本升级至 Java 17+</li> 
 <li>迁移至 Jakarta EE 9 API</li> 
 <li>升级依赖项至主要版本，如 Spring Framework 6.0</li> 
 <li>为事务隔离级别类型添加带有强类型参数的 setter</li> 
 <li>将 getDataSource 方法添加到 DefaultBatchConfigurer</li> 
 <li>弃用使用默认方法实现接口的支持类</li> 
 <li><span style="background-color:#ffffff; color:#24292f">简化 GET_LAST_STEP_EXECUTION</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">在 JdbcJobInstanceDao 中将 setJobIncrementer 重命名为 setJobInstanceIncrementer</span></li> 
 <li>修复 Oracle 创建新批处理作业时出错的问题</li> 
 <li><span style="background-color:#ffffff; color:#24292f">将 Assert.assertThat 替换为 MatcherAssert.assertThat</span></li> 
 <li><span style="background-color:#ffffff; color:#24292f">避免在 ExecutionContextSerializer 测试中进行字符串转换</span></li> 
 <li>……</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-batch%2Freleases%2Ftag%2F5.0.0-M1" target="_blank">完整变更内容查看 Changelog</a>。</p> 
<p>此外，开发团队还通过此次更新主要版本的机会删除了废弃的 API，并修复了一些需要向后兼容的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-batch%2Fwiki%2FSpring-Batch-5.0-Migration-Guide" onclick="s_objectID='apps_scodevmw : migration guide : 75'" target="_blank">迁移指南</a>包含了关于这些变化的更多细节，并提供了升级说明。</p>
                                        </div>
                                      
</div>
            