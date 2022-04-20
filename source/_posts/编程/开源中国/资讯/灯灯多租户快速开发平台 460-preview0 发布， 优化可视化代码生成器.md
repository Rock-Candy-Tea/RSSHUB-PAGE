
---
title: '灯灯多租户快速开发平台 4.6.0-preview.0 发布， 优化可视化代码生成器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-79d3339e46311849b51aa65ca4cb7eeea7a.png'
author: 开源中国
comments: false
date: Wed, 20 Apr 2022 02:29:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-79d3339e46311849b51aa65ca4cb7eeea7a.png'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzuihou%2Fzuihou-admin-cloud%2F1465302" target="_blank">4.6.0-预览版.0 版本 更新详情:</a></h2> 
<h2>feat</h2> 
<ul> 
 <li>(代码生成器): 前端控制需要生成的每个文件是生成还是覆盖</li> 
 <li>(代码生成器): 新增前端模板支持主从(1对多)结构</li> 
 <li>(代码生成器): 新增主从(1对多)增删改查示例</li> 
 <li>(代码生成器): 新增字典管理页面，采用主从(1对多)方式布局</li> 
 <li>(lamp-util): SaveController、Service增加复制接口</li> 
 <li>(lamp-util): 增强mp的枚举类型处理器(MybatisEnumTypeHandler.java)，解决实体类中存在<strong>任意枚举类型</strong>时，执行mybatis查询时，支持数据库中NULL、空字符串、非枚举类型、指定枚举值</li> 
</ul> 
<pre><code>ps: 比mybatis plus的MybatisEnumTypeHandler类功能更强一些，mp的不支持任意枚举类型，必须实现他提供枚举接口或注解，给他提pr不接受只能自己实现了。</code></pre> 
<ul> 
 <li>(lamp-web-pro): 组件ApiSelect新增属性allData，用于控制是否将所有数据绑定在options中</li> 
</ul> 
<p> </p> 
<h2>refactor</h2> 
<p> </p> 
<ul> 
 <li>重构后端项目、全局格式化代码、优化导包</li> 
 <li>(代码生成器): 重构后端、前端的代码生成配置页面</li> 
 <li>(代码生成器): 配置文件配置优化</li> 
 <li>(代码生成器): 优化代码预览、生成、下载页面布局和交付</li> 
 <li>配置文件属性中写死的 lamp.xx 前缀改为读取全局常量：Constants.PROJECT_PREFIX 方便二次开发时替换</li> 
 <li>将lamp-oauth-api服务中的公共接口调整到lamp-common-api</li> 
 <li>新增lamp-model模块，用于存放业务中最基础、最公共的实体、VO、枚举等</li> 
 <li>lamp-annotation模块中仅保留全局注解，interfactes 和 model 移动到lamp-core</li> 
 <li>lamp-core中 cache 相关model的包路径调整</li> 
 <li>新增lamp-parent模块，废弃并删除lamp-dependencies模块(使得项目更易分模块构建)</li> 
 <li>删除lamp-userinfo-sdk对业务模块的依赖，并将原来依赖业务代码的代码移动到sdk内部，使其和业务模块解耦</li> 
 <li>删除lamp-data-scope-sdk对业务模块的依赖，并将原来依赖业务代码的代码移动到sdk内部，使其和业务模块解耦</li> 
 <li>删除lamp-tenant-datasource-init对业务模块的依赖，并将原来依赖业务代码的代码移动到sdk内部，使其和业务模块解耦</li> 
 <li>移动DistributedLock类到lamp-cache-starter模块</li> 
 <li>DictionaryType 类重命名为 DictType</li> 
 <li>DictType、EchoConstants 类移动到lamp-model模块</li> 
 <li>重构依赖关系，使得单独编译项目时，顺序为： lamp-util-pro > lamp-dependencies-parent > lamp-public > lamp-system > lamp-base > lamp-generator > 二次开发的业务服务 > lamp-oauth > lamp-gateway > lamp-support调整表结构和代码中的@Echo注释</li> 
 <li>优化本地文件存储文件采用的接口</li> 
 <li>调整CI/CD脚本 Jenkinsfile</li> 
 <li>(代码生成器): 优化模板，给表单设置name属性，防止同一个页面生成相同id的表单</li> 
</ul> 
<h2>fix</h2> 
<p> </p> 
<ul> 
 <li>修复员工的部门未正确设置时，数据权限接口报错</li> 
 <li>修复升级导致的序列化规则失效导致的bug</li> 
 <li>修复生成serviceImpl和manageImpl代码并配置了子包名时，路径和包地址拼接异常</li> 
 <li>(lamp-web-pro): 修复Tree组件如果重新定义fieldNames的title字段后设置actionList失效的问题</li> 
 <li>(lamp-web-pro): 修复由于之前版本调整了枚举类返回类型，导致的Upload组件无法预览的bug。</li> 
</ul> 
<p> </p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">更多功能，等你来体验：     </h2> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li style="text-align:left">《灯灯》官网： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftangyh.top%2F" target="_blank">https://tangyh.top/</a> </li> 
 <li style="text-align:left">4.x体验地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpro.tangyh.top%2F" target="_blank">https://pro.tangyh.top/</a></li> 
 <li style="text-align:left">3.x 体验地址1： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fboot.tangyh.top%2F" target="_blank">https://boot.tangyh.top/</a></li> 
 <li style="text-align:left">3.x 体验地址2： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fboot.tangyh.top%2Flamp-web%2F" target="_blank">https://boot.tangyh.top/lamp-web/</a></li> 
</ol> 
<h1 style="margin-left:0; margin-right:0; text-align:left">本次上线重点功能预览</h1> 
<table border="1" cellpadding="1" cellspacing="1" style="width:100%"> 
 <tbody> 
  <tr> 
   <td> <p><img height="2584" src="https://oscimg.oschina.net/oscnet/up-79d3339e46311849b51aa65ca4cb7eeea7a.png" width="4986" referrerpolicy="no-referrer"></p> </td> 
   <td> <p><img height="1751" src="https://oscimg.oschina.net/oscnet/up-58a43a88a42d9fba47b997b26bb49401ce1.png" width="2326" referrerpolicy="no-referrer"></p> </td> 
  </tr> 
  <tr> 
   <td> <p><img height="1824" src="https://oscimg.oschina.net/oscnet/up-2888d5e5444971f2f43effa1a8d7bc5d85c.png" width="4616" referrerpolicy="no-referrer"></p> </td> 
   <td> <p> </p> </td> 
  </tr> 
  <tr> 
   <td> <p><img height="2358" src="https://oscimg.oschina.net/oscnet/up-e330417875df01558f98c40d87f4d7fb2ef.png" width="4588" referrerpolicy="no-referrer"></p> </td> 
   <td> <p><img height="1760" src="https://oscimg.oschina.net/oscnet/up-c2cb3dbedd3aef6391a00accf447295455d.png" width="4560" referrerpolicy="no-referrer"></p> </td> 
  </tr> 
 </tbody> 
</table> 
<h1 style="margin-left:0; margin-right:0; text-align:left">《灯灯》中后台快速开发平台</h1> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">如果你非要说 lamp 是 Linux+Apache+MySQL+PHP，那就算是吧，毕竟 PHP 是世界上最好的语言，我也希望此项目成为世界上最好的后台框架！😈😈😈</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>lamp-cloud</code><span> </span>基于 jdk11/jdk8 +<span> </span><code>SpringCloud</code><span> </span>+ SpringCloudAlibaba+<span> </span><code>SpringBoot</code><span> </span>的微服务快速开发平台，专注于解决 SaaS 多租户体系问题， 具备 RBAC 功能、网关统一鉴权、Xss 防跨站攻击、自动代码生成、多种存储系统、分布式事务、分布式定时任务等多个模块，支持多业务系统并行开发， 支持多服务并行开发，可以作为后端服务的开发脚手架。代码简洁，注释齐全，架构清晰，非常适合学习和企业作为基础框架使用。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">核心技术采用 Spring Cloud Alibaba、SpringBoot、Mybatis、Seata、Sentinel、RabbitMQ、FastDFS/MinIO、SkyWalking 等主要框架和中间件。 希望能努力打造一套从<span> </span><code>JavaWeb基础框架</code><span> </span>-<span> </span><code>分布式微服务架构</code><span> </span>-<span> </span><code>持续集成</code><span> </span>-<span> </span><code>系统监测</code><span> </span>的解决方案。<code>本项目旨在实现基础能力，不涉及具体业务。</code></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">项目截图：</h1> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px; max-width:100%; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>预览</th> 
   <th>预览</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt src="https://oscimg.oschina.net/oscnet/up-7f261718f81c0e9943894231d0fedf51bb6.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/99e21a50fe4cd8e644bc2a2c693b9b86.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/315afa0201968de0b20c1af42fb981c5.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/cdb488d0ed1c35613025613df6a36f96.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/c8d8936b144fe568ef394289ddbf0268.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt src="https://oscimg.oschina.net/oscnet/up-16787bac9c056bad7ff6538a0fa5f676234.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/58ae227c8b3e98129091dc86efb219c8.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/7e34b4c35c24445f72898c95fb2d6347.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/2f1bcc485ca1ff3ee22995b6b276cc6f.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/cbcafbcff1e2404f2fb466ab257de6de.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/45111269e0acd9173e480e31505b04f3.png" referrerpolicy="no-referrer"></td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px"><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/67e0575c0c9acb0e787e17194e5fba0d.png" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table> 
<p> </p>
                                        </div>
                                      
</div>
            