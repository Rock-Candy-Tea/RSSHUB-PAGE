
---
title: 'JeeSite Vue 5.0.4 发布，Spring Boot 快速开发平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b6a11e6130872416da8d7df0883fc1ba13a.png'
author: 开源中国
comments: false
date: Tue, 28 Jun 2022 09:02:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b6a11e6130872416da8d7df0883fc1ba13a.png'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0; margin-right:0; text-align:start">升级内容</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 ListSelect 列表选择组件</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 锁屏密码支持账号密码解锁</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 后台页面黑暗主题，流程图黑暗主题下调色</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 避免文件名过长挤出操作列</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 文件下载显示原文件名</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 checkImgType 支持 base64 格式</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 上传文件个数判断差 1 个</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 Switch 为 false 的时候 foramt 不调用问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 展开的表格不显示水平滚动条问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 展开的表格双击展开图标的时候显示加载框问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 使用展开表格时拖拽报错问题</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">升级方法</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">请与 <code>jeesite-vue</code> 代码仓库源码进行同步，合并代码，手动解决冲突代码。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">前端与后端版本不同，匹配后端版本为 <code>JeeSite v5.0.2</code></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">后端升级内容</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">Spring Boot 2.5.13、Shiro 1.9.0 等等</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 Dao 批量操作等系列的方法</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 BootStrap CSS 的黑暗主题模式</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 Spring configuration metadata yml 配置信息友好提示</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 是否启用默认 Servlet 映射（启用后可访问 webapp 下的静态资源访问）</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 支持 Spring Boot 带减号的 key 写法，自动转换为驼峰格式</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 BPM 查询全部待办、已办流程数据接口</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 OAuth2 state 缓存集群共享</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 CacheUtils exists 方法</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 去掉 Service 类上的事务注解，方便用户二开开定义</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 切换租户条件改为权限方式，有租户管理权限的既有切换租户权限</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 ListUtils.pageList 共 1 页的时候直接返回</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 mime 加载，避免第三方包里含 mine.types 导致加载不正确</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 Swagger 文档配置，内置功能增加中文解释。</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 已经登录的账号，正常返回登录失败信息，方便前端判断</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 DiffDataUtils 差异比较工具，新增 DiffOptions 差异比较选项，自定义包含和排除等设置</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 便捷脚本、Docker脚本优化、Maven配置优化</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 CacheUtils 不存储当前用户信息，防止流程标题生成串用户</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 多线程，Redis 消息监听线程池、用户缓存清理线程池、消息推送线程池，避免高并发情况下太多的线程问题。</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 服务器监控磁盘列表，隐藏一些不必要的盘符</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 访问日志的控制台日志信息输出</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 Cloud网关路由简化配置</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 删除用户没有及时清除 session 问题 pr!22</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 BPM 流程异步事件微服务下不执行问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">升级 Shardingsphere 5.1.1 分库分表框架</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">可视化数据大屏升级 Avue-data v2.3</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">无用户数限制，无在线人数限制</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">后端升级方法</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">修改 <code>pom.xml</code> 文件中的 <code>jeesite-parent</code> 版本号为 <code>5.0.2-SNAPSHOT</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你导入了 <code>jeesite-common</code> 源码项目，请与 <code>git</code> 上的代码进行同步</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你导入了 <code>jeesite-module-core</code> 源码项目，请与 <code>git</code> 上的代码进行同步</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你是跨版本升级，请注意每一个版本的升级方法，业务上有调整的地方进行修改</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Shiro 升级到 1.9.0 shiroFilter 方法 getInstance() 替换为 getObject()</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">执行 <code>root/package.bat(sh)</code> 打包脚本，强制更新依赖即可。</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">了解更多</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite 官网地址：http://jeesite.com</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite 在线文档：http://docs.jeesite.com</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite 演示地址：http://demo.jeesite.com</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite <span>Vue</span> 演示地址：http://vue.jeesite.com</p> <p style="margin-left:0; margin-right:0"> </p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-b6a11e6130872416da8d7df0883fc1ba13a.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            