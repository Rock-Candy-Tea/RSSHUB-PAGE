
---
title: 'Jpom v2.8.2 已经发布，Java 项目在线管理'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7332'
author: 开源中国
comments: false
date: Fri, 24 Dec 2021 10:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7332'
---

<div>   
<div class="content">
                                                                                            <p>Jpom v2.8.2 已经发布，Java 项目在线管理</p> 
<p>此版本更新内容包括：</p> 
<h3>新增功能</h3> 
<ol> 
 <li>【server】仓库新增导入 Gitee、Github 仓库信息（感谢@ℳ๓₯㎕斌）</li> 
 <li>【server】ssh 新增命令模版、可以用于批量执行命令脚本</li> 
 <li>新增配置属性 <code>system.timerMatchSecond</code> 调度(定时任务)是否开启秒级匹配（感谢@大土豆）</li> 
 <li>缓存管理新增清除旧版本程序包功能</li> 
 <li>【server】用户权限新增绑定工作空间权限（指定工作空间的修改、删除、上传、执行等权限）</li> 
</ol> 
<h3>解决BUG、优化功能</h3> 
<ol> 
 <li>【server】nginx 列表显示不全，无法滚动问题（感谢@）</li> 
 <li>【server】独立节点分发显示节点名称（感谢@奥特曼打猪）</li> 
 <li>【server】用户ID（登录名）支持邮箱格式（感谢@陈力）</li> 
 <li>【server】优化清除构建和删除构建时候删除相关文件操作（使用系统命令快速删除）（感谢@大土豆、<a href="https://gitee.com/dromara/Jpom/pulls/155" target="_blank">Gitee PR</a> ）</li> 
 <li>【server】项目搜索菜单名变更为项目列表</li> 
 <li>【server】调整自动清理日志数据逻辑、默认保留日志数据条数修改为 <code>10000</code></li> 
 <li>【server】脚本模版在服务端统一查看、编辑、执行（感谢@ʟᴊx）</li> 
 <li>【server】ssh 私钥支持配置文件和加载用户目录下的私钥文件</li> 
 <li>【server】初始化超级管理员不能使用 <code>demo</code> 关键词（感谢@A.Nevermore）</li> 
</ol> 
<blockquote> 
 <p>注意：</p> 
 <ol> 
  <li>已经添加的用户重新绑定工作空间权限（默认没有工作空间操作权限）</li> 
 </ol> 
</blockquote> 
<p>详情查看：<a href="https://gitee.com/dromara/Jpom/releases/v2.8.2">https://gitee.com/dromara/Jpom/releases/v2.8.2</a></p>
                                        </div>
                                      
</div>
            