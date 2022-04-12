
---
title: 'MineAdmin v0.6.3 发布，权限管理后台框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4346'
author: 开源中国
comments: false
date: Tue, 12 Apr 2022 10:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4346'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">[新增] 每月清理日志定时任务，默认未开启<br> [新增] 队列日志点击行查看队列日志详情</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">[修复] 代码生成器已知bug<br> [修复] 非核心模块存在多个时，启停用混乱bug<br> [修复] 修复setting模块其中几个表迁移文件回滚表名称错误问题</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">[优化] 移除用户登录jwt的token载荷有敏感字段数据<br> [优化] 定时任务表达式生成器兼容PHP<br> [优化] 优化列表更多搜索显示方式，同步已更新到代码生成器<br> [优化] 用户缓存信息减少一次查询<br> [优化] API接口中间件执行逻辑判断问题</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">提示：更新到0.6.3版本方法</p> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">更新后端依赖，执行 composer install 命令<br> 后端执行升级SQL命令：php bin/hyperf.php mine:update</p> 
<p> </p>
                                        </div>
                                      
</div>
            