
---
title: 'Jpom v2.8.1 发布，Java 项目在线管理'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=454'
author: 开源中国
comments: false
date: Fri, 17 Dec 2021 17:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=454'
---

<div>   
<div class="content">
                                                                                            <p>Jpom v2.8.1 已经发布，Java 项目在线管理</p> 
<p>此版本更新内容包括：</p> 
<h3>新增功能</h3> 
<ol> 
 <li>节点缓存页面新增定时作业列表</li> 
 <li>节点首页新增其他类型进程监控（感谢@大土豆）</li> 
 <li>构建中的项目发布新增差异发布（多文件项目或者网络不佳情况只发布有变化的文件节省项目发布时间）（感谢@大灰灰）</li> 
</ol> 
<h3>解决BUG、优化功能</h3> 
<ol> 
 <li>【server】解决节点未配置监控周期接口报错+页面循环提示（感谢@周健全）</li> 
 <li>Windows 无法关闭 Jpom 程序（感谢@……）</li> 
 <li>【server】修护项目搜索、节点分发项目的文件、控制管理无法正常使用（感谢@刘志远）</li> 
 <li>脚本文件提示内容取消中文，修改为英文</li> 
 <li>【agent】新增检查 jps 命令执行是否存在异常,异常则提示用户（感谢@……）</li> 
 <li>部分控制台输出日志调整为英文</li> 
 <li>【server】优化 ssh 安装插件端,不输入节点ID、没有配置权限报错（感谢@大土豆）</li> 
 <li>【agent】修护项目 <code>JavaExtDirsCp</code> 模式加载非 Jar 文件问题（感谢@大灰灰）</li> 
 <li>升级 SpringBoot 版本 2.6.1</li> 
 <li>【agent】修护项目配置 webhook 后无法关闭进程的情况（感谢@大土豆）</li> 
 <li>【server】ssh 命令日志低版本字段类型文件修护（感谢@大土豆）</li> 
 <li>【server】释放独立分发和删除分发项目提示更明确（感谢@周健全）</li> 
 <li>【server】修护自动导入节点异常（感谢@平安茹意）</li> 
 <li>修护节点密码包含特殊字符时节点控制台等相关功能无法正常使用问题（感谢@魔方技术-李广生）</li> 
</ol> 
<p>详情查看：<a href="https://gitee.com/dromara/Jpom/releases/v2.8.1">https://gitee.com/dromara/Jpom/releases/v2.8.1</a></p>
                                        </div>
                                      
</div>
            