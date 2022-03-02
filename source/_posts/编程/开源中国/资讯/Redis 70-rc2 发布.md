
---
title: 'Redis 7.0-rc2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8905'
author: 开源中国
comments: false
date: Wed, 02 Mar 2022 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8905'
---

<div>   
<div class="content">
                                                                                            <p>Redis 7.0-rc2 现已发布，具体更新内容如下：</p> 
<h4><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新特性</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li>添加 stream 消费者组滞后跟踪和报告 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9127" target="_blank">#9127</a> )</li> 
 <li>为函数和评估 Lua 脚本添加 API 以明确检查 ACL ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10220" target="_blank">#10220</a> )</li> 
</ul> 
<h4><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新的用户命令或命令参数</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li>COMMAND GETKEYSANDFLAGS 子命令 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10237" target="_blank">#10237</a> )</li> 
 <li>INFO 命令可以采用多个部分参数 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F6891" target="_blank">#6891</a> )</li> 
 <li>XGROUP CREATE 和 SETID：新的 ENTRIESREAD 可选参数 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9127" target="_blank">#9127</a> )</li> 
 <li>XSETID 新的 ENTRIESADDED 和 MAXDELETEDID 可选参数 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9127" target="_blank">#9127</a> )</li> 
</ul> 
<h4><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>已扩展的 Command replies</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li>XINFO 报告消费者组滞后和其他一些字段（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9127" target="_blank">#9127</a>）</li> 
 <li>XAUTOCLAIM 返回一个带有删除 ID 列表的新元素 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10227" target="_blank">#10227</a> )</li> 
</ul> 
<h4><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>性能和资源利用改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li>减少客户端回复的系统调用和小数据包 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9934" target="_blank">#9934</a> )</li> 
 <li>减少陈旧客户端的内存使用量 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9822" target="_blank">#9822</a> )</li> 
 <li>修复 Redis 6.2 中引入的 Z[REV]RANGE 命令（按等级）中的回归（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10337" target="_blank">#10337</a>）</li> 
</ul> 
<h4><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li>Modules：修复模块线程添加错误回复时的线程安全违规（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10278" target="_blank">#10278</a>）</li> 
 <li>Lua：修复 Eval scripts active defrag ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10271" target="_blank">#10271</a> )</li> 
 <li>修复地理搜索边界框检查导致丢失结果 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10018" target="_blank">#10018</a> )</li> 
 <li>Lua：在评估 Lua 脚本和函数时添加对 min-slave-* 配置的检查( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10160" target="_blank">#10160</a> )</li> 
 <li>Modules：在具有挂起计时器的模块上使用 MODULE UNLOAD 时防止崩溃和内存泄漏 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10187" target="_blank">#10187</a> )</li> 
 <li>修复被阻止客户端的错误统计信息和失败的命令统计信息 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10309" target="_blank">#10309</a> )</li> 
 <li>Lua/Modules：修复脚本和模块的缺失和重复错误统计信息（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10329" target="_blank">#10329</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10278" target="_blank">#10278</a>）</li> 
 <li>在集群 setslot 期间检查目标节点是否为主节点（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10277" target="_blank">#10277</a>）</li> 
 <li>Sentinel：如果配置保存失败返回错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10151" target="_blank">#10151</a>）</li> 
</ul> 
<p>更多详情可查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Freleases%2Ftag%2F7.0-rc2" target="_blank">release note</a><span style="background-color:#ffffff; color:#333333">。</span></p>
                                        </div>
                                      
</div>
            