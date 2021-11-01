
---
title: '低代码平台，JeecgBoot v3.0 版本发布—新里程牌开始，迎接 VUE3 版本到来'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img-blog.csdnimg.cn/img_convert/44fce0865cc8cca093c5e9b8846b8456.png'
author: 开源中国
comments: false
date: Sun, 31 Oct 2021 19:34:00 GMT
thumbnail: 'https://img-blog.csdnimg.cn/img_convert/44fce0865cc8cca093c5e9b8846b8456.png'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0; margin-right:0; text-align:left">项目介绍</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">JeecgBoot是一款基于代码生成器的低代码平台！前后端分离架构 SpringBoot2.x，SpringCloud，Ant Design&Vue，Mybatis-plus，Shiro，JWT 支持微服务。强大的代码生成器让前后端代码一键生成! JeecgBoot引领低代码开发模式(OnlineCoding-> 代码生成-> 手工MERGE)， 帮助解决Java项目70%的重复工作，让开发更多关注业务。既能快速提高效率，节省成本，同时又不失灵活性！</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>当前版本</strong>：v3.0 | 2021-11-01</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">源码下载</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot" target="_blank">https://github.com/jeecgboot/jeecg-boot</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot">https://gitee.com/jeecg/jeecg-boot</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">技术文档</h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>官方网站：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jeecg.com" target="_blank">http://www.jeecg.com</a></li> 
 <li>新手入门：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjeecg.com%2Fdoc%2Fquickstart" target="_blank">http://jeecg.com/doc/quickstart</a></li> 
 <li>技术文档：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jeecg.com" target="_blank">http://doc.jeecg.com</a></li> 
 <li>在线演示：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fboot.jeecg.com" target="_blank">http://boot.jeecg.com</a></li> 
 <li>在线演示(VUE3 beta)：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fboot3.jeecg.com" target="_blank">http://boot3.jeecg.com</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">升级日志</h3> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">迎接VUE3到来的衔接版本，后台为VUE3兼容做了一些优化和升级工作，并彻底重构了Online查询逻辑，支持更多数据库含国产和解决SQL漏洞问题。Vue3.0新版研发工作进入尾声，2022年将是JeecgBoot的VUE3里程碑元年。</p> 
</blockquote> 
<h4 style="margin-left:0; margin-right:0; text-align:left">严重Bug修复</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Online三级联动组件，列表翻译有问题</li> 
 <li>Online表单权限控制页面打开报错<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4E0NO">I4E0NO</a></li> 
 <li>Online功能测试详情里的ID隐藏</li> 
 <li>Online表单重复rowKey属性定义，导致IE11不兼容</li> 
 <li>Online js增强点击无效<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2912" target="_blank">#2912</a></li> 
 <li>WebMvcConfiguration升级，后端将long转为string后，导致分页报错和时间类型等问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3058" target="_blank">#3058</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3057" target="_blank">#3057</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3051" target="_blank">#3051</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3041" target="_blank">#3041</a><span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4BNGY">I4BNGY</a></li> 
 <li>升级mybatisPlus后，多租户插件导致SqlServer兼容问题，sql解析多了一个字段column<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2915" target="_blank">#2915</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">低代码升级</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>升级积木报表到最新版本 1.4.0</li> 
 <li>升级代码生成器，支持vue3页面的生成，vue3版本即将出炉！</li> 
 <li>升级Minidao 支持配置多数据源</li> 
 <li>为了VU3新版UI出炉，后端做了兼容性改造（相关请求、代码生成器、生成器模板、权限接口等）</li> 
 <li>重构Online表单、Online报表查询逻辑，兼容更多数据库(包括国产数据库)</li> 
 <li>重构Online表单同步逻辑，兼容更多数据库(包括国产数据库)</li> 
 <li>解决Online表单和Online报表的查询SQL注入漏洞问题</li> 
 <li>Online表单java增强新增http模式</li> 
 <li>Online表单关联查询问题，只勾选一个附表，结果生成了两个附表的sql</li> 
 <li>Online报表配置SQL解析，不支持 “ >= ”</li> 
 <li>Online子表增加组件textarea</li> 
 <li>Online 用户组件,支持唯一校验</li> 
 <li>Online存在服务器目录遍历漏洞，限制只有admin用户才有权限<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3060" target="_blank">#3060</a></li> 
 <li>online单表加入外键修改失败问题<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4BXOH">I4BXOH</a><span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I49F81">I49F81</a></li> 
 <li>Online报表支持安全模式配置，数据源选择在安全模式下为必填</li> 
 <li>【Online表单】修复ERP风格不能保存的问题</li> 
 <li>【Online报表】字典和href互斥</li> 
 <li>online表单，附表用户选择组件支持属性 &#123;“multiSelect”:false&#125;</li> 
 <li>前端地域翻译写法简化</li> 
 <li>JVXETable新增后台查询三级联动示例</li> 
 <li>JVXETable新增多级联动</li> 
 <li>ShiroToken验证异常AuthorizationException不能被Spring统一拦截（过滤器异常）<a href="https://gitee.com/jeecg/jeecg-boot/issues/I40JKA">I40JKA</a></li> 
 <li>代码生成器一对多，子表组件支持选择部门、选择用户控件生成</li> 
 <li>Online表单支持自定义弹出表单宽度</li> 
 <li>升级Mysql驱动包，解决MySQL JDBC XXE漏洞(CVE-2021-2471)</li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Issues修复</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Online表单对接积木报表接口参数不匹配问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3106" target="_blank">#3106</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3072" target="_blank">#3072</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2994" target="_blank">#2994</a></li> 
 <li>授权首页菜单后，自定义首页功能不生效<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3069" target="_blank">#3069</a></li> 
 <li>第三方APP消息测试问题 “字段太长,超出数据库字段的长度” 解决方案<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2898" target="_blank">#2898</a></li> 
 <li>SQL to parse以后与sqlserver不兼容<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2915" target="_blank">#2915</a></li> 
 <li>online java 增强当设置的增强过多时，显示异常<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2880" target="_blank">#2880</a></li> 
 <li>online文本太长时，会遮挡页面<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I44F0R">issues/I44F0R</a></li> 
 <li>oline在线内嵌子表主表与附表，设置扩展参数限制宽度不起作用<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2881" target="_blank">#2881</a></li> 
 <li>online点击详情，出现id，好难看<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2922" target="_blank">#2922</a></li> 
 <li>升级2.4.6后Online表单开发无法使用“一对多”的“ERP主题”<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I468JY">I468JY</a></li> 
 <li>JVXETable联动展示与选择BUG<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2867" target="_blank">#2867</a></li> 
 <li>2.4.6 钉钉人员同步时手机号未能正确同步<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I471XE">I471XE</a></li> 
 <li>微服务版集成企业微信单点登录<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2959" target="_blank">#2959</a></li> 
 <li>JEditable 下子表 addBefore()方法，在其中自定义调用其他方法不生效如何解决<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2939" target="_blank">#2939</a></li> 
 <li>字段label设置过长被遮盖怎么解决？<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3046" target="_blank">#3046</a></li> 
 <li>Online表单,两个在线表单tab之间切换，产生多余查询<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3016" target="_blank">#3016</a></li> 
 <li>在线表单功能，内嵌主题“高级查询”按钮权限设置完不起作用<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3020" target="_blank">#3020</a></li> 
 <li>自定义按钮如何选多条数据？？<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3032" target="_blank">#3032</a></li> 
 <li>online表单用户组件控件类型 支持唯一性校验规则<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2949" target="_blank">#2949</a></li> 
 <li>online在线表单加载字典错误导致页面崩溃<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I49F4F">#I49F4F</a></li> 
 <li>在多数据源管理，添加新数据源时mysql5.7和Postgresql冲突<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2918" target="_blank">#2918</a></li> 
 <li>数据库脚本中，sys_dict_item表“数据库类型”的item_value值重复问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2914" target="_blank">#2914</a></li> 
 <li>JTreeSelect在树结构没有子节点的情况下依然显示展开箭头<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2885" target="_blank">#2885</a></li> 
 <li>扩展配置的弹窗宽度和默认全屏对 内嵌子表 和 TAB主题 无效<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I46AQR">I46AQR</a></li> 
 <li>Online报表配置-SQL解析，不支持 “ >= ”<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2985" target="_blank">#2985</a></li> 
 <li>同步钉钉人员到本地错误<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2990" target="_blank">#2990</a></li> 
 <li>ShiroToken验证异常AuthorizationException不能被Spring统一拦截（过滤器异常）<a href="https://gitee.com/jeecg/jeecg-boot/issues/I40JKA">#I40JKA</a></li> 
 <li>联动组件显示问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3084" target="_blank">#3084</a></li> 
 <li>导入定时任务，并不会被启动和调度，需要手动点击启动，才会加入调度任务中<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2986" target="_blank">#2986</a></li> 
 <li>Online表单如果是附表，控件类型选项缺少了多行文本、富文本框等<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2948" target="_blank">#2948</a></li> 
 <li>【Online表单开发】移除表单，没有删除关联表数据<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2988" target="_blank">#2988</a></li> 
 <li>省市三级联动列表无法显示<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I48I0E">I48I0E</a><span> </span>-【2.4.6】在线开发的排序存在打开新页面tab而带前面tab页有点击过排序字段会导致报错<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I47FEZ">I47FEZ</a></li> 
 <li>JEditableTable 表头多选框如何默认选中<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I49IE7">I49IE7</a></li> 
 <li>消息队列中报微服务Feign异常<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I49ENE">I49ENE</a></li> 
 <li>Online在线表单保存失败问题<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I49F81">I49F81</a></li> 
 <li>online表单权限控制页面打开报错<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4E0NO">I4E0NO</a></li> 
 <li>附表部门、用户控件有问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3088" target="_blank">#3088</a></li> 
 <li>autopoi模板导出，赋值的方法建议增加空判断或抛出异常说明。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3005" target="_blank">#3005</a></li> 
 <li>jpopup 表格key重复BUG<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3121" target="_blank">#3121</a></li> 
 <li>oracle路由网关新增小bug<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4EV2J">I4EV2J</a></li> 
 <li>Online 存在SQL注入问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3075" target="_blank">#3075</a></li> 
 <li>online 报表中类型配置为日期（yyyy-MM-dd ），但是实际展示为日期时间格式(yyyy-MM-dd HH🇲🇲ss)<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3042" target="_blank">#3042</a></li> 
 <li>online表单，附表用户选择器&#123;"multiSelect":false&#125;不生效，单表可以生效<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3036" target="_blank">#3036</a></li> 
 <li>字典表翻译注解缓存未更新<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F3061" target="_blank">#3061</a></li> 
 <li>附表控件类型没有时间控件<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4C854">I4C854</a></li> 
 <li>online报表查询条件配置了数据字典情况下首次选择下拉框的值，查询后，无法清空查询值<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4C23E">I4C23E</a></li> 
 <li>websocket报错<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4C0MU">I4C0MU</a></li> 
 <li>网关动态更新路由报错<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I4C5QR">I4C5QR</a></li> 
 <li>微服务下路由网关删除或禁用某项，仍可以从网关路由到对应的服务中<span> </span><a href="https://gitee.com/jeecg/jeecg-boot/issues/I47DEM">I47DEM</a></li> 
 <li>路由网关禁用Demo配置后，系统仍可以通过网关路由到Demo服务。<a href="https://gitee.com/jeecg/jeecg-boot/issues/I49457">I49457</a></li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Online重构兼容数据库</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>mysql 、mariadb 、oracle 、db2 、h2 、hsql 、sqlite 、postgresql 、sqlserver</li> 
 <li>达梦数据库 、虚谷数据库 、人大金仓 、南大通用</li> 
 <li>Phoenix 、presto 、Gauss 、Firebird、clickhouse 、 OceanBase</li> 
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
                                        </div>
                                      
</div>
            