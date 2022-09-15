
---
title: 'JeeSite Vue 5.1.0 发布，Spring Boot 快速开发平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b6a11e6130872416da8d7df0883fc1ba13a.png'
author: 开源中国
comments: false
date: Thu, 15 Sep 2022 08:54:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b6a11e6130872416da8d7df0883fc1ba13a.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="margin-left:0; margin-right:0; text-align:start">升级内容</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 初始密码提醒和强制修改初始密码功能</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 上传文件在线预览、SSO 单点登录实例</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 ListSelect 组件增加左树右表功能配置</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 ListSelect 组件自适应表格高度优化</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 TreeSelect 组件字典类型支持树结构展示</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 切换多语言情况下vue前端没有刷新菜单问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 rules: [&#123; required: true &#125;] 时的验证应与直接写 required: true 的验证相同</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 BasicTable 表格翻页时默认自动滚动到顶部</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 接口启用 apiUrlPrefix 参数，axios 可通过 joinPrefix 参数取消添加前缀 /js</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 BPM 组件，并添加请假流程表单审批意见和下一步处理信息</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 字典管理的字典数据数据加停用启用按钮</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 单独设置 pagination: &#123;defaultPageSize: 10 &#125; 不生效问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 在线用户点击重置没有重置操作用户组件问题 #I5NX4V</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 用户管理的二级管理员下部门树缺少权限条件问题</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">升级方法</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">请与 <code>jeesite-vue</code> 代码仓库源码进行同步，合并代码，手动解决冲突代码。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">匹配后端版本为 <code>JeeSite v5.1.0</code></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">后端升级内容</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">升级 spring boot 2.6.10、mybatis 3.5.10、jsqlparser 4.5、druid 1.2.11、spring cloud 2021.0.2、alibaba cloud 2021.0.1.0、more..</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 方法 ValidCodeUtils.generateCaptcha 便捷生成验证码图片</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 job.jobStore.misfireThreshold 参数</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 BPM 获取节点的下一步处理人信息接口</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 OSS 对象存储的文件预览（阿里、腾讯、七牛、MinIO）</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 默认允许 @Table orderBy 排序 设置为空 v4.5.0 v5.1.0</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 开发环境时避免 userfiles 在系统临时路径下，提升开发体验</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 验证文件后缀放到最前面验证，防止秒传的时候没有验证文件后缀</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 数据大屏动态查询接口，输出执行状态等错误信息</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 消息推送接口，在特殊场景下的健壮性</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 BPM 下一步处理人，多选情况下覆盖默认设定处理人</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 BPM 设计器人员选择和角色选择，只显示状态为正常的数据</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 菜单路由 menuRoute 接口，返回扩展字段信息</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 代码生成数值类型最大数值的越界优化 #I5J7UR</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 Cloud 流程异步脚本下报 lazy loading 异常，更新 BpmCloudUtils 文件</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 日志记录 Log 创建时间增加秒</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 黑暗模式下增行编辑表格的单选按钮颜色</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 黑暗模式下的流程节点显示和选择组件的背景颜色</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 BPM 撤回任务，下一个任务是会签的时候，提示流程已经结束的问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 form:fileupload 组件 preview=false 无效问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 tableAndColumn.prefixSuffix 失效问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 文件柜管理修改后未刷新文件列表问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 编辑 job 时 cron 表达式回显不完整问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 Cloud 下 bpm 参数 dueDate 序列化问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">移除 JaxbMapper 工具类，使用 XmlMapper 替代</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">可视化数据大屏升级 Avue-data v2.4 支持快速自定义组件</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">无用户数限制，无在线人数限制</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">后端升级方法</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">修改 <code>pom.xml</code> 文件中的 <code>jeesite-parent</code> 版本号为 <code>5.1.0-SNAPSHOT</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你导入了 <code>jeesite-common</code> 源码项目，请与 <code>git</code> 上的代码进行同步</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你导入了 <code>jeesite-module-core</code> 源码项目，请与 <code>git</code> 上的代码进行同步</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你是跨版本升级，请注意每一个版本的升级方法，业务上有调整的地方进行修改</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">本次跨中版本升级了 Spring Boot 及 Spring Cloud 框架，建议做下完整测试</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">检查 sql 中是否有 ur 关键字，可能会导致 jsqlparser 4.5 不能解析</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">执行 <code>root/package.bat(sh)</code> 打包脚本，强制更新依赖。</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">了解更多</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite 官网地址：http://jeesite.com</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite 在线文档：http://docs.jeesite.com</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite 演示地址：http://demo.jeesite.com</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite <span>Vue</span> 演示地址：http://vue.jeesite.com</p> <p style="margin-left:0; margin-right:0"><img src="https://oscimg.oschina.net/oscnet/up-b6a11e6130872416da8d7df0883fc1ba13a.png" referrerpolicy="no-referrer"></p> <p><img height="901" src="https://oscimg.oschina.net/oscnet/up-2cb6074f9717021e6b7eca4707f443b52c2.png" width="1919" referrerpolicy="no-referrer"></p> </li> 
</ul> 
<p style="color:rgba(255, 255, 255, 0.6); margin-left:0; margin-right:0; text-align:center"> </p>
                                        </div>
                                      
</div>
            