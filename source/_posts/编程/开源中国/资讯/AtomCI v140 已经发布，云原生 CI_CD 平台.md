
---
title: 'AtomCI v1.4.0 已经发布，云原生 CI_CD 平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8989'
author: 开源中国
comments: false
date: Fri, 18 Feb 2022 17:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8989'
---

<div>   
<div class="content">
                                                                                            <p>AtomCI v1.4.0 已经发布，云原生 CI/CD 平台</p> 
<p>此版本更新内容包括：</p> 
<h2>功能新增</h2> 
<ul> 
 <li>支持任何V2版本的Registry作为镜像仓库 by <a href="https://www.oschina.net/sampsonye">@零零一 </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F37" target="_blank">https://github.com/go-atomci/atomci/pull/37</a></li> 
 <li>新增github、gitee、gitea代码仓库支持 by <a href="https://www.oschina.net/fanhousanbu">@徐超越 </a> #70 #71 #83</li> 
 <li>添加支持一键部署脚本 by <a href="https://www.oschina.net/sampsonye">@零零一 </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F45" target="_blank">https://github.com/go-atomci/atomci/pull/45</a></li> 
 <li>新增通知功能（支持邮件、钉钉） by <a href="https://www.oschina.net/fanhousanbu">@徐超越 </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F52" target="_blank">https://github.com/go-atomci/atomci/pull/52</a></li> 
</ul> 
<h2>功能优化</h2> 
<ul> 
 <li>服务集成数据加密存储 <a href="https://www.oschina.net/fanhousanbu">@徐超越 </a> #61</li> 
 <li>权限条目存储调整为mysql adapter by <a href="https://www.oschina.net/fanhousanbu">@徐超越 </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F58" target="_blank">https://github.com/go-atomci/atomci/pull/58</a></li> 
 <li>修改生成K8S secrets逻辑，不依赖于registry名称 by <a href="https://www.oschina.net/sampsonye">@零零一 </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F44" target="_blank">https://github.com/go-atomci/atomci/pull/44</a></li> 
 <li>Feat project layout by <a href="https://www.oschina.net/colynn">@colynn.liu </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F46" target="_blank">https://github.com/go-atomci/atomci/pull/46</a></li> 
 <li>change go-scm to use public repostiry(drone/go-scm), ignore vendor by <a href="https://www.oschina.net/colynn">@colynn.liu </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F64" target="_blank">https://github.com/go-atomci/atomci/pull/64</a></li> 
 <li>build: 将vue的引用方式从cdn转换为本地 by @CraiGZero in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F74" target="_blank">https://github.com/go-atomci/atomci/pull/74</a></li> 
</ul> 
<h2>BUG修复</h2> 
<ul> 
 <li>Fix app YAML parser by <a href="https://www.oschina.net/colynn">@colynn.liu </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F38" target="_blank">https://github.com/go-atomci/atomci/pull/38</a></li> 
 <li>Fix: 修复前端语法错误 <a href="https://www.oschina.net/sampsonye">@零零一 </a> #79 <a href="https://www.oschina.net/colynn">@colynn.liu </a> #81</li> 
 <li>Fix: 腾讯云容器服务连接不上的Bug by <a href="https://www.oschina.net/sampsonye">@零零一 </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F72" target="_blank">https://github.com/go-atomci/atomci/pull/72</a></li> 
</ul> 
<h2>New Contributors</h2> 
<ul> 
 <li><a href="https://www.oschina.net/fanhousanbu">@徐超越 </a> made their first contribution in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F52" target="_blank">https://github.com/go-atomci/atomci/pull/52</a></li> 
 <li>@CraiGZero made their first contribution in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F74" target="_blank">https://github.com/go-atomci/atomci/pull/74</a></li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/goatom/atomci/releases/v1.4.0">https://gitee.com/goatom/atomci/releases/v1.4.0</a></p>
                                        </div>
                                      
</div>
            