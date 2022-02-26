
---
title: 'go-fastdfs 分布式文件系统 v1.4.3 发布，增加性能调试选项'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4710'
author: 开源中国
comments: false
date: Fri, 25 Feb 2022 18:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4710'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:start">go-fastdfs 是一个基于 http 协议的分布式文件系统，它基于大道至简的设计理念，一切从简设计，使得它的运维及扩展变得更加简单，它具有高性能、高可靠、无中心、免维护等优点。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>v1.4.3  go-fastdfs 分布式文件系统 v1.4.3 发布，增加性能调试选项</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><br> 注意：使用前请认真阅读 使用文档 或 视频教程。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">优点</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>支持curl命令上传</li> 
 <li>支持浏览器上传</li> 
 <li>支持HTTP下载</li> 
 <li>支持多机自动同步</li> 
 <li>支持断点下载</li> 
 <li>支持https</li> 
 <li>支持配置自动生成</li> 
 <li>支持小文件自动合并(减少inode占用)</li> 
 <li>支持秒传</li> 
 <li>支持一键迁移</li> 
 <li>支持并行体验</li> 
 <li>支持断点续传(tus)</li> 
 <li>支持docker部署</li> 
 <li>支持自监控告警</li> 
 <li>支持集群文件信息查看</li> 
 <li>使用通用HTTP协议</li> 
 <li>无需专用客户端（支持wget,curl等工具）</li> 
 <li>类fastdfs</li> 
 <li>高性能 </li> 
 <li>高可靠</li> 
 <li>无中心设计(所有节点都可以同时读写)</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">更新历史</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li style="text-align:start">v1.4.2 修复下载时&符号被转义，断点续传同一文件无回调</li> 
 <li style="text-align:start">v1.4.1 修复下载时&符号被转义，断点续传同一文件无回调</li> 
 <li style="text-align:start">v1.4.0 修复禁用组同步失败,windows临时文件删除失效</li> 
 <li>v1.3.9 修复禁用组同步失败,windows临时文件删除失效</li> 
 <li>v1.3.8 增加 https 支持,增加 0.0.0.0 IP 白名单放行所有内网</li> 
 <li>v1.3.7 增加上传返回格式 json2，修证生成 google secret 认证 bug</li> 
 <li>v1.3.6 修复并发备份BUG，增加备份队列参数与延迟备份参数</li> 
 <li>v1.3.5支持断点续传自定义认证，路径自定义认证</li> 
 <li>v1.3.4 优化并发上传内存占用</li> 
 <li>v1.3.3 优化集群管理，支持下载域名自定定义协议(http,https)</li> 
 <li>v1.3.2 修正跨域options方法，断点续传无法访问</li> 
 <li>v1.3.1发布，修复同步超时文件异常情况</li> 
 <li>v1.3.0 增加nginx集群配置样例，支持文件类型上传白名单</li> 
 <li>v1.2.9 支持断点续传认证(具体参阅浏览器上传)优化内存占用</li> 
 <li>v1.2.8 增加文件列表接口，优化文件快速迁移功能(实测性能可以跑到机器上限，如：磁盘或网络)</li> 
 <li>v1.2.7 增加nginx配置模版，完善README文档</li> 
 <li>v1.2.6 支持通用文件认证接口</li> 
 <li>v1.2.5 支持图片缩放</li> 
 <li>v1.2.4支持google认证，实现文件安全访问</li> 
 <li>v1.2.3 增加跨域访问支持</li> 
 <li>v1.2.2增加节点只读选项，保证磁盘满的情况下还能迁移集群</li> 
 <li>v1.2.1 优化下载体验，不再重定向，简化nginx配置,可重复文件同步bug修复</li> 
 <li>v1.2.0 增加后台启动脚本，支持后台运行</li> 
 <li>v1.1.9增加文件自动迁移功能，增加文件可重复选项</li> 
 <li>v1.1.8 统一删除接口，优化内存占用，优化文件同步</li> 
 <li>v1.1.7 增加单元测试，为go-fastdfs稳定运行保驾护行</li> 
 <li>v1.1.6 支持web断点续传</li> 
 <li>v1.1.5 支持断点上传功能(tus)</li> 
 <li>v1.1.4 增加docker部署功能</li> 
 <li>v1.1.3增加小文件合并功能</li> 
 <li>v1.1.2 修证同时传输大文件时同步失败问题</li> 
 <li>v1.1.1支持按组（集群）上传文件</li> 
 <li>v1.1.0增加peer_id防止文件被覆盖</li> 
 <li>v1.0.9 重构代码，优化同步逻辑，减少内存占用</li> 
 <li>v1.0.8增加sha1文件去重算法</li> 
 <li>v1.0.7增加动态加载配置功能</li> 
 <li>v1.0.6修改文件同步的方式，由原来的推改为拉，提升大文件同步性能</li> 
 <li>v1.0.5 优化文件统计记录方式</li> 
 <li>v1.0.４ 增加压力测试</li> 
 <li>v1.0.3增加自动修复统计信息</li> 
</ul>
                                        </div>
                                      
</div>
            