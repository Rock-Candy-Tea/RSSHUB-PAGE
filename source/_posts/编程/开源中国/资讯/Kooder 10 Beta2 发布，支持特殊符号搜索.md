
---
title: 'Kooder 1.0 Beta2 发布，支持特殊符号搜索'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5187'
author: 开源中国
comments: false
date: Thu, 22 Apr 2021 14:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5187'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Kooder 1.0 Beta2 发布啦，如果要升级到该版本需要重建索引。</p> 
<p>重建的方式：删除 data/lucene 目录，重新启动 Kooder 即可。</p> 
<p>Kooder 1.0 Beta2 改进内容包括：</p> 
<ol> 
 <li><strong>改进索引的方式，支持特殊符号的检索</strong> <a href="https://gitee.com/oschina/dashboard?issue_id=I3NCP6">#I3NCP6:对带特殊字符的搜索处理不够友好</a></li> 
 <li>修复了源码文件太长导致索引失败的问题 <a href="https://gitee.com/oschina/dashboard?issue_id=I3NIBB">#I3NIBB:UTF8 encoding is longer than the max length 32766</a></li> 
 <li>修复高亮时特殊符号的处理 bug</li> 
 <li><strong>不再处理代码作者信息，可提升代码索引性能 100 倍以上</strong></li> 
 <li>修复 gitea 下的一些小 bug</li> 
</ol> 
<p>其中加粗的改进内容是值得关注的内容。</p> 
<p>Kooder 代码：<a href="https://gitee.com/koode/kooder">https://gitee.com/koode/kooder</a></p>
                                        </div>
                                      
</div>
            