
---
title: 'JeecgBoot 2.4.3 版本发布，企业级低代码平台'
categories: 
    - 编程
    - 开源中国
    - 资讯

author: 开源中国
comments: false
date: Sun, 21 Mar 2021 10:37:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-34f20499033be8c19b6ccd491657dc933dd.png'
---

<div>   
<div class="content">
                                                                                            <h3 style="text-align:left">项目介绍</h3> 
<blockquote> 
 <p>JeecgBoot是一款基于代码生成器的低代码平台！前后端分离架构 SpringBoot2.x，SpringCloud，Ant Design&Vue，Mybatis-plus，Shiro，JWT 支持微服务。强大的代码生成器让前后端代码一键生成! JeecgBoot引领低代码开发模式(OnlineCoding-> 代码生成-> 手工MERGE)， 帮助解决Java项目70%的重复工作，让开发更多关注业务。既能快速提高效率，节省成本，同时又不失灵活性！</p> 
</blockquote> 
<p style="text-align:left"><strong>当前版本</strong>：v2.4.3 | 2021-03-22</p> 
<h3 style="text-align:left">源码下载</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot" target="_blank">https://github.com/zhangdaiscott/jeecg-boot</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot">https://gitee.com/jeecg/jeecg-boot</a></li> 
</ul> 
<h3 style="text-align:left">技术文档</h3> 
<ul> 
 <li>技术官网： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jeecg.com" target="_blank">http://www.jeecg.com</a></li> 
 <li>在线演示： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fboot.jeecg.com" target="_blank">http://boot.jeecg.com</a></li> 
 <li>技术文档： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jeecg.com" target="_blank">http://doc.jeecg.com</a></li> 
 <li>常见问题： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjeecg.com%2Fdoc%2Fqa" target="_blank">http://jeecg.com/doc/qa</a></li> 
 <li>视频教程： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjeecg.com%2Fdoc%2Fvideo" target="_blank">http://jeecg.com/doc/video</a></li> 
 <li>QQ群：③816531124</li> 
</ul> 
<h3 style="text-align:left">升级日志</h3> 
<blockquote> 
 <p>此版本为优化易用版，重点重构了前端和代码生成器模板，将Form升级为FormModel支持双向绑定简化前端；另外优化了微服务的使用模式，提供简易机制，进一步降低了微服务的使用难度；</p> 
</blockquote> 
<p>前端升级</p> 
<ul> 
 <li>重构前端大部分页面，将表单升级为FormModel模式（涉及常见案例、系统管理等）</li> 
 <li>重构代码生成器全部模板，生成的表单默认为FormModel模式</li> 
 <li>新增示例：一对多JVxeTable</li> 
 <li>新增示例：JVXETable 省市县联动</li> 
 <li>Online表单，高级查询按钮布局问题</li> 
 <li>Online视图，恢复支持JS增强等功能</li> 
 <li>登录密码错误修改验证码</li> 
</ul> 
<p>后台升级</p> 
<ul> 
 <li>进一步简化微服务开发模式，提供一系列的简易工具</li> 
 <li>单体和微服务 docker compose 脚本优化</li> 
 <li>代码生成器的数据库配置，改造默认走平台的配置</li> 
 <li>Excel多sheet导出导入例子</li> 
 <li>升级autopoi到1.3版本，poi升级到4.1.2</li> 
 <li>升级jimureport到1.2.1-RC版本，低代码报表优化</li> 
 <li>提供单体和微服务模块自动创建骨架archetype</li> 
 <li>登录后清除redis中验证码</li> 
 <li>重复check接口，sql注入检查</li> 
 <li>代码生成器，开关组件进一步优化</li> 
 <li>积木报表支持系统变量</li> 
 <li>Excel图片导出报错，本地upload情况下，ImageBasePath未设置</li> 
 <li>TomcatServletWebServerFactory重复注册问题处理</li> 
 <li>支持达梦数据库</li> 
 <li>取消jeecg-boot-starter-redis模块，合并到core中</li> 
 <li>消息推送采用redis发布订阅模式，支持集群</li> 
 <li>nacos server本地化采用jar方式启动，简化开发省掉nacos的安装</li> 
 <li>删除jeecg-cloud-example，合并到jeecg-cloud-system-start</li> 
 <li>修改xxljob执行器默认端口，防止默认9999端口冲突</li> 
 <li>集成xxl-job-2.2.0之后，注解没有删掉，导致启动报端口冲突</li> 
 <li>进一步优化重构分布式锁</li> 
 <li>新增几个单元测试类</li> 
</ul> 
<p>Issues处理</p> 
<ul> 
 <li>Excel 导入注解name包含下划线抛出空指针异常 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2004" target="_blank">#2004</a></li> 
 <li>导出图片到Excel，按照官方文档，导出报错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F1811" target="_blank">#1811</a></li> 
 <li>账号登录安全问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2207" target="_blank">#2207</a></li> 
 <li>excel 导出分隔符问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F1126" target="_blank">#1126</a></li> 
 <li>模板导出功能，#fe: 横向遍历怎么用不了呢 &#123;&#123;#fe:maplist t.xxx&#125;&#125; 是这样格式吧？ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2139" target="_blank">#2139</a></li> 
 <li>Autopoi的@Excel注解 disctTable、dicCode dicText 导出解析不成功 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2158" target="_blank">#2158</a></li> 
 <li>SQL注入漏洞 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2201" target="_blank">#2201</a></li> 
 <li>建议优化Online表单开发代码生成器不能成功生成代码的错误日志 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2234" target="_blank">#2234</a></li> 
 <li>积木报表API请求获得不到查询条件 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I2NXEV">I2NXEV</a></li> 
 <li>字典导入window下能可 linux部署得环境下出错 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I35AUG">I35AUG</a></li> 
 <li>绕过验证码漏洞 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2227" target="_blank">#2227</a></li> 
 <li>pop选择器列主键问题 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I29P9Q">I29P9Q</a></li> 
 <li>最后一页中分页删除问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2239" target="_blank">#2239</a></li> 
 <li>集成xxl-job-2.2.0之后，注解没有删掉，导致启动报端口冲突 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2228" target="_blank">#2228</a></li> 
 <li>常见案例=>JVXETable示例(NEW)=>普通示例页面下高级示例 前端页面报错误！ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2134" target="_blank">#2134</a></li> 
 <li>在数据库 mysql8.0.15 上报错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2268" target="_blank">#2268</a></li> 
 <li>微服务Feign调用Provider报错Token为空的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2263" target="_blank">#2263</a></li> 
 <li>教程里关于feign调用拿不到token的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2244" target="_blank">#2244</a></li> 
 <li>swagger密码访问不生效 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2253" target="_blank">#2253</a></li> 
 <li>online报表中字段类型为长整形时，合计的显示能否不加.00，数值类型的时候加上.00 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2279" target="_blank">#2279</a></li> 
 <li>feign 动态创建client，拦截器执行多次 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2275" target="_blank">#2275</a></li> 
 <li>有个小Bug <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3854N">I3854N</a></li> 
 <li>feign调用 500错误 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I37PFB">I37PFB</a></li> 
 <li>微服务化后-cloud-demo项目导出无法和字典关联 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I37PNL">I37PNL</a></li> 
 <li>FeignConfig重复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2286" target="_blank">#2286</a></li> 
 <li>部门管理员添加上级用户时缺失负责部门列 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I2SDU1">I2SDU1</a></li> 
 <li>批量导入部门以后，不能追加下一级部门 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2245" target="_blank">#2245</a></li> 
 <li>关于测边菜单遮挡内容问题详细说明 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2255" target="_blank">#2255</a></li> 
 <li>屏幕适配 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2224" target="_blank">#2224</a></li> 
 <li>Online表单开发功能，附表外键配置非主表主键问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2281" target="_blank">#2281</a></li> 
 <li>用online报表配置设计的报表，每页会多出一条空行，导致分页总数合计不对 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2242" target="_blank">#2242</a></li> 
 <li>数据量大时导出不能自动分批<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2243" target="_blank"> #2243</a></li> 
 <li>部门表太大导致的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2204" target="_blank">#2204</a></li> 
 <li>请求url里面带分号，绕过token校验 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2256" target="_blank">#2256</a></li> 
 <li>字典【是否启用】按钮会错误的保存状态 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2311" target="_blank">#2311</a></li> 
 <li>微服务部署下代码生成失效，单体模式下代码生成可用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2324" target="_blank">#2324</a></li> 
 <li>system服务和demo服务有办法同时使用xxl-job吗 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2313" target="_blank">#2313</a></li> 
 <li>PermissionDataAspect.filterUrl() 方法有代码bug <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2325" target="_blank">#2325</a></li> 
 <li>省市区组件无限递归 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2335" target="_blank">#2335</a></li> 
</ul> 
<h3 style="text-align:left">为什么选择 JeecgBoot?</h3> 
<blockquote> 
 <p>开源界“小普元”超越传统商业平台。引领低代码开发模式(OnlineCoding-> 代码生成器 -> 手工MERGE)，低代码开发同时又支持灵活编码， 可以帮助解决Java项目70%的重复工作，让开发更多关注业务。既能快速提高开发效率，节省成本，同时又不失灵活性。</p> 
</blockquote> 
<ul> 
 <li>采用最新主流前后分离框架（SpringBoot+Mybatis-plus+Ant-Design+Vue），容易上手; 代码生成器依赖性低,灵活的扩展能力，可灵活实现二次开发;</li> 
 <li>开发效率很高,采用代码生成器，单表数据模型和一对多(父子表)、树列表等数据模型，增删改查功能自动生成，菜单配置直接使用（前端代码和后端代码都一键生成）；</li> 
 <li>代码生成器提供强大模板机制，支持自定义模板风格。目前提供四套风格模板（单表两套、一对多两套）</li> 
 <li>封装完善的用户、角色、菜单、组织机构、数据字典、在线定时任务等基础功能。强大的权限机制，支持访问授权、按钮权限、数据权限、表单权限等</li> 
 <li>零代码在线开发能力，在线配置表单、在线配置报表、在线配置图表、在线设计表单</li> 
 <li>常用共通封装，各种工具类(定时任务,短信接口,邮件发送,Excel导入导出等),基本满足80%项目需求</li> 
 <li>简易Excel导入导出，支持单表导出和一对多表模式导出，生成的代码自带导入导出功能</li> 
 <li>集成简易报表工具，图像报表和数据导出非常方便，可极其方便的生成图形报表、pdf、excel、word等报表；</li> 
 <li>采用前后分离技术，页面UI精美，针对常用组件做了封装：时间、行表格控件、截取显示控件、报表组件，编辑器等等</li> 
 <li>查询过滤器：查询功能自动生成，后台动态拼SQL追加查询条件；支持多种匹配方式（全匹配/模糊查询/包含查询/不匹配查询）；</li> 
 <li>数据权限（精细化数据权限控制，控制到行级，列表级，表单字段级，实现不同人看不同数据，不同人对同一个页面操作不同字段</li> 
 <li>在线配置报表（无需编码，通过在线配置方式，实现曲线图，柱状图，数据等报表）</li> 
 <li>页面校验自动生成(必须输入、数字校验、金额校验、时间空间等);</li> 
 <li>提供单点登录CAS集成方案，项目中已经提供完善的对接代码</li> 
 <li>表单设计器，支持用户自定义表单布局，支持单表，一对多表单、支持select、radio、checkbox、textarea、date、popup、列表、宏等控件</li> 
 <li>专业接口对接机制，统一采用restful接口方式，集成swagger-ui在线接口文档，Jwt token安全验证，方便客户端对接</li> 
 <li>接口安全机制，可细化控制接口授权，非常简便实现不同客户端只看自己数据等控制</li> 
 <li>高级组合查询功能，在线配置支持主子表关联查询，可保存查询历史</li> 
 <li>提供各种系统监控，实时跟踪系统运行情况（监控 Redis、Tomcat、jvm、服务器信息、请求追踪、SQL监控）</li> 
 <li>消息中心（支持短信、邮件、微信推送等等）</li> 
 <li>集成Websocket消息通知机制</li> 
 <li>提供APP发布方案：</li> 
 <li>支持多语言，提供国际化方案；</li> 
 <li>数据变更记录日志，可记录数据每次变更内容，通过版本对比功能查看历史变化</li> 
 <li>平台UI强大，实现了移动自适应</li> 
 <li>平台首页风格，提供多种组合模式，支持自定义风格</li> 
 <li>提供简单易用的打印插件，支持谷歌、IE浏览器等各种浏览器</li> 
 <li>示例代码丰富，提供很多学习案例参考</li> 
 <li>采用maven分模块开发方式</li> 
 <li>支持菜单动态路由</li> 
 <li>权限控制采用 RBAC（Role-Based Access Control，基于角色的访问控制）</li> 
</ul> 
<h3 style="text-align:left">系统功能模块</h3> 
<pre style="text-align:left"><code>├─系统管理
│  ├─用户管理
│  ├─角色管理
│  ├─菜单管理
│  ├─权限设置（支持按钮权限、数据权限）
│  ├─表单权限（控制字段禁用、隐藏）
│  ├─部门管理
│  ├─我的部门（二级管理员）
│  └─字典管理
│  └─分类字典
│  └─系统公告
│  └─职务管理
│  └─通讯录
│  └─多租户管理
├─<span style="color:#d73a49">Online</span>在线开发(低代码)
│  ├─<span style="color:#d73a49">Online</span>在线表单 <span style="color:#d73a49">-</span> 功能已开放
│  ├─<span style="color:#d73a49">Online</span>代码生成器 <span style="color:#d73a49">-</span> 功能已开放
│  ├─<span style="color:#d73a49">Online</span>在线报表 <span style="color:#d73a49">-</span> 功能已开放
│  ├─<span style="color:#d73a49">Online</span>在线图表(暂不开源)
│  ├─<span style="color:#d73a49">Online</span>图表模板配置(暂不开源)
│  ├─<span style="color:#d73a49">Online</span>布局设计(暂不开源)
│  ├─多数据源管理 <span style="color:#d73a49">-</span> 功能已开放
├─积木报表设计器(低代码)
│  ├─打印设计器 <span style="color:#d73a49">-</span> 功能已开放
│  ├─数据报表设计 <span style="color:#d73a49">-</span> 功能已开放
│  ├─图形报表设计(支持Echart) <span style="color:#d73a49">-</span> 功能已开放
│  ├─大屏设计器(暂不开源)
├─消息中心
│  ├─消息管理
│  ├─模板管理
├─代码生成器(低代码)
│  ├─代码生成器功能（一键生成前后端代码，生成后无需修改直接用，绝对是后端开发福音）
│  ├─代码生成器模板（提供<span style="color:#d73a49">4</span>套模板，分别支持单表和一对多模型，不同风格选择）
│  ├─代码生成器模板（生成代码，自带<span style="color:#d73a49">excel</span>导入导出）
│  ├─查询过滤器（查询逻辑无需编码，系统根据页面配置自动生成）
│  ├─高级查询器（弹窗自动组合查询条件）
│  ├─<span style="color:#d73a49">Excel</span>导入导出工具集成（支持单表，一对多 导入导出）
│  ├─平台移动自适应支持
├─系统监控
│  ├─<span style="color:#d73a49">Gateway</span>路由网关
│  ├─性能扫描监控
│  │  ├─监控 <span style="color:#d73a49">Redis</span>
│  │  ├─<span style="color:#d73a49">Tomcat</span>
│  │  ├─<span style="color:#d73a49">jvm</span>
│  │  ├─服务器信息
│  │  ├─请求追踪
│  │  ├─磁盘监控
│  ├─定时任务
│  ├─系统日志
│  ├─消息中心（支持短信、邮件、微信推送等等）
│  ├─数据日志（记录数据快照，可对比快照，查看数据变更情况）
│  ├─系统通知
│  ├─<span style="color:#d73a49">SQL</span>监控
│  ├─<span style="color:#d73a49">swagger-ui</span>(在线接口文档)
│─报表示例
│  ├─曲线图
│  └─饼状图
│  └─柱状图
│  └─折线图
│  └─面积图
│  └─雷达图
│  └─仪表图
│  └─进度条
│  └─排名列表
│  └─等等
│─大屏模板
│  ├─作战指挥中心大屏
│  └─物流服务中心大屏
│─常用示例
│  ├─自定义组件
│  ├─对象存储(对接阿里云)
│  ├─<span style="color:#d73a49">JVXETable</span>示例（各种复杂<span style="color:#d73a49">ERP</span>布局示例）
│  ├─单表模型例子
│  └─一对多模型例子
│  └─打印例子
│  └─一对多<span style="color:#d73a49">TAB</span>例子
│  └─内嵌<span style="color:#d73a49">table</span>例子
│  └─常用选择组件
│  └─异步树<span style="color:#d73a49">table</span>
│  └─接口模拟测试
│  └─表格合计示例
│  └─异步树列表示例
│  └─一对多<span style="color:#d73a49">JEditable</span>
│  └─<span style="color:#d73a49">JEditable</span>组件示例
│  └─图片拖拽排序
│  └─图片翻页
│  └─图片预览
│  └─<span style="color:#d73a49">PDF</span>预览
│  └─分屏功能
│─封装通用组件
│  ├─行编辑表格<span style="color:#d73a49">JEditableTable</span>
│  └─省略显示组件
│  └─时间控件
│  └─高级查询
│  └─用户选择组件
│  └─报表组件封装
│  └─字典组件
│  └─下拉多选组件
│  └─选人组件
│  └─选部门组件
│  └─通过部门选人组件
│  └─封装曲线、柱状图、饼状图、折线图等等报表的组件（经过封装，使用简单）
│  └─在线<span style="color:#d73a49">code</span>编辑器
│  └─上传文件组件
│  └─验证码组件
│  └─树列表组件
│  └─表单禁用组件
│  └─等等
│─更多页面模板
│  ├─各种高级表单
│  ├─各种列表效果
│  └─结果页面
│  └─异常页面
│  └─个人页面
├─高级功能
│  ├─系统编码规则
│  ├─提供单点登录<span style="color:#d73a49">CAS</span>集成方案
│  ├─提供<span style="color:#d73a49">APP</span>发布方案
│  ├─集成<span style="color:#d73a49">Websocket</span>消息通知机制
│─流程模块功能 (暂不开源)
│  ├─流程设计器
│  ├─在线表单设计
│  └─我的任务
│  └─历史流程
│  └─历史流程
│  └─流程实例管理
│  └─流程监听管理
│  └─流程表达式
│  └─我发起的流程
│  └─我的抄送
│  └─流程委派、抄送、跳转
│  └─。。。
└─其他模块
   └─更多功能开发中。。
</code></pre> 
<h3 style="text-align:left">系统截图</h3> 
<p>积木报表效果</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-34f20499033be8c19b6ccd491657dc933dd.png" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/up-bc66e7698915e47ee10f367449d36f5cfdc.png" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/up-cec93f41f5f871417220825bef7d25d828c.gif" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/up-4911e610685b9a1a565f2ec1c15e4e3c94d.png" referrerpolicy="no-referrer"></p> 
<p>大屏数据模板</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-b6d97fe09894247b0ca4a7012efc56d4b04.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-24e4d3a9f8872445103b995b6f616cf2bfb.png" referrerpolicy="no-referrer"></p> 
<p>PC端</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/556469bb6b699d5d97f3334d2d85d364886.jpg" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/ba807921197596ba56f495d4b22ee3280ca.jpg" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/ab91f1358fdfdd7184893f71ae2e5fc26c4.jpg" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/a06ef89af77ca6bfd3b8c9fbdbf9eeb2fc4.jpg" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/5d9cd002910559c940f241692c1e67b33cd.jpg" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/3654e2ac746ad358b3f988746af8709ae71.jpg" referrerpolicy="no-referrer"></p> 
<p>手机端</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/da543c5d0d57baab0cecaa4670c8b68c521.jpg" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/fda4bd82cab9d682de1c1fbf2060bf14fa6.jpg" referrerpolicy="no-referrer"></p> 
<p>PAD端</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/e90fef970a8c33790ab03ffd6c4c7cec225.jpg" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/d78218803a9e856a0aa82b45efc49849a0c.jpg" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/0404054d9a12647ef6f82cf9cfb80a5ac02.jpg" referrerpolicy="no-referrer"> <img alt src="https://oscimg.oschina.net/oscnet/59c23b230f52384e588ee16309b44fa20de.jpg" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">欢迎吐槽，欢迎star~ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot" target="_blank"><img alt="GitHub stars" src="https://img.shields.io/github/stars/zhangdaiscott/jeecg-boot.svg?style=social&label=Stars" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot" target="_blank"><img alt="GitHub forks" src="https://img.shields.io/github/forks/zhangdaiscott/jeecg-boot.svg?style=social&label=Fork" referrerpolicy="no-referrer"></a></p>
                                        </div>
                                      
</div>
            