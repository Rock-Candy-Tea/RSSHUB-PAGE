
---
title: 'restfx 0.17.0 发布，适用于 Python 3 的 restful 多应用自动路由框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6899'
author: 开源中国
comments: false
date: Mon, 19 Jul 2021 17:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6899'
---

<div>   
<div class="content">
                                                                    
                                                        <p>restfx 0.17.0 已经发布，适用于 Python 3 的 restful 多应用自动路由框架</p> 
<p>此版本更新内容包括：</p> 
<ul> 
 <li>添加 genid 命令，用于生成或者更新 <code>app_id</code> 的值</li> 
 <li>优化 在启动开发服务器时，检查指定的端口是否被占用</li> 
 <li>优化 在接口页面测试功能上，测试窗口关闭后取消未完成的请求 fix #I3VX6J</li> 
 <li>优化 如果路由相关的包或模块名称是系统保留字，那么抛出异常（修复生成路由文件会无法引入的问题）</li> 
 <li>优化 错误堆栈处理</li> 
 <li>修复 模块名为 globals 与关键字冲突的问题</li> 
 <li>修复 session 存储时，指定的数据库 id 字段过长而导致的潜在问题</li> 
 <li>修复 session 组件继承时的调用顺序错误导致的问题</li> 
 <li>修复 中间件中 <code>on_coming</code> 和 <code>on_leaving</code> 的返回值没有被处理的问题</li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/hyjiacan/restfx/releases/0.17.0">https://gitee.com/hyjiacan/restfx/releases/0.17.0</a></p>
                                        </div>
                                      
</div>
            