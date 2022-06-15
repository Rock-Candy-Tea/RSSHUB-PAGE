
---
title: 'FastCFS V3.4 发布，支持双活互备防脑裂'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6976'
author: 开源中国
comments: false
date: Wed, 15 Jun 2022 09:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6976'
---

<div>   
<div class="content">
                                                                    
                                                        <p>历经一个半月的紧张研发和测试，FastCFS V3.4发布了。V3.4主要改进：</p> 
<p><span>  </span>1. 引入选举节点，双副本防脑裂（即双活互备防脑裂，保证数据一致性）；</p> 
<p><span>  </span>2. fdir和fstore的binlog去重及历史数据清理，减少不必要的磁盘空间占用；</p> 
<p><span>  </span>3. fdir实现的文件锁严格遵循POSIX规范：</p> 
<p><span>    </span>1) 允许重入（同一进程内多次重复加锁）；</p> 
<p><span>    </span>2) UNLOCK均返回成功；</p> 
<p><span>    </span>3) 一次UNLOCK可以解开多个锁；</p> 
<p><span>    </span>4) UNLOCK支持部分解锁。</p> 
<p><span>  </span>4. 去掉不必要的错误日志，网络连接失败日志中增加服务名称，方便定位问题。</p> 
<p> </p> 
<p>v3.4修复的bug如下：</p> 
<p><span>[fdir] bugfixed: must check load children for list dentry when storage engine is enabled</span></p> 
<p><span>[fdir] bugfixed: CAS set data version correctly</span></p> 
<p><span>[fdir] bugfixed: MUST change replication ptr array in the cluster thread</span></p> 
<p><span>[fauth] bugfixed: padding with the terminating '\0' character for strtoll</span></p> 
<p><span>[fstore] bugfixed: send active test when (task->offset == 0 && task->length == 0)</span></p> 
<p>V3.4版本中fdir的稳定性得到了增强，欢迎大家安装和使用V3.4版本，使用过程中有任何问题或建议，欢迎提交issue或加入微信群交流。</p>
                                        </div>
                                      
</div>
            