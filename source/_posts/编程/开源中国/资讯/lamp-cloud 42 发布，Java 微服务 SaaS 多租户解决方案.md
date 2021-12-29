
---
title: 'lamp-cloud 4.2 发布，Java 微服务 SaaS 多租户解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7f261718f81c0e9943894231d0fedf51bb6.png'
author: 开源中国
comments: false
date: Wed, 29 Dec 2021 09:29:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7f261718f81c0e9943894231d0fedf51bb6.png'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzuihou%2Fzuihou-admin-cloud%2F1465302" target="_blank">4.2.0 版本 更新详情:</a></h2> 
<h2 style="margin-left:0; margin-right:0; text-align:left">build</h2> 
<ul> 
 <li>依赖升级</li> 
</ul> 
<pre><code>// lamp-util-pro
spring.boot.version > 2.5.8
spring-boot-admin.version>2.5.5
hutool.version>5.7.18

// lamp-web-pro
"typescript": "^4.5.4",
"vite": "^2.7.3",
"ant-design-vue": "3.0.0-alpha.16",
"@vueuse/core": "^7.4.0",
"@vueuse/shared": "^7.4.0",</code></pre> 
<ul> 
 <li>base_file 表名改为 com_file</li> 
</ul> 
<h2>feat</h2> 
<ul> 
 <li>lamp-boot-datasource-column: <strong>基于SpringBoot实现的单体版后端工程首次发布</strong></li> 
 <li>docs: <strong>基于4.2版本编写的第一版文档 首次发布。</strong></li> 
 <li>lamp-web-pro: 开发运营系统增加附件管理功能，用于查看默认库的附件。</li> 
 <li>lamp-cloud-pro: 新的SQL数据脚本</li> 
 <li>lamp-util-pro: 废弃lamp-security-starter模块</li> 
 <li>lamp-cloud-pro: 新增lamp-userinfo-sdk模块（原lamp-security-starter模块实现的基于注解的uri权限由网关拦截器取代，@LoginUser功能由lamp-userinfo-sdk取代）</li> 
 <li>lamp-web-pro: 首页增加引导语</li> 
</ul> 
<h2>refactor</h2> 
<ul> 
 <li>lamp-cloud-pro: <strong>优化uri权限相关配置</strong></li> 
 <li>lamp-cloud-pro: 优化删除数据源方法</li> 
 <li>lamp-cloud-pro: 资源树数据按sortValue排序</li> 
 <li>lamp-cloud-pro: 优化文件上传、下载、回显接口</li> 
 <li>lamp-cloud-pro: 消息接受调整为员工ID</li> 
 <li>lamp-web-pro: <strong>按钮权限校验支持 withoutAny 模式</strong></li> 
 <li>lamp-web-pro: 基础平台只静态加载 我的企业 路由；开发运营平台只静态加载 vben官方页面</li> 
 <li>lamp-web-pro: 优化消息管理、我的消息页面数据回显功能。</li> 
</ul> 
<h2>fix</h2> 
<ul> 
 <li>lamp-util-pro： 升级logback规避漏洞<span style="background-color:#ffffff; color:#333333">：CVE-2021-42550  (spring boot 升级后，logback版本就自动升级了)</span></li> 
 <li>lamp-cloud-pro: 修复依赖合并错误导致的报错</li> 
 <li>lamp-web-pro: 修复租户维护页面 状态字段 Badge color 属性问题</li> 
 <li>lamp-web-pro: 修复我的企业页面 地区选择bug</li> 
 <li>lamp-web-pro: 升级 vueuse/core 修复点击退出系统时，web socket 导致的报错</li> 
 <li>lamp-web-pro: 修复上传附件之后回显了多余条目 (#1495)</li> 
 <li>lamp-web-pro: 修复多tab带参数匹配不正确的bug (#1482)</li> 
 <li>lamp-web-pro: 修复可编辑单元格不显示0的bug (#1486)</li> 
 <li>lamp-web-pro: 多次调用 createAxios 函数转换参数被其他调用覆盖 (1474)</li> 
 <li>lamp-web-pro: 修复表单重置失效</li> 
 <li>lamp-web-pro: 修复pnpm版本过高导致编译项目报错的问题</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">更多功能，等你来体验：     </h2> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li style="text-align:left"> 4.x体验地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftangyh.top%2F" target="_blank">https://tangyh.top/</a></li> 
 <li style="text-align:left">3.x 体验地址1： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fboot.tangyh.top%2F" target="_blank">https://boot.tangyh.top/</a></li> 
 <li style="text-align:left">3.x 体验地址2： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fboot.tangyh.top%2Flamp-web" target="_blank">https://boot.tangyh.top/lamp-web</a></li> 
</ol> 
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
            