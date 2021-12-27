
---
title: 'Apache IoTDB 0.12.4 发布，物联网时序数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3233'
author: 开源中国
comments: false
date: Mon, 27 Dec 2021 07:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3233'
---

<div>   
<div class="content">
                                                                                            <p>Apache IoTDB 0.12.4 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202112.mbox%2F%253CCAJ0E_HTBE6OZ1%3D%2BBmq%3DVQYvBsZNv7CKHW_MywBRYdfCeKBv5Qg%40mail.gmail.com%253E" target="_blank">已发布</a>，Apache IoTDB 是一个物联网原生数据库，具有高性能的数据管理和分析功能，可部署在边缘和云端。</p> 
<p>0.12.4 是错误修复版本，更新内容包括改进和引入新功能。</p> 
<p><strong>新特性</strong></p> 
<ul> 
 <li>[IOTDB-1823] 支持多级分组</li> 
</ul> 
<p><strong>改进</strong></p> 
<ul> 
 <li>[IOTDB-2027] WAL 写入失败后回滚无效条目</li> 
 <li>[IOTDB-2061] 添加最大并发子查询参数，分批读取数据以限制最大 IO，并增加最大缓存缓冲区大小配置</li> 
 <li>[IOTDB-2065] 当不再使用 TsFileSequenceReader 时，尽快释放它</li> 
 <li>[IOTDB-2072] 删除 TVListAllocator 以降低 TVList 内存成本</li> 
 <li>[IOTDB-2101] 减少 QueryDataSource 的内存占用</li> 
 <li>[IOTDB-2102] 将限制运算符推送到每个读取器上</li> 
 <li>[IOTDB-2123] 加快 recovery process 更新 cpp-cpi 的用户指南，并在 cpp-cli 中禁用编译 nodejs，以及忽略过多的 WAL BufferOverflow 日志</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fraw.githubusercontent.com%2Fapache%2Fiotdb%2Fv0.12.4%2FRELEASE_NOTES.md" target="_blank">详情查看 release note</a>。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fiotdb.apache.org%2FDownload" target="_blank">http://iotdb.apache.org/Download</a></p>
                                        </div>
                                      
</div>
            