
---
title: 'Jpom v2.8.7 已经发布，Java 项目在线管理'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3165'
author: 开源中国
comments: false
date: Mon, 24 Jan 2022 14:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3165'
---

<div>   
<div class="content">
                                                                                            <p>Jpom v2.8.7 已经发布，Java 项目在线管理</p> 
<p>此版本更新内容包括：</p> 
<h3>新增功能</h3> 
<ol> 
 <li>【server】新增系统配置-节点白名单、节点系统配置分发功能，方便集群节点统一配置</li> 
 <li>【server】新增构建快捷复制功能,方便快速创建类型一致的项目</li> 
 <li>【server】新增系统配置-配置菜单是否显示,用于非超级管理员页面菜单控制</li> 
 <li>【server】新增节点统计功能，快速了解当前所有节点状态</li> 
 <li>【server】新增节点心跳检测配置<code>system.nodeHeartSecond</code></li> 
 <li>新增缓存管理查看定时任务执行统计</li> 
 <li>【server】新增接触 SSH 终端禁止命令权限（感谢@ooooooam）</li> 
</ol> 
<h3>解决BUG、优化功能</h3> 
<ol> 
 <li>【server】新增全局关闭引导导航配置<code>jpom.disabledGuide</code>（感谢@南有乔木）</li> 
 <li>【server】修复快速安装服务端 ping 检查超时时间 5ms to 5s</li> 
 <li>项目文本文件支持在线实时阅读（感谢@）</li> 
 <li>【server】控制台日志支持搜索高亮</li> 
 <li>【server】跨工作空间更新节点授权将自动同步更新</li> 
 <li>【server】取消节点监控周期字段（采用全局统一配置）</li> 
 <li>【server】监控周期调整为 cron 表达式配置,用户可以自定义监控频率</li> 
 <li>【server】邮箱配置菜单移动到监控管理</li> 
 <li>【server】节点分发白名单配置区分工作空间（不同工作空间不能配置）</li> 
 <li>【server】升级 SpringBoot 版本 2.6.2</li> 
 <li>脚本模版执行目录修改为脚本所在目录</li> 
 <li>【server】SSH 命令模版支持取消默认加载环境变量：<code>#disabled-template-auto-evn</code></li> 
 <li>【server】优化页面分页交互逻辑,只有一页不显示分页条</li> 
 <li>【server】修复删除 SSH 没有删除执行日志</li> 
</ol> 
<blockquote> 
 <p>⚠️ 特别提醒：强烈建议升级该版本,当前版本完善了权限拦截相关问题</p> 
</blockquote> 
<p>详情查看：<a href="https://gitee.com/dromara/Jpom/releases/v2.8.7">https://gitee.com/dromara/Jpom/releases/v2.8.7</a></p>
                                        </div>
                                      
</div>
            