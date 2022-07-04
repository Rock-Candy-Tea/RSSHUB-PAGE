
---
title: 'Diboot v2.6.0 已经发布，轻代码开发平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2938'
author: 开源中国
comments: false
date: Mon, 04 Jul 2022 10:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2938'
---

<div>   
<div class="content">
                                                                                            <p>Diboot v2.6.0 已经发布，轻代码开发平台</p> 
<p>此版本更新内容包括：</p> 
<h1>Diboot v2.6.0 release notes</h1> 
<h2>内核 diboot-core & core-starter v2.6.0</h2> 
<p>新增：</p> 
<ul> 
 <li>支持达梦、人大金仓 数据库</li> 
 <li>@BindCount注解，用于子项汇总计数的绑定场景</li> 
 <li>新增Pagination.isPaginationParam用于过滤请求参数是否为分页参数</li> 
 <li>新增MapUtils工具类，用于Oracle、DM等需要忽略大小写的Map取值等场景</li> 
</ul> 
<p>优化：</p> 
<ul> 
 <li>绑定注解的condition中支持添加主表扩展条件，如 "AND this.gender = 'M' "</li> 
 <li>BindQuery空值处理优化，支持指定构建IsNull</li> 
 <li>优化获取schema及数据库类型的逻辑，规避不兼容问题</li> 
 <li>BeanUtils.buildTree支持非id命名主键，指定各节点名</li> 
 <li>Context监听切换为ApplicationReadyEvent，避免特定情况下被刷新问题</li> 
 <li>Spring类型转换器优化，支持LocalDateTime等，支持扩展</li> 
 <li>BeanUtils get*Property支持从map对象中提取属性值</li> 
 <li>缓存接口增加synchronized，避免多线程场景的潜在问题</li> 
 <li>升级依赖版本：spring boot 2.7.0, mybatis-plus 3.5.2</li> 
</ul> 
<h2>IAM组件 diboot-IAM-starter v2.6.0</h2> 
<p>新增：</p> 
<ul> 
 <li>支持达梦、人大金仓 数据库</li> 
</ul> 
<p>优化：</p> 
<ul> 
 <li>默认为无状态，不再依赖session，以降低集群部署场景复杂度</li> 
 <li>token 缓存与刷新替换逻辑优化</li> 
 <li>接口与权限码的提取与检查校验逻辑优化重构，更合理更高效</li> 
 <li>数据权限范围控制预置实现类优化为前端岗位-数据权限设置的后端完整实现</li> 
</ul> 
<p>修复：</p> 
<ul> 
 <li>fix: 多租户场景下，默认service在保存账号时无法setTenantId的问题</li> 
</ul> 
<h2>文件组件 diboot-file-starter v2.6.0</h2> 
<p>新增：</p> 
<ul> 
 <li>支持达梦、人大金仓 数据库</li> 
</ul> 
<p>优化：</p> 
<ul> 
 <li>升级easy-excel组件至3.1.1</li> 
</ul> 
<h2>消息通知组件 diboot-message-starter v2.6.0</h2> 
<p>新增：</p> 
<ul> 
 <li>支持达梦、人大金仓 数据库</li> 
</ul> 
<p>优化：</p> 
<ul> 
 <li>message组件简化优化（全新变量注解，变量类可为任意类，注解自动提取）</li> 
</ul> 
<h2>定时任务组件 diboot-scheduler-starter v2.6.0</h2> 
<p>新增：</p> 
<ul> 
 <li>支持达梦、人大金仓 数据库</li> 
</ul> 
<h2>移动端组件 diboot-mobile-starter v2.6.0</h2> 
<p>新增：</p> 
<ul> 
 <li>支持达梦、人大金仓 数据库</li> 
</ul> 
<h2>移动端前端 diboot-mobile-ui v2.6.0</h2> 
<p>优化：</p> 
<ul> 
 <li>优化表单提交，增加防误触控制</li> 
</ul> 
<p>修复：</p> 
<ul> 
 <li>修复移动端分页同一页面多次加载数据问题</li> 
</ul> 
<h2>PC前端 diboot-antd-admin v2.6.0</h2> 
<p>优化：</p> 
<ul> 
 <li>优化资源权限的权限码接口配置功能，更简单</li> 
 <li>优化角色权限选择配置</li> 
 <li>验证码增加traceId标识串，以剔除后端session依赖</li> 
 <li>打包移除cdn，调整富文本的无效cdn</li> 
</ul> 
<p>修复：</p> 
<ul> 
 <li>fix：antdv版本人员无法选择的问题</li> 
</ul> 
<h2>PC前端 diboot-element-admin v2.6.0</h2> 
<p>优化：</p> 
<ul> 
 <li>优化资源权限的权限码接口配置功能，更简单</li> 
 <li>优化角色权限选择配置</li> 
 <li>验证码增加traceId标识串，以剔除后端session依赖</li> 
 <li>打包移除cdn，调整富文本的无效cdn</li> 
</ul> 
<p>修复：</p> 
<ul> 
 <li>fix：组织机构页面特定情况下出现的无响应问题</li> 
</ul> 
<h2>开发工具 diboot-devtools v2.6.0</h2> 
<p>新增：</p> 
<ul> 
 <li>支持达梦、人大金仓 数据库</li> 
 <li>支持多组件数据联动的配置与生成</li> 
 <li>支持前端搜索日期时间的范围生成配置</li> 
</ul> 
<p>优化：</p> 
<ul> 
 <li>优化前端生成：列表页生成配置支持直观切换为树列表形式</li> 
 <li>优化统计图表生成的逻辑</li> 
 <li>优化建表规则提示，命名要求更规范</li> 
</ul> 
<p>修复：</p> 
<ul> 
 <li>fix：配置各层代码生成至不同路径的设置未生效问题</li> 
 <li>fix: 修复关联子表单批量中，删除只删除最后一行问题</li> 
</ul> 
<h2>微服务版（企业版） diboot-cloud v2.6.0</h2> 
<p>新增：</p> 
<ul> 
 <li>支持达梦、人大金仓 数据库</li> 
 <li>接口与权限码的提取与检查校验逻辑优化重构，更合理更高效</li> 
 <li>登录页增加验证码</li> 
</ul> 
<p>优化：</p> 
<ul> 
 <li>升级依赖版本: spring-cloud 2021.0.3，spring-boot 2.6.8</li> 
</ul> 
<h2>工作流版（企业版）diboot-workflow v2.6.0</h2> 
<p>新增：</p> 
<ul> 
 <li>支持达梦、人大金仓 数据库（扩展包）</li> 
 <li>支持移动端（扩展包，基于diboot-mobile-ui）</li> 
 <li>支持多租户</li> 
 <li>候选组支持选部门</li> 
 <li>新增多实例加签、减签支持</li> 
 <li>新增动态分配下一节点执行人支持分配候选组</li> 
 <li>支持流程图版本回退</li> 
 <li>支持消息中间事件</li> 
 <li>动态表单支持业务对象选择器组件配置与集成</li> 
 <li>选项型组件选项数据支持级联数据联动功能</li> 
</ul> 
<p>优化：</p> 
<ul> 
 <li>升级diboot基础组件及 admin-ui 至 2.6.0</li> 
 <li>优化流程配置候选部分UI，简化操作</li> 
 <li>优化动态分配用户</li> 
 <li>优化流程图展示效果</li> 
 <li>固定表单命名统一为静态表单</li> 
 <li>支持静态表单与动态表单混用并在流程中支持多个静态表单</li> 
 <li>动态表单子表单校验与数据处理优化</li> 
 <li>优化代码：逻辑下放，完善注释等</li> 
</ul> 
<p>修复：</p> 
<ul> 
 <li>修复串行多实例不支持分配用户的问题</li> 
 <li>修复流程基础信息无法更新问题</li> 
 <li>修复网关可视化配置字段值可能存在条件解析失败的问题</li> 
 <li>修复XML新导入流程中后续节点字段权限配置可能存在必须配读写权限的问题</li> 
</ul> 
<p>详细内容参考：<a href="https://gitee.com/link?target=https%3A%2F%2Fwww.diboot.com" target="_blank">https://www.diboot.com</a></p> 
<p>详情查看：<a href="https://gitee.com/dibo_software/diboot/releases/v2.6.0">https://gitee.com/dibo_software/diboot/releases/v2.6.0</a></p>
                                        </div>
                                      
</div>
            