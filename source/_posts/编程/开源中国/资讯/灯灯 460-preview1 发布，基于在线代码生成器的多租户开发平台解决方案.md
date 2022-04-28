
---
title: '灯灯 4.6.0-preview.1 发布，基于在线代码生成器的多租户开发平台解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-79d3339e46311849b51aa65ca4cb7eeea7a.png'
author: 开源中国
comments: false
date: Thu, 28 Apr 2022 14:01:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-79d3339e46311849b51aa65ca4cb7eeea7a.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzuihou%2Fzuihou-admin-cloud%2F1465302" target="_blank">4.6.0-预览版.1 版本 更新详情:</a></h2> 
<h2>feat</h2> 
<ul> 
 <li>生成代码的同时，可以根据字段注释在EchoRef、EchoDictType和EchoApi类中增加常量</li> 
 <li>支持识别注释中的字典列表，生成初始化字典的sql</li> 
 <li>lamp-userinfo-sdk模块 增加用户、员工、机构、岗位、资源、角色相关帮助类</li> 
 <li>租户表加"类别"字段</li> 
</ul> 
<h2>refactor</h2> 
<ul> 
 <li>(lamp-generator): 代码生成器同时适配window、linux、mac 3大操作系统的 IDE启动 和 jar启动 2种启动方式</li> 
 <li>(lamp-generator): 优化前端data.tsx模板，使生成的枚举和字典类型字段不会报错</li> 
 <li>(lamp-generator): 代码生成器中 generator.* 的配置调整为 lamp.generator.*</li> 
 <li>(lamp-generator): 优化 GeneratorConfig，使得所有的配置在yml都均能提示</li> 
 <li>(lamp-model): DictType 类重命名为 EchoDictType</li> 
 <li>(lamp-model): EchoConstants 类重命名为 EchoApi</li> 
 <li>(lamp-web-pro): BasicTitle组件支持下划线、下划线虚线、左侧垂直分割线、加粗等参数</li> 
 <li>(lamp-web-pro): BasicForm组件支持BasicTitle</li> 
 <li>(lamp-web-pro): 首页提示优化</li> 
</ul> 
<h2>fix</h2> 
<ul> 
 <li>(数据源维护): 测试数据源连接接口无法正常链接</li> 
 <li>(lamp-generator): 模板的parent属性调整以适配新版本源码</li> 
 <li>(lamp-web-pro): 资源维护页面回显使用了Card的bug</li> 
</ul> 
<h2>更多功能，等你来体验：</h2> 
<ol> 
 <li>《灯灯》官网： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftangyh.top%2F">https://tangyh.top/</a></li> 
 <li>4.x体验地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpro.tangyh.top%2F">https://pro.tangyh.top/</a></li> 
 <li>3.x 体验地址1： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fboot.tangyh.top%2F">https://boot.tangyh.top/</a></li> 
 <li>3.x 体验地址2： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fboot.tangyh.top%2Flamp-web%2F">https://boot.tangyh.top/lamp-web/</a></li> 
</ol> 
<h1>本次上线重点功能预览</h1> 
<table> 
 <thead> 
  <tr> 
   <th>图片</th> 
   <th>图片</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td><img alt src="https://oscimg.oschina.net/oscnet/up-79d3339e46311849b51aa65ca4cb7eeea7a.png" referrerpolicy="no-referrer"></td> 
   <td><img alt src="https://oscimg.oschina.net/oscnet/up-58a43a88a42d9fba47b997b26bb49401ce1.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td><img alt src="https://oscimg.oschina.net/oscnet/up-2888d5e5444971f2f43effa1a8d7bc5d85c.png" referrerpolicy="no-referrer"></td> 
   <td><img alt src="https://oscimg.oschina.net/oscnet/up-c2cb3dbedd3aef6391a00accf447295455d.png" referrerpolicy="no-referrer"> <p> </p> </td> 
  </tr> 
  <tr> 
   <td><img alt src="https://oscimg.oschina.net/oscnet/up-e330417875df01558f98c40d87f4d7fb2ef.png" referrerpolicy="no-referrer"></td> 
   <td> </td> 
  </tr> 
 </tbody> 
</table> 
<h1>《灯灯》中后台快速开发平台</h1> 
<blockquote> 
 <p>如果你非要说 lamp 是 Linux+Apache+MySQL+PHP，那就算是吧，毕竟 PHP 是世界上最好的语言，我也希望此项目成为世界上最好的后台框架！😈😈😈</p> 
</blockquote> 
<p><code>lamp-cloud</code>基于 jdk11/jdk8 +<code>SpringCloud</code>+ SpringCloudAlibaba+<code>SpringBoot</code>的微服务快速开发平台，专注于解决 SaaS 多租户体系问题， 具备 RBAC 功能、网关统一鉴权、Xss 防跨站攻击、自动代码生成、多种存储系统、分布式事务、分布式定时任务等多个模块，支持多业务系统并行开发， 支持多服务并行开发，可以作为后端服务的开发脚手架。代码简洁，注释齐全，架构清晰，非常适合学习和企业作为基础框架使用。</p> 
<p>核心技术采用 Spring Cloud Alibaba、SpringBoot、Mybatis、Seata、Sentinel、RabbitMQ、FastDFS/MinIO、SkyWalking 等主要框架和中间件。 希望能努力打造一套从<code>JavaWeb基础框架</code>-<code>分布式微服务架构</code>-<code>持续集成</code>-<code>系统监测</code>的解决方案。<code>本项目旨在实现基础能力，不涉及具体业务。</code></p> 
<h1>项目截图：</h1> 
<table> 
 <thead> 
  <tr> 
   <th>预览</th> 
   <th>预览</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td><img alt src="https://oscimg.oschina.net/oscnet/up-7f261718f81c0e9943894231d0fedf51bb6.png" referrerpolicy="no-referrer"></td> 
   <td><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/99e21a50fe4cd8e644bc2a2c693b9b86.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/315afa0201968de0b20c1af42fb981c5.png" referrerpolicy="no-referrer"></td> 
   <td><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/cdb488d0ed1c35613025613df6a36f96.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/c8d8936b144fe568ef394289ddbf0268.png" referrerpolicy="no-referrer"></td> 
   <td><img alt src="https://oscimg.oschina.net/oscnet/up-16787bac9c056bad7ff6538a0fa5f676234.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/58ae227c8b3e98129091dc86efb219c8.png" referrerpolicy="no-referrer"></td> 
   <td><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/7e34b4c35c24445f72898c95fb2d6347.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/2f1bcc485ca1ff3ee22995b6b276cc6f.png" referrerpolicy="no-referrer"></td> 
   <td><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/cbcafbcff1e2404f2fb466ab257de6de.png" referrerpolicy="no-referrer"></td> 
  </tr> 
  <tr> 
   <td><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/45111269e0acd9173e480e31505b04f3.png" referrerpolicy="no-referrer"></td> 
   <td><img alt="预览.png" src="https://img-blog.csdnimg.cn/img_convert/67e0575c0c9acb0e787e17194e5fba0d.png" referrerpolicy="no-referrer"></td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            