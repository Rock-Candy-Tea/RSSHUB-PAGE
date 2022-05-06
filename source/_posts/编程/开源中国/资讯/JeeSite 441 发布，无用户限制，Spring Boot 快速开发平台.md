
---
title: 'JeeSite 4.4.1 发布，无用户限制，Spring Boot 快速开发平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4093'
author: 开源中国
comments: false
date: Fri, 06 May 2022 08:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4093'
---

<div>   
<div class="content">
                                                                                            <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">被封闭的这段时间深感从业不易，为支持小微企业发展，今后发布的所有社区版将全线解除用户数限制。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">愿疫情早日散去，山河无恙，人间皆安。🌞🌞</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">升级内容</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">升级 Spring Boot 2.5.13、Shiro 1.9.0、其它工具等等</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 Spring configuration metadata yml 配置信息友好提示</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 是否启用默认 Servlet 映射（启用后可访问 webapp 下的静态资源访问）</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 支持<span> </span><span style="background-color:#ffffff; color:#002127">Spring Boot</span><span> </span>带减号的 key 写法，自动转换为驼峰格式</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 BPM 查询全部待办、已办流程数据接口</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 OAuth2 state 缓存集群共享</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 CacheUtils exists 方法</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 便捷脚本、Docker脚本优化、Maven配置优化</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 CacheUtils 不存储当前用户信息，防止流程标题生成串用户</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 多线程，Redis 消息监听线程池、用户缓存清理线程池、消息推送线程池，避免高并发情况下太多的线程问题。</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 服务器监控磁盘列表，隐藏一些不必要的盘符</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 访问日志的控制台日志信息输出</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 Cloud网关路由简化配置</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 ie10下用户缓存问题修改头像未刷新</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 sqlserver下流程名称排序错误</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">可视化数据大屏升级 Avue-data v2.3</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">无用户数限制，无在线人数限制</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">升级方法</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">修改 <code>pom.xml</code> 文件中的 <code>jeesite-parent</code> 版本号为 <code>4.4.1-SNAPSHOT</code></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你导入了 <code>jeesite-common</code> 源码项目，请与 <code>git</code> 上的代码进行同步</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你导入了 <code>jeesite-module-core</code> 源码项目，请与 <code>git</code> 上的代码进行同步</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果你是跨版本升级，请注意每一个版本的升级方法，业务上有调整的地方进行修改</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">Shiro 升级到 1.9.0 shiroFilter 方法 getInstance() 替换为 getObject()</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">执行 <code>root/package.bat(sh)</code> 打包脚本，强制更新依赖即可</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">了解更多</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite 官网地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjeesite.com" target="_blank">http://jeesite.com</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite 在线文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.jeesite.com" target="_blank">http://docs.jeesite.com</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.jeesite.com" target="_blank">http://demo.jeesite.com</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite<span> </span><span style="background-color:#ffffff; color:#002127">Vue</span><span> </span>演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fvue.jeesite.com" target="_blank">http://vue.jeesite.com</a></p> </li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            