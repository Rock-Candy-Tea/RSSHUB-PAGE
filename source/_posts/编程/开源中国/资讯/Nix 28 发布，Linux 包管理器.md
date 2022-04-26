
---
title: 'Nix 2.8 发布，Linux 包管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=851'
author: 开源中国
comments: false
date: Tue, 26 Apr 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=851'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Nix 是一个操作系统包管理器。同 RPM、APT 和许多其它的软件包管理系统一样，它可以用来控制软件包的安装。Nix 可以用来管理 NixOS 操作系统中包括 Linux 内核在内的所有部分。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Nix 2.8 正式发布，更新内容如下：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>新的实验性命令：<span> </span><code>nix fmt</code>，它将<span> </span><code>formatter.<system></code><span> </span>flake 输出所定义的 formatter 应用于 flake 中的 Nix 表达式。</li> 
 <li>各种 Nix 命令现在可以使用<span> </span><code>-file -</code><span> </span>从标准输入读取表达式。</li> 
 <li>新的实验性内置函数<span> </span><code>builtins.fetchClosure</code><span> </span>可以在评估时从二进制缓存中复制一个闭包，并将其重写为内容地址形式。和<span> </span><code>buildins.storePath</code><span> </span>一样，它允许导入预先建立的存储路径；不同的是，它不要求用户配置二进制缓存和可信的公钥。</li> 
 <li>新的实验性功能：<em>impure derivations</em></li> 
 <li><code>nix store mak-content-addressable</code><span> </span>已被更名为 nix store<span> </span><code>mak-content-addressed</code></li> 
 <li><code>nixosModule</code><span> </span>的 flake 输出属性已被重新命名，与 Nix 2.7 中的<span> </span><code>.default</code><span> </span>重命名一致。 
  <ul style="margin-left:0; margin-right:0"> 
   <li><code>nixosModule</code><span> </span>→<span> </span><code>nixosModules.default</code></li> 
  </ul> </li> 
 <li><code>nix run</code><span> </span>现在对其接受的内容更加严格</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnixos.org%2F" target="_blank">https://nixos.org/</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            