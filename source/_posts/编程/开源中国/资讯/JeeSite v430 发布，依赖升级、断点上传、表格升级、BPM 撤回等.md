
---
title: 'JeeSite v4.3.0 发布，依赖升级、断点上传、表格升级、BPM 撤回等'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://mmbiz.qpic.cn/mmbiz_png/MSghjRkCh6x2kd5CBkQT82UCKPD6ARtGMvUibqaobtDj3s84S6a7ib4AZa4onAxYWpAkgRRibicfvkgtFW58lB0vPQ/640?wx_fmt=png'
author: 开源中国
comments: false
date: Fri, 16 Jul 2021 00:18:00 GMT
thumbnail: 'https://mmbiz.qpic.cn/mmbiz_png/MSghjRkCh6x2kd5CBkQT82UCKPD6ARtGMvUibqaobtDj3s84S6a7ib4AZa4onAxYWpAkgRRibicfvkgtFW58lB0vPQ/640?wx_fmt=png'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="text-align:start">升级内容</h3> 
<p style="text-align:start"><strong>框架升级</strong></p> 
<ul> 
 <li> <p>升级 Spring Boot 2.5.2、MyBatis 3.5.6、Jackson 2.12.3、Druid 1.2.6、Beetl 3.3 等等其他众多依赖</p> </li> 
 <li> <p>升级 Spring Cloud 2020.0.3、Alibaba Cloud 2021.1、Nacos 2.0、Seata 1.4.2 等等其他众多依赖</p> </li> 
 <li> <p>新增 readwriteSplitting 读写分离配置(不依赖shardingsphere)、高性能、支持复杂SQL、两种读库负载均衡算法、支持附加数据源读写分离、支持读写分离数据源事务</p> </li> 
 <li> <p>新增 mybatisDaoAndDataSourceMappings 配置，指定 MyBatisDao 与数据源映射，支持使用 yml 配置的方式，即可指定 Dao 对应的数据源；数据源名支持变量，包括：&#123;corpCode&#125;、&#123;userCode&#125;、&#123;userCache中的Key名&#125;、&#123;yml或sys_config中的Key名&#125;，支持分库分模式的租户模式</p> </li> 
 <li> <p>新增 ajaxParamName、ajaxHeaderName、sessionIdHeaderName、sessionIdCookieSecure、writeCookieParamName、rememberMeHeaderName、contentSecurityPolicy 参数，详情可看 yml 对应注释</p> </li> 
 <li> <p>新增 gen.checkTableExists 参数，支持启动项目时，不检查平台表是否存在，不执行数据库自动更新程序</p> </li> 
 <li> <p>新增 job.jobStore.driverDelegateClass 参数，可自定义 Quartz 方言</p> </li> 
 <li> <p>在线文档 swagger ui 替换 knife4j ui 升级体验</p> </li> 
 <li> <p>分库分表框架 ShardingSphere 升级到 5.0</p> </li> 
 <li> <p>i18n 语言设置，支持客户端存储和读取</p> </li> 
 <li> <p>新增 LDAP 认证登录</p> </li> 
 <li> <p>支持神通数据库</p> </li> 
</ul> 
<p style="text-align:start"><strong>功能模块</strong></p> 
<ul> 
 <li> <p>代码生成：生成环节新增子表展示，生成结果的界面预览，更直观展示生成的内容</p> </li> 
 <li> <p>表单实例：新增9栅格布局，方便支持3列表单，第一个标签对齐演示</p> </li> 
 <li> <p>表单实例：新增A4纸格式的表格表单/单据实例/表单打印等实例</p> </li> 
 <li> <p>表单实例：新增下拉框级联选择组件，城市联动例子</p> </li> 
 <li> <p>主题美化：主子表样式美化，可编辑表格样式美化</p> </li> 
 <li> <p>用户管理：导入导出问的人比较多，放到醒目位置</p> </li> 
 <li> <p>用户管理：搜索条件新增，按角色查询框</p> </li> 
 <li> <p>用户类型：授权角色，支持其它用户类型角色授权</p> </li> 
 <li> <p>字典管理：增加图标设置，下拉框选项前显示图标</p> </li> 
 <li> <p>模块管理：限制内置模块不能创建代码，防止创建空模块的误解</p> </li> 
 <li> <p>文件预览：增加预览图片窗口的上一张和下一张功能</p> </li> 
 <li> <p>内容管理：栏目和站点添加快捷进入站点链接</p> </li> 
 <li> <p>菜单管理：地址变量新增 corpCode、corpName、userCache 中的 Key</p> </li> 
 <li> <p>BPM 内核 Flowable 升级到 6.6.0 版本，忽略 Flowable 的数据库版本更新错误检查</p> </li> 
 <li> <p>BPM 新增导出和导入流程 zip 压缩包（包含：流程bpmn、流程图、表单、流程事件）</p> </li> 
 <li> <p>BPM 新增撤回/取回/撤销功能，当下一步未办理时，可进行该操作</p> </li> 
 <li> <p>BPM 新增退回快捷键：退回到发起人、退回到上一步、退回到任意环节</p> </li> 
 <li> <p>BPM 流程退回环节列表优化，只能选择上游节点</p> </li> 
 <li> <p>BPM 增加流程选项的一些工具提示</p> </li> 
 <li> <p>BPM 脚本编辑器离开的光标隐藏，美化界面</p> </li> 
 <li> <p>BPM 增加脚本安全简单检查代码</p> </li> 
 <li> <p>BPM 打通业务和任务，支持从我相关的流程和业务表单里进入，进行快速办理任务</p> </li> 
 <li> <p>BPM API 方面新增通过业务找当前用户的任务接口</p> </li> 
 <li> <p>BPM 增加 CMD 权限验证，提高接口调用的安全性</p> </li> 
 <li> <p>BPM 优化已知异常，控制台不显示无用的错误信息，方便审计</p> </li> 
 <li> <p>BPM 表单模式的时候，待办、已办、我相关的页面，改进点击没有进行弹窗的问题</p> </li> 
 <li> <p>BPM 模型设计器，如果不是删除全部，则恢复第一个历史数据，作为新版本使用。删除的版本存入历史版本</p> </li> 
 <li> <p>BPM 模型设计器，增加自定义 flowable.modelerMybatisMappingFile 设置</p> </li> 
 <li> <p>BPM 模型设计器，增加分页功能，数据多的时候提升性能</p> </li> 
 <li> <p>数据大屏：内核升级，新增导出、新增数据源、新增模板库、众多功能改进</p> </li> 
</ul> 
<p style="text-align:start"><strong>工具组件</strong></p> 
<ul> 
 <li> <p>DataGrid 新增右侧锁定列，演示详见用户管理列表；</p> </li> 
 <li> <p>DataGrid 支持小屏幕或大屏幕情况下自动隐藏锁定列；</p> </li> 
 <li> <p>DataGrid 支持多表头情况下的锁定列；</p> </li> 
 <li> <p>DataGrid 支持分组表的展开和折叠锁定列；</p> </li> 
 <li> <p>DataGrid 完成ie9+及其他所有浏览器的锁定列测试；</p> </li> 
 <li> <p>DataGrid 列名为actions的操作列自动为锁定列；</p> </li> 
 <li> <p>DataGrid 子表新增单选框和复选框的支持</p> </li> 
 <li> <p>DataGrid 新增支持 url+postData 方式的排序功能</p> </li> 
 <li> <p>DataGrid 给操作列增加一些默认值 fixed:true,frozen:true,sortable:false,title:false 所以去掉代码里的默认设置</p> </li> 
 <li> <p>DataGrid 编辑的表格默认表格左上角显示加号；</p> </li> 
 <li> <p>DataGrid 新增新增行属性和事件：插入行位置、插入位置源、插入行后回调</p> </li> 
 <li> <p>DataGrid 默认启用表单验证，layout 添加 libs: [‘validate’]（升级注意）</p> </li> 
 <li> <p>DataGrid 优化体验，点击分页控件后数据滚动到顶部</p> </li> 
 <li> <p>DataGrid 的行 id 将为空，导致代码生成的列出现非编辑状态的问题</p> </li> 
 <li> <p>$(element).select2() 替换为 js.select2() 方便统筹</p> </li> 
 <li> <p>Excel 新增 RoleListType 导入导出类型转换类</p> </li> 
 <li> <p>Excel 改进导入导出，属性为对象的时候，不用再进行判断为空并new对象了</p> </li> 
 <li> <p>xssFilter 去掉 UReport 的单引号和双引号的替换</p> </li> 
 <li> <p>xssFilter 和 sqlFilter 增加附加参数，方便追踪调用来源</p> </li> 
 <li> <p>JsonMapper 增加日期类型的默认转换格式，并兼容 @JsonFormat 注解</p> </li> 
 <li> <p>PropertiesUtils 增加 getPropertyToBoolean、getPropertyToInteger 方法</p> </li> 
 <li> <p>ReflectUtils 支持级联对象为空的方法赋值</p> </li> 
 <li> <p>CacheUtils 增加 get 带 ttl 参数的方法</p> </li> 
 <li> <p>OAuth2 新增 oauth2.</p> <p>.className 配置参数，支持自定义客户端</p> </li> 
 <li> <p>ObjectUtils.toDouble 支持带 * 的值，方便字节赋值，如：<code>10*1024*1024</code></p> </li> 
 <li> <p>FileUploadUtils.saveFileUpload 增加 entity 参数，以便支持 @RequestBody 的文件上传接口</p> </li> 
 <li> <p><code>上传文件</code> 新增 上传断点续传 file.checkpoint，支持多线程并发分片上传</p> </li> 
 <li> <p><code>上传文件</code> 新增 是否启用秒传开关 file.checkmd5，关闭后不检查 MD5</p> </li> 
 <li> <p>强化 md5File 截取前后内容，更确保唯一性，支持读取超大文件秒级完成</p> </li> 
 <li> <p>JustAuth 升级到 1.16.1</p> </li> 
 <li> <p>WxJava 升级到 4.0.9</p> </li> 
</ul> 
<p style="text-align:start"><strong>其它改进</strong></p> 
<ul> 
 <li> <p>IE 下的登录输入框右侧的图标被叉号盖住的问题优化</p> </li> 
 <li> <p>文件上传优化 ie10 ie11 支持h5，就不需要安装flash</p> </li> 
 <li> <p>优化体验，弹窗内容高度与设定高度差值小于50的自动修正高度</p> </li> 
 <li> <p>改进消息推送高并发下报错 ConcurrentModificationException 问题</p> </li> 
 <li> <p>记住用户名 Cookie 增加过期时间（如果不指定可能会 Session 失效后过期）</p> </li> 
 <li> <p>如果默认数据源，不是 DruidDataSource 数据源，则创建新的 job 数据源</p> </li> 
 <li> <p>优化 preInsert 的 this.updateBy 属性赋值 改为 this.setUpdateBy 方法赋值</p> </li> 
 <li> <p>将带下划线的请求头，改为减号，统一规范，省去一些设置</p> </li> 
 <li> <p>修正当 job.autoStartup 为 false 的时候，导致永久不能启动的问题</p> </li> 
 <li> <p>SpringBoot 2.4 以后不支持 .json 后缀的 URL 的问题改进</p> </li> 
 <li> <p>data-layer-full=”true” 有时无效的问题修正</p> </li> 
 <li> <p>form:treeselect 的搜索 change 加一点延迟</p> </li> 
</ul> 
<p style="text-align:start"><strong>Cloud微服务</strong></p> 
<ul> 
 <li> <p>移除 ribbon 替换为 loadbalancer，移除 hystrix 替换为 sentinel，升级时注意依赖管理</p> </li> 
 <li> <p>更新 Cloud 版本的代码生成器（强劲生成，提供微服务模块生成和增删改查生成，无需手写一行代码）</p> </li> 
 <li> <p>新增 test3 模块，用来展示代码生成示例结果，该模块完全没有手写，全部为生成的</p> </li> 
 <li> <p>POM 依赖，结构优化调整，增加 parent-web 项目，方便统一维护 web 项目必须的一些依赖</p> </li> 
 <li> <p>修正 EmpUtils.getOffice() 的时候报找不到 employeeService 的问题 v4.2.3+</p> </li> 
 <li> <p>开箱即用，简化 Seata 分布式事务处理的操作</p> </li> 
</ul> 
<h3 style="text-align:start">升级方法</h3> 
<ul> 
 <li> <p>升级前请先备份数据库，因为升级 Flowable 后，可能会导致旧项目启动异常</p> </li> 
 <li> <p>修改 <code>pom.xml</code> 文件中的 <code>jeesite-parent</code> 版本号为 <code>4.3.0-SNAPSHOT</code></p> </li> 
 <li> <p>如果你导入了 <code>jeesite-common</code> 源码项目，请与 <code>git</code> 上的代码进行同步</p> </li> 
 <li> <p>如果你导入了 <code>jeesite-module-core</code> 源码项目，请与 <code>git</code> 上的代码进行同步</p> </li> 
 <li> <p>升级 SpringBoot 2.5 文档：https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-2.5-Release-Notes</p> </li> 
 <li> <p>升级 ShardingSphere 5.0 文档：https://github.com/apache/shardingsphere/releases/tag/5.0.0-beta</p> </li> 
 <li> <p>DataGrid 给操作列增加了 <code>fixed:true</code> 默认值，检查所有列表的<code>操作列</code>是否显示完整</p> </li> 
 <li> <p>如果 DataGrid 页面的 layout 添加了 <code>libs: ['validate']</code>，将会默认启用搜索条件的表单验证</p> </li> 
 <li> <p>请求头重命名：原 Header 名称 __ajax、__sid，更改为 x-ajax、x-token、x-remember</p> </li> 
 <li> <p>Swagger ui 替换 knife4j ui，不支持 API 名称中带 <code>/</code> 斜杠，请替换为 <code>-</code> 减号</p> </li> 
 <li> <p>重命名类 CasAuthenticationFilter 为 CasFilter；FormAuthenticationFilter 为 FormFilter；PermissionsAuthorizationFilter 为 PermissionsFilter；RolesAuthorizationFilter 为 RolesFilter</p> </li> 
 <li> <p>Cloud 升级 nacos 2.0.2，升级文档：https://nacos.io/zh-cn/docs/2.0.0-upgrading.html</p> </li> 
 <li> <p>Cloud 移除 ribbon 替换为 loadbalancer，移除 hystrix 替换为 sentinel，升级时注意依赖管理</p> </li> 
 <li> <p>Cloud 替换 jeesite-cloud-42 为 jeesite-cloud-43，注意配置文件引用路径</p> </li> 
 <li> <p>本次升级了众多依赖，请完整测试。</p> </li> 
</ul> 
<p style="text-align:center"><img src="https://mmbiz.qpic.cn/mmbiz_png/MSghjRkCh6x2kd5CBkQT82UCKPD6ARtGMvUibqaobtDj3s84S6a7ib4AZa4onAxYWpAkgRRibicfvkgtFW58lB0vPQ/640?wx_fmt=png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            