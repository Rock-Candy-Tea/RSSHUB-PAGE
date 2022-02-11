
---
title: 'ModStartCMS 模块化万能建站系统 v3.2.0 兼容环境检测 自动审核驱动'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-86ca3b9db8f8992ec3d76d26a66f83dd71d.jpg'
author: 开源中国
comments: false
date: Fri, 11 Feb 2022 11:56:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-86ca3b9db8f8992ec3d76d26a66f83dd71d.jpg'
---

<div>   
<div class="content">
                                                                                            <p style="color:#2c3e50; margin-left:.5em; margin-right:0; text-align:left"><code>ModStart</code> 是一个基于 <code>Laravel</code> 模块化极速开发框架。模块市场拥有丰富的功能应用，支持后台一键快速安装，让开发者能快的实现业务功能开发。</p> 
<p style="color:#2c3e50; margin-left:.5em; margin-right:.5em; text-align:left">系统完全开源，基于 Apache 2.0 开源协议，<span>免费且不限制商业使用</span>。<span style="color:#636b6f"> </span></p> 
<p style="color:#2c3e50; margin-left:.5em; margin-right:.5em; text-align:left"><img alt height="385" src="https://oscimg.oschina.net/oscnet/up-86ca3b9db8f8992ec3d76d26a66f83dd71d.jpg" width="536" referrerpolicy="no-referrer"></p> 
<p style="color:#2c3e50; margin-left:.5em; margin-right:.5em; text-align:left"><span style="color:#636b6f">ModStartCMS发布v3.2.0版本，新功能和Bug修复累计22项，兼容环境检测 自动审核驱动。</span></p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">2022年02月11日ModStartCMS发布v3.2.0版本，增加了以下22个特性：</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[新功能] Type 字段增加 CanCascadeFields</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[新功能] 富文本代码美化库 prettyCode.js</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[新功能] 代码格式化风格配置文件</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[新功能] 模块安装兼容环境检测（目前 laravel5 和 laravel9 ）</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[新功能] 平台操作系统检测工具包</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[新功能] 图片审核和文字审核驱动</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[新功能] Job 中新增静态文件路径补全方法</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[新功能] Grid 筛选默认值（文本、下拉、单选）</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[新功能] 可升级模块筛选，显示系统可升级的模块</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[新功能] 本地模块筛选Tab，只显示本地模块</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[新功能] 用户VIP为空时，默认初始化VIP等级</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[新功能] 用户VIP增加图标</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[新功能] 用户首页显示VIP数据信息</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[新功能] Banner批量删除功能</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[新功能] 二级导航功能</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[新功能] 导航批量删除功能</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[新功能] 导航位置Tab切换</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[系统优化] 列表操作文字样式优化</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[系统优化] 内容审核后台概况新增待审核列表</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[系统优化] 事件触发兼容不同 Laravel 版本</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[系统优化] 后台自动升级Token存储优化</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left">·[系统优化] 移除部分依赖，系统部署更轻便</p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left"> </p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left"><strong>前台演示：</strong></p> 
<p style="color:#2c3e50; margin-left:.5em; margin-right:.5em; text-align:left"><span style="color:#6867f6"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fcms.demo.tecmz.com%2F" target="_blank">http://cms.demo.tecmz.com/</a></span></p> 
<p style="color:#2c3e50; margin-left:.5em; margin-right:.5em; text-align:left"><strong><span style="background-color:#ffffff; color:#2c3e50"><strong>后台演示：</strong></span></strong></p> 
<p style="color:#2c3e50; margin-left:.5em; margin-right:.5em; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fcms.demo.tecmz.com%2Fadmin" target="_blank">http://cms.demo.tecmz.com/admin</a></p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left"><strong>下载试用：</strong></p> 
<p style="color:#636b6f; margin-left:.5em; margin-right:.5em; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmodstart.com%2Fdownload" target="_blank">https://modstart.com/download</a></p>
                                        </div>
                                      
</div>
            