
---
title: 'lamp-cloud-pro 4.1 百余项更新，Java SaaS 多租户解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7f261718f81c0e9943894231d0fedf51bb6.png'
author: 开源中国
comments: false
date: Thu, 16 Dec 2021 10:39:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7f261718f81c0e9943894231d0fedf51bb6.png'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0px; margin-right:0px; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzuihou%2Fzuihou-admin-cloud%2F1465302" target="_blank">4.1 版本 更新详情:</a></h2> 
<h2>build：</h2> 
<ul> 
 <li>lamp-util-pro:</li> 
</ul> 
<pre><code>spring.boot.version>2.5.7
spring-boot-admin.version>2.5.4
dynamic.datasource.version>3.5.0
hutool.version>5.7.17
aliyun-java-sdk-core.version>4.5.30
qiniu-java-sdk.version>7.9.0
</code></pre> 
<ul> 
 <li>lamp-web-pro:</li> 
</ul> 
<pre><code>vue > 3.2.26
ant-design-vue > 3.0.0
vite > 2.7.1
moment 替换为 dayjs</code></pre> 
<ul> 
 <li>lamp-cloud-pro: <strong>msg、file、authority服务合并为base服务</strong></li> 
 <li>lamp-cloud-pro: <strong>tenant服务变更为system服务</strong></li> 
 <li>lamp-cloud-pro: 合并nacos中的配置文件</li> 
</ul> 
<h2>feat：</h2> 
<ul> 
 <li>docs: 完善4.x部分文档</li> 
 <li>lamp-util-pro: TreeEntity 增加 addChildren 方法</li> 
 <li>lamp-web-pro: 资源维护页面，配置菜单和视图时，支持配置<strong>打开方式</strong>为：组件内打开页面、组件内打开链接、组件外打开链接</li> 
 <li>lamp-web-pro: 资源维护页面，优化各个字段的逻辑，使配置者更加不容易出错</li> 
 <li>lamp-web-pro: 新增租户查询页面</li> 
 <li>lamp-web-pro: 调整页面name属性和菜单名称一致， 便于keep alive</li> 
 <li>lamp-web-pro: 表单支持全局 readonly</li> 
 <li>lamp-web-pro: BasicTree支持控制工具栏下拉功能</li> 
 <li>lamp-web-pro: 员工界面可绑定角色</li> 
 <li>lamp-cloud-pro: <strong>在网关拦截器增加URI鉴权功能</strong></li> 
 <li>lamp-cloud-pro: <strong>租户管理员无需分配权限</strong>，即拥有其租户的所有资源权限和URI权限，且任何人不得修改此管理员的权限。</li> 
 <li>lamp-cloud-pro: 统一 IgnoreProperties 和 uri权限校验器 的URI校验规则为AntPathMatcher</li> 
 <li>lamp-cloud-pro: 新增地区数据json下载接口，方便前端地区数据更新和下载</li> 
 <li>lamp-cloud-pro: 后台创建的员工和用户，默认密码读取nacos配置</li> 
 <li>lamp-cloud-pro: 新增系统参数功能</li> 
 <li>lamp-cloud-pro: 优化 用户信息注入功能</li> 
 <li>lamp-cloud-pro: 完善用户重置密码</li> 
 <li>新增feign全局超时配置</li> 
 <li>包含以上但不限于以上功能的其他若干功能</li> 
</ul> 
<h2>refactor</h2> 
<ul> 
 <li>lamp-util-pro: <strong>屏蔽UpdateAll方法</strong>，需要此方法的自己在子类重写</li> 
 <li>lamp-util-pro: 默认不在依赖dozer</li> 
 <li>lamp-util-pro: 优化树结构的实体类，path字段 拼接父子关系层级</li> 
 <li>lamp-cloud-pro: 优化企业管理的流程</li> 
 <li>lamp-cloud-pro: <strong>合并租户的lamp_base库和lamp_extend库</strong>，降低入门门槛</li> 
 <li>lamp-cloud-pro: 优化RouterMeta，实现meta参数自定义扩展</li> 
 <li>lamp-cloud-pro: 消息中心，发送消息功能，只查询自己企业下的用户</li> 
 <li>lamp-cloud-pro: 调整 TraceFilter 为WebFilter，且优先级最高</li> 
 <li>lamp-web-pro: <strong>调整前端拦截器的请求头为：Token、TenantId、ApplicationId、Authorization</strong>，且改为明文传输，降低入门门槛</li> 
 <li>lamp-web-pro: 修复部分页面contentFullHeight参数导致的bug</li> 
 <li>lamp-web-pro: 修复图片预览组件的背景图问题</li> 
 <li>lamp-web-pro: 优化表单全局 disabled 功能</li> 
 <li>优化logback扫描日志配置</li> 
 <li>docs: 优化架构图</li> 
 <li>代码格式、导包、注释优化</li> 
 <li>优化nginx配置，解决服务器获取ip异常</li> 
 <li>包含以上但不限于以上优化的其他若干优化</li> 
</ul> 
<h2>fix</h2> 
<p> </p> 
<ul> 
 <li>lamp-web-pro: <strong>适配升级到ant design vue3.0后Tree、Table等组件产生的一系列bug</strong></li> 
 <li>lamp-web-pro: <strong>修复默认库和租户库上传文件和回显文件不正确的bug</strong></li> 
 <li>lamp-util-pro: SystemApiScan组件扫描的URI接口前缀不正确问题</li> 
 <li>lamp-util-pro: 修复没有连接wifi情况下，启动时lamp-uid模块无法获取ip地址报错</li> 
 <li>lamp-util-pro: 中文请求头 异步feign调用时报错</li> 
 <li>lamp-util-pro: 修复column模式插件 多个join时的报错</li> 
 <li>lamp-cloud-pro: 排除第三方的log4j</li> 
 <li>lamp-cloud-pro: 修复mq配置错误导致的启动报错</li> 
 <li>lamp-cloud-pro: 修复回显字典查询到base库的bug</li> 
 <li>lamp-cloud-pro: 修复资源名称、资源path 校验重复时，跨应用校验的问题</li> 
 <li>lamp-cloud-pro: 修复地区爬取和下载接口 数据异常问题</li> 
 <li>lamp-cloud-pro: 修复租户链接模式，远程链接模式的bug</li> 
 <li>包含以上但不限于以上bug的其他bug</li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left">更多功能，等你来体验：     </h2> 
<ol> 
 <li style="text-align:left"> 4.x体验地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftangyh.top%2F" target="_blank">https://tangyh.top/</a></li> 
 <li style="text-align:left">3.x 体验地址1： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fboot.tangyh.top%2F" target="_blank">http://boot.tangyh.top/</a></li> 
 <li style="text-align:left">3.x 体验地址2： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fboot.tangyh.top%2Flamp-web" target="_blank">http://boot.tangyh.top/lamp-web</a></li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">《灯灯》中后台快速开发平台</h1> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">如果你非要说 lamp 是 Linux+Apache+MySQL+PHP，那就算是吧，毕竟 PHP 是世界上最好的语言，我也希望此项目成为世界上最好的后台框架！😈😈😈</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>lamp-cloud</code><span> </span>基于 jdk11/jdk8 +<span> </span><code>SpringCloud</code><span> </span>+ SpringCloudAlibaba+<span> </span><code>SpringBoot</code><span> </span>的微服务快速开发平台，专注于解决 SaaS 多租户体系问题， 具备 RBAC 功能、网关统一鉴权、Xss 防跨站攻击、自动代码生成、多种存储系统、分布式事务、分布式定时任务等多个模块，支持多业务系统并行开发， 支持多服务并行开发，可以作为后端服务的开发脚手架。代码简洁，注释齐全，架构清晰，非常适合学习和企业作为基础框架使用。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">核心技术采用 Spring Cloud Alibaba、SpringBoot、Mybatis、Seata、Sentinel、RabbitMQ、FastDFS/MinIO、SkyWalking 等主要框架和中间件。 希望能努力打造一套从<span> </span><code>JavaWeb基础框架</code><span> </span>-<span> </span><code>分布式微服务架构</code><span> </span>-<span> </span><code>持续集成</code><span> </span>-<span> </span><code>系统监测</code><span> </span>的解决方案。<code>本项目旨在实现基础能力，不涉及具体业务。</code></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"> </h2> 
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
                                        </div>
                                      
</div>
            