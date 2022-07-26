
---
title: 'FastCFS V3.5 发布，支持多数派数据复制'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4544'
author: 开源中国
comments: false
date: Tue, 26 Jul 2022 10:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4544'
---

<div>   
<div class="content">
                                                                                            <p>  经过一个多月紧锣密鼓的研发，FastCFS v3.5发布了。v3.5主要完成了异常情况下保证数据一致性的改进工作：数据提交采用多数派确认机制保证在高负载等不稳定情况下数据一致性和可靠性；实现了数据不一致时的自动恢复机制（以前版本是持续报错），包括如下两点：<br>    1. slave自动回滚不一致的数据，然后从master恢复数据；<br>    2. 在重启情况下，如果slave的数据版本比master高，则自动提升为master。</p> 
<p>  其他小改进：<br>    1. 支持跨机器幂等机制；<br>    2. 默认开启日志按天轮转和日志清除。</p> 
<p>  修复的bug列表：<br>  [fdir]  dentry_list_by_path must call dentry_check_load_children<br>  [fdir & fstore]  select leader/master distinguish success count and active count<br>  [fdir & fstore] get_myself_in_cluster_cfg by service, cluster and replica ports<br>  [fstore] MUST ignore errno EOPNOTSUPP when leader notify</p> 
<p>FastCFS v3.5是极端情况下保证数据一致性和可靠性的里程碑版本，欢迎大家下载和使用。使用FastCFS旧版本的用户，请及时升级到最新版本。</p>
                                        </div>
                                      
</div>
            