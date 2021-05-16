
---
title: 'sapic（picbed）v1.13 发布，基于 Flask 的 Web 自建图床'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5895'
author: 开源中国
comments: false
date: Sat, 15 May 2021 22:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5895'
---

<div>   
<div class="content">
                                                                    
                                                        <div> 
 <p>功能：</p> 
 <ul> 
  <li>管理员控制台 <code>Ctrl/Command + S</code> 快捷键保存配置</li> 
  <li>关于本站：公开了部分公共信息</li> 
  <li>上传字段用户可由 <code>_upload_field</code> 自行指定。</li> 
  <li>上传视频功能（及周边兼容），api、cli、homepage均支持</li> 
 </ul> 
 <p>优化：</p> 
 <ul> 
  <li>上传大小限制，后端接口实现</li> 
 </ul> 
 <p>更改：</p> 
 <ul> 
  <li>部分picbed字样更改为sapic 
   <ul> 
    <li>更新文档</li> 
    <li>更新hook</li> 
    <li>配置读取环境变量时兼容sapic前缀</li> 
    <li>docker镜像同时上传 staugur/picbed 和 staugur/sapic</li> 
   </ul> </li> 
  <li>cli客户端命令行工具兼容</li> 
 </ul> 
 <p>修复：</p> 
 <ul> 
  <li>尝试性修复 nginx with docker 模式下 local 生成 https url 问题（感谢nestle）</li> 
 </ul> 
</div>
                                        </div>
                                      
</div>
            