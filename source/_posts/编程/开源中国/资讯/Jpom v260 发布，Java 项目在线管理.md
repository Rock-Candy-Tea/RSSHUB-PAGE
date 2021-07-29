
---
title: 'Jpom v2.6.0 发布，Java 项目在线管理'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3369'
author: 开源中国
comments: false
date: Wed, 28 Jul 2021 23:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3369'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Jpom v2.6.0 已经发布，Java 项目在线管理。</p> 
<p>此版本更新内容包括：</p> 
<h3>新增功能</h3> 
<ol> 
 <li>【server】新增配置 h2 数据账号密码参数（注意之前已经存在的数据不能直接配置、会出现登录不成功情况）</li> 
 <li>【agent】项目新增配置控制台日志输出目录 （感谢<a href="https://www.oschina.net/lmh_java">@落泪归枫 </a> <a href="https://gitee.com/dromara/Jpom/issues/I22O4N" target="_blank">Gitee I22O4N</a>）</li> 
 <li>【server】新增配置 jwt token 签名 key 参数</li> 
 <li>【server】ssh 新增配置禁止执行的命令,避免执行高风险命令</li> 
 <li>【server】构建发布方式为 ssh 检查发布命令是否包含禁止执行的命令</li> 
 <li>【server】新增 ssh 执行命令初始化环境变量配置 <code>ssh.initEnv</code></li> 
</ol> 
<h3>解决BUG、优化功能</h3> 
<ol> 
 <li>【agent】 修护 nginx 重载判断问题（<a href="https://www.oschina.net/linjianhui">@大灰灰大 </a> 码云 issue <a href="https://gitee.com/dromara/Jpom/issues/I40UE7" target="_blank">I40UE7</a> ）</li> 
 <li>【server】修护 ssh 上传文件时候不会自动创建多级文件夹（@大灰灰大）</li> 
 <li>【server】角色动态权限显示分组</li> 
 <li>【agent】 新增 stop 项目等待进程关闭时间配置 <code>project.stopWaitTime</code>、停止项目输出 kill 执行结果</li> 
 <li>bat 管理命令更新环境变量，避免部分服务器出现无法找到 taskkill 命令（ 感谢@Sunny°晴天、<a href="https://www.oschina.net/zt0330">@zt0330 </a> ）</li> 
 <li>升级SpringBoot、Hutool等 第三方依赖版本</li> 
 <li>去掉旧版本 ui (thymeleaf、layui)</li> 
 <li>【server】fix： ssh 分发执行命令找不到环境变量问题</li> 
 <li>【server】在线升级显示打包时间、并发执行分发 jar 包、部分逻辑优化</li> 
 <li>【server】 构建历史增加下载构建产物按钮（感谢@房东的喵。）</li> 
 <li>【server】项目控制台新增心跳消息，避免超过一定时间后无法操作的情况</li> 
 <li>【server】ssh 新增心跳消息，避免超过一定时间后无法操作的情况</li> 
 <li>【server】系统缓存中的文件占用空间大小调整为定时更新（10分钟）</li> 
 <li>【server】修复 bug：分发列表页面点击【创建分发项目】按钮之后不能正常显示【分发节点】感谢 <a href="https://www.oschina.net/xingenhi">@balloon </a> <a href="https://gitee.com/dromara/Jpom/commit/bd38528fbd3067d220b7569f08449d7796e07c74" target="_blank">点击查看提交记录</a> <a href="https://www.oschina.net/hotstrip">@Hotstrip </a></li> 
 <li>【server】fix: 编辑管理员时用户名不可修改</li> 
 <li>【server】折叠显示部分列表操作按钮（减少误操作）</li> 
</ol> 
<blockquote> 
 <p>注意：当前版本为 beta 版本。项目中升级了较多依赖版本、新增了部分重要配置（建议确认好后再配置）.如果大家在升级后使用中发现任何问题请及时到微信群反馈,我们会尽快协助排查解决</p> 
 <ol> 
  <li>如果是已经安装 Jpom、升级到当前版本请勿直接配置数据库账号密码,如果需要配置请手动连接数据库人工修改密码后再配置</li> 
 </ol> 
</blockquote> 
<p>详情查看：<a href="https://gitee.com/dromara/Jpom/releases/v2.6.0">https://gitee.com/dromara/Jpom/releases/v2.6.0</a></p>
                                        </div>
                                      
</div>
            