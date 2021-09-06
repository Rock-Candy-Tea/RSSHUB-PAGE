
---
title: 'Gitea 1.15.2 发布，一键部署的自助 Git 服务'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8605'
author: 开源中国
comments: false
date: Mon, 06 Sep 2021 08:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8605'
---

<div>   
<div class="content">
                                                                                            <p>Gitea 最近在 2 天内连续发布了 1.15.1 和 1.15.2 版本，原因是在 1.15.1 版本中表约束意外自动删除。直接从 1.14.x 升级到 1.15.1 的用户不受影响，从 1.15.0 升级到 1.15.1 的用户可以通过升级到 1.15.2 来解决。</p> 
<p><strong>以下是这两个版本的主要更新内容：</strong></p> 
<ul> 
 <li>将唯一约束添加回 issue_index</li> 
 <li>clean 前关闭存储对象</li> 
 <li>允许 BASIC 身份验证访问 /:owner/:repo/releases/download/*</li> 
 <li>防止因自动填写字段而出现离开更改的对话框</li> 
 <li>修复错误的附件移除</li> 
 <li>Gitlab 迁移器：不忽略上次请求的反应</li> 
 <li>正确返回组织的存储库数量</li> 
 <li>测试 LFS 对象是否可访问</li> 
 <li>修复转储和恢复存储库</li> 
 <li>修复和改进 GetDiffRangeWithWhitespaceBehavior</li> 
 <li>修复 wiki 原始提交差异/补丁视图 </li> 
 <li>确保 wiki 存储库全部关闭</li> 
 <li>如果在 API 上进行身份验证，则列出有限的和私有的组织</li> 
 <li>简化拆分差异视图生成并删除 JS 依赖项</li> 
 <li>确保在用户创建页面上设置了默认可见性</li> 
 <li>将 xorm 升级到 v1.2.2</li> 
 <li>将 primary_key 添加到 issue_index</li> 
 <li>修复分支分页错误</li> 
 <li>将缺失的返回添加到 handleSettingRemoteAddrError</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.gitea.io%2F2021%2F09%2Fgitea-1.15.2-is-released%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            