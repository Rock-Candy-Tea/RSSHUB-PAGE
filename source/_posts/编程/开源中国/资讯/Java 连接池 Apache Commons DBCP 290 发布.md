
---
title: 'Java 连接池 Apache Commons DBCP 2.9.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4396'
author: 开源中国
comments: false
date: Fri, 06 Aug 2021 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4396'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Commons DBCP 2.9.0 现已发布，这是一个次要版本，主要包含 bug 修复和改进。DBCP（Database Connection Pool）是一个依赖 Jakarta commons-pool 对象池机制的数据库连接池，Tomcat 的数据源使用的就是 DBCP。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>添加并重新使用 Constants.KEY_USER 和 Constants.KEY_PASSWORD</li> 
 <li>添加并重新使用 DriverAdapterCPDS.&#123;get|set&#125;DurationBetweenEvictionRuns()，弃用 &#123;get|set&#125;TimeBetweenEvictionRunsMillis(long)</li> 
 <li>修复 TestSynchronizationOrder.testInterposedSynchronization 上的测试随机失败</li> 
 <li>ManagedConnection 必须在事务完成后清除其缓存状态</li> 
 <li>使用 abort 而不是 close 来清理废弃的连接</li> 
 <li>性能增强：以零数组大小调用 toArray</li> 
 <li>避免由于 JMX 暴露密码</li> 
 <li>DataSource 实现没有正确实现 Wrapper 接口</li> 
 <li>DataSourceConnectionFactory.getUserPassword() 可以通过返回 DataSourceConnectionFactory.userPassword 来暴露内部表示</li> 
 <li>使用 Collections.synchronizedList() 而不是 Vector</li> 
 <li>更新 PoolKey#toString() 以避免泄露用户名</li> 
 <li>内部包私有 UserPassKey 类将其用户名存储为 char[] </li> 
 <li>BasicDataSource 应该动态测试安全管理器的存在，而不是在初始化时测试一次</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202108.mbox%2F%253CCACZkXPzHzr32k%3Dyp_rLsy623Wu6c2kr%2Bhyn30HxaAUER-vbZsw%40mail.gmail.com%253E" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            