
---
title: 'Spring Batch 5.0.0-M5 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1298'
author: 开源中国
comments: false
date: Sat, 27 Aug 2022 07:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1298'
---

<div>   
<div class="content">
                                                                                            <p>这个里程碑的主要主题是改善 Spring Batch 的测试支持。</p> 
<h3>测试工具配置更新</h3> 
<p>到 4.3 版本为止， <code>JobLauncherTestUtils</code> 用来自动连接被测 Job，目的是为了方便测试设置。但如果在测试上下文中定义了多个 Job 呢？如果根本就没有定义 Job beans 呢？因此，虽然这种自动布线在大多数情况下是很方便的，但在上述情况下，它被证明会引起一些问题。在这个版本中，根据社区的反馈，我们决定删除 <code>JobLauncherTestUtils</code> 中任何作业的自动接线。</p> 
<h2>迁移到 JUnit Jupiter</h2> 
<p>在这个里程碑式的版本中，Spring Batch 的整个测试套件被迁移到了 JUnit 5。虽然这并不直接影响最终用户，但它有助于Batch团队以及社区贡献者使用下一代的 JUnit 来编写更好的测试。</p> 
<h2>改进的文档</h2> 
<p>在这个里程碑式的版本中，文档被更新为使用 Spring Asciidoctor 后端。为了与其他项目保持一致，在这个版本中，Spring Batch 的参考文档也更新为使用这个后端。</p> 
<h2>弃用和 API 变化</h2> 
<p>这个版本包括一些弃用和 API 变化。</p> 
<h3>弃用</h3> 
<p>这个里程碑式的版本引入了以下的弃用。</p> 
<ul> 
 <li>Hibernate 项目读取器和项目写入器被弃用，转而使用基于 JPA 的项目</li> 
 <li><code>org.springframework.batch.test.AssertFile</code> 实用程序类被弃用，转而使用现代测试库提供的类似实用程序</li> 
</ul> 
<h3>API 变化</h3> 
<p>在这个版本中，在 <code>ItemWriter</code> 接口中引入了一个突破性变化。</p> 
<pre><code>public interface ItemWriter<T> &#123;

-- void write(List<? extends T> items) throws Exception;
++ void write(Chunk<? extends T> items) throws Exception;

&#125;
</code></pre> 
<h2>依赖升级</h2> 
<p>主要的依赖已经升级到了以下版本：</p> 
<ul> 
 <li>升级到 Spring Framework 6.0.0-M5</li> 
 <li>升级到 Spring Data 2022.0.0-M5</li> 
 <li>升级到 Spring Integration 6.0.0-M4</li> 
 <li>升级到 Spring AMQP 3.0.0-M3</li> 
 <li>升级到 Spring for Apache Kafka 3.0.0-M5</li> 
 <li>升级至 Micrometer 1.10.0-M4</li> 
 <li>升级到 Hibernate 6.1.2.Final</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2022%2F08%2F24%2Fspring-batch-5-0-0-m5-is-available-now" target="_blank">https://spring.io/blog/2022/08/24/spring-batch-5-0-0-m5-is-available-now</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            