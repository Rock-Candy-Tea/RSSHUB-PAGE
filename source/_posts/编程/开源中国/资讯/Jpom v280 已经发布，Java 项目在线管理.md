
---
title: 'Jpom v2.8.0 已经发布，Java 项目在线管理'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=137'
author: 开源中国
comments: false
date: Tue, 14 Dec 2021 16:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=137'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Jpom v2.8.0 已经发布，Java 项目在线管理</p> 
<p>此版本更新内容包括：</p> 
<h3>新增功能</h3> 
<ol> 
 <li>【server】新增工作空间概念（取代角色相关）【系统将自动创建默认工作空间、默认工作空间是不能删除】</li> 
 <li>【server】用户新增可以配置管理员功能【管理员可以管理系统中的账号、系统管理等功能（除升级系统、导入数据外）】</li> 
 <li>【server】新增超级管理员（第一次初始化系统等账号为超级管理员），超级可以拥有整个系统权限不受任何限制</li> 
 <li>【server】列表数据都新增分页、搜索、排序功能（搜索字段、排序字段正在完善补充中）</li> 
 <li>【server】新增通过命令行重置 IP 白名单配置参数 <code>--rest:ip_config</code></li> 
 <li>【server】新增通过命令行重置超级管理员参数 <code>--rest:super_user_pwd</code></li> 
 <li>【server】新增通过命令行重新加载数据库初始化操作参数 <code>--rest:load_init_db</code></li> 
 <li>【server】构建新增<code>本地命令</code>发布方式 用户在服务端执行相关命令进行发布操作</li> 
 <li>【server】发布命令（SSH发布命令、本地命令）支持变量替换：<code>#&#123;BUILD_ID&#125;</code>、<code>#&#123;BUILD_NAME&#125;</code>、<code>#&#123;BUILD_RESULT_FILE&#125;</code>、<code>#&#123;BUILD_NUMBER_ID&#125;</code></li> 
 <li>【server】新增自动备份全量数据配置 <code>db.autoBackupIntervalDay</code> 默认一天备份一次,执行备份时间 凌晨0点或者中午12点</li> 
 <li>【agent】项目的 webhook 新增项目启动成功后通知，并且参数新增 <code>type</code> 指包括：<code>beforeStop</code>,<code>start</code>,<code>stop</code>,<code>beforeRestart</code></li> 
 <li>【agent】项目新增自启动配置项,在 agent 启动时候检查对应项目是否启动，未启动执行启动逻辑 <a href="https://gitee.com/dromara/Jpom/issues/I4IJFK" target="_blank">Gitee issues I4IJFK</a></li> 
 <li>【server】构建新增 webhook，实时通知构建进度</li> 
 <li>【server】节点分发新增分发间隔时间配置</li> 
 <li>新增控制台日志配置数据 <code>consoleLog.charset</code> 避免部分服务器执行命令响应乱码 （感谢@……）</li> 
 <li>【server】构建触发器新增批量触发 <a href="https://gitee.com/dromara/Jpom/issues/I4A37G" target="_blank">Gitee issues I4A37G</a></li> 
 <li>【server】构建支持定时触发 <a href="https://gitee.com/dromara/Jpom/issues/I4FY5C" target="_blank">Gitee issues I4FY5C</a></li> 
</ol> 
<h3>解决BUG、优化功能</h3> 
<ol> 
 <li>【server】用户账号、节点、SSH、监控、节点分发等数据由 JSON 文件转存 h2</li> 
 <li>【server】取消节点、构建分组字段</li> 
 <li>【server】取消角色概念（新增工作空间取代）</li> 
 <li>【server】操作监控数据由于数据字段不兼容将不自动升级需要用户重新配置</li> 
 <li>【server】系统参数相关配置都由 JSON 转存 h2（邮箱配置、IP白名单、节点分发白名单、节点升级）</li> 
 <li>【server】关联节点项目支持绑定单个节点不同项目</li> 
 <li>【server】构建触发器新增跟随创建用户走，历史 url 将失效,需要重新生成</li> 
 <li>【server】仓库<code>假删</code>功能下线，已经删除的仓库将恢复正常（假删功能后续重新开发）</li> 
 <li>【agent】项目数据新增工作空间字段、取消分组字段</li> 
 <li>【server】节点 ID 取消用户自定义采用系统生成</li> 
 <li>【server】优化节点弹窗和菜单折叠页面布局</li> 
 <li>【server】编辑节点、SSH、邮箱配置不回显密码字段</li> 
 <li>【server】优化 SSH 终端不能自动换行问题</li> 
 <li>【agent】脚本模版新增工作空间字段、列表数据并缓存到服务端、新增执行日志</li> 
 <li>【server】优化批量操作项目启动、关闭、重启交互</li> 
 <li>【agent】修护在线升级插件端提示 [Agent-.jar] 已经存在啦,需要手动到服务器去上传新包</li> 
 <li>自动注册对节点需要手动绑定工作空间后,节点才能正常使用 (感谢@ℳ๓₯㎕斌)</li> 
</ol> 
<blockquote> 
 <p>特别感谢：Jpom 社区测试组成员【】、【ʟᴊx】、【hu丶向...】等参与内测的人员</p> 
</blockquote> 
<blockquote> 
 <p>注意：</p> 
 <p>【特别说明】：分组字段将失效，目前所有数据在升级后都将默认跟随<code>默认工作空间</code>。</p> 
 <p>1: 升级该版本会自动将原 JSON 文件数据转存到 h2 中，如果转存成功旧数据文件将自动移动到数据目录中的 <code>backup_old_data</code> 文件夹中</p> 
 <p>2: 升级过程请注意控制台日志是否出现异常</p> 
 <p>3: 操作监控数据由于数据字段不兼容将不自动升级需要用户重新配置</p> 
 <p>4: 监控报警记录、构建记录、操作记录由于字段兼容问题存在部分字段为空的情况</p> 
 <p>5：非超级管理员用户会出现由于未分配工作空间不能正常登录或者不能使用的情况，需要分配工作空间才能登录</p> 
 <p>6: 用户绑定工作空间后，用户在对应工作空间下可以创建、修改、删除对应的数据（包括但不限于管理节点）</p> 
 <p>7: 此次升级启动耗时可能需要2分钟以上（耗时根据数据量来决定），请耐心等待和观察控制台日志输出</p> 
 <p>8: 一个节点建议不要被多个服务端绑定（可能出现数据工作空间错乱情况）</p> 
</blockquote> 
<p>详情查看：<a href="https://gitee.com/dromara/Jpom/releases/v2.8.0">https://gitee.com/dromara/Jpom/releases/v2.8.0</a></p>
                                        </div>
                                      
</div>
            