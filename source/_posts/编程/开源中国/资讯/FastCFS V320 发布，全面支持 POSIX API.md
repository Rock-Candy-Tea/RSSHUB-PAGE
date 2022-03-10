
---
title: 'FastCFS V3.2.0 发布，全面支持 POSIX API'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=834'
author: 开源中国
comments: false
date: Thu, 10 Mar 2022 10:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=834'
---

<div>   
<div class="content">
                                                                    
                                                        <p>经过一个半月的研发和测试，FastCFS V3.2.0和大家见面了。这个版本主要改进：</p> 
<p>  1. 提供诸如 open/fopen、write/fwrite、read/fread、close/fclose、readv、writev 等全套POSIX API，应用程序可以通过这套API使用FastCFS存储；</p> 
<p>  2. 提供了LD_PRELOAD方式，在用户态实现虚拟mount point；</p> 
<p>  3. 为了支持POSIX API，fdir进行了调整和完善，比如 list/remove denry 和 get/list/remove xattr 支持flags；libfastcommon 和 fstore 支持 readv 和 writev；</p> 
<p>  4. fstore支持集群扩容后清除多余的binlog数据（启动 fs_serverd时带上参数 --migrate-clean）。</p> 
<p><strong>其他改进和 bugfix 如下：</strong></p> 
<ul> 
 <li>  [fastcfs-csi] config optimization</li> 
 <li>  [fstore] read ahead support prefetch automatically</li> 
 <li>  [fuseclient] fuse.conf add parameter: xattr_enabled</li> 
 <li>  [fdir] bugfixed: update field "mode" correctly</li> 
 <li>  [fdir] bugfixed: server_parse_inode_for_update MUST set dentry_type</li> 
</ul> 
<p>FastCFS POSIX API及LD_PRELOAD机制参见博客：https://my.oschina.net/u/3334339/blog/5481119</p>
                                        </div>
                                      
</div>
            