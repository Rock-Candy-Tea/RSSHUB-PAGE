
---
title: 'OPSLI 1.4.0 发布，低代码快速开发平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3700'
author: 开源中国
comments: false
date: Fri, 04 Jun 2021 08:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3700'
---

<div>   
<div class="content">
                                                                    
                                                        <p>低代码快速开发平台 OPSLI 1.4.0 已经发布，此版本更新内容包括：</p> 
<p>一、重构</p> 
<ol> 
 <li>重构代码生成器</li> 
 <li>重构非对称加密工具类，抽象为非对称插件</li> 
 <li>重构邮件服务</li> 
</ol> 
<hr> 
<p>二、新增</p> 
<ol> 
 <li>新增代码生成器模版</li> 
 <li>新增对称加密插件</li> 
 <li>新增docker和docker-compose部署</li> 
 <li>新增用户密码强度检测</li> 
 <li>新增代码生成器反响生成菜单功能</li> 
 <li>新增SMTP邮件服务在线配置化</li> 
 <li>新增参数配置模块</li> 
 <li>新增登录Token续命模式</li> 
 <li>新增菜单是否总是显示选项</li> 
 <li>新增树状结构工具类</li> 
 <li>新增租户启用接口，一键启用租户</li> 
 <li>新增云存储OSS服务（目前支持又拍云... 持续增加中）</li> 
</ol> 
<hr> 
<p>三、优化</p> 
<ol> 
 <li>前端：响应式UI兼容 手机、Pad、PC端</li> 
 <li>前端：调整主题颜色</li> 
 <li>前端：Dialog 弹出高斯模糊蒙层</li> 
 <li>前端：优化 RSA加解密（支持长字符）</li> 
 <li>前端：优化个人中心相关显示，更改个人中心不受菜单控制</li> 
 <li>后端：优化Redis反序列化容错性</li> 
 <li>后端：优化登录鉴权验证</li> 
 <li>后端：优化 伪穿透过滤器，防止一次直接锁死，给予3次 穿透nil机会</li> 
 <li>后端：优化行锁错误提示</li> 
 <li>后端：规范化菜单路径</li> 
 <li>后端：工具类增加初始化异常，防止在未初始化前使用</li> 
 <li>后端：优化文件上传功能，为后续OSS服务做足准备</li> 
 <li>后端：优化系统健康模块</li> 
 <li>后端：优化菜单模块，菜单可选则上级</li> 
 <li>后端：优化用户/租户逻辑</li> 
 <li>后端：优化多线程锁等待执行器，消除线程死锁操作隐患</li> 
 <li>后端：优化字典类型</li> 
 <li>后端：优化TokenAop拦截器</li> 
 <li>后端：优化系统逻辑结构</li> 
 <li>后端：优化租户修改权限</li> 
 <li>后端：优化条件构造器、分页类</li> 
</ol> 
<hr> 
<p>四、修复</p> 
<ol> 
 <li>前端：修复编辑页面模版取消dialog框，刷新列表BUG</li> 
 <li>前端：修复防抖处理无法正常使用问题</li> 
 <li>前端：修复头像更新异常问题</li> 
 <li>前端：修复Tree控件 及联选择BUG</li> 
 <li>后端：修复参数配置缓存 获得全部 可能数据丢失问题</li> 
 <li>后端：修复手机号更改被清空问题</li> 
 <li>后端：修复ThreadLocal 在Controller可能无法获得Token问题</li> 
</ol> 
<hr> 
<p>官网地址: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.opsli.com" target="_blank">OPSLI 快速开发平台官网</a> 文档地址: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.opsli.bedebug.com%2Fdocs%2Fopsli%2Fopsli-1c83h9o28e1cm" target="_blank">OPSLI 快速开发平台文档</a> 演示环境: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdemo.opsli.bedebug.com" target="_blank">OPSLI 演示环境地址</a></p> 
<p>详情查看：<a href="https://gitee.com/hiparker/opsli-boot/releases/1.4.0">https://gitee.com/hiparker/opsli-boot/releases/1.4.0</a></p>
                                        </div>
                                      
</div>
            