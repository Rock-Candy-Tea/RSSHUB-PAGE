
---
title: 'JeecgBoot 3.4.2 版本发布，Vue3 版本大升级'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img-blog.csdnimg.cn/img_convert/44fce0865cc8cca093c5e9b8846b8456.png'
author: 开源中国
comments: false
date: Mon, 26 Sep 2022 10:43:00 GMT
thumbnail: 'https://img-blog.csdnimg.cn/img_convert/44fce0865cc8cca093c5e9b8846b8456.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="margin-left:0; margin-right:0; text-align:left">项目介绍</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">JeecgBoot 是一款企业级的低代码平台！前后端分离架构 SpringBoot2.x，SpringCloud，Ant Design&Vue，Mybatis-plus，Shiro，JWT 支持微服务。强大的代码生成器让前后端代码一键生成！JeecgBoot 引领低代码开发模式 (OnlineCoding-> 代码生成 -> 手工 MERGE)， 帮助解决 Java 项目 70% 的重复工作，让开发更多关注业务。既能快速提高效率，节省成本，同时又不失灵活性！</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>当前版本</strong>：v3.4.2 | 2022-09-26</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">源码下载</h3> 
<p>前端源码</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3" target="_blank">https://github.com/jeecgboot/jeecgboot-vue3</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecgboot-vue3">https://gitee.com/jeecg/jeecgboot-vue3</a></li> 
</ul> 
<p>后台源码</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot" target="_blank">https://github.com/jeecgboot/jeecg-boot</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot">https://gitee.com/jeecg/jeecg-boot</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">升级日志</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">重点升级 ant-design-vue 到 3.2.12、升级 vite 等前端依赖；优化基础功能、修复 bug 等；本次未升级 online 相关功能。</p> 
</blockquote> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Vue3 UI 升级</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>升级 ant-design-vue 到 3.2.12、升级 vite 等前端依赖</li> 
 <li>升级 antd3 后，moment 全部替换为 dayjs</li> 
 <li>websocket 功能优化</li> 
 <li>表单支持右侧嵌入评论区、附件区</li> 
 <li>代码格式化调整</li> 
 <li>自动检查 vue3, 自动切换 vue3 库表</li> 
 <li>菜单列表支持通过菜单名模糊查询</li> 
 <li>支持年度控件</li> 
 <li>同步 vben 部分代码</li> 
 <li>升级 antd3 后一系列兼容改造工作</li> 
 <li>表单 label 支持自定义显示字数，超长截取显示</li> 
 <li>Table 表格自定义排序字段例子（角色列表）</li> 
 <li>用户设置上传头像不生效解决</li> 
 <li>Table 的全屏功能有问题，默认关闭</li> 
 <li>系统通知，未读的排到最上面</li> 
 <li>编译后主题色切换不生效黑屏的问题</li> 
 <li>系统通知图标，没有随着主题色变</li> 
 <li>修复 labelWidth 设置无效的问题</li> 
 <li>form 表单 label 宽度支持设置，默认去掉一些表单的宽度设置，默认自适应</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">升级 and3 后兼容问题（遇到请修改）</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Table 废弃了 slots 插槽，需要修改写法（目前老用法可以继续用，会有警告）</li> 
 <li>Form.tem 只能收集一个表单项的数据，如果有多个表单项，会导致收集搭乱 (item 里面有多个元素，会报警告)</li> 
 <li>antd3 采用 dayjs 替换掉了 moment，升级需要搜索 moment 换成 dayjs（dayjs 与 moment 语法差不多，替换不难）</li> 
 <li>针对 Table 废弃 slots 插槽和 Form.tem 只能一个表单项，代码尚未改造完，虽然有警告，但不影响使用（antd3 做了兼容）</li> 
 <li>Tabs 的动画默认没有了，如果出现问题，需要加上 animated 参数</li> 
 <li>样式更名.ant-tabs-bar —> .ant-tabs-nav</li> 
 <li>下拉类型的 SelectTypes 更名为 SelectValue</li> 
 <li>更多升级日志见<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.antdv.com%2Fdocs%2Fvue%2Fmigration-v3-cn" target="_blank">从 ant-design-vue 2.x 版本升级到 ant-design-vue 3.x 版本</a></li> 
 <li>form 表单 label 宽度设置问题修复，如表单宽度效果有问题，可以去掉宽度设置</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">新功能升级</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>新版系统通知风格（支持直接打开业务单）</li> 
 <li>消息模板新增 Markdown 类型</li> 
 <li>在线文件存储，文档预览文档采用 pdf 模式预览</li> 
 <li>钉钉和企业微信推送支持 markdown 格式</li> 
 <li>Swagger2 文档，token 保存问题</li> 
 <li>文件存储 minio 上传失败，提示错误不准确（禁止特殊文件类型上传）</li> 
 <li>重构系统通知 WebSocket 代码，简化逻辑</li> 
 <li>新建部门的 ID 规则改造为 IdWorker</li> 
 <li>jdbc 连接地址漏洞问题修复</li> 
 <li>/actuator/shiro 默认不排除，有漏洞风险</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">修复 bug</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>vben 更新<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F90" target="_blank">issues/90</a></li> 
 <li>代码下载下来后，没有代码提示<span> </span><a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5PCKT">issues/I5PCKT</a></li> 
 <li>vue3 版本升级<span> </span><a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5LXZA">issues/I5LXZA</a></li> 
 <li>vue3 版本升级<span> </span><a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5BFTY">issues/I5BFTY</a></li> 
 <li>下拉多选、年份选择更新<span> </span><a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5C9BY">issues/I5C9BY</a></li> 
 <li>用户列表 判断是否是 admin 的功能无效<span> </span><a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5N591">issues/I5N591</a></li> 
 <li>部门选择弹框出来数据有遮挡<span> </span><a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5IWFM">issues/I5IWFM</a></li> 
 <li>vue3 模板生成报错<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I5MU66">issues/I5MU66</a></li> 
 <li>到首页动画就进不去了<span> </span><a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5MTLQ">issues/I5MTLQ</a></li> 
 <li>更换头像失败<span> </span><a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5Q2W8">issues/I5Q2W8</a></li> 
 <li>代码生成器里选择 3 列表单，运行后 lable 的宽度很窄<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I5L3SK">issues/I5L3SK</a></li> 
 <li>表格展示 右侧选项时，列选项为空<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F139" target="_blank">issues/139</a></li> 
 <li>JVxeTable 的 JVxeTypes.inputNumber 类型项目无法输入小数点<span> </span><a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5R7ZI">issues/I5R7ZI</a></li> 
 <li>online 表单新增报错<span> </span><a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5ITL3">issues/I5ITL3</a></li> 
 <li>vue3 版本中，online 报表 动态参数设置无效<span> </span><a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5HB7P">issues/I5HB7P</a></li> 
 <li>主附表启用联合查询后导入有问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F111" target="_blank">issues/111</a></li> 
 <li>JVxeTable 中的 inputNumber 不能输入小数<span> </span><a href="https://gitee.com/jeecg/jeecgboot-vue3/issues/I5IHN7">issues/I5IHN7</a></li> 
 <li>积木报表无法保存<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I5J3QO">issues/I5J3QO</a></li> 
 <li>Excel 注解中不支持超链接，但文档中支持<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I5I840">issues/I5I840</a></li> 
 <li>代码生成 主子表 vue3 模板报错<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I5I5EL">issues/I5I5EL</a></li> 
 <li>redis 配置连接池问题<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I5KQMA">issues/I5KQMA</a></li> 
 <li>Shiro 版本和 postgresql 驱动版本漏洞修复<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3882" target="_blank">issues/3882</a></li> 
 <li>无法使用年份范围选择器<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecgboot-vue3%2Fissues%2F153" target="_blank">issues/153</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">为什么选择 JeecgBoot?</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">开源界 “小普元” 超越传统商业平台。引领低代码开发模式 (OnlineCoding-> 代码生成器 -> 手工 MERGE)，低代码开发同时又支持灵活编码， 可以帮助解决 Java 项目 70% 的重复工作，让开发更多关注业务。既能快速提高开发效率，节省成本，同时又不失灵活性。</p> 
</blockquote> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>采用最新主流前后分离框架（SpringBoot+Mybatis-plus+Ant-Design+Vue），容易上手；代码生成器依赖性低，灵活的扩展能力，可灵活实现二次开发；</li> 
 <li>开发效率很高，采用代码生成器，单表数据模型和一对多 (父子表)、树列表等数据模型，增删改查功能自动生成，菜单配置直接使用（前端代码和后端代码都一键生成）；</li> 
 <li>代码生成器提供强大模板机制，支持自定义模板风格。目前提供四套风格模板（单表两套、一对多两套）</li> 
 <li>封装完善的用户、角色、菜单、组织机构、数据字典、在线定时任务等基础功能。强大的权限机制，支持访问授权、按钮权限、数据权限、表单权限等</li> 
 <li>零代码在线开发能力，在线配置表单、在线配置报表、在线配置图表、在线设计表单</li> 
 <li>常用共通封装，各种工具类 (定时任务，短信接口，邮件发送，Excel 导入导出等), 基本满足 80% 项目需求</li> 
 <li>简易 Excel 导入导出，支持单表导出和一对多表模式导出，生成的代码自带导入导出功能</li> 
 <li>集成简易报表工具，图像报表和数据导出非常方便，可极其方便的生成图形报表、pdf、excel、word 等报表；</li> 
 <li>采用前后分离技术，页面 UI 精美，针对常用组件做了封装：时间、行表格控件、截取显示控件、报表组件，编辑器等等</li> 
 <li>查询过滤器：查询功能自动生成，后台动态拼 SQL 追加查询条件；支持多种匹配方式（全匹配 / 模糊查询 / 包含查询 / 不匹配查询）；</li> 
 <li>数据权限（精细化数据权限控制，控制到行级，列表级，表单字段级，实现不同人看不同数据，不同人对同一个页面操作不同字段</li> 
 <li>在线配置报表（无需编码，通过在线配置方式，实现曲线图，柱状图，数据等报表）</li> 
 <li>页面校验自动生成 (必须输入、数字校验、金额校验、时间空间等);</li> 
 <li>提供单点登录 CAS 集成方案，项目中已经提供完善的对接代码</li> 
 <li>表单设计器，支持用户自定义表单布局，支持单表，一对多表单、支持 select、radio、checkbox、textarea、date、popup、列表、宏等控件</li> 
 <li>专业接口对接机制，统一采用 restful 接口方式，集成 swagger-ui 在线接口文档，Jwt token 安全验证，方便客户端对接</li> 
 <li>接口安全机制，可细化控制接口授权，非常简便实现不同客户端只看自己数据等控制</li> 
 <li>高级组合查询功能，在线配置支持主子表关联查询，可保存查询历史</li> 
 <li>提供各种系统监控，实时跟踪系统运行情况（监控 Redis、Tomcat、jvm、服务器信息、请求追踪、SQL 监控）</li> 
 <li>消息中心（支持短信、邮件、微信推送等等）</li> 
 <li>集成 Websocket 消息通知机制</li> 
 <li>提供 APP 发布方案：</li> 
 <li>支持多语言，提供国际化方案；</li> 
 <li>数据变更记录日志，可记录数据每次变更内容，通过版本对比功能查看历史变化</li> 
 <li>平台 UI 强大，实现了移动自适应</li> 
 <li>平台首页风格，提供多种组合模式，支持自定义风格</li> 
 <li>提供简单易用的打印插件，支持谷歌、IE 浏览器等各种浏览器</li> 
 <li>示例代码丰富，提供很多学习案例参考</li> 
 <li>采用 maven 分模块开发方式</li> 
 <li>支持菜单动态路由</li> 
 <li>权限控制采用 RBAC（Role-Based Access Control，基于角色的访问控制）</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">系统截图</h3> 
<p>PC 端</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/44fce0865cc8cca093c5e9b8846b8456.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/5a396adc1ff8f074082fa002b88b5915.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/69de4ca50e51c70b6e2f48a530be6eb3.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/df82289dcc7326cdf7adc073d4feab3a.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/b91d1ae6ff0177c728434150bc82a72a.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/5091f504924e235ca0d49196a686c643.png" referrerpolicy="no-referrer"></p> 
<p>手机端</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/320e78580453295b47c97f1c31d0c050.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/0f607ab82712c1f240aa14827091e94e.png" referrerpolicy="no-referrer"></p> 
<p>PAD 端</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/0eba9d8fa3a4847599cfe940ff6a80d3.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/7debc83021006b8fdae7f65378fd6492.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/2cc9e7b01a99248033bd5da69802842f.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/62f5720f2fd20b43bdccfaeb469d4460.png" referrerpolicy="no-referrer"></p> 
<p>报表效果</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/55d6dc8d7baef718d3032d6b6d1265ab.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/366b4070ca053dcbd267e0eaa2971950.png" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/f343d6821db09a2448baef238948a6ca.gif" referrerpolicy="no-referrer"><span> </span><img alt src="https://img-blog.csdnimg.cn/img_convert/4f5ffd3b8357185a0226b9c317bc2c55.png" referrerpolicy="no-referrer"></p> 
<p>大屏效果</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/60ae64fe29fd6ec26d75a225389b53dd.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">欢迎吐槽，欢迎 star~</p> 
<p> </p>
                                        </div>
                                      
</div>
            