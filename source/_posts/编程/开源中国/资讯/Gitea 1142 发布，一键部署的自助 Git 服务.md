
---
title: 'Gitea 1.14.2 发布，一键部署的自助 Git 服务'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4990'
author: 开源中国
comments: false
date: Wed, 12 May 2021 07:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4990'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Gitea 1.14.2 现已发布，该版本修复了一些重要 bug，并合并了 44 个 pr。Gitea 的首要目标是创建一个极易安装，运行非常快速，安装和使用体验良好的自建 Git 服务。项目采用 Go 作为后端语言，只要生成一个可执行程序即可。并且他还支持跨平台，支持 Linux、 macOS 和 Windows 以及各种架构，除了x86、amd64，还包括 ARM 和 PowerPC 。</p> 
<p><strong>部分更新内容</strong></p> 
<ul> 
 <li>API 
  <ul> 
   <li>使更改存储库设置适用于空存储库</li> 
   <li>在 API 中添加拉动 "合并" 的通知主题状态</li> 
  </ul> </li> 
 <li>BUGFIXES 
  <ul> 
   <li>确保 ctx.written 在调用 issues(...) 后被检查</li> 
   <li>除非禁用了拉取，否则在提交图中使用拉取</li> 
   <li>如果没有设置 GIT_DIR，请正确设置它</li> 
   <li>修复存储库未被采用的错误</li> 
   <li>回退以将 IsAnInteractiveSession 用于 SVC</li> 
   <li>修复转储中的版本表设置</li> 
   <li>修复简单区域内删除时关闭按钮的变化</li> 
  </ul> </li> 
 <li>ENHANCEMENTS 
  <ul> 
   <li>显示拉取请求的无冲突合并消息</li> 
   <li>问题列表对齐调整</li> 
   <li>实现删除发布附件和更新发布附件的名称</li> 
   <li>添加占位符文本以部署关键文本区域</li> 
  </ul> </li> 
</ul> 
<p>详细内容请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.gitea.io%2F2021%2F05%2Fgitea-1.14.2-is-released%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            