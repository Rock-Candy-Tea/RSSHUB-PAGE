
---
title: 'libzip 1.8.0 发布，读取、创建和修改 zip 压缩包的 C 开发库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3732'
author: 开源中国
comments: false
date: Sun, 20 Jun 2021 23:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3732'
---

<div>   
<div class="content">
                                                                    
                                                        <p>libzip 是一个用于读取、创建和修改 zip 压缩包的 C 开发库。可以从数据缓冲区、文件或直接从其他 zip 压缩包复制的压缩数据中添加文件。可以恢复在未关闭压缩包的情况下所做的更改。</p> 
<p>libzip 1.8.0 正式发布，该版本更新内容如下：</p> 
<ul> 
 <li>增加对 zstd（Zstandard）压缩的支持；</li> 
 <li>增加对 lzma（ID14）压缩的支持；</li> 
 <li>添加 <code>zip_source_window_create()</code>；</li> 
 <li>在 <code>zip_source_zip()</code> 中添加 <code>zip_source_zip_create()</code> 变体；</li> 
 <li>在 <code>zip_set_file_compression()</code> 中允许特定方法 <code>comp_flags</code>；</li> 
 <li>允许在不支持搜索的源上使用 <code>zip_source_tell()</code> 和压缩的数据上使用 <code>zip_ftell()</code>；</li> 
 <li>为一致性检查错误提供更多细节；</li> 
 <li>改进 <code>zipcmp</code> 的输出；</li> 
 <li>在 <code>zipcmp</code> 中，当比较目录列表时，不要忽略空目录；</li> 
 <li>在 <code>zip_file_set_encryption()</code>、 <code>zip_fopen_encrypted()</code> 和 <code>zip_set_default_password()</code> 中，将空字符串视为没有给出密码；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flibzip.org%2Fnews%2F" target="_blank">https://libzip.org/news/</a></p>
                                        </div>
                                      
</div>
            