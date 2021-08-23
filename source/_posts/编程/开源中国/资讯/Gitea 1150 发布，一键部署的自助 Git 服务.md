
---
title: 'Gitea 1.15.0 发布，一键部署的自助 Git 服务'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3730'
author: 开源中国
comments: false
date: Mon, 23 Aug 2021 06:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3730'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Gitea 1.15.0 现已发布，该版本合并了 488 个拉取请求。</p> 
<p><strong>部分更新内容</strong></p> 
<ul> 
 <li>BREAKING 
  <ul> 
   <li>升级到最新版本的 golang-jwt，并且 go 升级到 1.15</li> 
   <li>更改了 :latest 在 docker 上的映射</li> 
   <li>更严格的 app.ini 权限，Gitea 创建这个文件时，app.ini 的默认文件权限模式已更改为 -rw-------</li> 
   <li>Webhook 重构。Webhook 有效负载已更改，因此 Secret 字段不再作为有效负载的一部分传递，并且历史记录显示了在 Webhook 中发送的真实 URL</li> 
   <li>添加了非对称 JWT 签名密，Gitea 将默认使用非对称密钥对进行 JWT 签名</li> 
   <li>清理 issue_indexer 队列的设置层次结构</li> 
   <li>将默认队列设置更改为低 go-routines</li> 
   <li>合并资产处理中间件</li> 
   <li>将 StaticUrlPrefix 重命名为 AssetUrlPrefix，具有使用 StaticUrlPrefix 的自定义模板的管理员将需要更新这些模板以使用 AssetUrlPrefi</li> 
   <li>使用标记类来渲染外部标记</li> 
   <li>将节点更新到 v12</li> 
   <li>添加 /assets 作为公共文件的根目录</li> 
   <li>使 Markdown 中的链接绝对指向存储库而不是服务器</li> 
   <li>继承子日志部分的日志级别</li> 
  </ul> </li> 
 <li>SECURITY 
  <ul> 
   <li>使用 SECRET_KEY 加密 db 中的 LDAP 绑定密码</li> 
   <li>删除 Dockerfiles 中的随机密码</li> 
   <li>正确创建 git-daemon-export-ok 文件</li> 
   <li>不在探索视图中显示私人用户的存储库</li> 
   <li>更新节点 tar 依赖到 6.1.6</li> 
  </ul> </li> 
 <li>FEATURES 
  <ul> 
   <li>更新 Go-Git 以利用 LargeObjectThreshold</li> 
   <li>支持文本文件的自定义 mime 类型映射</li> 
   <li>添加 LRU 内存缓存实现</li> 
   <li>本地化电子邮件模板</li> 
   <li>将授权密钥中的命令设为模板</li> 
   <li>添加在分支页面中创建分支的可能性</li> 
   <li>添加电子邮件标题</li> 
   <li>使任务列表复选框可点击</li> 
   <li>在比较页面上添加选择标签</li> 
   <li>添加 cron 作业以从数据库中删除旧操作</li> 
   <li>在打开的存储库上打开通用 cat 文件批处理和批处理检查</li> 
   <li>添加标签保护</li> 
   <li>添加推送到远程镜像仓库</li> 
   <li>为 SVG 文件添加图像差异</li> 
   <li>添加 LFS 迁移和镜像 </li> 
   <li>改进 WIP 草案 PR 的通知 </li> 
   <li>禁用 Stars 配置选项 </li> 
   <li>使用签名令牌进行 GPG 密钥所有权验证</li> 
   <li>OAuth2 自动注册</li> 
  </ul> </li> 
</ul> 
<p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.gitea.io%2F2021%2F08%2Fgitea-1.15.0-is-released%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            