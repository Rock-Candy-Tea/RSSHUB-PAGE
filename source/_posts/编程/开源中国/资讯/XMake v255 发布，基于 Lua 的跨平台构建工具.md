
---
title: 'XMake v2.5.5 发布，基于 Lua 的跨平台构建工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2687'
author: 开源中国
comments: false
date: Thu, 01 Jul 2021 10:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2687'
---

<div>   
<div class="content">
                                                                    
                                                        <p>XMake v2.5.5 已经发布，基于 Lua 的跨平台构建工具。</p> 
<p>此版本更新内容包括：</p> 
<h3>新特性</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1421" target="_blank">#1421</a>: 针对 target 目标，增加目标文件名的前缀，后缀和扩展名设置接口。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1422" target="_blank">#1422</a>: 支持从 vcpkg, conan 中搜索包</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1424" target="_blank">#1424</a>: 设置 binary 作为默认的 target 目标类型</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1140" target="_blank">#1140</a>: 支持安装时候，手动选择从第三包包管理器安装包</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1339" target="_blank">#1339</a>: 改进 <code>xmake package</code> 去产生新的本地包格式，无缝集成 <code>add_requires</code>，并且新增生成远程包支持</li> 
 <li>添加 <code>appletvos</code> 编译平台支持, <code>xmake f -p appletvos</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1437" target="_blank">#1437</a>: 为包添加 headeronly 库类型去忽略 <code>vs_runtime</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1351" target="_blank">#1351</a>: 支持导入导出当前配置</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1454" target="_blank">#1454</a>: 支持下载安装 windows 预编译包</li> 
</ul> 
<h3>改进</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1425" target="_blank">#1425</a>: 改进 tools/meson 去加载 msvc 环境，并且增加一些内置配置。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1442" target="_blank">#1442</a>: 支持从 git url 去下载包资源文件</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1389" target="_blank">#1389</a>: 支持添加工具链环境到 <code>xrepo env</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1453" target="_blank">#1453</a>: 支持 protobuf 规则导出头文件搜索目录</li> 
 <li>新增对 vs2022 的支持</li> 
</ul> 
<h3>Bugs 修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1413" target="_blank">#1413</a>: 修复查找包过程中出现的挂起卡死问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1420" target="_blank">#1420</a>: 修复包检测和配置缓存</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1445" target="_blank">#1445</a>: 修复 WDK 驱动签名错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1465" target="_blank">#1465</a>: 修复缺失的链接目录</li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/tboox/xmake/releases/v2.5.5">https://gitee.com/tboox/xmake/releases/v2.5.5</a></p>
                                        </div>
                                      
</div>
            