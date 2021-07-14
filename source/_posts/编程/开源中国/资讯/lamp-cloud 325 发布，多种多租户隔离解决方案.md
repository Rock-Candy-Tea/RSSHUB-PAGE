
---
title: 'lamp-cloud 3.2.5 发布，多种多租户隔离解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-efe2e1b81fc35dab6f6bea8082cd6503f57.png'
author: 开源中国
comments: false
date: Wed, 14 Jul 2021 09:24:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-efe2e1b81fc35dab6f6bea8082cd6503f57.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzuihou%2Fzuihou-admin-cloud%2F1465302" target="_blank">3.2.5 版本更新详情:</a></h1> 
<h1>build:  依赖升级</h1> 
<pre><code>  spring.boot.version>2.3.12.RELEASE
  spring.cloud.version>Hoxton.SR12
  spring-cloud-alibaba.version>2.2.6.RELEASE
  nacos.version>2.0.2
  druid.version>1.2.6
  mybatis.version>3.5.7
  mybatisplus.version>3.4.3.1
  knife4j.version>2.0.9
  hutool.version>5.7.3</code></pre> 
<h1>feat: 新功能</h1> 
<ul> 
 <li><strong>增加 SCHEMA + 字段 混合模式： SCHEMA_COLUMN  🎉🎉🎉🎉🎉🎉</strong></li> 
 <li><strong>增加 数据源 + 字段 混合模式：DATASOURCE_COLUMN  🎉🎉🎉🎉🎉🎉</strong></li> 
</ul> 
<blockquote> 
 <p>适用于一个连锁店多个分门店、一个集团多个分子公司、一个商户多个售货机 等场景</p> 
</blockquote> 
<ul> 
 <li>Echo模块支持内存缓存，默认关闭。</li> 
</ul> 
<h1>fix: 修复</h1> 
<ul> 
 <li>新增租户时，初始化的菜单图标使用ant design样式</li> 
</ul> 
<h1>refactor: 增强</h1> 
<ul> 
 <li>Echo注解取消method字段。</li> 
 <li>调整 LoadService接口 单一职责，删除findNameByIds方法。</li> 
</ul> 
<blockquote> 
 <p>可以通过新增多个实现类来替代method和findNameByIds的功能</p> 
</blockquote> 
<h1 style="text-align:left">《灯灯》中后台快速开发平台</h1> 
<h2 style="text-align:left">lamp 项目组成</h2> 
<p style="text-align:left"><strong>1） 工具集 （lamp-util 项目必备，其他2个可选）</strong></p> 
<table cellspacing="0" style="width:776px"> 
 <thead> 
  <tr> 
   <th>项目</th> 
   <th>gitee</th> 
   <th>github</th> 
   <th>备注</th> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">工具集</td> 
   <td style="border-color:#dddddd"><a href="https://gitee.com/zuihou111/lamp-util">lamp-util</a></td> 
   <td style="border-color:#dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuihou%2Flamp-util" target="_blank">lamp-util</a></td> 
   <td style="border-color:#dddddd">业务无关的工具集，cloud和boot 项目都依赖它</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">代码生成器</td> 
   <td style="border-color:#dddddd"><a href="https://gitee.com/zuihou111/lamp-util">lamp-generator</a></td> 
   <td style="border-color:#dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuihou%2Flamp-util" target="_blank">lamp-generator</a></td> 
   <td style="border-color:#dddddd">给开发人员使用</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">定时调度器</td> 
   <td style="border-color:#dddddd"><a href="https://gitee.com/zuihou111/lamp-job">lamp-job</a></td> 
   <td style="border-color:#dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuihou%2Flamp-job" target="_blank">lamp-job</a></td> 
   <td style="border-color:#dddddd">尚未开发</td> 
  </tr> 
 </thead> 
</table> 
<p style="text-align:left"><strong>2） 后端 （下面2个项目功能一致，任选其一即可）</strong></p> 
<table cellspacing="0" style="width:776px"> 
 <thead> 
  <tr> 
   <th>项目</th> 
   <th>gitee</th> 
   <th>github</th> 
   <th>备注</th> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">微服务版</td> 
   <td style="border-color:#dddddd"><a href="https://gitee.com/zuihou111/lamp-cloud">lamp-cloud</a></td> 
   <td style="border-color:#dddddd">l<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuihou%2Flamp-cloud" target="_blank">amp-cloud</a></td> 
   <td style="border-color:#dddddd">SpringCloud 版</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">单体版</td> 
   <td style="border-color:#dddddd"><a href="https://gitee.com/zuihou111/lamp-boot">lamp-boot</a></td> 
   <td style="border-color:#dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuihou%2Flamp-boot" target="_blank">lamp-boot</a></td> 
   <td style="border-color:#dddddd">SpringBoot 版(和lamp-cloud功能基本一致)</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">示例项目</td> 
   <td style="border-color:#dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuihou%2Flamp-samples" target="_blank">lamp-samples</a></td> 
   <td style="border-color:#dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuihou%2Flamp-samples" target="_blank">lamp-samples</a></td> 
   <td style="border-color:#dddddd">微服务版的示例功能</td> 
  </tr> 
 </thead> 
</table> 
<p style="text-align:left"><strong> 3） 前端 （下面3个项目功能一致，任选其一即可）</strong></p> 
<table cellspacing="0" style="width:776px"> 
 <thead> 
  <tr> 
   <th>项目</th> 
   <th>gitee</th> 
   <th>github</th> 
   <th>备注</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">租户后台</td> 
   <td style="border-color:#dddddd"><a href="https://gitee.com/zuihou111/lamp-web">lamp-web</a></td> 
   <td style="border-color:#dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuihou%2Flamp-web" target="_blank">lamp-web</a></td> 
   <td style="border-color:#dddddd">基于vue-admin-element开发 （vue2.x）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">租户后台</td> 
   <td style="border-color:#dddddd"><a href="https://gitee.com/zuihou111/lamp-web-beautiful">lamp-web-beautiful</a></td> 
   <td style="border-color:#dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuihou%2Flamp-web-beautiful" target="_blank">lamp-web-beautiful</a></td> 
   <td style="border-color:#dddddd">基于vue-admin-beautiful开发 （vue2.x）</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">租户后台 （强烈推荐！👏👏👏）</td> 
   <td style="border-color:#dddddd"><a href="https://gitee.com/zuihou111/lamp-web-plus">lamp-web-plus</a></td> 
   <td style="border-color:#dddddd"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuihou%2Flamp-web-plus" target="_blank">lamp-web-plus</a></td> 
   <td style="border-color:#dddddd">基于vue-vben-admin开发 （vue3.x）</td> 
  </tr> 
 </tbody> 
</table> 
<blockquote> 
 <p>如果你非要说lamp是Linux+Apache+MySQL+PHP，那就算是吧，毕竟PHP是世界上最好的语言，我也希望此项目成为世界上最好的后台框架！😈😈😈</p> 
</blockquote> 
<h1 style="text-align:left">lamp-cloud 简介</h1> 
<p style="text-align:left"><code>lamp-cloud</code>的前身是<code>zuihou-admin-cloud</code>，从3.0.0版本开始，改名为lamp-cloud，它是<code>lamp</code>项目的其中一员。</p> 
<p style="text-align:left"><code>lamp-cloud</code> 基于 jdk11/jdk8 + <code>SpringCloud(Hoxton.SR12)</code> + <code>SpringBoot(2.3.12.RELEASE)</code> 的微服务快速开发平台，其中的可配置的SaaS功能尤其闪耀， 具备RBAC功能、网关统一鉴权、Xss防跨站攻击、自动代码生成、多种存储系统、分布式事务、分布式定时任务等多个模块，支持多业务系统并行开发， 支持多服务并行开发，可以作为后端服务的开发脚手架。代码简洁，注释齐全，架构清晰，非常适合学习和企业作为基础框架使用。</p> 
<p style="text-align:left">核心技术采用Spring Cloud Alibaba、SpringBoot、Mybatis、Seata、Sentinel、RabbitMQ、FastDFS/MinIO、SkyWalking等主要框架和中间件。 希望能努力打造一套从 <code>JavaWeb基础框架</code> - <code>分布式微服务架构</code> - <code>持续集成</code> - <code>系统监测</code> 的解决方案。<code>本项目旨在实现基础能力，不涉及具体业务。</code></p> 
<h2 style="text-align:left">lamp 租户模式介绍</h2> 
<p style="text-align:left">本项目可以通过配置，轻松切换项目的 <strong>多租户实现方式</strong>。</p> 
<table cellspacing="0" style="width:776px"> 
 <thead> 
  <tr> 
   <th>租户模式</th> 
   <th>描述</th> 
   <th>优点</th> 
   <th>缺点</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">NONE(非租户模式)</td> 
   <td style="border-color:#dddddd">没有租户</td> 
   <td style="border-color:#dddddd">简单、适合独立系统</td> 
   <td style="border-color:#dddddd">缺少租户系统的优点</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">COLUMN(字段模式)</td> 
   <td style="border-color:#dddddd">租户共用一个数据库，在业务表中增加字段来区分</td> 
   <td style="border-color:#dddddd">简单、不复杂、开发无感知</td> 
   <td style="border-color:#dddddd">数据隔离性差、安全性差、数据备份和恢复困难、</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">SCHEMA(独立数据库)</td> 
   <td style="border-color:#dddddd">每个租户独立一个 数据库(schema)，执行sql时，动态在表名前增加schema</td> 
   <td style="border-color:#dddddd">简单、开发无感知、数据隔离性好</td> 
   <td style="border-color:#dddddd">配置文件中必须配置数据库的root账号、不支持复杂sql和 sql嵌套自定义函数</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">DATASOURCE(独立数据源)</td> 
   <td style="border-color:#dddddd">每个租户独立一个数据源，执行代码时，动态切换数据源</td> 
   <td style="border-color:#dddddd">可独立部署数据库，数据隔离性好、扩展性高、故障影响小</td> 
   <td style="border-color:#dddddd">相对复杂、开发需要注意切换数据源时的事务问题、需要较多的数据库</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">SCHEMA_COLUMN(独立数据库+字段模式)</td> 
   <td style="border-color:#dddddd">每个租户独立一个 数据库，执行代码时，先动态切换数据源，在动态拼接 子租户id进行二次隔离</td> 
   <td style="border-color:#dddddd">简单、开发无感知、数据隔离性好、支持大租户小门店形式</td> 
   <td style="border-color:#dddddd">配置文件中必须配置数据库的root账号、不支持复杂sql和 sql嵌套自定义函数</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">DATASOURCE_COLUMN(独立数据源+字段模式)</td> 
   <td style="border-color:#dddddd">每个租户独立一个 数据库(数据源)，执行代码时，动态切换数据源，在动态拼接 子租户id 二次隔离</td> 
   <td style="border-color:#dddddd">可独立部署数据库，数据隔离性好、扩展性高、故障影响小、支持大租户小门店形式</td> 
   <td style="border-color:#dddddd">相对复杂、开发需要注意切换数据源时的事务问题、需要较多的数据库</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:left">lamp 项目演示地址 </h2> 
<ul> 
 <li style="text-align:left">  后端使用lamp-cloud-plus，前端使用lamp-web-plus。演示地址： https://tangyh.top</li> 
 <li style="text-align:left">  后端使用lamp-cloud-plus，前端使用lamp-web。演示地址： https://tangyh.top/lamp-web</li> 
 <li style="text-align:left">  后端使用lamp-boot-plus， 前端使用lamp-web-plus。演示地址： https://boot.tangyh.top</li> 
 <li style="text-align:left">  后端使用lamp-boot-plus， 前端使用lamp-web。演示地址： https://boot.tangyh.top/lamp-web    </li> 
</ul> 
<h2 style="text-align:left">演示地址账号：</h2> 
<ul> 
 <li>平台管理员： lamp_pt/lamp (内置给公司内部运营人员使用)</li> 
 <li>超级管理员： lamp/lamp</li> 
 <li>普通管理员： general/lamp</li> 
 <li>普通账号： normal/lamp</li> 
</ul> 
<blockquote> 
 <p>ps: 演示环境中内置租户没有写入权限，若要在演示环境测试增删改，请使用lamp_pt账号查询租户管理员账号后,登录新租户测试</p> 
</blockquote> 
<h2 style="text-align:left">lamp-cloud 项目亮点功能介绍:</h2> 
<ol> 
 <li> <p><strong>服务鉴权:</strong></p> <p>通过JWT的方式来加强服务之间调度的权限验证，保证内部服务的安全性。</p> </li> 
 <li> <p><strong>监控：</strong></p> <p>利用Spring Boot Admin 来监控各个独立Service的运行状态；利用turbine来实时查看接口的运行状态和调用频率；通过Zipkin来查看各个服务之间的调用链等。</p> </li> 
 <li> <p><strong>链路调用监控：</strong></p> <p>同时实现了Zipkin和SkyWalking作为本项目的全链路性能监控， 从整体维度到局部维度展示各项指标，将跨应用的所有调用链性能信息集中展现，可方便度量整体和局部性能，并且方便找到故障产生的源头，生产上可极大缩短故障排除时间。</p> </li> 
 <li> <p><strong>数据权限</strong></p> <p>利用基于Mybatis的DataScopeInnerInterceptor拦截器实现了数据权限功能</p> </li> 
 <li> <p><strong>SaaS(多租户)的无感解决方案</strong></p> <p>本项目支持6种常见的租户解决方案和无租户方案，同一套代码，修改一个配置即可实现租户模式只有切换。</p> </li> 
 <li> <p><strong>缓存抽象</strong></p> <p>采用CacheOps操作缓存，内置2种实现：Caffeine、 Redis，可以让项目应急时在无Redis环境正常运行</p> </li> 
 <li> <p><strong>优雅的Bean转换</strong></p> <p>采用Dozer、BeanUtil等组件来对 DTO、DO、PO等对象的优化转换</p> </li> 
 <li> <p><strong>前后端统一表单验证</strong></p> <p>严谨的表单验证通常需要 前端+后端同时验证， 但传统的项目，均只能前后端各做一次检验， 后期规则变更，又得前后端同时修改。 故在<code>hibernate-validator</code>的基础上封装了<code>lamp-validator-starter</code>起步依赖，提供一个通用接口，可以获取需要校验表单的规则，然后前端使用后端返回的规则， 以后若规则改变，只需要后端修改即可。</p> </li> 
 <li> <p><strong>防跨站脚本攻击(XSS)</strong></p> 
  <ul> 
   <li>通过过滤器对所有请求中的 表单参数 进行过滤</li> 
   <li>通过Json反序列化器实现对所有 application/json 类型的参数 进行过滤</li> 
  </ul> </li> 
 <li> <p><strong>当前登录用户信息注入器</strong></p> 
  <ul> 
   <li>通过注解实现用户身份注入</li> 
  </ul> </li> 
 <li> <p><strong>在线文档</strong></p> <p>由于原生swagger-ui某些功能支持不够友好，故采用了国内开源的<code>knife4j</code>，并制作了stater，方便springboot用户使用。</p> </li> 
 <li> <p><strong>代码生成器</strong></p> <p>基于Mybatis-plus-generator自定义了一套代码生成器， 通过配置数据库字段的注释，自动生成枚举类、数据字典注解、SaveDTO、UpdateDTO、表单验证规则注解、Swagger注解等。</p> </li> 
 <li> <p><strong>定时任务调度器</strong>：</p> <p>基于xxl-jobs进行了功能增强。(如：指定时间发送任务、执行器和调度器合并项目、多数据源)</p> </li> 
 <li> <p><strong>大文件/断点/分片续传</strong></p> <p>前端采用webupload.js、后端采用NIO实现了大文件断点分片续传，启动Eureka、Zuul、File服务后，直接打开docs/chunkUploadDemo/demo.html即可进行测试。 经测试，本地限制堆栈最大内存128M启动File服务,5分钟内能成功上传4.6G+的大文件，正式服耗时则会受到用户带宽和服务器带宽的影响，时间比较长。</p> </li> 
 <li> <p><strong>分布式事务</strong></p> <p>集成了阿里的分布式事务中间件：seata，以 <strong>高效</strong> 并且对业务 <strong>0侵入</strong> 的方式，解决 微服务 场景下面临的分布式事务问题。</p> </li> 
 <li> <p><strong>跨表、跨库、跨服务的关联数据自动注入器</strong></p> <p>用于解决跨表、跨库、跨服务分页数据的属性或单个对象的属性 回显关联数据之痛, 支持对静态数据属性(数据字典)、动态主键数据进行自动注入。</p> </li> 
 <li> <p><strong>灰度发布</strong></p> <p>为了解决频繁的服务更新上线，版本回退，快速迭代，公司内部协同开发，本项目采用修改ribbon的负载均衡策略来实现来灰度发布。</p> </li> 
</ol> 
<h2 style="text-align:left">lamp-cloud 技术栈/版本介绍：</h2> 
<ul> 
 <li>所涉及的相关的技术有： 
  <ul> 
   <li>JSON序列化:Jackson</li> 
   <li>消息队列：RabbitMQ</li> 
   <li>缓存：Redis</li> 
   <li>数据库： MySQL 5.7.9 或者 MySQL 8.0.19</li> 
   <li>定时器：采用xxl-jobs项目进行二次改造</li> 
   <li>前端：vue + element-ui</li> 
   <li>持久层框架： Mybatis-plus</li> 
   <li>代码生成器：基于Mybatis-plus-generator自定义</li> 
   <li>API网关：Gateway/zuul</li> 
   <li>服务注册&发现和配置中心: Nacos</li> 
   <li>服务消费：OpenFeign</li> 
   <li>负载均衡：Ribbon</li> 
   <li>服务熔断：Hystrix</li> 
   <li>项目构建：Maven</li> 
   <li>分布式事务： seata</li> 
   <li>分布式系统的流量防卫兵： Sentinel</li> 
   <li>监控： spring-boot-admin</li> 
   <li>链路调用跟踪： zipkin/SkyWalking</li> 
   <li>文件服务器：FastDFS 5.0.5/阿里云OSS/本地存储/MinIO</li> 
   <li>Nginx</li> 
  </ul> </li> 
 <li>部署方面： 
  <ul> 
   <li>服务器：CentOS</li> 
   <li>Jenkins</li> 
   <li>Docker</li> 
   <li>Kubernetes</li> 
  </ul> </li> 
</ul> 
<h1 style="text-align:left">项目截图：</h1> 
<table cellspacing="0" style="width:776px"> 
 <thead> 
  <tr> 
   <th>预览</th> 
   <th>预览</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd"><img alt src="https://oscimg.oschina.net/oscnet/up-efe2e1b81fc35dab6f6bea8082cd6503f57.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/99e21a50fe4cd8e644bc2a2c693b9b86.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/315afa0201968de0b20c1af42fb981c5.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/cdb488d0ed1c35613025613df6a36f96.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/c8d8936b144fe568ef394289ddbf0268.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/4d3c5d0ab011266821fe02482db33c38.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/58ae227c8b3e98129091dc86efb219c8.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/7e34b4c35c24445f72898c95fb2d6347.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/2f1bcc485ca1ff3ee22995b6b276cc6f.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/cbcafbcff1e2404f2fb466ab257de6de.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/45111269e0acd9173e480e31505b04f3.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/67e0575c0c9acb0e787e17194e5fba0d.png" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            