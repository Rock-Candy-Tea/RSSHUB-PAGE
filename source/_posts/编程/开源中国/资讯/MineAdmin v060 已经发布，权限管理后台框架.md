
---
title: 'MineAdmin v0.6.0 已经发布，权限管理后台框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5242'
author: 开源中国
comments: false
date: Wed, 09 Mar 2022 14:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5242'
---

<div>   
<div class="content">
                                                                                            <p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start"><strong>变更</strong></p> 
<ul> 
 <li style="color: rgb(64, 72, 91); margin-left: 0em; margin-right: 0em; text-align: start;">[变更] 全面使用PHP8.0的原生注解特性</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0em; margin-right: 0em; text-align: start;">[变更] 更新SCUI一些新功能</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0em; margin-right: 0em; text-align: start;">[变更] xmo/jwt-auth组件更新版本</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0em; margin-right: 0em; text-align: start;">[变更] 更换定时规则生成器为SCUI版</li> 
</ul> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start"><strong>修复</strong></p> 
<ul> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">[修复] toTree方法漏缺参数</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">[修复] 下载文件时使用操作日志注解报错问题</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">[修复] 生成JWT密钥命令，替换配置值失败 (感谢 smallpure)</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">[修复] 生成代码无表前缀bug</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">[修复] 消息重连bug</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">[修复] 修复缓存注解删除不存在缓存报错问题</li> 
</ul> 
<p style="color:#40485b; margin-left:0px; margin-right:0px; text-align:start"><strong>优化</strong></p> 
<ul> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">[优化] 数据权限算法优化</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">[优化] 多选上传组件multiple增加最大选择数量maxSelect属性 (感谢 zio)</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">[优化] 命令文件命名调整及功能优化</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">[优化] 在某些情况下无法获取用户信息则抛出异常</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">[优化] 上传本地和OSS目录统一</li> 
</ul> 
<p style="color:#40485b; margin-left:0px; margin-right:0px; text-align:start"><strong>增强</strong></p> 
<ul> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">[增强] 登录和操作日志添加IP搜索</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">[增强]<span> </span><code>maTable</code>组件的 beforeQuery 事件增加第二个参数 requestData</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">[增强] 模块配置文件增加启用项</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">[增强] 模块命令增强，支持安装和卸载。</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">[增强] 后台模块管理新增安装、停用功能</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: start;">[增强] user()函数获取角色、岗位方法</li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">提示：更新到<code>0.6.0</code>版本方法</p> 
<ol> 
 <li>更新后端依赖，执行<span> </span><code>composer update</code><span> </span>命令</li> 
 <li>后端执行升级SQL命令：<code>php bin/hyperf.php mine:update</code></li> 
 <li>更新前端依赖，执行<span> </span><code>yarn</code><span> </span>命令</li> 
</ol>
                                        </div>
                                      
</div>
            