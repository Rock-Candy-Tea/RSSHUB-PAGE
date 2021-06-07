
---
title: 'JeecgBoot 低代码平台 2.4.5 版本发布，钉钉与企业微信集成版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-34f20499033be8c19b6ccd491657dc933dd.png'
author: 开源中国
comments: false
date: Mon, 07 Jun 2021 09:52:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-34f20499033be8c19b6ccd491657dc933dd.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="text-align:left">项目介绍</h3> 
<blockquote> 
 <p>JeecgBoot是一款基于代码生成器的低代码平台！前后端分离架构 SpringBoot2.x，SpringCloud，Ant Design&Vue，Mybatis-plus，Shiro，JWT 支持微服务。强大的代码生成器让前后端代码一键生成! JeecgBoot引领低代码开发模式(OnlineCoding-> 代码生成-> 手工MERGE)， 帮助解决Java项目70%的重复工作，让开发更多关注业务。既能快速提高效率，节省成本，同时又不失灵活性！</p> 
</blockquote> 
<p style="text-align:left"><strong>当前版本</strong>：v2.4.5 | 2021-06-07</p> 
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
 <p>此版本无缝集成了钉钉和企业微信，实现了用户与部门的同步、公告和系统消息推送支持推送到钉钉和企业微信，快速建立与第三方APP的互通</p> 
</blockquote> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.jeecg.com%2F2292480" target="_blank">JeecgBoot与钉钉企业微信集成文档</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1Y541147m1%3Fp%3D25" target="_blank">JeecgBoot零基础对接企业微信</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1Y541147m1%3Fp%3D24" target="_blank">JeecgBoot零基础对接钉钉</a></li> 
</ul> 
<p>新功能升级</p> 
<ul> 
 <li>无缝集成钉钉，实现用户和部门同步，公告和系统消息推送支持推送到钉钉</li> 
 <li>无缝集成企业微信，实现用户和部门同步，公告和系统消息推送支持推送到企业微信</li> 
 <li>钉钉和企业微信消息推送，支持普通文本和图文两种类型</li> 
 <li>Online新增支持按照部门进行权限授权</li> 
 <li>Online导入功能支持校验规则，友好提示成功多少行失败多少行</li> 
 <li>Online图表、Online报表、Online报表加缓存，提升低代码性能</li> 
 <li>Online popup支持单选和多选设置</li> 
 <li>代码生成器生成popup只支持单选和多选配置</li> 
 <li>Online表字典下拉支持异步搜索</li> 
 <li>优化微服务应用下存在表字段需要字典翻译时加载缓慢问题</li> 
 <li>提供新的部门管理列表，支持异步加载数据</li> 
 <li>定时任务支持一个类，开启多个定时任务</li> 
 <li>【页面改造】登录、注册相关代码改成v-model绑定模式</li> 
 <li>【页面改造】其他改造成v-model的代码（常见案例、通讯录、定时任务、校验规则、填值规则）</li> 
 <li>【页面改造】 登录页面拆分重构优化</li> 
 <li>JVXETable 支持默认出现输入框选项配置</li> 
 <li>积木报表升级到最新版本</li> 
 <li>查询过滤器，支持多字段排序</li> 
 <li>Online报表 sql解析把大写字母变成小写的了，导致查询没有结果</li> 
</ul> 
<p>Issues修复</p> 
<ul> 
 <li>自定义树控件在代码生成显示问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2507" target="_blank"> #2507</a></li> 
 <li>redis-cluster集群模式在开启密码时启动报NOAUTH Authentication required错误 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3QNIC">issues/I3QNIC</a></li> 
 <li>autopoi增加新属性show=true <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3RPDM">issues/I3RPDM</a></li> 
 <li>视图给自定义按钮添加sql增强后，sql语句生效，但再次进入sql增强页面，sql语句无法显示，也就无法修改 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3SP1K">issues/I3SP1K</a></li> 
 <li>online，下拉搜索框无法在表单提交页面使用 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I1VW3E">issues/I1VW3E</a></li> 
 <li>JS增强根据条件怎么限制不让编辑和删除呢？<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2592" target="_blank"> #2592</a></li> 
 <li>redis配置max-active为0后，前端启动时读取不到验证码<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2428" target="_blank"> #2428</a></li> 
 <li>autopoi导入excel 如果单元格被设置边框，即使没有内容也会被当做是一条数据导入<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2484" target="_blank"> #2484</a></li> 
 <li>excel 导入时，小数点后的数据会丢失 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2555" target="_blank">#2555</a></li> 
 <li>自定义树控件的表单里的外键直接显示id不显示name的问题<a href="https://gitee.com/jeecg/jeecg-boot/issues/I3HTFI">issues/I3HTFI</a></li> 
 <li>online在线表单缓存与数据库不一致的问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2561" target="_blank"> #2561</a></li> 
 <li>j-upload 组件无法接收父组件传值<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2529" target="_blank"> #2529</a></li> 
 <li>cron表达式解析失败<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2569" target="_blank"> #2569</a></li> 
 <li>【报表设计器】地图使用静态数据无变化<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2528" target="_blank"> #2528</a></li> 
 <li>JEditableTable,当 type=popup 时,popup里面的数据排序问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2545" target="_blank">#2545</a></li> 
 <li>JEditableTable的setValues方法，被赋值的列如果为file、upload类型，会提示找不到当前列 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3OKKH">issues/I3OKKH</a></li> 
 <li>JVxeTable组件的拖拽排序功能异常 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2551" target="_blank">#2551</a></li> 
 <li>Online内嵌风格子表访问授权问题修复</li> 
 <li>Online组合报表无法选择图表（分页问题）</li> 
 <li>Online表单同步数据库报错 Could not parse mapping document: null</li> 
 <li>Oracle数据库原类型是nvarchar2 但是同步后变成varchar2</li> 
 <li>Excel 导入注解name包含下划线抛出空指针异常 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2004" target="_blank">#2004</a></li> 
 <li>用户名称检查有安全漏洞，可以字典猜测破解密码 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2362" target="_blank">#2362</a></li> 
 <li>Nginx会忽略租户tenant_id，建议把下划线改成-号 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I38V6W">issues/I38V6W</a></li> 
 <li>BindingResult无法使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2219" target="_blank">#2219</a></li> 
 <li>nacos分组配置问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2355" target="_blank">#2355</a></li> 
 <li>积木报表sql数据集，带参条件解析错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2306" target="_blank">#2306</a></li> 
 <li>升级2.4.3后，微服务网关路由更新bug <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3CNED">issues/I3CNED</a></li> 
 <li>OnLine报表ref属性链接页面，由于在调用页面翻页，导致被ref的页面为空，其实是有数据的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2315" target="_blank">#2315</a></li> 
 <li>打成jar 使用 -Dfile.encoding=utf-8启动控制台和日志文件乱码 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3AVHC">I3AVHC</a></li> 
 <li>微服务模式部署下，nacos的账户密码如果不使用默认提供的nacos/nacos，会导致gateway读取路由信息失败 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2375" target="_blank">#2375</a></li> 
 <li>JImageUpload组件单张无法预览 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2382" target="_blank">#2382</a></li> 
 <li>online报表配置如何实现多租户 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3CL75">issues/I3CL75</a></li> 
 <li>用户管理模块新增、编辑接口事务不一致，会导致脏数据产生 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F1812" target="_blank">#1812</a></li> 
 <li>FormTypes.popup重复点击会将子表值置空 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2117" target="_blank">#2117</a></li> 
 <li>日志里把具体的文件加上吧 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3BJDQ">issues/I3BJDQ</a></li> 
 <li>minio上传文件，文件名包含点的时候拼接文件名有问题 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3CLFL">issues/I3CLFL</a></li> 
 <li>一对多代码生成（ERP模板）生成的子表实体ApiModel注释中value为附表名称 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2365" target="_blank">#2365</a></li> 
 <li>Online表单无法按部门授权 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2342" target="_blank">#2342</a></li> 
 <li>redis监控的token获取了2次不同的值，导致后台报错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2405" target="_blank">#2405</a></li> 
 <li>关于多租户的数据权限配置问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2425" target="_blank">#2425</a></li> 
 <li>打开报表设计器报错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2438" target="_blank">#2438</a></li> 
 <li>代码生成器导入数据库表错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2456" target="_blank">#2456</a></li> 
 <li>macOS 环境 SnowflakeIdWorker#generateId 初始化时空指针<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2FJimuReport%2Fissues%2F184" target="_blank"> #184</a></li> 
 <li>online报表，给某一列设置合计属性后，每页会多出一条空行，导致分页总数合计不对，还会导致ref子页中的数据每页都加一个空行 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2390" target="_blank">#2390</a></li> 
 <li>内嵌子表导入异常 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3ESNH">issues/I3ESNH</a></li> 
 <li>JEditableTable 查看时，内容过长显示有问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2435" target="_blank">#2435</a></li> 
 <li>JEditableTable 当 type: FormTypes.popup,时 能不能向组件内传参数 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3BXH3">issues/I3BXH3</a></li> 
 <li>配置minio上传，遇到没有后缀的文件名会报错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2434" target="_blank">#2434</a></li> 
 <li>JVXETable在列表popup是否支持传参？ <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3J1UY">issues/I3J1UY</a></li> 
 <li>通过扩展参数设置popup是否支持多选，Jpopup.vue未使用扩展参数<a href="https://gitee.com/jeecg/jeecg-boot/issues/I3IA7Z">issues/I3IA7Z</a></li> 
 <li>ONLINE表单 修改添加 没有数据的时候，sql异常 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3HTON">issues/I3HTON</a></li> 
 <li>online表单开发查询配置下拉搜索框，placeholder会出现‘请选择qq’ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2500" target="_blank">#2500</a></li> 
 <li>JVXETable获取当前行，row参数出现undefined <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2501" target="_blank">#2501</a></li> 
 <li>online 表单，选中行，操作后，选中行让然存在，需要手动点清空<a href="https://gitee.com/jeecg/jeecg-boot/issues/I3FLJ3">issues/I3FLJ3</a></li> 
 <li>不支持mariaDB数据库，近期会考虑支持吗<a href="https://gitee.com/jeecg/jeecg-boot/issues/I3QID1">issues/I3QID1</a></li> 
 <li>文件上传建议可根据当前业务类型分类文件 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2531" target="_blank">#2531</a></li> 
 <li>提交一个在线代码生成的bug <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3EL13">issues/I3EL13</a></li> 
 <li>账号安全问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2449" target="_blank">#2449</a></li> 
 <li>请教为什么要限制同个任务类名 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2460" target="_blank">#2460</a></li> 
 <li>JDictSelectTag选择后不能触发验证 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2472" target="_blank">#2472</a></li> 
 <li>附件下载的文件报400 <a href="https://gitee.com/jeecg/jeecg-boot/issues/I3NQQW">issues/I3NQQW</a></li> 
 <li>代码生成树表haschild存在问题，为什么不在add时就给haschild赋值为0<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzhangdaiscott%2Fjeecg-boot%2Fissues%2F2558" target="_blank"> #2558</a></li> 
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
<p style="text-align:left">欢迎吐槽，欢迎star~</p>
                                        </div>
                                      
</div>
            