
---
title: 'Croc v9.6.0 发布，跨平台 CLI 文件传输工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4764'
author: 开源中国
comments: false
date: Sun, 10 Jul 2022 07:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4764'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Croc 是一种允许任意两台计算机简单安全地传输文件和文件夹的工具。目前已发布 9.5.5 版本，带来如下变更：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fschollz%2Fcroc%2Fcommit%2F0e93f1e285aee2ca54e90485de3a72d164af517c" target="_blank">0e93f1e</a><span> </span>println -> print os.stderr</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fschollz%2Fcroc%2Fcommit%2F7e0814a57ed34a6660540638f573c1a4166feb15" target="_blank">7e0814a</a><span> </span>更新依赖</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fschollz%2Fcroc%2Fcommit%2Fc6bcb79928d17167b0cfe7eb9e0961565c0fd065" target="_blank">c6bcb79</a><span> </span>删除 zip 压缩并添加<span> </span><code>--zip</code><span> </span>发送命令</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fschollz%2Fcroc%2Fcommit%2F134673691e4425ff7fef43c23edb6c60b95b0952" target="_blank">1346736</a><span> </span>合并来自 stefins/zip 文件夹的拉取请求<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fschollz%2Fcroc%2Fpull%2F488" target="_blank">#488</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fschollz%2Fcroc%2Fcommit%2Fd226ba536e14bb81ae9e87991baf8eed93b4018d" target="_blank">d226ba5</a><span> </span>修复了相对路径/ Bug </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fschollz%2Fcroc%2Fcommit%2Fb50fe884745e42215c4b097d39c729f0008705e9" target="_blank">b50fe88</a><span> </span> 增加了对发送文件夹的支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fschollz%2Fcroc%2Fcommit%2F37ae453ff7e535ae0103799e9c043d11b3b29c10" target="_blank">37ae453</a><span> </span>可在接收端解压文件</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fschollz%2Fcroc%2Fcommit%2Fee772c4ceca473dc34c9b65c459dd6972415f50a" target="_blank">ee772c4</a><span> </span>添加了 UnzipDirectory 功能</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fschollz%2Fcroc%2Fcommit%2Fed030375e5ba58ae0e37f7af56bd52248548cf11" target="_blank">ed03037</a><span> </span>修改了测试中 GetFilesInfo 的参数</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fschollz%2Fcroc%2Fcommit%2Fad36e21051035596f0ecf6544e57e6f6095bf373" target="_blank">ad36e21</a><span> </span>处理 --zip 标志</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fschollz%2Fcroc%2Fcommit%2F4ea9a96d884d294d9cc6bc5de4a4d5d9e80e6872" target="_blank">4ea9a96</a><span> </span>添加了用于压缩所有指定目录的 --zip CLI 参数</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fschollz%2Fcroc%2Fcommit%2Ff0f9b80bdfcc167c6d68909a20a28e676dfce6d8" target="_blank">f0f9b80</a><span> </span>添加 ZipDirectory 功能</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fschollz%2Fcroc%2Fcommit%2F7a0c0a820025c0aea766fef342fa01eac33ec8d0" target="_blank">7a0c0a8</a><span> </span>合并来自 tjanez/fedora-package 的拉取请求<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fschollz%2Fcroc%2Fpull%2F474" target="_blank">#474 </a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fschollz%2Fcroc%2Fcommit%2Fa5d3e00f2b997d4c7096c892d48421ddc30f32d8" target="_blank">a5d3e00</a><span> </span>将 Fedora 指令添加到 README</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fschollz%2Fcroc%2Freleases%2Ftag%2Fv9.6.0" target="_blank">https://github.com/schollz/croc/releases/tag/v9.6.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            