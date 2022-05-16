
---
title: 'Apollo 配置中心发布 2.0 版本，支持 Java 17！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-121b4e3d71b4bfd01b0a96fcb03b10ed8dc.png'
author: 开源中国
comments: false
date: Mon, 16 May 2022 08:42:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-121b4e3d71b4bfd01b0a96fcb03b10ed8dc.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0; margin-right:0">『 此次发布是 Apollo 自 1.0.0 以来的又一次大版本更新，凝结了 39 位 Contributor 的贡献，包含了诸如 Java 17 支持、唯一键索引增强、Spring Boot 版本升级等重大更新。』</p> 
<h1 style="margin-left:0px; margin-right:0px">1. Highlights</h1> 
<h3 style="margin-left:0; margin-right:0; text-align:start">Java 17 支持</h3> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">Apollo 客户端和服务端均已支持 Java 8、11 和 17 版本。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">公共 Namespace 列表页</h3> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">Apollo 主页新增了公共 Namespace 列表视图，用户可以在此页面上查看和搜索公共 Namespace。</p> 
<p><img height="1154" src="https://oscimg.oschina.net/oscnet/up-121b4e3d71b4bfd01b0a96fcb03b10ed8dc.png" width="2514" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">灰度发布支持标签</h3> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">灰度规则支持通过标签来标识灰度的实例列表，适用于 IP 不固定的场景如 Kubernetes</p> 
<p><img height="896" src="https://oscimg.oschina.net/oscnet/up-abd9fe838a2ebfd38661dc429df53198d19.png" width="1896" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">配置导入导出功能增强</h3> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">批量配置导入导出功能进行了重新设计并增强。</p> 
<p><img height="1230" src="https://oscimg.oschina.net/oscnet/up-0e51753ae2ddd02c08d7c98f6f2eabaa313.png" width="2336" referrerpolicy="no-referrer"></p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">每个 Namespace 下现也已支持单独导入和导出。</p> 
<p><img height="744" src="https://oscimg.oschina.net/oscnet/up-eeccdfb445cec0de8665450599155b62685.png" width="2498" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">唯一键索引</h3> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">由于软删除的设计，Apollo 之前版本的数据库除主键外没有唯一键约束，在一些并发的情况下可能会遇到重复数据的问题。基于 2.0.0 版本新增的 DeletedAt 列，我们为大多数表都增加了唯一索引。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">Spring Boot 和 Spring Cloud 版本升级</h3> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">Apollo 服务端的 Spring Boot 和 Spring Cloud 分别升级到了 2.6.6 和 2021.0.1 版本。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">不兼容更新 </h3> 
<p style="margin-left:0; margin-right:0">apollo-client 从 2.0.0 版本开始不再支持 Java 1.7 版本，最低的 Java 运行时环境是 1.8。</p> 
<h1 style="margin-left:0px; margin-right:0px">2. What's Changed</h1> 
<h3 style="margin-left:0; margin-right:0; text-align:start">功能增强</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">switch apollo.config-service log from warning to info level by @lonre</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Make Access Key Timestamp check configurable by @nisiyong</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">refactor: let open api more easier to use and development by @Anilople</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat(scripts): use bash to call openapi by @Anilople</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">support search by item by @lepdou</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feature: implement password policies to avoid weak passwords by @WillardHu</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">public namespace basic function by @youabcd</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Extend the gray release capability to support dimensions other than IP by @zcy1010</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">bump to 2.0.0 and drop java 1.7 support by @nobodyiam</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat: add a shortcut to scroll to the top in the dashboard by @NICEXAI</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">change scrollbar css by @zeemood</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">support java 17 by @nobodyiam</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">optimize navbar style by @lepdou</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">add language.png icon by @lepdou</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">support export import config by env by @lepdou</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">support only show difference keys when compare namespace by @lepdou</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">add zookeeper service discovery support(#3557) by @CalebZYC</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">bump guava version to 31.0.1 by @Shoothzj</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Bump client springboot version by @Shoothzj</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">The release history of namespaces that are not properties will also show comments and release times by @klboke</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Allow disable apollo client cache by @Shoothzj</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feature: isCommonlyUsed password check not hardcoded #4018 by @WillardHu</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">canonical zh-cn text by @lepdou</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">optimize create namespace page by @lepdou</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Add Ordered interface to ProviderManager SPI by @darcydai</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Bump xstream from 1.4.18 to 1.4.19 by @dependabot</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Using commons-lang3 to replace commons-lang by @ruanwenjun</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">optimize import/export config by @lepdou</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Configure publish and rollback modal boxes to add scrollbars by @klboke</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">add custom define discovery by @gy09535</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Refactor the soft delete design by @nisiyong</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">upgrade spring boot to 2.6.6 and spring cloud to 2021.0.1 by @nobodyiam</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">upgrade mysql-connector-java to 8.0.28 by @Anilople</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Upgrade flyway to 8.0.5 by @Shoothzj</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Broadcast ConfigChangeEvent using Spring ApplicationEvent @nobodyiam</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">问题修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">Fix issue that the $ symbol is not used when reading shell variables by @ReganHe93</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Fix issue: ingress syntax by @lijiansgit</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">fix helm scripts BUG by @w-a-n-g-s-h-u-n</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Catch LinkageError for ClassLoaderUtil.isClassPresent in case class is present but is failed to load by @nobodyiam</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">fix gray publish refresh item status(#4039) by @CalebZYC</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Fix the issue that property placeholder doesn't work for dubbo reference beans by @lonre</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Fix the NPE occurred when using EnableApolloConfig with Spring 3.1.1 by @nobodyiam</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">fix the json number display issue when it's longer than 16 by @CalebZYC</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">fix update user password failure bug by @lepdou</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Fix bug: associated namespace display incorrect in text view by @darcydai</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">fix import config bug by @lepdou</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">fix the potential data inconsistency issue by @nobodyiam</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">use item.isDeleted to check whether the item is deleted by @nobodyiam</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Fix the apollo portal start failed issue by @nobodyiam</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">其它更新</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">remove ctrip profile by @JaredTan95</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Remove spring dependencies from internal code by @klboke</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">remove ctrip profile dependency. by @Accelerator96</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">fix gpg signing issues when deploying to maven repository with github action by @nobodyiam</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Fixed some code smells in apollo-portal module by @WillardHu</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">clean ctrip profile by @JaredTan95</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Fixed some code smells in apollo-portal module #2 by @WillardHu</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">fix NullPointerException hazard in StringUtils.join(..) method by @WillardHu</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Replace String.format() with newly created class OpenApiPathBuilder by @WillardHu</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Make the constructor of AbstractApolloHttpException implementation class to support string template by @WillardHu</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Removed useless hardcoded Strings in EnvUtils. by @DiegoKrupitza</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">chore: Simplified the Env class in apollo-portal that links to Env enum in apollo-core by @DiegoKrupitza</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Chore: Future-proofed ConfigFileFormat by @DiegoKrupitza</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">ConfigFileFormat#Properties are now fully compatible with themselves by @DiegoKrupitza</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Fix flaky test testGetPropertyNames. by @yyfMichaelYan</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Fix flaky test testAssembleQueryConfigUrl. by @yyfMichaelYan</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Update RelativeDateFormat.java by @xuxiawei</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">chore: change 'ctripcorp' to 'apolloconfig' in .yaml files by @void1104</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Flaky test fields iteration order by @yyfMichaelYan</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">test(apollo-core): PropertiesUtilTest by @youyulan</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">optimization omits unnecessary time conversion by @xuxiawei</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Split helm chart into another repo by @JaredTan95</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">refactor: SpringValueProcessor extract duplicate code by @mghio</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">build: ctripcorp -> apolloconfig in .github/workflows/cla.yml by @Fool-coder</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Add unit tests for Utils by @joshknopp</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Change Copy Right year to 2022 by @Shoothzj</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Adding JUnit. Fixes #3874 by @ayush0407</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Test coverage by @ayush0407</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Test coverage by @ayush0407</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Fix flaky test by @plzdoo</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Update ReleaseMessageServiceWithCacheTest.java by @plzdoo</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Translation of Apollo Official Chinese Document(s) by @misselvexu</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">fix a title indent error by @Alceatraz</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Misc changes by @nobodyiam</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">feat: update secret access key tips by @weiyichao</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Misc changes by @lepdou</p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0">更多内容可以查看 2.0.0 的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapolloconfig%2Fapollo%2Freleases%2Ftag%2Fv2.0.0" target="_blank">Release Note</a>。</p> 
<p style="margin-left:0; margin-right:0">感谢以下贡献者对此版本的贡献(排名不分先后)</p> 
<p style="margin-left:0; margin-right:0; text-align:left">@ReganHe93 @lonre @JaredTan95 @nisiyong @klboke @Accelerator96 @nobodyiam @lijiansgit @WillardHu @Anilople @lepdou @DiegoKrupitza @youabcd @zcy1010 @NICEXAI @zeemood @w-a-n-g-s-h-u-n @yyfMichaelYan @xuxiawei @void1104 @youyulan @CalebZYC @mghio @Fool-coder @Shoothzj @joshknopp @darcydai @dependabot @ruanwenjun @gy09535 @ayush0407 @czd890 @pengweiqhca @sy-records @dazuimao1990 <span style="background-color:#ffffff; color:#24292f">@plzdoo</span> <span style="background-color:#ffffff; color:#24292f">@misselvexu</span> <span style="background-color:#ffffff; color:#24292f">@Alceatraz</span> <span style="background-color:#ffffff; color:#24292f">@weiyichao</span></p> 
<h1 style="margin-left:0px; margin-right:0px">欢迎加入我们</h1> 
<p style="margin-left:0; margin-right:0; text-align:left">Apollo 社区欢迎大家以任何形式为社区做出贡献，包括但不限于文档改进、提交 issue/bug、贡献代码、Review PR、技术讨论等，一起促进开源生态的发展。</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left">Apollo 官方网站：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.apolloconfig.com%2F" target="_blank">https://www.apolloconfig.com/</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left">Apollo 仓库地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapolloconfig%2Fapollo" target="_blank">https://github.com/apolloconfig/apollo</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left">Apollo 公共邮箱：apollo-config@googlegroups.com</p> </li> 
</ul>
                                        </div>
                                      
</div>
            