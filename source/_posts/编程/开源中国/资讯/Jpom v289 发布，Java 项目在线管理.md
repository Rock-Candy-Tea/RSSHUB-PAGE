
---
title: 'Jpom v2.8.9 发布，Java 项目在线管理'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9509'
author: 开源中国
comments: false
date: Mon, 14 Feb 2022 12:58:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9509'
---

<div>   
<div class="content">
                                                                                            <p>Jpom v2.8.9 已经发布，Java 项目在线管理。</p> 
<p>此版本更新内容包括：</p> 
<h3>新增功能</h3> 
<ol> 
 <li>【server】容器构建新增 go 环境支持</li> 
 <li>【server】新增查看 docker 容器日志</li> 
 <li>【server】新增在线进入 docker 容器终端</li> 
 <li>【server】构建 ssh 发布支持发布到多个服务器（感谢@<a href="https://gitee.com/laoshirenggo" target="_blank">老诗人</a> ）</li> 
 <li>【server】构建发布方式新增 docker 镜像</li> 
 <li>【server】容器管理新增在线镜像创建容器功能</li> 
 <li>【server】容器管理新增在线拉取镜像功能</li> 
 <li>【server】构建新增是否缓存构建目录</li> 
</ol> 
<h3>解决BUG、优化功能</h3> 
<ol> 
 <li>在线升级新增验证兼容最小版本号</li> 
 <li>【server】支持在线修改数据库账户密码</li> 
 <li>执行脚本文件由 <code>/bin/sh</code> 改为 <code>/bin/bash</code> 兼容 ubuntu</li> 
 <li>【agent】项目 dsl 模式执行脚本变量支持直接引入 $&#123;PROJECT_ID&#125;、同时保留 #&#123;PROJECT_ID&#125; 引用</li> 
 <li>【server】多处日志查看弹窗新增高亮搜索</li> 
 <li>【server】本地构建命令 容器构建支持引用工作空间变量</li> 
 <li>【server】修复构建触发器无法执行（感谢@<a href="https://gitee.com/laoshirenggo" target="_blank">老诗人</a> ）</li> 
 <li>【server】服务端脚本新增工作空间环境变量</li> 
 <li>修复检查 Jpom 包中没有释放资源（感谢@<a href="https://gitee.com/hasape" target="_blank">大海</a> <a href="https://gitee.com/dromara/Jpom/issues/I4T9L0" target="_blank">Gitee issues I4T9L0</a> ）</li> 
</ol> 
<p>详情查看：<a href="https://gitee.com/dromara/Jpom/releases/v2.8.9">https://gitee.com/dromara/Jpom/releases/v2.8.9</a></p>
                                        </div>
                                      
</div>
            