
---
title: 'JeecgBoot 3.1.0 版本发布，基于代码生成器的企业级低代码平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img-blog.csdnimg.cn/img_convert/44fce0865cc8cca093c5e9b8846b8456.png'
author: 开源中国
comments: false
date: Tue, 01 Mar 2022 09:17:00 GMT
thumbnail: 'https://img-blog.csdnimg.cn/img_convert/44fce0865cc8cca093c5e9b8846b8456.png'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0; margin-right:0; text-align:left">项目介绍</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">JeecgBoot是一款企业级的低代码平台！前后端分离架构 SpringBoot2.x，SpringCloud，Ant Design&Vue，Mybatis-plus，Shiro，JWT 支持微服务。强大的代码生成器让前后端代码一键生成! JeecgBoot引领低代码开发模式(OnlineCoding-> 代码生成-> 手工MERGE)， 帮助解决Java项目70%的重复工作，让开发更多关注业务。既能快速提高效率，节省成本，同时又不失灵活性！</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>当前版本</strong>：v3.1.0 | 2021-03-01</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">源码下载</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot" target="_blank">https://github.com/jeecgboot/jeecg-boot</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot">https://gitee.com/jeecg/jeecg-boot</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">技术文档</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>官方网站：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jeecg.com" target="_blank">http://www.jeecg.com</a></li> 
 <li>技术文档：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jeecg.com" target="_blank">http://doc.jeecg.com</a></li> 
 <li>在线演示：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fboot.jeecg.com" target="_blank">http://boot.jeecg.com</a></li> 
 <li>新手入门：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjeecg.com%2Fdoc%2Fquickstart" target="_blank">http://jeecg.com/doc/quickstart</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">升级日志</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">此版本历经两个月的打版测试工作，是一个阶段性重要的稳定版本，重点巩固了vue2版本功能，加强了国产数据库兼容和大数据的支撑 （后续工作会针对vue3开展，vue2的前端进入稳定期）</p> 
</blockquote> 
<h4 style="margin-left:0; margin-right:0; text-align:left">重点升级</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>达梦数据库深度测试，兼容工作</li> 
 <li>Postgres数据库深度测试，兼容工作</li> 
 <li>代码生成器，支持uniapp端列表和表单生成</li> 
 <li>严重安全漏洞修复</li> 
 <li>前端集成qiankun，支持微前端开发</li> 
 <li>新增分库分表示例和分布式事务示例代码</li> 
 <li>前端添加config配置文件，支持打包部署后修改配置</li> 
 <li>进一步重构调整后台接口，vue3兼容工作</li> 
 <li>积木报表、autopoi升级到最新版</li> 
 <li>代码生成器模板升级，增加vue3的支持</li> 
 <li>Online报表支持大数据导出，分sheet</li> 
 <li>Online表单java增强重构，拆分独立导入增强接口</li> 
 <li>系统管理等基础模块，一系列细节优化</li> 
 <li>反馈的issue问题处理</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">功能升级</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>添加扫码登录逻辑</li> 
 <li>分类字典导入错误信息处理</li> 
 <li>我的部门系列问题优化</li> 
 <li>通知公告列表查询优化</li> 
 <li>枚举首页设置，支持顺序权重</li> 
 <li>同步到本地的部门，子部门的机构类型不对</li> 
 <li>定时任务功能导出，导出人写死了</li> 
 <li>修复企业微信、钉钉工号同步失败的问题</li> 
 <li>自定义树查询条件查不出数据</li> 
 <li>@dict注解支持 dicttable 设置where条件</li> 
 <li>代码生成一对多TAB，时间组件有遮挡</li> 
 <li>升级autopoi版本、解决Log4j2爆雷漏洞问题</li> 
 <li>为了支持模块单独启动，引用system模块的类改成懒加载<a href="https://my.oschina.net/u/145675">@Lazy</a></li> 
 <li>针对接口字典翻译，新增注解方式@AutoDict</li> 
 <li>树表单功能测试无法删除数据</li> 
 <li>新增示例：表格合计新的写法</li> 
 <li>固定tinymce版本号，解决富文本框JEditor，属性设置下拉选层级显示问题</li> 
 <li>JEditableTable，slot新增buildProps参数</li> 
 <li>菜单搜索里点击跳转的菜单，无法将Token信息传递过去</li> 
 <li>通讯录 选中某个部门查询部门人员，想再取消选中查全部，无法取消</li> 
 <li>前端密码控件可以查看密码</li> 
 <li>磁盘监控没有加载效果</li> 
 <li>退出登录体验不好</li> 
 <li>数据规则，选择自定义SQL 规则值无法输入空格</li> 
 <li>issues/3331 SQL injection vulnerability</li> 
 <li>online单表不允许设置外键给提醒</li> 
 <li>online菜单如果配置成一级菜单 权限查询不到</li> 
 <li>online报表带参数的菜单配置数据权限无效</li> 
 <li>online表单字段db类型，区分年月日和年月日时分秒</li> 
 <li>online表单默认字段排序规则改造</li> 
 <li>online表单导入，校验不起作用</li> 
 <li>Online表单，部门选择、用户选择、多行文本优化禁用效果</li> 
 <li>Online表单一对多子表，没有按钮权限</li> 
 <li>Online表单一对多tab风格，最大化，高度有问题</li> 
 <li>online自定义按钮未激活状态下，sql/JAVA增强列表显示出问题</li> 
 <li>Online报表查询 会出现java.lang.OutOfMemoryError: Java heap space</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Issues处理</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4GG21">https://gitee.com/jeecg/jeecg-boot/issues/I4GG21</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4HW20">https://gitee.com/jeecg/jeecg-boot/issues/I4HW20</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3159" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3159</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4HZAL">https://gitee.com/jeecg/jeecg-boot/issues/I4HZAL</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4GH9O">https://gitee.com/jeecg/jeecg-boot/issues/I4GH9O</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3126" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3126</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4CMHK">https://gitee.com/jeecg/jeecg-boot/issues/I4CMHK</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3005" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3005</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3162" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3162</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3154" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3154</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3170" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3170</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4IP3D">https://gitee.com/jeecg/jeecg-boot/issues/I4IP3D</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3195" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3195</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4ICIN">https://gitee.com/jeecg/jeecg-boot/issues/I4ICIN</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4K3S1">https://gitee.com/jeecg/jeecg-boot/issues/I4K3S1</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3126" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3126</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3196" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3196</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4JNHR">https://gitee.com/jeecg/jeecg-boot/issues/I4JNHR</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4IFWX">https://gitee.com/jeecg/jeecg-boot/issues/I4IFWX</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3203" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3203</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3225" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3225</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4IRE5">https://gitee.com/jeecg/jeecg-boot/issues/I4IRE5</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4UI2T">https://gitee.com/jeecg/jeecg-boot/issues/I4UI2T</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4KTU1">https://gitee.com/jeecg/jeecg-boot/issues/I4KTU1</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4K3Z7">https://gitee.com/jeecg/jeecg-boot/issues/I4K3Z7</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4KW0G">https://gitee.com/jeecg/jeecg-boot/issues/I4KW0G</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3232" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3232</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3245" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3245</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4MBB3">https://gitee.com/jeecg/jeecg-boot/issues/I4MBB3</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3303" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3303</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3297" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3297</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3293" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3293</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3269" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3269</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4O14W">https://gitee.com/jeecg/jeecg-boot/issues/I4O14W</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3274" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3274</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3311" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3311</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I43TB5">https://gitee.com/jeecg/jeecg-boot/issues/I43TB5</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I45C32">https://gitee.com/jeecg/jeecg-boot/issues/I45C32</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3312" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3312</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4PW73">https://gitee.com/jeecg/jeecg-boot/issues/I4PW73</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4P70L">https://gitee.com/jeecg/jeecg-boot/issues/I4P70L</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3348" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3348</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3347" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3347</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3379" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3379</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3366" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3366</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4RX5V">https://gitee.com/jeecg/jeecg-boot/issues/I4RX5V</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4SWYR">https://gitee.com/jeecg/jeecg-boot/issues/I4SWYR</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3163" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3163</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4I3ZY">https://gitee.com/jeecg/jeecg-boot/issues/I4I3ZY</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3391" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3391</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3412" target="_blank">https://github.com/jeecgboot/jeecg-boot/issues/3412</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">为什么选择 JeecgBoot?</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">开源界“小普元”超越传统商业平台。引领低代码开发模式(OnlineCoding-> 代码生成器 -> 手工MERGE)，低代码开发同时又支持灵活编码， 可以帮助解决Java项目70%的重复工作，让开发更多关注业务。既能快速提高开发效率，节省成本，同时又不失灵活性。</p> 
</blockquote> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
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
<h3 style="margin-left:0; margin-right:0; text-align:left">系统功能模块</h3> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>├─系统管理
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
<h3 style="margin-left:0; margin-right:0; text-align:left">系统截图</h3> 
<p>PC端</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/44fce0865cc8cca093c5e9b8846b8456.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/5a396adc1ff8f074082fa002b88b5915.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/69de4ca50e51c70b6e2f48a530be6eb3.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/df82289dcc7326cdf7adc073d4feab3a.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/b91d1ae6ff0177c728434150bc82a72a.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/5091f504924e235ca0d49196a686c643.png" referrerpolicy="no-referrer"></p> 
<p>手机端</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/320e78580453295b47c97f1c31d0c050.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/0f607ab82712c1f240aa14827091e94e.png" referrerpolicy="no-referrer"></p> 
<p>PAD端</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/0eba9d8fa3a4847599cfe940ff6a80d3.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/7debc83021006b8fdae7f65378fd6492.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/2cc9e7b01a99248033bd5da69802842f.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/62f5720f2fd20b43bdccfaeb469d4460.png" referrerpolicy="no-referrer"></p> 
<p>报表效果</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/55d6dc8d7baef718d3032d6b6d1265ab.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/366b4070ca053dcbd267e0eaa2971950.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/f343d6821db09a2448baef238948a6ca.gif" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/4f5ffd3b8357185a0226b9c317bc2c55.png" referrerpolicy="no-referrer"></p> 
<p>大屏效果</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/60ae64fe29fd6ec26d75a225389b53dd.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">欢迎吐槽，欢迎star~</p> 
<p> </p>
                                        </div>
                                      
</div>
            