
---
title: 'Tengine 2.3.3 即将发布，阿里巴巴开源的轻量级 Web 服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3232'
author: 开源中国
comments: false
date: Thu, 25 Mar 2021 23:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3232'
---

<div>   
<div class="content">
                                                                                            <p>轻量级开源 Web 服务器 Tengine 在 GitHub repo 公布了 2.3.3 的 release note，此版本将新增如下特性：</p> 
<ul> 
 <li> <p>支持 DTLSv1 和 DTLSv1.2.</p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ftengine%2Fblob%2F2.3.3" target="_blank">Prometheus</a> 格式和其他 json 属性已添加至 ngx_http_upstream_check_module 模块</p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ftengine%2Fblob%2F2.3.3" target="_blank">dubbo_pass</a> 指令支持使用变量</p> </li> 
</ul> 
<p>以及其他主要变化：</p> 
<ul> 
 <li>Change：继承了 nginx-1.18.0 所有特性，即 100% 兼容 nginx</li> 
 <li>Change：将钉钉用户组添加至 README.</li> 
 <li>Change：修改 mod_dubbo 的格式文件</li> 
</ul> 
<p>此外还修复了不少 bug：</p> 
<ul> 
 <li>修复 ngx_http_lua_module 模块中的内存泄漏问题</li> 
 <li>修复 ngx_http_upstream_check_module 模块中共享内存出现互斥锁的问题</li> 
 <li>修复当重写字符串包含 ASCII 0 字符时出现内存泄漏的问题</li> 
 <li>修复 ngx_http_upstream_vnswrr_module 模块不支持"dynamic_resolve"指令的问题</li> 
 <li>修复 hex_str 变量在 mod_dubbo 中没有被使用的问题</li> 
 <li>……</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ftengine%2Freleases%2Ftag%2F2.3.3" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            