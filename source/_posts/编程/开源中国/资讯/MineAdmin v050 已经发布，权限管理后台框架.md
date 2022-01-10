
---
title: 'MineAdmin v0.5.0 已经发布，权限管理后台框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1171'
author: 开源中国
comments: false
date: Mon, 10 Jan 2022 10:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1171'
---

<div>   
<div class="content">
                                                                                            <p>MineAdmin v0.5.0 已经发布，权限管理后台框架</p>
<p>此版本更新内容包括：</p>
<p>[新增] RabbitMQ队列功能（默认未开启，安装<code>rabbitMQ</code>后，请看最下面的开启教程） [新增] 新增队列日志管理 [新增] 新增发布公告和通知功能 [新增] 新增消息功能及消息中心 [新增] websocket消息服务器 [新增] 适配SCUI的资源选择组件 [新增] 新增用户选择器组件 [新增] 表设计器新增id是否生成雪花ID</p> 
<p>[修复] 生成模型判断数据表与模块是否有关系 [修复] value() 方法返回值类型删除 [修复] 某些页面图标不显示问题 [修复] 删除上传目录查询逻辑 [修复] 部分页面因调整<code>request.js</code>返回code造成操作无响应问题 [修复] 修复头像不显示问题，优化上传 [修复] 修复部门列表不显示回收站按钮 [修复] 修复树表代码生成器bug [修复] 修改数据权限的自定义权限bug</p> 
<p>[优化] 前端新增.env环境变量 [优化] Class类型定时任务增加返回结果记录日志里 [优化] 代码生成vue目录名调整 [优化] 定时任务日志排序 [优化] 调用数据权限缺少用户id时，抛出异常 [优化] 代码生成器功能 [优化] 升级到hyperf最新版 [优化] 对部分数据表结构调整 [优化] 滑块验证器视觉上的问题</p> 
<p>老版本升级请按以下操作进行： 1、进入到后端根目录，首先执行 composer install 命令，安装新依赖。 2、在后端根目录执行 php bin/hyperf.php mine:update 命令，执行升级SQL语句 3、若使用队列功能，请在后台.env文件增加以下内容：</p> 
<div class="markdown-code-block"> 
 <pre><code>AMQP_HOST = 127.0.0.1
AMQP_PORT = 5672
AMQP_USER = guest
AMQP_PASSWORD = guest
AMQP_VHOST = /
AMQP_ENABLE = true
</code></pre> 
 <div class="markdown-code-block-copy-btn"></div> 
</div> 
<p>4、开启<code>rabbitMQ</code>的生产和消费进程（请确保已安装rabbitMQ） 打开 <code>App\System\Queue\Consumer\MessageConsumer.php</code> 搜索文件 把 <code>#Consumer</code> 替换成 <code>@Consumer</code></p> 
<p>打开 <code>App\System\Queue\Producer\MessageProducer.php</code> 搜索文件 把 <code>#Producer</code> 替换成 <code>@Producer</code></p>
<p>详情查看：<a href="https://gitee.com/xmo/MineAdmin/releases/v0.5.0" blank="_target">https://gitee.com/xmo/MineAdmin/releases/v0.5.0</a></p>
                                        </div>
                                      
</div>
            