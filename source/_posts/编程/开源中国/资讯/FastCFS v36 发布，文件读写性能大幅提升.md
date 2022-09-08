
---
title: 'FastCFS v3.6 发布，文件读写性能大幅提升'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6665'
author: 开源中国
comments: false
date: Thu, 08 Sep 2022 09:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6665'
---

<div>   
<div class="content">
                                                                                            <div style="margin-left:0; margin-right:0; text-align:start"> 
 <div>
  <span><span>    历时3星期的研发，FastCFS v3.6发布了，文件读写性能提升明显，尤其顺序写相信会惊艳到大家，感兴趣的朋友可以用 dd或scp等工具体验一下飞一般的感觉。我们租用3台阿里云本地SSD ECS 和 1台普通ECS作为客户端进行压测，2个fio并发线程即可把3gb网络带宽打满（约 351MB/s），而v2.2在4并发线程下只有126MB/s。</span></span>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <div>
  <span><span>  v3.6性能优化主要包括如下两方面：</span></span>
 </div> 
</div> 
<div>
 <span><span> <strong> 1. fstore server优化</strong></span></span>
</div> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <div>
  <span><span>    文件写引入选项write_to_cache，默认为true，表示异步写盘，以充分发挥磁盘写入能力。另外，通过内存池动态分配数据buffer，从网络上接收数据，然后把数据buffer直接传递给磁盘写入线程和数据同步线程，避免内存拷贝。</span></span>
 </div> 
</div> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <div>
  <span><span>    文件读引入配置项read_direct_io，表示是否采用direct io模式，默认不采用（即使用系统缓存）。对于SATA或SAS普通硬盘，建议使用系统缓存；而SSD硬盘可以根据实际需要采用 direct io模式。</span></span>
 </div> 
 <div>
   
 </div> 
</div> 
<div>
 <span><span>  <strong>2. fuse client优化</strong></span></span>
</div> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <div>
  <span><span>    支持fuse选项writeback_cache，告诉Linux kernel是否启用合并写。开启这个选项，将迅猛提升连续写入小块数据（比如一次写入4KB）的性能。</span></span>
 </div> 
</div> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <div>
  <span><span>    fuse.conf增加配置项kernel_cache，表示是否使用Linux kernel的文件缓存。开启这个选项，相当于在fuse客户端启用了文件缓存，在某些情况下将大幅提升文件读取性能。对于多节点共享数据场景，最好不要启用kernel_cache。</span></span>
 </div> 
</div> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <div>
  <span><span>    使用这两个fuse选项，程序内部合理设置fuse相关参数，文件读写性能提升明显。</span></span>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <div>
  <span><span>  v3.6修复的bug列表：</span></span>
 </div> 
</div> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <div>
  <span><span>    [fstore] bugfixed: MUST call set_binlog_indexes to set start_index</span></span>
  <br> 
  <span><span>    [fuseclient] bugfixed: write_to_pid_file move before fcfs_api_start_ex</span></span>
 </div> 
</div> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <div>
  <span><span>    bugfixed: base_path support relative path</span></span>
 </div> 
 <div>
   
 </div> 
</div> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <div>
  <span><span>  FastCFS v3.6的文件读写性能又上了一个台阶，欢迎大家测试和使用。</span></span>
 </div> 
</div>
                                        </div>
                                      
</div>
            