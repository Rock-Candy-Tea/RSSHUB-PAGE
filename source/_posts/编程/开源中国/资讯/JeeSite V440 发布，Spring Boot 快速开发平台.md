
---
title: 'JeeSite V4.4.0 发布，Spring Boot 快速开发平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cb3fd34c0191de84a26a7bee28ace2daca6.png'
author: 开源中国
comments: false
date: Thu, 17 Mar 2022 09:39:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cb3fd34c0191de84a26a7bee28ace2daca6.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="text-align:start">升级内容</h3> 
<ul> 
 <li>升级 spring boot 2.5.10、spring cloud gateway 3.0.7</li> 
 <li>新增 动态数据源配置接口，提供更好的动态数据源操作方法。</li> 
 <li>新增 属性获取Utils，新增 getPropertyToLong 方法。</li> 
 <li>新增 代码生成模板，子表生成的后端验证注解</li> 
 <li>新增 单点登录接口 token 可以设置时效性 shiro.sso.encryptKeyDateFormat</li> 
 <li>优化 登录和未登录的session超时时间分开</li> 
 <li>优化 登录的 deviceType 设备类型，默认 pc</li> 
 <li>优化 新增孤立会话集群模式Quartz清理，减少清理任务执行次数，节省资源</li> 
 <li>优化 微服务情况下可关闭孤立会话清理任务，只需开启core服务即可</li> 
 <li>优化 在线用户游客列表，删除还未来得及清理的已超时会话</li> 
 <li>优化 在线人数统计，增加缓存3分钟的数据，节省服务器资源</li> 
 <li>优化 管理界面默认不关联查询附属部门，根据自行业务修改</li> 
 <li>优化 取消webuploader上传超时参数 #I4WP8B</li> 
 <li>优化 ObjectUtils 反序列化遇到错误时忽略</li> 
 <li>修正 grid 当 autoencode 为 false 的时候，如果 title 未编码</li> 
 <li>修正 流程设计器弹窗时按 Ctrl+V 导致不能关闭对话框问题</li> 
 <li>修正 微服务下 fileUpload.getFileName() 为空的错误忽略</li> 
</ul> 
<h3 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjeesite.com%2Fdocs%2Fupgrade%2F%23%25E5%258D%2587%25E7%25BA%25A7%25E6%2596%25B9%25E6%25B3%2595" target="_blank">#</a>升级方法</h3> 
<ul> 
 <li>修改<span> </span><code>pom.xml</code><span> </span>文件中的<span> </span><code>jeesite-parent</code><span> </span>版本号为<span> </span><code>4.4.0-SNAPSHOT</code></li> 
 <li>如果你导入了<span> </span><code>jeesite-common</code><span> </span>源码项目，请与<span> </span><code>git</code><span> </span>上的代码进行同步</li> 
 <li>如果你导入了<span> </span><code>jeesite-module-core</code><span> </span>源码项目，请与<span> </span><code>git</code><span> </span>上的代码进行同步</li> 
 <li>如果你是跨版本升级，请注意每一个版本的升级方法，业务上有调整的地方进行修改</li> 
 <li>用户管理界面默认不关联查询附属部门，EmpUserDao.xml 根据自行业务修改</li> 
 <li>登录和未登录的session超时时间分开，注意 yml 中的 session 默认设置参数</li> 
 <li>集群环境部署下注意，本版本新增了集群模式的孤立会话清理 yml 里请开启 job</li> 
 <li>动态数据源 RoutingDataSource 接口发生变化，文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjeesite.com%2Fdocs%2Fdao-mybatis%2F%23%25E5%258A%25A8%25E6%2580%2581%25E6%2593%258D%25E4%25BD%259C%25E6%2595%25B0%25E6%258D%25AE%25E6%25BA%2590" target="_blank">https://jeesite.com/docs/dao-mybatis/#动态操作数据源</a></li> 
 <li>执行<span> </span><code>root/package.bat(sh)</code><span> </span>打包脚本，强制更新依赖即可。</li> 
</ul> 
<p><img height="957" src="https://oscimg.oschina.net/oscnet/up-cb3fd34c0191de84a26a7bee28ace2daca6.png" width="1809" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><strong>进一步了解</strong></h3> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>JeeSite 官网地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjeesite.com" target="_blank">http://jeesite.com</a></li> 
 <li>JeeSite 在线文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.jeesite.com" target="_blank">http://docs.jeesite.com</a></li> 
 <li>JeeSite 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.jeesite.com" target="_blank">http://demo.jeesite.com</a></li> 
 <li>JeeSite 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fvue.jeesite.com" target="_blank">http://vue.jeesite.com</a>  (Vue3分离版本)</li> 
 <li>JeeSite 源码下载：<a href="https://gitee.com/thinkgem/jeesite4" target="_blank">https://gitee.com/thinkgem/jeesite4</a></li> 
</ul>
                                        </div>
                                      
</div>
            