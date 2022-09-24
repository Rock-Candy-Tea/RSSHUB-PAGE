
---
title: 'Spring Batch 5.0.0-M6 和 4.3.7 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7819'
author: 开源中国
comments: false
date: Sat, 24 Sep 2022 07:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7819'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Spring Batch 5.0.0-M6 和 4.3.7 已发布。</p> 
<blockquote> 
 <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Spring Batch 是一个轻量级且功能全面的批处理框架，使用 Spring 和 Java 编写离线和批处理应用程序，旨在为开发对企业系统日常运行至关重要的批处理应用程序提供支持。</span></p> 
</blockquote> 
<p>Spring Batch 5.0.0-M6 的更新内容集中在优化 Spring Batch 的配置过程，让它更加灵活和直观。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-batch%2Freleases%2Ftag%2F5.0.0-M6" target="_blank">详情查看 release note</a>。</p> 
<p>4.3.7 则是常规的补丁更新，可用来替代 4.3.6，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fspring-projects%2Fspring-batch%2Freleases%2Ftag%2F4.3.7" target="_blank">详情查看 release note</a>。</p> 
<p><strong>Spring Batch 5.0.0-M6 主要变化</strong></p> 
<ul> 
 <li><strong>EnableBatchProcessing 引入新注解属性</strong></li> 
</ul> 
<p><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span>在此版本中，<code>@EnableBatchProcessing</code>注解引入了新属性，用于指定应使用哪些组件和参数来配置 Batch 基础设施 bean。例如，现在可以指定 Spring Batch 应在作业仓库中配置的数据源和事务管理器。下面的代码段展示了进行此类配置的新方法：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<pre><code class="language-xml">@Configuration
@EnableBatchProcessing(dataSourceRef = "batchDataSource", transactionManagerRef = "batchTransactionManager")
public class MyJobConfiguration &#123;

@Bean
public Job job(JobRepository jobRepository) &#123;
return new JobBuilder("myJob", jobRepository)
 //define job flow as needed
 .build();
&#125;

&#125;</code></pre> 
<ul> 
 <li><strong>用于基础设施 Beans 的新配置类</strong></li> 
</ul> 
<p>在此版本中，可以使用一个名为<code>DefaultBatchConfiguration</code>的新配置类，作为配置基础设施 bean <code>@EnableBatchProcessing</code>的替代方法。此类为基础设施 bean 提供默认配置，可以根据需要对其进行自定义。下面的代码片段展示了此类的典型用法：</p> 
<pre><code class="language-xml">@Configuration
class MyJobConfiguration extends DefaultBatchConfiguration &#123;

@Bean
public Job job(JobRepository jobRepository) &#123;
return new JobBuilder("myJob", jobRepository)
//define job flow as needed
.build();
&#125;

&#125;</code></pre> 
<ul> 
 <li><strong>JobExplorer 和 JobOperator 中的事务支持</strong></li> 
</ul> 
<p>此版本在通过<code>JobExplorerFactoryBean</code>在创建<code>JobExplorer</code>时引入了事务支持。开发者现在可以在查询 Batch 元数据时指定使用哪个事务管理器来驱动已准备就绪的事务。此外还可以自定义事务属性。同样的事务支持也通过一个新的工厂Bean (<code>JobOperatorFactoryBean</code>) 被添加到<code>JobOperator</code>中。</p> 
<p><strong>升级依赖</strong></p> 
<ul> 
 <li>Upgrade to Spring Framework 6.0.0-M6</li> 
 <li>Upgrade to Spring Data 2022.0.0-M6</li> 
 <li>Upgrade to Spring Integration 6.0.0-M5</li> 
 <li>Upgrade to Spring AMQP 3.0.0-M4</li> 
 <li>Upgrade to Spring for Apache Kafka 3.0.0-M6</li> 
 <li>Upgrade to Spring Retry 2.0.0-M1</li> 
 <li>Upgrade to Spring LDAP 3.0.0-M4</li> 
 <li>Upgrade to Micrometer 1.10.0-M5</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F09%2F22%2Fspring-batch-5-0-0-m6-and-4-3-7-are-out" target="_blank">发布公告</a>。</p>
                                        </div>
                                      
</div>
            