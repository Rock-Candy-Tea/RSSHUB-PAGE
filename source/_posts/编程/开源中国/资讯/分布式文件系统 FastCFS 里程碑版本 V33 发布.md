
---
title: '分布式文件系统 FastCFS 里程碑版本 V3.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6777'
author: 开源中国
comments: false
date: Mon, 25 Apr 2022 09:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6777'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span>经过一个半月的紧张研发和测试，</span><span>FastCFS V3.3</span><span>如期发布了。</span><span>V3.3是一个里程碑版本，正常重启和kill -9强杀</span>，系统的稳定性和数据一致性，均得到了充分测试和保障。<span>V3.3主要改进为：</span></p> 
<p><span><span>  1</span>. [fstore] </span><span>修复了服务器重启等情况下的数据一致性问题；</span></p> 
<p><span><span>  2</span>. [fstore] </span><span>单盘数据恢复：单盘故障恢复后，可通过命令行参数恢复数据；</span></p> 
<p><span><span>  3</span>. [fstore] master</span><span>再平衡：机器故障或网络短暂故障恢复后，</span><span>master</span><span>重新均衡分布；</span></p> 
<p><span><span>  </span>4. [fauth & fdir & fstore] </span><span>引入防脑裂机制：</span><span>leader/master</span><span>选举投票采用过半原则。</span></p> 
<p><span>修复的</span><span>bug</span><span>列表如下：</span></p> 
<p><span><span>  </span>1. bugfixed: done_bytes must use atom decrease under multi threads</span></p> 
<p><span><span>  </span>2. bugfixed: DG master election stopped in rare case</span></p> 
<p><span><span>  </span>3. bugfixed: MUST waiting slice write done before trunk reclaim</span></p> 
<p><span><span>  </span>4. bugfixed: should keep delete-slice binlog when ob_index_get_slice_count > 0</span></p> 
<p><span><span>  </span>5. timestamp in the replica and slice binlogs increases monotonically</span></p> 
<p><span><span>  </span>6. bugfixed: should scan last N + 1 seconds binlog when binlog check and repair</span></p> 
<p><span><span>  </span>7. bugfixed: log replica binlog by the fetched binlog</span></p> 
<p>FastCFS V3.3已达到生产环境使用要求，欢迎大家体验和测试，有任何问题欢迎随时反馈。</p>
                                        </div>
                                      
</div>
            