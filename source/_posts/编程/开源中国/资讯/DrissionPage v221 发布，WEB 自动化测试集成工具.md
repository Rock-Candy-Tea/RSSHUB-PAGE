
---
title: 'DrissionPage v2.2.1 发布，WEB 自动化测试集成工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8833'
author: 开源中国
comments: false
date: Tue, 04 Jan 2022 11:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8833'
---

<div>   
<div class="content">
                                                                    
                                                        <p>DrissionPage v2.2.1 已经发布，WEB 自动化测试集成工具。</p> 
<p>此版本更新内容包括：</p> 
<ul> 
 <li>新增基于页面布局的相对定位方法 left()，right()，below()，above()，near()，lefts()，rights()，belows()，aboves()，nears()</li> 
 <li>修改基于 DOM 的相对定位方法：删除 parents()方法，parent 属性改为 parent()方法，next 属性 改为 next() 方法，prev 属性改为 prev() 方法，nexts() 和 prevs() 方法改为返回多个对象</li> 
 <li>增加 after()，before()，afters()，before() 等基于 DOM 的相对定位方法</li> 
 <li>定位语法增加 <a href="https://www.oschina.net/sunhl">@@ </a> 和 @@- 语法，用于同时匹配多个条件和排除条件</li> 
 <li>改进 ShadowRootElement 功能，现在在 shadow-root 下查找元素可用完全版的定位语法。</li> 
 <li>DriverElement 的 after 和 before 属性改为 pseudo_after 和 pseudo_before</li> 
 <li>DriverElement 的 input() 增加 timeout 参数</li> 
 <li>DriverElement 的 clear() 增加 insure_clear 参数</li> 
 <li>优化 DriverElement 的 submit() 方法</li> 
 <li>DriverPage 增加 active_ele 属性，获取焦点所在元素</li> 
 <li>DriverPage 的 get_style_property() 改名为 style()</li> 
 <li>DriverPage 的 hover() 增加偏移量参数</li> 
 <li>DriverPage 的 current_tab_num 改名为 current_tab_index</li> 
 <li>DriverPage 的 to_frame() 方法返回页面对象自己，便于链式操作</li> 
 <li>优化自动下载 driver 逻辑</li> 
 <li>set_paths() 增加 local_port 参数</li> 
 <li>默认使用 9222 端口启动浏览器</li> 
 <li>其它优化和问题修复</li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/g1879/DrissionPage/releases/v2.2.1">https://gitee.com/g1879/DrissionPage/releases/v2.2.1</a></p>
                                        </div>
                                      
</div>
            