
---
title: '极简 Windows 包管理器 Baulk 4.0 发布 - 新的里程碑'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/baulk/baulk/raw/master/docs/images/brand.png'
author: 开源中国
comments: false
date: Thu, 31 Mar 2022 10:59:00 GMT
thumbnail: 'https://gitee.com/baulk/baulk/raw/master/docs/images/brand.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">在 Baulk 4.0 中，我们添加了 VFS 机制，改进了包管理器并改进或提供了如下功能</p> 
<ul> 
 <li>更好的<span> </span><strong>VFS</strong><span> </span>设计</li> 
 <li>代码更多的使用 C++20/23 风格编写</li> 
 <li>更好的文件解压体验, 新增<span> </span><code>baulk extract</code><span> </span>命令.</li> 
 <li>对 scoop manifest 的有限兼容 (兼容模式，无法使用 baulk 高级特性，如 Virtual Env 特性)。</li> 
 <li>baulk 有限断点下载支持。</li> 
 <li>集成内存管理器 mimalloc，改进解压缩时的内存分配。</li> 
 <li>添加 baulk brand 命令 (类似 neofetch)</li> 
 <li>添加图形化文件解压命令<span> </span><code>unscrew</code>，进度条基于<span> </span><code>IProgressDialog</code>，支持添加到 Windows 11 菜单。</li> 
 <li>baulk-terminal Windows 11 上下文菜单支持。</li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">注意：由于没有开发者账号，集成 Windows 11 上下文菜单需要用户自己去生成签名并安装。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">unscrew 支持 zip(deflate/bzip/ppmd/zstd/xz/deflate64 ...)/tar/7z 等压缩文件，支持解压自解压安装包，支持平整解压目录，支持文件名编码自动检测，在解压 tar.gz 之类的文件比 7z 更方便的是能够一次性提取，而不用多次解压。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">baulk brand 截图：</p> 
<p><img src="https://gitee.com/baulk/baulk/raw/master/docs/images/brand.png" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p>unscrew 解压文件截图</p> 
<p><img src="https://gitee.com/baulk/baulk/raw/master/docs/images/unscrew.png" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p>unscrew 集成 Windows 11 菜单截图</p> 
<p><img src="https://gitee.com/baulk/baulk/raw/master/docs/images/unscrew-2.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            