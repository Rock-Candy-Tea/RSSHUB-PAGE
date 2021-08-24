
---
title: 'Spring系列之多个数据源配置'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/589b3fcea5244211ad6890dc7d09774a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 22:15:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/589b3fcea5244211ad6890dc7d09774a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>在上篇文章讲到了如何配置单数据源，但是在实际场景中，会有需要配置多个数据源的场景，比如说，我们在支付系统中，单笔操作（包含查询、插入、新增）中需要操作主库，在批量查询或者对账单查询等对实时性要求不高的场景，需要使用读库来操作，依次来减轻数据库的压力。那么我们如何配置多数据源？</p>
<p><strong>这里还是基于springboot应用的情况下，我们看一下怎么配置。</strong><br>
因为SpringBoot会实现自动配置，但是SpringBoot并不知道我们的业务场景分别要使用哪一个数据源，因此我们需要把相关的自动配置关闭。</p>
<p><strong>首先，生成项目骨架，引入相应的依赖</strong></p>
<pre><code class="hljs language-xml copyable" lang="xml">  <span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>org.springframework.boot<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>spring-boot-starter-jdbc<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
 <span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>org.springframework.boot<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>spring-boot-starter-actuator<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
 <span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>org.springframework.boot<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>spring-boot-starter-web<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
 <span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>

 <span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.h2database<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>h2<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">scope</span>></span>runtime<span class="hljs-tag"></<span class="hljs-name">scope</span>></span>
 <span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>org.projectlombok<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>lombok<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">optional</span>></span>true<span class="hljs-tag"></<span class="hljs-name">optional</span>></span>
 <span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>org.springframework.boot<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>spring-boot-starter-test<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">scope</span>></span>test<span class="hljs-tag"></<span class="hljs-name">scope</span>></span>
 <span class="hljs-tag"></<span class="hljs-name">dependency</span>></span>
 ```
**然后，在Application排除自动装配类**   

```java
@SpringBootApplication(exclude = &#123; DataSourceAutoConfiguration.class,DataSourceTransactionManagerAutoConfiguration.class,JdbcTemplateAutoConfiguration.class&#125;)
@Slf4j
public class MultiDataSourceDemoApplication &#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，我们排除了DataSourceAutoConfiguration、DataSourceTransactionManagerAutoConfiguration、JdbcTemplateAutoConfiguration三个类，然后就可以自己定义DataSource了。</p>
<p><strong>配置数据源</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">//第一个数据源</span>
<span class="hljs-meta">@Bean</span>
<span class="hljs-meta">@ConfigurationProperties("first.datasource")</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> DataSource <span class="hljs-title">firstDataSource</span><span class="hljs-params">()</span> </span>&#123;
<span class="hljs-keyword">return</span> DataSourceBuilder.create().build();
&#125;

<span class="hljs-meta">@Bean</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> JdbcTemplate <span class="hljs-title">firstJdbcTemplate</span><span class="hljs-params">()</span> </span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> JdbcTemplate(firstDataSource());
&#125;


<span class="hljs-meta">@Bean</span>
<span class="hljs-meta">@Resource</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> PlatformTransactionManager <span class="hljs-title">firstTxManager</span><span class="hljs-params">(DataSource firstDataSource)</span> </span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> DataSourceTransactionManager(firstDataSource);
&#125;

<span class="hljs-comment">//第二个数据源</span>
<span class="hljs-meta">@Bean</span>
<span class="hljs-meta">@ConfigurationProperties("second.datasource")</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> DataSource <span class="hljs-title">secondDataSource</span><span class="hljs-params">()</span> </span>&#123;
<span class="hljs-keyword">return</span> DataSourceBuilder.create().build();
&#125;

<span class="hljs-meta">@Bean</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> JdbcTemplate <span class="hljs-title">secondJdbcTemplate</span><span class="hljs-params">()</span> </span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> JdbcTemplate(secondDataSource());
&#125;

<span class="hljs-meta">@Bean</span>
<span class="hljs-meta">@Resource</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> PlatformTransactionManager <span class="hljs-title">secondTxManager</span><span class="hljs-params">(DataSource secondDataSource)</span> </span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> DataSourceTransactionManager(secondDataSource);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>application.properties的配置项信息</strong></p>
<pre><code class="hljs language-xml copyable" lang="xml">management.endpoints.web.exposure.include=*
spring.output.ansi.enabled=ALWAYS

first.datasource.jdbc-url=jdbc:mysql://localhost:3306/first
first.datasource.username=root
first.datasource.password=xxx
second.datasource.jdbc-url=jdbc:mysql://localhost:3306/second
second.datasource.username=root
second.datasource.password=xxx
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>看一下表结构和数据</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/589b3fcea5244211ad6890dc7d09774a~tplv-k3u1fbpfcp-watermark.image" alt="file" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02b8ff11db1246f1940ad6517bc062a9~tplv-k3u1fbpfcp-watermark.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>运行测试代码：</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Test</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">testMutilDataSource</span><span class="hljs-params">()</span></span>&#123;
firstJdbcTemplate.queryForList(<span class="hljs-string">"SELECT * FROM test1"</span>)
.forEach(row -> log.info(<span class="hljs-string">"记录："</span>+row.toString()));

secondJdbcTemplate.queryForList(<span class="hljs-string">"SELECT * FROM test2"</span>)
.forEach(row -> log.info(<span class="hljs-string">"记录："</span>+row.toString()));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>我们看一下运行效果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aaf7be96b0b047cdb6268f48e6b9282d~tplv-k3u1fbpfcp-watermark.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以看到，两个数据源都初始化成功了，并且各自数据源执行的结果准确。</p>
<blockquote>
<p>上面的方式没有集成Mybatis，使用的是jdbcTemplate，网络上还有很多配置方式，比如动态选择数据源，大同小异，不过笔者还是建议不同的业务单独指定数据源，容易维护。
我们已经演示了简单的单数据源和多数据源的配置方式，我们下一篇文章将讲一下，SpringBoot默认的连接池HikariCP。</p>
</blockquote></div>  
</div>
            