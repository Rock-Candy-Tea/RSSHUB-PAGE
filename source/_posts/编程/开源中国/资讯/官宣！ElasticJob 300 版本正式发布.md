
---
title: '官宣！ElasticJob 3.0.0 版本正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-33eae89f3313f62dfb4324969e64da24c89.png'
author: 开源中国
comments: false
date: Wed, 07 Jul 2021 03:54:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-33eae89f3313f62dfb4324969e64da24c89.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>ElasticJob 是面向互联网生态和海量任务的分布式调度解决方案，由两个相互独立的子项目 ElasticJob-Lite 和 ElasticJob-Cloud 组成。它通过弹性调度、资源管控、以及作业治理的功能，打造一个适用于互联网场景的分布式调度解决方案，并通过开放的架构设计，提供多元化的作业生态。ElasticJob 的各个产品使用统一的作业 API，开发者仅需一次开发，即可随意部署。</p> 
<p>在经过 alpha、beta、RC1 版本的打磨后，我们宣布 ElasticJob 3.0.0 版本正式发布！这是 ElasticJob 项目自 2020 年 5 月 28 日重启并成为 Apache ShardingSphere 子项目以来的第一个正式版本。</p> 
<p>相比 3.0.0-RC1 版本，ElasticJob 3.0.0 正式版优化了以下方面：</p> 
<h2><strong>漏洞修复</strong></h2> 
<ol> 
 <li> <p>修复 failover 在分布式部署的情况下可能不生效的问题</p> </li> 
 <li> <p>修复 ReconcileService 在作业关闭后没有正确关闭的问题</p> </li> 
</ol> 
<h2><strong>增强</strong></h2> 
<ol> 
 <li> <p>错误处理器模块-邮件通知增加 SMTP SSL trust 配置参数</p> </li> 
</ol> 
<h2><strong>依赖调整</strong></h2> 
<ol> 
 <li> <p>ElasticJob Spring Boot Starter 模块中的 spring-boot-starter-jdbc 调整为非必需</p> </li> 
</ol> 
<p>中央仓库：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsearch.maven.org%2Fsearch%3Fq%3Dg%3Aorg.apache.shardingsphere.elasticjob%2520AND%2520v%3A3.0.0" target="_blank">https://search.maven.org/search?q=g:org.apache.shardingsphere.elasticjob%20AND%20v:3.0.0</a></p> 
<p>下载链接：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshardingsphere.apache.org%2Felasticjob%2Fcurrent%2Fen%2Fdownloads%2F" target="_blank">https://shardingsphere.apache.org/elasticjob/current/en/downloads/</a></p> 
<p>更新日志：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fshardingsphere-elasticjob%2Fblob%2Fmaster%2FRELEASE-NOTES.md" target="_blank">https://github.com/apache/shardingsphere-elasticjob/blob/master/RELEASE-NOTES.md</a></p> 
<p>项目地址：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fshardingsphere-elasticjob" target="_blank">https://github.com/apache/shardingsphere-elasticjob</a></p> 
<h2><strong>社区建设</strong></h2> 
<p>自 ElasticJob 3.0.0-RC1 发布后，共有 11 位 Contributor 的 26 个 PR 被合并，感谢大家的贡献与支持。</p> 
<p><img alt height="500" src="https://oscimg.oschina.net/oscnet/up-33eae89f3313f62dfb4324969e64da24c89.png" width="1000" referrerpolicy="no-referrer"></p> 
<p>相较 ElasticJob 2.x 版本而言，ElasticJob 3.0.0 对内核进行了大量的重构和解耦，并扩充了一系列的生态对接，例如开箱即用的企业微信或钉钉作业出错通知。后续我们将对 ElasticJob 3.0.0 进行详细技术文章解读，欢迎大家的持续关注！</p> 
<p>欢迎点击“<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshardingsphere.apache.org%2Felasticjob%2Fcurrent%2Fen%2Fdownloads%2F" target="_blank">链接</a>”下载使用。</p>
                                        </div>
                                      
</div>
            