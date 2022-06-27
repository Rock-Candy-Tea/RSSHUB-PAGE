
---
title: 'Zinc v0.2.5 发布，轻量级全文索引引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8409'
author: 开源中国
comments: false
date: Mon, 27 Jun 2022 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8409'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Zinc 是一个进行全文索引的搜索引擎，是 Elasticsearch 的轻量级替代品，运行在不到 100 MB 的 RAM 中。它使用 bluge 作为底层索引库。与 elasticsearch 不同，它非常简单且易于操作。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">目前 Zinc v0.2.5 发布了，此版本带来如下改动：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>允许自定义时间戳（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F231" target="_blank">#231</a>）</li> 
 <li><span style="color:#24292f">默认压缩器更改为 ZSTD</span></li> 
 <li>复数字字段上的字符串值（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F227" target="_blank">#227</a>）</li> 
 <li>基于代码推送的完整构建（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F232" target="_blank">#232</a>）</li> 
 <li>改进<span> </span><span style="color:#24292f">swagger</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F220" target="_blank">#220</a>）</li> 
 <li>优化多搜索方法</li> 
 <li>在 UI 中显示分片编号 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F230" target="_blank">#230</a>)</li> 
 <li>为元数据添加更多存储空间 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F207" target="_blank">#207</a>)</li> 
 <li>添加刷新数据 api (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F203" target="_blank">#203</a>)</li> 
 <li>添加版本命令</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F165023d501b6baaa7d8c307bc334ea918c467f3f" target="_blank">165023d</a><span> </span>修复搜索 ui 中的字符</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2Fcd481e60451401ecbb1bb3d976b31a21cacd36da" target="_blank">cd481e6</a><span> </span>修复覆盖</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F635364163d4bdde1211fe552f4af11dbb9fa8bf6" target="_blank">6353641</a><span> </span>修复 UI 中的 docNum</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F64701e155e2ecb9cd618238372db8099b2b88a5c" target="_blank">64701e1</a><span> </span>修复多次搜索时为空目标时的错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2Fcb4e6e516db4f58097d78c31f88f52c209f22397" target="_blank">cb4e6e5</a><span> </span>修复拼写错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F019b8fe832501dbe00071d06d9e7240e5009bdad" target="_blank">019b8fe</a><span> </span> 修复单元测试</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F8425d852450dd8ef718e8b5d39891b368aecbe63" target="_blank">8425d85</a><span> </span>实现多个后端索引（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F202" target="_blank"><span> </span>#202</a>）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F494381ecf38a9a3d4452bc94090f95a20539392a" target="_blank">494381e</a><span> </span>改善应用入口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F87a04330b26e80d8ce905b803c917d8c2a078dc8" target="_blank">87a0433</a><span> </span>提高 es bulk 的兼容性</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F70456a3699b446eef4e89dc0b24fc59b55939403" target="_blank">70456a3</a><span> </span>改进对 es API 的兼容</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2Fec6d123a93a305f197b6283fb9f10d0406cb08c3" target="_blank">ec6d123</a><span> </span>改进了元数据的 etcd</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F4c4812633907c3fd31bea4da72efcec75801b615" target="_blank">4c48126</a><span> </span>改进了数据路径检查的消息</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F7a6fa178b90ac42bcf919ebe3c7080bc89695fa9" target="_blank">7a6fa17</a><span> </span>改进范围查询</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Freleases%2Ftag%2Fv0.2.5" target="_blank">https://github.com/zinclabs/zinc/releases/tag/v0.2.5</a></p>
                                        </div>
                                      
</div>
            