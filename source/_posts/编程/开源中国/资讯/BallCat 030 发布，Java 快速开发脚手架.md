
---
title: 'BallCat 0.3.0 发布，Java 快速开发脚手架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6869'
author: 开源中国
comments: false
date: Thu, 09 Sep 2021 09:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6869'
---

<div>   
<div class="content">
                                                                                            <p>BallCat 0.3.0 已经发布，Java 快速开发脚手架。</p> 
<p>此版本更新内容包括：</p> 
<h3>Warning</h3> 
<ul> 
 <li>多个模块包名调整，注意重新 import 对应路径</li> 
 <li>国际化重构，改动较大，注意对应代码调整。国际化使用文档参看：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.ballcat.cn%2Fguide%2Ffeature%2Fi18n.html" target="_blank">http://www.ballcat.cn/guide/feature/i18n.html</a></li> 
 <li>由于 <strong>ballcat-common-conf</strong> 的删除，非 admin 服务中的 mybatis-plus 的相关配置，如分页插件，批量插入方法的注入，需要按需添加。</li> 
 <li>操作日志优化，修改了 <code>OperationLogHandler</code> 的相关方法，如果有自定义 OperationLogHandler ，需要注意同步更新</li> 
</ul> 
<h3>Added</h3> 
<ul> 
 <li>feat: 国际化功能的默认支持，新增 <strong>ballcat-i18n</strong> 相关模块，以便提供默认的业务国际化实现方式</li> 
 <li>feat: 登录用户名密码错误时的错误消息国际化处理</li> 
 <li>feat: <strong>ballcat-common-redis</strong> 针对 PUB/SUB 新增 <code>MessageEventListener</code> 接口，<strong>ballcat-spring-boot-starter-redis</strong> 中会自动注册所有实现 <code>MessageEventListener</code> 接口的监听器</li> 
 <li>feat: <strong>ballcat-common-redis</strong> 中的 <code>@CacheDel</code> 注解，新增 multiDel 属性，方便批量删除缓存</li> 
 <li>feat: 新增 <strong>ballcat-common-idempotent</strong> 幂等模块</li> 
 <li>feat: 针对 hibernate-validation 校验的提示消息，支持使用 &#123;&#125;，占位替代 defaultMessage</li> 
 <li>feat: <strong>ballcat-common-core</strong> 中默认新增了 <code>CreateGroup</code> 和 <code>UpdateGroup</code> 接口，方便分组校验使用</li> 
 <li>feat: 新增 <strong>ballcat-spring-boot-starter-web</strong> 模块，该模块基于 <code>spring-boot-starter-web</code>, 并使用 undertow 作为默认的嵌入式容器，且将 <strong>ballcat-common-conf</strong> 中对 web 应用的配置增强，如全局异常管理，以及 Sql 防注入处理，jackson 的默认配置等配置移动到此项目中</li> 
 <li>feat: <strong>ballcat-extend-mybatis-plus</strong> 模块中，为了支持连表查询的条件构建，新增 <code>OtherTableColumnAliasFunction</code> ，方便使用 <code>LambdaAliasQueryWrapperX</code> 进行关联表查询条件的构建</li> 
 <li>feat: <strong>ballcat-spring-boot-starter-easyexcel</strong> 支持导出时进行 Excel 头信息的国际化处理，使用 <code>&#123;&#125;</code> 进行占位表示，使用示例可参看 I18nData 的导出使用</li> 
 <li>feat: <strong>ballcat-spring-boot-starter-swagger</strong> 配置的扫描路径 <code>basePackage</code> ，支持使用 <code>,</code> 进行多包名的分割扫描</li> 
 <li>feat: <strong>ballcat-spring-boot-starter-datascope</strong> 中的数据权限控制注解 @DataPermission 扩展支持在 Mapper 之外使用，且支持方法嵌套调用时使用不同的 @DataPermission 环境</li> 
</ul> 
<h3>Changed</h3> 
<ul> 
 <li> <p>refactor: <strong>ballcat-common-conf</strong> 内原先对于 mybati-plus 的自动填充、分页插件、以及批量插入方法注入的配置移动到 <strong>ballcat-admin-core</strong> 中</p> </li> 
 <li> <p>refactor: <code>SpELUtils</code> 改名为 <code>SpelUtils</code>，并移动到 <strong>ballcat-common-util</strong> 模块中</p> </li> 
 <li> <p>refactor: <code>ApplicationContextHolder</code> 改名为 <code>SpringUtils</code>，并移动到 <strong>ballcat-common-util</strong> 模块中</p> </li> 
 <li> <p>refactor: <strong>ballcat-spring-boot-starter-log</strong> 中拆分出 <strong>ballcat-common-log</strong> 模块，解决在 log-biz 模块中需要引入 starter 的问题，部分代码的包名有变更</p> </li> 
 <li> <p>refactor: <strong>ballcat-spring-boot-starter-redis</strong> 中拆分出 <strong>ballcat-common-redis</strong> 模块</p> </li> 
 <li> <p>refactor: 重构原先的国际化 i18n 功能，新增 <strong>ballcat-common-i18n</strong> 模块，移除原先的 <strong>ballcat-extend-i18n</strong> 模块</p> </li> 
 <li> <p>pref: 取消 <strong>ballcat-spring-boot-starter-web</strong> 中 <strong>spring-security-core</strong> 的传递依赖</p> </li> 
 <li> <p>fix: 修复当查询一个不存在的系统配置后，由于缓存空值，导致添加配置后依然查询不到的问题</p> </li> 
 <li> <p>pref: 菜单查询的返回类型修改为 SysMenuPageVO</p> </li> 
 <li> <p>fix: 修复 excel 导出的 content-type 和实际文件类型不匹配的问题</p> </li> 
 <li> <p>fix: 提高缓存切面的 Order，使其在事务提交后执行更新或删除操作，防止并发导致缓存数据错误</p> </li> 
 <li> <p>pref: 菜单支持删除 icon</p> </li> 
 <li> <p>fix: 修复当菜单 id 修改时，未级联修改其子菜单的父级 id 的问题</p> </li> 
 <li> <p>pref: 优化操作日志，改为在方法执行前获取方法参数信息，防止用户在执行方法时将方法入参修改了</p> </li> 
 <li> <p>pref: <strong>ballcat-admin-core</strong> 中默认扩展 springboot 默认的 TaskExecutor 配置，将拒绝策略从抛出异常修改为使用当前线程执行</p> </li> 
 <li> <p>refactor: 移动 TreeNode 模型到 common-util 包中，以便减少 common-util 包的依赖</p> </li> 
 <li> <p>refactor: <strong>ballcat-spring-boot-starter-xss</strong> 抽象出 XssCleaner 角色，用于控制 Xss 文本的清除行为，方便用户自定义</p> </li> 
 <li> <p>pref: 用户登陆时的错误信息返回原始的细节信息，而不是全部返回用户名密码错误</p> </li> 
 <li> <p>fix: <strong>ballcat-system-biz</strong> websocket 包名拼写错误修复</p> </li> 
</ul> 
<h3>Removed</h3> 
<ul> 
 <li>移除 <strong>ballcat-common-conf</strong>，相关代码拆分入 <strong>ballcat-spring-boot-starter-web</strong> 和 <strong>ballcat-admin-core</strong></li> 
</ul> 
<h3>Dependency</h3> 
<ul> 
 <li>Bump jsoup from 1.13.1 to 1.14.2</li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/ballcat-projects/ballcat/releases/0.3.0">https://gitee.com/ballcat-projects/ballcat/releases/0.3.0</a></p>
                                        </div>
                                      
</div>
            