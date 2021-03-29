
---
title: 'Chemex v3.0.0-rc 已经发布，现代化风格 ICT 设备资产管理系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3320'
author: 开源中国
comments: false
date: Mon, 29 Mar 2021 10:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3320'
---

<div>   
<div class="content">
                                                                                            <p>Chemex v3.0.0-rc 已经发布，现代化风格 ICT 设备资产管理系统</p>
<p>此版本更新内容包括：</p>
<h3>更新方式</h3> 
<blockquote> 
 <p>仅支持 3.0.0-beta18 升级至 3.0.0-rc ，没有升级到 3.0.0-beta18 的用户请自行下载本仓库内的 3.0.0-beta18 发行版覆盖到程序目录中进行升级。</p> 
</blockquote> 
<p>由于版本特殊，故不能使用在线升级方式，请按照以下操作步骤执行：</p> 
<p>1，执行 <code>git remote remove origin && git remote add origin https://gitee.com/celaraze/chemex.git && git fetch --all && git reset --hard origin/main</code> 。一定要等到执行结束后且没有报错才可以进行之后的操作，不要一股脑的执行，仔细判断是否有报错。</p> 
<p>2，执行 <code>php artisan chemex:db-backup</code> 对数据进行备份。</p> 
<p>3，执行 <code>php artisan chemex:db-reset</code> 重建数据库。</p> 
<p>4，执行 <code>php artisan migrate</code> 重建数据库表。</p> 
<p>5，执行 <code>php artisan chemex:reset</code> 临时初始化管理员帐户。</p> 
<p>6，使用 admin/admin 登陆系统，手动创建之前用到过的自定义字段。</p> 
<p>7，执行 <code>php artisan db:seed</code> 恢复数据。</p> 
<h3>修复</h3> 
<p>资产归属页面搜索错误的问题。</p> 
<p>耗材导出时总数为空的问题。</p> 
<p>配件自定义字段排序失效的问题。</p> 
<p>软件自定义字段排序失效的问题。</p> 
<p>耗材自定义字段排序失效的问题。</p> 
<p>服务自定义字段排序失效的问题。</p> 
<p>自定义字段如果是选项列表无法正确筛选的问题。</p> 
<p>设备履历导出数据不准确的问题。</p> 
<p>删除资产后不会自动删除与之相关的其它信息的问题。</p> 
<p>设备无法通过用户姓名筛选的问题。</p> 
<p>AD可能连接验证失败的问题。</p> 
<p>AD可能登陆失败的问题。</p> 
<h3>优化</h3> 
<p>用户名字段改为工号。</p> 
<p>选择用户从原先的显示姓名，改为显示姓名-工号。</p> 
<p>自定义字段的删除按钮改为行操作。</p> 
<p>echarts静态资源本地化。</p> 
<p>首页仪表盘更新。</p> 
<h3>增强</h3> 
<p>自定义字段支持修改。</p> 
<p>自定义字段支持在资产详情页的排序。</p> 
<p>设备详情页可直接归属、解除归属。</p> 
<p>配件详情页可直接归属、解除归属。</p> 
<p>服务详情页可直接归属、解除归属。</p>
<p>详情查看：<a href="https://gitee.com/celaraze/chemex/releases/v3.0.0-rc" blank="_target">https://gitee.com/celaraze/chemex/releases/v3.0.0-rc</a></p>
                                        </div>
                                      
</div>
            