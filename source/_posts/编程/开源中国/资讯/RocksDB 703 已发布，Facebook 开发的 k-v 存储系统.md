
---
title: 'RocksDB 7.0.3 已发布，Facebook 开发的 k-v 存储系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6304'
author: 开源中国
comments: false
date: Tue, 29 Mar 2022 07:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6304'
---

<div>   
<div class="content">
                                                                                            <p>rocksdb-7-0-3-released</p> 
<p><span style="background-color:#ffffff; color:#000000">RocksDB 7.0.3 现已发布，RocksDB 是一个来自 Facebook 的可嵌入的支持持久化的 key-value 存储系统，也可作为 C/S 模式下的存储数据库，基于 LevelDB 构建。更新内容如下：</span></p> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Fpull%2F9590" target="_blank">修复了一个重大的性能错误，由于在 #9590</a> 中对 FilterPolicy::Name() 的更改，早期 7.0.x 版本无法读取 7.0 之前的版本生成的 Bloom 过滤器（反之亦然）。这会严重影响现有数据库升级或降级时的读取性能和读取 I/O，但不会影响数据正确性。</li> 
 <li>修复了<code>Iterator::Refresh()</code>在执行 DeleteRange() 后读取 stale keys 的错误。</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Public API changes</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>添加了纯虚拟 FilterPolicy::CompatibilityName()，这是修复涉及 SST 元数据中 FilterPolicy 命名的主要性能错误所需要的，而不影响 FilterPolicy 的 Customizable 方面。对于源代码来说，这一变化只影响到那些拥有自己的自定义或包装 FilterPolicy 类的用户，但在补丁版本中确实破坏了编译库的二进制兼容性。</li> 
 <li>从 RocksDB 7 开始，RocksJava 现在需要 Java 8（以前是 Java 7）。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Freleases%2Ftag%2Fv7.0.3" target="_blank">https://github.com/facebook/rocksdb/releases/tag/v7.0.3</a></p>
                                        </div>
                                      
</div>
            