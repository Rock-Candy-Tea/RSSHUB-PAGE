
---
title: 'Drupal 9.3.0 发布，实验性支持 CKEditor 5'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8078'
author: 开源中国
comments: false
date: Wed, 15 Dec 2021 07:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8078'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.drupal.org%2Fblog%2Fdrupal-9-3-0" target="_blank">Drupal 9.3.0 已发布</a>，这是 Drupal 9 的第三个功能版本，更新内容包括添加对 CKEditor 5 的实验性支持，使 Olivero 主题变稳定，并针对内容编辑器和面向开发者的使用进行了优化。</p> 
<p><strong>Olivero 前端主题已处于稳定阶段</strong></p> 
<p>新的 Olivero 主题于 Drupal 9.1.0 中引入，现在已到达稳定阶段。作为一个现代的主题，Olivero 计划在以后成为新的 Drupal 默认主题（取代 Bartik）。目前尚不支持 Subtheming Olivero，未来可能会加入正式支持。</p> 
<p>主题以 Rachel Olivero (1982-2019) 命名。她是美国盲人联合会组织技术组的负责人，是知名的无障碍专家，是 Drupal 社区的贡献者，也是很多人的朋友。</p> 
<p><strong>对 CKEditor 5 的实验性支持</strong></p> 
<p>Drupal 9.3.0 包含一个新的 beta 实验性 CKEditor 5 模块。CKEditor 5 是一个全新的编辑器，在视觉和架构方面均有所改进。在构建集成的过程中，该团队与 CKSource 一起努力实现对 Drupal 站点至关重要的功能，例如常规 HTML 支持和动态加载 CKEditor 插件的方法，因此基于可视化 Web 的编辑器设置在 Drupal 中仍然可用。此外，开发团队还特意提供了一个流畅的从 CKEditor 4 配置进行升级的路径。</p> 
<p><strong>新的内容编辑角色</strong></p> 
<p>一个新的专门的内容编辑角色被添加到了标准配置文件中，并默认启用内容编辑、媒体管理、翻译、内容工作流和修订处理权限。</p> 
<p><strong>面向开发者的改进</strong></p> 
<p>实体包现在可以声明自己的类，封装所需的业务逻辑。捆绑类必须是基础实体类的一个子类，如 \Drupal\node\Entity\Node。开发者可将每个 bundle 的所有所需逻辑封装到自己的子类中，为制作更清晰、简单、可维护和可测试的代码提供了许多可能性。</p> 
<p>每个用户角色现在都依赖于提供该角色权限的模块，这意味着当一个模块被卸载时，权限会被自动清理掉。</p> 
<p>最后，<a href="https://www.oschina.net/news/170803/php-8-1-0-released">PHP 8.1.0</a> 于 11 月底正式发布，Drupal 9.3.0 已完全支持新版本。安装 Drupal 9.3.0 的推荐 PHP 版本也是 PHP 8，但同时保留了对 PHP 7.3+ 的支持。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.drupal.org%2Fproject%2Fdrupal%2Freleases%2F9.3.0" target="_blank">详情查看 release notes</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            