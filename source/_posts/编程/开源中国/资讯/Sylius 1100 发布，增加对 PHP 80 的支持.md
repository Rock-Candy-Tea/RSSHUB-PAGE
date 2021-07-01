
---
title: 'Sylius 1.10.0 发布，增加对 PHP 8.0 的支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5248'
author: 开源中国
comments: false
date: Thu, 01 Jul 2021 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5248'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Sylius 是一个开源的 PHP 电子商务网站框架，基于 Symfony 和 Doctrine 构建，为用户量身定制解决方案。可管理任意复杂的产品和分类，每个产品可以设置不同的税率，支持多种配送方法，集成 Omnipay 在线支付。</p> 
<p>Sylius 1.10.0 正式发布，该版本更新内容如下：</p> 
<h3>新增</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12333" target="_blank">#12333</a> [API] 删除促销优惠券；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12360" target="_blank">#12360</a> [API] 密码重置；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12391" target="_blank">#12391</a> [API] 重置密码并进行验证；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12382" target="_blank">#12382</a> 通过产品和选项值过滤产品；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12445" target="_blank">#12445</a> [API] 订阅新闻简报；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12368" target="_blank">#12368</a> [API] 账号验证；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12441" target="_blank">#12441</a> [UserBundle] 允许 SSO 的用户密码为空；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12451" target="_blank">#12451</a> [Docs] 新增文档「如何在 Sylius API 中通过选项向购物车添加产品变体？」</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12474" target="_blank">#12474</a> [API] 重新发送验证邮件；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12476" target="_blank">#12476</a> [API] 在账户注册时订阅新闻简报；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12477" target="_blank">#12477</a> [API] 产品评论过滤器；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12472" target="_blank">#12472</a> [Api] 游客和客户添加产品评论；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12498" target="_blank">#12498</a> 在 AddProductReview 命令中把 iri 转换成代码；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12499" target="_blank">#12499</a> [API][Shop] 为添加产品评论添加验证；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12509" target="_blank">#12509</a> [API] 增加管理员和商店部分的解析器；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12552" target="_blank">#12552</a> 增加对 PHP 8.0 的支持；</li> 
 <li>……</li> 
</ul> 
<h3>变化</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12297" target="_blank">#12297</a> 把要求提高到 PHP 7.4；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12304" target="_blank">#12304</a> 更新 PHPStan 配置；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12303" target="_blank">#12303</a> 从 CI 中缓存哈希中删除锁定文件；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12347" target="_blank">#12347</a> 暂时删除路线图链接</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12357" target="_blank">#12357</a> 用 laminas/laminas-stdlib 代替 zendframework/zend-stdlib；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12048" target="_blank">#12048</a> [API] 从 API 实现中明确排除功能；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12393" target="_blank">#12393</a> [ApiBundle] 修复测试应用</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12402" target="_blank">#12402</a> 删除 composer 文件中的重复条目，并在 setup trait 中添加返回类型；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12411" target="_blank">#12411</a> [API] 改进覆盖 api 配置的测试；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12410" target="_blank">#12410</a> [ApiBundle] 改进对测试应用中自定义 Sylius 资源的测试；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12416" target="_blank">#12416</a> [ApiBundle] 改进测试应用程序中自定义实体的测试；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12401" target="_blank">#12401</a> 在 README 中使用粗体字来提醒一些变化</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12384" target="_blank">#12384</a> Doc: 修复 Doctrine 项目的网址；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12419" target="_blank">#12419</a> [API] 添加缺失的规格，并对重置密码 PR 进行修复；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12420" target="_blank">#12420</a> [API] 调整重置密码请求</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12457" target="_blank">#12457</a> 弃用 spooky13/yaml-standards ^5.1，改用^6.0</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12510" target="_blank">#12510</a> 更新到 api 平台 v2.6；</li> 
</ul> 
<h3><strong>修复</strong></h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12398" target="_blank">#12398</a> [API] 添加缺失的规范；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12417" target="_blank">#12417</a> [API][Documentation] 修复指向 jwt 文档的链接；</li> 
 <li>修复 CoreBundle 和 ApiBundle 包的构建；</li> 
 <li>将 elliptic 从 6.5.3 升级到 6.5.4；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12439" target="_blank">#12439</a> 如果已经渲染了 _token 字段，就不要再渲染了；</li> 
 <li>产品选项空值返回400而不是500；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12504" target="_blank">#12504</a> 将 app.php 改为 index.php；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12458" target="_blank">#12458</a> [Locale] 根据要求设置当前的 locale；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12516" target="_blank">#12516</a> 修复 CustomerComponent 的错字；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12699" target="_blank">#12699</a> [Documentation] 更新 Themes doc 中的模板目录；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Fissues%2F12736" target="_blank">#12736</a> 在 GitHub Actions 中强制使用 Symfony 5.2.x；</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSylius%2FSylius%2Freleases%2Ftag%2Fv1.10.0" target="_blank">https://github.com/Sylius/Sylius/releases/tag/v1.10.0</a></p>
                                        </div>
                                      
</div>
            