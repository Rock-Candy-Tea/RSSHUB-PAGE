
---
title: 'JeecgBoot 2.4.6 版本发布，基于代码生成器的企业级低代码平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img-blog.csdnimg.cn/img_convert/44fce0865cc8cca093c5e9b8846b8456.png'
author: 开源中国
comments: false
date: Mon, 16 Aug 2021 09:44:00 GMT
thumbnail: 'https://img-blog.csdnimg.cn/img_convert/44fce0865cc8cca093c5e9b8846b8456.png'
---

<div>   
<div class="content">
                                                                                            <h3 style="text-align:left">项目介绍</h3> 
<blockquote> 
 <p>JeecgBoot是一款基于代码生成器的低代码平台！前后端分离架构 SpringBoot2.x，SpringCloud，Ant Design&Vue，Mybatis-plus，Shiro，JWT 支持微服务。强大的代码生成器让前后端代码一键生成! JeecgBoot引领低代码开发模式(OnlineCoding-> 代码生成-> 手工MERGE)， 帮助解决Java项目70%的重复工作，让开发更多关注业务。既能快速提高效率，节省成本，同时又不失灵活性！</p> 
</blockquote> 
<p style="text-align:left"><strong>当前版本</strong>：v2.4.6 | 2021-08-16</p> 
<h3 style="text-align:left">源码下载</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot" target="_blank">https://github.com/jeecgboot/jeecg-boot</a></li> 
 <li><a href="https://gitee.com/jeecg/jeecg-boot">https://gitee.com/jeecg/jeecg-boot</a></li> 
</ul> 
<h3 style="text-align:left">技术文档</h3> 
<ul> 
 <li>官方网站： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.jeecg.com" target="_blank">http://www.jeecg.com</a></li> 
 <li>新手入门： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjeecg.com%2Fdoc%2Fquickstart" target="_blank">http://jeecg.com/doc/quickstart</a></li> 
 <li>在线演示： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fboot.jeecg.com" target="_blank">http://boot.jeecg.com</a></li> 
 <li>技术文档： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jeecg.com" target="_blank">http://doc.jeecg.com</a></li> 
</ul> 
<h3 style="text-align:left">升级日志</h3> 
<blockquote> 
 <p>主要四大方面优化： Online表单功能强化、数据库兼容优化、性能优化、底层依赖升级</p> 
</blockquote> 
<h4 style="text-align:left">新功能升级</h4> 
<ul> 
 <li>新增微服务模块 jeecg-cloud-sentinel</li> 
 <li>新增OAuth2登录，支持企业微信和钉钉的静默授权</li> 
 <li>新增在线用户监控，支持踢掉功能</li> 
 <li>支持自定义首页，通过枚举方式配置</li> 
 <li>升级代码生成器兼容更多数据库</li> 
 <li>升级Online报表分页功能，兼容更多数据库</li> 
 <li>升级在线数据源配置，支持更多数据库</li> 
 <li>Online表单，支持按用户授权</li> 
 <li>Online表单，部门、人员选择组件支持自定义存储显示字段</li> 
 <li>Online表单，支持与积木报表对接</li> 
 <li>Online表单，支持多字段排序</li> 
 <li>Online表单，支持关联查询和关联列表展示</li> 
 <li>Online表单，sql增强支持选中多条数据</li> 
 <li>字典拦截器性能优化，将循环查询改造成一次性查询</li> 
 <li><a href="https://my.oschina.net/u/2429969">@Dict</a> 字典翻译时，增加redis缓存</li> 
 <li>进一步优化前端，压缩online js lib减少1M</li> 
 <li>解决IE兼容问题</li> 
 <li>去掉durid广告</li> 
 <li>接口签名密钥串移到配置文件里</li> 
 <li>SQL注入漏洞处理</li> 
 <li>查询过滤器，值为逗号、空格报错</li> 
 <li>多租户配置升级</li> 
 <li>工具类hutool缩减依赖，只引用必须模块</li> 
 <li>Demo模块默认改成多租户示例</li> 
 <li>代码生成器数据库配置不支持密码加密</li> 
 <li>主键策略修改 IdType.ID_WORKER_STR --> IdType.ASSIGN_ID</li> 
 <li>gateway默认走database、增加swagger关闭配置</li> 
</ul> 
<h4 style="text-align:left">支持数据库</h4> 
<p>Online报表兼容</p> 
<ul> 
 <li>mysql 、mariadb 、oracle 、db2 、h2 、hsql 、sqlite 、postgresql 、sqlserver</li> 
 <li>达梦数据库 、虚谷数据库 、人大金仓 、南大通用</li> 
 <li>Phoenix 、presto 、Gauss 、Firebird、clickhouse 、 OceanBase</li> 
</ul> 
<p>Online表单兼容</p> 
<ul> 
 <li>mysql 、mariadb 、oracle 、postgresql 、sqlserver 、达梦数据库</li> 
</ul> 
<p>代码生成器兼容</p> 
<ul> 
 <li>mysql、mariadb、sqlserver、oracle、postgresql、sqlite、polardb、clickhouse、edb</li> 
 <li>达梦数据库、人大金仓数据库、华为高斯、derby</li> 
</ul> 
<h4 style="text-align:left">升级底层依赖</h4> 
<ul> 
 <li>jimureport-spring-boot-starter 1.3.4-beta >> 1.3.78</li> 
 <li>autopoi 1.3.2 >> 1.3.5</li> 
 <li>jeewx-api 1.4.3 >> 1.4.5</li> 
 <li>codegenerate 1.3.2 >> 1.3.6</li> 
 <li>mybatis-plus 3.4.1 >> 3.4.3.1</li> 
 <li>knife4j-spring-boot-starter:2.0.8 --> 2.0.9</li> 
 <li>fastjson 1.2.75 >> 1.2.76</li> 
 <li>redisson 3.13.6 >> 3.16.1</li> 
</ul> 
<h4 style="text-align:left">Issues修复</h4> 
<ul> 
 <li>修改头像modal <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2593" target="_blank">#2593</a></li> 
 <li>2.4.5升级后出现后端排序报错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2639" target="_blank">#2639</a></li> 
 <li>JS增强怎么实现点击一个表单的列表页面的自定义按钮弹出另一个表单的新增页面呢？<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2580" target="_blank">#2580</a></li> 
 <li>分类字典修改后不自动刷新内容<a href="https://gitee.com/jeecg/jeecg-boot/issues/I3TO07">#I3TO07</a></li> 
 <li>JS增强根据条件怎么限制不让编辑和删除呢？<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2592" target="_blank">#2592</a></li> 
 <li>列表页面限制删除没效果！限制编辑有用 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3V547">#I3V547</a></li> 
 <li>online表单中，下拉多选框控件无法查询 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3N16Y">#I3N16Y</a></li> 
 <li>从2.4.3更新后online表单开发，js增强使用beforeEdit方法，编辑点击无效，删除beforeEdit即可恢复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2647" target="_blank">#2647</a></li> 
 <li>DictAspect字典解析性能问题 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3IB91">#I3IB91</a></li> 
 <li>online表单控件 用户选择控件 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2619" target="_blank">#2619</a></li> 
 <li>关于 token 命名问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2232" target="_blank">#2232</a></li> 
 <li>online表单数据源配置，数据库类型识别错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2671" target="_blank">#2671</a></li> 
 <li>online表单数据源配置，不支持数据库密码加密 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2672" target="_blank">#2672</a></li> 
 <li>2.4.5前台定时任务无法翻页 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2666" target="_blank">#2666</a></li> 
 <li>部门查询问题 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3UD06">#I3UD06</a></li> 
 <li>定时任务, 数量超过12个时分页失效 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3Y1G5">#I3Y1G5</a></li> 
 <li>多租户服务端对请求头校验 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2598" target="_blank">#2598</a></li> 
 <li>JeecgListMixin.js 中loadData没有对request超时做处理 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2584" target="_blank">#2584</a></li> 
 <li>前端用户选择单选无法置空的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2610" target="_blank">#2610</a></li> 
 <li>关于OL排列逻辑的小建议 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F1785" target="_blank">#1785</a></li> 
 <li>online在线表单新增字段时，焦点不会自动定位到最新行数据 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2511" target="_blank">#2511</a></li> 
 <li>【online表单开发】新增数据库字段时，顺序可否放在ID的后面，而不是所属部门的后面 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F1823" target="_blank">#1823</a></li> 
 <li>pgsql 数据库 代码生成，配置 之后 取得表是public下面的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2101" target="_blank">#2101</a></li> 
 <li>postgresql 模式问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2656" target="_blank">#2656</a></li> 
 <li>数据库改成postgresql后，导入数据库表无法使用 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3VN62">#I3VN62</a></li> 
 <li>online表单中主从表权限相互影响 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2680" target="_blank">#2680</a></li> 
 <li>Online 报表配置中，报表SQL语句是多行的时候没法全选SQL语句 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2674" target="_blank">#2674</a></li> 
 <li>自动任务cron表达式生成的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2696" target="_blank">#2696</a></li> 
 <li>2.4.5企业微信中应用中是否可以设置自动登录 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3Z8SE">#I3Z8SE</a></li> 
 <li>Sign 签名校验失败 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2728" target="_blank">#2728</a></li> 
 <li>jeecgboot采用达蒙数据库后，online代码生成模块配置数据库连接无法连接 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2725" target="_blank">#2725</a></li> 
 <li>前端发现BUG <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3ZL4T">#I3ZL4T</a></li> 
 <li>最新代码在开发环境无法在ie11上打开 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2812" target="_blank">#2812</a></li> 
 <li>关于postgresql数据源连接问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2747" target="_blank">#2747</a></li> 
 <li>JEditableTable.formTypes.upload组件，显示错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2691" target="_blank">#2691</a></li> 
 <li>前端省市县组件太旧了，有部分县区没有维护进去 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I40MGS">#I40MGS</a></li> 
 <li>AutoPOI中@EXCEL注解参数没有 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3ZE9E">#I3ZE9E</a></li> 
 <li>已冻结的租户下的用户依然可以登陆 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2796" target="_blank">#2796</a></li> 
 <li>删除租户时,未验证租户是否已被引用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2795" target="_blank">#2795</a></li> 
 <li>JVxeTable用loadNewData问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2784" target="_blank">#2784</a></li> 
 <li>JS增强，beforeDelete无效 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I42OAU">#I42OAU</a></li> 
 <li>IE11打开登录页，无法正常显示，一直转圈 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2841" target="_blank">#2841</a></li> 
 <li>前端省市县组件太旧了，有部分县区没有维护进去 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I40MGS">#I40MGS</a></li> 
 <li>省市区组件内容缺少 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I4074O">#I4074O</a></li> 
 <li>代码优化和规范（ExcelImportServer.class） <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2783" target="_blank">#2783</a></li> 
 <li>多租户安全问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2814" target="_blank">#2814</a></li> 
 <li>导入mixins缺少加载中的动画，数据量比较大时，导入进行中没有反应，建议加上this.loading = true进行控制 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3O4YL">#I3O4YL</a></li> 
 <li>根据数据权限前缀获取允许导出的表格字段查询，期望查询是一条数据，应用户有两个角色，查出两个角色 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3ZKGU">#I3ZKGU</a></li> 
 <li>beforeDelete无效 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2815" target="_blank">#2815</a></li> 
 <li>2.4.5 online内嵌子表，设置按时间范围查询时，日期选择框叠加 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2764" target="_blank">#2764</a></li> 
 <li>请问，online表单设置按钮，绑定JAVA增强或SQL增强，无法多选，只能一次选一条 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2766" target="_blank">#2766</a></li> 
 <li>sql增强问题，如果操作多行，例如截图中，多选后，可以激活多行被勾选的数据。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2743" target="_blank">#2743</a></li> 
 <li>在jeecg中如何使用自定义按钮，选中一行或多行数据后，打印jimu单据，未找到教程，请大佬指点 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2739" target="_blank">#2739</a></li> 
 <li>登录系统，系统管理-系统通告-新增-“标题”处存在存储型XSS <a href="https://gitee.com/jeecg/jeecg-boot/issues/I40W1W">#I40W1W</a></li> 
 <li>钉钉同步到本地的人员没有状态，导致同步之后无法登录 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3ZC2L">#I3ZC2L</a></li> 
 <li>nacos修改了端口号不生效，启动时候还是默认端口8848 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2819" target="_blank">#2819</a></li> 
 <li>使用autopoi导入提示缺少方法 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2868" target="_blank">#2868</a></li> 
 <li>JPopup组件在modal中使用报错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2729" target="_blank">#2729</a></li> 
 <li>2.4.5 没有用记管理没有同步钉钉功能 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I44JE9">I44JE9</a></li> 
 <li>mybatis plus 3.4.1版本 @SqlParser 注解过时，近期有考虑升级到mybatis plus 3.4.3吗？ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2840" target="_blank">#2840</a></li> 
 <li>在线报表导出的合计数据与页面上显示的不一致 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2852" target="_blank">#2852</a></li> 
 <li>BusinessException能否前端提示异常信息 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I42UOQ">#I42UOQ</a></li> 
 <li>第三方APP消息测试问题 “字段太长,超出数据库字段的长度” 解决方案 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjeecgboot%2Fjeecg-boot%2Fissues%2F2898" target="_blank">#2898</a></li> 
</ul> 
<h3 style="text-align:left">系统截图</h3> 
<p>PC端</p> 
<p style="text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/44fce0865cc8cca093c5e9b8846b8456.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/5a396adc1ff8f074082fa002b88b5915.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/69de4ca50e51c70b6e2f48a530be6eb3.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/df82289dcc7326cdf7adc073d4feab3a.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/b91d1ae6ff0177c728434150bc82a72a.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/5091f504924e235ca0d49196a686c643.png" referrerpolicy="no-referrer"></p> 
<p>手机端</p> 
<p style="text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/320e78580453295b47c97f1c31d0c050.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/0f607ab82712c1f240aa14827091e94e.png" referrerpolicy="no-referrer"></p> 
<p>PAD端</p> 
<p style="text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/0eba9d8fa3a4847599cfe940ff6a80d3.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/7debc83021006b8fdae7f65378fd6492.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/2cc9e7b01a99248033bd5da69802842f.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/62f5720f2fd20b43bdccfaeb469d4460.png" referrerpolicy="no-referrer"></p> 
<p>报表效果</p> 
<p style="text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/55d6dc8d7baef718d3032d6b6d1265ab.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/366b4070ca053dcbd267e0eaa2971950.png" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/f343d6821db09a2448baef238948a6ca.gif" referrerpolicy="no-referrer"> <img alt src="https://img-blog.csdnimg.cn/img_convert/4f5ffd3b8357185a0226b9c317bc2c55.png" referrerpolicy="no-referrer"></p> 
<p>大屏效果</p> 
<p style="text-align:left"><img alt src="https://img-blog.csdnimg.cn/img_convert/60ae64fe29fd6ec26d75a225389b53dd.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">欢迎吐槽，欢迎star~</p>
                                        </div>
                                      
</div>
            