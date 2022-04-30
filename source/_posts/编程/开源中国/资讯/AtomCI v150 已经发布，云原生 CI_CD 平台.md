
---
title: 'AtomCI v1.5.0 已经发布，云原生 CI_CD 平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2261'
author: 开源中国
comments: false
date: Fri, 29 Apr 2022 22:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2261'
---

<div>   
<div class="content">
                                                                                            <p>AtomCI v1.5.0 已经发布，云原生 CI/CD 平台</p> 
<p>此版本更新内容包括：</p> 
<h2>What's Changed</h2> 
<h3>功能新增</h3> 
<ul> 
 <li>添加db migrate实现，可以实现轻松升级, Feature db migration by <a href="https://www.oschina.net/sampsonye">@零零一 </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F96" target="_blank">https://github.com/go-atomci/atomci/pull/96</a>, <a href="https://www.oschina.net/colynn">@colynn.liu </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F120" target="_blank">https://github.com/go-atomci/atomci/pull/120</a>, <a href="https://www.oschina.net/sampsonye">@零零一 </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F116" target="_blank">https://github.com/go-atomci/atomci/pull/116</a></li> 
 <li>添加单元测试用例, Issue 90 unit test by <a href="https://www.oschina.net/fanhousanbu">@徐超越 </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F104" target="_blank">https://github.com/go-atomci/atomci/pull/104</a>, <a href="https://www.oschina.net/colynn">@colynn.liu </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F111" target="_blank">https://github.com/go-atomci/atomci/pull/111</a></li> 
 <li>应用纬度调整, 将应用源数据调整为全局唯一 by <a href="https://www.oschina.net/colynn">@colynn.liu </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F94" target="_blank">https://github.com/go-atomci/atomci/pull/94</a> , <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F108" target="_blank">https://github.com/go-atomci/atomci/pull/108</a> , <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F119" target="_blank">https://github.com/go-atomci/atomci/pull/119</a></li> 
 <li>添加gogs代码源的支持， 目前已经支持Gitee/Gitea/GitHub/GitLab/Gogs, add git for Gogs by <a href="https://www.oschina.net/yoyofx">@yoyofx </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F118" target="_blank">https://github.com/go-atomci/atomci/pull/118</a></li> 
 <li>支持使用Token方式访问K8S by <a href="https://www.oschina.net/sampsonye">@零零一 </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F107" target="_blank">https://github.com/go-atomci/atomci/pull/107</a></li> 
</ul> 
<h3>功能优化</h3> 
<ul> 
 <li>添加应用配置模板, Add app.conf.template by <a href="https://www.oschina.net/sampsonye">@零零一 </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F97" target="_blank">https://github.com/go-atomci/atomci/pull/97</a></li> 
 <li>用户授权项目访问后，添加项目成员的显示 Issue #112 by @liuzilong66666 in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F122" target="_blank">https://github.com/go-atomci/atomci/pull/122</a></li> 
 <li>弹窗显示jenkins流水线日志 by <a href="https://www.oschina.net/sampsonye">@零零一 </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F109" target="_blank">https://github.com/go-atomci/atomci/pull/109</a>, <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F110" target="_blank">https://github.com/go-atomci/atomci/pull/110</a></li> 
</ul> 
<h3>BUG修复</h3> 
<ul> 
 <li>Fix: Casbin MySQL adapter import error by <a href="https://www.oschina.net/colynn">@colynn.liu </a> in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F114" target="_blank">https://github.com/go-atomci/atomci/pull/114</a></li> 
 <li>feat: improve migrate init date by</li> 
 <li>解决部分时间不是中国时区的问题 by @liuzilong66666 in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F85" target="_blank">https://github.com/go-atomci/atomci/pull/85</a></li> 
</ul> 
<h2>New Contributors</h2> 
<ul> 
 <li>@liuzilong66666 made their first contribution in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F85" target="_blank">https://github.com/go-atomci/atomci/pull/85</a></li> 
 <li><a href="https://www.oschina.net/yoyofx">@yoyofx </a> made their first contribution in <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fpull%2F118" target="_blank">https://github.com/go-atomci/atomci/pull/118</a></li> 
</ul> 
<p><strong>Full Changelog</strong>: <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgo-atomci%2Fatomci%2Fcompare%2Fv1.4.0...v1.5.0" target="_blank">https://github.com/go-atomci/atomci/compare/v1.4.0...v1.5.0</a></p> 
<p>详情查看：<a href="https://gitee.com/goatom/atomci/releases/v1.5.0">https://gitee.com/goatom/atomci/releases/v1.5.0</a></p>
                                        </div>
                                      
</div>
            